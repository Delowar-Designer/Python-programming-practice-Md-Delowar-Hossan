# Making a Digital Clock by Simple
import time
from tkinter import *
import sys

root = Tk()
root.title("Digital Clock Programer Delowar.Designer") # if is the name of your clock

def get_time():
    time_string = time.strftime("%I:%M:%S %p") # you can use %H for 24 hours format or use %I for 12 hours format
    clock.config(text=time_string)
    clock.after(200,get_time)

clock = Label(root,font=("time",100,"bold","italic"))  # here you can change font size and style

clock.pack()

get_time()

root.mainloop()