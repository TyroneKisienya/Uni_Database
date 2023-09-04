from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Notepad")

text = Text(root)
text.grid(column=1, row=1, rowspan=3)


def SaveAs():
    global text
    t = text.get("1.0", "end-1c")
    saveLocation = filedialog.asksaveasfilename()
    file = open(saveLocation, "w+")
    file.write(t)
    file.close()


button = Button(root, text="Save", font="Serif", command=SaveAs)
button.grid(column=1, row=4)


root.mainloop()
