import random

class Question:
	
	answerIndex = ['A','B','C','D']
	def __init__(self, q, a):
		self.rightAnswerIndex = ''
		self.question = q
		self.rightAnswer = a[0]

		self.answers = a
		random.shuffle(self.answers)
		
		self.rightAnswerIndex = self.answerIndex[self.answers.index(self.rightAnswer)]