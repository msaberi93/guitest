# import tkinter as tk
# from  tkinter import *
# root=tk.Tk()
# root.title("Guest Application")
# root.geometry("300x220")
# root.resizable(False,False)
# lst=Listbox(root)
# lst.place(height=150,width=100,x=100,y=30)
# lst.insert(1, "آنالوگ")
# lst.insert(2, "دیجیتال")
# lst.insert(3, "نرم افزار")
# lst.insert(4, "برنامه نویسی")
# lst.insert(5, "AVR")
# lst.insert(6, "ARM")
# lst.insert(7, "Rasbery Pie")
# lst.insert(8, "تجهیزات پزشکی")
# lst.insert(9,"دانه بندی اوره")
# root.mainloop()

#**************************************#
# import tkinter as tk
# from  tkinter import *
# root=tk.Tk()
# root.title("Guest Application")
# root.geometry("320x220")
# root.resizable(False,False)
# def show(event):
#     itemnumber = lst.curselection()
#     lblNumber.configure(text=itemnumber)
# lst=Listbox(root)
# lst.place(height=150,width=100,x=100,y=30)
# lst.insert(1, "آنالوگ")
# lst.insert(2, "دیجیتال")
# lst.insert(3, "نرم افزار")
# lst.insert(4, "برنامه نویسی")
# lst.insert(5, "دانه بندی اوره")
# lblNumber=Label(root, text="Number")
# lblNumber.place(height=10,width=60,x=100,y=10)
# # lst.bind('<Double-1>', show)
# lst.bind('<<ListboxSelect>>', show)
# root.mainloop()

#****************************************#
# import tkinter as tk
# from  tkinter import *
# root=tk.Tk()
# root.title("Guest Application")
# root.geometry("300x220")
# root.resizable(False,False)
# def show(event):
#     itemnumber = lst.curselection()
#     lblNumber.configure(text=itemnumber)
# categories=("آنالوگ","دیجیتال","نرم افزار","برنامه نویسی","دانه بندی اوره")
# categories_var = tk.StringVar(value=categories)
# lst=Listbox(root,listvariable=categories_var)
# lst.place(height=150,width=100,x=100,y=30)
# lblNumber=Label(root, text="Number")
# lblNumber.place(height=10,width=60,x=100,y=10)
# lst.bind('<<ListboxSelect>>', show)
# root.mainloop()

#*********************************************#
import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.title("Guest Application")
root.geometry("320x220")
root.resizable(False,False)
def show(event):
    itemnumber = lst.curselection()
    itemname=lst.get(itemnumber)
    lblName.configure(text=itemname)
categories=("آنالوگ","دیجیتال","نرم افزار","برنامه نویسی","دانه بندی اوره")
categories_var = tk.StringVar(value=categories)
lst=Listbox(root,listvariable=categories_var)
lst.place(height=150,width=100,x=100,y=40)
lblName=Label(root, text="Item")
lblName.place(height=20,width=100,x=100,y=10)
lst.bind('<<ListboxSelect>>', show)
root.mainloop()

