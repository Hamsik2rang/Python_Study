class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def print(self):
        print(f"text = {self.text}")
        print(f"answer = {self.answer}")
