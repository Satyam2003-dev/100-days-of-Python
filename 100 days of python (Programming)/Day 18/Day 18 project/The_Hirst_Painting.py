
import random
import turtle as turtle_module

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 15)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     if r > 230 and g > 230 and b > 230:
#         continue
#     else:
#         new_color = (r,g,b)
#         rgb_colors.append(new_color)

# 10 x 10 rows and col or spots
# 20 size dot and 50 away from each other


def random_color():
    #   '''created rgb_colors using above code using cologram'''
    rgb_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149)]
    return random.choice(rgb_colors)


def line_of_Dots():
    for i in range(10):
        tim.dot(20, random_color())
        if i == 9:
            continue
        else:
            tim.forward(50)

def left_Turn():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)

def right_Turn():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


screen = turtle_module.Screen()                                     # '''Set up Screen size'''
screen.setup(width=900, height=900, startx=0, starty=0)

tim = turtle_module.Turtle()
tim.hideturtle()
tim.speed("fastest")
turtle_module.colormode(255)
tim.penup()
# setheading 0-east, 90-north, 180-west, 270-south
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

'''Execution'''
for i in range(5):
    line_of_Dots()
    left_Turn()
    line_of_Dots()
    right_Turn()

screen.exitonclick()
