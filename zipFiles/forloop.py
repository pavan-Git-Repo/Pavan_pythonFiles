for i in [0,1,2]:
    print("Hello world")
for i in range(7):
    print("Hello world")
for i in range(3,1):
    print("Hello world")
2
lst = [x**2 for x in range(0,11)]
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst)
3
fruits = [ "mango", "banana","apple"]
for fruit in fruits:
    print("myfruit: ", fruit)
print("The end")
4
from math import factorial


num = int(input("Number: "))
factorial = 1
if num<0:
    print("must be positive")
elif num==0:
    print("factorial = 1")
else:
    for i in range(1,num+1):
        factorial = factorial*1
print(factorial)

5
from math import sqrt
n = int(input("Maximal number? "))
for a in range(1,n+1):
    for b in range(a,n):
        c_squar = a**2 + b**2
        c = int(sqrt(c_squar))
        if ((c_squar - c)==0):
            print(a,b,c)
x= int(input(''))
sum = 0 
for i in range(x):
    sum = sum+i
    print(sum)
    
n=5
sum = 0
for i in range(0,n):
    sum = sum+i
    print(sum)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
for fruit in fruits:
    print(fruit)
    print(fruit +"pie")