import random


def pick_random_word():
    word_list = []
    with open("words.txt", "r") as f:
        for line in f:
            word_list.append(line.strip())
    return random.choice(word_list)


def ask_for_letter():
    while True:
        letter = input("Please enter a letter: ")
        print()  # newline

        # if the user enters 0, exit the game
        if letter == "0":
            return 0
        
        # check if the user entered a single letter
        if len(letter) == 1 and letter.isalpha():
            return letter.lower()
        else:
            print("Please enter a single letter.\n")


def main():
    print("Hello, welcome to the game of Hangman!\n")
    letters_used = []  # keep track of letters used
    max_lives = 6  # maximum number of lives

    word = pick_random_word()  # the word to guess
    lives_left = max_lives

    # main game loop
    while True:
        # print the word with underscores for missing letters
        print("Word to guess: ", end="")
        for letter in word:
            if letter in letters_used:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()  # newline

        # display lives left
        print(f"Lives left: {lives_left}/{max_lives}\n")

        # the user guesses a letter first
        given_letter = ask_for_letter()

        if given_letter == 0:  # if the user enters 0, exit the game
            break

        # check if the user has already tried that letter
        if given_letter in letters_used:
            print("You already used that letter.")
            continue
        letters_used.append(given_letter)

        # check if the user guessed the word
        if all(letter in letters_used for letter in word):
            print(f"Congratulations! You guessed the word: {word}!\n")
            break


if __name__ == "__main__":
    main()
    print("Thanks for playing!\n")
    quit()