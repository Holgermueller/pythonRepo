import random
import string

userChoice = ""
randomLetter = random.choice(string.ascii_letters)

while True:
    print("Guess the secret letter: ")
    print("Enter QUIT to exit the game.")
    print(randomLetter)
    userChoice = input()

    if userChoice == "QUIT":
        break

    if userChoice == randomLetter:
        print("You won!")
    else:
        print("Sorry, that's not the correct letter.")

print("Thank you for playing. See you later.")
