from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1 # use with time.sleep

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1 # reset ball move_speed
        # change direction when one side wins
        self.bounce_x()
