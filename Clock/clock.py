import datetime
from tkinter import *
from time import *
from datetime import *
from  winsound import *


def time():
    s=strftime('%H:%M:%S  \n %x\n  %A \n %z,\n %Z')
    clk.config(text=s)
    clk.after(1000,time)


root =Tk()
root.grid_bbox('1000x1000')

root.title("Clock")

clk =Label(root,font=('DS-DIGITAL',60,'bold'),bg="#068ad6")
clk.pack(anchor='center')

time()
mainloop()
clk =Label(root,font=('DS-DIGITAL',60,'bold'),bg="#068ad6")
clk.pack(anchor='center')

