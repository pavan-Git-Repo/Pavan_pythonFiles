class Sample():
    pass
my_sample = Sample()
print(type(my_sample))

2
class Dog():

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
my_dog = Dog(breed='lab',name='sammy')
print(my_dog.name)

3

class Dog():

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    def bark(self,number):
        print("woof! my name  is {} and my number is {}".format(self.name,number))
my_dog = Dog("Lab","franky")
my_dog.bark(10)

class Circle():
    pi = 3.14

    def __init__(self,radious=1):
        self.radious = radious
    def another_circle(self):
        return self.radious*self.pi*2
my_circle = Circle()
print(my_circle.radious)

class Circle():
    pi = 3.14

    def __init__(self,radious=1):
        self.radious = radious
    def another_circle(self):
        return self.radious*self.pi*2
my_circle = Circle(20)
print(my_circle.radious)

3

class Circle():
    pi = 3.14

    def __init__(self,radious=1):
        self.radious = radious
    def another_circle(self):
        return self.radious * self.pi * 2
my_circle = Circle(30)
print(my_circle.another_circle())

4
class Circle():
    pi = 3.14

    def __init__(self,radious=1):
        self.radious = radious
        self.area = radious*radious*self.pi
    def another_circle(self):
        return self.radious * self.pi * 2
my_circle = Circle(30)
print(my_circle.area)

5
class Animal():
    def __init__(self):
        print('Animal created')
    def who_are_u(self):
        print('I am an animal')
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog is created')
myanimal = Dog()

6
class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says woof!'
cuty = Dog('cuty')
print(cuty.speak())

7 # __str__ working
class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author 
        self.pages = pages
    def __str__(self):
        return f"{self.name} by {self.author}"
b = Book('pythan','jatin','45')
print(b)

8 #without __str__working
class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author 
        self.pages = pages
b = Book('pythan','jatin','45')
print(b.name)

9 #__len__working
class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author 
        self.pages = pages
        
    def __len__(self):
        return self.pages
b = Book('pythan','jatin',45)
print(len(b))

10 
class line():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1) / (x2-x1)
c1 = (3,2)
c2 = (7,8)
myline = line(c1,c2)
print(myline.distance())

11
class Account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep_amount):
        self.balance = self.balance + dep_amount
        print(f"Amount {dep_amount} added to your account")
    def withdraw(self,wtdraw_amt):
        if self.balance >= wtdraw_amt:
            self.balance = self.balance - wtdraw_amt
            print("withdraw accepted")
        else:
            print("Sorry insufficient balance ")
myaccount = Account('jyoshna',500)
myaccount.deposit(200)

12
class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author 
        self.pages = pages
b = Book('pythan','jatin','45')
print(b.__dict__)


