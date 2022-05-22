import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.geometry("300x150")
root.resizable(False,False)
root.title('Icon Guest')
lblRate=Label(root, text="You Can see the default Icon. ")
lblRate.place(height=20,width=160,x=70,y=50)
root.mainloop()

#############################################

import os
import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.geometry("450x200")
root.resizable(False,False)
root.title('Icon Guest')
lblRate=Label(root, text="You Can see Your Icon. ")
lblRate.place(height=20,width=160,x=70,y=50)
currentDir=os.path.dirname(os.path.abspath(__file__))
photo = PhotoImage(file = currentDir + "\Guest.png")
root.iconphoto(False,photo)
root.mainloop()

#############################################

