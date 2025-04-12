# Password Generator

import random
import string

def Password_generated(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input ("Enter the length of your desired password:" ))
password = Password_generated(length)
print("Your desired password generator:" , password)