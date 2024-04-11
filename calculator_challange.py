from arts import calculator_logo
from replit import clear

print(calculator_logo)


def add(a, b):
    result = int(a + b)
    return result


def substract(a, b):
    result = int(a - b)
    return result


def muliply(a, b):
    result = int(a * b)
    return result


def division(a, b):
    result = int(a / b)
    return result


all_operations_dict = {
    "+": add,
    "-": substract,
    "*": muliply,
    "/": division
}


def calculator():
    num1 = float(input("what is the first number? : "))
    calculation_continue = True
    while calculation_continue:

        for operator in all_operations_dict:
            print(operator)
        operator_symbol = input("Pick the operator from the list above : ")
        num2 = float(input("what is the second number? : "))
        calculation = all_operations_dict[operator_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operator_symbol} {num2} = {answer}")
        calc_options = input(
            f"if you want to continue calculation with {answer} please press 'y'\nif you want to start a new calculation please press 'n'\nyou want to exit from the calculator please press 'e' : ")
        if calc_options == 'y':
            num1 = answer
        elif calc_options == 'n':
            clear()
            print(calculator_logo)
            num1 = float(input("Let's start the new calculation\nwhat is the first number : "))
        else:
            print(f"Recent calculation : {num1} {operator_symbol} {num2} = {answer}")
            calculation_continue = False


calculator()