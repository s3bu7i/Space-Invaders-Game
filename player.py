
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.shapesize(1.7, 1.2)
        self.color("blue")
        self.setheading(90)
        self.penup()
        self.goto(0,-290)
        self.missiles = []

    def turn_right(self):
        new_heading = self.heading() - 15
        self.setheading(new_heading)

    def turn_left(self):
        new_heading = self.heading() + 15
        self.setheading(new_heading)

    def create_missile(self):
        new_missile = Turtle()
        new_missile.penup()
        new_missile.goto(0,-268)
        new_missile.color("red")
        new_missile.setheading(self.heading())
        self.missiles.append(new_missile)

    def fire(self):
        for m in self.missiles:
            m.forward(14)




