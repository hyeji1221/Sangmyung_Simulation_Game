import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtGui import *

import os

sys.path.append("C:/Users/USER/PycharmProjects/sangmyung_simulation_game/SSG_BS/basic_screen")
#from * import basic_screen

form_class=uic.loadUiType("first_screen.ui")[0]
form_class1=uic.loadUiType("init_screen.ui")[0]

class WindowClass(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("first_screen.ui", self)
        self.init.clicked.connect(self.initButton)
        self.continue_2.clicked.connect(self.continueButton)
        self.exit.clicked.connect(QCoreApplication.instance().quit)

    def initButton(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print("init")
    def continueButton(self):
        widget.setCurrentIndex(widget.currentIndex() + 2)
        print("continue")
class InitClass(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("init_screen.ui", self)
        self.label.hide()
        self.OK.hide()
        self.time.clicked.connect(self.timeButton)
    def timeButton(self):
        self.label.show()
        file=QFileDialog.getOpenFileNames(self)
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("time.jpg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaled(801,571)
        self.label.setPixmap(self.qPixmapFileVar)
        self.OK.show()
        self.OK.clicked.connect(self.OKButton)
    def OKButton(self):
        self.label.hide()
        self.OK.hide()

class ContinueCalss(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("continue_screen.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    myWindow = WindowClass()
    InitWindow = InitClass()
    continueWindow=ContinueCalss()

    widget.addWidget(myWindow)
    widget.addWidget(InitWindow)
    widget.addWidget(continueWindow)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()
    app.exec_()