import os.path

from cryptography.fernet import Fernet


class EncryptionModule:

    def __init__(self):
        self.key = self.load_key()

    def load_key(self):
        if os.path.exists('key.txt'):
            with open('key.txt', 'rb') as key:
                return key.read()
        else:
            new_key = Fernet.generate_key()
            with open('key.txt', 'wb') as key:
                key.write(new_key)
            return new_key

    def encrypt_password(self, password):
        cipher_suite = Fernet(self.key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        cipher_suite = Fernet(self.key)
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password
