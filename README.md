# CodeAlpha_ObjectDetection

A real time object detection and tracking application built with Python, OpenCV and YOLOv11 that detects and tracks multiple objects through a webcam feed.

## Features

- Real time object detection using YOLOv11
- Object tracking with unique tracking IDs
- Supports detection of 80 different object classes
- Bounding boxes with labels drawn on each frame
- Webcam support
- Press Q to quit the application

## Technologies Used

- Python 3.x
- OpenCV
- Ultralytics YOLOv11

## Installation

1. Clone the repository
git clone https://github.com/yourusername/CodeAlpha_ObjectDetection.git

2. Navigate to project directory
cd CodeAlpha_ObjectDetection

3. Install required libraries
pip install opencv-python ultralytics

## Usage

Run the application using the following command:
python app.py

The webcam will open automatically and start detecting objects in real time.
Press Q to quit the application.

## Detectable Objects

YOLOv11 can detect 80 different objects including:

- Person
- Car
- Motorcycle
- Bus
- Truck
- Laptop
- Phone
- Chair
- Bottle
- And many more

## How It Works

1. Webcam captures video frames in real time
2. Each frame is passed to YOLOv11 model
3. Model detects objects and assigns tracking IDs
4. Bounding boxes and labels are drawn on each frame
5. Processed frame is displayed in a window
