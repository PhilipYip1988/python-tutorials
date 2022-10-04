# Working with Files and Directories

## Reading and Writing to Files

### Reading Files

The Documents folder can be opened in file explorer:

![img_000.png](./images/img_000.png)

An interactive notebook file can be created in the Documents folder and opened with JupyterLab:

![img_001.png](./images/img_001.png)

A new text file can be created in the file explorer:

![img_002.png](./images/img_002.png)

![img_003.png](./images/img_003.png)

Some text can be added into this text file:

![img_004.png](./images/img_004.png)

The text file can be opened in Python using the following syntax:

```
file_object = open(file="text_file.txt", mode="r")
```

![img_005.png](./images/img_005.png)

Because ```text_file.txt``` is in the same folder as ```file_os_module.ipynb```. The file can be expressed implicitly without explicitly specifying the full path.

The mode can be ```"r"``` for read, ```"w"``` for write and ```"a"``` for append.

The file_object has a number of attributes and methods which can be accessed by typing in the file object names followed by a dot ```.``` and tab ```↹```:

![img_006.png](./images/img_006.png)

![img_007.png](./images/img_007.png)

![img_008.png](./images/img_008.png)

The ```close``` method is used to close the file and should always be used after working with the file.

The ```with``` keyword is typically used to open the file over the duration of a code block. 

```
with open(file="text_file.txt", mode="r") as file_object:
    file_object.close()
    
    
```

![img_009.png](./images/img_009.png)

In the code block above, the final line of the code block explicitly closes the file object. However since the keyword ```with``` is used, the file will automatically close the file when the code block ends. The file will be closed after this code block executes: 

```
with open(file="text_file.txt", mode="r") as file_object:
    pass
    
    
```

![img_010.png](./images/img_010.png)

For clarity, the close method will explicitly be stated at the bottom of a code block. The file contents can be read using the method ```read```.

```
with open(file="text_file.txt", mode="r") as file_object:
    file_contents = file_object.read()
    print(file_contents)
    file_object.close()
    
    
```

![img_011.png](./images/img_011.png)

The object ```file_contents``` can be explored on the variable explorer and is a string of length 193 characters:

![img_015.png](./images/img_015.png)

The read method has a positional input argument size. This can be used to specify the upper size of characters to read from a file.

![img_012.png](./images/img_012.png)

This can be set to 10 for example:

```
with open(file="text_file.txt", mode="r") as file_object:
    file_contents = file_object.read(10)
    print(file_contents)
    file_object.close()
    
    
```    

![img_013.png](./images/img_013.png)

The object ```file_contents``` can be explored on the variable explorer and is a string of length 10:

![img_014.png](./images/img_014.png)

Before this code block closes the file, the cursor of the text file can be visualised at the position 10:

![img_016.png](./images/img_016.png)

The code can be updated to read two 10 character strings from the file.


```
with open(file="text_file.txt", mode="r") as file_object:
    file_contents = file_object.read(10)
    print(file_contents)
    file_contents2 = file_object.read(10)
    print(file_contents2)
    file_object.close()
    
    
```    

![img_017.png](./images/img_017.png)

Now ```file_contents``` and ```file_contents2``` display on the variable explorer:

![img_018.png](./images/img_018.png)

Before this code block closes the file, the cursor of the text file can be visualised at the position 20:

![img_019.png](./images/img_019.png)

The function ```seek``` can be used to change the offset position of the cursor. The starting position for example can be set at position ```25```

```
with open(file="text_file.txt", mode="r") as file_object:
    file_object.seek(25)
    file_contents = file_object.read(30)
    print(file_contents)
    file_object.close()
    
    
```    

![img_020.png](./images/img_020.png)

![img_021.png](./images/img_021.png)

![img_022.png](./images/img_022.png)

Notice that ```file_contents``` is a multi-line string.

There is an associated readline method which can be used read a single line, including the newline character at the end of the line. 

```
with open(file="text_file.txt", mode="r") as file_object:
    file_contents = file_object.readline()
    print(file_contents, end="*")
    file_object.close()
    
    
```

