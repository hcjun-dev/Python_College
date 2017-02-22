## Hyungchol
# 2014-04-11
# P_9.7

'''
Implement a class Student. For the purpose of this exercise, a student has a name and a total quiz score.
Supply and appropriate constructor and methods getName(), addQuiz(score), getTotalScore(), and getAverageScore().
To continue the latter, you also need to store the number of quizzes that the student took.
'''
import random

# class student
class Student(object):
    def __init__(self, name, quizscore):
        self._name = str(name)
        self._quizScore = quizscore
        self._totalScore = quizscore
        self._numOfQuiz = 0

    def getName(self): # if calling self, getting name
        return self._name

    def getTotalScore(self):
        return self._totalScore

    def getAverageScore(self):
        return self._totalScore / self._numOfQuiz

    def addQuiz(self, score):  # add value no returns
        self._numOfQuiz += 1
        self._totalScore = self._totalScore + score


# Just a sample main using random quiz scores.
def func0414():
    Hyungchol = Student("Hyungchol", 100)
    for i in range(random.randint(1, 10)):
        Hyungchol.addQuiz(random.randint(1, 100))
    print(Hyungchol.getName())
    print(Hyungchol.getTotalScore())
    print("%.2f" %Hyungchol.getAverageScore())

