from turtle import Turtle
FONT = ("Arial", 25, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,240)
        self.score_point = 0
        with open('data.txt') as file:
            self.high_score= int(file.read())
        self.pencolor('orange')
        self.hideturtle()
        self.write(f"Score: {self.score_point} High Score: {self.high_score}",align='center', font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_point} High Score: {self.high_score}",align='center', font=FONT)

    def plus_score(self):
        self.score_point += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align='center', font=FONT)
        
    def reset_score(self):
        if self.score_point > self.high_score:
            self.high_score = self.score_point
            with open('data.txt',mode='w') as file:
                file.write(f"{self.score_point}")
        self.score_point = 0
        self.update_score()
