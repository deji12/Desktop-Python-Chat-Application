from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name") # gives input a default text

def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text='Enter your name', command=myClick, fg="blue", bg="grey")
# state= DISABLED helps to disable button
# padx and pady help resize button
# command = function tells program action to perform when button is clicked
# fg is for text color | bg is for button background color 
# borderline is for input border width
# .get gets input 
myButton.pack()

root.mainloop()