from ultralytics import YOLO
import cv2

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Single stream with batch-size 1 inference
source = "rtsp://admin:hik12345@10.25.18.235/Streaming/Channels/2"  # RTSP, RTMP, TCP, or IP streaming address

# Run inference on the source
results = model(source, stream=True)  # generator of Results objects

for result in results:
    # Extract the image with detections
    img_with_detections = result.plot()  # this adds bounding boxes and labels

    # Display the image with OpenCV
    cv2.imshow("YOLO Inference", img_with_detections)

    # Wait for a key press to continue or exit
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release resources
cv2.destroyAllWindows()
