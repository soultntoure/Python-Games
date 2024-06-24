from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qn in question_data:
    question_text = qn['text']
    question_answer = qn['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_qns():
    quiz.next_qn()


print("You've completed the quiz!")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")   