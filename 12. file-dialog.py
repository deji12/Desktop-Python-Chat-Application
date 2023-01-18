from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon

root.filename = filedialog.askopenfile(initialdir="/imgs", title="Select a file", filetypes=(("png files", "*.png")))


root.mainloop()