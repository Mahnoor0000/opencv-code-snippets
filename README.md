# OpenCV Project
This repository contains various OpenCV-related Python scripts demonstrating different computer vision tasks.
## Features
- Face Detection
- Motion Detection
- Geometric Shape Detection
- Image Thresholding
## Setup
To set up the project, clone the repository and install the dependencies:
`git clone https://github.com/username/opencv-project.git`
`cd opencv-project`
`pip install -r requirements.txt`
## Example: Motion Detection Script
```python
import cv2

# Load video
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect motion (example)
    # (your motion detection logic goes here)

    # Display the result
    cv2.imshow('Motion Detection', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
