# OX 퀴즈
from data import question_data
from question_model import Question
from quiz_brain import QuizManager


question_bank = []

for question in question_data:
    temp_text = question["text"]
    temp_answer = question["answer"]
    new_question = Question(answer=temp_answer, text=temp_text)
    question_bank.append(new_question)

quiz_manager = QuizManager(question_bank)

quiz_manager.process()