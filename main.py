from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

while quiz.is_next_question():
    quiz.next_question()

print("You completed the quiz.")
print(f"Your final score is: {quiz.score}/12")
