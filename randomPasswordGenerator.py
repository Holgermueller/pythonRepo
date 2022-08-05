from operator import truediv
import random
import string

characterLength = 0
digitsVariable = string.digits
digitsInput = ''
punctuationVariable = string.punctuation
punctuationInput = ''

if digitsInput == 'y':
    digitsVariable = random.choices(string.digits)
else:
    digitsVariable = ''

if punctuationInput == 'y':
    punctuationVariable = random.choices(string.punctuation)
else:
    punctuationVariable = ''

print('Generate a random password.')
print('Indicate how long you want the password to be.')
characterLengthInput = input()
characterLength = int(characterLengthInput)
print('Do you want digits in your password: y/n')
digitsInput = input()
print(digitsVariable)
print('Do you want punctuation in your password: y/n')
punctuationInput = input()
print(''.join(random.choices(string.ascii_letters +
      digitsVariable + punctuationVariable, k=characterLength)))
