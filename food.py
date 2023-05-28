from turtle import Turtle
import random


class Food(Turtle):
    """
    Contains everything related with the food element of the game.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,
                       stretch_len=0.5)  # Return or set the pen’s attributes x/y-stretch-factors and/or outline.
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Creates a randomly located dot of food.
        """
        x_random = random.randint(-280, 280)  # To avoid food getting to close to the borders in x.
        y_random = random.randint(-280, 280)  # To avoid food getting to close to the borders in y.
        self.goto(x=x_random, y=y_random)
