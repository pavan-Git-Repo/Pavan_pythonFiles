import replit
from replit import clear
from arts import auction_logo
print(logo)
"""
bids = {}
bidding_finished = False

def find_highest_bidder(biddind_record):
    highest_bid = 0
    winner = ""
    for each_bidder in biddind_record:
        bid_amount = biddind_record[each_bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = each_bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid? $"))
    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes or no'.\n")
    if should_continue == 'no':
        bidding_finished = True
    elif should_continue == 'yes':
        clear()

find_highest_bidder(bids)
# print(name)
# print(bid_price)
"""

bid_record = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid_price = 0
    winner = ""
    for each_bidder in bidding_record:
        bid_amount = bid_record[each_bidder]
        if bid_amount > highest_bid_price:
            highest_bid_price = bid_amount
            winner = each_bidder
    print(f"The winner is {winner} with the bid amount of {highest_bid_price}")



while not bidding_finished:
    name = input("What is your name? : ")
    bid_price = int(input("What is your bid price? :"))
    bid_record[name] = bid_price
    bidder_continue = input("Are there any other bidder? enter 'yes or no': ")
    if bidder_continue == 'no':
        bidding_finished = True
    elif bidder_continue == 'yes':
        clear()

find_highest_bidder(bid_record)


