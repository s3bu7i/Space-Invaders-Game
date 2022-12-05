
from turtle import Turtle,colormode
import random

colormode(255)

class Invader:
    def __init__(self):
        self.enemies = []
        self.create_invader()

    def create_invader(self):
        random_number = random.randint(1,10)
        if random_number == 1:
            new_invader = Turtle()
            r = random.randint(0,255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            new_invader.color((r,g,b))
            new_invader.penup()
            new_invader.shape("turtle")
            new_invader.goto(random.randint(-280, 280), random.randint(320, 380))
            new_invader.setheading(new_invader.towards(0, -200))
            self.enemies.append(new_invader)


    def move(self):
        for e in self.enemies:
            e.forward(5)

