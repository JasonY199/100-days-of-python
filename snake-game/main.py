from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jason's Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# Create a snake body
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

















# Keep the window open
screen.exitonclick()