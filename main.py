import tkinter as tk
from tkinter import Tk,ttk
from tkinter import *
from tkinter import messagebox
import pymysql
root=tk.Tk()
root.minsize(350, 450)
root.title("CRUD Operation ")
con=pymysql.Connect(host="localhost",user='root',password='1234',database='tkinterdb')
cur=con.cursor()

def save():
    name = nametext.get()
    course = namecourse.get()
    if name=="" and course=="":
        messagebox.showerror("Status","Please Enter Your Details ")
    else:
        s = "insert into student(name,course) values('" + name + "','" + course + "')"
        cur.execute(s)
        con.commit()
        messagebox.showinfo("Status","You Ragistration Sucess ")

def showdata():
    s="select * from student limit 0,10"
    cur.execute(s)
    d=cur.fetchall()
    id=""
    name=""
    course=""
    var.set("id\t name\t course")
    for i in range(0,len(d)):
        var.set(d[i])
        print(d[i])




def update():
    top=Toplevel(root)
    top.minsize(350,400)

    def fetch():
        try:
            getid = id.get()
            cur.execute("select * from student where id='" + getid + "'")
            d = cur.fetchone()
            a=0

            getname.set(d[1])
            getcourse.set(d[2])
            messagebox.showinfo("Status", "Data feched Sucessfully")

        except Exception as e:
            messagebox.showerror('Status',"Enter Your Correct Id ")
    def updatedata():
        getid = str(id.get())
        uname = course.get()
        cur.execute("select * from student where id='" + getid + "'")
        d = cur.fetchone()

        cur.execute("update student set course='"+uname+"' where id='"+getid+"'")
        con.commit()
        messagebox.showinfo('Status',"Data updated")
        top.destroy()

    def delete():
        try:
            getid=str(id.get())
            cur.execute("delete from student where id ='"+getid+"'")
            messagebox.showinfo("Status","Your Detail is deleted '"+getid+"'")
        except Exception as e :
            messagebox.showerror("Status","Enter you Correct ID")
    id=Entry(top)
    id.pack()
    getname=StringVar()
    name=Label(top,text="name",textvariable=getname)
    name.pack()

    getcourse=StringVar()
    course=Entry(top,textvariable=getcourse)
    course.pack()
    btn2 = Button(top, text="fetch", command=fetch)
    btn2.pack()
    btn=Button(top,text="update",command=updatedata)
    btn.pack()
    btn3 = Button(top, text="Delete", command=delete)
    btn3.pack()
    top.mainloop()


welcome= Label(root,text="Welcome to DhangarJi coding Plateform ",font="10" ,width="35", height="2",bg="pink",fg="Black")
welcome.place(x="15",y="10")

nameLable=Label(root,text="Name : ", height="2",fg="Black")
nameLable.place(x=15,y=50)
var=StringVar
nametext=Entry(root)
nametext.place(x=60,y=60)

courseLable=Label(root,text="Course :  ", height="2",fg="Black")
courseLable.place(x=15,y=80)
namecourse=Entry(root)
namecourse.place(x=60,y=90)

subbtn=Button(text="Submit", command=save)
subbtn.place(x=35,y=130)




subbtn1= Button(text="Show Data",command=showdata)
subbtn1.place(x=140,y=130)

btn1= Button(text="update",command=update)
btn1.place(x=230,y=130)
sp=Spinbox(root,from_=0, to=56)
sp.place(x=50,y=160)

var=StringVar()
dis=Label(root,text="Show all the data", bg='red',width="40",height='12', textvariable=var)
dis.place(x=40,y=190)











root.mainloop()