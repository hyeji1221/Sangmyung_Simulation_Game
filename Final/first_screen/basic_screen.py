import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from lunch_sreen import lunch_screen
import numpy as np
import pandas as pd
import pathlib

form_class=uic.loadUiType("basic_screen.ui")[0]

class basic_screen(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.show_image()
        self.show()

        self.setWindowTitle('SSG')
        self.setWindowIcon(QIcon('smu.jpg'))

        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(242, 245, 253))
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.menuBox.hide()
        self.textEdit.hide()
        self.finishBtn.hide()
        self.downBtn.hide()
        self.upBtn.hide()
        self.rightBtn.hide()
        self.leftBtn.hide()
        self.start()
        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)
        self.upBtn.clicked.connect(self.up_btn)
        self.downBtn.clicked.connect(self.down_btn)
        self.rightBtn.clicked.connect(self.up_btn)
        self.leftBtn.clicked.connect(self.down_btn)
        self.goBtn.clicked.connect(self.go_btn)
        self.finishBtn.clicked.connect(self.finish_btn)
        self.number = 0

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
        self.upBtn.setStyleSheet("background-color: #DFECFF")
        self.leftBtn.setStyleSheet("background-color: #DFECFF")
        self.rightBtn.setStyleSheet("background-color: #DFECFF")
        self.downBtn.setStyleSheet("background-color: #DFECFF")
        self.goBtn.setStyleSheet("background-color: #DFECFF")
        self.finishBtn.setStyleSheet("background-color: #DFECFF")


    def start(self):
        self.chat.setText("    강의실을 입력하세요.")
        self.number = 0
        self.textEdit.show()
        self.finishBtn.hide()
        self.goBtn.show()

    def go_btn(self):
        self.textEdit.hide()
        self.chat.setText("")
        self.goBtn.hide()
        pixmap = QPixmap('img/1.PNG')
        self.img_label.setPixmap(pixmap.scaled(self.img_label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.show()
        self.downBtn.show()
        self.upBtn.show()

    def finish_btn(self): # 종료버튼 클릭
        self.start()



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
        pathpath = str(pathlib.Path(__file__).parent.absolute())+"\\"+"basic_screen.py"
        print(pathpath)
        info = pd.read_csv("../info1.csv") # , index_col='Date'

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
        self.exit.disconnect()

    def upShow(self):
        self.upBtn.show()
        self.downBtn.show()
        self.rightBtn.hide()
        self.leftBtn.hide()

    def upHide(self):
        self.rightBtn.show()
        self.leftBtn.show()
        self.upBtn.hide()
        self.downBtn.hide()

    def closeEvent(self, QCloseEvent):
        re = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)

        if re == QMessageBox.Yes:
            print("exit")
            QCloseEvent.accept()
        else:
            print("Not exit")
            QCloseEvent.ignore()

    def condition(self):
        if (self.number == 20):
            self.chat.setText("    도착했다!\n    수업을 들으러 가볼까?")
            self.upBtn.hide()
            self.downBtn.hide()
            self.finishBtn.show()
            self.finishBtn.clicked.connect(self.finishBtnButton)
        elif (self.number == 1):
            self.chat.setText("    강의실로 가자!")
            self.upShow()

        elif (self.number == 7):
            self.chat.setText("    에스컬레이터를 타자!")
            self.upShow()

        elif (self.number == 14 or self.number == 15):
            self.chat.setText("    오른쪽으로 가자!")
            self.upHide()
        elif (self.number == 18):
            self.chat.setText("    왼쪽으로 가자!")
            self.upHide()
            self.rightBtn.clicked.connect(self.down_btn)
            self.leftBtn.clicked.connect(self.up_btn)

        elif (self.number == 16):
            self.upShow()
            self.chat.setText("    엘리베이터를 타자!\n    1층으로 가기!")
        else:
            self.upShow()
            self.chat.setText("    직진하자!")

    def finishBtnButton(self):
        self.hide()
        self.lunch_screen = lunch_screen()

    def up_btn(self):
        self.number += 1
        print(self.number)
        root = 'img/' + str(self.number) +'.PNG'
        pixmap = QPixmap(root)
        self.img_label.setPixmap(pixmap.scaled(self.img_label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.show()
        self.condition()


    def down_btn(self):
        self.number -= 1
        print(self.number)
        root = 'img/' + str(self.number) + '.PNG'
        pixmap = QPixmap(root)
        self.img_label.setPixmap(pixmap.scaled(self.img_label.size(), QtCore.Qt.IgnoreAspectRatio))
        self.show()
        self.condition()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = basic_screen()
    myWindow.show()
    app.exec_()