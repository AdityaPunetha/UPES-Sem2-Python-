from tkinter import *


def username():
    name = uia.get()
    print("User Name = ", name)


def click_me():
    print("Button was clicked")


def sel():
    selected = "You selected the option " + str(var.get())
    label.config(text=selected)
    print(selected)


root = Tk()
root.geometry('500x500')
root.title("First Mission")
L1 = Label(root, text="Greeting Seeker").pack()
user_name = Label(root, text="Username").place(x=100, y=100)
uia = Entry(root)
uia.pack(padx=100, pady=80)

but = Button(root, text='Click Me', bg="yellow", fg="black",
             width=10, command=click_me).place(x=200, y=300)
bu = Button(root, text='stop', border=3, width=10,
            command=root.destroy).place(x=200, y=350)
button = Button(root, text='Submit UserName',
                command=username).place(x=200, y=130)

var = IntVar()
R1 = Radiobutton(root, text="First", variable=var, value=1, command=sel)
R1.pack()

R2 = Radiobutton(root, text="Second", variable=var, value=2, command=sel)
R2.pack()

R3 = Radiobutton(root, text="Third", variable=var, value=3, command=sel)
R3.pack()

label = Label(root)
label.pack()
root.mainloop()
