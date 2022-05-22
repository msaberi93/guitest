import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('Text Guest')
def transfer():
    mytext = txt.get('1.0','end')
    lbl.config(text=mytext)
def clear():
    txt.delete('1.0','end')
    transfer()
txt = Text(root) 
txt.place(height=100,width=260,x=20,y=20)
txt.insert(INSERT, "Hello world")
txt.insert(END, " From Guest")  
txt_content = txt.get('1.0','end')
lbl=Label(root, relief="groove")
lbl.place(height=100,width=260,x=20,y=130)
btnClear=tk.Button(root, text="Clear", command=clear)
btnClear.place(height=30,width=50,x=50,y=250)
btnTransfer=tk.Button(root, text="Write", command=transfer)
btnTransfer.place(height=30,width=50,x=200,y=250)
root.mainloop()

