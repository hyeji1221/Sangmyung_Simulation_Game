import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("menu.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chat.setStyleSheet('QLabel {background-color: #C3C3C3}')
        self.menuBox.hide()

        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)

    def slot_toggle(self):
        if self.menu.isChecked():
            self.button_clicked()
        else:
            self.menuBox.hide()

    def button_clicked(self):
        self.count=0
        self.menuBox.show()
        self.map.clicked.connect(self.mapButton)
        self.mission.clicked.connect(self.missionButton)
        self.save.clicked.connect(self.saveButton)
        self.exit.clicked.connect(self.exitButton)

    def mapButton(self):
        print("map")

    def missionButton(self):
        print("mission")

    def saveButton(self):
        print("save")

    def exitButton(self):
        print("exit")

    def menuOff(self):
        self.menuBox.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()