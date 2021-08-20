import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import pandas as pd
import subprocess
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

form_SaveInformationScreen = uic.loadUiType("SaveInformation_screen.ui")[0]

class SaveInformation_screen(QDialog,QWidget, form_SaveInformationScreen):
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

        self.cancelButton.clicked.connect(self.Home)
        self.data1Start.clicked.connect(self.dataStart)
        self.dataset()

        # 스타일 변경------------------------------------------------
        self.cancelButton.setStyleSheet("background-color: #DFECFF")
        self.data1Start.setStyleSheet("background-color: #B6D0F7")
        self.Data1_deleteButton.setStyleSheet("background-color: #DFECFF")
        self.Data1_infoChangeButton.setStyleSheet("background-color: #DFECFF")

        self.Data2_startButton.setStyleSheet("background-color: #B6D0F7")
        self.Data2_deleteButton.setStyleSheet("background-color: #DFECFF")
        self.Data2_infoChangeButton.setStyleSheet("background-color: #DFECFF")

        self.Data3_startButton.setStyleSheet("background-color: #B6D0F7")
        self.Data3_deleteButton.setStyleSheet("background-color: #DFECFF")
        self.Data3_infoChangeButton.setStyleSheet("background-color: #DFECFF")

        self.Data1.setStyleSheet("background-color: rgb(255,255,255)")
        self.Data2.setStyleSheet("background-color: rgb(255,255,255)")
        self.Data3.setStyleSheet("background-color: rgb(255,255,255)")

    def Home(self):
        self.close()  # 창 닫기

    def dataStart(self):
        print("hi")
        data = pd.read_csv('../info1.csv')
        path = data['path'][0]
        print(path)
        subprocess.call(['python', path])

    def dataset(self):
        data = pd.read_csv('../info1.csv')
        name = data['name'][0]
        id = data['id'][0]
        cl = data['cl'][0]
        grade = data['grade'][0]
        print(name, id, cl, grade)
        self.Data1_name.setText(str(name))
        self.Data1_ID.setText(str(id))
        self.Data1_department.setText(str(cl))
        self.Data1_grade.setText(str(grade))
