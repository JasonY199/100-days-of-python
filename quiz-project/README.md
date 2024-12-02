# Quiz Project

This project is a quiz game that allows users to test their knowledge on a variety of topics. The user will be able to select a topic and answer a series of questions. The user will be given feedback on their answers and a final score at the end of the quiz.

In this projects course tutorial, they are not dynamically fetching the questions from the Open Trivia Database API. Instead, they are using a set of local questions that have fetched using the API once during the development phase. I, on the other hand, made the program dynamically fetch the questions from the API each time the program is run. This way, the user should get a unique set of questions each time they run the program.

## Features

- The program is dynamically using the Open Trivia Database API to fetch questions. Each time the program is run, the user should get a unique set of questions. If the API call fails, the program will use a set of local questions.
- The backend is implemented using OOP principles. The program is divided into classes that represent the different components of the quiz game.

## How to run the project

1. Ensure Python 3.12.x is installed on your system (what was using during development of this program)
2. Clone the repository

    ```git clone https://github.com/jason/100-days-of-python.git```

3. Open the terminal and navigate to the project directory

    ```cd 100-days-of-python/quiz_project```

4. Create a virtual environment by running the command:

    ```python3 -m venv venv```

5. On Mac, activate the virtual environment by running the command:

    ```source venv/bin/activate```

6. Install the dependencies by running the command:

    ```pip install -r requirements.txt```

7. Start the application by running the command:

    ```python3 main.py```