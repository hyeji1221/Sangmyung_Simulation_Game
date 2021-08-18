import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType("going_univ_screen.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuBox.hide()
        self.goHomeMenu.hide()
        self.backButton.hide()

        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)

        self.nextButton.clicked.connect(self.selectGoHome)
        self.backButton.clicked.connect(self.goBack)
    def selectGoHome(self):
        self.goHomeMenu.show()
        self.nextButton.hide()
        self.backButton.hide()
        self.chat.setText("등교 할 시간이다. 어떻게 갈까?")
        self.bus7016.clicked.connect(self.selectbus7016)
        self.bus13.clicked.connect(self.selectbus13)
        self.bus08.clicked.connect(self.selectbus08)
        self.goHillUp.clicked.connect(self.selecthillDown)

    def goBack(self):
        self.selectGoHome()

    def selectbus7016(self):
        self.goHomeMenu.hide()
        self.backButton.show()
        self.chat.setText("7016 버스를 타고 가자. \n정차 지하철역 : 홍대입구역, 신촌역, 대흥역, 공덕역, 마포역, 남영역, 숙대입구역, 시청역, 경복궁역")

    def selectbus13(self):
        self.goHomeMenu.hide()
        self.backButton.show()
        self.chat.setText("종로13 버스를 타고 가자. \n언덕을 걸어올라오지 않아도 된다.")

    def selectbus08(self):
        self.goHomeMenu.hide()
        self.backButton.show()
        self.chat.setText("서대문08 버스를 타고 가자.\n정차 지하철역 : 홍제역")

    def selecthillDown(self):
        self.goHomeMenu.hide()
        self.backButton.show()
        self.chat.setText("언덕을 걸어 올라가자.")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()