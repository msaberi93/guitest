import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.geometry("600x350")
root.resizable(False,False)
def Xchanged(none):
    xx=sclX.get()    
    lblX.configure(text="X: " + str(xx))
def Ychanged(none):
    yy=sclY.get()    
    lblY.configure(text="Y: " + str(yy))
dblX=DoubleVar()
dblY=DoubleVar()
lblX=Label(root, text="X:" )
lblX.place(height=50,width=50,x=50,y=50)
lblY=Label(root, text="Y:" )
lblY.place(height=50,width=50,x=50,y=100)
sclX=Scale(root, label='X:', from_=0, to=100, variable=dblX, tickinterval=5, length=500, showvalue=0, resolution=5, orient=HORIZONTAL, command=Xchanged)
sclX.place(x=10,y=230)
sclY=Scale(root, label='Y:', from_=0, to=100, variable=dblY, tickinterval=10, length=200, orient=VERTICAL, command=Ychanged)
sclY.place(x=500,y=40)
root.mainloop()