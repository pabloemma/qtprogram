# Program to keep track of calories
# read in calories and store it in a csv file with date and time
# it uses pandas and QT


import pandas as PD
import datetime as dt 
import numpy as np
from pathlib import Path
from loguru import logger

class MyCalories_qt(object):
    
    def __init__(self,filename = None):
        
        self.filename = Path(filename)
        PD.options.mode.chained_assignment = None # remove warings when editing the pandas

        # before we do anything give your weight
        #self.EnterWeight()
        
    def open_file(self): 

        # check if filename exists
        if self.filename.is_file():
            logger.info("filename {} exists".format(self.filename))
            self.my_df = PD.read_csv(self.filename) 
        else:
            
            logger.warning("filename {} does not exist".format(self.filename))
            logger.info("creating file {}".format(self.filename))
            self.CreateFile()

        return

    def CreateFile(self):
        '''create calories file'''
        # the structure will be 
        # date
        # time
        # calories

        self.my_df = PD.DataFrame({'day':[],
                             'time':[],
                              'calories':[],
                               'weight':[] })
        
        # write data frame to file 
        self.SavePandaFile() # the index=False makes sure there is no empty starting column where the index would be
        return

    def EnterCalories(self):
        """adds new entry"""
        self.calories = input("give calories")
        self.calories = int(self.calories)
        now=dt.datetime.now()
        #self.weight=float(0)
        self.output = [now.strftime("%d/%m/%Y"),now.strftime("%H:%M:%S")]
        if 'self.weight' not in globals():
            self.EnterWeight()
            self.my_df.loc[len(self.my_df)]=[self.output[0],self.output[1],self.calories,self.weight]
        else:
            self.my_df.loc[len(self.my_df)]=[self.output[0],self.output[1],self.calories,self.weight]
           
        
        
        self.SavePandaFile()

    def EnterWeight(self):
        self.weight = float(input("what is your weight ?  "))
        return
    
    def SavePandaFile(self):
    
        self.my_df.to_csv(self.filename,encoding = 'utf-8',index=False)
        return
    
    def GetMorning(self):
        """ get the morning calories"""

        index = PD.DatetimeIndex(self.my_df['time'])
        morning = self.my_df.iloc[index.indexer_between_time('00:00','12:00')]
        #morning = self.my_df.between_time('17:00','17:11',inclusive ='both')
        print("you have eaten {} calories in the morning".format(self.GetSum(morning)))
        return

    def GetAfternoon(self):
        """ get the morning calories"""

        index = PD.DatetimeIndex(self.my_df['time'])
        afternoon = self.my_df.iloc[index.indexer_between_time('12:01','18:00')]
        #morning = self.my_df.between_time('17:00','17:11',inclusive ='both')
        print("you have eaten {} calories in the afternoo".format(self.GetSum(afternoon)))
 
        print(afternoon)
        return
    
    def GetEvening(self):
        """ get the morning calories"""

        index = PD.DatetimeIndex(self.my_df['time'])
        evening = self.my_df.iloc[index.indexer_between_time('18:01','23:59')]
        #morning = self.my_df.between_time('17:00','17:11',inclusive ='both')
        print("you have eaten {} calories in the morning".format(self.GetSum(evening)))
       
        return
       
    def GetWeight(self):
        '''check if weight is already in csv file'''
        now=dt.datetime.now()
        temp= self.my_df[self.my_df['day'] == now.strftime("%d/%m/%Y")]
        try:
            if temp['weight'].iloc[0] == 0. :
                self.weight =  self.EnterWeight()
            else:
                print(temp['weight'].iloc[0]) # get first entry, requires that first entry has weight
        except:
            print("no entries found")
        
        # now check for weight:


        
    
    def GetSum(self,mydata):
        """determines the sum of the calories"""
        return mydata['calories'].sum()

    def GetCurrentCount(self):
        """adds up the current calories for today"""
        now=dt.datetime.now()
        self.temp = temp= self.my_df[self.my_df['day'] == now.strftime("%d/%m/%Y")]
        # now add up all of todays calories
        #mysum = temp['calories'].sum()
        print("up to now you have eaten {} calories".format(self.GetSum(temp)))
    

        print(temp)

    def ChangeCalories(self):
        """lets you change an entry based on time"""
        print (self.my_df)
        myindex, mycal = input('give index of entry and value; separated by comma').split(',')
        mycal = int(mycal)
        myindex = int(myindex)
        self.my_df['calories'].iloc[myindex]= mycal
        # give new updated count
        self.GetCurrentCount()

 
        # now we write the new data base back
        self.SavePandaFile()


        pass







if __name__  == "__main__": 
    MyC = MyCalories("/Users/klein/git/qtprogram/data/calories.csv")

    MyC.open_file()
    #MyC.GetMorning()
    #MyC.EnterCalories()
    #MyC.GetCurrentCount()
    #MyC.ChangeCalories()
    MyC.GetWeight()