The presence of the newline character can be seen by changing the ```end``` keyword input argument in the ```print``` function to ```*```. The ```*``` starts of a newline indicating the last character in the string ```file_contents``` is the newline.

![img_023.png](./images/img_023.png)

This newline can be seen in the variable explorer, if examined with care:

![img_024.png](./images/img_024.png)

Before this code block closes the file, the cursor of the text file can be visualised at the start of the second line:

![img_025.png](./images/img_025.png)


Readlines can be used to read multiple lines into an output list.

```
with open(file="text_file.txt", mode="r") as file_object:
    file_contents = file_object.readlines()
    print(file_contents)
    file_object.close()


```

![img_026.png](./images/img_026.png)

![img_027.png](./images/img_027.png)

### Creating Files

A new blank file can be created by use fo a new file name ```"text_file2.txt"``` and setting the mode to ```"w"``` for write access.

```
with open(file="text_file2.txt", mode="w") as file_object:
    file_object.close()
    
    
```

![img_031.png](./images/img_031.png)

The blank file can be opened in file explorer:

![img_028.png](./images/img_028.png)

The blank contents can be seen in notepad:

![img_029.png](./images/img_029.png)

Some text can be added:

![img_030.png](./images/img_030.png)

Using write mode when an existing file is present, will overwrite the file:

```
with open(file="text_file2.txt", mode="w") as file_object:
    file_object.close()
    
    
```

![img_032.png](./images/img_032.png)

![img_033.png](./images/img_033.png)

### Appending Files

If some text is added to the file, in notepad again.

![img_034.png](./images/img_034.png)

The third mode of operation append can be explored. In the append mode, the file will be opened with write access, however the offset position of the cursor will be at the end of the file.

The method ```writelines``` can be used to write a list of strings to a file. The associated method ```write``` can be used to write a single string to a file. These mehtods follow similar behaviour to their read counterparts:

```
new_file_contents = ["Mary, Mary, quite contrary,\n",
                     "How does your garden grow?\n",
                     "With silver bells, and cockle shells,\n",
                     "And pretty maids all in a row."]
                     
with open(file="text_file2.txt", mode="a") as file_object:
    file_object.writelines(new_file_contents)
    file_object.close()
    
```    

![img_035.png](./images/img_035.png)

Notice the updated contents of the file. The cursor started immediately after ```Hello``` and there was no new line or space so, the first sentance continued immediately after Hello: 

![img_036.png](./images/img_036.png)

## Working with Directories

In Python and Linux, a folder is known as a directory.

In Windows File Explorer, a directory is known as a folder.

### os Module

The inbuilt operating system module ```os``` is used for file and folder manipulation. Although this module is inbuilt into Python, it must be imported before use:

```
import os
```

![img_037.png](./images/img_037.png)

A large number of objects can be called from the ```os``` by typing in ```os``` followed by a dot ```.``` and tab ```↹```.

### Current Working Directory

The method getcwd is an abbreviation for get current working directory:

```
os.getcwd()
```

![img_038.png](./images/img_038.png)

By default, this is the folder or directory of the currently executed script (.py file) or interactive notebook (.ipynb file). This folder can be viewed in Windows Explorer to visualise its contents:

![img_039.png](./images/img_039.png)

### List Directory

The method ```listdir``` will list all items in the current working directory:

```
os.listdir()
```

![img_040.png](./images/img_040.png)

This method has a keyword input argument path that can be used to select a different location. If unspecified, path defaults to the current working directory.

![img_041.png](./images/img_041.png)

The path searched for will also be in reference to the current directory unless explicitly specified. The path can be changed to Downloads by going up a level ```..``` to get to ```$UserProfile$``` and then to Downloads using:

```
os.listdir(r"../Downloads")
```

![img_042.png](./images/img_042.png)

![img_043.png](./images/img_043.png)

### Environmental Variables

The ```$UserProfile$``` is typically found in the ```C:\Users``` folder within file explorer.

![img_044.png](./images/img_044.png)

![img_045.png](./images/img_045.png)

