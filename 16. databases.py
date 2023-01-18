from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon
root.geometry("400x400") # default size of window

# create or connect to a database
conn = sqlite3.connect('address_book.db')

c = conn.cursor()

# create table
c.execute("""CREATE TABLE addresses (
    first_name text, 
    last_name text,
    address text,
    city text, 
    state text,
    zipcode integer
)""")

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()