import random
import string


user_choice = ""
random_letter = random.choice(string.ascii_letters)
user_tries = 26

while user_choice != random_letter:
    print("Guess the secret letter: ")
    print("Hint: The Letter could be capital or lower case!")
    print("You have a 50/50 chance of winning.")
    print("Attempts remaining: ")
    print(user_tries)
    print("Enter QUIT to exit the game.")

    user_choice = input()

    if user_choice == "QUIT":
        break

    if user_choice == random_letter:
        print("You won!")
        user_tries = 26
    else:
        print("Sorry, that's not the correct letter.")
        user_tries -= 1

    if(user_tries == 0):
        print("Sorry, but ran out of lives before guessing the correct letter.")
        print("The correct letter was " + random_letter)
        break

print("Thank you for playing. See you later.")
