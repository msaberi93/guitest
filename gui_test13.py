import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Menu Guest')

cv = Canvas(root, bg = "white",bd=3,relief="groove")
cv.place(height=100,width=220,x=125,y=20)
img=tk.PhotoImage(file='C:/Users/Saberi/Desktop/GUI_TEST/Guest.png')
canvas_img=cv.create_image(10,10,image=img, anchor=NW)

def choice():
    lblSelect.config(text='Your choice is ' + strChoice.get())
strChoice = tk.StringVar()
lblChoice = tk.Label(text="Please select an item: ")
lblChoice.place(height=20,width=150,x=145,y=150)
rdbElectronic = tk.Radiobutton(root, text='Electronic Engineering', variable=strChoice, value='Electronic Engineering', command=choice)
rdbElectronic.place(height=20,width=150,x=145,y=170)
rdbComputer = tk.Radiobutton(root, text='Computer Engineering', variable=strChoice, value='Computer Engineering', command=choice)
rdbComputer.place(height=20,width=150,x=145,y=190)
rdbBiomedical = tk.Radiobutton(root, text='Biomedical Engineering', variable=strChoice, value='Biomedical Engineering', command=choice)
rdbBiomedical.place(height=20,width=150,x=145,y=210)
strChoice.set("Electronic")
lblSelect = tk.Label(text="",relief="groove")
lblSelect.place(height=20,width=220,x=125,y=250)
choice()

def sayhello():
    tk.messagebox.showinfo(title='Guest message', message='Hello world!')
def showabout():
    tk.messagebox.showinfo(title='Guest Menu', message='This program is made by Guest-co to show you how to add menus to your GUI.')
def about_Guest():
    tk.messagebox.showinfo(title='Guest Menu', message='Guest is a company active in the field of artificial intelligence and machine vision.')
def Qask():
    ans=tk.messagebox.askyesno(title='Guest-app ok cancel', message=strChoice.get()+', Do you want to Quit?')
    if ans :
        root.destroy()
    else:
        pass
menubar = Menu(root)
root.config(menu=menubar)
mainmenu=Menu(menubar)
helpmenu=Menu(menubar)
Guestpmenu=Menu(menubar)
quitmenu=Menu(menubar)

menubar.add_cascade(label="Main", menu=mainmenu)
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_cascade(label="Guest", menu=Guestpmenu)
menubar.add_cascade(label="Quit!", menu=quitmenu)

mainmenu.add_command(label="Hello", command=sayhello)
mainmenu.add_separator()
helpmenu.add_command(label="About", command=showabout)
Guestpmenu.add_command(label="About-Guest", command=about_Guest)
# menubar.add_command(label="Quit!", command=root.quit)
quitmenu.add_command(label="Quit!", command=Qask)

root.mainloop()