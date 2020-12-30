from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    #get website
    website = website_input.get()

    #get email
    email = email_input.get()

    #get password
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message="Don't let filds empty")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {email}\nPassword: {password} \n "
                                                              f"Is it ok to save?")

        #check empty and save
        if is_ok:
            f = open("my_password.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()

            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=30)

#canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

#email/username
email_label = Label(text="Email / Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=39)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "cecilaw0118@gmail.com")

#password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=20)
password_input.grid(column=1, row=3)

password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(column=2, row=3)

#add btn
add_btn = Button(text="Add", width=38, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
