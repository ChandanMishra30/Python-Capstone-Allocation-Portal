from tkinter import *
from tkinter import messagebox
#import random
import time
import sqlite3

    
root = Tk()
root.geometry("800x450")
root.title("Capstone Allocation Portal")
list1 = ['Wifi Based Secure Wireless Communication Using RSA','Android Task Monitoring','Automated Canteen Ordering System using Android','RFID Based Automatic Traffic Violation Ticketing','Sports Events Management Platform for Colleges','Secure Online Auction System','School Security System (SSS) using RFID','RFID Parking System Using Android','Quality checking using image processing','Orange Fruit Recognition Using Image Segmentation','Optical character extraction under different illumination conditions','Filtering political sentiment in social media from textual information','Evaluation of Academic Performance of Students with Fuzzy Logic','E Authentication System Using QR Code & OTP','Document Sentiment Analysis Using Opinion Mining','Diabetic Retinopathy Detection From Retinal Images','Cursor Movement On Object Motion','Crime Rate Prediction Using K Means','Cooking Recipe Rating Based On Sentiment Analysis','Brain Tumor Detection Using Image Segmentation','Android Smart Ticketing Using Rfid','Android Battery Saver System','Android Based Encrypted SMS System','Advanced Tour Guide']

def d(event):
    
    index=list2.curselection()[0]
    selected_tuple=list2.get(index)
        
def superv():
    framenull.pack_forget()
    studentframe.pack_forget()  
    signinframe.pack_forget()
    loginframe.pack_forget()
    signinframe1.pack_forget()
    loginframe1.pack_forget()
    afterlogin.pack_forget()
    supervframe.pack()
    suplogin.pack_forget()
    whours.pack_forget()
    

def student():
    framenull.pack_forget()
    signinframe.pack_forget()
    loginframe.pack_forget()
    signinframe1.pack_forget()
    loginframe1.pack_forget()    
    supervframe.pack_forget()
    afterlogin.pack_forget()
    studentframe.pack() 
    suplogin.pack_forget()
    whours.pack_forget()
    

def login():
    return None
    
def signin():
    framenull.pack_forget()
    studentframe.pack_forget()   
    loginframe.pack_forget()
    signinframe1.pack_forget()
    loginframe1.pack_forget()
    supervframe.pack_forget()
    afterlogin.pack_forget()
    signinframe.pack()
    suplogin.pack_forget()
    whours.pack_forget()

def viewall():
    conn=sqlite3.connect("projec.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM projec")
    row=cur.fetchall()
    conn.close()
    return row  
        
def reject():
     messagebox.showinfo("tite","student selected")
     list2.delete(0,END)
def view():
    list2.delete(0,END)
    for row in viewall():
        list2.insert(END,row)
    
def showlogin():
    framenull.pack_forget()
    studentframe.pack_forget()
    signinframe1.pack_forget()
    loginframe1.pack_forget()
    signinframe.pack_forget()
    supervframe.pack_forget()
    afterlogin.pack_forget()
    loginframe.pack()
    suplogin.pack_forget()
    whours.pack_forget()

    
def signin1():
    whours.pack_forget()
    supervframe.pack_forget()
    framenull.pack_forget()
    studentframe.pack_forget()  
    signinframe.pack_forget()
    loginframe.pack_forget()
    loginframe1.pack_forget()
    afterlogin.pack_forget()
    suplogin.pack_forget()
    whours.pack_forget() 
    signinframe1.pack()   
def work_hours():
    supervframe.pack_forget()
    framenull.pack_forget()
    studentframe.pack_forget()  
    signinframe.pack_forget()
    loginframe.pack_forget()
    signinframe.pack_forget()
    loginframe1.pack_forget()
    afterlogin.pack_forget()
    suplogin.pack_forget() 
    whours.pack()      
def showlogin1():
    whours.pack_forget()
    supervframe.pack_forget()
    framenull.pack_forget()
    studentframe.pack_forget()  
    signinframe.pack_forget()
    loginframe.pack_forget()
    signinframe1.pack_forget()
    afterlogin.pack_forget()
    suplogin.pack_forget()
    loginframe1.pack()
def work():
    return None

def create():
    name=name1.get()
    passw=pass1.get()
    mobno=mobno1.get()
    emailid=emailid1.get()
    spec=spec1.get()
    regno=regno1.get()
    conn=sqlite3.connect('student.db')
    with conn:
        
        cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs student (name TEXT , passw TEXT , mobno INTEGER , emailid TEXT, special TEXT , regno INTEGER )")
    cur.execute("INSERT INTO student VALUES (?,?,?,?,?,?)",(name,passw,mobno,emailid,spec,regno))
    conn.commit()
    messagebox.showinfo("title","user created")
    
