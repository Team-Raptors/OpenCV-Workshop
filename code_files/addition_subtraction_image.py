# Python add
# arithmetic operation of 
# organizing imports 
import cv2 
import numpy as np 
	
image1 = cv2.imread('Images/add input1.jpg') 
image2 = cv2.imread('Images/add input 2.jpg') 

cv2.imshow('img1', image1)
cv2.imshow('img2', image2)

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0) 
sub = cv2.subtract(image1, image2)


cv2.imshow('Weighted Image', weightedSum) 
cv2.imshow('Subtracted Image', sub)

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
