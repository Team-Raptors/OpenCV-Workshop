import cv2 as cv

# Open the video file for reading
cap = cv.VideoCapture('your_video.mp4')

while True:
    ret, frame = cap.read()  # Read a frame from the video
    if not ret:
        break  # Break the loop if we reach the end of the video
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break  # Press 'q' to exit the video

cap.release()  # Release the video capture object
cv.destroyAllWindows()  # Close OpenCV windows
