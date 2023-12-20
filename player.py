import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset_position()

    def move(self):
        new_position = self.ycor() + MOVE_DISTANCE
        if new_position <= FINISH_LINE_Y:
            self.sety(new_position)

    def reset_position(self):
        self.goto(STARTING_POSITION)
