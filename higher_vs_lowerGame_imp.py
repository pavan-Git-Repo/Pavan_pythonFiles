from arts import higher_lower_Game_logo as game_logo
from arts import vs as vs_logo
from gameData import data
import random
from replit import clear

def get_random_data():
    random_person_data = random.choice(data)
    return random_person_data

def extract_data_from_dict(random_data):
    name = random_data['name']
    follower_count = random_data['follower_count']
    description = random_data['description']
    country = random_data['country']
    return f"'Name': {name} ; 'Description': {description}, from {country}", follower_count

def check_answer(guess, person_a_follower_count, person_b_follower_count ):
    if person_a_follower_count > person_a_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    print(game_logo)
    score = 0
    continue_game = True
    person_a = get_random_data()
    person_b = get_random_data()
    while continue_game:
        print(f"Compare: {extract_data_from_dict(person_a)[0]}")
        print(vs_logo)
        print(f"Against: {extract_data_from_dict(person_b)[0]}")
        guess = input("Who has the highest Fan Following guess and choose one option like 'A' or 'B' : ").lower()
        person_a_follower_count = extract_data_from_dict(person_a)[1]
        # print(person_a_follower_count)
        person_b_follower_count = extract_data_from_dict(person_b)[1]
        # print(person_b_follower_count)
        while person_a == person_b:
            person_a = get_random_data()
        while person_b == person_a:
            person_b = get_random_data()

        is_correct = check_answer(guess, person_a_follower_count, person_b_follower_count)
        if is_correct:
            clear()
            score += 1
            print(f"You're Right, Your Score is {score} ")
            person_a = person_b
        else:
            continue_game = False
            print(f"Sorry You're Wrong, You're Final Score is {score}")

game()