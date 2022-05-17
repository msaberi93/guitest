import tkinter as tk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
root = tk.Tk()
root.geometry('300x250')
root.resizable(False, False)
root.title('Radiobutton Guest')
def choice():
    lblSelect.config(text='Your choice is ' + strChoice.get())
strChoice = tk.StringVar()
lblChoice = tk.Label(text="Please select an item: ")
lblChoice.place(height=20,width=150,x=70,y=15)
rdbElectronic = tk.Radiobutton(root, text='Electronic Engineering', variable=strChoice, value='Electronic Engineering', command=choice)
rdbElectronic.place(height=20,width=150,x=60,y=50)
rdbComputer = tk.Radiobutton(root, text='Computer Engineering', variable=strChoice, value='Computer Engineering', command=choice)
rdbComputer.place(height=20,width=150,x=60,y=80)
rdbBiomedical = tk.Radiobutton(root, text='Biomedical Engineering', variable=strChoice, value='Biomedical Engineering', command=choice)
rdbBiomedical.place(height=20,width=150,x=60,y=110)
strChoice.set("Electronic")
lblSelect = tk.Label(text="",relief="groove")
lblSelect.place(height=20,width=250,x=30,y=150)
choice()

# Exit Module
def Qask():
    ans=tk.messagebox.askyesno(title='Guest-app ok cancel', message=strChoice.get()+' , Do you want to Quit ? ')
    if ans :
        root.destroy()
    else:
        pass
# Exit Module
btn=Button(root, text="Quit", command=Qask)
btn.place(height=30,width=100,x=90,y=180)
root.mainloop()