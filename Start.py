import tkinter
from tkinter import *
from tkinter import Label

def login():
    root.destroy()
    import Login
def register():
    root.destroy()
    import Register

root = Tk()
root.geometry("2048x1024")
root.title("SKAI TECHNOLOGIES")
root.configure(background = "light blue")
label = Label(root, text = "MINISTRY of HEALTH",foreground = "White", background = "light blue", font = ("Serif",100,"bold"))
label.place(x = 100, y = 220)

start_button = Button(root, text = "Register", fg = "White", bg = "blue",relief = RAISED, font = ("Arial", 18, "bold"), command = register)
start_button.place(x = 620, y = 420)

start_button = Button(root, text = "Login", fg = "White", bg = "blue",relief = RAISED, font = ("Arial", 20, "bold"), command = login)
start_button.place(x= 820, y = 420)


root.mainloop()
