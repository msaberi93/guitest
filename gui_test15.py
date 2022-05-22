import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry('300x150')
root.resizable(False, False)
root.title('Button Menu Guest')
def analog():
    lbl.configure(text='Analog Circuits')
def digital():
    lbl.configure(text='Digital Circuits')
def unknow():
    lbl.configure(text='Unknow Circuits')
mbtn = Menubutton(root, text="category", relief="groove")
mbtn.place(height=30,width=100,x=30,y=30)
mbtn.menu=Menu(mbtn, tearoff=0)
# mbtn.menu=Menu(mbtn)
mbtn["menu"]=mbtn.menu  
mbtn.menu.add_command ( label="Analog", command=analog )
mbtn.menu.add_command ( label="Digital", command=digital )
mbtn.menu.add_command ( label="Unknow", command=unknow )

lbl=Label(root, relief="groove")
lbl.place(height=30,width=100,x=170,y=30)
root.mainloop()