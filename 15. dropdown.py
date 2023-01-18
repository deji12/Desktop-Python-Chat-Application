from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon
root.geometry("400x400") # default size of window

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday", "Tyesday", "Wednesday"
]

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, *options)
drop.pack()

mybtn = Button(root, text='show selection', command=show).pack()

root.mainloop()