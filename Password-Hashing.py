
from tkinter import *
import bcrypt

def validate(entered_password):
    #my password = "foobar"
    hash = b'$2b$12$c0yvMNCYGxIdm.WAt42wd.cUydXSEjx22t0xYbtIsfIwWSjjlhh9C'
    entered_password = bytes(entered_password, encoding='utf-8')
    if bcrypt.checkpw(entered_password, hash):
        print("Login Successful")

    else:
        print("Invalid password")



root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

btn = Button(text="Validate", command=lambda: validate(password_entry.get()))
btn.pack()

root.mainloop()

