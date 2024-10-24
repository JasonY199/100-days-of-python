from password_generator import PasswordGenerator


def print_menu():
    print("Please choose an option:")
    print("  1. Generate a new password")
    print("  2. Regenerate the last password")
    print("  3. Display last five generated passwords")
    print("  4. Clear the password history")
    print("  0. Exit")


def get_option():
    '''Get the user's option.'''
    option = input("Option: ")
    while option not in ['0', '1', '2', '3', '4']:
        print("Invalid option. Please try again.")
        option = input("Option: ")
    return option


def get_positive_integer(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a valid number.")


def get_password_params():
    num_letters = get_positive_integer("How many letters would you like in your password? ")
    num_symbols = get_positive_integer("How many symbols would you like in your password? ")
    num_numbers = get_positive_integer("How many numbers would you like in your password? ")
    return num_letters, num_symbols, num_numbers


def main():
    # Create an instance of the PasswordGenerator class
    pass_gen = PasswordGenerator()

    print("Welcome to the PyPassword Generator!")

    # Main loop
    while True:
        print_menu()  # Print the menu
        option = get_option()  # Get the user's option
        print()  # Add a blank line for readability

        # Exit the main loop, then the program
        if option == '0':
            break
        
        # Generate a new password
        if option == '1':
            letters, symbols, numbers = get_password_params()
            pass_gen.set_password_parameters(letters, symbols, numbers)
            pass_gen.generate_password()
            print(f"\nPassword generated: {pass_gen.get_last_password()}\n")
            continue

        # Regenerate the last password
        if option == '2':
            password_history = pass_gen.get_password_history()
            if password_history == None:
                print("To regenerate the last password, you must first generate a password.\n")
            else:
                print(f"Last password: {pass_gen.get_last_password()}")
                pass_gen.generate_password()
                print(f" New password: {pass_gen.get_last_password()}\n")
            continue

        # View the password history
        if option == '3':
            password_history = pass_gen.get_password_history()
            if password_history == None:
                print("No passwords have been generated yet.\n")
            else:
                print("Password history:")
                for i, password in enumerate(password_history):
                    print(f"{i + 1}. {password}")
                print()
            continue

        # Clear the password history
        if option == '4':
            pass_gen.clear_password_history()
            print("Password history cleared.\n")
            continue

    # End of main loop
    print("Thanks for using PyPassword Generator, goodbye!")


if __name__ == "__main__":
    main()
    exit()
