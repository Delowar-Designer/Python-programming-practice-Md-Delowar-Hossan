# Creating a dice Rolling game
from  tkinter import *
import random

root = Tk()
root.geometry('400x400')
l1 = Label(root, font=('Helvetica',260))
l1.pack()

def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text = f'{random.choice(dice)}')
    l1.pack()

b1 = Button(root,text="Roll",bg="white",fg = "blue",command = roll,font = ('Helvetica',20))
b1.place(x = 170, y = 10)
roll()
root.mainloop()