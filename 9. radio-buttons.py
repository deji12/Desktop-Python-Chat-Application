from tkinter import *

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon

r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(root, text=value).pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myButton = Button(root, text="Click me", command=lambda: clicked(r.get())).pack()

root.mainloop()