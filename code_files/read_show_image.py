import cv2 as cv

# Read and display an image
img = cv.imread('your_image.jpg')
cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()
