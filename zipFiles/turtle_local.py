from turtle import Turtle,Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('red','green')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()  

##2

from turtle import Turtle,Screen
timmy = Turtle()
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)
# or 
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)

#3
from turtle import *
timmy  = Turtle()
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    

#4
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

#5
import turtle as t
import random
timmy = t.Turtle()
colours = ["red","CornflowerBlue","DeepSkyBlue","wheat","LightSeaGreen","SlateGray","SeeGreen"]

def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for  _ in range(num_of_sides):
        timmy.forward(100)
        timmy.right(angle)
for shade_side_n in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(shade_side_n)

#6
import turtle as t
import random
timmy = t.Turtle()
t.colormode(255)
def random_clo():
    r = random.randint(0,255)
    g= random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b
directions  = [0,90,180,270]
timmy.pensize(15)
timmy.speed("fastest")
for _ in range(200):
    timmy.color((random_clo()))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

#7
import turtle as t
import random 
timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
def random_clo():
    r = random.randint(0,255)
    g= random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors
def draw_spirograph(size_of_gap):

    for circles in range(int(360/size_of_gap)):
        timmy.color(random_clo())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)
draw_spirograph(6)
screen=t.Screen()
screen.exitonclick()

#8


import colorgram
rgb_colors = []
colors = colorgram.extract("C:\\Users\\91817\\Downloads\\sweet_pic.jpg",30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)


###
import turtle as turtle_module
import random
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

color_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
num_of_dots = 100
def random_clo():
    r = random.randint(0,255)
    g= random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

for dot_count in range(1, num_of_dots-1):
    timmy.dot(random_clo())
    timmy.forward(50)

    if dot_count%10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
screen = turtle_module.Screen()

##
from turtle import Turtle,Screen
timmy = Turtle()
screen = Screen()

def move_forwrd():
    timmy.forward(10)
screen.listen()
screen.onkey(key="space",fun=move_forwrd)
screen.exitonclick()
#after this press spacebar


##
from turtle import Turtle,Screen, clear
timmy = Turtle()
screen = Screen()

def move_forwrd():
    timmy.forward(10)
def move_backwards():
    timmy.backward(10)
def turn_left():
    new_heading  = timmy.heading()+10
    timmy.setheading(new_heading)

def turn_right():
    new_heading  = timmy.heading()-10
    timmy.setheading(new_heading)
def all_clear(): 
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
screen.listen()
screen.onkey(move_forwrd,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
all_clear()
screen.exitonclick()


        
