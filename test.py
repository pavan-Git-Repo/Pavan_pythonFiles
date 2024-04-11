# import random
#
# from arts import black_jack_logo
# from arts import cards
# from arts import cards_dict
# print(black_jack_logo)
# # print(cards)
# # print(len(cards))
#
#
# def deal_card():
#     cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards_list)
#     if card == 10:
#         ten_card = random.choice(cards_dict[str(card)])
#         print(ten_card)
#         return card
#     else:
#         card_art = random.choice(cards_dict[str(card)])
#         print(card_art)
#     return card
#
# user_cards = []
# computer_cards = []
#
# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())
# print(user_cards)
# print(computer_cards)
#
#
#
# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
#
#
# a_function(10)
# print(a_variable)

#
# i = 50
#
#
# def foo():
#     i = 100
#     return i
#
#
# foo()
# print(i)

def bar():
    my_variable = 9

    if 16 > 9:
        my_variable = 16

    print(my_variable)


bar()