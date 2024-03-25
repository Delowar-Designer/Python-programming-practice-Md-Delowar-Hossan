# Create gift from video with Python program
# import necessary library
from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

# open file for load video
video = askopenfilename()

# load file in a variable
clip = VideoFileClip(video)

# Make Gif of Uploaded viddeo
clip.write_gif("Water fall GIF.gif", fps = 600)