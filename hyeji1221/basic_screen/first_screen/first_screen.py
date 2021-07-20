import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from start_screen1 import start_screen1
from start_screen2 import start_screen2


form_class=uic.loadUiType("first_screen.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init.clicked.connect(self.initButton)
        self.continue_2.clicked.connect(self.continueButton)
        self.exit.clicked.connect(QCoreApplication.instance().quit)

    def initButton(self):
        #print("init")
        self.hide()
        self.start_screen1 = start_screen1()
        self.start_screen1.exec()
        self.show()

    def continueButton(self):
        #print("continue")
        self.hide()
        self.start_screen2 = start_screen2()
        self.start_screen2.exec()
        self.show()

  #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()