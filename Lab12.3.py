from tkinter import *


def submitt():
    name = uia.get()
    m1 = marks1.get()
    m2 = marks2.get()
    m3 = marks3.get()
    per = ((int(m1) + int(m2) + int(m3)) / 300) * 100
    labe = Label(window, text="User name is " + name, font="Arial").place(x=300, y=500)
    lab = Label(window, text="The Percentage is " + str(per) + "%", font="Arial").place(x=300, y=550)


window = Tk()
window.geometry('800x800')
window.title("Student details")

l = Label(window, text="Fill up the following details", font="Arial").place(x=300, y=10)
user_name = Label(window, text="Username", font="Arial").place(x=200, y=55)
uia = Entry(window)
uia.place(x=300, y=60)

sub = Label(window, text="Select the Gender", font="Arial").place(x=110, y=140)
var = StringVar()
R1 = Radiobutton(window, text="Male", variable=var, value="Male", font="Arial")
R1.place(x=300, y=100)
R2 = Radiobutton(window, text="Female", variable=var, value="Female", font="Arial")
R2.place(x=300, y=140)

sub = Label(window, text="Select the Qualification", font="Arial").place(x=80, y=260)
listbox = Listbox(window, height=4, width=20, font="Helvetica")
listbox.insert(1, "10+2 only")
listbox.insert(2, "Graduate")
listbox.insert(3, "Post Graduate")
listbox.place(x=300, y=230)

sub = Label(window, text="Enter marks of three subject", font="Arial").place(x=200, y=350)
l1 = Label(window, text="Subject 1").place(x=240, y=390)
l2 = Label(window, text="Subject 2").place(x=240, y=430)
l3 = Label(window, text="Subject 3").place(x=240, y=470)
marks1 = Entry(window)
marks1.place(x=300, y=390)
marks2 = Entry(window)
marks2.place(x=300, y=430)
marks3 = Entry(window)
marks3.place(x=300, y=470)

button = Button(window, text='Submit Details', bd=10, width=25, bg="yellow", fg="black", command=submitt).place(x=300,
                                                                                                                y=600)
bu = Button(window, text='Stop the Program', border=3, width=20, command= root

window.mainloop()
