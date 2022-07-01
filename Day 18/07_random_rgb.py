from turtle import Turtle
from turtle import Screen
import random

doodle = Turtle()
doodle.width(10)
doodle.speed(10)

# screen.colormode(255)
# There are 2 colormodes which signify how you address r, g, b values for your turtle
# Either your rgb values can range from 0 to 1 (colormode(1)) or 
# They can range from 0 to 255 which is the standard way.


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    tup = (r, g, b)
    return tup


directions = [0, 90, 270, 180]

while True:
    direction = random.choice(directions)
    doodle.color((random.random(), random.random(), random.random()))
    doodle.setheading(direction)
    doodle.forward(30)


screen = Screen()
screen.exitonclick()