import cv2 as cv
import numpy as np

# Load an image
img = cv.imread("Images/colors.jpg")

# Define a kernel for image dilation
kernel = np.ones((5, 5), np.uint8)

# Crop the image to a specific region of interest
imgcropped = img[0:200, 200:500]

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blur = cv.GaussianBlur(gray, (9, 9), 0)

# Apply Canny edge detection to the original image
canny = cv.Canny(img, 150, 200)

# Apply dilation to the Canny edges
dilat = cv.dilate(canny, kernel, iterations=1)

# Threshold the grayscale image
_, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

# Display the minimum value of the thresholding result
print(_)

# Display the original image
cv.imshow("Original Image", img)

# Display the cropped image
cv.imshow("Cropped Image", imgcropped)

# Display the grayscale image
cv.imshow("Gray", gray)

# Display the blurred image
cv.imshow("Blur", blur)

# Display the Canny edges
cv.imshow("Canny", canny)

# Display the dilated edges
cv.imshow("Dilated Edges", dilat)

# Display the thresholded image
cv.imshow("Threshold", thresh)

# Wait for a key press and close the OpenCV windows
if cv.waitKey(0) & 0xFF == 27:  # Press 'q' to exit
    cv.destroyAllWindows()
