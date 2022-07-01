from turtle import Turtle 
from turtle import Screen
import random

doodle = Turtle()
doodle.speed("fastest")

while True:
    doodle.color((random.random(), random.random(), random.random()))
    doodle.circle(100)
    doodle.right(5)



screen = Screen()
screen.exitonclick()