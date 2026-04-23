import cv2
from ultralytics import YOLO

# Load YOLO Model
model = YOLO("yolo11n.pt")

# Open Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not found!")
    exit()

print("Object Detection Started. Press Q to quit.")

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame!")
        break

    # Run YOLO detection and tracking
    results = model.track(frame, persist=True)

    # Draw results on frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Detection stopped.")