#1 Digital Clack in Python
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("my clock")
label = Label(root,font=("ds-digital",150),background='black',foreground='red')
label.pack(anchor='center')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000,time)

time()
mainloop()
