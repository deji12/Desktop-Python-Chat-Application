from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! i clicked a button")
    myLabel.pack()

myButton = Button(root, text='Click me', command=myClick, fg="blue", bg="grey")
# state= DISABLED helps to disable button
# padx and pady help resize button
# command = function tells program action to perform when button is clicked
# fg is for button text color | bg is for button background color 
myButton.pack()

root.mainloop()