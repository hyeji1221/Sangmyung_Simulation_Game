import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

class WindowClass(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi("mission.ui", self)
        self.menuBox.hide()
        self.missionBox.hide()
        self.mission_show.hide()
        self.imageLabel.hide()
        self.front.hide()
        self.left.hide()
        self.right.hide()
        self.next.hide()
        self.go.hide()
        self.mapclose.hide()
        self.front.setIcon(QtGui.QIcon('front.png'))
        self.front.setIconSize(QtCore.QSize(75, 71))
        self.left.setIcon(QtGui.QIcon('left.png'))
        self.left.setIconSize(QtCore.QSize(75, 71))
        self.right.setIcon(QtGui.QIcon('right.png'))
        self.right.setIconSize(QtCore.QSize(75, 71))
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
        self.imageLabel.show()
        self.pixmap = QImage("map.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.mapclose.show()
        self.mapclose.clicked.connect(self.mapcloseButton)

    def mapcloseButton(self):
        self.imageLabel.hide()
        self.mapclose.hide()

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
        self.next.clicked.connect(self.nexButton)

    def YesButton(self):
        self.missionBox.hide()

    def nexButton(self):
        self.imageLabel.show()
        self.pixmap = QImage("li_1.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.chat.setText("도서관을 찾으러 갑시다.")
        self.next.hide()
        self.front.show()
        self.left.show()
        self.right.show()
        self.front.clicked.connect(self.frontButton)
        self.left.clicked.connect(self.leftButton)
        self.right.clicked.connect(self.rightButton)
    def frontButton(self):
        self.go.hide()
        self.chat.setText("여긴 아닌 것 같다.")
    def leftButton(self):
        self.go.hide()
        self.chat.setText("여긴 아닌 것 같다.")
    def rightButton(self):
        self.chat.setText("도서관으로 가보겠다.")
        self.go.show()
        self.go.clicked.connect(self.GoButton)
    def GoButton(self):
        Mission.widget.setCurrentIndex(Mission.widget.currentIndex() + 1)
    def closeEvent(self, QCloseEvent):
        re = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)

        if re == QMessageBox.Yes:
            print("exit")
            QCloseEvent.accept()
        else:
            print("Not exit")
            QCloseEvent.ignore()


class LibraryClass(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("library.ui", self)
        self.menuBox.hide()
        self.front.setIcon(QtGui.QIcon('front.png'))
        self.front.setIconSize(QtCore.QSize(75, 71))
        self.pixmap = QImage("li_2.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.chat.setText("안으로 들어가자.")
        self.front.clicked.connect(self.frontButton)


    def frontButton(self):
        Mission.widget.setCurrentIndex(Mission.widget.currentIndex() + 1)

class StudentClass(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("student.ui",self)
        self.pixmap = QImage("li_3.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.missionBox.hide()
        self.menuBox.hide()
        self.go.hide()
        self.go_2.hide()
        self.chat.setText("도서관에 입장하기에는 학생증이 필요하다.")
        self.front.hide()
        self.left.hide()
        self.right.hide()
        self.front.setIcon(QtGui.QIcon('front.png'))
        self.front.setIconSize(QtCore.QSize(75, 71))
        self.left.setIcon(QtGui.QIcon('left.png'))
        self.left.setIconSize(QtCore.QSize(75, 71))
        self.right.setIcon(QtGui.QIcon('right.png'))
        self.right.setIconSize(QtCore.QSize(75, 71))
        self.next.clicked.connect(self.NextButton)
        self.OK.clicked.connect(self.OKButton)

    def NextButton(self):
        self.missionBox.show()
    def OKButton(self):
        self.missionBox.hide()
        self.chat.setText("학생증이 있으면 찍고 들어가면 된다.\n이제 프린터기를 찾아보자")
        self.next.hide()
        self.go.show()
        self.go.clicked.connect(self.GoButton)
    def GoButton(self):
        self.pixmap = QImage("li_4.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.front.show()
        self.left.show()
        self.right.show()
        self.front.clicked.connect(self.frontButton)
        self.left.clicked.connect(self.leftButton)
        self.right.clicked.connect(self.rightButton)
    def frontButton(self):
        self.go_2.hide()
        self.chat.setText("여긴 아닌 것 같다.")
    def leftButton(self):
        self.go_2.show()
        self.chat.setText("프린트를 찾으러 간다.")
        self.go_2.clicked.connect(self.Go2Button)
    def rightButton(self):
        self.chat.setText("여긴 아닌 것 같다.")
        self.go_2.hide()
    def Go2Button(self):
        Mission.widget.setCurrentIndex(Mission.widget.currentIndex() + 1)

class PrintClass(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("print.ui",self)
        self.menuBox.hide()
        self.com.hide()
        self.mission_show.hide()
        self.missionBox.hide()
        self.front.hide()
        self.left.hide()
        self.right.hide()
        self.go.hide()
        self.front.setIcon(QtGui.QIcon('front.png'))
        self.front.setIconSize(QtCore.QSize(75, 71))
        self.left.setIcon(QtGui.QIcon('left.png'))
        self.left.setIconSize(QtCore.QSize(75, 71))
        self.right.setIcon(QtGui.QIcon('right.png'))
        self.right.setIconSize(QtCore.QSize(75, 71))
        self.chat.setText("계속 찾아보자.")
        self.next.clicked.connect(self.nextButton)
    def nextButton(self):
        self.pixmap = QImage("li_5.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.front.show()
        self.left.show()
        self.right.show()
        self.front.clicked.connect(self.frontButton)
        self.left.clicked.connect(self.leftButton)
        self.right.clicked.connect(self.rightButton)
    def frontButton(self):
        self.go.show()
        self.chat.setText("다왔다.")
        self.go.clicked.connect(self.GoButton)
    def leftButton(self):
        self.go.hide()
        self.chat.setText("여긴 아닌 것 같다.")
    def rightButton(self):
        self.chat.setText("여긴 아닌 것 같다.")
        self.go.hide()
    def GoButton(self):
        self.pixmap = QImage("li_7.jpg").scaled(651, 361)
        self.imageLabel.setPixmap(QPixmap(self.pixmap))
        self.front.hide()
        self.left.hide()
        self.right.hide()
        self.go.hide()
        self.com.show()
        self.chat.setText("프린터기를 찾았다.")
        self.com.clicked.connect(self.comButton)
    def comButton(self):
        self.mission_show.hide()
        self.missionBox.show()
        self.OK.clicked.connect(self.OKButton)
    def OKButton(self):

        print("다음화면으로")

class Mission(QDialog,QWidget):
    #if __name__ == "__main__":
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    widget = QtWidgets.QStackedWidget()
    myWindow = WindowClass()
    libraryWindow = LibraryClass()
    studentWindow = StudentClass()
    printWindow = PrintClass()

    widget.addWidget(myWindow)
    widget.addWidget(libraryWindow)
    widget.addWidget(studentWindow)
    widget.addWidget(printWindow)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    #app.exec_()