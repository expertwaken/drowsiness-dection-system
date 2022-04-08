import os
import time
from tkinter import *
root=Tk()
root.title("Drowsiness Detection System")
root.geometry("600x200")
root.resizable(False, False)
title=Label(root, text="DROWSINESS DETECTION SYSTEM",font="courrier",fg="blue")
def call():
  os.system('python drowsiness_detection.py')
btn=Button(root, text="START",padx=30,font=('courrier', 15, 'bold'),fg="black",bg="red",command=call)
dec=Label(root, text="This is a car safety technology which helps prevent \n accidents caused by the driver getting drowsy.",font="courrier",fg="red")
title.grid(row=1,column=4)
dec.grid(row=2,column=4)
title.config(font=("Courier", 24))
copy=Label(root, text="Mr.Kennedy wafula @ copyright 2022",font="courrier",fg="blue")
copy.grid(row=5,column=4)
btn.grid(row=3,column=4)

time1 = ''
clock = Label(root, font=('times', 15, 'bold'), fg="blue")
clock.grid(row=5,column=5)


def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)


tick()
root=mainloop()