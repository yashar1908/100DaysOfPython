from turtle import Turtle
from turtle import Screen

doodle = Turtle()

doodle.shape("turtle")
doodle.pencolor("Blue")
doodle.fillcolor("Green")

# Approach 1:
doodle.forward(100)  # go forward by x steps
doodle.right(90)  # rotate to the right by y degrees
doodle.forward(100)
doodle.right(90)
doodle.forward(100)
doodle.right(90)
doodle.forward(100)

# Approach 2:
i = 4
while i:
    doodle.forward(100)
    doodle.left(90)
    i -= 1

screen = Screen()
screen.exitonclick()
