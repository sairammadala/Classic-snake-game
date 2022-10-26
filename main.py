from snake import *
from food import Food
frame.listen()
frame.setup(width=600, height=600)
frame.title("Snake Game")
frame.bgcolor("black")

"""snake = []
frame.tracer(0)
for i in range(3):
    t = Turtle(shape="square")
    t.penup()
    t.color("white")
    t.goto(x=(0-(i*20)), y=0)
    t.speed('fastest')
    snake.append(t)

game_on = True
while game_on:
    frame.update()
    time.sleep(0.1)
    for seg in range(len(snake)-1, 0, -1):
        x = snake[seg-1].xcor()
        y = snake[seg-1].ycor()
        snake[seg].goto(x, y)
    snake[0].fd(10)"""


snake = Snake()
food = Food(600,600)


frame.onkey(snake.turn_left, "Left")
frame.onkey(snake.turn_right, "Right")
frame.onkey(snake.turn_up, "Up")
frame.onkey(snake.turn_down, "Down")

snake.move(500, 600, food)



frame.exitonclick()