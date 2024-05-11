# calcontrol
# a. klein may24
# uses mycalories and QT to control claory intake
#calcontrol is the gui to mycalories
'''
The main control should have a tab for input calories, weight
and some tab for outputting the quantities
I will start with an easy example, four widgets in one window
'''

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
            QApplication,
            QComboBox,
            QMainWindow

)
import os
import datetime as dt
from loguru import logger
import sys


class calcontrol(QMainWindow):

    def __init__(self):
        super().__init__()
        

        
        self.setWindowTitle("my calories")

        self.widget = QComboBox()
        self.widget.addItems(["weight","calories"])
        self.widget.currentIndexChanged.connect(self.index_changed)
        self.widget.currentTextChanged.connect(self.index_changed)

        self.setCentralWidget(self.widget)
    
    def index_changed(self,i):
        print(i)
        return

    def text_changed(self,s):
        print(s)
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = calcontrol()
    window.show()
    app.exec()