def create1():
    name=name2.get()
    passw=pass2.get()
    mobno=mobno2.get()
    emailid=emailid2.get()
    spec=spec2.get()
    uid0=uid.get()
    conn=sqlite3.connect('svisor.db')
    with conn:
        
        cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs svisor (name TEXT , passw TEXT , mobno INTEGER , emailid TEXT, special TEXT , uid INTEGER )")
    cur.execute("INSERT INTO svisor VALUES (?,?,?,?,?,?)",(name,passw,mobno,emailid,spec,uid0))
    conn.commit()
    messagebox.showinfo("title","user created")
    


def home():
    whours.pack_forget()
    framenull.pack()
    studentframe.pack_forget()  
    signinframe.pack_forget()
    loginframe.pack_forget()
    signinframe1.pack_forget()
    loginframe1.pack_forget()
    supervframe.pack_forget()
    afterlogin.pack_forget()
    suplogin.pack_forget()
def after_login():
    name=loginname2.get()
    passw=loginpass2.get()
    conn=sqlite3.connect('student.db')
    with conn:
        
        cur=conn.cursor()
    find_user=("SELECT * FROM student WHERE name=? AND passw=? ")
    cur.execute(find_user,[(name),(passw)])
    result = cur.fetchall()

    if result:
        act()
    else:
        messagebox.showerror("title","wrong user")
def sub():
    
    project=e4.get()
    name=loginname2.get()
    conn=sqlite3.connect('projec.db')
    with conn:
        
        cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs projec (name Text,project TEXT )")
    cur.execute("INSERT INTO projec VALUES (?,?)",(name,project))
    conn.commit()
    messagebox.showinfo("title","project selected done")

    
    

def act():
    whours.pack_forget()
    afterlogin.pack()
    framenull.pack_forget()
    studentframe.pack_forget()  
    signinframe.pack_forget()
    loginframe.pack_forget()
    signinframe1.pack_forget()
    loginframe1.pack_forget()
    supervframe.pack_forget()
    suplogin.pack_forget()

def sup_login():
    name=loginname.get()
    passw=loginpass.get()
    conn=sqlite3.connect('svisor.db')
    with conn:
        
        cur=conn.cursor()
    find_user=("SELECT * FROM svisor WHERE name=? AND passw=? ")
    cur.execute(find_user,[(name),(passw)])
    result = cur.fetchall()

    if result:
        act1()
    else:
        messagebox.showerror("title","wrong user")
    

def act1():
    whours.pack_forget()
    afterlogin.pack_forget()
    framenull.pack_forget()
    studentframe.pack_forget()  
    signinframe.pack_forget()
    loginframe.pack_forget()
    signinframe1.pack_forget()
    loginframe1.pack_forget()
    supervframe.pack_forget()
    suplogin.pack()
    
loginname=StringVar()
loginpass=StringVar()
signinname=StringVar()
signinpass=StringVar()
name2=StringVar()
pass2=StringVar()
mobno2=StringVar()
emailid2=StringVar()
uid=StringVar()
spec2=StringVar()

loginname2=StringVar()
loginpass2=StringVar()
name1=StringVar()
pass1=StringVar()
mobno1=StringVar()
emailid1=StringVar()
spec1=StringVar()
regno1=StringVar()
e4=StringVar()
e5=StringVar()
name3=[]
name3.append(loginname2)



frame00=Frame(root,width=800,height=70)
frame00.pack(side=TOP)
frame00.configure(bg='#8e1637')
Button(frame00,width=15,height=2,text='HOME',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=home).place(x=520,y=20)



frame0=Frame(root,width=800,height=450)
frame0.pack()

frame0.configure(bg='#eae6e9')
Label(frame0,text="Capstone Allocation Portal",foreground='#383f3d',font=('fixedsys',18),bg='#eae6e9').place(x=160,y=25)
x=Button(frame0,width=15,height=2,text='Student',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=student).place(x=180,y=160)
Button(frame0,width=15,height=2,text='Supervisor',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=superv).place(x=400,y=160)

