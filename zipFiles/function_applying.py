class Calculation:
  
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def add(self,addition):
        return self.arg1+self.arg2
    def sub(self):
        return self.arg1-self.arg2
    def mul(self):
        return self.arg1*self.arg2
    def div(self):
        return self.arg1/self.arg2
calc = Calculation(2,3)
print(calc.add())
# def calc(arg1, operator, arg2):
#     if type(arg1) and type(arg2) == int:
#         print("you have entered integer to calcuate")
#     else:
#         print("you have entered a non integer element here....")
#         print("Please enter an integer according to this calculation. ")
#     if operator == "+":
#         print("Addition of given integers== ", arg1 + arg2)
#     elif operator == "-":
#         print("Subtraction of given integers== ", arg1 - arg2)
#     elif operator == "*":
#         print("Multiplication of given integers== ", arg1 * arg2)
#     elif operator == "/":
#         print("Division of given integers== ", arg1 / arg2)
#     else:
#         print("operator is not found (or) selected ")
# if _name_ == '_main_':
#     arg1 = int(input("Give an first integer: "))
#     operator = input("Please select an operator like +, -, *, /  : ")
#     agr2 = int(input("Give a second integer: "))

#     calc(arg1, operator, agr2)
