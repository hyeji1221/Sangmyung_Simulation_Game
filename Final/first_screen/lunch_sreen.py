import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from lunch_location_screen import lunch_location_screen
import pandas as pd
import pathlib

form_class=uic.loadUiType("lunch_screen.ui")[0]

class lunch_screen(QMainWindow, form_class):
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
        self.hillBox.hide()
        self.hillUpMenuBox.hide()
        self.hillMenuOptionBox.hide()
        self.hillDownMenuBox.hide()
        self.hillMenuBox1.hide()
        self.hillMenuBox2.hide()
        self.hillMenuBox3.hide()
        self.hillMenuBox4.hide()
        self.nextButton2.hide()

        self.pixmap = QImage("img/20.PNG").scaled(801, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))


        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)

        self.nextButton.clicked.connect(self.selectStart)

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
        self.nextButton.setStyleSheet("background-color: #DFECFF")
        self.nextButton2.setStyleSheet("background-color: #DFECFF")

        self.hillBox.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.hillDownMenuBox.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.hillMenuBox1.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.hillMenuBox2.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.hillMenuBox3.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.hillMenuBox4.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.hillMenuOptionBox.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.hillUpMenuBox.setStyleSheet("background-color: rgb(255,255,255,150)")
        self.hillButton.setStyleSheet("background-color: #DFECFF")
        self.hillDownButton.setStyleSheet("background-color: #DFECFF")
        self.hillUpButton.setStyleSheet("background-color: #DFECFF")
        self.hillDownMenu1.setStyleSheet("background-color: #DFECFF")
        self.hillDownMenu2.setStyleSheet("background-color: #DFECFF")
        self.hillDownMenu3.setStyleSheet("background-color: #DFECFF")
        self.hillDownMenu4.setStyleSheet("background-color: #DFECFF")
        self.hillMenu1_1.setStyleSheet("background-color: #DFECFF")
        self.hillMenu1_2.setStyleSheet("background-color: #DFECFF")
        self.hillMenu1_3.setStyleSheet("background-color: #DFECFF")
        self.hillMenu1_4.setStyleSheet("background-color: #DFECFF")
        self.hillMenu2_1.setStyleSheet("background-color: #DFECFF")
        self.hillMenu2_2.setStyleSheet("background-color: #DFECFF")
        self.hillMenu2_3.setStyleSheet("background-color: #DFECFF")
        self.hillMenu2_4.setStyleSheet("background-color: #DFECFF")
        self.hillMenu3_1.setStyleSheet("background-color: #DFECFF")
        self.hillMenu3_2.setStyleSheet("background-color: #DFECFF")
        self.hillMenu3_3.setStyleSheet("background-color: #DFECFF")
        self.hillMenu4_1.setStyleSheet("background-color: #DFECFF")
        self.hillMenu4_2.setStyleSheet("background-color: #DFECFF")
        self.hillMenu4_3.setStyleSheet("background-color: #DFECFF")
        self.hillMenu4_4.setStyleSheet("background-color: #DFECFF")
        self.hillMenuOption1.setStyleSheet("background-color: #DFECFF")
        self.hillMenuOption2.setStyleSheet("background-color: #DFECFF")
        self.hillMenuOption3.setStyleSheet("background-color: #DFECFF")
        self.hillMenuOption4.setStyleSheet("background-color: #DFECFF")
        self.hillUpMenu1.setStyleSheet("background-color: #DFECFF")
        self.hillUpMenu2.setStyleSheet("background-color: #DFECFF")
        self.hillUpMenu3.setStyleSheet("background-color: #DFECFF")
        self.hillUpMenu4.setStyleSheet("background-color: #DFECFF")

    def selectStart(self):
        self.hillBox.show()
        self.nextButton.hide()
        self.hillUpButton.clicked.connect(self.selectHillUp)
        self.hillButton.clicked.connect(self.selectHill)
        self.hillDownButton.clicked.connect(self.selectHillDown)

# 언덕 위 / 언덕 / 언덕 아래 선택 -----------------------------------------------------------
    def selectHillUp(self):
        self.hillBox.hide()
        self.hillUpMenuBox.show()
        self.chat.setText("점심 장소는 \"언덕 위에 있는,")
        self.hillUpMenu1.clicked.connect(self.selectHillUpMenu1)
        self.hillUpMenu2.clicked.connect(self.selectHillUpMenu2)
        self.hillUpMenu3.clicked.connect(self.selectHillUpMenu3)
        self.hillUpMenu4.clicked.connect(self.selectHillUpMenu4)

    def selectHill(self):
        self.hillBox.hide()
        self.hillMenuOptionBox.show()
        self.chat.setText("점심 장소는 \"언덕에 있는,")
        self.hillMenuOption1.clicked.connect(self.selectHillMenuOption1)
        self.hillMenuOption2.clicked.connect(self.selectHillMenuOption2)
        self.hillMenuOption3.clicked.connect(self.selectHillMenuOption3)
        self.hillMenuOption4.clicked.connect(self.selectHillMenuOption4)

    def selectHillDown(self):
        self.hillBox.hide()
        self.hillDownMenuBox.show()
        self.chat.setText("점심 장소는 \"언덕 아래에 있는,")
        self.hillDownMenu1.clicked.connect(self.selectHillDownMenu1)
        self.hillDownMenu2.clicked.connect(self.selectHillDownMenu2)
        self.hillDownMenu3.clicked.connect(self.selectHillDownMenu3)
        self.hillDownMenu4.clicked.connect(self.selectHillDownMenu4)

