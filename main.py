import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = player.is_alive
while game_is_on:
    car_manager.move_cars()
    if any(player.distance(car) < 20 for car in car_manager.cars):
        player.hit()
        scoreboard.game_over()
        game_is_on = False
    level_status = player.level_finished()
    if level_status:
        scoreboard.increment_level()
        car_manager.increase_speed()
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
