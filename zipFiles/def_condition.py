
1
def employee_check(work_hours):
    
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours>current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)
work_hours = [('Tani' ,100), ('Moki', 200), ('pratyu' ,90)]
print(employee_check(work_hours))

2
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
print(makes_twenty(22,25))

3
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
print(has_33([1,3,3]))
        
4
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i:i+2]==[3,3]:
            return True
        else:
            return False
print(has_33([1,3,3,1,5]))

5
def three_times(text):
    result = ''   
    for letters in text:
        result += letters*3
    return result
text = 'hello'
print(three_times(text))

6
name = ' THIS IS A GLOBAL STRING'
def greet():
    name = 'Moksha'
    def hello():
        print('Hello '+name)
    hello()
greet()

7
x = 50
def func(x):
    print(f'X is {x}')
print(func(x))

8
def valume_(rad):
    return (4/3)*(3.14)*(rad**3)
print(valume_(2))

9
def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range of low and high')
    else:
        print('not in range')
ran_check(5,3,7)

10 
import string
def up_low(s):
    upper_case = 0
    lower_case = 0
    for item in s:
        if item.isupper():
            upper_case += 1
        elif item.islower():
            lower_case += 1
        else:
            pass
    return (f'Number of uppercase: {upper_case}') , (f'Number of lowercase: {lower_case}')
s = 'Hello Mr. Rogers'
print(up_low(s))

11 
def unique_list(mylist):
    return list(set(mylist))
print(unique_list([1,1,2,3,2,4,2,3,3,5,6,7]))

12
def multiply(nums):
    total = 1
    for num in nums:
        total = total*num
    return total
print(multiply([1,2,3,-4]))

def addition(nums):
    total = 0
    for num in nums:
        total = total+num
    return total
print(addition([1,2,3,4,5,6]))

13
def create_cube(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result
print(create_cube(3))
14
def create_cube(n):
    for x in range(n):
        yield x**3
for x in create_cube(10):
    print(x)

13
def polindrom(s):
    s = s.replace(' ','')
    return s == s[::-1]
print(polindrom('nur s es r un'))
14

def func1(functi):
    def wrapper():
        print("Hello")
        functi()
        print("Welcome to the class")
    return wrapper
def func2():
    print("pythonista")
func2 = func1(func2)
func2()

15
#map in def
def new(a):
    return a*a
x = map(new,[1,2,3,4])
print(tuple(x))
16
#map in def
def new(a,b):
    return a*b
x = map(new,[1,2,3,4],[6,7,8,9])
print(tuple(x))

def new1(i):
    if i>=3:
        return i
j = filter(new1,(1,2,3,4,5,6)) 
print(list(j))

17

def foo(a, b=4, c=6):
    print(a, b, c)
 
foo(20, c=12)

18
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2:
      return 29
  return month_days[month-1]
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

19 
def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 

operations = {"+": add,"-":subtract,"*":multiply,"/":divide}
num1 = int(input("What is your first number: "))
num2 = int(input("What is your last number: "))
for symbol in operations:
    print(symbol)
operation_symbol=input("Pick an operating from the line above: ")
calculation_operation = operations[operation_symbol]
answer = calculation_operation(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

20

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
operations = {"+": add,"-":subtract,"*":multiply,"/":divide}

def calculator():
    num1 = int(input("What is your first number: "))
    
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol=input("Pick an operating from the line above: ")
        
        num2 = int(input("What is your last number: "))
        calculation_operation = operations[operation_symbol]
        answer = calculation_operation(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
          num1= answer
        else:
          should_continue=False
          calculator()
calculator()

21
def fun_one(n):
    return[str(num) for num in range(n)]
print(fun_one(10))
def fun_two(n):
    return list(map(str,range(n)))
print(fun_two(10))