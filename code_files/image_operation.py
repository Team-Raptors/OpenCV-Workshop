import cv2 as cv
import numpy as np

cap = cv.VideoCapture()
cap = cv.VideoCapture("Images\colors.mp4")
kernel = np.ones((5,5),np.uint8)


while True:
    success, img = cap.read()
    imgcropped = img[0 : 200, 200 : 500]
    
    Gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(Gray, (9, 9), 0.)
    canny = cv.Canny(img, 150, 200)
    dilat = cv.dilate(canny, kernel, iterations = 1)
    # eroded = cv.erode(dilat, kernel, iterations = 1)
    _, thresh = cv.threshold(Gray, 150, 255, cv.THRESH_BINARY)

    #shows the minimum value
    print(_)
    
    cv.imshow("main", img)
    cv.imshow("oputput", Gray)
    cv.imshow("oput", blur)
    cv.imshow("can", canny)
    cv.imshow("dilat", dilat)
    # cv.imshow("eros", eroded)
    cv.imshow("threshold", thresh)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
 
