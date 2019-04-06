import cv2

centre = (0, 0)
button_clicked = False

def draw_circle(event, x, y, flags, param):
    
    global centre, button_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        if button_clicked:
            centre = (x, y)
            button_clicked = True
        
        elif not button_clicked:
            centre = (x, y)
            button_clicked = True
        

cap = cv2.VideoCapture(0)

cv2.namedWindow(winname = "My_Window")
cv2.setMouseCallback("My_Window", draw_circle)

while True:
    
    _, frame = cap.read()
     
    if button_clicked:
        cv2.circle(frame, centre, radius = 40, color = (255, 0, 0), thickness = 3)
            
    cv2.imshow("My_Window", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
    
cap.release()
cv2.destroyAllWindows()

