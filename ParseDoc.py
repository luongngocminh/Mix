# -*- coding: UTF-8 -*-
import  random,re
from docx import Document
from Export import export
from QuestionObject import Question


def Execute(filePath):
	document = Document(filePath)
	questions = []
	para = document.paragraphs
	for i in range(len(para)):	
		answers = []
		if (u'Question' in para[i].text) or (u'Câu' in para[i].text):
			try:
				q = para[i].text.split(':')[1]
				a = para[i+1].text
				a = re.sub(r'\s\s+','\t',a).split('\t')
				for j in range(len(a)):
					answers.append(a[j].split('.')[1])
			except Exception, e:
				print (q,  e)
			question = Question(q,answers)
			questions.append(question)


	# Shuffle the questions
	random.shuffle(questions)

	# Get right Answer
	for i in questions:
		print i.answers
		print i.rightAnswerIndex

	# Export all the shuffled questions to a new document
	export(questions)
