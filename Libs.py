# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:04:11 2019

@author: Yashar.Eskandari
"""
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sys

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
def writeExcel(*df):
    
    root = tk.Tk()
    root.withdraw()
    
    options = {}
    options['defaultextension'] = 'xlsx'
    options['filetypes'] = [('Excel', '.xlsx'), ('All Files', '.*')]
    options['initialdir'] = 'C:/Users/y.eskandari/Downloads/'
    options['initialfile'] = 'Result'
    options['title'] = 'Save As:'
    
    file = filedialog.asksaveasfile(**options).name
    
    try:    
        writer = pd.ExcelWriter(file)
        i = 1   
        for dataframe in df:
            dataframe.reset_index(inplace = True)
            if "index" in dataframe.columns:
                dataframe.drop(['index'], axis = 1, inplace = True)
            dataframe.to_excel(writer, sheet_name ='Sheet-'+str(i), index = False)
            i += 1
        writer.save()
        
    except:
        input("BloodyError! " + str(sys.exc_info()[0]))
