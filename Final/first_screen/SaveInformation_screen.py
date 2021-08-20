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

        self.cancelButton.clicked.connect(self.Home)
        self.data1Start.clicked.connect(self.dataStart)
        self.dataset()

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
