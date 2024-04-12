print('Welcome to Iron Bank of Bravoos ATM')
restart = ('y')
chances = 3
balance = 670.14


while chances >=0:
    pin = int(input('Please enter your 4 digit pin: '))
    if pin == (1234):
        print('You entered your pin correctly\n')
        while restart not in ('n','No','no','N'):
            print('Please press 1 for your Balance\n')
            print('please press 2 to make Withdrawl\n')
            print('please press 3 to pay in\n')
            print('please press 4 to return card\n')
            option = int(input("please select a number: "))
            if option == 1:
                print('Your balance is Rs' ,balance,'\n')
                restart = input('Would you like to go back? ')
                if restart in ('n','No','no','N'):
                    print('Thank you')
                    break
            elif option == 2:
                restart = ('y')
                withdrawl = float(input('How much would you like to withdraw? \nRs100/Rs200/Rs300/Rs400'))
                if withdrawl in [100,200,300,400]:
                    balance = balance-withdrawl
                    print('\nYour account balance now Rs', balance)
                    restart = input('Would to like to go back? ')
                    if restart in ('n','No','no','N'):
                        print('Thank you')
                        break
                elif withdrawl != [100,200,300,400]:
                    print('Invalid amount re-try\n')
                    restart = ('y')
                elif withdrawl ==1:
                    withdrawl = float(input('Please enter desired amount: '))
            elif option == 3:
                pay_in = float(input('How much would you like to pay in? '))
                balance = balance + pay_in
                print('\n Your balance is now Rs', balance)
                restart = input('Would you like to go back?' )
                if restart in ('n','No','no','N'):
                    print('Thank you')
                    break
            elif option ==4:
                print('Please wait while your card is returned...\n')
                print('Thank you for your service')
                break
            else:
                print('Please enter a correct number. \n')
                restart = ('y')
    elif pin != (1234):
        print('Incorrect password')
        chances = chances - 1
        if chances ==0:
            print('\nno more tries')
            break
