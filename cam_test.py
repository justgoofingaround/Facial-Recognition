import numpy as np
import cv2 

cap = cv2.VideoCapture(0)
while  (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #for_gray_color
    cv2.imshow('frame', frame) #impshow
    c .imshow('gray', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break  
cv2.destroyAllWindows        