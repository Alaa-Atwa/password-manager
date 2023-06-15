import tkinter.messagebox
from tkinter import *
from password_gen import generate_password
import pyperclip

def random_password():
    password_entry.delete(0, END)  # delete previous value
    password_entry.insert(END, generate_password())


def get_entries():
    website_name = website_entry.get()
    email_address = Email_entry.get()
    password = password_entry.get()

    # check for no entry
    if not website_name:
        tkinter.messagebox.showerror(title="input required", message="you must enter the website name ")
    elif not password:
        tkinter.messagebox.showerror(title="input required", message="you must enter or generate a password.")
    else:
        # copying password to clipboard
        pyperclip.copy(password)

        msg = f"Email: {email_address} \n Password: {password} \n is this ok ?"
        confirm = tkinter.messagebox.askyesno(title="Confirmation", message=msg)
        if confirm:
            with open("./passwords.txt", mode='a') as file:
                file.write(f"{website_name} | {email_address} | {password} \n")
            # reset inputs after saving
            website_entry.delete(0, END)  # delete from first index to end.
            password_entry.delete(0, END)
            website_entry.focus()


# --------------------------- SETUP THE UI ------------------------- #

# configure the window screen
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

# adding the image with canvas
canvas = Canvas(width=450, height=400, highlightthickness=0)
password_img = PhotoImage(file='./password.png')  # it must a png photo
canvas.create_image(200, 200, image=password_img)  # 200 , 200 is the position inside the canvas.
canvas.grid(row=0, column=1)

website_label = Label(padx=20, text="Website:", highlightthickness=0)
website_label.grid(row=1, column=0, pady=3)

website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(row=1, column=1, pady=3)

Email_label = Label(padx=20, text="Email/Username:", highlightthickness=0)
Email_label.grid(row=2, column=0, pady=3)

# email
email = "alaa.atwa555@gmail.com"
Email_entry = Entry(width=50)
Email_entry.insert(END, email)
Email_entry.grid(row=2, column=1, pady=3)

# password
Password_label = Label(padx=20, text="Password:", highlightthickness=0)
Password_label.grid(row=3, column=0, pady=3)

password_entry = Entry(width=30)
password_entry.grid(padx=20, row=3, column=1, pady=3, sticky=W)

password_button = Button(padx=5, text="Generate Password", highlightthickness=0, command=random_password)
password_button.grid(padx=20, row=3, column=1, pady=3, sticky=E)

# ADD button
Add_button = Button(padx=5, text="Add", width=50, highlightthickness=0, command=get_entries)
Add_button.grid(row=4, column=1, padx=20, pady=3)

window.mainloop()
