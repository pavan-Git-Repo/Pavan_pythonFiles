loc = 'Bank'

if loc == 'auto shop':
    print('cars are cool')
else:
    print('i do not know much')


for num in range(0,101):
    if num%3 == 0 and num%5 == 0:
        print('FIZZBUZZ')
    elif num%3 == 0:
        print('FIZZ')
    elif num%5 == 0:
        print('BUZZ')
    else:
        print(num) 


def makes_twenty(n1,n2):
    if n1+n2==20:
        return True
    elif n1==20:
        return True
    elif n2==20:
        return True
    else:
        return False
print(makes_twenty(2,18))


def blackjack(a,b,c):
    if sum([a,b,c])<=21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])<=31:
        return sum([a,b,c])-10
    else:
        return 'BUST'
print(blackjack(10,7,11))
#finding largest number among 3 numbers

a=10
b=12
c=8
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)