from shutil import copy
import string
import secrets
import random


def generate_random(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    return crypt


for i in range(1, 100):
    s = random.randint(10000, 200000)
    chp = open("C:/1/text.txt", "w")
    chp.write(generate_random(s))
    copy("C:\\1\\text.txt", "C:\\1\\text" + str(i) + ".txt")
