from turtle import Turtle
from turtle import Screen
import random

steps = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
colors = ["red", "blue", "green", "violet", "yellow", "orange"]

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

turtles = [t1,t2,t3,t4,t5,t6]

screen = Screen()
screen.setup(width = 500,height = 400) # height, width

guess = screen.textinput("Guess the winner", "Which turtle do you think will win?")

for t in turtles:
    t.shape("turtle")
    t.color(colors[0])
    colors.remove(colors[0])
    t.penup()

t1.setposition(-240, 150)
t2.setposition(-240, 100)
t3.setposition(-240, 50)
t4.setposition(-240, 0)
t5.setposition(-240, -50)
t6.setposition(-240, -100)

race_over = False


while not race_over:
    for t in turtles:
        t.forward(random.randint(1,5))
        if t.xcor() > 230:
            race_over = True
            winner = t.pencolor()

if winner == guess:
    print(f"You won! {winner} is the winner!")
else:
    print(f"You lost! {winner} is the winner")


screen.exitonclick()


