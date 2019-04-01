import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('Rishi.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))
while True:
    _, frame = cap.read()
    writer.write(frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.realease()
writer.release()
cv2.destroyAllWindows()