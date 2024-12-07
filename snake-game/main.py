from turtle import Screen
from snake import Snake
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jason's Snake Game")
screen.tracer(0)

# Create the snake
snake = Snake()

# Game loop
is_playing = True
while is_playing:
    screen.update()
    time.sleep(0.1)
    snake.move()




# Keep the window open
screen.exitonclick()