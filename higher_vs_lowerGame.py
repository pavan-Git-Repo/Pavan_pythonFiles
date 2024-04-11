import random
from arts import higher_lower_Game_logo as logo
from arts import vs
from gameData import data
from replit import clear


def get_random_data():
  random_person_data = random.choice(data)
  return random_person_data


def get_extracted_data_from_Dict(random_data):
  name = random_data['name']
  followers_count = random_data['follower_count']
  description = random_data['description']
  country = random_data['country']
  return f"'Name': {name}; 'Description': {description}, from {country} ", followers_count


def check_correct_answer(guess, person_a_F_count, person_b_F_count):
  """Checking Who as the highest fan following"""
  if person_a_F_count > person_b_F_count:
    return guess == 'a'
  else:
    return guess == 'b'


def game():
  print(logo)
  score = 0
  continue_game = True
  # person_a = get_random_data()
  person_b = get_random_data()
  while continue_game:
    person_a = person_b
    person_b = get_random_data()
    # print(logo)
    print(f"Compare: {get_extracted_data_from_Dict(person_a)[0]}.")
    print(vs)
    print(f"Against: {get_extracted_data_from_Dict(person_b)[0]}.")
    guess = input(
      "Who has the highest fan following guess and choose an option like 'A' or 'B': "
    ).lower()

    person_a_F_count = get_extracted_data_from_Dict(person_a)[1]
    person_b_F_count = get_extracted_data_from_Dict(person_b)[1]

    is_guess_correct = check_correct_answer(guess, person_a_F_count,
                                            person_b_F_count)

    if is_guess_correct:
      # clear()
      score += 1
      print(f"You're Right, Your Current Score : {score}. ")
      print(f" {person_a['name']} has: {person_a_F_count} Followers.")
      print(f" {person_b['name']} has: {person_b_F_count} Followers.")
      print(
        f" Difference Between the count of fan Following: {abs(person_a_F_count - person_b_F_count)}. \n "
      )
      # clear()
    else:
      continue_game = False
      print(f" {person_a['name']} has: {person_a_F_count} Followers.")
      print(f" {person_b['name']} has: {person_b_F_count} Followers.")
      print(f" Difference Between the count of fan Following: {abs(person_a_F_count - person_b_F_count)}.")
      print(f"Sorry You're Wrong, Your Final Score : {score}. ")


if __name__ == '__main__':
  game()