import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def speed_up():
    global STARTING_MOVE_DISTANCE
    STARTING_MOVE_DISTANCE += MOVE_INCREMENT


class CarManager(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.setheading(180)
        self.goto(315, random.randint(-250, 250))
        self.speed_up_increment = 0

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
