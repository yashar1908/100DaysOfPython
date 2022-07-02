from turtle import Turtle
from turtle import Screen

doodle = Turtle()
screen = Screen()

def move_forward():
    doodle.setheading(0)
    doodle.forward(10)
def move_upwards():
    doodle.setheading(90)
    doodle.forward(10)
def move_backward():
    doodle.setheading(180)
    doodle.forward(10)
def move_downwards():
    doodle.setheading(270)
    doodle.forward(10)

screen.listen() #tells the screen object to start listening for actions -- letting the screen know that it needs to look out for action listeners

screen.onkey(move_forward, "d")
screen.onkey(move_upwards, "w")
screen.onkey(move_backward, "a")
screen.onkey(move_downwards, "s")

screen.exitonclick()