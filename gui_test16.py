import tkinter as tk
from tkinter import *
from tkinter import filedialog
root = tk.Tk()
root.geometry('400x400')
root.resizable(False, False)
root.title('Files Guest')
def open_file():
   mypath = filedialog.askopenfilename (initialfile = 'Untitled.txt' , title="Open Text file",   defaultextension=".txt",filetypes=[("Text Documents","*.txt")])
   if not mypath:
        return
   myfile = open(mypath, 'r', encoding='utf8')
   textcontent = myfile.read()
   txt.insert(END,textcontent)
   root.title(mypath)
def save_file():
   mypath = filedialog.asksaveasfilename (initialfile = 'Untitled.txt' , title="Save Text file",initialdir="/",defaultextension=".txt",filetypes=[("Text Documents","*.txt")])
   if not mypath:
        return
   myfile =open(mypath, 'w', encoding='utf8')
   mytext=txt.get(1.0,END) 
   myfile.write(mytext)
   root.title(mypath)
txt = Text(root) 
txt.place(height=320,width=380,x=10,y=20)
btnOpen= Button(root, text= "Open", command= open_file)
btnOpen.place(height=30,width=40,x=130,y=355)
btnSave= Button(root, text= "Save", command= save_file)
btnSave.place(height=30,width=40,x=200,y=355)
root.mainloop()