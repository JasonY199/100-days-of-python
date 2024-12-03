"""This program is a collection of challenges from the 100 Days of Code - The Complete Python Pro Bootcamp for 2021 course on Udemy. Uncomment the function calls to run the challenges."""

from random import randint
from turtle import Turtle, Screen, colormode


# Set the color mode to 255
colormode(255)

# Create a turtle object
tim = Turtle()

# Set the turtle's shape and color
#tim.shape("turtle")
#tim.color("red")


########################################################################
## Challenge #1 - Draw a square

def draw_square(angle=90, length=100):
    '''Draws a square with the given angle and length. 
    Defaults too 90 degrees and 100 units length.'''
    for _ in range(4):
        tim.right(angle)
        tim.forward(length)

def go_to_shape_starting_position(side_lengths=100, extra_up=0, extra_right=0):
    '''Assuming we will be using 100 as length for sides of the shape.
    If a different length is needed, pass it as an argument.
    Can also pass extra_up and extra_right to move the starting position.'''
    tim.penup()
    tim.left(90)
    tim.forward((side_lengths // 2) + extra_up)
    tim.right(90)
    tim.forward((side_lengths // 2) + extra_right)
    tim.pendown()

#go_to_shape_starting_position(100)
#draw_square()

########################################################################
## Challenge #2 - Draw a dashed line

def draw_dashed_line():
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

#draw_dashed_line()

########################################################################
## Challenge #3 - Draw some shapes

def random_color()-> tuple:
    '''Returns a random color tuple.'''
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def draw_shapes():
    """Draws the following shapes:
    Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon, Hendecagon, Dodecagon.
    Picks a random color for each shape."""
    go_to_shape_starting_position(extra_up=150)
    for i in range(3, 13):
        angle = 360 / i
        tim.color(random_color())
        for _ in range(i):
            tim.right(angle)
            tim.forward(100)

#draw_shapes()

########################################################################
## Challenge #4 - Generate a random walk

def random_walk(steps=10):
    '''Generates a random walk with the given number of steps.
    Note: It's possible for the turtle to move off the screen.'''
    tim.pensize(10)
    possible_directions = [0, 90, 180, 270]
    current_heading = tim.heading()

    # Generate the random walk
    for _ in range(steps):
        print(tim.heading())  # Debugging
        new_random_heading = possible_directions[randint(0, 3)]

        # Prevent the turtle from moving backwards
        if new_random_heading == 0 and current_heading == 180:
            new_random_heading = 90
        elif new_random_heading == 90 and current_heading == 270:
            new_random_heading = 180
        elif new_random_heading == 180 and current_heading == 0:
            new_random_heading = 270
        elif new_random_heading == 270 and current_heading == 90:
            new_random_heading = 0

        # New color if the heading changes
        # Also, set the new heading to the current heading
        if new_random_heading != current_heading:
            tim.color(random_color())
            current_heading = new_random_heading
        
        # Set the new heading to the turtle and move forward
        tim.setheading(new_random_heading)
        tim.forward(30)

#random_walk(100)

########################################################################
## Challenge #5 - Draw a spirograph

def draw_spirograph(size_of_gap):
    '''Draws a spirograph with random colors.'''
    tim.speed("fastest")
    for _ in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(200)
        tim.setheading(tim.heading() + size_of_gap)

#draw_spirograph(4)



########################################################################
# Draw the screen
screen = Screen()
screen.exitonclick()