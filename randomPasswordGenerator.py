from operator import truediv
import random
import string

characterLength = 0


print('Generate a random password.')
print('Indicate how long you want the password to be.')
characterLengthInput = input()
characterLength = int(characterLengthInput)


print(''.join(random.choices(string.ascii_letters +
      string.digits + string.punctuation, k=characterLength)))
