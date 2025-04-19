import numpy as np 
import cv2 
import imutils
import datetime
import time

gun_cascade = cv2.CascadeClassifier('cascade.xml')
video = cv2.VideoCapture(0)

firstframe = None
gun_exist = None

while True:
    check, frame = video.read()
    frame = imutils.resize(frame, width=500)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun = gun_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))

if len(gun) > 0:
    gun_exist = True
    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
    
        if firstframe is None:
           firstframe = gray
           continue
    
        cv2.imshow("Security Feed", frame)
        key = cv2.waitKey(1)& 0xFF
    
        if key == ord('q'):
           break   

if gun_exist :
    print("Gun detected")
else:
    print("No gun detected")    
video.release()
cv2.destroyAllWindows()    
        
    