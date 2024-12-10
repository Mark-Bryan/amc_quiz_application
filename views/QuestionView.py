from tkinter import *


class QuestionView:

    def __init__(self, question, nextBtnAction, prevBtnAction, submitBtnAction):
        self.question = question
        self.optionBtns = []
        self.nextBtnAction = nextBtnAction
        self.prevBtnAction = prevBtnAction
        self.submitBtnAction = submitBtnAction

        self.window = Tk()
        self.window.title(self.question.question)

        self.response = StringVar(value="")

        questionLabel = Label(self.window, text=self.question.question)
        questionLabel.pack(padx=50, pady=50)

        for option in self.question.options:
            radioBtn = Radiobutton(
                self.window,
                text=option,
                value=option,
                variable=self.response,
                command=lambda opt=option: self.response.set(opt),
            )
            radioBtn.pack(pady=10)
            self.optionBtns.append(radioBtn)

        self.optionBtns[0].select()

        actionPanel = Frame(self.window)

        previousBtn = Button(actionPanel, text="Previous", command=self.handlePrevious)
        previousBtn.pack(pady=10, side=LEFT)

        submitBtn = Button(actionPanel, text="Submit", command=self.handleSubmit)
        submitBtn.pack(pady=10, side=LEFT)

        nextBtn = Button(actionPanel, text="Next", command=self.handleNext)
        nextBtn.pack(pady=10, side=RIGHT)

        actionPanel.pack(pady=20)

        self.window.mainloop()

    def closeWindow(self):
        self.window.destroy()

    def handlePrevious(self):
        self.window.destroy()
        self.prevBtnAction()

    def handleNext(self):
        self.window.destroy()
        self.nextBtnAction()

    def handleSubmit(self):
        self.window.destroy()
        self.submitBtnAction(self.response.get())
        self.nextBtnAction()
