from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",20,"normal")
class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score=0
    self.color("white")
    self.penup()
    self.goto(0,270)
    self.write(f"Score : {self.score}",align="center",font=("Arial",20,"normal"))
    self.hideturtle()

  def update_score(self):
     self.write(f"Score : {self.score}",align=ALIGNMENT,font=FONT)

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER",align=ALIGNMENT,font=FONT)
    
  def Increase_score(self):
    self.score+=1
    self.clear()
    self.update_score()
   
