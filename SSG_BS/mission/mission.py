import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType("mission.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuBox.hide()
        self.missionBox.hide()
        self.mission_show.hide()
        self.next.hide()
        self.chat.setText("미션이 도착했습니다. 확인해보세요!")
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
        print("map")

    def missionButton(self):
        self.missionBox.show()
        self.OK.clicked.connect(self.OKButton)
        self.Yes.clicked.connect(self.YesButton)

    def saveButton(self):
        print("save")

    def timeButton(self):
        print("time")

    def menuOff(self):
        self.map.disconnect()
        self.mission.disconnect()
        self.save.disconnect()
        self.exit.disconnect()

    def OKButton(self):
        self.missionBox.hide()
        self.mission_show.show()
        self.next.show()
        self.next.clicked.connect(self.nextButton)

    def YesButton(self):
        self.missionBox.hide()

    def nextButton(self):
        self.chat.setText("도서관을 찾으러 갑시다.")
        self.next.hide()

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