import numpy as np
import cv2 
import pickle

face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_eye.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name":1}
with open("labels.pickle",'rb') as f:
	labels = pickle.load(f)
	labels = {v:k for k,v in labels.items()}

cap = cv2.VideoCapture(0)

while  (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) 
    for(x ,y, w, h) in faces:
    	#print(x,y,w,h)
    	roi_gray = gray[y:y+h,x:x+w]          #[ycord_start, ycord_end]
    	roi_color = frame[y:y+h,x:x+w]



    	#recognize? deep learned model predeict keras tensorflow pytorch scikit learn
    	id_, conf = recognizer.predict(roi_gray)
    	if conf>=45: #and conf<=85:
        	print(id_)
        	print(labels[id_])
        	font = cv2.FONT_HERSHEY_SIMPLEX
        	name = labels[id_]
        	color = (255,255,255)
        	stroke = 2
        	cv2.putText(frame, name ,(x,y), font, 1, color, stroke, cv2.LINE_AA)

    	img_item = "7.png"
    	cv2.imwrite(img_item, roi_color)

    	color = (255, 0 ,0) #BGR values = 0-255
    	stroke = 2 #thickness of line
    	end_chord_x = x + w #width
    	end_chord_y = y + h #heigth
    	cv2.rectangle(frame, (x,y), (end_chord_x , end_chord_y), color, stroke)
    	eyes = eye_cascade.detectMultiScale(roi_gray)
    	for(ex,ew,ey,eh) in eyes:
    		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    #display the resulting frame
    cv2.imshow('frame', frame) #impshow
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
      
cv2.destroyAllWindows()       