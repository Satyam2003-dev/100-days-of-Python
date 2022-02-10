
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#   screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

timmy = Snake()
food = Food()
scoreboard = Scoreboard()

#   move snake
screen.listen()
screen.onkey(timmy.up, "Up")
screen.onkey(timmy.down, "Down")
screen.onkey(timmy.left, "Left")
screen.onkey(timmy.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    timmy.move()

    #   Detect collision with food
    if timmy.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        timmy.extend()

    #   Detect collision with wall
    if timmy.head.xcor() > 290 or timmy.head.xcor() < -290 or timmy.head.ycor()>290 or timmy.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    #   Detect collision with tail
    for segment in timmy.segments[1:]:
        if timmy.head.distance(segment)<10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
