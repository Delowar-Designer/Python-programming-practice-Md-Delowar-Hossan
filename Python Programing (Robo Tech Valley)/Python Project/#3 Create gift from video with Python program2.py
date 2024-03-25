# Create GIF from video with Python program
from moviepy.editor import VideoFileClip
from tkinter.filedialog import askopenfilename

# Open file dialog to select video
video_path = askopenfilename()

# Check if a file is selected
if video_path:
    # Load video clip
    clip = VideoFileClip(video_path)

    # Set FPS value (adjust as needed)
    fps = 24  # Example: 24 frames per second

    # Create GIF from video
    clip.write_gif("Waterfall_GIF.gif", fps=fps)

    # Confirm GIF creation
    print("GIF created successfully.")
else:
    print("No file selected. Please select a video file.")
