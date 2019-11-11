from tkinter import *
import sqlite3 as sql
scr=Tk()
scr.geometry('1200x800+0+0')
def retrieve_input():
    input1=v.get()
l=Label(scr,text="Phishing Website Detection",font=('times',20,'bold'),bg='blue',fg='yellow')
l.pack(side=TOP,fill=X)
f=Frame(scr,bg='orange')
f.pack(fill=BOTH,expand=12)
v=StringVar()
v1=StringVar()
#v1.set('lol')
l1=Label(f,text='Write The Website',font=('times',20,'bold'),bg='blue',fg='yellow')
l1.place(x=200,y=100)
l2=Label(f,text='Phishing / Not Phishing',textvariable=v1,font=('times',20,'bold'),bg='red',fg='yellow')
l2.place(x=400,y=300)
us=Entry(f,font=('times',20,'bold'),bg='blue',fg='yellow',textvariable=v)
us.place(x=500,y=100)
#ps=Entry(f,font=('times',20,'bold'),bg='blue',fg='yellow',textvariable=v1)
#ps.place(x=500,y=300)
b1=Button(f,text='Predict',font=('times',20,'bold'),command=lambda:retrieve_input)
b1.place(x=400,y=200)
scr.mainloop()





#input1 = website name
#v1= phishing or not print
