import cv2 as cv
import numpy as np

# Load the two input images
img1 = cv.imread('input1.png')
img2 = cv.imread('input2.png')

# Perform bitwise AND operation on the two images
bit_and = cv.bitwise_and(img2, img1, mask=None)

# Perform bitwise OR operation on the two images
bit_or = cv.bitwise_or(img1, img2, mask=None)

# Display the result of bitwise AND operation
cv.imshow('Bitwise And', bit_and)

# Display the result of bitwise OR operation
cv.imshow('Bitwise Or', bit_or)

# Wait for a key press and then close the windows
cv.waitKey(0)
cv.destroyAllWindows()
