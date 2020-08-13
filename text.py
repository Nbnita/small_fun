import tkinter
from tkinter import *

def delete1():
    screen1.destroy()
    screen.destroy()
    window.destroy()
def delete():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Message")
    screen1.geometry("300x250")
    screen1.resizable(0,0)

    name_info=name.get()
    message_info=message.get()

    file=open(name_info+".txt","w")
    file.write(name_info+"\n")
    file.write(message_info)
    file.close()

    name_entry.delete(0,END)
    message_entry.delete(0,END)

    Label(screen1, text="Message Send successfully", fg="green", height=5, width=50, font=("Calibri",15)).pack()
    Label(text="").pack()
    Button(screen1, text="Ok", height=1, width=5, command=delete1).pack()

def message():
    global screen
    screen=Toplevel(window)
    screen.title("Message")
    screen.geometry("500x350")
    screen.resizable(0,0)

    global name
    global message

    name= StringVar()
    message=StringVar()

    Label(screen, text="Please enter your message below-", fg="grey",height=2, width= 50, font=("Calibri",15)).pack()
    Label(text="").pack()
    global name_entry
    global message_entry

    Label(screen, text="Name", fg="black", height=2, width=50, font=("Calibri",15)).pack()
    name_entry=Entry(screen,textvariable="name")
    name_entry.pack()
    Label(text="").pack()

    Label(screen, text="Message", fg="black", height=2, width=50, font=("Calibri",15)).pack()
    message_entry=Entry(screen,textvariable="message")
    message_entry.pack()
    Label(text="").pack()

    Button(screen,text="Submit", height=1, width=10,command=delete).pack()

def text():
    global window
    window=Tk()
    window.title("Message")
    window.geometry("500x350")
    window.resizable(0,0)

    Label(window, text="Welcome! Wanna send any message?", fg="grey", height=4, width=50, font=("Calibri", 15)).pack()
    Label(text="").pack()
    Button(window,text="Send Message", height=2, width=25, command=message).pack()
    window.mainloop()
text()
