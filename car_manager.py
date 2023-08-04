from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = [Turtle() for _ in range(15)]
        self.speed = STARTING_MOVE_DISTANCE
        self.spawn_cars()

    def spawn_cars(self):
        for car in self.cars:
            car.color(choice(COLORS))
            car.shape("square")
            car.penup()
            car.shapesize(1, 2)
            car.goto(300 + randint(0, 300), randint(-260, 200))
            car.setheading(180)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.goto(300 + randint(0, 200), randint(-260, 200))
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT


