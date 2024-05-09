# Program to keep track of calories
# read in calories and store it in a csv file with date and time
# it uses pandas and QT

import pandas as PD
import datetime as dt
import numpy as np
from pathlib import Path
from loguru import logger

class MyCalories(object):
    
    def __init__(self,filename = None):
        
        self.filename = Path(filename)
        
    def open_file(self): 

        # check if filename exists
        if self.filename.is_file():
            logger.info("filename {} exists".format(self.filename))
            self.my_df = PD.read_csv(self.filename) 
        else:
            
            logger.warning("filename {} does not exist".format(self.filename))
            logger.info("creating file {}".format(self.filename))
            self.CreateFile()


    def CreateFile(self):
        '''create calories file'''
        # the structure will be 
        # date
        # time
        # calories

        self.my_df = PD.DataFrame({'day':[],
                             'time':[],
                              'calories':[] })
        
        # write data frame to file 
        self.my_df.to_csv(self.filename,encoding = 'utf-8',index=False) # the index=False makes sure there is no empty starting column where the index would be
        return

    def CreateEntry(self):
        """adds new entry"""
        self.calories = input("give calories")
        self.calories = int(self.calories)
        now=dt.datetime.now()
        
        self.output = [now.strftime("%d/%m/%Y"),now.strftime("%H:%M:%S")]
        self.my_df.loc[len(self.my_df)]=[self.output[0],self.output[1],self.calories]
        self.my_df.to_csv(self.filename,encoding = 'utf-8',index=False)


    def GetCurrentCount(self):
        """adds up the current calories for today"""
        now=dt.datetime.now()
        self.temp = temp= self.my_df[self.my_df['day'] == now.strftime("%d/%m/%Y")]
        # now add up all of todays calories
        mysum = temp['calories'].sum()
        print("up to now you have eaten {}".format(mysum))
    

        print(temp)

    def ChangeCalories(self):
        """lets you change an entry based on time"""
        pass







if __name__  == "__main__": 
    MyC = MyCalories("/Users/klein/git/qtprogram/data/calories.csv")

    MyC.open_file()
    MyC.CreateEntry()
    MyC.GetCurrentCount()