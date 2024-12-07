from turtle import Turtle


# Constants
TEXT_POSITION = (0, 265)
TEXT_FONT = ("Courier", 22, "normal")
TEXT_COLOR = "white"
TEXT_ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(TEXT_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(TEXT_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current score"""
        self.clear()
        self.write(f"Score: {self.score}", align=TEXT_ALIGN, font=TEXT_FONT)

    def increase_score(self):
        """Increase the score by 1"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Display GAME OVER message"""
        self.goto(0, 0)
        self.write("GAME OVER", align=TEXT_ALIGN, font=TEXT_FONT)