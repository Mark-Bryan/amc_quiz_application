from tkinter import *
from classes.Question import Question
from views.QuestionView import QuestionView


class QuizView:

    questions = []
    responses = {}
    currentQuestion = 0
    score = 0
    questionWindow = None

    def __init__(self, questions):
        for index in range(1, len(questions) + 1):
            newQuestion = Question(id=index, questionData=questions[str(index)])
            self.questions.append(newQuestion)

        welcomeScreen = Tk()
        welcomeScreen.geometry("400x200")
        welcomeScreen.title("Welcome to the Quiz App")
        welcomeTxt = Label(welcomeScreen, text="Press the button to start your quiz")
        welcomeTxt.pack()

        startBtn = Button(welcomeScreen, text="Start", command=self.start)
        startBtn.pack(padx=50, pady=50)

        welcomeScreen.mainloop()

    def start(self):
        self.currentQuestion = 0
        question = self.questions[self.currentQuestion]
        self.questionWindow = QuestionView(
            question, self.nextQuestion, self.previousQuestion, self.submit
        )

    def nextQuestion(self):
        self.currentQuestion += 1
        if self.currentQuestion < (len(self.questions)):
            nextQuestion = self.questions[self.currentQuestion]
            self.questionWindow = QuestionView(
                nextQuestion, self.nextQuestion, self.previousQuestion, self.submit
            )
        else:
            self.displayScore()

    def previousQuestion(self):
        if self.currentQuestion > 0:
            self.currentQuestion -= 1
            previousQuestion = self.questions[self.currentQuestion]

            self.questionWindow = QuestionView(
                previousQuestion, self.nextQuestion, self.previousQuestion, self.submit
            )

    def displayQuestion(self):
        pass

    def submit(self, selectedAnswer):
        self.responses[str(self.currentQuestion)] = selectedAnswer

    def endQuiz(self):
        pass

    def getScore(self):
        i = 0
        for answer in self.responses.values():
            if answer == self.questions[i].answer:
                self.score += 1
                i += 1
            else:
                i += 1
        return self.score

    def displayScore(self):
        scoreWindow = Tk()
        scoreWindow.title("Quiz Results")

        scoreMessage = Label(
            scoreWindow,
            text=f"Your final score is {self.getScore()} out of {len(self.questions)}",
        )
        scoreMessage.pack(padx=20, pady=20)

        closeBtn = Button(scoreWindow, text="Close", command=scoreWindow.destroy)
        closeBtn.pack(pady=10)

        scoreWindow.mainloop()
