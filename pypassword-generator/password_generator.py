import random


class PasswordGenerator:
    '''
    A class to generate secure passwords with customizable components.

    This class allows users to generate passwords by specifying the 
    number of letters, symbols, and numbers. It also maintains a 
    history of the last five generated passwords for easy reference.
    '''
    def __init__(self):
        # Code for these 3 lists was provided in the "100 Days of Python" course on Udemy.
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        self.num_letters = None
        self.num_symbols = None
        self.num_numbers = None
        self.password_history = []  # List to store generated passwords
        self.max_history = 5  # Maximum number of passwords to store
    

    def set_password_parameters(self, num_letters: int, num_symbols: int, num_numbers: int) -> None:
        '''Set the number of letters, symbols, and numbers in the password.'''
        self.num_letters = num_letters
        self.num_symbols = num_symbols
        self.num_numbers = num_numbers


    def generate_password(self) -> None:
        password = []  # List to store the password

        # Add the required number of letters, symbols, and numbers to the password
        for _ in range(self.num_letters):
            password.append(random.choice(self.letters))
        for _ in range(self.num_symbols):
            password.append(random.choice(self.symbols))
        for _ in range(self.num_numbers):
            password.append(random.choice(self.numbers))

        random.shuffle(password)  # Shuffle the password
        password = ''.join(password)  # Convert the list to a string
        self.password_history.append(password)  # Add the generated password to the history

        # Remove the oldest password if the history is too long
        if len(self.password_history) > self.max_history:
            self.password_history.pop(0)


    def clear_password_history(self) -> None:
        '''Clear the password history.'''
        self.password_history = []


    def get_last_password(self) -> str:
        '''Return the last generated password.'''
        if len(self.password_history) == 0:
            return None
        return self.password_history[-1]

    
    def get_password_history(self) -> list:
        '''Return the list of generated passwords.'''
        if len(self.password_history) == 0:
            return None
        return self.password_history
