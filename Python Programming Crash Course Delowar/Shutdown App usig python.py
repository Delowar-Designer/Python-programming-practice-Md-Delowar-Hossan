from tkinter import *
import os

def restart():
    os.system("shutdown -r -t 1")

def restart_time():
    os.system("shutdown -r -t 20")

def shutdown():
    os.system("shutdown -s -t 1")


st = Tk()
st.title("Shut Down App")
st.geometry("500x500")
st.config(bg="blue")
#Restetart batton
r_buton = Button(st,text="Restart",font=("arial",20,"bold"),bg="red",cursor="plus",command=restart)
r_buton.place(x=150,y=60,width=200,height=50)
#Restart with time
r_buton = Button(st,text="Restart Time",font=("arial",20,"bold"),bg="red",cursor="plus",command=restart_time)
r_buton.place(x=150,y=170,width=200,height=50)
#shutdown
r_buton = Button(st,text="shutdown",font=("arial",20,"bold"),bg="red",cursor="plus",command=shutdown)
r_buton.place(x=150,y=270,width=200,height=50)
#closed button
r_buton = Button(st,text="Closed",font=("arial",20,"bold"),bg="red",cursor="plus",command=st.destroy)
r_buton.place(x=150,y=370,width=200,height=50)

st.mainloop()