import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class=uic.loadUiType("basic_screen.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuBox.hide()
        self.optionBox.hide()
        self.optionBox_2.hide()

        self.menu.setCheckable(True)
        self.menu.clicked.connect(self.slot_toggle)

        self.nextButton.clicked.connect(self.selectStart)

    def selectStart(self):
        self.optionBox.show()
        self.nextButton.hide()
        self.hillUpButton.clicked.connect(self.selectHillUp)
        # self.hillButton.clicked.connect()
        # self.hillDownButton.clicked.connect()

    def selectHillUp(self):
        self.optionBox.hide()
        self.optionBox_2.show()
        self.chat.setText("점심 장소는 \"언덕 위에 있는,")
        self.andamiroButton.clicked.connect(self.selectANDAMIRO)

    def selectANDAMIRO(self):
        self.optionBox_2.hide()
        self.chat.setText("점심 장소는 \"언덕 위에 있는 안다미로!\".")


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()