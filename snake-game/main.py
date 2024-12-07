from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
BACKGROUND_COLOR = "black"
GAME_TITLE = "Jason's Snake Game"
GAME_SPEED = 0.09  # Lower is faster


# Set up the screen
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

# Create the needed objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
is_playing = True
while is_playing:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("Eating food")  # Debugging
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect collision with wall
    if snake.get_x() < -280 or snake.get_x() > 280 or snake.get_y() < -280 or snake.get_y() > 280:
        print(f"Hit the wall at: X={snake.get_x()}, Y={snake.get_y()}")  # Debugging
        scoreboard.game_over()
        is_playing = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print("Hit the tail")  # Debugging
            scoreboard.game_over()
            is_playing = False

# Keep the window open
screen.exitonclick()