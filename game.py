# Build a command line app to let users guess a random number
# Build a command line app that does the following:

# - Pick a random number between 0 and 100
# - Ask the user to guess the number
# - If the guess is correct, tell the user they guessed correctly and ask if they'd like to play again.
# - If the guess is incorrect, tell the user it's incorrect and ask them for another guess. This action will repeat until the user gives the correct number.
# - When the user guessed correctly and chose to play again, a new random number is selected. The user will need to guess the new number.

import random

def random_num():
    play_again = "y"
    while play_again.lower() == "y":
        comp_num = random.randrange(0, 10)
        user_num = int(input("Pick a number between 0-10!: "))
        while user_num != comp_num:
            user_num = int(input("Incorrect. Try again: "))
        play_again = input("Winner! Would you like to play again?(y or n): ")
    print("Thanks for playing!")

random_num()