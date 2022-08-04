import random
import string


userChoice = ""
randomLetter = random.choice(string.ascii_letters)
userTries = 26

while True:
    print("Guess the secret letter: ")
    print("Hint: The Letter could be capital or lower case!")
    print("Attempts remaining: ")
    print(userTries)
    print("Enter QUIT to exit the game.")

    userChoice = input()

    if userChoice == "QUIT":
        break

    if userChoice == randomLetter:
        print("You won!")
        userTries = 26
    else:
        print("Sorry, that's not the correct letter.")
        userTries -= 1

    if(userTries == 0):
        print("Sorry, but ran out of lives before guessing the correct letter.")
        print("The correct letter was " + randomLetter)
        break

print("Thank you for playing. See you later.")
