
# PCB Component Detection

A comprehensive computer vision system for detecting and classifying electronic components on Printed Circuit Boards (PCBs) using YOLO transfer learning.

## Features
-  Web-based interface for easy component detection
-  YOLO transfer learning for accurate component recognition
-  Real-time detection results
-  Support for 20+ electronic components


## Detectable Components
The system can detect the following 20 electronic components:

# Component  

 **Resistor** - **Capacitor** - **IC**- **Potentiometer**- **Transducer** -**Transistor** - **Diode** - **Connector** - **Fuse** -
 **Pads** - **Led** - **Pins** - **Inductor**- **Relay** - **Transformer**- **Battery** - **Button** - **Buzzer** - **Switch** - **Clock** -
**Display** 

## Dataset Download
Download the PCB component detection dataset from:
[https://www.kaggle.com/datasets/aryanstein/pcb-component-detection-consolidated-dataset](https://www.kaggle.com/datasets/aryanstein/pcb-component-detection-consolidated-dataset)

## Model Download
Download the trained model (250MB) from: https://www.dropbox.com/scl/fi/dg0bs6bqnjqpd5cu5g2a4/bcp_detector.pt?rlkey=vqw8k5gmlwgfxw3b7adtlkn3h&st=c8pwi9d4&dl=0.
Place the model file in the `model/` folder after download.

## Installation
```bash
pip install -r requirements.txt
