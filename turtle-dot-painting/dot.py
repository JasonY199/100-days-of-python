from turtle import Turtle, Screen, colormode
import random


# Drawing board requirements
# 10 rows and 10 columns
# 50 units apart
# 20 units in size

def pick_color(color_list):
    '''Returns a color from the filtered colors.'''
    return random.choice(color_list)

def draw_dot():
    '''Draws a dot with a random color.'''
    tim.dot(20, pick_color(filtered_colors))

def draw_row():
    '''Draws a row of dots.'''
    for _ in range(10):
        draw_dot()
        tim.forward(UNITS_APART)

def draw_board():
    '''Draws a 10x10 board of dots.'''
    for _ in range(10):
        draw_row()
        tim.left(90)
        tim.forward(UNITS_APART)
        tim.left(90)
        tim.forward(FULL_BOARD_SIZE)
        tim.right(180)

# Create a turtle object
tim = Turtle()

# Initial configuration
colormode(255)
FULL_BOARD_SIZE = 500
UNITS_APART = 50
DRAWING_BOARD_SIZE = UNITS_APART * 9
DOT_SIZE = 20
tim.pensize(DOT_SIZE)
tim.speed("fastest")

# Used this to extract colors from the image
"""
colors = colorgram.extract('image.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
"""

# Then after using above commented out code, I got the following colors, and checked which colors are most suitable for the project, removing the ones that are not suitable
filtered_colors = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]


# Set the starting position
tim.penup()
tim.goto(-DRAWING_BOARD_SIZE//2, -DRAWING_BOARD_SIZE//2)

# Draw the board
draw_board()

# Hide the turtle
tim.hideturtle()






# Draw the screen
screen = Screen()
screen.exitonclick()