frame=Frame(root,width=800,height=310)
frame.pack()
frame.configure(bg='#eae6e9')
Label(frame,text="Student",foreground='#383f3d',font=('fixedsys',18),bg='#eae6e9').place(x=250,y=25)
Button(frame,width=15,height=2,text='LogIn',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=showlogin).place(x=150,y=140)
Button(frame,width=15,height=2,text='New User',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=signin).place(x=400,y=140)
#Button(frame,width=20,height=2,text='Request for Supervisor',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=request).place(x=450,y=160)

frame1=Frame(root,width=800,height=330)
frame1.pack()
frame1.configure(bg='#eae6e9')

Label(frame1,text="User Login",foreground='#383f3d',font=('fixedsys',18),bg='#eae6e9').place(x=190,y=25)
Label(frame1,text="Username",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=80)
Entry(frame1,font='Ubuntu',bd=0,textvariable=loginname2).place(x=284,y=89)

Label(frame1,text="Password",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=137)
Entry(frame1,font='Ubuntu',bd=0,textvariable=loginpass2,show="*").place(x=284,y=146)
        
Button(frame1,width=15,height=2,text='LogIn',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=after_login).place(x=190,y=200)
        
Button(frame1,width=15,height=2,text='Sign Up',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=signin).place(x=400,y=200)
        
frame2=Frame(root,width=800,height=330)
frame2.pack()
frame2.configure(bg='#eae6e9')
       
Label(frame2,text="Sign Up",foreground='#383f3d',font=('fixedsys',18),bg='#eae6e9').place(x=190,y=25)
        
Label(frame2,text="Username",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=70)
Entry(frame2,font='Ubuntu',bd=0,textvariable=name1).place(x=284,y=75)

Label(frame2,text="Password",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=100)
Entry(frame2,font='Ubuntu',bd=0,textvariable=pass1).place(x=284,y=105)

Label(frame2,text="Mobile_No",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=130)
Entry(frame2,font='Ubuntu',bd=0,textvariable=mobno1).place(x=284,y=135)

Label(frame2,text="EmailId",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=160)
Entry(frame2,font='Ubuntu',bd=0,textvariable=emailid1).place(x=284,y=165)

Label(frame2,text="Specialization",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=190)
Entry(frame2,font='Ubuntu',bd=0,textvariable=spec1).place(x=284,y=195)

Label(frame2,text="Reg. No",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=220)
Entry(frame2,font='Ubuntu',bd=0,textvariable=regno1).place(x=284,y=225)

          
Button(frame2,width=15,height=2,text='Create',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=create).place(x=190,y=260)
        
Button(frame2,width=15,height=2,text='Back',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=showlogin).place(x=400,y=260)



frame3=Frame(root,width=800,height=330)
frame.pack()
frame3.configure(bg='#eae6e9')
Label(frame3,text="Supervisor",foreground='#383f3d',font=('fixedsys',18),bg='#eae6e9').place(x=250,y=25)
Button(frame3,width=15,height=2,text='LogIn',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=showlogin1).place(x=180,y=110)
Button(frame3,width=15,height=2,text='New User',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=signin1).place(x=400,y=110)
Button(frame3,width=20,height=2,text='Working Hours',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=work_hours).place(x=277,y=200)
#Button(frame3,width=20,height=2,text='Select Student',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=request1).place(x=380,y=245)


frame4=Frame(root,width=800,height=330)
frame4.pack()
frame4.configure(bg='#eae6e9')

Label(frame4,text="User Login",foreground='#383f3d',font=('fixedsys',18),bg='#eae6e9').place(x=190,y=25)
Label(frame4,text="Username",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=80)
Entry(frame4,font='Ubuntu',bd=0,textvariable=loginname).place(x=284,y=89)

Label(frame4,text="Password",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=137)
Entry(frame4,font='Ubuntu',bd=0,textvariable=loginpass,show="*").place(x=284,y=146)
        
Button(frame4,width=15,height=2,text='LogIn',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=sup_login).place(x=190,y=200)
        
Button(frame4,width=15,height=2,text='Sign Up',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=signin1).place(x=400,y=200)
        
frame5=Frame(root,width=800,height=330)
frame5.pack()
frame5.configure(bg='#eae6e9')
       
Label(frame5,text="Sign Up",foreground='#383f3d',font=('fixedsys',18),bg='#eae6e9').place(x=190,y=25)
        
Label(frame5,text="Username",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=70)
Entry(frame5,font='Ubuntu',bd=0,textvariable=name2).place(x=284,y=75)

Label(frame5,text="Password",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=100)
Entry(frame5,font='Ubuntu',bd=0,textvariable=pass2).place(x=284,y=105)

