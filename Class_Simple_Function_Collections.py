# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 08:45:49 2019

@author: 李鹏飞
"""

#%%
import numpy as np
import time
import datetime
import csv
import pandas as pd

#%%
class SimpleFunctionCollections:
    def __init__(self,arg1 = 1, arg2 =2):        
        self.arg1 = arg1
        self.arg2 = arg2
        
    def GetDateTimeStr_P0(self):
        CurrentDateTime = datetime.datetime.now()
        StrCurrentDateTime = CurrentDateTime.strftime("%Y_%m_%d--%H_%M_%S")
        return StrCurrentDateTime
    
    def GetDateTimeStr(self):
        FileNameExt = time.strftime("%m%d%Y_%H-%M-%S")
        return FileNameExt
    
    def Save_Matrix2CSV_with_TimeStamp(self,CSVFileName,Data):
        # =============================================================================
        #  # These can be saved directly, their shape is (m,),not (m,n), iterables are expected,
        #  # you have to have the following operations to make csv save work.   
        #     OneDList = [1,2,3,4,5]    
        #     OneDList_np = np.array(OneDList)   
        #     OneDArray = np.arange(1,10,1) 
        #     ListContainer = []
        #     ListContainer.append(OneDList)#2D list works fine
        #     OneDArrayShapeConversion = OneDArray.reshape((1,len(OneDArray)))
        # =============================================================================       
        TimeStamp = self.GetDateTimeStr()
        PathName = "StoredData/"+CSVFileName+"_"+TimeStamp+".csv"
        with open (PathName,"w",newline="") as CSVFile:
            fwriter = csv.writer(CSVFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            fwriter.writerows(Data)
                        
    def Save_Matrix2CSV_without_TimeStamp(self,CSVFileName,Data):
        PathName = "StoredData/"+CSVFileName+"_"+".csv"                   
        with open (PathName,"w",newline="") as CSVFile:
            fwriter = csv.writer(CSVFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            fwriter.writerows(Data) 

    def ReadCSV(self,CSVFileName):
        PathName = "StoredData/"+CSVFileName+".csv"        
        CSVReadout = []
        with open(PathName, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                CSVReadout.append(row)
                print(row)
        return CSVReadout
    
    def SaveXlsx(self,FileName,Data):
        PathName = "StoredData/"+FileName+".xlsx"
        # Create a Pandas dataframe from some data.
        #df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
        df = pd.DataFrame({'Data': Data})
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(PathName, engine='xlsxwriter')        
        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name='Sheet1')       
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        
    def ReadXlsx(self,FileName):
         PathName = "InputData/"+FileName+".xlsx"
         df = pd.read_excel(PathName,"Sheet1")
         #column_index = df.columns
         data = df.get_values()
         return data
                 
#%%
if __name__ == "__main__":
    #Create a one 1D array
    import numpy as np
    from Class_Simple_Function_Collections import SimpleFunctionCollections
    SFCObj = SimpleFunctionCollections(1,1)
    
    OneDArray = np.arange(1,100,1)
    #OneDArray = [1,2,3,4]
    Data = []
    Data.append(OneDArray)
    Data = np.array(OneDArray)
    #ata = OneDArray    
    #SFCObj.ReadCSV("SaveCSVExample_2019_09_28--18_13_04")
    SFCObj.Save_Matrix2CSV_with_TimeStamp("SaveCSVExample",OneDArray.reshape((1,len(OneDArray))))
    SFCObj.SaveXlsx("excelsavetest",Data)

FileName = "InputExcel"   
PathName = "InputData/"+FileName+".xlsx"
df = pd.read_excel(PathName,"Sheet1")
column_index = df.columns
  
    
    