from tkinter import *
from tkinter import messagebox
import subprocess

top = Tk()
top.geometry("500x500")
top.title('Abhi System Control!')

def m_box():
    m = messagebox.showinfo("Get Ready...","Shutdown")

def shut_down():
    output = subprocess.check_output(['shutdown', '-s', '-t', '2'])
def restart():
    output = subprocess.check_output(['shutdown', '/r'])
def hibernate():
    output = subprocess.check_output(['shutdown', '/h'])
def sleep():
    output = subprocess.check_output(['RUNDLL32.EXE', 'powrprof.dll,SetSuspendState', '0,1,0'])
def timed_shut_down():
    output = subprocess.check_output(['shutdown', '-i'])

    
var = StringVar()
var.set("What should i do Master Abhi ???")
lb1 = Label( top, textvariable = var, relief=RAISED, bg = "yellow",
             fg="blue", anchor="center", bd=10, font=40)
lb1.place(x=110,y=100)

b1 = Button(top, text = "*Shutdown?*", fg = "red", bg = "yellow", activebackground = "yellow", font=8,  command = shut_down)
b1.place(x=40, y=200)

b2 = Button(top, text = "**Restart?**", fg = "red", bg = "yellow", activebackground = "yellow",  font=8, command = restart)
b2.place(x=150, y=200)

b3 = Button(top, text = "*Hibernate?*", fg = "red", bg = "yellow", activebackground = "yellow", font=8, command = hibernate)
b3.place(x=255, y=200)

b4 = Button(top, text = "***Sleep****", fg = "red", bg = "yellow", activebackground = "yellow", font=8, command = sleep)
b4.place(x=365, y=200)

b5 = Button(top, text = "Timed Shutdown", fg = "red", bg = "yellow", activebackground = "yellow", font=8, command = timed_shut_down)
b5.place(x=195, y = 250)
top.mainloop(); 

