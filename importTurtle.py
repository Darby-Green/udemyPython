# import turtle
#
# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()

import turtle
from math import radians, cos
from turtle import Screen

turtle.speed()

def square(length: int) -> None:
    """draws a square of length 'length'"""
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)

def circleSquare(length: int) -> None:
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)

Screen().tracer(0) # disables updating the turtle window
for s in range(72):
    circleSquare(300)
    turtle.left(5)


Screen().update() # update the turtle window with the finished drawing
turtle.done()

# print(dir())