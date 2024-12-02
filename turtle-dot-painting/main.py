from turtle import Turtle, Screen


# Create a turtle object
timmy_the_turtle = Turtle()

# Set the turtle's shape and color
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# Draw a square
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)







# Draw the screen
screen = Screen()
screen.exitonclick()