square = lambda num: num**2
print(square(5))

my_nums = [1,2,3,4,5,6]
print(list(map(lambda num: num**2,my_nums)))
    
my_nums = [1,2,3,4,5,6]
print(list(filter(lambda num: num%2==0,my_nums)))

def A(x):
    return(lambda y:x+y)
t = A(7)
print(t(7))

#map (functins, iterables)
mylist = [1,2,3,4,5,6]
result = list(map(lambda a:(a/3!=2),mylist))
print(result)

import functools
from functools import reduce
print(reduce(lambda a,b:a+b,[21,34,5,678,988]))

func = lambda x,y: 3*x+4*y
print(func(2,6))

x = filter(lambda a: (a>=3),(1,2,3,4,5,6))
print(list(x))