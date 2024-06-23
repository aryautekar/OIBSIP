import random
import string

def generate_password(length, char=True, digits=True, symbols=True):
    characters = ""
    if char:
        characters += string.ascii_letters
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected.")
        return None
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Welcome to the Password Generator!")
length = int(input("Enter the length of the password: "))
char = input("Include letters? (yes/no): ").lower() == "yes"
digits = input("Include numbers? (yes/no): ").lower() == "yes"
symbols = input("Include symbols? (yes/no): ").lower() == "yes"

password = generate_password(length, char, digits, symbols)
print("Your generated password is:", password)
