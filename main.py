# IMPORTS
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# SCREEN SETTINGS
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Snake Game")
screen.tracer(0)  # Turn turtle animation on/off and set delay for update drawings

# ---------------------------------------------------------------------------------------------------------------
still_playing = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()  # Set focus on TurtleScreen (in order to collect key-events)
screen.onkey(snake.up, key="Up")  # .onkey: Bind fun to key-release event of key.
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

while still_playing:
    screen.update()  # Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(0.1)  # sleep function is used to add delay in the execution of a program.
    snake.move()
    # DETECTING COLLISION WITH FOOD
    if snake.snake_head.distance(food) < 15:  # Return the distance from the turtle to (x,y).
        food.refresh()
        snake.extend()
        scoreboard.plus_1()
    # DETECTING COLLISION WITH WALL
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 \
            or snake.snake_head.ycor() < -280:
        still_playing = False
        scoreboard.game_over()
    # DETECTING COLLISION WITH SNAKE BODY
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            still_playing = False
            scoreboard.game_over()

# ---------------------------------------------------------------------------------------------------------------
# SCREEN SETTINGS EXIT
screen.exitonclick()
