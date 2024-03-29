from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("~ My Snake Game ~")
screen.setup(width=600, height=600)

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
time.sleep(1)
game_on = True
while game_on:
  screen.update()
  time.sleep(0.2)
  snake.move()
  if snake.head.distance(food) < 15:
    food.Refresh()
    snake.extend()
    scoreboard.Increase_score()

  if snake.head.xcor()>290 or snake.head.xcor()< -290 or snake.head.ycor()>300 or snake.head.ycor()< -290:
    game_on = False
    scoreboard.game_over()

  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_on=False
      scoreboard.game_over()

screen.exitonclick()
