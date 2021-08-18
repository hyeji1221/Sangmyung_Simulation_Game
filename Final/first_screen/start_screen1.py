import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

global name,id,cl,grade
form_class=uic.loadUiType("start_first.ui")[0]

class start_screen1(QDialog,QWidget, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.start_btn.clicked.connect(self.startButton)
        self.time_btn.clicked.connect(self.timeButton)
        self.cancel_btn.clicked.connect(self.cancelBtn)


    def cancelBtn(self):
        self.close()

    def startButton(self):
        name = self.textEdit.toPlainText()
        id= self.textEdit_2.toPlainText()
        cl=self.textEdit_3.toPlainText()
        grade=self.textEdit_4.toPlainText()
        print(name,id,cl,grade)

    def timeButton(self):
        global FileOpen
        FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')
        pixmap = QPixmap(FileOpen[0])
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.show()
        print(FileOpen[0])
