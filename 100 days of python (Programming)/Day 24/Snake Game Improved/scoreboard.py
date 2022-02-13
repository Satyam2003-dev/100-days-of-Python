from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",20,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high-score.txt", mode='r') as file:
            self.high_score = int(file.read())
        # move turtle before displaying
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        # display scoreboard
        self.color("white")
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1  
        self.clear()
        self.update_scoreboard()

    # Added High score
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high-score.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
