# PCB Component Detection

A comprehensive computer vision system for detecting and classifying electronic components on Printed Circuit Boards (PCBs) using YOLO transfer learning.

## Features
- Web-based interface for easy component detection
- YOLO transfer learning for accurate component recognition
- Real-time detection results
- Support for 20+ electronic components

## Detectable Components
The system can detect the following  electronic components:

**Resistor** - **Capacitor** - **IC** - **Potentiometer** - **Transducer** - **Transistor** - **Diode** - **Connector** - **Fuse** - **Pads** - **Led** - **Pins** - **Inductor** - **Relay** - **Transformer** - **Battery** - **Button** - **Buzzer** - **Switch** - **Clock** - **Display**

## Quick Start

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Download the trained Model
Download the trained model (250MB) from:
[https://www.dropbox.com/scl/fi/dg0bs6bqnjqpd5cu5g2a4/bcp_detector.pt?rlkey=vqw8k5gmlwgfxw3b7adtlkn3h&st=c8pwi9d4&dl=0](https://www.dropbox.com/scl/fi/dg0bs6bqnjqpd5cu5g2a4/bcp_detector.pt?rlkey=vqw8k5gmlwgfxw3b7adtlkn3h&st=c8pwi9d4&dl=0)

Create the model folder and place the downloaded file:
```bash
mkdir model
# Move bcp_detector.pt to model/ folder
```

### 3. Run the Application
```bash
python app.py
```

Open your browser and navigate to: `http://localhost:5000`

## Dataset Download
For training your own model, download the PCB component detection dataset from:
[https://www.kaggle.com/datasets/aryanstein/pcb-component-detection-consolidated-dataset](https://www.kaggle.com/datasets/aryanstein/pcb-component-detection-consolidated-dataset)

## Training Your Model

### 1. Prepare Dataset
- Download and extract the dataset


### 2. Run Training
Open and execute the training notebook:
```bash
jupyter notebook main.ipynb
```

### 3. Training Process
The notebook will guide you through:
- Data preprocessing and augmentation
- Model configuration and transfer learning
- Training execution and monitoring
- Model evaluation and export

### 4. Use Custom Model
After training, replace `model/bcp_detector.pt` with your trained model and restart the application.

## Project Structure
```
├── model/                 # Trained models
├── static/               # Web app static files
├── templates/            # HTML templates
├── uploads/              # User uploaded images
├── app.py               # Flask web application
├── main.ipynb           # Training notebook
├── requirements.txt     # Dependencies
└── README.md           # Documentation
```

## Usage
1. Start the application with `python app.py`
2. Open `http://localhost:5000` in your browser
3. Upload a PCB image
4. View detection results with bounding boxes and labels

## Support
For issues or questions:
- Check that all dependencies are installed
- Ensure the model file is in the correct location
- Verify the dataset format when training

## Notes
- The application uses Flask for the web interface
- YOLOv8 is used for object detection
- Pre-trained model provides immediate detection capability
- Custom training allows for model fine-tuning on specific datasets
