from turtle import Turtle

FONT = ("Verdana", 20, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-320, 260)
        self.hideturtle()
        self.level_board()

    def increase_level(self):
        """ increases the level """
        self.level += 1
        self.level_board()

    def level_board(self):
        """ informs player about the level he/she is at """
        self.clear()
        self.write(f"level : {self.level}", False, "center", FONT)

    def gameOver(self):
        """ informs player about the game over """
        self.speed("fastest")
        self.goto(0, 0)
        self.write("Game  Over", False, "center", FONT)
