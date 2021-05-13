from tkinter import *


def click():
    print(txt.get())


window = Tk()
window.geometry('200x100')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me", bg="red", fg="white",command=click)
btn.grid(column=1, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=2)
r1 = Radiobutton(window,text='First', value=1)
r2 = Radiobutton(window,text='Second', value=2)
r3 = Radiobutton(window,text='Third', value=3)
r1.grid(column=0, row=3)
r2.grid(column=1, row=3)
r3.grid(column=2, row=3)
window.mainloop()
