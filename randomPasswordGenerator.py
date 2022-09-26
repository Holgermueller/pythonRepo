#from operator import truediv
import random
import string

character_length = 0
has_numbers = ''
has_symbols = ''


print('Generate a random password.')
print('Indicate how long you want the password to be.')
character_length_input = input()
character_length = int(character_length_input)

print("Would you like numbers in your password? y/n")
number_input = input()

if number_input == 'y':
    has_numbers = string.digits
else:
    has_numbers = ''

print('Would you like your password to have special characters? y/n')
symbol_input = input()

if symbol_input == 'y':
    has_symbols = string.punctuation
else:
    has_symbols = ''


print(''.join(random.choices(string.ascii_letters +
      has_numbers + has_symbols, k=character_length)))
