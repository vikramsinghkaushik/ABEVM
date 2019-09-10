import sys
import os
from tkinter import *
import tkinter
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename

root=Tk()
root.geometry("800x480")
#root.overrideredirect(1)
image = PhotoImage(file="D:\evm.png")
background1=Label(root, image=image)
background1.place(x=0,y=0)

aadharno = ""
passwordno= ""
Name=""

PARTYNAME = StringVar()
CANDIDATENAME = StringVar()
PARTYLOGO = StringVar()


             
def Restart():
    Exit=tkinter.messagebox.askyesno("Restart","Conform if you want to restart")
    if Exit>0:
        os.execl(sys.executable, os.path.abspath("‪Maingui.py"), *sys.argv)
    return
    
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
    background.place(x=0,y=0)
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
            admin.destroy()
            loginframe=Frame(root,height=480,width=800)
            loginframe.pack()
            background=Label(loginframe, image=image)
            background.place(x=0,y=0)
            restart = Button(loginframe, text=' X ', background='white', font=("Helvetica", 10,"bold"), command=Restart,)
            restart.place(x=771,y=2)


            def parties():
                loginframe.destroy()
                partiesframe=Frame(root,height=480,width=800)
                partiesframe.pack()
                background=Label(partiesframe, image=image)
                background.place(x=0,y=0)
                restart = Button(partiesframe, text=' X ', background='white', font=("Helvetica", 10,"bold"), command=Restart)
                restart.place(x=771,y=2)
                PartyInfoLabel = Label(partiesframe, text="PARTY INFORMATION", background='white',fg='Navy Blue', font=("Helvetica", 14,"bold"),width=20)
                PartyInfoLabel.place(x=80, y=155)
                PartyDetailLabel = Label(partiesframe, text="PARTIES DETAILS", background='white',fg='Navy Blue', font=("Helvetica", 14,"bold"),width=15)
                PartyDetailLabel.place(x=513, y=155)
                PartyNameLabel= Label(partiesframe, background='white', text="Party Name:", font=("Helvetica", 12,"bold"),width=10)
                PartyNameLabel.place(x=32, y=200)
                PartylogoLabel= Label(partiesframe, background='white', text="Party Logo:", font=("Helvetica", 12,"bold"),width=10)
                PartylogoLabel.place(x=30, y=250)
                PartylogoEntry= Entry(partiesframe, textvariable=PARTYLOGO, background='white', font=("Helvetica", 15,"bold"), width=15)
                PartylogoEntry.place(x=145, y=249)
                tree = ttk.Treeview(partiesframe, columns=("PartyID", "PartyName", "PartyLogo"), height=5)
                def Database():
                   conn = sqlite3.connect("partiesdatabse.db")
                   cursor = conn.cursor()
                   cursor.execute("CREATE TABLE IF NOT EXISTS `party` (party_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, partyname TEXT, partylogo BLOB)")
                   cursor.execute("SELECT * FROM `party` ORDER BY `party_id` ASC")
                   fetch = cursor.fetchall()
                   for data in fetch:
                       tree.insert('', 'end', values=(data))
                   cursor.close()
                   conn.close()


                def convertToBinaryData(filename):
                    with open(filename, 'rb') as file:
                        blobData = file.read()
                    return blobData
                    
                def SubmitData():
                    global Name
                    if  PARTYNAME.get() == "" or PARTYLOGO.get() == "":
                        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
                    else:
                        tree.delete(*tree.get_children())
                        conn = sqlite3.connect("partiesdatabse.db")
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO `party` (partyname, partylogo) VALUES(?, ?)", (str(PARTYNAME.get()), convertToBinaryData(PARTYLOGO.get())))
                        conn.commit()
                        cursor.execute("SELECT * FROM `party` ORDER BY `party_id` ASC")
                        fetch = cursor.fetchall()
                        for data in fetch:
                            tree.insert('', 'end', values=(data))
                        cursor.close()
                        conn.close()
                        PARTYNAME.set("")
                        PARTYLOGO.set("")
                        Name= ""

                def OnSelected(event):
                    global Name
                    curItem = tree.focus()
                    contents =(tree.item(curItem))
                    selecteditem = contents['values']
                    mem_id = selecteditem[0]
                    PARTYNAME.set("")
                    Name= ""
                    PARTYLOGO.set("Select Image")
                    PARTYNAME.set(selecteditem[1])

                def Partylogo():
                    name = askopenfilename(filetypes =(("Image File", "*.jpg"),("All Files","*.*")),title = "Choose a file.")
                    PARTYLOGO.set(name)

                def DeleteData():
                    global Name
                    if not tree.selection():
                        result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
                    else:
                        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
                        if result == 'yes':
                            curItem = tree.focus()
                            contents =(tree.item(curItem))
                            selecteditem = contents['values']
                            tree.delete(curItem)
                            conn = sqlite3.connect("partiesdatabse.db")
                            cursor = conn.cursor()
                            cursor.execute("DELETE FROM `PARTY` WHERE `PARTY_id` = %d" % selecteditem[0])
                            conn.commit()
                            cursor.close()
                            conn.close()
                            PARTYNAME.set("")
                            PARTYLOGO.set("")
                            Name= ""
                            
                Partylogobutton= Button(partiesframe, text=' Browse ', background='white', font=("Helvetica", 10,"bold"), command=Partylogo, width=10)
                Partylogobutton.place(x=270, y=249)
                Submitbutton= Button(partiesframe, text=' SUBMIT ', font=("Helvetica", 10,"bold"), command=SubmitData, width=10)
                Submitbutton.place(x=30, y=300)
                Deletebutton= Button(partiesframe, text=' DELETE ', font=("Helvetica", 10,"bold"), command=DeleteData, width=10)
                Deletebutton.place(x=270, y=300)

                tree.heading('PartyID', text="Party ID")
                tree.heading('PartyName', text=" Party Name ")
                tree.heading('PartyLogo', text=" Party Logo ")
                tree.column('#0', stretch=NO, minwidth=0, width=0)
                tree.column('#1', stretch=NO, minwidth=0, width=0)
                tree.column('#2', stretch=NO, minwidth=0, width=150)
                tree.column('#3', stretch=NO, minwidth=0, width=150)
                tree.place(x=450, y=190)
                tree.bind('<Double-Button-1>',OnSelected)


                Database()

                def press(value):
                    global Name
                    Name=Name+value
                    PARTYNAME.set(Name);
                def clear():
                    global Name
                    Name = ""
                    PARTYNAME.set("")
                    PARTYLOGO.set("")

                PartyNameEntry= Entry(partiesframe, textvariable=PARTYNAME, background='white', font=("Helvetica", 15,"bold"),width=19)
                PartyNameEntry.place(x=145, y=199)
                button1 = Button(partiesframe, text=' Q ',  font=("Helvetica", 15,"bold"), command=lambda: press('Q'), height=1, width=6) 
                button1.place(x=0, y=360) 
                button2 = Button(partiesframe, text=' W ',  font=("Helvetica", 15,"bold"), command=lambda: press('W'), height=1, width=6)
                button2.place(x=80, y=360) 
                button3 = Button(partiesframe, text=' E ',  font=("Helvetica", 15,"bold"), command=lambda: press('E'), height=1, width=6)
                button3.place(x=160, y=360) 
                button4 = Button(partiesframe, text=' R ',  font=("Helvetica", 15,"bold"), command=lambda: press('R'), height=1, width=6) 
                button4.place(x=240, y=360) 
                button5 = Button(partiesframe, text=' T ',  font=("Helvetica", 15,"bold"), command=lambda: press('T'), height=1, width=6) 
                button5.place(x=320, y=360)
                button6 = Button(partiesframe, text=' Y ',  font=("Helvetica", 15,"bold"), command=lambda: press('Y'), height=1, width=6)
                button6.place(x=400, y=360) 
                button7 = Button(partiesframe, text=' U ',  font=("Helvetica", 15,"bold"), command=lambda: press('U'), height=1, width=6)
                button7.place(x=480, y=360) 
                button8 = Button(partiesframe, text=' I ',  font=("Helvetica", 15,"bold"), command=lambda: press('I'), height=1, width=6) 
                button8.place(x=560, y=360) 
                button9 = Button(partiesframe, text=' O ' ,font=("Helvetica", 15,"bold"), command=lambda: press('O'), height=1, width=6)
                button9.place(x=640, y=360)
                button10 = Button(partiesframe, text=' P '   ,font=("Helvetica", 15,"bold"), command=lambda: press('P'), height=1, width=6)
                button10.place(x=720, y=360) 
                button11 = Button(partiesframe, text=' A ',  font=("Helvetica", 15,"bold"), command=lambda: press('A'), height=1, width=6) 
                button11.place(x=0, y=400) 
                button12 = Button(partiesframe, text=' S ',  font=("Helvetica", 15,"bold"), command=lambda: press('S'), height=1, width=6)
                button12.place(x=80, y=400) 
                button13 = Button(partiesframe, text=' D ', font=("Helvetica", 15,"bold"), command=lambda: press('D'), height=1, width=6)
                button13.place(x=160, y=400) 
                button14 = Button(partiesframe, text=' F ', font=("Helvetica", 15,"bold"), command=lambda: press('F'), height=1, width=6) 
                button14.place(x=240, y=400) 
                button15 = Button(partiesframe, text=' G ', font=("Helvetica", 15,"bold"), command=lambda: press('G'), height=1, width=6) 
                button15.place(x=320, y=400)
                button16 = Button(partiesframe, text=' H ',  font=("Helvetica", 15,"bold"), command=lambda: press('H'), height=1, width=6)
                button16.place(x=400, y=400) 
                button17 = Button(partiesframe, text=' J ',  font=("Helvetica", 15,"bold"), command=lambda: press('J'), height=1, width=6)
                button17.place(x=480, y=400) 
                button18 = Button(partiesframe, text=' K ',  font=("Helvetica", 15,"bold"), command=lambda: press('K'), height=1, width=6) 
                button18.place(x=560, y=400) 
                button19 = Button(partiesframe, text=' L ',  font=("Helvetica", 15,"bold"), command=lambda: press('L'), height=1, width=6)
                button19.place(x=640, y=400)
                button20 = Button(partiesframe, text=' Z ',  font=("Helvetica", 15,"bold"), command=lambda: press('Z'), height=1, width=6)
                button20.place(x=720, y=400) 
                button21 = Button(partiesframe, text=' X ',  font=("Helvetica", 15,"bold"), command=lambda: press('X'), height=1, width=6)
                button21.place(x=0, y=440)
                button22 = Button(partiesframe, text=' C ',  font=("Helvetica", 15,"bold"), command=lambda: press('C'), height=1, width=6)
                button22.place(x=80, y=440)
                button23 = Button(partiesframe, text=' V ', font=("Helvetica", 15,"bold"), command=lambda: press('V'), height=1, width=6)
                button23.place(x=160, y=440)
                space = Button(partiesframe, text=' SPACE ',font=("Helvetica", 15,"bold"), command=lambda: press(' ') ,height=1, width=13)
                space.place(x=240, y=440)
                button24 = Button(partiesframe, text=' B ', font=("Helvetica", 15,"bold"), command=lambda: press('B'), height=1, width=6)
                button24.place(x=400, y=440)
                button25 = Button(partiesframe, text=' N ', font=("Helvetica", 15,"bold"), command=lambda: press('N'), height=1, width=6)
                button25.place(x=480, y=440)
                button25 = Button(partiesframe, text=' M ', font=("Helvetica", 15,"bold"), command=lambda: press('M'), height=1, width=6)
                button25.place(x=560, y=440)
                exitbutton = Button(partiesframe, text='  CLEAR  ',  font=("Helvetica", 15,"bold"), command=clear, height=1, width=13) 
                exitbutton.place(x=640, y=440)
                clearbutton= Button(partiesframe, text=' UPDATE ', font=("Helvetica", 10,"bold"), width=10)
                clearbutton.place(x=150, y=300)

            parties = Button(loginframe, text=' Parties ', background='white', font=("Helvetica", 15,"bold"), command=parties, height=1, width=18)
            parties.place(x=425, y=220)

            def clearparties():
                result = tkMessageBox.askquestion('Delete Parties Record', 'Are you want to delete all parties record?', icon="warning")
                if result == 'yes':
                    conn = sqlite3.connect("partiesdatabse.db")
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM party")
                    conn.commit()
                    conn.close()
                        
            clearparties = Button(loginframe, text=' Clear Parties ', background='white', font=("Helvetica", 15,"bold"), command=clearparties, height=1, width=18)
            clearparties.place(x=425, y=300)

    
            logwelcomeLabel = Label(loginframe, background='white', text="Welcome To Admin Panel", font=("Helvetica", 22,"bold"),width=22)
            logwelcomeLabel.place(x=200, y=150)
            result = Button(loginframe, text=' Result ', background='white', font=("Helvetica", 15,"bold"), command=clear, height=1, width=18)
            result.place(x=145, y=220)
            clearresult = Button(loginframe, text=' Clear Result ', background='white', font=("Helvetica", 15,"bold"), command=clear, height=1, width=18)
            clearresult.place(x=145, y=300)

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
