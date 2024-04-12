import random
random.seed(101)
print(random.randint(0,100))

import random
mylist = list(range(0,30))
print(random.choice(mylist))
print(random.choices(population=mylist,k=10))

#random.random() gives 0 to 1 float numbers
import random
random_int = random.randint(1,10)
random_float = random.random()
print(random_float)
#random.uniform gives float number between given numbers
random_flt= random.uniform(1,10)

#it will gives random choices to choose
my_lst = ["hii","hello","hey"]
random_choice = random.choice(my_lst)
print(random_choice + ' Moki')

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


random_number= random.randint(0,len(names)-1)
random_name = names[random_number]
    
print( random_name + " is going to buy the meal today!")


from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])