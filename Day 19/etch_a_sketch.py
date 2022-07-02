from turtle import Turtle
from turtle import Screen

doodle = Turtle()
screen = Screen()

def move_forward():
    doodle.forward(10)
def move_backward():
    doodle.backward(10)
def turn_left():
    doodle.setheading(doodle.heading()+10)
def turn_right():
    doodle.setheading(doodle.heading()-10)
def clear():
    doodle.clear()
    doodle.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
