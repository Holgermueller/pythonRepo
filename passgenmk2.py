import random

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*_-+="
length = 0

digitInput = ''
punctuationInput = ''

password = ''

chars = alpha

if digitInput == 'y':
    numbers = "0123456789"
else:
    numbers = ''

if punctuationInput == 'y':
    symbols = "!@#$%^&*_-+="
else:
    symbols = ''

print('How long do you want your password to be? y/n')
characterLengthInput = input()
length = int(characterLengthInput)

print('Do you want numbers? y/n')
digitInput = input()


print('Do you want special characters? y/n')
punctuationInput = input()

print(password)
