import cv2
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

n_markers = 10
current_marker = 1
marker_updated = False

road = cv2.imread('/home/rishisharma/Documents/Computer Vision with OpenCV and Deep Learning/Computer-Vision-with-Python Notebooks/DATA/road_image.jpg')

road_copy = road.copy()
marker = np.zeros(road.shape[:2], dtype = np.int32)
segment = np.zeros(road.shape, dtype = np.uint8)

def color(i):
    x = np.array(cm.tab10(i))[:3]*255
    return tuple(x)

colors = []
for i in range(n_markers):
    colors.append(color(i))
     
def mouse_call_back(event, x, y, flags, param):
    
    global marker_updated
    
    if event == cv2.EVENT_LBUTTONDOWN:
        marker_updated = True
        
        cv2.circle(marker, (x, y), 10, (current_marker), -1)
        cv2.circle(road_copy, (x, y), 10, colors[current_marker], -1)
        
        marker_updated = True
        
cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_call_back)
        
while True:
    
    cv2.imshow('Image', segment)
    cv2.imshow('Road Image', road_copy)
   
    k = cv2.waitKey(1)
    if k == 27:
        break
        
    elif k == ord('c'):
        
        road_copy = road.copy()
        marker = np.zeros(road_copy.shape[:2], dtype = np.int32)
        segment = np.zeros(road.shape, dtype = np.uint8)
        
    elif k > 0 and chr(k).isdigit():
        
        current_marker = int(chr(k))
      
    if marker_updated:
        
        marker_image_copy = marker.copy()
        cv2.watershed(road, marker_image_copy)
        
        segment = np.zeros(road.shape,dtype=np.uint8)
        
        for color_ind in range(n_markers):
            segment[marker_image_copy == (color_ind)] = colors[color_ind]
        
        marker_updated = False
        
cv2.destroyAllWindows()