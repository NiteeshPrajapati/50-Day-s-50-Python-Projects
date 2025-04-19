from MoviePy.editor import * # pip install moviepy
from tkinter.filedialog import *

vid = askopenfilename()
video = MoviePy.editor.VideoFileClip("D:\Python Project\50_Project\videoplayback.mp4") #also add video path
aud = video.audio
aud.write_audiofile("audio.mp3") #to save audio in mp3 format or file
video.close()
aud.close()
print('___END___')
# This code converts a video file to an audio file using the moviepy library.
