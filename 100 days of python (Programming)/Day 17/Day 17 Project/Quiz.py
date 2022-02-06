
# Day 17 Quiz Project 
# and benefits of Object Oriented Programming

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# converting questions from question_data to object
question_bank = []
for question in question_data:
    ## using question_data
    #new_question = Question(q_text = question["text"],q_attribute = question["answer"])
    # using new question_data
    new_question = Question(q_text = question["question"],q_attribute = question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score: {quiz.score}")