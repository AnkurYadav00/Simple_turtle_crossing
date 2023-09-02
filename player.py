from turtle import Turtle

STARTING_LOCATION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.shapesize(1.1, 1.1)
        self.penup()
        self.goto(STARTING_LOCATION)
        self.setheading(90)

    def moveForward(self):
        """ control car motion, look into main file for listeners used"""
        self.forward(20)

    def finishLine(self):
        """ checks if turtle has reached finishline """
        if (300 - self.ycor()) < 30:
            return True
        return False

    def car_collision(self, cars):
        """ checks for player collision with car """
        for car in cars:
            if car.xcor() in range(-28, 28):
                if self.distance(car) < 22:
                    return False
        return True

    def reset_player(self):
        """ resets player location to starting position """
        self.goto(STARTING_LOCATION)
