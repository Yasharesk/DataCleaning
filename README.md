<h2>DataCleaning</h2>
This repo contains basic functionalities required to facilitate recurring tasks. <br>
First leg, currently called "Libs" for no good reason, mostly consists of reading and writing options for Excel files.<br>

There are 3 Functions so far:<br>
<hr>
<h3>get_file_name(fileType="", initDir = os.getcwd()):</h3> <br>
Simply adds a dialog box to the task of reading files. <br>
  Input: A string to specify file type.<br>  
  Returns: A dictionary with:<br>
    <ul>
          <li>"CompleteFile": path+file name</li>
          <li>"FileName": only the file name</li>
          <li>"Path" : only the path</li>
          <li>"FileExtension": only the file extension</li>
    </ul>
<hr>
<h3>write_excel(*df, _index = False, name='Result'): </h3><br>
  A Save As dialog box to choose the directory and the name of the excel file to be written. <br>
  Input: <br>
  <ol>
    <li>multiple data frames (*df).</li>
    <li>Takes a boolean (_index) to indicate if datafram index should be written or not. </li>
    <li>Takes a string (name) to be passed to save as dialog box for inital file name. </li>
  </ol>
  Returns: Full path and name of the file. <br>
<hr>
<h3>break_file_by_size(file, limit): </h3><br>
Breaks a file to chuncks with sizes smaller than limit<br>
  Input: A CompleteFile returned by "GetFileName" and a limit (INT) in MB.<br>
  Returns: A dictionary with:<br>
          <ul>
              <li>"files": count of files created</li>
              <li>"rows": total number of rows created in files (0 if the main file is smaller than limit)</li>
          </ul>
<hr>
<h3>break_file_by_column(path, file, column_name): </h3><br>
Breaks a file down based on unique values of a column, creating a new file for each value<br>
  Input: Path and File name and column name to be used for breaking down.<br>
  
