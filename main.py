from tkinter import *
import pandas as pan
from encryption_module import EncryptionModule

NEON_GREEN = '#06FA45'
NEON_PURPLE = '#7D06FA'
BLACK = '#000000'
GRAY = '#787A78'


def save_pass():
    pass_df = pan.read_csv('saved_pass.csv')

    encrypt = EncryptionModule()

    en_pass = encrypt.encrypt_password(input_password.get())

    row = len(pass_df)


    pass_df.loc[row, 'website'] = input_website.get()
    pass_df.loc[row, 'username'] = input_email_username.get()
    pass_df.loc[row, 'password'] = en_pass

    pass_df.to_csv('saved_pass.csv', index=False)

    input_website.delete(0, 'end')
    input_email_username.delete(0, 'end')
    input_password.delete(0, 'end')


window = Tk()
window.title('Password Manager')
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

button_save_pass = Button(text='Save Password', width=36, bg=GRAY, fg=BLACK, command=save_pass)
button_save_pass.grid(column=1, row=4, columnspan=3)

window.mainloop()
