import cv2 as cv

# Open the default webcam (usually 0 or 1)
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    cv.imshow('Webcam', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break  # Press 'q' to exit the webcam feed

cap.release()  # Release the webcam capture object
cv.destroyAllWindows()  # Close OpenCV windows
