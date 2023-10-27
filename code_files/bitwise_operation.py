# Python program to illustrate 
# arithmetic operation of 
# bitwise AND of two images 
	
# organizing imports 
import cv2 
import numpy as np 
	
# path to input images are specified and 
# images are loaded with imread command 
img1 = cv2.imread('input1.png') 
img2 = cv2.imread('input2.png') 

# cv2.bitwise_and is applied over the 
# image inputs with applied parameters 
dest_and = cv2.bitwise_and(img2, img1, mask = None) 
dest_or = cv2.bitwise_or(img1, img2, mask = None) 

# the window showing output image 
# with the Bitwise AND operation 
# on the input images 
cv2.imshow('Bitwise And', dest_and) 

# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
