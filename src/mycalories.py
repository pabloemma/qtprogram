# Program to keep track of calories
# read in calories and store it in a csv file with date and time
# it uses pandas and QT

import pandas as PD
import datetime as dt
import numpy as np
from pathlib import Path
import loguru

class MyCalories(object):
    
    def __init__(self,filename = None):
        
        self.filename = Path(filename)
        
    def open_file(self): 

        # check if filename exists
        if self.filename.is_file():
            print("filename {} exists".format(self.filename))
        else:
            print("filename {} does not exist".format(self.filename))

if __name__  == "__main__": 
    MyC = MyCalories("calories.csv")

    MyC.open_file()