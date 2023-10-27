import cv2 as cv

# Initialize the camera or video capture (0 for the default camera)
cap = cv.VideoCapture(0)

# Create an initial frame for reference
ret, frame1 = cap.read()
gray1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

while True:
    ret, frame2 = cap.read()
    if not ret:
        break  # Break the loop when the video ends or an error occurs

    # Convert the current frame to grayscale
    gray2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

    # Compute the absolute difference between the two frames
    frame_diff = cv.absdiff(gray1, gray2)

    # Apply a threshold to the difference frame
    _, thresh = cv.threshold(frame_diff, 30, 255, cv.THRESH_BINARY)

    # Find contours in the thresholded frame
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around moving objects
    for contour in contours:
        if cv.contourArea(contour) > 200:  # Adjust the area threshold as needed
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Create a copy of the original image to draw contours on
    contour_image = thresh.copy()

    # Draw the contours on the copy of the image
    cv.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # -1 indicates to draw all detected contours

    # Display the frame with motion detection
    cv.imshow('Motion Detection', frame2)
    cv.imshow("frame1", frame1)
    cv.imshow('frame difference', frame_diff)
    cv.imshow('contours image', contour_image)

    # Update the previous frame
    gray1 = gray2.copy()

    # Exit the loop when the 'q' key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
