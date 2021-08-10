import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

form_lunch_location_screen = uic.loadUiType("lunch_location_screen.ui")[0]

class lunch_location_screen(QDialog,QWidget, form_lunch_location_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()  # 두번째 ui창을 띄우기
        self.menuBox.hide()

        self.condition=0
        self.pixmap = QImage("location1.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))

        self.upButton.clicked.connect(self.selectUp)
        self.leftButton.clicked.connect(self.selectLeft)

        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)

    def selectUp(self):
        if self.condition == 0:
            self.pixmap = QImage("location2.jpg").scaled(651, 361)
            self.imageLabel.setPixmap(QPixmap(self.pixmap))
        elif self.condition == 1:
            self.pixmap = QImage("location4.jpg").scaled(651, 361)
            self.imageLabel.setPixmap(QPixmap(self.pixmap))
        elif self.condition == 2:
            self.pixmap = QImage("location5.jpg").scaled(651, 361)
            self.imageLabel.setPixmap(QPixmap(self.pixmap))
        elif self.condition == 3:
            self.pixmap = QImage("location6.jpg").scaled(651, 361)
            self.imageLabel.setPixmap(QPixmap(self.pixmap))
        elif self.condition == 4:
            self.pixmap = QImage("location7.jpg").scaled(651, 361)
            self.imageLabel.setPixmap(QPixmap(self.pixmap))
        elif self.condition == 5:
            self.pixmap = QImage("location8.jpg").scaled(651, 361)
            self.imageLabel.setPixmap(QPixmap(self.pixmap))

        self.condition += 1

    def selectLeft(self):
        self.pixmap = QImage("location3.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))


# 메뉴 버튼 구현 -------------------------------------------------------------------------
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
        self.time.disconnect()

    def closeEvent(self, QCloseEvent):
        re = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)

        if re == QMessageBox.Yes:
            print("exit")
            QCloseEvent.accept()
        else:
            print("Not exit")
            QCloseEvent.ignore()
