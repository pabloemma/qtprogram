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
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (
            QApplication,
            QLabel,
            QGridLayout,
            QMainWindow,
            QDoubleSpinBox,
            QLineEdit,
            QFileDialog,
            QWidget

)

from layout_colorwidget import Color
import MyCalories_qt as MyC

import os
import datetime as dt
from loguru import logger
import sys




class calcontrol(QMainWindow):

    def __init__(self):
        super().__init__()
        

        #instantiate the mycalories

        self.GetFilename()
 
 
        # set title
        self.setWindowTitle("my calories")

        #setup the different widgets
        self.CreateWeightBox() # interface for weight entry
        self.CreateCaloriesBox()


        self.SetupLayout()

    def GetFilename(self):
        """ get the name for the calory file"""

        self.file_name,filter = QFileDialog.getOpenFileName(self,"open caloryfile","/Users/kelin/git/qtprogram/data")
        #instantiate calories
        
        self.MyCal = MyC.MyCalories_qt(filename = self.file_name)

 
        # now read the data
        self.MyCal.open_file()





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

        # create the label for weight
        self.weight_label = QLabel("Enter a weight between {}  and {}" .format(100.,200.))

    def CreateCaloriesBox(self):
        ''' creates a spinner for the weight entry'''

        widget  =  QDoubleSpinBox()
        #widget = QLineEdit()
        widget.setKeyboardTracking(False) # to ensure we only get a final number

        widget.setSingleStep(1.)
        widget.editingFinished.connect(self.CaloriesAction) #ensures we only get one signal with hitting return
 

        self.calories_widget = widget
        self.calories_label = QLabel("Enter your calories ")




    def SetupLayout(self):
        '''we use a gridlayout'''
        layout = QGridLayout()
        layout 
        layout.addWidget(self.weight_label, 0, 0) 
        layout.addWidget(self.weight_widget, 1, 0) 
        layout.addWidget(self.calories_label, 0, 1) 
        layout.addWidget(self.calories_widget,1,1) 
        #layout.addWidget(Color("blue"), 1, 0)
        #layout.addWidget(Color("purple"),1,1)
    
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)


    
    def WeightAction(self):
        if(self.weight_widget.value() == 100.):
            print("you haven't entered anything")

        else:
            print(self.weight_widget.value())


    def CaloriesAction(self):
        if(self.calories_widget.value() == 0.):
            print("seriously, no calories?")
        else:
            print(self.calories_widget.value())

    def ShowData(self):
        ''' shows the calories table'''

        # get the pandas frame from mycalories_qt
        my_df = self.MyCal.my_df
        print(my_df)
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = calcontrol()
    window.ShowData()
    window.show()
    app.exec()