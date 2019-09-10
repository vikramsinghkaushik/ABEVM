import sys
import os
from tkinter import *
import tkinter
import tkinter.messagebox as tk1MessageBox

root=Tk()
root.geometry("800x480")
root.overrideredirect(1)
image = PhotoImage(file="D:\evm.png")
background1=Label(root, image=image)
background1.place(x=0,y=0)

aadharno = ""
passwordno= ""

def Restart():
    os.execl(sys.executable, os.path.abspath("‪Maingui.py"), *sys.argv)

mainframe=Frame(root,height=480,width=800)
mainframe.pack()
background=Label(mainframe, image=image)
background.place(x=0,y=0)

Labelmain = Label(mainframe, background='white', text="Enter Aadhar Number :", font=("Helvetica", 19,"bold"),width=18)
Labelmain.place(x=84, y=150)

def press(num):
        global aadharno
        aadharno = aadharno + str(num)
        number.set(aadharno)
def submit():
        global aadharno
        aadharno = ""
        number.set("Invalid")
def clear(): 
	global aadharno 
	aadharno = ""
	number.set("")
number = StringVar() 
aadharno_field = Entry(mainframe, textvariable=number, background='white', font=("Helvetica", 19,"bold"),width=23) 
aadharno_field.place(x=370,y=150) 
button1 = Button(mainframe, text=' 1 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(1), height=1, width=7) 
button1.place(x=85, y=205) 
button2 = Button(mainframe, text=' 2 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(2), height=1, width=7) 
button2.place(x=215, y=205) 
button3 = Button(mainframe, text=' 3 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(3), height=1, width=7) 
button3.place(x=345, y=205) 
button4 = Button(mainframe, text=' 4 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(4), height=1, width=7) 
button4.place(x=475, y=205) 
button5 = Button(mainframe, text=' 5 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(5), height=1, width=7) 
button5.place(x=605, y=205) 
button6 = Button(mainframe, text=' 6 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(6), height=1, width=7) 
button6.place(x=85, y=270) 
button7 = Button(mainframe, text=' 7 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(7), height=1, width=7) 
button7.place(x=215, y=270) 
button8 = Button(mainframe, text=' 8 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(8), height=1, width=7) 
button8.place(x=345, y=270) 
button9 = Button(mainframe, text=' 9 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(9), height=1, width=7) 
button9.place(x=475, y=270) 
button0 = Button(mainframe, text=' 0 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(0), height=1, width=7) 
button0.place(x=605, y=270) 
enter = Button(mainframe, text=' Submit ', background='white', font=("Helvetica", 15,"bold"), command=submit, height=1, width=29) 
enter.place(x=343, y=330) 
clear = Button(mainframe, text=' Clear ', background='white', font=("Helvetica", 15,"bold"), command=clear, height=1, width=18) 
clear.place(x=85, y=330)

def admin():
    mainframe.destroy()
    
    admin=Frame(root,height=480,width=800)
    admin.pack()
    background=Label(admin, image=image)
    background.place(x=1,y=1)
    restart = Button(admin, text=' X ', background='white', font=("Helvetica", 10,"bold"), command=Restart,)
    restart.place(x=771,y=2)
    passwordLabel = Label(admin, background='white', text="Enter Password :", font=("Helvetica", 19,"bold"),width=15)
    passwordLabel.place(x=100, y=165)
    def press(num):
        global passwordno
        passwordno = passwordno + str(num)
        password.set(passwordno)
    def clear():
        global passwordno
        passwordno = ""
        password.set("")
    def login():
        global passwordno
        if passwordno=='3198':
            passwordno= ""
            password.set("")
        else:
            passwordno = ""
            password.set("")
            tk1MessageBox.showerror( 'Message','Invalid Password!')      
    password = StringVar()
    passwordno_field = Entry(admin, textvariable=password, background='white', font=("Helvetica", 19,"bold"),width=23)
    passwordno_field.place(x=340, y=167)
    abutton1 = Button(admin, text=' 1 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(1), height=1, width=7)
    abutton1.place(x=85, y=215)
    abutton2 = Button(admin, text=' 2 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(2), height=1, width=7)
    abutton2.place(x=215, y=215)
    abutton3 = Button(admin, text=' 3 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(3), height=1, width=7)
    abutton3.place(x=345, y=215)
    abutton4 = Button(admin, text=' 4 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(4), height=1, width=7)
    abutton4.place(x=475, y=215)
    abutton5 = Button(admin, text=' 5 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(5), height=1, width=7)
    abutton5.place(x=605, y=215)
    abutton6 = Button(admin, text=' 6 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(6), height=1, width=7)
    abutton6.place(x=85, y=270)
    abutton7 = Button(admin, text=' 7 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(7), height=1, width=7)
    abutton7.place(x=215, y=270)
    abutton8 = Button(admin, text=' 8 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(8), height=1, width=7)
    abutton8.place(x=345, y=270)
    abutton9 = Button(admin, text=' 9 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(9), height=1, width=7)
    abutton9.place(x=475, y=270)
    abutton0 = Button(admin, text=' 0 ', background='white', font=("Helvetica", 15,"bold"), command=lambda: press(0), height=1, width=7)
    abutton0.place(x=605, y=270)
    alogin = Button(admin, text=' Log In ', background='white', font=("Helvetica", 15,"bold"),command=login, height=1, width=29)
    alogin.place(x=343, y=325)
    aclear = Button(admin, text=' Clear ', background='white', font=("Helvetica", 15,"bold"), command=clear, height=1, width=18)
    aclear.place(x=85, y=325)
setting = Button(mainframe, text='ADMIN', command=admin,background='white', font=("Helvetica", 10,"bold"))
setting.place(x=746, y=452)

root.mainloop()
