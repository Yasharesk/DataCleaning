<h2>DataCleaning</h2>
This repo contains basic functionalities required to facilitate recurring tasks. <br>
First leg, currently called "Libs" for no good reason, mostly consists of reading and writing options for Excel files.<br>

There are 3 Functions so far:<br>
<hr>
<h3>GetFileName(title):</h3> <br>
Simply adds a dialog box to the task of reading excel files. <br>
  Input: A string to be shown on the title of open dialog box.<br>  
  Returns: A dictionary with:<br>
    <ul>
          <li>"CompleteFile": path+file name</li>
          <li>"FileName": only the file name</li>
          <li>"Path" : only the path</li>
    </ul>
<hr>
<h3>WriteExcel(*df, _index = False, name='Result'): </h3><br>
  A Save As dialog box to choose the directory and the name of the excel file to be written. <br>
  Input: <br>
  <ol>
    <li>multiple data frames (*df).</li>
    <li>Takes a boolean (_index) to indicate if datafram index should be written or not. </li>
    <li>Takes a string (name) to be passed to save as dialog box for inital file name. </li>
  </ol>
  Returns: nothing. <br>
<hr>
<h3>break_file_by_size(file, limit): </h3><br>
Breaks a file to chuncks with sizes smaller than limit<br>
  Input: A CompleteFile returned by "GetFileName" and a limit (INT) in MB.<br>
  Returns: A dictionary with:<br>
          <ul>
              <li>"files": count of files created</li>
              <li>"rows": total number of rows created in files (0 if the main file is smaller than limit)</li>
          </ul>
