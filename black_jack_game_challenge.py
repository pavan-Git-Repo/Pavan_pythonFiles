from arts import black_jack_logo
import random
from replit import clear

def deal_card():
  card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(card_list)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    print("BLACK JACK")
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "You Lose, opponent has BlackJack 😱"
  elif user_score == 0:
    return "You Win with the BlackJack 😎"
  elif user_score > 21:
    return "You went over, You Lose 😤"
  elif computer_score > 21:
    return "Opponent went over, You win 😁"
  elif user_score < 21 and user_score > computer_score:
    return "You win 😁"
  elif user_score > 21 and computer_score > 21:
    return "You went Over, You lose "
  else:
    return "You lose 😤"

def play_BlackJack_Game():
  print(black_jack_logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over:
    # print(user_cards)
    # print(computer_cards)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   your cards : {user_cards}, current Score: {user_score}")
    print(f"   Computer's Firs card : {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final Score: {user_score}")
  print(f"   Computer's  final hand: {computer_cards}, final Score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play game of BlackJack? Type 'y' or 'n': ") == 'y':
  clear()
  play_BlackJack_Game()


