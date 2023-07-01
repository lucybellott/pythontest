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


################################################################

from capitals import states
import random

def play_game():
    print("Greetings! How well do you know the geography of the United States?\nGuess the capitals of each state and test your knowledge!")
    random.shuffle(states)
    correct_answer_score = 0
    incorrect_answer_score = 0
    for state in states:
        capital_guess = input(f"What is the capital of {state['name']}?: ")
        # allows for more flexibility in the answers
        formatted_guess = capital_guess.lower().replace(".", "")
        formatted_answer = state['capital'].lower().replace(".", "")
        if formatted_guess == formatted_answer:
            correct_answer_score += 1
            print(f"Correct: {correct_answer_score} Incorrect: {incorrect_answer_score}")
        else:
            incorrect_answer_score += 1
            print(f"Incorrect. The capital of {state['name']} is actually {state['capital']}.\nCorrect: {correct_answer_score} Incorrect: {incorrect_answer_score}")
    print(f"Your final score is {correct_answer_score}!")
    play_again = input("Would you like to play again? (y or n)?: ")
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing! Come back soon!")


play_game()