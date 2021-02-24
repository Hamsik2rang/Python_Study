import random


class QuizManager:
    def __init__(self, quiz):
        self.quiz = quiz
        self.next_quiz = random.choice(self.quiz)
        self.score = 0
        self.is_finish = False

    def check(self, answer):
        if answer == self.next_quiz.answer.lower():
            self.score += 1
            print(
                f"Correct! Your current score is {self.score}. Let's go to next quiz."
            )
            return False
        else:
            return True

    def next_question(self):
        self.quiz.remove(self.next_quiz)
        self.next_quiz = random.choice(self.quiz)

    def process(self):
        while not self.is_finish:
            print(f"Quiz {self.score+1}.")
            print(f"{self.next_quiz.text}")
            answer = input("If it is true, Type 'true', or 'false': ").lower()

            self.is_finish = self.check(answer)
            if self.is_finish:
                print(f"You were Wrong. Game Over. Your final score is {self.score}.")
            elif len(self.quiz) == 0:
                print(f"You hitted ALL quizzes! Your final score is {self.score}")
                self.is_finish = True
            else:
                self.next_question()