# import tkinter 
# from  tkinter import ttk
# root=tkinter.Tk()
# lbl=ttk.Label(root, text="Hello Guest")
# lbl.grid(column=0, row=0)
# root.mainloop()

# import tkinter 
# from  tkinter import ttk
# root=tkinter.Tk()
# lbl=ttk.Label(root, text="Hello Guest")
# lbl.pack()
# root.mainloop()

# import tkinter 
# from  tkinter import ttk
# root=tkinter.Tk()
# root.geometry("300x200")
# root.resizable(False,False)
# lbl=ttk.Label(root, text="Hello Guest", background='pink')
# lbl.place(height=50,width=100,x=100,y=40)
# root.mainloop()

# import tkinter 
# from tkinter import *
# root=tkinter.Tk()
# root.geometry("300x200")
# root.resizable(False,False)
# root.title("label")
# lbl=Label(root, text="Hello Guest",bg="pink")
# lbl.place(height=50,width=100,x=100,y=40)
# root.mainloop()


# import tkinter 
# from tkinter import *
# root=tkinter.Tk()
# root.geometry("300x200")
# root.resizable(False,False)
# root.title("label")
# lbl=Label(root, text="Hello Guest",bg="blue" , relief = "flat")
# lbl.place(height=50,width=100,x=100,y=40)
# lbl.configure(fg="pink")
# root.mainloop()

# import tkinter 
# from tkinter import *
# root=tkinter.Tk()
# root.geometry("260x280")
# root.resizable(False,False)
# lblFlat=Label(root, text="flat",bd=2,relief="flat")
# lblFlat.place(height=30,width=60,x=100,y=10)
# lblRaised=Label(root, text="raised",bd=2,relief="raised")
# lblRaised.place(height=30,width=60,x=100,y=50)
# lblSunken=Label(root, text="sunken",bd=2,relief="sunken")
# lblSunken.place(height=30,width=60,x=100,y=90)
# lblRidge=Label(root, text="ridge",bd=2,relief="ridge")
# lblRidge.place(height=30,width=60,x=100,y=130)
# lblSolid=Label(root, text="solid",bd=2,relief="solid")
# lblSolid.place(height=30,width=60,x=100,y=170)
# lblGroove=Label(root, text="groove",bd=2,relief="groove")
# lblGroove.place(height=30,width=60,x=100,y=210)
# root.mainloop()

import tkinter 
from tkinter import *
root=tkinter.Tk()
root.geometry("300x200")
root.resizable(False,False)
root.title("label")
lbl=Label(root, text="Hello Guest",bg="blue" , relief = "raised")
lbl.place(height=50,width=100,x=100,y=40)
lbl.configure(fg="pink")
root.mainloop()