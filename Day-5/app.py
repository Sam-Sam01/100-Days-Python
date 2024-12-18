import random
import string

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like to generate in your password?"))
nr_symbols = int(input(f"How many characters would you like to generate in your password?"))
nr_numbers = int(input(f"How many numbers would you like to generate in your password?"))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
password_list = []
password = ""
for char in range(1, nr_letters+1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
for n in password_list:
    password += n

print(f"Your generated password is: {password}")
