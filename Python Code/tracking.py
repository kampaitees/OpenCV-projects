import numpy as np
import cv2

cap = cv2.VideoCapture(0)
_, frame1 = cap.read()
prev_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
prevPts = cv2.goodFeaturesToTrack(prev_frame, maxCorners = 2, qualityLevel = 0.04, minDistance = 7, blockSize = 7, mask = None)
mask = np.zeros_like(frame1)


while True:
    
    _, frame2 = cap.read()
    current_frame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_frame, current_frame, prevPts, None, winSize = (200, 200), maxLevel = 4, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.3))
    
    good_prev = prevPts[status == 1]
    good_new = nextPts[status == 1]
    
    for i, (prev, new) in enumerate(zip(good_prev, good_new)):
        
        x_prev, y_prev = prev.ravel()
        x_next, y_next = new.ravel()
        
        mask = cv2.line(mask, (x_prev, y_prev), (x_next, y_next), (255, 0, 0), 3)
        frame2 = cv2.circle(frame2, (x_next, y_next), 4, (255, 255, 0), -1)
        
    img = cv2.add(frame2, mask)
    cv2.imshow('Image Tracker', img)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    prev_frame = current_frame
    
cap.release()
cv2.destroyAllWindows()