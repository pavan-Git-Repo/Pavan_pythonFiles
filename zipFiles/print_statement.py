print("I'm going to inject %s here." %'something')
2
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))
3
print('He said his name was %s.' %'Fred')
print('He said his name was %r.' %'Fred')
4
print('I once caught a fish %s.' %'this \tbig')
print('I once caught a fish %r.' %'this \tbig')
5
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75) 
6
print('Floating point numbers: %5.2f' %(13.144))
print('Floating point numbers: %10.2f' %(13.144))
7
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
8
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
9
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
10
print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))
11
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
12
s = "Hello world"
print(s[::2])

13
x = 10
name ='name'
print(str(x)+name)
14 
a = 10
a**=5
print(a)
14 #ascii table
print(ord('a'))

15 
a = input("a: ")
b = input("b: ")

a,b = b,a
print("a: " + a)
print("b: " + b)

16
two_digit = input("give two digits: ")
c = int(two_digit)
a = c//10
b = c%10
print(a)
print(b)
e = a + b
print(e)