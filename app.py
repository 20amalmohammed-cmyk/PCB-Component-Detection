import os
import cv2
import numpy as np
from flask import Flask, request, render_template, jsonify
from ultralytics import YOLO
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Debug information
print("=" * 50)
print("🚀 Starting PCB Component Detection Server")
print("=" * 50)
print(f"📁 Current directory: {os.getcwd()}")
print(f"📁 Templates folder: {os.path.join(os.getcwd(), 'templates')}")
print(f"✅ Templates exists: {os.path.exists('templates')}")
print(f"✅ Index.html exists: {os.path.exists('templates/index.html')}")
print(f"✅ Static folder exists: {os.path.exists('static')}")
print(f"✅ Uploads folder exists: {os.path.exists('static/uploads')}")
print(f"✅ Results folder exists: {os.path.exists('static/results')}")
print("=" * 50)

# Load your trained model
model_path = 'model/bcp_detector.pt'

try:
    model = YOLO(model_path)
    print("✅ Model loaded successfully!")
    print(f"✅ Model classes: {model.names}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = YOLO('yolov8n.pt')
    print("⚠️  Using fallback model for testing")

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
RESULTS_FOLDER = 'static/results'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULTS_FOLDER'] = RESULTS_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"""
        <h1>PCB Component Detection</h1>
        <div style="color: red; padding: 20px; border: 2px solid red;">
            <h2>Template Error</h2>
            <p><strong>Error:</strong> {e}</p>
            <p><strong>Current directory:</strong> {os.getcwd()}</p>
            <p><strong>Templates folder exists:</strong> {os.path.exists('templates')}</p>
            <p><strong>Index.html exists:</strong> {os.path.exists('templates/index.html')}</p>
            <p>Please make sure you have a 'templates' folder with 'index.html' inside it.</p>
        </div>
        """

@app.route('/detect', methods=['POST'])
def detect_components():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        try:
            # Save uploaded file
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            print(f"📸 Image saved: {upload_path}")
            
            # Perform detection
            print("🔍 Running detection...")
            results = model(upload_path)
            
            # Process results
            result_filename = f"result_{filename}"
            result_path = os.path.join(app.config['RESULTS_FOLDER'], result_filename)
            
            # Save annotated image
            annotated_img = results[0].plot()
            cv2.imwrite(result_path, annotated_img)
            print(f"💾 Result saved: {result_path}")
            
            # Extract detection information
            detections = []
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        detection = {
                            'class': model.names[int(box.cls)],
                            'confidence': float(box.conf),
                            'bbox': box.xyxy[0].tolist()
                        }
                        detections.append(detection)
            
            print(f"✅ Detection complete: {len(detections)} components found")
            
            return jsonify({
                'success': True,
                'original_image': f'/static/uploads/{filename}',
                'result_image': f'/static/results/{result_filename}',
                'detections': detections,
                'count': len(detections)
            })
            
        except Exception as e:
            print(f"❌ Detection error: {e}")
            return jsonify({'error': f'Detection failed: {str(e)}'}), 500
    
    return jsonify({'error': 'Invalid file type. Please upload: PNG, JPG, JPEG, GIF, BMP'}), 400

@app.route('/test')
def test_page():
    """Test page to verify the server is working"""
    return """
    <h1>PCB Detection Server - Test Page</h1>
    <p>✅ Server is running correctly!</p>
    <p><a href="/">Go to Main Page</a></p>
    <p><strong>Debug Info:</strong></p>
    <ul>
        <li>Templates folder exists: {}</li>
        <li>Index.html exists: {}</li>
        <li>Static folder exists: {}</li>
        <li>Model loaded: {}</li>
    </ul>
    """.format(
        os.path.exists('templates'),
        os.path.exists('templates/index.html'),
        os.path.exists('static'),
        'best.pt' in str(model)
    )

if __name__ == '__main__':
    print("🎯 Server starting on http://127.0.0.1:5000")
    print("📝 Visit http://127.0.0.1:5000/test to check if everything is working")
    app.run(host='0.0.0.0', port=5000, debug=True)