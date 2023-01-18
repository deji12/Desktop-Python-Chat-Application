from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon
root.geometry("400x400") # default size of window
root.config(background='green')

# create or connect to a database
conn = sqlite3.connect('address_book.db')

c = conn.cursor()

# create table
# c.execute("""CREATE TABLE addresses (
#     first_name text, 
#     last_name text,
#     address text,
#     city text, 
#     state text,
#     zipcode integer
# )""")

# create submit function

def submit():
    # create or connect to a database
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    # insert to table
    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zip)", 
        {
            'first_name': first_name.get(),
            'last_name': last_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zip': zip.get()
        })


    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear the text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip.delete(0, END)

# create query function

def query():
    # create or connect to a database
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()

    # to query database

    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # loop through records
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # commit changes
    conn.commit()

    # close connection
    conn.close()

# text boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20)

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zip = Entry(root, width=30)
zip.grid(row=5, column=1)

# text box labels
f_name = Label(root, text='first name')
f_name.grid(row=0, column=0)
l_name = Label(root, text='last name')
l_name.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='city')
city_label.grid(row=3, column=0)
state_label = Label(root, text='state')
state_label.grid(row=4, column=0)
zip_label = Label(root, text='zip code')
zip_label.grid(row=5, column=0)

# create submit button
submit_button = Button(root, text='Submit', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a query button
query_button = Button(root, text='Show Records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()