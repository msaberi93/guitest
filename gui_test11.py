import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Checkbutton Guest')
def choice():
    if intChoice1.get()==1:
        lbl1.configure(text="Item 1 is selected.")
    else:
        lbl1.configure(text="Item 1 is NOT selected.")
    if intChoice2.get()==1:
        lbl2.configure(text="Item 2 is selected.")
    else:
        lbl2.configure(text="Item 2 is NOT selected.")   

def Qask():
    ans=tk.messagebox.askyesno(title='Guest-app ok cancel', message='Do you want to Quit?')
    if ans :
        root.destroy()
    else:
        pass

lblSelect = tk.Label(text="Please select an item: ")
lblSelect.place(height=20,width=150,x=40,y=20)
intChoice1 = tk.IntVar()
# intChoice1.set(1)
intChoice2 = tk.IntVar()
chkChoice1 = tk.Checkbutton(root, text="Item 1" , variable=intChoice1,  command=choice)
chkChoice1.place(height=20,width=100,x=40,y=50)
chkChoice2 = tk.Checkbutton(root, text="Item 2" , variable=intChoice2,  command=choice)
chkChoice2.place(height=20,width=100,x=40,y=80)
lbl1 = tk.Label(text="Item 1 is NOT selected. ",relief="groove")
lbl1.place(height=20,width=130,x=140,y=50)
lbl2 = tk.Label(text="Item 2 is NOT selected. ",relief="groove")
lbl2.place(height=20,width=130,x=140,y=80)

# Exit Module
btn=Button(root, text="Quit", command=Qask)
btn.place(height=30,width=100,x=100,y=120)
root.mainloop()