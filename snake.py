from turtle import Turtle, Screen
import time
from scoreboard import *
frame = Screen()

score = Score()


ko = Turtle()
ko.hideturtle()
ko.color("white")
ko.penup()


class Snake:
    snake = []

    def __init__(self):
        self.create_snake()

    def create_snake(self):
        frame.tracer(0)
        for i in range(3):
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.goto(x=(0 - (i * 20)), y=0)
            t.speed('fastest')
            self.snake.append(t)

    def move(self, w, h, food):
        game_on = True
        while game_on:
            frame.update()
            time.sleep(0.1)
            for seg in range(len(self.snake) - 1, 0, -1):
                x = self.snake[seg - 1].xcor()
                y = self.snake[seg - 1].ycor()
                self.snake[seg].goto(x, y)
            game_on = self.game_control(w, h, food)
            if not game_on:
                #self.reset()
                score.reset()
                #game_on = True
        ko.write(f"Game Over", align="center", font=("Arial", 24, "normal"))


    def game_control(self, w, h, food):
        global  s
        self.xl = [(-w//2)-30, (w//2)+20]
        self.yl = [(-h // 2) + 30, (h // 2) - 20]
        if self.snake[0].xcor() <= self.xl[1] and self.snake[0].xcor() >= self.xl[0] and self.snake[0].ycor() <= self.yl[1] and self.snake[0].ycor() >= self.yl[0]:
            self.snake[0].fd(20)
            if self.check_body_hit():
                if self.snake[0].distance(food) < 15:
                    food.new_location(w, h)
                    self.add_segment()
                    score.update_score()

                return True
            else:
                return False
        else:
            return False

    def turn_up(self):
        self.snake[0].setheading(90)

    def turn_left(self):
        self.snake[0].setheading(180)

    def turn_right(self):
        self.snake[0].setheading(0)

    def turn_down(self):
        self.snake[0].setheading(270)

    def add_segment(self):
        self.last_x_cor = self.snake[len(self.snake)-1].xcor()
        self.last_y_cor = self.snake[len(self.snake) - 1].ycor()
        self.new_seg_heading = self.snake[len(self.snake) - 1].heading()
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.speed('fastest')
        t.goto(self.last_x_cor, self.last_y_cor)
        self.snake.append(t)

    def check_body_hit(self):
        self.not_hit = True
        for i in range(1,len(self.snake)-1):
            if self.snake[0].distance(self.snake[i]) <= 10:
                self.not_hit = False
                break
        if self.not_hit:
            return True
        else:
            return False

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()






