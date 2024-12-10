class Question:

    def __init__(self, id, questionData):
        self.id = id
        self.question = questionData["question"]
        self.options = questionData["options"]
        self.answer = questionData["answer"]

    def checkAnswer(self, answer):
        pass
