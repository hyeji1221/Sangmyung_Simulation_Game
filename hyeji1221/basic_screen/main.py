import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

form_class = uic.loadUiType("first.ui")[0]
form_class1 = uic.loadUiType("menu.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QDialog) :
    def __init__(self) :
        super().__init__()
        #self.setupUi(self.form_class)

        loadUi("first.ui", self)
        self.btn1.clicked.connect(self.button1Function)
        self.btn2.clicked.connect(self.button2Function)
        #self.btn3.clicked.connect(self.instance().quit)

    def button1Function(self) :
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print("btn_1 Clicked")

    def button2Function(self) :
        print("btn_2 Clicked")
        #self.setupUi()

class MenuClass(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("menu.ui", self)
        self.menu_screen.hide()
        self.chat.hide()
        self.menu_btn.clicked.connect(self.buttonFunction)
        self.save_btn.clicked.connect(self.saveFunction)
        self.map_btn.clicked.connect(self.mapFunction)
        self.out_btn.clicked.connect(self.outFunction)
        self.quest_btn.clicked.connect(self.questFunction)
        self.exit_btn.clicked.connect(self.exitFunction)

    def buttonFunction(self):
        self.menu_screen.show()
        self.chat.show()
    def saveFunction(self):
        print("save")

    def mapFunction(self):
        print("map")

    def questFunction(self):
        print("quest")

    def outFunction(self):
        self.menu_screen.hide()
        self.chat.hide()

    def exitFunction(self):

        widget.setCurrentIndex(widget.currentIndex() - 1)



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    widget = QtWidgets.QStackedWidget()
    myWindow = WindowClass()
    menuWindow = MenuClass()

    widget.addWidget(myWindow)
    widget.addWidget(menuWindow)

    #프로그램 화면을 보여주는 코드
    widget.setFixedHeight(500)
    widget.setFixedWidth(540)

    widget.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()