This folder is defined by what is known as an Operating System wide Environmental Variable. These are listed within essentially a dictionary.

![img_046.png](./images/img_046.png)

![img_047.png](./images/img_047.png)

On Windows, inputting ```%UserProfile$"``` into the file explorer changes the directory of the file explorer to the user profile:

![img_048.png](./images/img_048.png)

The location can be accessed as a string from this dictionary-like object using the key ```"USERPROFILE"```:

```
os.environ["USERPROFILE"]
```

![img_049.png](./images/img_049.png)

On Linux, the equivalent key is called ```"HOME"```.

### path Methods

Concatenation of file paths can quickly get messy due to the multiple ```\``` in the file path.

```
os.environ["USERPROFILE"] + "Documents"
```

```
os.environ["USERPROFILE"] + r"\Documents"
```

![img_050.png](./images/img_050.png)

As a consequence a collection of operations relating to the file path are available under the ```os``` attribute ```path```:

![img_051.png](./images/img_051.png)

For example the function ```join``` can be used to join the os environmental variable, Documents folder and text file within the Documents folder:

```
os.path.join(os.environ["USERPROFILE"], "Documents")
os.path.join(os.environ["USERPROFILE"], "Documents", "text_file.txt")
```

![img_052.png](./images/img_052.png)

The file path above can be assigned to a variable ```file_path```:

```
file_path = os.path.join(os.environ["USERPROFILE"], 
                         "Documents", 
                         "text_file.txt")
```

```
file_path
```

![img_053.png](./images/img_053.png)

The os path method ```exists``` will check if the physical file path exists, returning a boolean value. In this case the ```file_path``` exists:

```
os.path.exists(path=file_path)
```

![img_054.png](./images/img_054.png)

The os path method ```isfile``` will check if the file path corresponds to a file, returning a boolean value. In this case, ```file_path``` is a file:

```
os.path.isfile(path=file_path)
```
![img_055.png](./images/img_055.png)

![img_056.png](./images/img_056.png)

The os path method ```isdir``` will check if the file path corresponds to a directory or folder, returning a boolean value. In this case, ```file_path``` is a file and not a folder:

```
os.path.isdir(s=file_path)
```

![img_057.png](./images/img_057.png)

For a file path that is a file, it can be split into a basename (name of the file itself, including the file extension) and also the dirname (directory or folder name) using the os path methods ```dirname``` and ```basename``` respectively:

```
os.path.basename(p=file_path)
os.path.dirname(p=file_path)
```

![img_058.png](./images/img_058.png)

This gives the file and path respectively:

```
os.path.isfile(path=os.path.basename(p=file_path))
os.path.isdir(s=os.path.dirname(p=file_path))
```

![img_059.png](./images/img_059.png)

The os path method ```splitext``` is an abbreviation for split extension. It will return a tuple containing the file path excluding the extension in the 0th index and the extension itself in the 1st index:

```
os.path.splitext(p=file_path)
os.path.splitext(p="text_file.txt")
```

![img_060.png](./images/img_060.png)

The os path method ```split``` on the other hand will split the directory or folder and the file name. It will return a tuple with the directory or folder name in the 0th index and the file name including the extension in the 1st index:

```
os.path.split(p=file_path)
folder, file = os.path.split(p=file_path)
folder
file
```

![img_061.png](./images/img_061.png)

### Make and Delete Directories

The ```mkdir``` function is an abbreviation, for make directory:

```
os.mkdir(path="Test")
```

![img_062.png](./images/img_062.png)

![img_063.png](./images/img_063.png)

The ```rmdir``` function is an abbreviation, for remove directory:

```
os.rmdir(path="Test")
```

![img_064.png](./images/img_064.png)

![img_065.png](./images/img_065.png)

### Rename Directory

The ```Test``` directory or folder can be remade using:

```
os.mkdir("Test")
```

![img_066.png](./images/img_066.png)

![img_067.png](./images/img_067.png)

The ```rename``` function can be used to rename a source directory to a destination directory. In this example ```"Test"``` will be renamed ```"Test2"```:

```
os.rename(src="Test", dst="Test2")
```

![img_068.png](./images/img_068.png)

![img_069.png](./images/img_069.png)

A file can also be renamed by specifying the source and the destination in terms of an original file name and a new file name:

```
os.rename(src="text_file2.txt", 
          dst="mary_mary_quite_contrary.txt")
