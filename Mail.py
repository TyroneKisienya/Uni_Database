import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_email():
    filetypes = (('text files', '*.txt'),  ('All files', '*.*'))
    # Get the email address and message from the user
    email = entry.get()
    message = entry1.get('1.0', 'end-1c')
    
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = 'tyronekisienya01@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Immunisable Children'
    msg.attach(MIMEText(message))
    
    # Add the attachment to the email message
    attachment = fd.askopenfile(filetypes= filetypes, initialdir="C:")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= Form.txt")
    msg.attach(part)
    
    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('tyronekisienya01@gmail.com', 'srvbkhsmfmxssexk')
    text = msg.as_string()
    server.sendmail('tyronekisienya01@gmail.com', email, text)
    server.quit()
    
# Create the GUI
root = Tk()
root.geometry("2048x1024")
root.title("SKAI TECHNOLOGIES")

label = Label(root, text="Email: ", font = ("arial", 20))
label.place(x = 10, y = 90)

entry = Entry(root, font = ("arial", 15), width = 30)
entry.place(x = 90, y = 97)

label1 = Label(root, text="Message:", font = ("arial", 20))
label1.place(x = 10, y = 150)

entry1 = Text(root)
entry1.place(x = 40, y = 190)

send = Button(root, text="Attach and Send mail", font = ("arial", 15), relief = GROOVE, fg = "black", bg = "light blue", command=send_email)
send.place(x = 300, y = 600)

root.mainloop()