Label(frame5,text="Mobile_No",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=130)
Entry(frame5,font='Ubuntu',bd=0,textvariable=mobno2).place(x=284,y=135)

Label(frame5,text="EmailId",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=160)
Entry(frame5,font='Ubuntu',bd=0,textvariable=emailid2).place(x=284,y=165)

Label(frame5,text="Specialization",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=190)
Entry(frame5,font='Ubuntu',bd=0,textvariable=spec2).place(x=284,y=195)

Label(frame5,text="UID",foreground='#9f9b9c',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=220)
Entry(frame5,font='Ubuntu',bd=0,textvariable=uid).place(x=284,y=225)

          
Button(frame5,width=15,height=2,text='Create',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=create1).place(x=190,y=260)
Button(frame5,width=15,height=2,text='Back',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=showlogin1).place(x=400,y=260)



#===========================================================================================================================



frame6=Frame(root,width=800,height=330)
frame6.pack()
frame6.configure(bg='#eae6e9')

Label(frame6,text="Name",foreground='Black',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=40)
Entry(frame6,font='Ubuntu',bd=0,textvariable=loginname2).place(x=284,y=40)

Label(frame6,text="Choose A Course",foreground='Black',font=('Ubuntu',11),bg='#eae6e9').place(x=190,y=70)

droplist=OptionMenu(frame6,e4,*list1)
droplist.config(width=20)
e4.set("Select the Project")  
droplist.place(x=330,y=70)

Checkbutton(frame6,text='Request For Supervisor').place(x=250 ,y=120)
Button(frame6,width=15,height=2,text='Submit',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=sub).place(x=250,y=190)


frame7=Frame(root,width=800,height=330)
frame7.pack()
frame7.configure(bg='#eae6e9')
Label(frame7,text="Selected Student",foreground='Black',font=('fixedsys',20),bg='#eae6e9').place(x=190,y=40)
list2=Listbox(frame7,height=7,width=59)
list2.place(x=190,y=120)
list2.bind('<<ListboxSelect>>',d)


Button(frame7,width=15,height=2,text='View student',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=view).place(x=200,y=270
                                                                                                                                                 )
Button(frame7,width=15,height=2,text='Select student',activebackground='#8e1641',foreground='white',bg='#8e1637',relief='flat',command=reject).place(x=450,y=270)




frame8=Frame(root,width=1280,height=768)
frame8.pack()
frame8.configure(bg='#eae6e9')
Label(frame8,text="WORKING HOURS OF DIFFERENT DEPARTMENTS",font=('Ubuntu',20),fg='navy blue',bg='#eae6e9').place(x=80,y=78)
Label(frame8,text="============================================================",font=('Ubuntu',15),bg='#eae6e9').place(x=65,y=110)
Label(frame8,text="Department",font=('Ubuntu',17,'bold'),bg='#eae6e9').place(x=150,y=150)
Label(frame8,text="Time",font=('Ubuntu',17),bg='#eae6e9').place(x=510,y=150)
Label(frame8,text="Civil Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=200)
Label(frame8,text="10:00 - 12:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=200)
Label(frame8,text="Biomedical Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=230)
Label(frame8,text="14:00 - 17:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=230)
Label(frame8,text="Computer Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=260)
Label(frame8,text="10:00 - 16:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=260)
Label(frame8,text="Aerospace Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=290)
Label(frame8,text="11:00 - 14:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=290)
Label(frame8,text="Electronic Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=320)
Label(frame8,text="10:00 - 12:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=320)
Label(frame8,text="Automobile Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=350)
Label(frame8,text="09:00 - 15:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=350)
Label(frame8,text="Mechanical Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=380)
Label(frame8,text="10:00 - 14:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=380)
Label(frame8,text="Mining Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=410)
Label(frame8,text="11:00 - 13:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=410)
Label(frame8,text="Aeronautics",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=440)
Label(frame8,text="13:00 - 15:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=440)
Label(frame8,text="Petroleum Engineering",font=('Ubuntu',13),bg='#eae6e9').place(x=150,y=470)
Label(frame8,text="14:00 - 17:00",font=('Ubuntu',13),bg='#eae6e9').place(x=500,y=470)





#================================================================================================================
framenull=frame0    
studentframe=frame        
loginframe=frame1
signinframe=frame2
supervframe=frame3
loginframe1=frame4
signinframe1=frame5
afterlogin=frame6
suplogin=frame7
whours=frame8
        
        
root.mainloop()