# 언덕 위 / 언덕 / 언덕 아래 선택 후 -> 메뉴 선택 --------------------------------------------
    def selectHillUpMenu1(self):
        self.hillUpMenuBox.hide()
        self.chat.setText("점심 장소는 \"언덕 위에 있는 안다미로!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillUpMenu2(self):
        self.hillUpMenuBox.hide()
        self.chat.setText("점심 장소는 \"언덕 위에 있는 학생식당!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillUpMenu3(self):
        self.hillUpMenuBox.hide()
        self.chat.setText("점심 장소는 \"언덕 위에 있는 블루포트!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillUpMenu4(self):
        self.hillUpMenuBox.hide()
        self.chat.setText("점심 장소는 \"언덕 위에 있는 무아타!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)


    def selectHillMenuOption1(self):
        self.hillMenuOptionBox.hide()
        self.hillMenuBox1.show()
        self.hillMenu1_1.clicked.connect(self.selectHillMenu1_1)
        self.hillMenu1_2.clicked.connect(self.selectHillMenu1_2)
        self.hillMenu1_3.clicked.connect(self.selectHillMenu1_3)
        self.hillMenu1_4.clicked.connect(self.selectHillMenu1_4)
    def selectHillMenuOption2(self):
        self.hillMenuOptionBox.hide()
        self.hillMenuBox2.show()
        self.hillMenu2_1.clicked.connect(self.selectHillMenu2_1)
        self.hillMenu2_2.clicked.connect(self.selectHillMenu2_2)
        self.hillMenu2_3.clicked.connect(self.selectHillMenu2_3)
        self.hillMenu2_4.clicked.connect(self.selectHillMenu2_4)
    def selectHillMenuOption3(self):
        self.hillMenuOptionBox.hide()
        self.hillMenuBox3.show()
        self.hillMenu3_1.clicked.connect(self.selectHillMenu3_1)
        self.hillMenu3_2.clicked.connect(self.selectHillMenu3_2)
        self.hillMenu3_3.clicked.connect(self.selectHillMenu3_3)
    def selectHillMenuOption4(self):
        self.hillMenuOptionBox.hide()
        self.hillMenuBox4.show()
        self.hillMenu4_1.clicked.connect(self.selectHillMenu4_1)
        self.hillMenu4_2.clicked.connect(self.selectHillMenu4_2)
        self.hillMenu4_3.clicked.connect(self.selectHillMenu4_3)
        self.hillMenu4_4.clicked.connect(self.selectHillMenu4_4)

    def selectHillMenu1_1(self):
        self.hillMenuBox1.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 The함께식탁!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu1_2(self):
        self.hillMenuBox1.hide()
        self.nextButton2.show()
        self.chat.setText("점심 장소는 \"언덕에 있는 부대통령 뚝배기!\".")
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu1_3(self):
        self.hillMenuBox1.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 치즈밥있슈!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu1_4(self):
        self.hillMenuBox1.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 청와설렁탕!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)

    def selectHillMenu2_1(self):
        self.hillMenuBox2.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 봉구스밥버거!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu2_2(self):
        self.hillMenuBox2.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 빨간계단!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu2_3(self):
        self.hillMenuBox2.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 윤가네!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu2_4(self):
        self.hillMenuBox2.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 신전떡볶이!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)

    def selectHillMenu3_1(self):
        self.hillMenuBox3.hide()
        self.chat.setText("점심 장소는 \"언덕에 있-는 멜팅그릴!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu3_2(self):
        self.hillMenuBox3.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 샌드앤닭!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu3_3(self):
        self.hillMenuBox3.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 파파존스!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)

    def selectHillMenu4_1(self):
        self.hillMenuBox4.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 GS25!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu4_2(self):
        self.hillMenuBox4.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 아리가또맘마!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu4_3(self):
        self.hillMenuBox4.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 네네치킨!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillMenu4_4(self):
        self.hillMenuBox4.hide()
        self.chat.setText("점심 장소는 \"언덕에 있는 팔선생!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)


    def selectHillDownMenu1(self):
        self.hillDownMenuBox.hide()
        self.chat.setText("점심 장소는 \"언덕 아래에 있는 나성집!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillDownMenu2(self):
        self.hillDownMenuBox.hide()
        self.chat.setText("점심 장소는 \"언덕 아래에 있는 송스키친!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillDownMenu3(self):
        self.hillDownMenuBox.hide()
        self.chat.setText("점심 장소는 \"언덕 아래에 있는 원테이블!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)
    def selectHillDownMenu4(self):
        self.hillDownMenuBox.hide()
        self.chat.setText("점심 장소는 \"언덕 아래에 있는 부암동으로 가자!\".")
        self.nextButton2.show()
        self.nextButton2.clicked.connect(self.lunchLocation)

# 다음 UI화면으로 이동 -------------------------------------------------------------------
    def lunchLocation(self):
        self.hide()
        self.lunch_location_screen = lunch_location_screen()

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
        pathpath = str(pathlib.Path(__file__).parent.absolute()) + "/lunch_sreen.py"
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

