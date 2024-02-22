from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 8))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)
    pwd = "".join(password_list)
    pwd_input.insert(0, pwd)
    pyperclip.copy(pwd)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = mail_input.get()
    password = pwd_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
            # with open("data.txt", "a") as data_file:
            #     data_file.write(f"{website} | {email} | {password} \n")
        finally:
            website_input.delete(0, END)
            pwd_input.delete(0, END)
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f"There are the details entered\nEmail : {email}\nPassword : {password}"
        #                                        f"\n Is it ok to save??")

        # if is_ok:
        #     with open("data.json", "w") as data_file:
        #         json.dump(new_data, data_file, indent=4)

        #     with open("data.json", "r") as data_file:
        #         data = json.load(data_file)
        #         print(data)




# ---------------------------- UI SETUP ------------------------------- #
def search():
   website = website_input.get()

   try:
       with open("data.json") as data_file:
           data = json.load(data_file)
   except FileNotFoundError:
       messagebox.showinfo(title="Error", message="No Data File Found.")
   else:
       if website in data:
           email = data[website]["email"]
           password = data[website]["password"]
           messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
       else:
           messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")
mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0, sticky="w")
pwd_label = Label(text="Password:")
pwd_label.grid(row=3, column=0, sticky="w")

website_input = Entry(width=40)
website_input.grid(row=1, column=1, sticky="w")
# set cursor on this input
website_input.focus()
mail_input = Entry(width=58)
mail_input.grid(row=2, column=1, columnspan=2, sticky="w")
mail_input.insert(0, "kruti@gmail.com")
pwd_input = Entry(width=40)
pwd_input.grid(row=3, column=1, sticky="w")

genpwd_button = Button(text="Generate Password", command=generate_pwd)
genpwd_button.grid(row=3, column=2, sticky="w")
add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2, sticky="w")

window.mainloop()
