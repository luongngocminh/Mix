# -*- coding: UTF-8 -*-

from Tkinter import *
import tkFileDialog as filedialog
from ui import Application







root = Tk()
app = Application(master=root)
app.master.title('Mixe')
app.mainloop()
root.destroy()