import random
from random import randint
from arts import guess_logo
print(guess_logo)


EASY_LEVEL = 10
HARD_LEVEL = 5


def checking_correct_answer(user_guess, correct_answer, no_turns):
    if user_guess > correct_answer:
        print(f"Your guessing is {user_guess} very high. ")
        # print("Guess again.")
        return no_turns - 1
    elif user_guess < correct_answer:
        print(f"Your guessing is {user_guess} very low. ")
        # print("Guess again.")
        return no_turns - 1
    elif user_guess < correct_answer - 5:
        print(f"Your guessing is {user_guess} very near. ")
        # print("Guess again.")
    elif user_guess == correct_answer:
        print(f"Your guess is Correct! The Correct Guess was **** {correct_answer} ****")
        # print(f"you got it with in the {no_turns + 1} attempts. ")


def set_difficulty_level():
    user_difficulty_input = input("Please choose your difficulty level press 'hard', 'h' or 'easy', 'e' : ")
    if user_difficulty_input == "hard" or user_difficulty_input == 'h':
        return HARD_LEVEL
    elif user_difficulty_input == 'easy' or user_difficulty_input == 'e':
        return EASY_LEVEL
    else:
        print("Please choose the valid Option for difficulty level.")
        return set_difficulty_level()

def guess_game():
    print("Welcome to the nuber Guessing Game.")
    print("I think my guessing is that the number is in between '1' and '100'. ")
    correct_answer = random.randint(1, 100)
    no_turns = set_difficulty_level()
    user_guess = 0

    while user_guess != correct_answer:
        print(f"You have {no_turns} attempts remaining to guess the number.")
        user_guess = int(input("Please enter your guess: "))
        no_turns = checking_correct_answer(user_guess, correct_answer, no_turns)
        if no_turns == 0:
            print("You run out of guesses, you lose")
            print(f"The Correct Guess is {correct_answer} ")
            return
        elif user_guess != correct_answer:
            print("Guess again.")

guess_game()


