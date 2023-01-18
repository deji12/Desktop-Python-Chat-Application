from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon

def open():
    global my_img
    top = Toplevel()
    top.title("new window")
    top.iconbitmap('./icon.ico') # setting an icon
    my_img = ImageTk.PhotoImage(Image.open('./imgs/w3.jpg'))
    my_Label = Label(top, image=my_img).pack()
    btn = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open second window:", command=open).pack()


root.mainloop()