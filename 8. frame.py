from tkinter import *

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon

frame = LabelFrame(root, text="This is my frame", padx=50, pady=50, background="#659DBD")
frame.pack(padx=10, pady=10) 

b = Button(frame, text="Don't click here")
b.pack()


root.mainloop()