from turtle import Turtle

STARTING_XY = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    """
    Class containing the functionality of the snake.
    """

    def __init__(self):
        self.segments = []
        self.origin_snake()
        self.snake_head = self.segments[0]

    def origin_snake(self):
        """
        Creates and locates at the origin the three first segments of the snake.
        """
        for xy in STARTING_XY:
            self.new_segment(xy)

        # print(f"""
        # TESTING_SEGMENTS ....................
        # {self.segments = }
        # {len(self.segments) = }
        # .....................................
        # """)

    def extend(self):
        """
        Add a new segment to the snake body.
        """
        self.new_segment(xy=self.segments[-1].position())

    def new_segment(self, xy):
        """
         Creates the new segment.
        """
        segment_new = Turtle("square")
        segment_new.color("white")
        segment_new.penup()
        segment_new.goto(xy)
        self.segments.append(segment_new)

    def move(self):
        """
        Makes the snake move, one segment follows the previous one.
        """
        for num_seg in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[num_seg - 1].xcor()
            y_new = self.segments[num_seg - 1].ycor()
            self.segments[num_seg].goto(x_new, y_new)
        self.snake_head.forward(MOVE_STEP)

    def up(self):
        """
        Rotates the snake heading north.
        """
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """
        Rotates the snake heading south.
        """
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        """
        Rotates the snake heading west.
        """
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        """
        Rotates the snake heading east.
        """
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
