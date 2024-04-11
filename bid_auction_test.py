import replit
from replit import clear
from arts import auction_logo
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