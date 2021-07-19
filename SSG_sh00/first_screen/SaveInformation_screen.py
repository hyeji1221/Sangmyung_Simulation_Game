import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

form_SaveInformationScreen = uic.loadUiType("SaveInformation_screen.ui")[0]

class SaveInformation_screen(QDialog,QWidget, form_SaveInformationScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.cancelButton.clicked.connect(self.Home)

    def Home(self):
        self.close()  # 창 닫기