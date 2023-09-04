import tkinter
import tkinter.ttk as ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox as mbox

def patient():
    Weekno= entry.get()
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Soft063#",
        database="Form"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT Week, FIrstName, Surname, MiddleName, ParentID, Physical_Address, Email_Address, Birth_Date FROM newborns WHERE Week = %s",(Weekno,))
    columns = [col[0] for col in cursor.description]

    if Weekno == '':
        mbox.showwarning("PROMPT","NO FIELD DISPLAYED")
    else:
        table ['columns'] = columns
        for col in columns:
            table.heading(col, text = col,)
            table.column(col)

        for row in cursor.fetchall():
            table.insert('', 'end', values = row)
    mydb.close()

def file():
    name = label1.get()
    date = label2.get()

    with open('FORM.txt', 'a') as file:
        file.write(f"Name: {name} Birth_Date: {date}\n")

def mail():
    root.destroy()
    import Mail

root = Tk()
root.geometry("2024x1024")
root.title("SKAI TECHNOLOGIES")

label = Label(root, text="BIRTH WEEK: ", font = ("arial", 17))
label.place(x = 10, y = 50)

entry = Entry(root, font = ("bold",15))
entry.place(x = 175, y = 55)

search = Button(root, text="RETRIEVE", font = ("arial", 15), bg = "blue", fg = "white", relief = GROOVE, command = patient)
search.place(x = 15, y = 90)

label1 = Label(root, text="PATIENT NAME: ", font = ("arial", 20))
label1.place(x = 10, y = 500)

label1 = Entry(root, font = ("bold",15))
label1.place(x = 222, y = 505)

label2 = Label(root, text="BIRTH DATE: ", font = ("arial", 20))
label2.place(x = 10, y = 600)

label2 = Entry(root, font = ("bold",15))
label2.place(x = 222, y = 605)

pdf = Button(root, text="SUBMIT", font = ("arial", 15), bg = "blue", fg = "white", relief = GROOVE, command = file)
pdf.place(x = 145, y = 705)

pdf = Button(root, text="FINISH", font = ("arial", 15), bg = "blue", fg = "white", relief = GROOVE, command = mail)
pdf.place(x = 145, y = 805)

columns = ['Week','FirstName','Surname','MiddleName','ParentID','Physical_Address','Email_Address','Birth_Date']
table = ttk.Treeview(root, columns = columns, show = 'headings')
table.place(x = 0, y = 150)

for col in columns:
    table.heading(col, text = col)

root.mainloop()

