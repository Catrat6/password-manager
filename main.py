from tkinter import *
from tkinter import messagebox
import pandas as pan
from encryption_module import EncryptionModule
from generator import generate_new, pass_phrase, remix_string
import pyperclip

NEON_GREEN = '#06FA45'
NEON_PURPLE = '#7D06FA'
BLACK = '#000000'
GRAY = '#787A78'

encrypt = EncryptionModule()


def save_pass():
    global encrypt

    check = encrypt.check_state()

    if check is False:
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

    check = encrypt.check_state()

    if check is False:
        panda_df = pan.read_csv('saved_pass.csv')
        website_name = get_pass_input.get().lower()
        credentials_dict = panda_df.to_dict(orient='index')

        for index, value in credentials_dict.items():
            if value['website'] == website_name:
                pyperclip.copy(value['password'])
                messagebox.showinfo('Your Password', f'Your Password is: {value['password']}\n it has been copied to your clipboard')
                return value['password']
    else:
        messagebox.showinfo('Warning', 'File is encrypted! Can Not Read!')


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
input_website.grid(column=1, row=1, pady=15)

input_email_username = Entry(width=35, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 14))
input_email_username.grid(column=1, row=2, pady=15)

input_password = Entry(width=21, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 14))
input_password.grid(column=1, row=3, pady=15)

button_save_pass = Button(text='Save Password', width=32, bg=GRAY, fg=BLACK, command=save_pass)
button_save_pass.grid(column=1, row=4)

field_get_pass = Label(text='Retrieve Password:', fg=NEON_GREEN, bg='black', font=('Ariel', 14, 'bold'))
field_get_pass.grid(column=0, row=5)

get_pass_input = Entry(width=21, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 14))
get_pass_input.grid(column=1, row=5, pady=30)
get_pass_input.insert(0, 'Enter Website')

button_retrieve_pass = Button(text='Get Password', width=30, bg=GRAY, fg=BLACK, command=return_pass)
button_retrieve_pass.grid(column=2, row=5, pady=30)

button_encrypt = Button(text='Encrypt/Decrypt Data', bg=GRAY, fg=BLACK, font=('Ariel', 18),
                        command=encrypt.encrypt_decrypt)
button_encrypt.grid(column=2, row=8)

warning = Label(text='Data must be decrypted to read and write', fg=NEON_GREEN, bg='black', font=('Ariel', 14, 'bold'))
warning.grid(column=1, row=7, pady=20)


# Password Generator Window

def open_window():
    generator_window = Toplevel(window)
    generator_window.config(padx=100, pady=100, bg='black')
    generator_window.title('Password Generator')

    def generate_random():
        if switch_one.get() == 1:
            a = int(toggle_one_input.get())
            b = generate_new(a)
            pyperclip.copy(b)
            messagebox.showinfo('Your New Password', f'Your New Password: {b}\n It has been copied to your clip board')
            toggle_one_input.delete(0, 'end')

        if switch_two.get() == 1:
            a = int(toggle_two_input.get())
            b = pass_phrase(a)
            pyperclip.copy(b)
            messagebox.showinfo('Your New Password', f'Your New Password: {b}\n It has been copied to your clip board')
            toggle_two_input.delete(0, 'end')

    switch_one = IntVar()
    switch_two = IntVar()

    label = Label(generator_window, text='Generate a random password', fg=NEON_GREEN, bg='black',
                  font=('Ariel', 14, 'bold'))
    label.grid(column=0, row=0, columnspan=3)

    label = Label(generator_window, text='Check Your preferred method and enter the length', fg=NEON_GREEN, bg='black',
                  font=('Ariel', 14, 'bold'))
    label.grid(column=0, row=1, columnspan=3)

    toggle_one = Checkbutton(generator_window, text='Random', fg=NEON_PURPLE, bg='black', font=('Arial', 12, 'bold'),
                             variable=switch_one)
    toggle_one.grid(column=0, row=2, pady=5)

    toggle_one_input = Entry(generator_window, width=5, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 12))
    toggle_one_input.grid(column=0, row=3, pady=5)

    toggle_two = Checkbutton(generator_window, text='Phrase/words', fg=NEON_PURPLE, bg='black',
                             font=('Arial', 12, 'bold'), variable=switch_two)
    toggle_two.grid(column=2, row=2, pady=5)

    toggle_two_input = Entry(generator_window, width=5, bg=NEON_PURPLE, fg=NEON_GREEN, font=('Arial', 12))
    toggle_two_input.grid(column=2, row=3, pady=5)

    button_gen_new_pass = Button(generator_window, text='Generate', width=32, bg=GRAY, fg=BLACK,
                                 command=generate_random)
    button_gen_new_pass.grid(column=1, row=4, pady=20)


button_gen_pass = Button(text='Password Generator', bg=GRAY, fg=BLACK, font=('Arial', 18), command=open_window)
button_gen_pass.grid(column=0, row=8, pady=50)

window.mainloop()
