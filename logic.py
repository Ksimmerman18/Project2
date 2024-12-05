from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_Grades):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.score_lable1.hide()
        self.score_lable2.hide()
        self.score_lable3.hide()
        self.score_lable4.hide()
        self.score_line_edit1.hide()
        self.score_line_edit2.hide()
        self.score_line_edit3.hide()
        self.score_line_edit4.hide()

