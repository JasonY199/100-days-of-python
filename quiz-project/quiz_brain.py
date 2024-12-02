import time


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self)-> bool:
        """Returns True if there are still questions in the quiz, False otherwise."""
        return self.question_number < len(self.question_list)
    
    def next_question(self)-> None:
        """Asks the user the next question in the quiz and checks if the answer is correct."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(choice, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer)-> None:
        """Checks if the user's answer is correct and lets them know. Updates the score."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        time.sleep(0.5)
        print(f"The correct answer was: {correct_answer}.")
        time.sleep(0.5)
        print(f"Your current score is: {self.score}/{self.question_number}\n")
        time.sleep(1)

    def final_score(self)-> None:
        """Prints the final score of the quiz."""
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}")