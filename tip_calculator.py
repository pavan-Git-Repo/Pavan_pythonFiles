"""Day2 Project Tip Calculator"""

bill_amount = float(input("Please enter the bill amount: "))
members = input("Please enter how many members you are: ")
tipPercent = float(input("Please enter the percentage of the tip on bill: "))/100 + 1
splitBill_withTip = round((float(bill_amount) / int(members)) * tipPercent)

print(splitBill_withTip)