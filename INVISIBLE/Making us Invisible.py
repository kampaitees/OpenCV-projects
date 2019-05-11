#IMPORTING DEPENDENCIES
import numpy as np
import cv2

#NAME OF VIDEO FILE
video_name = 'invisible.avi'

#CREATIG OBJECT FOR CAPTURING LIVE VIDEO
cap = cv2.VideoCapture(0)

#DEFINING WIDTH AND HEIGHT FOR OUR VIDEO
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#CREATING OBJECT OF VIDEO CLASS IN OPENCV TO SAVE OUR VIDEO
out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 25, (width, height))

#INFINITE WHILE LOOP
count = 0
while True:
    
    #CAPTURING LIVE VIDEO
    _, frame = cap.read()
    
    #CONDITION TO CHECK WHETHER WEBCAM IS WORKING OR NOT
    if _ == True:
        
        while count <= 10:
            count += 1
            bkg_image = frame
            continue
        
        #CONVERTING RGB FORMAT OF IMAGE TO HSV FORMAT AS IT BEST DESCRIBES OUR DAILY VISUALIZATION
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #SINCE THERE ARE TWO RANGES OF RED COLOR IN HSV(0-180) FORMAT SO DEFINING TWO RANGES
        
        #DEFINING RANGE 1
        lower_red_1 = np.array([0, 120, 70])
        upper_red_1 = np.array([10, 255, 255])
        
        #DEFINING RANGE 2
        lower_red_2 = np.array([170, 120, 70])
        upper_red_2 = np.array([180, 255, 255])
        
        #CREATING MASKS FOR THE ABOVE TWO RANGES
        mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
        mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
        
        #COMBIMING THE MASKS OF TWO DIFFERENT RANGES
        mask = mask1 + mask2
        
        #APPLYING MORPHOLOGICAL OPERATOR TO FILL NOISE IN THE MASK
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((11, 11),np.uint8))
        
        #CREATING BITWISE NOT(INVERTING THE PIXELS OF THE IMAGE) OF THE ABOVE MASK
        not_mask = cv2.bitwise_not(mask)
        
        #GETTING THE INTERMEDIATE IMAGES
        image_prime_1 = cv2.bitwise_and(frame, frame, mask = not_mask)
        image_prime_2 = cv2.bitwise_and(bkg_image, bkg_image, mask = mask)
        
        #GETTING THE FINAL IMAGES
        final_image = cv2.bitwise_or(image_prime_1, image_prime_2)
        
        #FLIPPING THE IMAGE SO THAT MOTION IN THE VIDEO IS SAME AS OURS
        final_image = cv2.flip(final_image, 1)
        
        #FINALLY SAVING OUR FRAMES IN A VIDEO
        out.write(final_image)
        
        #SHOWING VIDEO ON SCREEN
        cv2.imshow('Invisible image', final_image)
        
        #TO STOP THE LIVE STREAM 
        k = cv2.waitKey(1) & 0xFF
        
        #13 - ENTER KEY, 27 - ESCAPE KEY
        if k == 13 or k == 27 or k == ord('q'):
            break
            
#RELEASING THE VIDEO FRAMES
cap.release()

#DESTROYING THE OPENED 
cv2.destroyAllWindows()