from turtle import Turtle, Screen


# Create a turtle object
tim = Turtle()

# Set the turtle's shape and color
#tim.shape("turtle")
#tim.color("red")

########################################################################
## Challenge helper functions
########################################################################

def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def draw_dashed_line():
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

def go_to_starting_position_for_triangle():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)
    tim.pendown()

########################################################################
## Challenge #1

#draw_square()

########################################################################
## Challenge #2

#draw_dashed_line()

########################################################################
## Challenge #3

def run_challenge_3():
    go_to_starting_position_for_triangle()

run_challenge_3()



















########################################################################
# Draw the screen
screen = Screen()
screen.exitonclick()