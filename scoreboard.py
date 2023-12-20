import turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = -0
        self.level_up()

    def level_up(self):
        self.level += 1
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", font=FONT, align="center")

    def game_over(self):
        self.home()
        self.write("GAME OVER", font=FONT, align="center")
