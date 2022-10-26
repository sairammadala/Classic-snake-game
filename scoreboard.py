from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        #................vaiables
        self.score = 0
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = -1
        self.update_score()

