import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/home/rishisharma/Documents/Computer Vision with OpenCV and Deep Learning/Computer-Vision-with-Python Notebooks/DATA/haarcascades/haarcascade_frontalface_default.xml')

eyes_cascade = cv2.CascadeClassifier('/home/rishisharma/Documents/Computer Vision with OpenCV and Deep Learning/Computer-Vision-with-Python Notebooks/DATA/haarcascades/haarcascade_eye.xml')

smile_cascade = cv2.CascadeClassifier('/home/rishisharma/Documents/Computer Vision with OpenCV and Deep Learning/Computer-Vision-with-Python Notebooks/DATA/haarcascades/haarcascade_smile.xml')

def detect_face(image):
    
    face_image = image.copy()
    
    face_rect = face_cascade.detectMultiScale(face_image, scaleFactor = 1.2, minNeighbors = 10)
    eyes_rect = eyes_cascade.detectMultiScale(face_image, scaleFactor = 1.2, minNeighbors = 10)
    smile_rect = eyes_cascade.detectMultiScale(face_image, scaleFactor = 1.2, minNeighbors = 10)
    
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_image, (x, y), (x+w, y+h), (255, 0, 255), 4)
        
    for (x, y, w, h) in eyes_rect:
        cv2.rectangle(face_image, (x, y), (x+w, y+h), (0, 255, 255), 4)
        
    for (x, y, w, h) in smile_rect:
        cv2.rectangle(face_image, (x, y), (x+w, y+h), (0, 255, 255), 4)
        
    return face_image
    

while True:
    
    _, frame = cap.read(0)
    
    frame = detect_face(frame)
    cv2.imshow("Face Detection", frame)
    
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()