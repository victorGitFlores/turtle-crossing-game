from turtle import Screen
from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
screen.listen()
screen.onkey("turt_move_up", "Up")

game_on = True

# Create a turtle player that starts at the bottom middle, looking up.
# listen to the Up key to move turtle north

player = Player()
player.startmeup()


while game_on:
    sleep(.01)
    screen.update()




screen.exitonclick()