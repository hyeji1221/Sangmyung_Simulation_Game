import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

form_InformationScreen = uic.loadUiType("information_screen.ui")[0]

class information_screen(QDialog,QWidget, form_InformationScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.sid = QImage("basic.jpg").scaled(311,120)
        self.cancelButton.clicked.connect(self.Home)
        self.timetableButton.clicked.connect(self.openFileNameDialog)

    def Home(self):
        self.close()  # 창 닫기

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawImages(painter)
        painter.end()

    def drawImages(self, painter):
        painter.drawImage(300,370,self.sid)

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "불러올 시간표를 선택하세요.","",
                                                  "All Files (*);;Python Files (*.py)")
        if fileName:
            print(fileName)
            self.sid = QImage(fileName).scaled(311,120)
