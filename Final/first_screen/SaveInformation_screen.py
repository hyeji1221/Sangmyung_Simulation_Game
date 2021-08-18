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

    def Home(self):
        self.close()  # 창 닫기

    def dataStart(self):
        data = pd.read_csv('../info.csv')
        path = data['path'][0]
        path1 = path+'\lunch_screen.py'
        print(path1)
        subprocess.call(['python', path1])
        #exec(open(str(path1)).read())

    def a(self):
        path1="a"
        args = '"%s" "%s" "%s"' % (sys.executable,  # command
                                   path1,  # argv[0]
                                   os.path.basename(path1))  # argv[1]
        proc = subprocess.run(args)