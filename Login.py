import tkinter
from tkinter import *
from confirm import *
from tkinter import messagebox as mbox

root = Tk()
root.geometry("2048x1024")
root.title("SKAI TECHNOLOGIES")

fn = StringVar()

def correct():
    ent = fn.get()

    if ent == "AAR" or ent == "KNH" or ent == "JOOTRH" or ent =="MTRH" or ent == "JH":
        root.destroy()
        import Form
    else:
       mbox.showerror("Prompt", "INVALID PASSWORD")

label = Label(root, text = "LOGIN", relief = "solid", width = 40, font = ("bold", 20))
label.place(x = 440, y = 110)

ID = Label(root, text = "PASSWORD: ", font = ("arial", 15))
ID.place(x = 500, y = 222)

entry = Entry(root, textvar = fn, width = 20, font = ("arial", 15))
entry.place(x = 630, y =222)	

login = Button(root, text = "LOGIN", relief = RAISED, fg = "white", bg = "blue", font = ("arial", 20), command = correct)
login.place(x = 700, y = 320)

root.mainloop()
