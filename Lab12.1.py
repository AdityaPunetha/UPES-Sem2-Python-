def click_me():
    print("Button was clicked") 

from tkinter import *
window = Tk()
window.geometry('500x400')
window.title("First program")
l=Label(window,text="Hello").pack()
button = Button(window, text='Click me', bd=10,width=25,bg = "yellow",fg = "black",command=click_me)
button.pack(padx=100, pady=50)
window.mainloop()
