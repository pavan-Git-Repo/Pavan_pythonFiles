from quiz_class import QuizBrain
from new_question_data import question_data
class Question:
    def __init__(self,text,answer):
        self.text = text 
        self.answer  = answer
new_question = Question("What","False")
 
from new_question_data import question_data
question_bank = []
for question in question_data:
    question_text  = question["text"]
    question_answer  = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")


