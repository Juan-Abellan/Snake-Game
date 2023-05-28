from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Consolas", 20, "normal")


class ScoreBoard(Turtle):
    """
    Contains everything related to the score board.
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.food_eaten = 0
        self.color("white")
        self.goto(x=0, y=265)
        self.update_scoreboard()

    def plus_1(self):
        """
        add + 1 points to the score board.
        """
        self.food_eaten += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the score board after adding one food eaten unit.
        """
        self.write(arg=f"SCORE: {self.food_eaten}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Shows a GAME OVER sign in the middle of the screen.
        """
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
