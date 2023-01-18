from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesorno

def popup():
    #messagebox.showerror("This is my popup", "Hello world")
    response = messagebox.askyesno("This is my popup", "Hello world")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()
Button(root, text="Popup", command=popup).pack()

root.mainloop()