from tkinter import *

root = Tk()
root.geometry('400x400')
btn = Button(root, text='click me!', bd='5', command=root.destroy)
btn.pack()
root.mainloop()
