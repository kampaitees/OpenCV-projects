import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()
    
    faceCascade = cv2.CascadeClassifier('..DATA/haarcascades/haarcascade_frontalface_default.xml')
    faceDetector = faceCascade.detectMultiScale(frame, minNeighbors = 15)
    
    for (x, y, w, h) in faceDetector:
        rectanglegFrame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
    
    cv2.imshow('Detected Image', frame)
    
    if len(tuple(faceDetector)) != 0:
        (faceX, faceY, w, h) = tuple(faceDetector[0])
    
    k = cv2.waitKey(1) & 0xff
    
    if k == 27 or k == ord('q'):
        break
    
trackWindow = (faceX, faceY, w, h)

roi = frame[faceY:faceY+h, faceX:faceX+w]

roiHsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roiHist = cv2.calcHist([roiHsv], [0], None, [180], [0, 180])

cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)

termCriteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    
    _, framePrime = cap.read()

    hsv = cv2.cvtColor(framePrime, cv2.COLOR_BGR2HSV)
    
    dst = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)
    
    _, trackWindow = cv2.meanShift(dst, trackWindow, termCriteria)
    
    x, y, w, h = trackWindow
    
    rectangleFrame = cv2.rectangle(framePrime, (x, y), (x+w, y+h), (0, 255, 0), 4)
    cv2.imshow('Tracked Image', rectangleFrame)
    
    k = cv2.waitKey(1) & 0xff
    
    if k == 27 or k == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()