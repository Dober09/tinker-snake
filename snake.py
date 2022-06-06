from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0
class Snake:
    def __init__(self) :
        self.snake_parts = []
        self.snake_len = 3
        self.create_snake()
        self.head = self.snake_parts[0] 
# Create  a snake body
    def create_snake(self):
        for idx in range(self.snake_len):
            self.add_snake_part(idx)
            
# move the snake
    def move(self):
        for idx in range(self.snake_len - 1, 0, -1):
            x_cor = self.snake_parts[idx-1].xcor()
            y_cor = self.snake_parts[idx-1].ycor()
            self.snake_parts[idx].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def add_snake_part(self,place):
        snake_body = Turtle(shape='square')
        snake_body.penup()
        snake_body.color('white')
        self.snake_parts.append(snake_body)
        snake_body.goto(-20*place, self.snake_parts[-1].ycor())

    def extend_snake(self):
        self.snake_len +=1
        self.add_snake_part(self.snake_len)

    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)  
        

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def reset_snake(self):
        for snake_part in self.snake_parts:
            snake_part.goto(1000,1000)
        self.snake_parts.clear()
        self.snake_len = 3
        self.create_snake()
        self.head = self.snake_parts[0] 

    
