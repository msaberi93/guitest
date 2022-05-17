# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# root=tk.Tk()
# root.title("Guest Application")
# root.geometry("300x200")
# root.resizable(False,False)
# def showinformation():
#     tk.messagebox.showinfo(title='Guest info', message='Welcome to UREA granulation software !!!')
# btn=Button(root, text="show information", command=showinformation)
# btn.place(height=50,width=150,x=75,y=70)
# root.mainloop()

#********************************#
# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# root=tk.Tk()
# root.title("Guest Application")
# root.geometry("300x200")
# root.resizable(False,False)
# def showwarning():
#     tk.messagebox.showwarning(title='Guest warning', message='Welcome to UREA granulation software !!!')
# btn=Button(root, text="show warning", command=showwarning)
# btn.place(height=50,width=150,x=75,y=70)
# root.mainloop()
#********************************#
# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# root=tk.Tk()
# root.title("Guest Application")
# root.geometry("300x200")
# root.resizable(False,False)
# def showerror():
#     tk.messagebox.showerror(title='Guest App error', message='Welcome to UREA granulation software !!!')
# btn=Button(root, text="show error", command=showerror)
# btn.place(height=50,width=150,x=75,y=70)
# root.mainloop()
#********************************#

# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# root=tk.Tk()
# root.title('Guest Application')
# root.geometry("500x350")
# root.resizable(False,False)
# def ask():
#     ans=tk.messagebox.askquestion(title='Guest question', message='Do you like python?')
#     if ans == 'yes':
#         lbl.configure(text="You like python")
#     else:
#         lbl.configure(text="You don't like python")
# btn=Button(root, text="Question", command=ask)
# btn.place(height=50,width=150,x=175,y=120)
# lbl=Label(root,text="Your answer will be shown here")
# lbl.place(height=50,width=175,x=175,y=180)
# cv = Canvas(root, bg = "white",bd=3,relief="groove")
# cv.place(height=100,width=220,x=140,y=10)
# img=tk.PhotoImage(file='C:/Users/Saberi/Desktop/GUI_TEST/Guest.png')
# canvas_img=cv.create_image(10,10,image=img, anchor=NW)
# root.mainloop()

#**********************************#
# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# root=tk.Tk()
# root.title('Guest Application')
# root.geometry("500x350")
# root.resizable(False,False)
# def ask():
#     ans=tk.messagebox.askokcancel(title='Guest-app ok cancel', message='Do you want to Quit?')
#     if ans :
#         root.destroy()
#     else:
#         pass
# btn=Button(root, text="Quit", command=ask)
# btn.place(height=50,width=150,x=175,y=130)
# cv = Canvas(root, bg = "white",bd=3,relief="groove")
# cv.place(height=100,width=220,x=140,y=10)
# img=tk.PhotoImage(file='C:/Users/Saberi/Desktop/GUI_TEST/Guest.png')
# canvas_img=cv.create_image(10,10,image=img, anchor=NW)
# root.mainloop()
#**********************************#
# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# root=tk.Tk()
# root.title('Guest Application')
# root.geometry("500x350")
# root.resizable(False,False)
# def ask():
#     ans=tk.messagebox.askyesno(title='Guest-app ok cancel', message='Do you want to Quit?')
#     if ans :
#         root.destroy()
#     else:
#         pass
# btn=Button(root, text="Quit", command=ask)
# btn.place(height=50,width=150,x=175,y=130)
# cv = Canvas(root, bg = "white",bd=3,relief="groove")
# cv.place(height=100,width=220,x=140,y=10)
# img=tk.PhotoImage(file='C:/Users/Saberi/Desktop/GUI_TEST/Guest.png')
# canvas_img=cv.create_image(10,10,image=img, anchor=NW)
# root.mainloop()
#**********************************#
# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox
# root=tk.Tk()
# root.title('Guest Application')
# root.geometry("500x350")
# root.resizable(False,False)
# def ask():
#     ans=tk.messagebox.askretrycancel(title='Guest-app ok cancel', message='Do you want to Quit?')
#     if ans :
#         root.destroy()
#     else:
#         pass
# btn=Button(root, text="Quit", command=ask)
# btn.place(height=50,width=150,x=175,y=130)
# cv = Canvas(root, bg = "white",bd=3,relief="groove")
# cv.place(height=100,width=220,x=140,y=10)
# img=tk.PhotoImage(file='C:/Users/Saberi/Desktop/GUI_TEST/Guest.png')
# canvas_img=cv.create_image(10,10,image=img, anchor=NW)
# root.mainloop()
#**********************************#

import tkinter as tk
from tkinter import *
from tkinter import messagebox
root=tk.Tk()
root.title('Guest Application')
root.geometry("500x350")
root.resizable(False,False)
def ask():
    ans=tk.messagebox.askyesnocancel(title='karakit yes no cancel', message='YES or No or CANCEL?')
    if ans:
        lbl.configure(text="You chose YES!")
    elif ans is None:
        lbl.configure(text="You chose CANCEL!")
    else:
        lbl.configure(text="You chose NO!")
def ask():
    ans=tk.messagebox.askyesno(title='Guest-app ok cancel', message='Do you want to Quit?')
    if ans :
        root.destroy()
    else:
        pass
btn=Button(root, text="ask question", command=ask)
btn.place(height=50,width=150,x=175,y=130)
lbl=Label(root,text="Your answer will be shown here",relief="groove")
lbl.place(height=50,width=200,x=150,y=200,)
cv = Canvas(root, bg = "white",bd=3,relief="groove")
cv.place(height=100,width=220,x=140,y=10)
img=tk.PhotoImage(file='C:/Users/Saberi/Desktop/GUI_TEST/Guest.png')
canvas_img=cv.create_image(10,10,image=img, anchor=NW)
btn=Button(root, text="Quit", command=ask)
btn.place(height=40,width=100,x=195,y=260)
root.mainloop()
