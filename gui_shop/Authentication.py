from canvas import root, frame
from tkinter import Button, Entry

from helpers import clean_screen


def render_entry():
    register_button = Button(root, text="Register", bg="blue", fg="white", width=20, height=2, borderwidth=0,
                             command=register)

    frame.create_window(500, 500, window=register_button)

    logging_button = Button(root, text="Log in", bg="green", fg="white", width=20, height=2, borderwidth=0)

    frame.create_window(500, 450, window=logging_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:", font=('Times','20','italic'))
    frame.create_text(100, 100, text="Last name:", font=('Times','20','italic'))
    frame.create_text(100, 150, text="Username:", font=('Times','20','italic'))
    frame.create_text(100, 200, text="Password:", font=('Times','20','italic'))

    frame.create_window(300, 50, window=first_name_box, width=200, height=30)
    frame.create_window(300, 100, window=last_name_box, width=200, height=30)
    frame.create_window(300, 150, window=username_box, width=200, height=30)
    frame.create_window(300, 200, window=password_box, width=200, height=30)

    register_button = Button(root, text="Register", bg="blue", fg="white", width=20, height=2, borderwidth=0,
                             command=registration)

    frame.create_window(300, 300, window=register_button)


def registration():
    user_info_dict = {
        "First name": first_name_box.get(),
        "Last name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get()
    }

    print(user_info_dict)

    if check_registration(user_info_dict):
        pass



def check_registration(info):
    frame.delete("error")

    for key, value in info.items():
        if not value.strip():
            frame.create_text(300, 250,
                            text=f"{key} cannot be empty!",
                            fill="red",
                            tags="error",
                            font=('Times','20','bold')
                              )


            return False


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")




















