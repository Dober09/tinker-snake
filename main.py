from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title(titlestring="My Snake Game")
screen.tracer(0)

# Create  a snake body

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,key='Up')
screen.onkey(snake.down,key='Down')
screen.onkey(snake.left,key='Left')
screen.onkey(snake.right,key='Right')

# move the snake
wall = 280
move_snake = True
while move_snake:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collosion with food.
    if snake.head.distance(food) <14:
        food.refresh()
        snake.extend_snake()
        scoreboard.plus_score()

    # detect collision with wall
    if snake.head.xcor() > wall or snake.head.xcor() < -wall or snake.head.ycor() >wall or snake.head.ycor() <-wall:
        scoreboard.reset_score()
        snake.reset_snake()
        


    # detect  collision with tail
    for segment in snake.snake_parts[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()

