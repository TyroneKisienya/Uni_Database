import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mbox

win = tk.Tk()
win.title('Python GUI')
alabel = ttk.Label(win,text = "A Label")
alabel.grid(column=0,row=0)

def clickMe():
    action.configure(text= 'Hello ' + name.get())
    alabel.configure(foreground = "Red")
    
action = ttk.Button(win,text = "Click Me!", command = clickMe)
action.grid(column=2,row=1)

ttk.Label(win, text= "Choose a Number: ").grid(column = 1, row = 0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width = 16, textvariable=number)
numberChosen['values'] = (1,2,4,42,100)
numberChosen.grid(column=1,row=1)
numberChosen.current(0)

ttk.Label(win,text = "Enter a Name: ").grid(column=0,row=0)
name= tk.StringVar()
nameEntered = ttk.Entry(win, width=16, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state = 'disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)
chVarUn = tk.IntVar()

check2 = tk.Checkbutton(win,text = "unchecked", variable = chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chVarEn = tk.IntVar()

check3 = tk.Checkbutton(win, text = "Enabled", variable = chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background = COLOR1)
    elif radSel == 2: win.configure(background = COLOR2)
    elif radSel == 3: win.configure(background = COLOR3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text = COLOR1, variable = radVar, value=1, command = radCall)
rad1.grid(column=0, row=5, sticky=tk.W)
rad2 = tk.Radiobutton(win, text = COLOR2, variable =radVar, value=2, command = radCall)
rad2.grid(column=1, row=5, sticky=tk.W)
rad3 = tk.Radiobutton(win, text = COLOR3, variable=radVar, value=3, command = radCall)
rad3.grid(column=2, row=5, sticky=tk.W)

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

LabelsFrame = ttk.LabelFrame(win, text = ' Labels in a Frame ')
LabelsFrame.grid(column=0, row=7, padx=20, pady=40)
ttk.Label(LabelsFrame, text = "Lable(1").grid(column=0, row=0)
ttk.Label(LabelsFrame, text ="Label(2").grid(column=0, row=1)
ttk.Label(LabelsFrame, text = "Label(3").grid(column=0, row=2)

for child in LabelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

menuBar = Menu(win)
win.config(menu=menuBar)
def _quit():
    win.quit()
    win.destroy()
    exit()
fileMenu = Menu(menuBar, tearoff=0)

fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File",menu=fileMenu)

def _msgBox():
    mbox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe Year is 2023.')

#def _msgBox():
    #mbox.showwarning('Python Message warning Box', 'A Python GUI created using tkinter:\nWarning: There might be a bug in this code')

#def _msgBox():
    #mbox.showerror('Python Message error Box', 'A Python GUI created using tkinter:\nError: Houston - We Do have a serious PROBLEM')

#def _msgBox():
    #answer = mbox.askyesno('Python Message Dual Choice Box', 'Are you really sure you wish to do this?')
    #print(answer)
    
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu= helpMenu)
win.mainloop()
