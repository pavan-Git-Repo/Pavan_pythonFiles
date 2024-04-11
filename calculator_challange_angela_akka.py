from arts import calculator_logo



def add(a, b):
    result = a + b
    return result
def sub(a, b):
    result = a - b
    return result
def multi(a, b):
    result = a * b
    return result
def div(a, b):
    result = a / b
    return result

all_operators_dict = {"+": add,
                      "-": sub,
                      "*": multi,
                      "/": div}

def calculator():
    print(calculator_logo)
    num1 = float(input("Enter tne first number: "))
    for operator in all_operators_dict:
        print(operator)
    continue_calculation = True
    while continue_calculation:
        input_operator = input("Enter the operator like '+ - * /': ")
        num2 = float(input("Enter tne second number: "))
        calculation_output = all_operators_dict[input_operator]
        answer = float(calculation_output(num1, num2))
        print(f"{num1} {input_operator} {num2} = {answer}")
        continue_calc = input(f"Type 'y' to continue the calculation with {answer}, or 'n' to start the new calculation, or type 'e' to exit. : ")
        if continue_calc == 'y':
            num1 = answer
        elif continue_calc == 'n':
            # calculator()
            num1 = float(input("Enter tne first number: "))

        else:
            continue_calculation = False
            # exit(0)
if __name__ == '__main__':
    calculator()
