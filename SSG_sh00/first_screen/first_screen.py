import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from information_screen import information_screen
from SaveInformation_screen import SaveInformation_screen

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
        self.hide()  # 메인 윈도우 숨김
        self.information_screen = information_screen()
        self.information_screen.exec()  # 두번째창 닫을때까지 기다림
        self.show()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐

    def continueButton(self):
        print("continue")
        self.hide()  # 메인 윈도우 숨김
        self.SaveInformation_screen = SaveInformation_screen()
        self.SaveInformation_screen.exec()  # 두번째창 닫을때까지 기다림
        self.show()  # 두번째창 닫으면 다시 첫 번째 창 보여 짐


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()