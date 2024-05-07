import os.path
from cryptography.fernet import Fernet
from tkinter import messagebox


class EncryptionModule:

    def __init__(self):
        self.key = self.load_key()
        self.state = self.check_state()

    def check_state(self):
        with open('file_state.txt', 'r') as file:
            a = file.read().strip()
            if a == 'True':
                return True
            elif a == 'False':
                return False

    def update_state(self, state):
        with open('file_state.txt', 'w') as file:
            file.write(state)

    def load_key(self):
        if os.path.exists('file_key.key'):
            with open('file_key.key', 'rb') as key:
                return key.read()
        else:
            new_key = Fernet.generate_key()
            with open('file_key.key', 'wb') as key:
                key.write(new_key)
            messagebox.showinfo('New Key', f'Your key is {new_key}, this will only be shown once.')
            return new_key

    def encrypt_file(self):
        fernet = Fernet(self.key)

        with open('saved_pass.csv', 'rb') as file:
            og = file.read()

        encrypted = fernet.encrypt(og)

        with open('saved_pass.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        messagebox.showinfo('Files Done!', 'Your File Has Been Encrypted, The Program is now Locked')

        self.update_state('True')

    def decrypt_file(self):

        fernet = Fernet(self.key)

        with open('saved_pass.csv', 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open('saved_pass.csv', 'wb') as dec_file:
            dec_file.write(decrypted)

        messagebox.showinfo('Files Done!',
                            'Your File Has Been Un-encrypted, The Program is now Un-Locked and Passwords Are in Plain Text')

        self.update_state('False')

    def encrypt_decrypt(self):

        if self.check_state() is False:
            self.encrypt_file()

        elif self.check_state() is True:
            self.decrypt_file()
