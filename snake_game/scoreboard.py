from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,266)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write(f"CONDA is DEAD😭", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1   
        self.clear()
        self.update_scoreboard()