# import tkinter as tk
# from  tkinter import *
# root=tk.Tk()
# root.geometry("300x200")
# root.resizable(False,False)
# root.title('spinbox Guest-co')
# def agechanged():
#     lblAge.configure(text="Your age is: " + spnAge.get() + " years")
# intAge=IntVar
# spnAge=Spinbox(root, from_=18, to = 99 ,textvariable=intAge, command=agechanged)
# spnAge.place(height=20,width=50,x=110,y=80)
# lblAge=Label(root, text="How old are You?")
# lblAge.place(height=20,width=120,x=100,y=40)
# root.mainloop()
#*******************************************#
import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.geometry("300x200")
root.resizable(False,False)
root.title('spinbox Guest')
def seasonchanged():
    lblSeason.configure(text="فصل مورد علاقه شما: " + spnSeason.get()+" است")
strSeason=StringVar
seasons=['بهار','تابستان','پاییز','زمستان']
spnSeason=Spinbox(root, values=seasons ,textvariable=strSeason, command=seasonchanged)
spnSeason.place(height=20,width=100,x=110,y=80)
lblSeason=Label(root, text="فصل مورد علاقه شما چیست؟")
lblSeason.place(height=20,width=200,x=70,y=40)
root.mainloop()
#*******************************************#
