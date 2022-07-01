from turtle import Turtle
from turtle import Screen
import random

doodle = Turtle()
doodle.width(10)
doodle.speed(10)

directions = [0, 90, 270, 180]
colors = ["medium blue", "deep sky blue", "lime green", "dark green", "lime", "crimson", "maroon", "gold", "dark orchid"]

while True:
    direction = random.choice(directions)
    colour = random.choice(colors)
    doodle.color(colour)
    doodle.setheading(direction)
    doodle.forward(30)

screen = Screen()
screen.exitonclick()
