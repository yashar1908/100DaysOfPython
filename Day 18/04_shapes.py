from turtle import Turtle
from turtle import Screen

doodle = Turtle()

# 1. Triangle:
for i in range(3):
    doodle.forward(100)
    doodle.left(120)

# doodle.reset()

# 2. Square
for i in range(4):
    doodle.forward(100)
    doodle.left(90)

# doodle.reset()

# 3. Pentagon
for i in range(5):
    doodle.forward(100)
    doodle.left(72)

# doodle.reset()

# 4. Hexagon
for i in range(6):
    doodle.forward(100)
    doodle.left(60)

# 5. Heptagon
for i in range(7):
    doodle.forward(100)
    doodle.left(180-128.57)

# 6. Octagon
for i in range(8):
    doodle.forward(100)
    doodle.left(45)

# 7. Nonagon
for i in range(9):
    doodle.forward(100)
    doodle.left(40)

# 8. Decagom
for i in range(10):
    doodle.forward(100)
    doodle.left(36)

screen = Screen()
screen.exitonclick()
