from tkinter import *
from tkinter import messagebox
import pandas as pan
from encryption_module import EncryptionModule

NEON_GREEN = '#06FA45'
NEON_PURPLE = '#7D06FA'
BLACK = '#000000'
GRAY = '#787A78'

encrypt = EncryptionModule()


def save_pass():
    global encrypt

    if encrypt.state is False:
        pass_df = pan.read_csv('saved_pass.csv')

        row = len(pass_df)

        pass_df.loc[row, 'website'] = input_website.get().lower()
        pass_df.loc[row, 'username'] = input_email_username.get()
        pass_df.loc[row, 'password'] = input_password.get()

        pass_df.to_csv('saved_pass.csv', index=False)

        input_website.delete(0, 'end')
        input_email_username.delete(0, 'end')
        input_password.delete(0, 'end')
    else:
        messagebox.showinfo('Warning', 'File is encrypted! Can Not Read!')


def return_pass():
    global encrypt

    if encrypt.state is False:
        panda_df = pan.read_csv('saved_pass.csv')
        website_name = get_pass_input.get().lower()
        credentials_dict = panda_df.to_dict(orient='index')

        for index, value in credentials_dict.items():
            if value['website'] == website_name:
                print(value['password'])
                messagebox.showinfo('Your Password', f'Your Password is: {value['password']}')
                return value['password']
    else:
        messagebox.showinfo('Warning', 'File is encrypted! Can Not Read!')


def encrypt_decrypt():
    global encrypt

    if encrypt.state is False:
        encrypt.encrypt_file()
    elif encrypt.state is True:
        encrypt.decrypt_file()


window = Tk()
window.title('Black Magik Design')
window.config(pady=150, padx=100, bg='black')

canvas = Canvas(width=250, height=248, bg='black', highlightthickness=0)
logo = PhotoImage(file='bm-logo.png')

canvas.create_image(122, 122, image=logo)
canvas.grid(column=1, row=0)

field_website = Label(text='Website:', fg=NEON_GREEN, bg='black', font=('Ariel', 14, 'bold'))
field_website.grid(column=0, row=1)
field_website.focus()

field_email_username = Label(text='Email/Username:', fg=NEON_GREEN, bg='black', font=('Ariel', 14, 'bold'))
field_email_username.grid(column=0, row=2)

field_Password = Label(text='Password:', fg=NEON_GREEN, bg='black', font=('Ariel', 14, 'bold'))
field_Password.grid(column=0, row=3)

input_website = Entry(width=35, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 14))
input_website.grid(column=1, row=1, columnspan=2, pady=15)

input_email_username = Entry(width=35, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 14))
input_email_username.grid(column=1, row=2, columnspan=2, pady=15)

input_password = Entry(width=21, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 14))
input_password.grid(column=1, row=3, pady=15)

button_gen_pass = Button(text='Generate Password', bg=GRAY, fg=BLACK)
button_gen_pass.grid(column=2, row=3)

button_save_pass = Button(text='Save Password', width=32, bg=GRAY, fg=BLACK, command=save_pass)
button_save_pass.grid(column=1, row=4)

field_get_pass = Label(text='Retrieve Password:', fg=NEON_GREEN, bg='black', font=('Ariel', 14, 'bold'))
field_get_pass.grid(column=0, row=5)

get_pass_input = Entry(width=21, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 14))
get_pass_input.grid(column=1, row=5, pady=30)
get_pass_input.insert(0, 'Enter Website')

button_retrieve_pass = Button(text='Get Password', width=30, bg=GRAY, fg=BLACK, command=return_pass)
button_retrieve_pass.grid(column=2, row=5, pady=30)

button_encrypt = Button(text='Encrypt/Decrypt Data', width=30, bg=GRAY, fg=BLACK, command=encrypt_decrypt)
button_encrypt.grid(column=1, row=6)

warning = Label(text='Data must be decrypted to read and write', fg=NEON_GREEN, bg='black', font=('Ariel', 14, 'bold'))
warning.grid(column=1, row=7, pady=20)



window.mainloop()
