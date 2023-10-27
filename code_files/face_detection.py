import cv2 as cv

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open a video capture stream (0 for the default camera, or provide a video file path)
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle

    # Display the frame with detected faces
    cv.imshow('Object Detection', frame)

    # Exit the loop when the 'q' key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
