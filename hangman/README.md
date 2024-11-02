# Hangman Game

A classic command-line Hangman game developed in Python as part of the 100 Days of Python course. This project challenges players to guess a random word from various categories with a limited number of incorrect guesses allowed.

## Features

- **Random Word Selection**: Words are randomly selected from a variety of categories like fruits, animals, desserts, and beverages.
- **Hints**: Each word comes with a hint based on its category to help the player make better guesses.
- **Limited Guesses**: Players have a set number of incorrect guesses, displayed visually as part of a hangman drawing.
- **Feedback and Tracking**: The game tracks letters used and provides real-time feedback on correct and incorrect guesses.

## How to Play

1. Run the game from the command line.
2. A random word will be chosen, and a hint will display its category.
3. Type a letter to guess if it's in the word.
4. The game will show correctly guessed letters in their positions or draw a part of the hangman for incorrect guesses.
5. The game ends when you either guess the word or reach the maximum number of incorrect guesses.

## Setup and Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.12 installed.
3. Run the following command to start the game:

   ```bash
   python3 main.py
