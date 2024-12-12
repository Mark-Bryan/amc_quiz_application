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

        else:
            print("This is the first question. Cannot go back further.")

    def displayQuestion(self):
        pass

    def submit(self, selectedAnswer):
        self.responses[str(self.currentQuestion)] = selectedAnswer

    def endQuiz(self):
        pass

    def getScore(self):
        self.score = 0
        i = 0
        for answer in self.responses.values():
            if answer == self.questions[i].answer:
                self.score += 1
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
        # This frame is to hold the question details
        results_frame = Frame(scoreWindow)
        results_frame.pack(padx=20, pady=20)
        # Looping through the questions

        i = 0
        for question in self.questions:
            user_answer = self.responses.get(i)
            is_correct = user_answer == question.answer
            # Displaying the question text and number
            question_label = Label(results_frame, text=f"Q{i + 1}: {question.question}")
            question_label.pack(padx=5, pady=5)
            # Displaying the answer the user selected
            if is_correct:
                user_answer_label = Label(
                    results_frame, text=f"Your Answer : {user_answer}", fg="green"
                )
            else:
                user_answer_label = Label(
                    results_frame, text=f"Your Answer : {user_answer}", fg="red"
                )

                user_answer_label.pack(padx=20, pady=20)
            # Displaying the tick or cross
            if is_correct:
                correct_answer = Label(results_frame, text="✓", fg="green")
            else:
                correct_answer = Label(results_frame, text="X", fg="red")
                correct_answer.pack(padx=20, pady=20)

                i += 0

        closeBtn = Button(scoreWindow, text="Close", command=scoreWindow.destroy)
        closeBtn.pack(pady=10)

        scoreWindow.mainloop()
