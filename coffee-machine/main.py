import time

COFFEE_ART = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⢻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠘⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡆⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠃⠀⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⣀⣀⣀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⠒⠒⠋⠉⠉⠻⣧⠀⠀⠀⠈⠉⠁⠀⠀⠀⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⣀⣀⣀⣀⣤⣽⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⠷⠾⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠶⠚⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⡏⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⣸⠛⠻⣷⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⢠⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣹⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣎⣠⣴⠿⠃⠀⠀⠀
⠀⢀⣠⠔⠒⠈⠉⠀⠹⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠛⠉⠒⠢⣄⠀⠀
⠀⣿⡁⠀⠀⠀⠀⠀⠀⠈⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⡃⠀⠀⠀⠀⠀⠀⠀⡟⠀
⠀⠙⠻⣶⣀⠀⠀⠀⠀⠀⠀⠈⠙⠲⠦⣤⣄⣀⣀⣀⣤⣤⣾⣯⡵⠞⠋⠀⠀⠀⣀⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠛⠻⠿⠿⠶⠶⠤⠤⠤⣄⣀⣀⣀⣀⣀⣀⣀⣀⡠⠤⠤⠤⠴⠖⠉⠀⠀⠀⠀⠀⠀
"""
COFFEES = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
INDENT = " " * 4
TABLE_TWO_COLUMNS = "|  {:<20}  {:<28}  |"
CURRENCY_VALUES = {
    "Pennies": 0.01,
    "Nickles": 0.05,
    "Dimes": 0.10,
    "Quarters": 0.25,
    "One Dollar Bills": 1.00,
    "Five Dollar Bills": 5.00,
}
START_WATER, START_MILK, START_COFFEE = 300, 200, 100
resources = {
    "water": START_WATER,
    "milk": START_MILK,
    "coffee": START_COFFEE,
    "money": 0.00,
}

def clear_screen():
    """Prints newlines to clear the screen."""
    print("\n" * 50)

MENU_OPTIONS = [1, 2, 3, 7, 8, 9, 0]
def print_menu():
    print("\n{:^56}".format("Coffee Machine Options"))
    print("+" + "-" * 54 + "+")
    print(TABLE_TWO_COLUMNS.format("Make a Coffee", "Manage Machine"))
    print("+" + "=" * 54 + "+")
    print(TABLE_TWO_COLUMNS.format("1. Make Espresso", "7. Add money to machine"))
    print(TABLE_TWO_COLUMNS.format("2. Make Latte", "8. Top off machine resources"))
    print(TABLE_TWO_COLUMNS.format("3. Make Cappuccino", "9. View machine report"))
    print(TABLE_TWO_COLUMNS.format(" ", "0. Turn off machine"))
    print("+" + "-" * 54 + "+")

def validate_menu_choice():
    print_menu()
    while True:
        choice = input(f"\nWhat would you like to do? ")
        if not choice.isdigit():
            print("You must enter a number.")
            continue
        # convert to int
        choice = int(choice)
        if choice not in MENU_OPTIONS:
            print("Please select a valid menu option.")
            continue
        # input is validated
        print("")
        return choice

def make_coffee(menu_number):
    if menu_number == 1:
        kind = "espresso"
    elif menu_number == 2:
        kind = "latte"
    elif menu_number == 3:
        kind = "cappuccino"
    else:
        raise Exception("Critical Error: Machine does not have that kind of coffee option that was selected!")

    # notify user of resources required and how much they have in the machine
    print(f"\nYou selected {kind}...\n")
    time.sleep(1)
    print(f"This requires {COFFEES[kind]["ingredients"]["water"]}ml water and have {resources["water"]}ml in the machine.")
    time.sleep(2)
    print(f"This requires {COFFEES[kind]["ingredients"]["milk"]}ml milk and have {resources["milk"]}ml in the machine.")
    time.sleep(2)
    print(f"This requires {COFFEES[kind]["ingredients"]["coffee"]}g coffee and have {resources["coffee"]}g in the machine.")
    time.sleep(2)
    print(f"This requires {show_money(COFFEES[kind]["cost"])} and have {show_money()} in the machine.\n")
    time.sleep(2)

    # check if machine has required resources
    missing_resources = []  # concatenated list of missing resources, if any missing
    for item, amount in resources.items():
        if item != "money":
            if amount < COFFEES[kind]["ingredients"][item]:
                missing_resources.append(item)
        else:
            if amount < COFFEES[kind]["cost"]:
                missing_resources.append(item)

    # if missing resources detected, notify user and abort
    if missing_resources:
        print("Not enough", end=" ")
        if len(missing_resources) > 1:
            for i in range(0, len(missing_resources) - 1):
                print(f"{missing_resources[i]}, and", end=" ")
        print(missing_resources[-1], end=" ")
        print("in the coffee machine.\n\n")
    else:  # enough resources, deduct from machine resources
        resources["water"] -= COFFEES[kind]["ingredients"]["water"]
        resources["milk"] -= COFFEES[kind]["ingredients"]["milk"]
        resources["coffee"] -= COFFEES[kind]["ingredients"]["coffee"]
        resources["money"] -= COFFEES[kind]["cost"]

        # serve coffee
        print("Brewing...\n")
        time.sleep(2)
        print(f"Done! Enjoy your {kind}!\n\n")

    time.sleep(6)
    clear_screen()

def show_money(amount=float("-inf")):
    """Returns the money in coffee machine in a printable format if no argument is given,
    else will return the argument given in a printable format."""
    if amount != float("-inf"):
        return f"${amount:.2f}"
    else:
        return f"${resources["money"]:.2f}"

def add_money():
    money_user_adding = {}
    total_money_value = 0
    print(f"\nTotal money in coffee machine is {show_money()}")
    time.sleep(1)
    # display the currencies accepted at this machine
    print("\nThe machine accepts ", end="")
    for i, currency in enumerate(CURRENCY_VALUES):
        if i != len(CURRENCY_VALUES) - 1:
            print(f"{currency}, ", end="")
        else:
            print(f"and {currency}.\n")
    time.sleep(1)
    # ask user how much of each currency they want to add
    for currency in CURRENCY_VALUES:
        while True:
            amount = input(f"How many {currency} do you want to insert? ")
            if not amount.isdigit():
                print("Please enter a valid number.")
                time.sleep(1)
                continue
            money_user_adding[currency] = int(amount)
            break
    # calculate total money user has inserted into the machine
    for val in money_user_adding:
        total_money_value += CURRENCY_VALUES[val] * money_user_adding[val]
    # add money user added to machine resources
    resources["money"] += total_money_value
    print(f"\nYou have added a total of {show_money(total_money_value)} to the coffee machine!")
    print("Loading the machine main menu...")
    time.sleep(4)
    clear_screen()

def reset_machine_resources():
    global resources
    print("Topping off the coffee machine with water, milk, and coffee grounds...")
    time.sleep(2)
    resources["water"] = START_WATER
    resources["milk"] = START_MILK
    resources["coffee"] = START_COFFEE
    print("You finished topping off the water, milk, and coffee grounds in the machine!")
    time.sleep(1)
    print("\nReturning to machine main menu in 5...4...")
    time.sleep(5)
    clear_screen()

def print_resources():
    clear_screen()
    print("Current resources in machine:")
    print(f"{INDENT}Water: ".ljust(12, " ") + f"{resources["water"]}ml")
    print(f"{INDENT}Milk: ".ljust(12, " ") + f"{resources["milk"]}ml")
    print(f"{INDENT}Coffee: ".ljust(12, " ") + f"{resources["coffee"]}g")
    print(f"{INDENT}Money: ".ljust(12, " ") + show_money())
    print("\nReturning to machine main menu in 7...6...")
    time.sleep(7)
    clear_screen()

def shut_down():
    """Shuts down the coffee machine"""
    print(f"The machine ejects {show_money()}..")
    print("and screen displays: Shutting down...")
    exit()

def main():
    print(COFFEE_ART)
    print("You power on the coffee machine and insert $2.00 into the machine...\n\n\n")
    resources["money"] = 2.00
    time.sleep(2)
    while True:
        # force user to add money if machine has none
        if resources["money"] <= 0:
            clear_screen()
            print("Before you can interact with the coffee machine, you must first add some money...")
            time.sleep(1)
            add_money()
            continue
        # let user choose and perform a menu option on machine
        menu_choice = validate_menu_choice()
        if 1 <= menu_choice <= 3:
            make_coffee(menu_choice)
        elif menu_choice == 7:
            add_money()
        elif menu_choice == 8:
            reset_machine_resources()
        elif menu_choice == 9:
            print_resources()
        elif menu_choice == 0:
            shut_down()
        else:
            raise Exception("Critical Error: could not activate machine action!")

if __name__ == "__main__":
    main()