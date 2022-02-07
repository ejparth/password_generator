#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random

password = []
total_length = 0
total_length = nr_letters + nr_numbers + nr_symbols



for i in range(0,total_length):
  selector = random.randint(0,2)
  if selector == 0:
    index = random.randint(0,len(letters))
    password.append(letters[index])
  elif selector == 1:
    index = random.randint(0,len(symbols))
    password.append(symbols[index])
  elif selector == 2:
    index = random.randint(0,len(numbers))
    password.append(numbers[index])

full_pass = ""  #from line 38 to 40 converting list to string"
for i in password:
  full_pass+=i

print (f"The full password is:{full_pass}") 