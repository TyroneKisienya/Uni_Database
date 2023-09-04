import tkinter
from tkinter import *
from tkinter import messagebox as mbox
import mysql.connector

root = Tk()
root.geometry("2048x1024")
root.title("SKAI TECHNOLOGIES")

fn = StringVar()
fn2 = StringVar()
fn3 = StringVar()
fn4 = StringVar()
fn5 = StringVar()
fn6 = StringVar()
var = StringVar()
var1= StringVar()
var2 = StringVar()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Soft063#",
  database="Form"
)

mycursor = mydb.cursor()

def database():
    ent = fn.get()
    ent1 = var2.get()
    gen = var1.get()
    ent2 = fn2.get()
    ent3 = fn3.get()
    ent4 = fn4.get()
    ent5 = fn5.get()
    ent6 = fn6.get()
    local = var.get()
    sql = "INSERT INTO Newborns (ChildID, Gender, FirstName, Surname, MiddleName, ParentID, Physical_Address, Email_Address,  Week) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
    val = (ent, gen, ent2, ent3, ent4, ent5, local, ent6, ent1)

    mycursor.execute(sql, val)
    mydb.commit()

    if ent == "" or gen == "" or ent2 == "" or ent3 == "" or ent4 =="" or ent5 =="" or ent6 == "" or local =="":
     mbox.showerror( "Missed Entry","All fields are required!")            
    else:
        mbox.showinfo("Success", "Registration successful. Thank you!")

def login():
    root.destroy()
    import Login

label = Label(root, text = "REGISTER", width = 43, relief = "solid", font = ("bold",20))
label.place(x = 440, y = 110)

register = Button(root, text = "LOGIN", relief = RAISED,fg = "black", bg = "light blue", font = ("bold", 15), command = login)
register.place(x = 10, y = 60)

ID = Label(root, text = "CHILD ID: ", font = ("arial",10))
ID.place(x = 450, y = 220)

entry = Entry(root, textvar = fn)
entry.place(x = 515, y = 220)

week = Label(root, text = "BIRTH WEEK: ", font = ("arial", 10))
week.place(x = 685, y = 220)

week = ['1', '2', '3', '4']
droplist = OptionMenu(root, var2, *week)
droplist.configure(width = 3, font = ("arial", 10), relief = GROOVE, bg = "white")
droplist.place(x = 775, y = 216)

gender = Label(root, text = "SEX: ", font = ("arial", 10))
gender.place(x = 940, y = 220)

sex = ['Male', 'Female']
droplist = OptionMenu(root, var1, *sex)
droplist.configure(width = 5, font = ("arial", 10), relief = GROOVE, bg = "white")
droplist.place(x = 980, y = 215)

parent = Label(root, text = "PARENT: ",relief = "solid",width = 43,font = ("bold",20))
parent.place(x = 440, y = 300)

first_name = Label(root, text = "FIRST NAME: ",font = ("arial",10))
first_name.place(x = 450, y = 400)

entry2 = Entry(root,textvar = fn2)
entry2.place(x = 540, y = 400)

sur_name = Label(root, text = "SURNAME: ",font = ("arial",10))
sur_name.place(x = 690, y = 400)

entry3 = Entry(root, textvar = fn3)
entry3.place(x = 765, y = 400)

last_name = Label(root, text = "MIDDLE NAME: ",font = ("arial",10))
last_name.place(x = 900, y = 400)

entry4 = Entry(root, textvar = fn4)
entry4.place(x = 1000, y = 400)

ID = Label(root, text = "PARENT ID: ", font = ("arial",10))
ID.place(x = 450, y = 450)

entry5 = Entry(root, textvar = fn5)
entry5.place(x = 540 , y = 450)

address = Label(root, text = "PHYSICAL ADDRESS: ", font = ("arial",10))
address.place(x = 690, y = 450)

cons = ['Aldai', 'Chesumei', 'Emgwen', 'Mosop', 'Nandi Hill', 'Tinderet']
droplist = OptionMenu(root, var, *cons)
droplist.configure(width = 10, font = ("arial", 10), relief = GROOVE, bg = "white")
droplist.place(x = 833, y = 442)

mail = Label(root, text = "EMAIL: ", font = ("arial",10))
mail.place(x = 450, y = 500)

entry6 = Entry(root, textvar = fn6)
entry6.configure(width = 50)
entry6.place(x = 500, y = 500)

register = Button(root, text = "REGISTER", relief = RAISED,fg = "white", bg = "blue", font = ("bold", 20), command = database)
register.place(x = 690, y = 550)
root.mainloop()
