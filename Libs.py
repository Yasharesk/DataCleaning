# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:04:11 2019

@author: Yashar.Eskandari
"""
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sys
import os
#class Files:

#______________________________________________________________________________________________________________________    
#
#This is an Open Dialog box 
#You can Specify the name of file type on the window title as a String or leave it empty
#______________________________________________________________________________________________________________________    
#
def getFileName(fileType = "", initDir ='C:/Users/y.eskandari/Downloads/'):
    
    root = tk.Tk()
    root.withdraw()
    
    FileName = filedialog.askopenfilename(initialdir = initDir, 
                                          filetypes = (("Excel File", "*.xlsx"),("All Files","*.*")), 
                                          title = 'Choose the '+ fileType + ' file:')
    return {"CompleteFile":FileName, "Path": FileName.rsplit('/',1)[0] + "/", "FileName":FileName.rsplit('/',1)[1]}
#______________________________________________________________________________________________________________________
#    
#This is to write pnadas data frame to Excel file
#The path is chosen by dialog and a name is given
#The defualt file type is excel
#______________________________________________________________________________________________________________________
#
def writeExcel(*df, _index = False, name = 'Result'):
    
    root = tk.Tk()
    root.withdraw()
    
    options = {}
    options['defaultextension'] = 'xlsx'
    options['filetypes'] = [('Excel', '.xlsx'), ('All Files', '.*')]
    options['initialdir'] = 'C:/Users/y.eskandari/Downloads/'
    options['initialfile'] = name
    options['title'] = 'Save As:'
    
    file = filedialog.asksaveasfile(**options).name
    
    try:    
        writer = pd.ExcelWriter(file)
        i = 1   
        for dataframe in df:
            dataframe.reset_index(inplace = True)
            if "index" in dataframe.columns:
                dataframe.drop(['index'], axis = 1, inplace = True)
            dataframe.to_excel(writer, sheet_name ='Sheet-'+str(i), index = _index)
            i += 1
        writer.save()
        
    except:
        input("BloodyError! " + str(sys.exc_info()[0]))
    return file
#______________________________________________________________________________________________________________________
#    
#This function will check a file's size and compare it to a limit
#The limit is taken in MB
#If the file is larger than limit, it will break it to as many files 
#as required to keep the sizes smaller than limit
#Takes the file as an "getFileName" dict, returns a dict with 'files' and 
#'rows'. If no change is done the rows will be 0
#______________________________________________________________________________________________________________________
#
def break_file_by_size(file, limit):
    limit = limit*1024*1024
    size = os.path.getsize(file["CompleteFile"])
    if size > limit:
        df = pd.read_excel(file["CompleteFile"])
        batch_count = int(size/limit) + 1
        row_count = int(len(df)/batch_count) + 1
        row_counter = 0
        file_counter = 0
        for i in range(batch_count):
            dftemp = df.iloc[(row_count*i):min(row_count*(i+1), len(df)), :]
            writer = pd.ExcelWriter(file["Path"]+str(i)+'_'+file["FileName"])
            dftemp.to_excel(writer, index = False)
            writer.save()
            row_counter = row_counter + len(dftemp)
            file_counter = file_counter + 1
        return {'files':file_counter, 'rows':row_counter}
    else:
        return {'files': 1, 'rows': 0}