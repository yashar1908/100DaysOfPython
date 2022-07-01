from turtle import Turtle
from turtle import Screen

doodle = Turtle()  # creating an object of the Turtle class

doodle.shape("turtle")  # used to change the shape of the cursor on the screen.
# other available shapes are: arrow, circle, square, triangle, classic.

print(doodle.shape())  # outputs the current shape of the turtle cursor.

doodle.color("red", "green")  # first argument is pencolor; second argument is fillcolor
# if only one argument is given then both, pencolor and fillcolor are set to that color

print(doodle.color())  # outputs the current color of the cursor
# pencolor -> vo color ki drawing bane gi
# fillcolor -> vo cursor ka shape ka color hoga

screen = Screen()  # creating an object of screen class
screen.exitonclick()
