import random

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*_-+="
length = 0

digit_input = ''
punctuation_input = ''

password = ''

chars = alpha


print('How long do you want your password to be?')
character_lengt_input = input()
length = int(character_lengt_input)

print('Do you want numbers? y/n')
digit_input = input()

if digit_input == 'y':
    numbers = "0123456789"
else:
    numbers = ''


print('Do you want special characters? y/n')
punctuation_input = input()

if punctuation_input == 'y':
    symbols = "!@#$%^&*_-+="
else:
    symbols = ''

print(digit_input)
print(numbers)
print(punctuation_input)
print(symbols)
print(length)


print(password)
