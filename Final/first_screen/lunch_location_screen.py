import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from mission import Mission
import pathlib
import pandas as pd

form_lunch_location_screen = uic.loadUiType("lunch_location_screen.ui")[0]

class lunch_location_screen(QDialog,QWidget, form_lunch_location_screen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()  # 두번째 ui창을 띄우기
        self.menuBox.hide()
        self.finishButton.hide()

        self.condition=0
        self.pixmap = QImage("location1.jpg").scaled(801, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))

        self.upButton.clicked.connect(self.selectUp)
        self.leftButton.clicked.connect(self.selectLeft)
        self.rightButton.clicked.connect(self.selectRight)

        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)

        # 스타일 변경-------------------------------------------------------
        self.menuBox.setStyleSheet("background-color: rgb(246,246,246,130)")
        self.map.setStyleSheet("background-color: rgb(225)")
        self.mission.setStyleSheet("background-color: rgb(225)")
        self.time.setStyleSheet("background-color: rgb(225)")
        self.save.setStyleSheet("background-color: rgb(225)")
        self.out_btn.setStyleSheet("background-color: rgb(225)")
        self.exit.setStyleSheet("background-color: rgb(225)")

    def selectUp(self):
        self.move(1)
    def selectLeft(self):
        self.move(2)
    def selectRight(self):
        self.move(3)

    def move(self, condition):
        if self.pixmap==QImage("location1.jpg").scaled(801, 361):
            if condition==1:
                self.pixmap = QImage("location2.jpg").scaled(801, 361)
                self.imageLabel.setPixmap(QPixmap(self.pixmap))
                self.chat.setText("이 방향으로 가면 도착지와 가까워질 것 같다")
            else:
                self.chat.setText("이 방향으로 가면 도착지와 멀어질 것 같다...")

        elif self.pixmap==QImage("location2.jpg").scaled(801, 361):
            if condition==2:
                self.pixmap = QImage("location3.jpg").scaled(801, 361)
                self.imageLabel.setPixmap(QPixmap(self.pixmap))
                self.chat.setText("이 방향으로 가면 도착지와 가까워질 것 같다")
            else:
                self.chat.setText("이 방향으로 가면 도착지와 멀어질 것 같다...")

        elif self.pixmap==QImage("location3.jpg").scaled(801, 361):
            if condition==1:
                self.pixmap = QImage("location4.jpg").scaled(801, 361)
                self.imageLabel.setPixmap(QPixmap(self.pixmap))
                self.chat.setText("이 방향으로 가면 도착지와 가까워질 것 같다")
            else:
                self.chat.setText("이 방향으로 가면 도착지와 멀어질 것 같다...")

        elif self.pixmap==QImage("location4.jpg").scaled(801, 361):
            if condition==1:
                self.pixmap = QImage("location5.jpg").scaled(801, 361)
                self.imageLabel.setPixmap(QPixmap(self.pixmap))
                self.chat.setText("이 방향으로 가면 도착지와 가까워질 것 같다")
            else:
                self.chat.setText("이 방향으로 가면 도착지와 멀어질 것 같다...")

        elif self.pixmap==QImage("location5.jpg").scaled(801, 361):
            if condition==1:
                self.pixmap = QImage("location6.jpg").scaled(801, 361)
                self.imageLabel.setPixmap(QPixmap(self.pixmap))
                self.chat.setText("이 방향으로 가면 도착지와 가까워질 것 같다")
            else:
                self.chat.setText("이 방향으로 가면 도착지와 멀어질 것 같다...")

        elif self.pixmap==QImage("location6.jpg").scaled(801, 361):
            if condition==1:
                self.pixmap = QImage("location7.jpg").scaled(801, 361)
                self.imageLabel.setPixmap(QPixmap(self.pixmap))
                self.chat.setText("이 방향으로 가면 도착지와 가까워질 것 같다")
            else:
                self.chat.setText("이 방향으로 가면 도착지와 멀어질 것 같다...")

        elif self.pixmap==QImage("location7.jpg").scaled(801, 361):
            if condition==1:
                self.pixmap = QImage("location8.jpg").scaled(801, 361)
                self.imageLabel.setPixmap(QPixmap(self.pixmap))
                self.chat.setText("이 방향으로 가면 도착지와 가까워질 것 같다")
            else:
                self.chat.setText("이 방향으로 가면 도착지와 멀어질 것 같다...")
        elif self.pixmap==QImage("location8.jpg").scaled(801, 361):
            if condition==3:
                self.finishButton.show()
                self.pixmap = QImage("location9.jpg").scaled(801, 361)
                self.imageLabel.setPixmap(QPixmap(self.pixmap))
                self.chat.setText("목적지에 도착했다!")
                self.finishButton.clicked.connect(self.nextscreen)
            else:
                self.chat.setText("이 방향으로 가면 도착지와 멀어질 것 같다...")

    def nextscreen(self):
        self.hide()
        self.mission=Mission()

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
        pathpath = str(pathlib.Path(__file__).parent.absolute()) + "\\" + "basic_screen.py"
        print(pathpath)
        info = pd.read_csv("../info1.csv")  # , index_col='Date'

        new_info = info.copy()
        new_info['path'] = pathpath
        new_info.to_csv('../info1.csv', index=False,
                        encoding='cp949')

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
