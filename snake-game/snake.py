from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.next_direction = self.head.heading()  # Buffer for the next direction

    def create_snake(self):
        """Create the initial snake with starting segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at the given position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        """Move the snake forward and apply the buffered direction."""
        print(f"Current Direction: {self.head.heading()}, Next: {self.next_direction}")  # Debugging
        self.head.setheading(self.next_direction)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Buffer a direction change to up."""
        if self.head.heading() != DOWN:
            self.next_direction = UP

    def down(self):
        """Buffer a direction change to down."""
        if self.head.heading() != UP:
            self.next_direction = DOWN

    def left(self):
        """Buffer a direction change to left."""
        if self.head.heading() != RIGHT:
            self.next_direction = LEFT

    def right(self):
        """Buffer a direction change to right."""
        if self.head.heading() != LEFT:
            self.next_direction = RIGHT

    def extend(self):
        """Add a new segment to the snake at its current tail position."""
        self.add_segment(self.segments[-1].position())

    def get_x(self) -> int:
        """Return the x position of the snake head."""
        return int(self.head.xcor())

    def get_y(self) -> int:
        """Return the y position of the snake head."""
        return int(self.head.ycor())
