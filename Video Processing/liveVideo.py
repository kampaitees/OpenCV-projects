import cv2

pt1 = (0, 0)
pt2 = (0, 0)
top_left_corner = False
bottom_right_corner = False

def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, top_left_corner, bottom_right_corner
    if event == cv2.EVENT_LBUTTONDOWN:
        
        if top_left_corner and bottom_right_corner:
            pt1 = (0, 0)
            pt2 = (0, 0)
            top_left_corner = False
            bottom_right_corner = False
            
        if top_left_corner == False:
            pt1 = (x, y)
            top_left_corner = True
        elif  not bottom_right_corner:
            pt2 = (x, y)
            bottom_right_corner = True

cap = cv2.VideoCapture(0)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow(winname = 'Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    
    _ , frame = cap.read()
    
    if top_left_corner:
        cv2.circle(frame, pt1, radius = 4, color = (0, 255, 0), thickness = -1)
    if top_left_corner and bottom_right_corner:
        cv2.rectangle(frame, pt1, pt2, color = (255, 0, 0), thickness = 6)
    
    cv2.imshow("Test", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

