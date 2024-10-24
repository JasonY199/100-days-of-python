import random
from hands import show

def get_user_input(choice=None):
    if choice is None:
        choice = input("Please choose your hand (1. Rock, 2. Paper, 3. Scissors, 0. Quit): ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice, please try again.")
        return None

    if choice == 0:
        print("Thanks for playing, goodbye!")
        exit()
    elif choice < 1 or choice > 3:
        print("Invalid choice, please try again.")
        return None
    else:
        return choice

def play_round(user_choice, computer_choice):
    user_hand = show(user_choice)
    computer_hand = show(computer_choice)

    print(f"\nYou chose:\n{user_hand}")
    print(f"Computer chose:\n{computer_hand}")

    if user_choice == computer_choice:
        return "It's a tie!\n"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!\n"
    else:
        return "You lose!\n"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        choice = get_user_input()
        computer_choice = random.randint(1, 3)
        result = play_round(choice, computer_choice)
        print(result)

if __name__ == '__main__':
    main()
