import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

sys.path.append("C:/Users/USER/OneDrive/바탕 화면/sangmyung_simulation_game-main/sangmyung_simulation_game-main/SSG_BS")
#from . import basic_screen



form_class=uic.loadUiType("first_screen.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init.clicked.connect(self.initButton)
        self.continue_2.clicked.connect(self.continueButton)
        self.exit.clicked.connect(QCoreApplication.instance().quit)

    def initButton(self):
        print("init")
    def continueButton(self):
        print("continue")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec_()