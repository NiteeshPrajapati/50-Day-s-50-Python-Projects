###  ----> for camera opening
# import cv2
# video_cap = cv2.VideoCapture(0) # 0 for webcam, or provide a video file path
# while True:
#     ret, frame = video_cap.read()
#     if not ret: # If the frame is not captured correctly, break the loop
#         break
#     cv2.imshow('Video', frame)
#     if cv2.waitKey(5) & 0xFF == ord('q'): # Press 'q' to exit the loop
#         break
# video_cap.release() # Release the video capture object
# cv2.destroyAllWindows() # Close all OpenCV windows    

#### ----> for face detection
import cv2
face_cap = cv2.CascadeClassifier("D:/Python Project/50_Project/.venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml") # Load the Haar Cascade classifier for face detection
video_cap = cv2.VideoCapture(0) # 0 for webcam, or provide a video file path
while True:
    ret, frame = video_cap.read()
    col = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert the frame to grayscale
    faces = face_cap.detectMultiScale(col, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE) # Detect faces in the frame
    for (x, y, w, h) in faces: # Loop through the detected faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255, 0), 2)
        #cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    if not ret: # If the frame is not captured correctly, break the loop
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'): # Press 'q' to exit the loop
        break
video_cap.release() # Release the video capture object
cv2.destroyAllWindows() # Close all OpenCV windows    
