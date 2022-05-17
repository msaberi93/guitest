# import tkinter 
# from tkinter import *
# root=tkinter.Tk()
# root.geometry("300x200")
# root.resizable(False,False)
# def clicked():
#     lbl.configure(text="Guest")
# lbl=Label(root, text="Welcome to")
# lbl.place(height=50,width=100,x=100,y=40)
# btn=Button(root, text="Click Here!", command=clicked)
# btn.place(height=50,width=100,x=100,y=140)
# root.mainloop()


# import tkinter 
# from tkinter import *
# root=tkinter.Tk()
# root.title("Guest Application")
# root.geometry("300x200")
# root.resizable(False,False)
# def clicked():
#     lbl.configure(text="Guest")
#     btn.configure(state="disabled")
# lbl=Label(root, text="Welcome to")
# lbl.place(height=50,width=100,x=100,y=40)
# btn=Button(root, text="Click Here!", command=clicked)
# btn.place(height=50,width=100,x=100,y=140)
# root.mainloop()

import tkinter 
from tkinter import *
root=tkinter.Tk()
root.title("Guest Application")
root.geometry("350x250")
root.resizable(False,False)
def clicked():
    lbl.configure(text="Welcom to Guest-co")
    btn.configure(state="disabled")
def Terminate():
    root.destroy()
lbl=Label(root, text="Welcom to Guest-co")
lbl.place(height=100,width=150,x=100,y=40)
btn=Button(root, text="Exit", command=Terminate)
btn.place(height=50,width=100,x=120,y=150)
root.mainloop()

