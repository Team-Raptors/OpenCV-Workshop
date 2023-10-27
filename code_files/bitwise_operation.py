import cv2 
import numpy as np 
	
img1 = cv2.imread('input1.png') 
img2 = cv2.imread('input2.png') 

bit_and = cv2.bitwise_and(img2, img1, mask = None) 
bit_or = cv2.bitwise_or(img1, img2, mask = None) 

cv2.imshow('Bitwise And', dest_and) 
cv2.imshow('Bitwise Or', bit_or)

cv2.waitKey(0)
