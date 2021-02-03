<h2>DataCleaning</h2>
This repo contains basic functionalities required to facilitate recurring tasks. 
First leg, currently called "Libs" for no good reason, mostly consists of reading and writing options for Excel files.

There are 3 Functions so far:

GetFileName(title): </br>
Simply adds a dialog box to the task of reading excel files. </br>
  Input: A string to be shown on the title of open dialog box.</br>
  Returns: A dictionary with:</br>
          "CompleteFile": path+file name</br>
          "FileName": only the file name</br>
          "Path" : only the path</br>
</br>
WriteExcel(*df, _index = False, name='Result'): A Save As dialog box to choose the directory and the name of the excel file to be written. </br>
  Input: 
    1.multiple data frames (*df).</br>
    2.Takes a boolean (_index) to indicate if datafram index should be written or not. </br>
    3.Takes a string (name) to be passed to save as dialog box for inital file name. </br>
  Returns: nothing. </br>
</br>
break_file_by_size(file, limit): Breaks a file to chuncks with sizes smaller than limit</br>
  Input: A CompleteFile returned by "GetFileName" and a limit (INT) in MB.</br>
  Returns: A dictionary with:</br>
              "files": count of files created</br>
              "rows": total number of rows created in files (0 if the main file is smaller than limit)</br>
