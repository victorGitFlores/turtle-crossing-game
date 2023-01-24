from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280




class Player(Turtle):
    def startmeup(self):
        self.penup()
        self.setheading(90)  # north
        self.goto((0, -280))
        self.shape("turtle")


    def __init__(self):
        super().__init__()
        self.startmeup()

