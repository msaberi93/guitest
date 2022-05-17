import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
root = tk.Tk()
root.title('Guest-Co')
root.geometry('300x300')
root.resizable(False, False)
root.title('Combobox Guest-co')
def categorychanged(event):
    msg = f'You selected {cmbCategories.get()}!'
    showinfo(title='Result', message=msg)

def Qask():
    ans=tk.messagebox.askyesno(title='Guest-app ok cancel', message='Do you want to Quit?')
    if ans :
        root.destroy()
    else:
        pass

categories = ['ARM','AVR','Medical Equipment','Programming','Software','Analog','Digital','UREA']
lblCategory = ttk.Label(text="Please select a category: ")
lblCategory.place(height=20,width=150,x=75,y=120)
strCategory = tk.StringVar()
cmbCategories = ttk.Combobox(root, textvariable=strCategory)
cmbCategories.place(height=30,width=150,x=70,y=150)
cmbCategories['values'] = categories
cmbCategories.bind('<<ComboboxSelected>>', categorychanged)
cmbCategories.current(5)
# Picture Module
cv = Canvas(root, bg = "white",bd=3,relief="groove")
cv.place(height=100,width=220,x=40,y=10)
img=tk.PhotoImage(file='C:/Users/Saberi/Desktop/GUI_TEST/Guest.png')
canvas_img=cv.create_image(10,10,image=img, anchor=NW)
# Exit Module
btn=Button(root, text="Quit", command=Qask)
btn.place(height=30,width=100,x=90,y=200)
root.mainloop()