# DataCleaning
This repo contains basic functionalities required to facilitate recurring tasks. 
First leg, currently called "Libs" for no good reason, mostly consists of reading and writing options for Excel files.

There are 3 Functions so far:

GetFileName(title): Simply adds an dialog box to the task of reading excel files. 
  Takes a string to be shown on the title of open dialog box.
  Returns a dictionary with:
    "CompleteFile": path+file name
    "FileName": only the file name
    "Path" : only the path

WriteExcel(*df, _index = False, name='Result'): A Save As dialog box to choose the directory and the name of the excel file to be written. 
  Takes multiple data frames (*df).
  Takes a boolean (_index) to indicate if datafram index should be written or not. 
  Takes a string (name) to be passed to save as dialog box for inital file name. 
  Returns nothing. 
  
break_file_by_size(file, limit): Breaks a file to chuncks with sizes smaller than limit
  Takes a CompleteFile returned by "GetFileName" and a limit (INT) in MB.
  Returns a dictionary with:
    "files": count of files created
    "rows": total number of rows created in files (0 if the main file is smaller than limit)
    
  
