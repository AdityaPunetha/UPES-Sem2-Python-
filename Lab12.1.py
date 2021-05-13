from tkinter import *


def click():
    print("Button was clicked")


window = Tk()
window.geometry('100x100')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me", bg="red", fg="white",command=click)
btn.grid(column=1, row=0)
window.mainloop()
