import random


def generate_password():
    password = ''
    chars = "abcdefghijklmnopqrstuvwxyz"
    special_chars = "*/?$@!=/()&%_-"

    for c in range(10):
        char = random.choice(chars)
        if c % 2 == 0:
            password += char.upper()
            password += random.choice(special_chars)
        else:
            password += char

    for n in range(7):
        password += str(random.randint(0, 10))

    password_list = list(password)

    final_password = ""
    for c in password_list:
        final_password += random.choice(password_list)

    return final_password
