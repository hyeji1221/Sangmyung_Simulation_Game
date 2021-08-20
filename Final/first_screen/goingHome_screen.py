import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import pandas as pd
import pathlib

form_class=uic.loadUiType("going_home_screen.ui")[0]

class goingHome_screen(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.setWindowTitle('SSG')
        self.setWindowIcon(QIcon('smu.jpg'))

        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(242, 245, 253))
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.menuBox.hide()
        self.goHomeMenu.hide()
        self.backButton.hide()

        self.pixmap = QImage("busStop_Image.jpg").scaled(801, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))

        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)

        self.nextButton.clicked.connect(self.selectGoHome)
        self.backButton.clicked.connect(self.goBack)

        # 스타일 변경------------------------------------------------
        self.menu.setStyleSheet("background-color: #DFECFF")
        self.menuBox.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.map.setStyleSheet("background-color: #DFECFF")
        self.mission.setStyleSheet("background-color: #DFECFF")
        self.time.setStyleSheet("background-color: #DFECFF")
        self.save.setStyleSheet("background-color: #DFECFF")
        self.out_btn.setStyleSheet("background-color: #DFECFF")
        self.exit.setStyleSheet("background-color: #DFECFF")
        self.chat.setStyleSheet("background-color: rgb(255,255,255)")
        self.backButton.setStyleSheet("background-color: #DFECFF")
        self.nextButton.setStyleSheet("background-color: #DFECFF")

        self.goHomeMenu.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.bus7016.setStyleSheet("background-color: #DFECFF")
        self.bus13.setStyleSheet("background-color: #DFECFF")
        self.bus08.setStyleSheet("background-color: #DFECFF")
        self.goHillDown.setStyleSheet("background-color: #DFECFF")

    def goBack(self):
        self.selectGoHome()

    def selectGoHome(self):
        self.goHomeMenu.show()
        self.nextButton.hide()
        self.backButton.hide()
        self.pixmap = QImage("busStop_Image.jpg").scaled(801, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.chat.setText("집에 갈 시간이다. 어떻게 갈까?")
        self.bus7016.clicked.connect(self.selectbus7016)
        self.bus13.clicked.connect(self.selectbus13)
        self.bus08.clicked.connect(self.selectbus08)
        self.goHillDown.clicked.connect(self.selecthillDown)

    def selectbus7016(self):
        self.goHomeMenu.hide()
        self.backButton.show()
        self.pixmap = QImage("bus7016_Image.jpg").scaled(801, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.chat.setText("7016 버스를 타고 가자. \n나무데크부터 S관 앞쪽으로 줄을 잘 서자.")

    def selectbus13(self):
        self.goHomeMenu.hide()
        self.backButton.show()
        self.pixmap = QImage("bus13_Image.jpg").scaled(801, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.chat.setText("종로13 버스를 타고 가자. \n종로13 팻말 뒤로 줄을 잘 서자. \n부암동행과 평창동행을 잘 보고 타자!")

    def selectbus08(self):
        self.goHomeMenu.hide()
        self.backButton.show()
        self.pixmap = QImage("bus08_Image.jpg").scaled(801, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.chat.setText("서대문08 버스를 타고 가자.\n서대문08 팻말 뒤로 줄을 잘 서자.")

    def selecthillDown(self):
        self.goHomeMenu.hide()
        self.backButton.show()
        self.pixmap = QImage("hillDown_Image.jpg").scaled(801, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.chat.setText("언덕 아래로 내려가자.")

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
        pathpath = str(pathlib.Path(__file__).parent.absolute()) + "/goingHome_screen.py"
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
