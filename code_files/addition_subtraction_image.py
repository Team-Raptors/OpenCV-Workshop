import cv2 as cv  # Import OpenCV and alias it as cv
import numpy as np

# Load two images
image1 = cv.imread('Images/add input1.jpg')
image2 = cv.imread('Images/add input 2.jpg')

# Display the loaded images
cv.imshow('img1', image1)
cv.imshow('img2', image2)

# Perform weighted addition of the two images
weightedSum = cv.addWeighted(image1, 0.5, image2, 0.4, 0)

# Subtract image2 from image1
sub = cv.subtract(image1, image2)

# Display the resulting images
cv.imshow('Weighted Image', weightedSum)
cv.imshow('Subtracted Image', sub)

# Wait for a key press and close the OpenCV windows
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
