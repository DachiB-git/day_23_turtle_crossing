from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_to_start()
        self.is_alive = True

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_finished(self):
        if self.ycor() > 300:
            self.reset_to_start()
            return True
        else:
            return False

    def hit(self):
        self.is_alive = False

    def reset_to_start(self):
        self.goto(0, -260)
        self.setheading(90)
