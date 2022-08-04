import random
import string

userChoice = ""
randomLetter = random.choice(string.ascii_letters)

print("Guess the secret letter: ")
print(randomLetter)
userChoice = input()

if userChoice == randomLetter:
    print("You won!")
else:
    print("Sorry, that's not the correct letter.")