```

![img_070.png](./images/img_070.png)

![img_071.png](./images/img_071.png)

![img_072.png](./images/img_072.png)

Moving the location of a file is done using rename and specifying the folder location as part of the destination:

```
os.rename(src="mary_mary_quite_contrary.txt", 
          dst=r"Test2\\mary_mary_quite_contrary.txt")
```

![img_073.png](./images/img_073.png)

![img_074.png](./images/img_074.png)

![img_075.png](./images/img_075.png)

The changes to the file name and location can be reverted using:

```
os.rename(src=r"Test2//mary_mary_quite_contrary.txt", 
          dst="text_file2.txt")
```

![img_076.png](./images/img_076.png)

![img_077.png](./images/img_077.png)

![img_078.png](./images/img_078.png)

### Change Current Working Directory

So far, all operations have been carried out from the current working directory, which can be determined using the function get current working directory ```getcwd```.

```
os.getcwd()
```

![img_079.png](./images/img_079.png)

The items in the current working directory can be listed using the function list directory ```listdir```:

```
os.listdir()
```

![img_080.png](./images/img_080.png)

![img_081.png](./images/img_081.png)

The current working directory can be changed using the command change directory ```chdir``` which takes a positional input argument ```path```. The ```path``` can be expressed as a subfolder within the original current working directory: 

```
os.chdir(path="Test2")
```

![img_082.png](./images/img_082.png)

Now ```listdir``` shows an empty list as the directory is empty:

![img_083.png](./images/img_083.png)

```
os.listdir()
```

![img_084.png](./images/img_084.png)

The current working directory is now ```Test2``` or more explicitly ```r"C://Users//Philip//Documents//Test2"```. 

To get to ```r"C://Users//Philip//Documents"``` from this current directory in file explorer, press ```Alt``` + ```↑```

![img_085.png](./images/img_085.png)

To go up a level in Python the syntax ```r"..//"``` is used. For example, the directory can be changed up a level to ```r"C://Users//Philip//Documents"``` by using:

```
os.chdir(path=r"..//")
```

![img_086.png](./images/img_086.png)

```getcwd``` can be used to confirm that the ```r"C://Users//Philip//Documents"``` folder is now selected:

```
os.getcwd()
```

![img_087.png](./images/img_087.png)

The related syntax ```r"./"``` means in the same directory. Changing to the same directory should result in no changes:

```
os.chdir(path=r"./")
```

![img_088.png](./images/img_088.png)


```getcwd``` can be used to confirm that the current working directory is still the ```r"C://Users//Philip//Documents"``` folder:

```
os.getcwd()
```

![img_089.png](./images/img_089.png)

While the above operation may have seemed pointless (changing to the same directory). This syntax is sometimes explicitly used to indicated that a file is in the same directory as the current working directory. For example the text file ```r".//text_file2.txt"```

![img_090.png](./images/img_090.png)

The current working directory can also be changed using a full file path. For example ```r"C://Users//Philip//Documents//Test2"```:

```
os.chdir(path=r"C://Users//Philip//Documents//Test2")
```

![img_091.png](./images/img_091.png)

This change can once again be checked using ```getcwd```:

```
os.getcwd()
```

![img_092.png](./images/img_092.png)

Recall that the file path can also be constructed using the ```path``` method ```join``` with the ```os``` path environmental variable:

```
os.chdir(path=os.path.join(os.environ["USERPROFILE"], 
                           "Documents", 
                           "Test2")
        )
