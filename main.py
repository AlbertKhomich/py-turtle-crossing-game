import random
import time
from turtle import Screen

import car_manager
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
garage = []
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.listen()
    screen.onkeypress(player.move, "w")

    if random.randint(0, 6) == 1:
        car = car_manager.CarManager()
        garage.append(car)

    for vehicle in garage:
        vehicle.move()

        if player.distance(vehicle) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() == FINISH_LINE_Y:
        player.reset_position()
        car_manager.speed_up()
        score.level_up()

screen.exitonclick()
