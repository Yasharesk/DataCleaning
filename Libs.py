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


def get_file_name(fileType: str = "", initDir: str = os.getcwd()) -> dict:
    '''
    A simple open dialogue box to choose a file and get name and info.

    Parameters
    ----------
    fileType : str, optional
        Extention of the file on the window title. The default is "".
    initDir : str, optional
        The initial directory to be shown. The default is os.getcwd().

    Returns
    -------
    dict
        DESCRIPTION.

    '''
    root = tk.Tk()
    root.withdraw()

    if fileType == "":
        fileTypes = (("All Files", "*.*"), ("Excel File", "*.xlsx"))
        title = 'Choose a file to open:'
    else:
        fileTypes = ((f'User Specified', f'*.{fileType}'),
                     ('Excel File', '*.xlsx'), ('All Files', '*.*'))
        title = f'Choose a {fileType} file to open:'

    FileName = filedialog.askopenfilename(
        initialdir=initDir, filetypes=fileTypes, title=title)

    return {"CompleteFile": FileName,
            "Path": FileName.rsplit('/', 1)[0] + "/",
            "FileName": FileName.rsplit('/', 1)[1],
            "FileExtension": FileName.rsplit('.', 1)[-1]}


def write_excel(*df, _index=False, name='Result') -> str:
    '''
    Simple Save As dialogue box to write pandas data frames to Excel file.
    Easier control on finding the path, and giving the file name.
    Multiple dataframes will be written to different sheets of the file.

    Parameters
    ----------
    *df : pandas.DataFrame
        Dataframes to be written to excel file.
    _index : Bool, optional
        Indicates if the index should be written to the file.
        The default is False.
    name : str, optional
        An initial name to fill the dialogue box. The default is 'Result'.

    Returns
    -------
    file : str
        Full path to the selected file name.

    '''

    root = tk.Tk()
    root.withdraw()

    options = {}
    options['defaultextension'] = 'xlsx'
    options['filetypes'] = [('Excel', '.xlsx'), ('All Files', '.*')]
    options['initialdir'] = os.getcwd()
    options['initialfile'] = name
    options['title'] = 'Save As:'

    file = filedialog.asksaveasfile(**options).name

    try:
        writer = pd.ExcelWriter(file)
        for i, dataframe in enumerate(df):
            dataframe.reset_index(inplace=True)
            if 'index' in dataframe.columns:
                dataframe.drop(['index'], axis=1, inplace=True)
            dataframe.to_excel(writer,
                               sheet_name='Sheet-' + str(i),
                               index=_index)
        writer.save()

    except(Exception):
        input('There was an error! ' + str(sys.exc_info()[0]))
    return file


def break_file_by_size(file, limit) -> dict:
    '''
    Check a file's size and compare it to specified limit.
    The limit is given in MB.
    If the file is larger than the limit, it will break it to as many files
    as necessary to keep the sizes smaller than the limit.

    Parameters
    ----------
    file : get_file_name()
        Information of the file selected by getFileName function.
    limit : int
        Size limit in Mega Bytes.

    Returns
    -------
    dict
        Dictionary containing the number of files generated and
        number of rows processed and converted to those files.

    '''
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
            dftemp.to_excel(writer, index=False)
            writer.save()
            row_counter = row_counter + len(dftemp)
            file_counter = file_counter + 1
        return {'files': file_counter, 'rows': row_counter}
    else:
        return {'files': 1, 'rows': 0}
