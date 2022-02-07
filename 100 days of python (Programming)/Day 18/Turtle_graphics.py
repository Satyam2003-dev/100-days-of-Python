# import  turtle
# tim = turtle.Turtle()

# from turtle import  Turtle

# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

# from turtle import  *    # #    'import *' means import everything    # # try to avoid writing these code while importing module

import turtle as t  # here as 't' means turtle it is an alias function means short-name
import random
tim = t.Turtle()

# import  heroes
# print(heroes.gen())

# # to draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colours = ["red", "blue", "orange", "dark green"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()
