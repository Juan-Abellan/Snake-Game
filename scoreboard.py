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
        with open(file="data.txt") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
        self.food_eaten = 0
        self.color("white")
        self.goto(x=0, y=265)
        self.update_scoreboard()

    def plus_1(self):
        """
        add + 1 points to the score board.
        """
        self.food_eaten += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the score board after adding one food eaten unit.
        """
        self.clear()
        self.write(arg=f"SCORE: {self.food_eaten} HIGH SCORE: {self.high_score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def reset_max(self):
        """
        Resets the score board.
        """
        if self.food_eaten > self.high_score:
            self.high_score = self.food_eaten
            with open(file="data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.food_eaten = 0
        self.update_scoreboard()
