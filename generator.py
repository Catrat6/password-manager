import string
import random
from random_word import RandomWords


ALPHA = list(string.ascii_lowercase)
ALPHA_UPPER = list(string.ascii_uppercase)
NUM = list(range(1, 11))


def generate_new(length):

    characters = [ALPHA, ALPHA_UPPER, NUM]

    password = []

    for each in range(1, length):
        a = random.choice(characters)
        a = random.choice(a)
        password.append(str(a))
        random.shuffle(password)

    final = ''.join(password)

    return final

def remix_string(password):

    n_list = [each for each in password]

    for each in range(len(password)):
        random.shuffle(n_list)

    final = "".join(n_list)

    return final

def pass_phrase(length):
    r = RandomWords()
    phrase = [r.get_random_word() for each in range(1, length)]
    final = " ".join(phrase)

    return final


