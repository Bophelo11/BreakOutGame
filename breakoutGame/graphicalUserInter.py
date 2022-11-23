from turtle import Turtle
import time
import random

FONT = ("Courier",52, "normal")
FONT2 = ("Courier", 32, "normal")

ALIGNMENT = 'center'
LIST_OF_AMA_COLOR = [
              'light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki'

]
class GUI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(LIST_OF_AMA_COLOR))
        self.header()

    def header(self):
        self.clear()
        self.goto(x=0, y=-150)
        self.write("BRRRREHHHHKAHHHHHHHHHT, BLAAAAH BLAAAAAHH BLAAAAAH",align=ALIGNMENT, font=FONT)
        self.write("'SPACEBAR' to PAUSE or RESUME game.")

    def color_change(self):
        self.clear()
        self.color(random.choice(LIST_OF_AMA_COLOR))
        self.header()

    def game_paused(self):
        self.clear()
        self.color_change()
        time.sleep(0.5)
    #GameOver
    def chaile(self):
        self.clear()
        if win == True:
            self.write("You Fucking Champion you", align="center", font=FONT)
        else:
            self.write("Fucking Loser", align="center",font=FONT)



