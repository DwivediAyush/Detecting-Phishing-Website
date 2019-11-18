from tkinter import *
import PIL
import sqlite3 as sql
import run
from PIL import ImageTk, Image
from tkinter import filedialog
import os

scr=Tk()
scr.geometry('1200x800+0+0')
def retrieve_input():
    global us
    input1=us.get()
    print(input1)
    out=run.run(input1)
    print(out)
    if(out=="Warning The website is harmfull for you"):
        v1 = StringVar()
        v1.set(out)
        photo = r"C:\Users\admin\Downloads\warning.png"
        #print(v1)
        openfn(photo)

        l2 = Label(f, text='Phishing / Not Phishing', textvariable=v1, font=('times', 20, 'bold'), bg='white', fg='red')
        l2.place(x=500, y=300)
        #print('done')
    else:
        v1 = StringVar()
        v1.set(out)
        photo = r"C:\Users\admin\Downloads\ok_image.png"
        openfn(photo)

        # print(v1)
        l2 = Label(f, text='Phishing / Not Phishing', textvariable=v1, font=('times', 20, 'bold'), bg='white',fg='red')
        l2.place(x=500, y=300)
        #print('done else')



scr.geometry("550x300+300+150")
scr.resizable(width=True, height=True)

def openfn(y):
    filename = y
    open_img(filename)
def open_img(x):
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(scr, image=img)
    panel.image = img
    panel.pack()

#btn = Button(root, text='open image', command=open_img).pack()


l=Label(scr,text="Phishing Website Detection",font=('times',20,'bold'),bg='blue',fg='yellow')
l.pack(side=TOP,fill=X)
f=Frame(scr,bg='orange')
f.pack(fill=BOTH,expand=12)
v=StringVar()
#v1=StringVar()
#v1.set('lol')
l1=Label(f,text='  Write The Website  ',font=('times',20,'bold'),bg='white',fg='black')
l1.place(x=300,y=100)
#l2=Label(f,text='Phishing / Not Phishing',textvariable=v1,font=('times',20,'bold'),bg='red',fg='yellow')
#l2.place(x=400,y=300)
us=Entry(f,font=('times',20,'bold'),bg='white',fg='black',textvariable=v,width=50)
us.place(x=600,y=100)
#ps=Entry(f,font=('times',20,'bold'),bg='blue',fg='yellow',textvariable=v1)
#ps.place(x=500,y=300)
b1=Button(f,text='Predict',font=('times',20,'bold'),command=retrieve_input)
b1.place(x=700,y=200)
scr.mainloop()