```

![img_093.png](./images/img_093.png)

This change can once again be checked using ```getcwd```:

```
os.getcwd()
```

![img_094.png](./images/img_094.png)

Now that the current working directory is this folder ```"Test2"```, the function ```rename``` can be used to move the file ```"text_file2.txt"``` from up a level to the folder ```Test2```:

```
os.rename(src=r"..//text_file2.txt", dst="text_file2.txt")
```

![img_095.png](./images/img_095.png)

![img_096.png](./images/img_096.png)

![img_097.png](./images/img_097.png)

### Make and Delete Multi-Level Directories 

Unlike the function ```rename```, the function ```mkdir``` and ```rmdir``` 
only work within the current working directory and do not work over multiple levels:

```
os.mkdir(path="SubFolder1")
```

![img_098.png](./images/img_098.png)

![img_099.png](./images/img_099.png)

To create a subfolder within ```"Subfolder1"```, the directory needs to be changed to ```"Subfolder1"```. Then a ```SubSubfolder1``` can be created:

```
os.chdir(path="SubFolder1")
```

![img_100.png](./images/img_100.png)

![img_101.png](./images/img_101.png)

Now the ```"SubSubFolder1"``` can be created:

```
os.mkdir(path="SubSubFolder1")
```

![img_102.png](./images/img_102.png)

![img_103.png](./images/img_103.png)


```makedirs``` and ```removedirs``` are functions suited for multi-level operations. For example if the current working directory is change back to ```"Documents"```:

```
os.chdir(path=os.path.join(os.environ["USERPROFILE"], "Documents"))
```

![img_104.png](./images/img_104.png)

```
os.makedirs(name=r"Test2\\SubFolder2\\SubSubFolder2")
```

![img_105.png](./images/img_105.png)

![img_106.png](./images/img_106.png)


Care should be taken when using the function ```removedirs``` as it will remove all empty directories. FOr example if the following is used;

```
os.removedirs(name=r"Test2\\SubFolder2\\SubSubFolder2")
```

![img_107.png](./images/img_107.png)

```"SubSubFolder2"``` and ```"SubFolder2"``` will be removed as both are empty. ```"Test2"``` has a file in it and is not removed:

![img_108.png](./images/img_108.png)

### Walk

The ```walk``` function can be used to create a generator object consisting of tuples of the form (```root```, ```dirs```, ```files```). These can be print a list of all files and directories found contained within a file path:

```
file_path = os.path.join(os.environ["USERPROFILE"], "Documents")
for root, dirs, files in os.walk(file_path, topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
```

![img_109.png](./images/img_109.png)


### Statistics

From the right click contaxt menu of a file in WIndows Explorer, a files propteries can be examined:

![img_110.png](./images/img_110.png)

![img_111.png](./images/img_111.png)

These file properties or statistics can be obtained using the ```stat``` function:

```
os.stat(path="text_file.txt")
```

![img_112.png](./images/img_112.png)

Each statistic can be read off as an attribute. 

The size for Windows Explorer is ```st_size```:

```
os.stat(path="text_file.txt").st_size
```

![img_113.png](./images/img_113.png)

The created, modified and accessed time are ```st_ctime```, ```st_mtime``` and ```st_atime``` respectively:

```
os.stat(path="text_file2.txt").st_ctime
```

![img_114.png](./images/img_114.png)

The value given is a timestamp which is the time in milliseconds using ```00:00:00 1 January 1970``` as a reference. This can be converted into a date using the datetime class:

```
import datetime as dt
dt.datetime.fromtimestamp(os.stat(path="text_file.txt").st_ctime)
```

![img_115.png](./images/img_115.png)

```
import datetime as dt
print(dt.datetime.fromtimestamp(os.stat(path="text_file.txt").st_ctime))
```

![img_116.png](./images/img_116.png)

### Copy File

The ```os``` module has no copy function. ```copy``` is regarded as a higher level function. This high level function is however available in the shell utilities ```shutil``` module. In this example, only a basic copy will be explored:

```
import shutil
shutil.copy(src="text_file.txt", dst="text_file3.txt")
```

![img_117.png](./images/img_117.png)

![img_118.png](./images/img_118.png)

![img_119.png](./images/img_119.png)

Return to:
[Home](../../../)