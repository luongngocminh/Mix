from Tkinter import *
import tkFileDialog as filedialog
from ParseDoc import Execute

class Application(Frame):
	def open_setting():
		print 'OPEN'
	def find_doc(self):
		file_path = filedialog.askopenfilename()
		if file_path != '':
			Execute(file_path)
			self.Stt['text'] = 'DONE!'
	def find_docs(self):
		files_path = filedialog.askopenfilenames()

	def createWidgets(self):

		self.Open_doc = Button(self)
		self.Open_doc['text'] = 'Mix One Document'
		self.Open_doc['command'] = self.find_doc
		self.Open_doc['width'] = 20
		self.Open_doc['height'] = 2
		self.Open_doc.pack({'fill': 'none', 'expand': True,'pady': 2})

		self.Open_docs = Button(self)
		self.Open_docs['text'] = 'Mix From Other Documents'
		self.Open_docs['command'] = self.find_docs
		self.Open_docs['width'] = 20
		self.Open_docs['height'] = 2
		self.Open_docs.pack({'fill': 'none', 'expand': True,'pady': 2})
		
		self.Setting = Button(self)
		self.Setting['text'] = 'Setting'
		self.Setting['command'] = self.open_setting
		self.Setting['width'] = 20
		self.Setting['height'] = 2
		self.Setting.pack({'fill': 'none', 'expand': True,'pady': 2})

		self.QUIT = Button(self)
		self.QUIT["text"] = "Quit"
		self.QUIT['fg'] = 'red'
		self.QUIT['command'] = self.quit
		self.QUIT['width'] = 20
		self.QUIT['height'] = 2
		self.QUIT.pack({'fill': 'none', 'expand': True,'pady': 2})


		self.Stt = Label(self)
		self.Stt['text'] = 'Ready!'
		self.Stt['fg'] = 'green'
		self.Stt.pack({'fill': 'none', 'expand': True,'side': 'bottom','pady': 20})
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack(padx=20, pady=20)
		self.createWidgets()

