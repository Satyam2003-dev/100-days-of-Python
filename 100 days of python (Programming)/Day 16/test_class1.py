
import turtle

timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(300)

my_screen = turtle.Screen()
print(f"Screen Height: {my_screen.canvheight}")
print(f"Screen Width: {my_screen.canvwidth}")
my_screen.exitonclick()
