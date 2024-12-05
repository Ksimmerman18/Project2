# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Grades(object):
    def setupUi(self, Grades):
        Grades.setObjectName("Grades")
        Grades.resize(300, 250)
        Grades.setMinimumSize(QtCore.QSize(300, 250))
        Grades.setMaximumSize(QtCore.QSize(300, 250))
        self.centralwidget = QtWidgets.QWidget(parent=Grades)
        self.centralwidget.setObjectName("centralwidget")
        self.student_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.student_name_label.setGeometry(QtCore.QRect(10, 10, 125, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.student_name_label.setFont(font)
        self.student_name_label.setObjectName("student_name_label")
        self.Student_line_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Student_line_edit.setGeometry(QtCore.QRect(140, 10, 130, 20))
        self.Student_line_edit.setObjectName("Student_line_edit")
        self.attempts_line_edit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.attempts_line_edit.setGeometry(QtCore.QRect(140, 38, 130, 20))
        self.attempts_line_edit.setObjectName("attempts_line_edit")
        self.score_line_edit1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.score_line_edit1.setGeometry(QtCore.QRect(140, 68, 130, 20))
        self.score_line_edit1.setObjectName("score_line_edit1")
        self.score_line_edit2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.score_line_edit2.setGeometry(QtCore.QRect(140, 98, 130, 20))
        self.score_line_edit2.setObjectName("score_line_edit2")
        self.score_line_edit3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.score_line_edit3.setGeometry(QtCore.QRect(140, 128, 130, 20))
        self.score_line_edit3.setObjectName("score_line_edit3")
        self.score_line_edit4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.score_line_edit4.setGeometry(QtCore.QRect(140, 158, 130, 20))
        self.score_line_edit4.setObjectName("score_line_edit4")
        self.attemps_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.attemps_label.setGeometry(QtCore.QRect(10, 40, 125, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.attemps_label.setFont(font)
        self.attemps_label.setObjectName("attemps_label")
        self.score_lable1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.score_lable1.setGeometry(QtCore.QRect(10, 70, 125, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.score_lable1.setFont(font)
        self.score_lable1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.score_lable1.setObjectName("score_lable1")
        self.score_lable2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.score_lable2.setGeometry(QtCore.QRect(10, 100, 125, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.score_lable2.setFont(font)
        self.score_lable2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.score_lable2.setObjectName("score_lable2")
        self.score_lable3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.score_lable3.setGeometry(QtCore.QRect(10, 130, 125, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.score_lable3.setFont(font)
        self.score_lable3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.score_lable3.setObjectName("score_lable3")
        self.score_lable4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.score_lable4.setGeometry(QtCore.QRect(10, 160, 125, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.score_lable4.setFont(font)
        self.score_lable4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.score_lable4.setObjectName("score_lable4")
        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(50, 185, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        Grades.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Grades)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 18))
        self.menubar.setObjectName("menubar")
        Grades.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Grades)
        self.statusbar.setObjectName("statusbar")
        Grades.setStatusBar(self.statusbar)

        self.retranslateUi(Grades)
        QtCore.QMetaObject.connectSlotsByName(Grades)

    def retranslateUi(self, Grades):
        _translate = QtCore.QCoreApplication.translate
        Grades.setWindowTitle(_translate("Grades", "Grades"))
        self.student_name_label.setText(_translate("Grades", "Student name:"))
        self.attemps_label.setText(_translate("Grades", "No of attempts:"))
        self.score_lable1.setText(_translate("Grades", "Score 1:    "))
        self.score_lable2.setText(_translate("Grades", "Score 2:    "))
        self.score_lable3.setText(_translate("Grades", "Score 3:    "))
        self.score_lable4.setText(_translate("Grades", "Score 4:    "))
        self.submit_button.setText(_translate("Grades", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Grades = QtWidgets.QMainWindow()
    ui = Ui_Grades()
    ui.setupUi(Grades)
    Grades.show()
    sys.exit(app.exec())