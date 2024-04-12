class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        self.breathe = "watever"
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()
## see the difference by override means parent and child clss objects using same functions

class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"
doggo = Dog()
print(f"A dog is {doggo.temperament}")
 
sparky = Labrador()
print(f"Sparky is {sparky.temperament}")
