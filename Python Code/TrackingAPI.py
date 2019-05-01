import cv2

def selectTrackerForObj():
    
    print('Welcome in the Object Tracker API!!!')
    print('1.Boosting')
    print('2.TLD')
    print('3.MIL')
    print('4.KCF')
    print('5.Median Flow')
    
    choice = int(input('Enter the choice for the tracker:'))
    
    if choice == 1:
        tracker = cv2.TrackerBoosting_create()
    elif choice == 2:
        tracker = cv2.TrackerTLD_create()
    elif choice == 3:
        tracker = cv2.TrackerMIL_create()
    elif choice == 4:
        tracker = cv2.TrackerKCF_create()
    elif choice == 5:
        tracker = cv2.TrackerMedianFlow_create()
    else:
        print('Ooops!, You entered wrong chocie, Plz try again!!')
        
    return tracker

tracker = selectTrackerForObj()
trackerName = str(tracker).split()[0][1:]

cap = cv2.VideoCapture(0)
_, frame = cap.read()

roi = cv2.selectROI(frame, False)

ret = tracker.init(frame, roi)

while True:
    
    ret, frame = cap.read()
    
    success, roi = tracker.update(frame)
    
    if success:
        (x, y, w, h) = tuple(map(int, roi))
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 6)
        
    else:
        cv2.putText(frame, 'Object out of Frame!!!', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 5)
        
    cv2.putText(frame, trackerName, (5, 600), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 5)
    
    cv2.imshow(trackerName, frame)
    
    k = cv2.waitKey(1) & 0xFF
    
    if k == 27 or k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()