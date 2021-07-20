# 이어하기
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType("following.ui")[0]

class start_screen2(QDialog,QWidget, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save1_btn.clicked.connect(self.save1Button)
        self.save2_btn.clicked.connect(self.save2Button)
        self.save3_btn.clicked.connect(self.save3Button)
        self.cancel_btn.clicked.connect(self.cancelBtn)

    def save1Button(self):
        print("1")

    def save2Button(self):
        print("2")

    def save3Button(self):
        print("3")

    def cancelBtn(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = start_screen2()
    myWindow.show()
    app.exec_()
