import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType("basic_screen.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chat.setStyleSheet('QLabel {background-color: rgb(204,255,255)}')
        self.menu.setStyleSheet('background: rgb(255,204,0)')
        self.menu_screen.hide()
        self.menu.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.speak.hide()
        self.menu_screen.show()
        self.quit.clicked.connect(QCoreApplication.instance().quit)
        self.save.clicked.connect(self.saveButton)
        self.mission.clicked.connect(self.missionButton)
        self.map.clicked.connect(self.mapButton)
        self.out.clicked.connect(self.outButton)

    def saveButton(self):
        print("save")
    def missionButton(self):
        print("mission")
    def mapButton(self):
        print("map")
    def outButton(self):
        self.menu_screen.hide()
        #self.quit.disconnect()
        #self.save.disconnect()
        #self.mission.disconnect()
        #self.map.disconnect()
        self.speak.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec_()