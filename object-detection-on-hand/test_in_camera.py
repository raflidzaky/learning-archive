import cv2
from ultralytics import YOLO

# Load the trained model
model = YOLO('HOME-PATH\\yolov8s.pt')

# Open the video file
cap = cv2.VideoCapture('LOCAL-VIDEO-FILE')

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Width of the frames
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Height of the frames

# Set up the output video
output_video = cv2.VideoWriter(
    'C:\\Users\\Rafli\\cat-detection-project\\output_video.mp4', 
    cv2.VideoWriter_fourcc(*'mp4v'),  # Codec for mp4 files
    fps, 
    (width, height)
)

# Process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Stop if no frame is returned (end of video)

    # Perform inference on the current frame
    results = model(frame)

    # Render the bounding boxes on the frame (this draws on the frame)
    frame = results[0].plot()  # This will overlay bounding boxes on the frame

    # Write the processed frame to the output video
    output_video.write(frame)

# Release the video objects
cap.release()
output_video.release()

# Close any OpenCV windows
cv2.destroyAllWindows()

print("Video processed and saved!")

