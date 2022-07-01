from turtle import Turtle
from turtle import Screen

doodle = Turtle()

for i in range(0, 50):
    doodle.forward(5)
    doodle.penup()
    doodle.forward(5)
    doodle.pendown()

screen = Screen()
screen.exitonclick()

# turtle.penup() / turtle.up(): no drawing happens when the pen is up. Used to lift the pen and move the cursor
# turtle.pendown() / turtle.down(): no drawing happens until the pen is put back down.
