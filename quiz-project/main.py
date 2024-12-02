from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# build a question bank from the data in question_data
# each of these items will be a Question object in the question_bank list
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

# create a QuizBrain object and start the quiz
quiz = QuizBrain(question_bank)

# loop through the questions in the quiz
while quiz.still_has_questions():
    quiz.next_question()

# print the final score
quiz.final_score()