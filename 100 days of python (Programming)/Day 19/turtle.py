from turtle import Turtle, Screen

#tim and tom are separate instances, examples of the turtle objects
tim = Turtle()
tom = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    #home will move turtle back to starting position
    tim.home()
    tim.pendown()

screen.listen()
# function as argument does not need ()
screen.onkey(move_forwards, "Up")
screen.onkey(clear, "c")

screen.exitonclick()
