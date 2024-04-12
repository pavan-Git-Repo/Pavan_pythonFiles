class card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank+ " of " +self.suit
mycards = card("Hearts","Two")
print(mycards)
        
1
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Sven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+ " of " +self.suit
mycards = card("Clubs",'Three')
two_hearts = card("Heart",'Two')
print(two_hearts.value < mycards.value)  

2
import random
suits = ('Hearts', 'Diamonds', 'Spades' , 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Sven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Sven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+ " of " +self.suit
mycards = card("Clubs",'Three')

3

import random
suits = ('Hearts', 'Diamonds', 'Spades' , 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Sven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Sven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+ " of " +self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = card(suit,rank)
                self.all_cards.append(created_card)
new_deck = Deck()
first_card = new_deck.all_cards[0]
print(first_card)

4

import random
suits = ('Hearts', 'Diamonds', 'Spades' , 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Sven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Sven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+ " of " +self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = card(suit,rank)
                self.all_cards.append(created_card)
new_deck = Deck()
for  card_object in new_deck.all_cards:
    print(card_object)

4 # shuffle cards

import random
#from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades' , 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+ " of " +self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
new_deck = Deck()
bottom_card = new_deck.all_cards[-1]
print(bottom_card)
new_deck.shuffle()
print(new_deck.all_cards[-1])
    
5 #popping


import random
#from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades' , 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+ " of " +self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()
#new_deck.shuffle()
mycard = new_deck.deal_one()
print(mycard)
print(len(new_deck.all_cards))

6 #cards game
import random 
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        pass
    def add_cards(self,new_card):
        pass
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
new_player = Player('moksha')
print(new_player)

7 #adding ,multiple adding,removing cards from game
import random 
suits = ('Hearts', 'Diamonds', 'Spades' , 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+ " of " +self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()

new_deck.shuffle()
mycard = new_deck.deal_one()
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
new_player = Player('moksha')

new_player.add_cards(mycard)
print(new_player)
print(new_player.all_cards[0])
new_player.add_cards([mycard,mycard,mycard])
print(new_player)
new_player.remove_one()
print(new_player) 