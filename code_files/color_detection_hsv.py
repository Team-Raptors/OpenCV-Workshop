import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
# cap = cv.VideoCapture("Images\colors.mp4")

# Convert the image to the HSV color qspace
while True:
    success, image = cap.read()
    print(success)

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the color you want to detect (in HSV format)
    lower_color = np.array([0, 100, 100])  # Lower bound for green
    upper_color = np.array([10, 255, 255])  # Upper bound for green

    # Create a mask to extract the specified color
    mask = cv.inRange(hsv, lower_color, upper_color)

    # Apply the mask to the original image
    result = cv.bitwise_and(image, image, mask=mask)

    # Display the original image and the result
    cv.imshow('Original Image', image)
    cv.imshow('Color Detection Result', result)

    # Wait for a key press and close the windows
    if cv.waitKey(1) & 0xFF == ord("q"):
        break


