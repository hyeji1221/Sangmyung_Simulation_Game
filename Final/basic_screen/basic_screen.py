import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

form_class=uic.loadUiType("basic_screen.ui")[0]

class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("basic_screen.ui", self)
        self.menuBox.hide()
        self.imageLabel.hide()
        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)

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
        self.imageLabel.show()
        self.pixmap = QImage("map.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))

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

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    widget = QtWidgets.QStackedWidget()
    myWindow = WindowClass()
    widget.addWidget(myWindow)

    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()