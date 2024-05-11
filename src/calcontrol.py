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
            QLabel,
            QGridLayout,
            QMainWindow,
            QDoubleSpinBox,
            QLineEdit,
            QWidget

)

from layout_colorwidget import Color

import os
import datetime as dt
from loguru import logger
import sys


class calcontrol(QMainWindow):

    def __init__(self):
        super().__init__()
        

        # set title
        self.setWindowTitle("my calories")

        #setup the different widgets
        self.CreateWeightBox()


        self.SetupLayout()


    def CreateWeightBox(self):
        ''' creates a spinner for the weight entry'''

        widget  =  QDoubleSpinBox()
        #widget = QLineEdit()
        widget.setKeyboardTracking(False) # to ensure we only get a final number
        #widget.setMouseTracking(True) # have to hit return


        widget.setMinimum(100.)
        widget.setMaximum(160.)
        widget.setSingleStep(1.)
        widget.editingFinished.connect(self.WeightAction) #ensures we only get one signal with hitting return
        #widget.valueChanged.connect(self.WeightAction)


        self.weight_widget = widget



    def SetupLayout(self):
        '''we use a gridlayout'''
        layout = QGridLayout()
        layout 
        layout.addWidget(self.weight_widget, 0, 0) 
        layout.addWidget(Color("green"), 1, 0) 
        layout.addWidget(Color("blue"), 0, 1)
        layout.addWidget(Color("purple"),1,1)
    
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)


    
    def WeightAction(self):
        print(self.weight_widget.value())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = calcontrol()
    window.show()
    app.exec()