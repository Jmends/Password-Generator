import random
#list of possible symbols, numbers, and letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#collects input of how many of letters, symbols, and numbers the user would like
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

#appends letters, numbers, and symbols into list called password
for char in range(nr_letters):
  password.append(random.choice(letters)) 

for char in range(nr_symbols):
  password.append(random.choice(symbols))

for char in range(nr_numbers):
  password.append(random.choice(numbers)) 

#shuffles password for more security
random.shuffle(password)

#joins together the password list to create ine string
password = "".join(password)
print(password)
