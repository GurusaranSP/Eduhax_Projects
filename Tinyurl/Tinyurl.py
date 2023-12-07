from tkinter import *
import pyshorteners
import pyperclip
root = Tk()
root.geometry("500x500")
root.title("URL Shortner")
root.config(bg="#03589e")

a=StringVar()
b=StringVar()

def urls():
    urladd=a.get()
    print(a.get())
    url_short = pyshorteners.Shortener().tinyurl.short(urladd)
    b.set(url_short)
title = Label(root, text="URL Shortner", bd=10, relief=GROOVE,font=("Arial",30,"bold"), bg="#000000", fg ="RED")
title.pack(side=TOP, fill=X)
Entry(root,textvariable=a,font=("Arial",15,"bold"),bd=5, relief=GROOVE).pack(pady=50)
Button(root,text="Generate", command=urls).pack(pady=50)

def copy():
 x=b.get()
 pyperclip.copy(x)
Entry(root,textvariable=b, font=("Arial",15,"bold"),bd=5, relief=GROOVE).pack(pady=50)

Button(root,text="Copy",command=copy).pack(pady=10)


root.mainloop()