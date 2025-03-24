import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
car_list = []
screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
spawn_timer = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.move, "Up")
    spawn_timer += 4
    car_manager.create()
    car_manager.move()
    for car in car_manager.car_list:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() == 280:
        player.goto(0,-280)
        scoreboard.add_level()
        car_manager.increase_speed()
screen.exitonclick()