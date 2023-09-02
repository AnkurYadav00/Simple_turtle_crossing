import time
from turtle import Screen

from cars import Cars
from player import Player
from scoreboard import Score


def main():
    # set up the screen
    screen = Screen()
    screen.setup(800, 600)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    # creating required class objects
    player = Player()
    cars = Cars()
    score = Score()
    screen.listen()

    # execution listeners
    screen.onkeypress(player.moveForward, "Up")

    # game run condition
    is_game_on = True

    while is_game_on:
        time.sleep(0.1)
        screen.update()

        # creates cars and provides then motion
        cars.cars_flow()
        cars.motion()

        # checks for collision
        if not player.car_collision(cars.Cars_list):
            is_game_on = not is_game_on
            score.gameOver()

        # reset player location when player reaches finish line
        if player.finishLine():
            player.reset_player()
            score.increase_level()
            cars.level()

    # after game over if player clicks on screen it exits the game
    screen.exitonclick()


if __name__ == "__main__":
    main()
