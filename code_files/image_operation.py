import cv2 as cv
import numpy as np

# Initialize video capture object
cap = cv.VideoCapture("Images\colors.mp4")

# Define a kernel for image dilation
kernel = np.ones((5, 5), np.uint8)

# Infinite loop to continuously process frames
while True:
    # Read a frame from the video
    success, img = cap.read()
    
    # Crop the image to a specific region of interest
    imgcropped = img[0:200, 200:500]
    
    # Convert the frame to grayscale
    Gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the grayscale image
    blur = cv.GaussianBlur(Gray, (9, 9), 0.)
    
    # Apply Canny edge detection to the original frame
    canny = cv.Canny(img, 150, 200)
    
    # Apply dilation to the Canny edges
    dilat = cv.dilate(canny, kernel, iterations=1)
    
    # Threshold the grayscale image
    _, thresh = cv.threshold(Gray, 150, 255, cv.THRESH_BINARY)

    # Display the minimum value of the thresholding result
    print(_)

    # Display the original frame
    cv.imshow("main", img)
    
    # Display the grayscale image
    cv.imshow("Gray", Gray)
    
    # Display the blurred image
    cv.imshow("blur", blur)
    
    # Display the Canny edges
    cv.imshow("canny", canny)
    
    # Display the dilated edges
    cv.imshow("dilat", dilat)
    
    # Display the thresholded image
    cv.imshow("threshold", thresh)

    # Break the loop if the 'q' key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
