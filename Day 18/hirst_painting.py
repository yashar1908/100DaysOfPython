import colorgram
import random
from turtle import Turtle 
from turtle import Screen

colors = colorgram.extract("spot_painting.png",30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r,g,b)
    rgb_colors.append(tup)    

colorlist = [(188, 19, 46), (243, 232, 66), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96), (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (6, 60, 38), (148, 209, 220), (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187)]

doodle = Turtle()
doodle.speed("fastest")
screen = Screen()
screen.colormode(255)

for i in range(10):
    for j in range (10):
        doodle.dot(10, random.choice(colorlist))
        doodle.penup()
        doodle.forward(30)
        doodle.pendown()
    doodle.penup()
    doodle.setpos(0, 30*(i+1))
    doodle.pendown()
    doodle.setheading(0)

screen.exitonclick()
        