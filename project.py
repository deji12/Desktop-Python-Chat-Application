from tkinter import *
import requests
import json
from threading import Thread
import time

root = Tk()
root.title("Frame")
root.iconbitmap('./icon.ico') # setting an icon
root.config(background="#DAAD86")
root.geometry("400x400") # default size of window

USERNAME = None
ROOM = None

def LoginForm():
    submit_form = requests.post(
        'https://desktopchat.onrender.com/', 
        data = {
            'username': username.get(),
            'room': room.get()
        },
    )

    USERNAME = username.get()
    ROOM = room.get()

    response = json.loads(submit_form.content)['success']

    if response == 'Room exists' or response == 'Room created successfully':
        messageBox = Toplevel()

        root = messageBox

        root.title('Proton.com . Wikipedia')

        root.geometry('700x675')
        root.config(background="#DAAD86")

        def clear():

            my_entry.delete(0, END)

            my_text.delete(0.0, END)

        my_frame = Frame(root)

        my_frame.pack(pady=5)

        text_scroll = Scrollbar(my_frame)

        text_scroll.pack(side=RIGHT, fill=Y)

        hor_scroll = Scrollbar(my_frame, orient='horizontal')

        hor_scroll.pack(side=BOTTOM, fill=X)

        my_text = Text(my_frame, yscrollcommand=text_scroll.set, wrap='none', xscrollcommand=hor_scroll.set)

        my_text.pack()

        text_scroll.config(command=my_text.yview)

        hor_scroll.config(command=my_text.xview)

        #=====================================================================

        get_messages = requests.get(
            f'https://desktopchat.onrender.com/{room.get()}/{username.get}',  
        )
        messages = json.loads(get_messages.content)

        for i in messages['messages']:
                if i['sender'] != USERNAME:
                    my_text.insert(0.0, f"{i['sender']} ->  {i['message']}\n\n")
                else:
                    my_text.insert(0.0, f"|YOU| ->  {i['message']}\n\n")

        # =================================================================================

        my_label_frame = LabelFrame(root, text='Send Chat', background='#659DBD', fg='white')

        my_label_frame.pack(pady=20)

        my_entry = Entry(my_label_frame, font=('Helvetica', 18), width=47)

        my_entry.pack(pady=20, padx=20)

        # =================================================================================



        def sendMessage():

            send_new_message = requests.post(
                f'https://desktopchat.onrender.com/{ROOM}/{USERNAME}/', 
                data = {
                    'message': my_entry.get()
                },
            )

            clear()

            get_messages = requests.get(
                f'https://desktopchat.onrender.com/{room.get()}/{username.get}',  
            )
            messages = json.loads(get_messages.content)

            for i in messages['messages']:
                if i['sender'] != USERNAME:
                    my_text.insert(0.0, f"{i['sender']} ->  {i['message']}\n\n")
                else:
                    my_text.insert(0.0, f"|YOU| ->  {i['message']}\n\n")


        button_frame = Frame(root, background='#DAAD86')

        button_frame.pack(pady=10)

        search_button = Button(button_frame, text='Send', font=('Helvetica', 32), fg='#3a3a3a', command=sendMessage)

        search_button.grid(row=0, column=0, padx=20)

        clear_button = Button(button_frame, text='Clear', font=('Helvetica', 32), fg='#3a3a3a', command=clear)

        clear_button.grid(row=0, column=1)

        #root.after(5000, reloadForMessages) # run first time after 1000ms (1s)

        def reloadForMessages():
            while True:
                time.sleep(10)
                get_messages = requests.get(
                f'https://desktopchat.onrender.com/{room.get()}/{username.get}',  
                )
                messages = json.loads(get_messages.content)

                my_text.delete(0.0, END)
                for i in messages['messages']:
                    if i['sender'] != USERNAME:
                        my_text.insert(0.0, f"{i['sender']} ->  {i['message']}\n\n")
                    else:
                        my_text.insert(0.0, f"|YOU| ->  {i['message']}\n\n")
                    


        if __name__ == "__main__":
            
            thread = Thread(target = reloadForMessages)
            
            thread.start()

            root.mainloop()


# login form gui
myLabel = Label(root, text='Enter Room Details', fg='#000', bg='#659DBD', font='Arial 17 bold')
myLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

username_label = Label(root, text='Username', fg='#000', bg='#659DBD', font='Arial 10 bold')
username_label.place(relx=0.5, rely=0.3, anchor=CENTER)

username = Entry(root, width=50, borderwidth=5)
username.place(relx=0.5, rely=0.4, anchor=CENTER)

room_label = Label(root, text='Room', fg='#000', bg='#659DBD', font='Arial 10 bold')
room_label.place(relx=0.5, rely=0.5, anchor=CENTER)

room = Entry(root, width=50, borderwidth=5)
room.place(relx=0.5, rely=0.6, anchor=CENTER)

submitButton = Button(root, text='Submit', command=LoginForm, fg="white", bg="#659DBD")
submitButton.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()
