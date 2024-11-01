import random


from hangman_stages import hangman_stages_7 as draw_hangman


def pick_random_word():
    word_list = []
    with open("words.txt", "r") as f:
        for line in f:
            word_list.append(line.strip())
    return random.choice(word_list)

def ask_for_letter():
    while True:
        print()  # newline
        letter = input("Please enter a letter: ")
        print()  # newline

        # if the user enters 0, exit the game
        if letter == "0":
            print("Thanks for playing!\n")
            quit()
        
        # check if the user entered a single letter
        if len(letter) == 1 and letter.isalpha():
            return letter.lower()
        else:
            print("Please enter a single letter.\n")

def print_word_progress(word, letters_used):
    print(" " * 4, end="") # indent
    for letter in word:
        print(letter if letter in letters_used else "_", end=" ")
    print()  # newline

def print_drawing(times_wrong):
    if times_wrong < len(draw_hangman):
        print(draw_hangman[times_wrong])

def print_letters_used(letters_used):
    if letters_used:
        print("\nLetters used:", " ".join(sorted(letters_used)), "\n")

def main():
    print("Hello, welcome to the game of Hangman!")
    print("Enter 0 to exit the game at any time.\n")

    # initialize game variables
    word = pick_random_word()  # the word to guess
    letters_used = []  # keep track of letters used by the user
    lives_left = len(draw_hangman) - 1
    times_wrong = 0  # number of times the user guessed wrong
    feedback_message = ""  # to store feedback for each guess

    # main game loop
    while True:
        if letters_used:  # only print a divider if there are letters used
            print("\n" + "-" * 40 + "\n")

        # Print feedback from previous guess
        if feedback_message:
            print(feedback_message + "\n")
            feedback_message = ""  # Reset feedback message for next round

        print_drawing(times_wrong)
        print_word_progress(word, letters_used)
        print_letters_used(letters_used)

        given_letter = ask_for_letter()  # get user input

        # check if the user has already tried that letter
        if given_letter in letters_used:
            feedback_message = "You already used that letter."
            continue

        # add the letter to the list of used letters
        letters_used.append(given_letter)

        # Set feedback based on whether the letter is in the word or not
        if given_letter in word:
            feedback_message = f"Good job! The letter '{given_letter}' is in the word."
        else:
            times_wrong += 1
            feedback_message = f"Sorry, the letter '{given_letter}' is not in the word."
            # Check for game over and print final state
            if times_wrong >= lives_left:
                print("\n" + "-" * 30 + "\n")
                print(feedback_message + "\n")
                print_drawing(times_wrong)
                print(f"Game over! The word was: {word}\n")
                break

        # check if the user guessed the word
        if all(letter in letters_used for letter in word):
            print(f"Congratulations! You guessed the word: {word}!\n")
            break


if __name__ == "__main__":
    main()