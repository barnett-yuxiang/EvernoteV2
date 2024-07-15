# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#
# passward = ""
# random_char = random.choice(letters)
# print(random_char)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Hard Level
#
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list) # key function to shuffle the list
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")


# The provided code snippet is a password generator that creates a password based on user input for the number of letters, symbols, and numbers. The code has a minor typo and can be improved for efficiency and readability. Here's an improved version:

# Correct the typo in the variable name passward to password.
# Use list comprehensions to simplify the loops for adding letters, symbols, and numbers to the password list.
# Combine the final password creation step into a single line using the join() method.
#
# Hard Level - Order of characters randomised:
password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                [random.choice(symbols) for _ in range(nr_symbols)] + \
                [random.choice(numbers) for _ in range(nr_numbers)]

random.shuffle(password_list)  # Shuffle the list to randomize the order of characters

password = "".join(password_list)  # Combine the characters into a single string

print(f"Your password is: {password}")
