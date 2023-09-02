import random
import time
from turtle import Turtle, forward, backward

COLORS = ["red", "green", "yellow", "black", "blue", "pink", "orange"]
SPEED = 0.2

class Cars:
    def __init__(self):
        self.speed = SPEED
        self.y = None
        self.Cars_list = []

    def create_car(self):
        """ create cars with random color and in square shape """
        self.y = random.randint(-245, 245)
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(1, 3)
        car.penup()
        car.goto(400, self.y)
        self.Cars_list.append(car)

    def cars_flow(self):
        """ generate each car on screen with random frequency """
        for i in range(random.randint(0, 1)):
            self.create_car()

    def motion(self):
        time.sleep(self.speed)
        for i in self.Cars_list:
            i.backward(20)

    def level(self):
        if self.speed > 0:
            self.speed -= 0.01
