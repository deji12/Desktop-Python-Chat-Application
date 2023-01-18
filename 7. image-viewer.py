from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code")
root.iconbitmap('./icon.ico') # setting an icon


my_img = ImageTk.PhotoImage(Image.open('./imgs/palo.png'))
my_img2 = ImageTk.PhotoImage(Image.open('./imgs/w3.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('./imgs/palo3.png'))
my_img4 = ImageTk.PhotoImage(Image.open('./imgs/palo4.png'))
my_img5 = ImageTk.PhotoImage(Image.open('./imgs/palo5.png'))

image_list = [my_img, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

def foward(image_number):
    global my_label
    global button_foward
    global button_back

    # Deleting the image from the grid.
    my_label.grid_forget() # delete image
    my_label = Label(image=image_list[image_number-1])
    button_foward = Button(root, text=">>", command=lambda: foward(image_number +1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        button_foward = Button(root, text=">>", status=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_foward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_foward
    global button_back

    my_label.grid_forget() # delete image
    my_label = Label(image=image_list[image_number-1])
    button_foward = Button(root, text=">>", command=lambda: foward(image_number +1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", status=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_foward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit program", command=root.quit)
button_foward = Button(root, text=">>", command=lambda: foward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_foward.grid(row=1, column=2)

root.mainloop()