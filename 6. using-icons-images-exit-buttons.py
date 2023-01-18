from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code")
root.iconbitmap('./icon.ico') # setting an icon

button_quit = Button(root, text="Exit program", command=root.quit) # ending program
button_quit.pack()


my_img = ImageTk.PhotoImage(Image.open('./w3.jpg'))
my_label = Label(image=my_img)
my_label.pack()



root.mainloop()