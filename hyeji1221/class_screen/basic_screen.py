import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

form_class=uic.loadUiType("basic_screen.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_image()
        self.menuBox.hide()

        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)
        self.upBtn.clicked.connect(self.up_btn)
        self.downBtn.clicked.connect(self.down_btn)
        self.number = 0

    def show_image(self):

        pixmap = QPixmap('img/1.PNG')
        self.img_label.setPixmap(pixmap.scaled(self.img_label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.show()

    def slot_toggle(self):
        if self.menu.isChecked():
            self.button_clicked()
        else:
            self.menuOff()
            self.menuBox.hide()


    def button_clicked(self):
        self.menuBox.show()
        self.map.clicked.connect(self.mapButton)
        self.mission.clicked.connect(self.missionButton)
        self.time.clicked.connect(self.timeButton)
        self.save.clicked.connect(self.saveButton)
        self.exit.clicked.connect(self.close)

    def mapButton(self):
        print("map")

    def missionButton(self):
        print("mission")

    def saveButton(self):
        print("save")

    def timeButton(self):
        print("time")

    def menuOff(self):
        self.map.disconnect()
        self.mission.disconnect()
        self.save.disconnect()
        self.exit.disconnect()

    def closeEvent(self, QCloseEvent):
        re = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)

        if re == QMessageBox.Yes:
            print("exit")
            QCloseEvent.accept()
        else:
            print("Not exit")
            QCloseEvent.ignore()

    def up_btn(self):
        self.number += 1
        print(self.number)
        root = 'img/' + str(self.number) +'.PNG'
        pixmap = QPixmap(root)
        self.img_label.setPixmap(pixmap.scaled(self.img_label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.show()


    def down_btn(self):
        self.number -= 1
        print(self.number)
        root = 'img/' + str(self.number) + '.PNG'
        pixmap = QPixmap(root)
        self.img_label.setPixmap(pixmap.scaled(self.img_label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()