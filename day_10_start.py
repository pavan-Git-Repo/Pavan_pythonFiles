"""
def formatName(f_name, l_name):
    finalupdated_f_name = f_name.replace(f_name, f_name[0].upper()) + f_name[1:]
    finalupdated_l_name = l_name.replace(l_name, l_name[0].upper()) + l_name[1:]
    print(finalupdated_f_name + ' ' + finalupdated_l_name)

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
formatName(first_name, last_name)
"""

"""
def nameFormat(f_name, l_name):
    final_updated_f_name = f_name.title()
    final_updated_l_name = l_name.title()
    print(final_updated_f_name + ' ' + final_updated_l_name)

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
nameFormat(first_name, last_name)
"""


def nameFormat(f_name, l_name):
    if f_name == "" or l_name == "":
        return print("You do not entered the valid input. \n please enter the valid input and try again.")
    final_updated_f_name = f_name.title()
    final_updated_l_name = l_name.title()
    final_string = f"result: {final_updated_f_name} {final_updated_l_name}"
    return final_string

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
print(nameFormat(first_name, last_name))