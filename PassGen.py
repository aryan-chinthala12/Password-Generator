import random
import string

def generate_pass(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

try:
    length = int(input('Enter the length of the password: '))
    if length < 4:
        print("The password must be at least 4 characters long")
    else:
        password1 = generate_pass(length)
        print(f"The generated password is: {password1}")
except ValueError:
    print("Enter a valid length....")
