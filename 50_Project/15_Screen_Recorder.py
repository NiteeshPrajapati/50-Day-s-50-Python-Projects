import cv2
import pyautogui
import numpy as np
from win32api import GetSystemMetrics   #screen revolution
import time
width = GetSystemMetrics(0)  # screen width
height = GetSystemMetrics(1)  # screen height
dim = (width, height)  # screen dimension
fps = 30.0  # frame per second
f = cv2.VideoWriter_fourcc(*"XVID")  # codec
output = cv2.VideoWriter("output.mp4", f, fps, dim)  # output file nam
now_start_time = time.time()
duration = 10+4  # seconds //
end_time = now_start_time + duration  # end time
while True:
    # Capture the screen
    img = pyautogui.screenshot()
    # Convert to numpy array
    frame = np.array(img)
    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # save original color
    # Write the frame to the output file
    output.write(frame)
    c_time = time.time()
    # Display the screen
    cv2.imshow("Screen Recorder", frame)
    if c_time > end_time:
        break
    output.release()  # release the output file
    cv2.destroyAllWindows()  # destroy all windows
    print("Screen recording completed.")
