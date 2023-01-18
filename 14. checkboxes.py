from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon
root.geometry("400x400") # default size of window

def show():
    myLabel = Label(root, text=var.get()).pack()

var = IntVar()

c = Checkbutton(root, text='check this box, i dare you', variable=var)
c.pack()



my_button = Button(root, text='show selection', command=show).pack()

root.mainloop()