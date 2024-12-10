from views.QuizView import QuizView
import json

"""
1. Create a quiz view
2. Pass question data from json file
3. Save results to file
"""
with open("data/quiz1.json", "r") as quizData:
    questionsData = quizData.read()
    questions = json.loads(questionsData)
quiz = QuizView(questions)
