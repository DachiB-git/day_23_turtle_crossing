from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 240)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increment_level(self):
        self.level += 1
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    @staticmethod
    def game_over():
        go_obj = Turtle()
        go_obj.penup()
        go_obj.goto(0, 0)
        go_obj.write("GAME OVER", align="center", font=FONT)
