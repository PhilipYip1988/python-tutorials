# The Operating System Module

## Text Files

A text file can be created in the same folder as the Interactive Python Notebook File:

![img_001](./images/img_001.png)

The following text can be added to it:

```
Baa, baa, black sheep,
Have you any wool?
Yes, sir, yes, sir,
Three bags full.

One for my master,
One for my dame,
And one for the little boy
Who lives down the lane.
```

![img_002](./images/img_002.png)

Text files can be viewed in Notepad++ with View → Show Symbol → Show All Characters:

![img_026](./images/img_026.png)

Text files are opened in Python by using the ```open``` function. The docstring can be viewed by inputting ```open()``` and pressing shift ```⇧``` and tab ```↹```:

![img_003](./images/img_003.png)

The ```open``` function requires a file which can be specified directly when it is in the same folder as the interactive Python notebook file (or Python script file).

The ```mode``` keyword input argument can be specified using a single letter:

|mode|definition|
|---|---|
|'r'|open an existing file and read existing content|
|'w'|open an existing file and write over existing content|
|'a'|open an existing file and append new content|
|'x'|create a new file and write new content|

A second letter can also be used for the encoding. The encoding can be ```'t'``` text (default) which is also known as ```UTF-8``` or ```'b'``` binary which is known as ```'ASCII'```. 

```mode=rt``` for example is the default which reads a text file encoded as text ('ASCII'). 

For other encoding schemes, the ```encoding``` keyword argument is seperately used. For a CSV file created in Microsoft Excel, the ```'UTF-8-Sig'``` encoding needs to be used to properly handle the BOM. The other encoding schemes available were previously discussed in the text data types tutorial. 

|encoding|bit|bytes|byte order|BOM|
|---|---|---|---|---|
|'ASCII'|1|8| |---|
|'Latin1'|1|8| | |
|'UTF-16-LE'|2|16|little endian| |
|'UTF-16-BE'|2|16|big endian| |
|'UTF-16'|2|16| |BOM|
|'UTF-32-LE'|4|32|little endian| |
|'UTF-32-BE'|4|32|big endian| |
|'UTF-32'|4|32| |BOM|
|'UTF-8'|1-4|adaptive|1-4 adaptive| |
|'UTF-8-Sig'|1-4|adaptive|1-4 adaptive|BOM|

The ```newline``` keyword input argument can be used to specify the character that is used to represent a new line. In Python the escape characters ```\r\n``` are used to represent this which is the default.

A file is normally accessed using a ```with``` code block which opens the file and automatically closes it as the code block is exited:

```
with open('textfile.txt', mode='rt') as file:
    pass

```

A number of identifiers from the file object can be viewed by inputting ```file.``` and pressing tab ```↹```:

![img_004](./images/img_004.png)

```name```, ```mode```, ```encoding```, ```errors``` and ```closed``` are attributes.

```
with open('textfile.txt', mode='rt') as file:
    print(file.name)
    print(file.mode)
    print(file.encoding)
    print(file.errors)
    print(file.closed)


file.closed
```

![img_005](./images/img_005.png)

```readable```, ```writeable``` and ```seekable``` are methods which return a ```bool```:

```
with open('textfile.txt', mode='rt') as file:
    print(file.readable())
    print(file.writable())
    print(file.seekable())
    
```

![img_006](./images/img_006.png)

The ```read``` method can read all the text from a file as a multi-line string:

```
with open('textfile.txt', mode='rt') as file:
    data = file.read()
    
```

![img_007](./images/img_007.png)

![img_008](./images/img_008.png)

![img_009](./images/img_009.png)

The ```size``` input argument has a default value of ```-1``` meaning all the text is read. A custom ```size``` can be supplied positionally only to read up to a maximum ```size``` of characters:

```
with open('textfile.txt', mode='rt') as file:
    data = file.read(20)
    
```

![img_010](./images/img_010.png)

![img_011](./images/img_011.png)

The ```readline``` method will read text up to and including the next ```'\n'``` Unicode whitespace character:

```
with open('textfile.txt', mode='rt') as file:
    data = file.readline()
    
```

![img_012](./images/img_012.png)

![img_013](./images/img_013.png)

The ```readlines``` method will output a list of strings. Similar to ```readline``` each string will read text up to and including the next ```\n``` Unicode whitespace character:

```
with open('textfile.txt', mode='rt') as file:
    data = file.readlines()
    
```

![img_014](./images/img_014.png)

![img_015](./images/img_015.png)

![img_016](./images/img_016.png)

The file can be conceptualised as one long multi-line Unicode string. Each Unicode character has a zero-order index where the first Unicode character has an index value of ```0``` and the cursors index can be changed using ```seek```. Index ```10``` is equivalent to the following character:

![img_017](./images/img_017.png)

Moving the cursor to index 10 using the method ```seek``` and then using ```readline``` will read from the cursor at index position 10 up to and including the next ```\n``` Unicode whitespace character:

```
with open('textfile.txt', mode='rt') as file:
    file.seek(10)
    data = file.readline()
```

![img_018](./images/img_018.png)

![img_019](./images/img_019.png)

A ```file``` object is more similar to a multi-line Unicode string than an iterator of a multi-line string and it is possible to go back, for example using the method ```seek``` to return the cursor to index ```5```:

![img_020](./images/img_020.png)

```
with open('textfile.txt', mode='rt') as file:
    file.seek(10)
    data = file.readline()
    file.seek(5)
    data2 = file.readline()

```

![img_021](./images/img_021.png)

![img_022](./images/img_022.png)

When using the method ```seek``` care should be taken to ensure that the whitespace character ```'\n'``` shown as line feed in Notepad++ is included itself:

![img_023](./images/img_023.png)

```
with open('textfile.txt', mode='rt') as file:
    file.seek(22)
    data = file.read()

```

![img_024](./images/img_024.png)

![img_025](./images/img_025.png)

Notice this string begins with a ```'\n'```.

![img_027](./images/img_027.png)

The file can be opened using the mode ```at``` which stands for append text. When appended, the cursor position is automatically at the end of the file:

![img_028](./images/img_028.png)

The ```write``` function can be used to write additional text to the file:

```
with open('textfile.txt', mode='at') as file:
    file.write('Hello World')

```

![img_029](./images/img_029.png)

![img_030](./images/img_030.png)

There is no ```writeline``` method and instead the whitespace ```'\n'``` needs to be added manually:

```
with open('textfile.txt', mode='at') as file:
    file.write('\nHello World')
    
```

![img_031](./images/img_031.png)

![img_032](./images/img_032.png)

The ```writelines``` method can be used to write a list of lines:

```
with open('textfile.txt', mode='at') as file:
    file.writelines(['Text.',
                     'Text2.',
                     'Text3.'])
    
```    

![img_033](./images/img_033.png)

![img_034](./images/img_034.png)

Once again the new line line whitespace character needs to be explicitly specified ```'\n'```.

A new text file can be created with writeable access using the mode ```'xt'```:

```
with open('textfile2.txt', mode='xt') as file:
    file.write('a\n')
    file.write('b\n')
    file.write('c\n') 
    
```

![img_035](./images/img_035.png)

The file is displayed in the file explorer:

![img_036](./images/img_036.png)

Notice when the file is opened in Notepad++ there are actually two characters displayed for the new line, the carriage return and the line feed:

![img_037](./images/img_037.png)

There is a subtle difference in lines ending in line feed and carriage return and lines only ending in line feed. The default behaviour of a newline can be disabled by assigning it to an empty string. This means both ```'\r\n'``` and ```'\n'``` can be specified:

```
with open('textfile3.txt', mode='xt', newline='') as file:
    file.write('a\n') # new line
    file.write('b\r\n') # carriage return & line feed
    file.write('c\r') # line feed
    
```

![img_038](./images/img_038.png)

![img_039](./images/img_039.png)

Compare this to the default behaviour:

```
with open('textfile4.txt', mode='xt') as file:
    file.write('a\n') # new line
    file.write('b\r\n') # carriage return & line feed
    file.write('c\r') # line feed
    
```

![img_040](./images/img_040.png)

![img_041](./images/img_041.png)

The subtle differences here can influence the length of the strings which can be seen when the ```repr``` of the retrieved data is seen in the cell output:

```
with open('textfile2.txt', mode='rt', newline='') as file:
    data = file.read()

data
len(data)
```

![img_042](./images/img_042.png)

```
with open('textfile3.txt', mode='rt', newline='') as file:
    data = file.read()

data
len(data)
```

![img_043](./images/img_043.png)

This also changes the length of the string for each string in the list of strings when readlines is used:

```
with open('textfile2.txt', mode='rt', newline='') as file:
    data = file.readlines()

data
```

![img_044](./images/img_044.png)

```
with open('textfile2.txt', mode='rt', newline='') as file:
    data = file.readlines()

data
```

![img_045](./images/img_045.png)

Differences in this whitespace will also influence the index position used for the method ```seek```.

For this reason, ```readlines``` is often preferred as list comprehension can be used with the ```str``` method ```strip``` which by default strips the whitespace. ```str``` concatenation can also be used in the list comprehension to have a consistent line ending if desired:

```
data
[line.strip() for line in data]
[line.strip() + '\n' for line in data]
[line.strip() + '\r\n' for line in data]
```

![img_046](./images/img_046.png)

```
data = [line.strip() for line in data]
'\r\n'.join(data)
```

![img_047](./images/img_047.png)

If ```data2.txt``` is examined.

![img_048](./images/img_048.png)

![img_049](./images/img_049.png)

If the file is opened as a text file with write access, i.e. ```mode='wt'```, then all previous data in the file will be erased and the file can otherwise be treated as a blank file:

```
with open('textfile2.txt', mode='wt') as file:
    pass

```

![img_050](./images/img_050.png)

![img_051](./images/img_051.png)

If the file is opened as a raw binary file with write access. A ```byte``` can be written to it using hexadecimal escape characters:

```
with open('textfile2.txt', mode='wb') as file:
    file.write(b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21\x0d\x0a')

```

![img_052](./images/img_052.png)

![img_053](./images/img_053.png)

Note the ```'\x20'``` is the hexadecimal escape character for a space and the last two escape characters are ```'\x0d\x0a'``` which is the Carriage Return and Line Feed respectively.

![img_054](./images/img_054.png)

If the text is highlighted in Notepad++ and Plugins → Converter → ASCII to Hex is selected:

![img_055](./images/img_055.png)

This converted file can be be read in using text read i.e. ```mode='rt'```:. The ```bytes``` alternative constructor ```fromhex`` can be used to convert this back to ASCII characters:

```
with open('textfile2.txt', mode='rt') as file:
    data = file.read()
    
data

bytes.fromhex(data)
```

![img_056](./images/img_056.png)

Returning the file back to:

```
with open('textfile2.txt', mode='wb') as file:
    file.write(b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21\x0d\x0a')

```

![img_057](./images/img_057.png)

Its properties can be examined using the file explorer:

![img_058](./images/img_058.png)

![img_059](./images/img_059.png)

Note the size is 14 bytes, meaning there are 14 ASCII characters in it including the Carriage Return and Line Feed:

![img_060](./images/img_060.png)

If the file is opened as a raw binary file with append access. The ```truncate``` method can be used to truncate the file to a maximum number of bytes, for example ```5```:

```
with open('textfile2.txt', mode='ab') as file:
    file.truncate(5)
    
```

![img_061](./images/img_061.png)

The file when opened, now only has 5 ASCII characters:

![img_062](./images/img_062.png)

## OS Module

So far, the only text files examined have been in the same folder as the Interactive Python Notebook File. The Operating System Module ```os``` can be used to navigate around the Operating System. To import the module use:

```
import os
```

Details about the module can be found using:

```
? os
```

![img_063](./images/img_063.png)

The identifiers from the ```os``` module can be viewed by inputting ```os.``` followed by a tab ```↹```:

![img_064](./images/img_064.png)

The ```os``` module has a number of string identifiers such as current directory ```curdir``` represented by ```'.'```, parent directory ```pardir``` represented by ```'..'```, the seperator used between folders ```sep``` which on Windows is ```'\\'``` by default (recall for Python strings the ```\``` is used to insert an escape character, to insert ```\``` as the escape character ```\\``` is used.) The alternative seperator ```altsep``` is ```'/'``` which Linux also uses by default. The extension seperator ```extsep``` is ```'.'``` and the line seperator ```linesep``` is carriage return, line feed ```'\r\n'```:

```
os.curdir
os.pardir
os.sep
os.altsep
os.extsep
os.linesep
```

![img_065](./images/img_065.png)

These are commonly used for file path manipulation and can be imported directly using:

```
from os import curdir, pardir, sep, extsep
```

![img_066](./images/img_066.png)

The environmental variables path is a dictionary like collection of key value pairs:

```
os.environ
```

![img_067](./images/img_067.png)

It can be viewed in the Variable Explorer using:

```
environ = os.environ
```

![img_069](./images/img_069.png)

And for readibility, cast into a dicitionary using:

```
environ = dict(os.environ)
```

![img_070](./images/img_070.png)

![img_071](./images/img_071.png)

It is worthwhile examining this dictionary as it contains important locations in the Windows OS:

![img_072](./images/img_072.png)
![img_073](./images/img_073.png)
![img_074](./images/img_074.png)
![img_075](./images/img_075.png)
![img_076](./images/img_076.png)
![img_077](./images/img_077.png)
![img_078](./images/img_078.png)

Of particular importance are ```'USERNAME'``` which is different for all Windows Users and ````'USERPROFILE'``` which is dependent on the ```'USERNAME'```. If ```%USERPROFILE%``` is typed in the address bar in Windows Explorer, the UserProfile is displayed:

![img_079](./images/img_079.png)

This contains the Documents folder:

![img_080](./images/img_080.png)

This file path can be accessed using the key:

```
os.environ['USERPROFILE']
```

And Documents can therefore be accessed using string concatenation:

```
os.environ['USERPROFILE'] + sep + 'Documents'
```

![img_081](./images/img_081.png)

The ```notebook.ipynb``` file in Documents:

![img_082](./images/img_082.png)

Therefore has the full path

```
os.environ['USERPROFILE'] + sep + 'Documents' + sep + 'notebook' + extsep + 'ipynb'
```

![img_083](./images/img_083.png)

The function get environmental variables ```os.getenv``` can be used to retrieve the file path of the environmental variable using the key:

```
os.getenv('USERPROFILE')
```

![img_102](./images/img_102.png)

Concatenation using the above is quite cumbersome. The ```os.path``` module compartmentalises useful path related identifiers: 

![img_084](./images/img_084.png)

Its list of identifiers can be viewed by inputting ```os.``` followed by a tab ```↹```:

![img_085](./images/img_085.png)

The string instances ```curdir```, ```pardir```, ```sep```, ```extsep```, ```altsep``` are available as before.

The three most commonly used functions in the ```os``` module, get current working directory ```os.getcwd```,  change directory ```os.chdir``` and list directories ```os.listdir``` are frequently used in combination with ```path``` identifiers.

The current working directory can be examined using:

```
os.getcwd()
```

![img_086](./images/img_086.png)

If ```os.listdir()``` is input followed by a shift ```⇧``` and tab ```↹```, its docstring will display:

![img_087](./images/img_087.png)

It has the keyword input argument ```path``` which by defaults to ```None``` meaning the current working directory is selected:

![img_088](./images/img_088.png)

Each directory within the current working directory and file within the current working directory are shown. Note that the files have file extensions and the directory names have no extensions.

The absolute path ```os.path.abspath``` will retrieve the full path name from a file:

```
os.path.abspath('textfile.txt')
```

![img_089](./images/img_089.png)

The relative path ```os.path.relpath``` will retrieve the relative path from the current working directory:

```
os.path.relpath('C:\\Users\\Philip\\Documents\\textfile.txt')
```

![img_090](./images/img_090.png)

If a new folder ```SubDirectory``` is created:

![img_091](./images/img_091.png)

And the absolute path is examined:

```
os.path.abspath('SubDirectory')
```

![img_092](./images/img_092.png)

Because this ```SubDirectory``` is within the current working directory, the directory can be changed to it using the relative path:

```
os.chdir('SubDirectory')
```

Notice if the relative path of the same file explored earlier is examined:

```
os.path.relpath('C:\\Users\\Philip\\Documents\\textfile.txt')
```

That the prefix ```..``` now displays which instructs to go up a level to the parent directory:

![img_093](./images/img_093.png)

The directory name of this file can be found using the function ```os.path.dirname```:

```
os.path.dirname('..\\textfile.txt')
```

![img_094](./images/img_094.png)

The expand user profile ```os.path.expanduser``` can be used to expand a user path beginning with the ```'~'```, normally these involve a raw string:

```
os.path.expanduser('~')
os.path.expanduser('~\\Documents')
os.path.expanduser(r'~\Documents')
```

![img_095](./images/img_095.png)

The expand environmental variables ```os.path.expandvar``` can be used to expand a user path beginning with an environmental variable enclosed in ```%``` signs:

```
os.path.expandvars('%UserProfile%')
os.path.expandvars('%AppData%')
os.path.expandvars('%WinDir%')
os.path.expandvars('%UserProfile%\\Documents')
```

![img_096](./images/img_096.png)

The split extension ```os.splitext``` returns a ```tuple``` where the first element is the path to the file and the second element is the file extension:

```
os.path.splitext(os.path.expanduser(r'~\Documents\notebook.ipynb'))
```

![img_097](./images/img_097.png)

The split ```os.path.split``` returns a ```tuple``` where the first element is the directory of the file and the second element is the file including the extension:

```
os.path.split(os.path.expanduser(r'~\Documents\notebook.ipynb'))
```

![img_098](./images/img_098.png)

The join ```os.path.join``` joins elements of a file path. This function is particularly useful as it automatically adds the ```\\``` which can be easily missed out when using string concatenation:

```
os.path.join(os.path.expanduser('~'), 
             'Documents', 
             'notebook.ipynb')
```

![img_099](./images/img_099.png)

The exists ```os.path.exists``` can be used to check whether a directory or file exists:

```
os.path.exists(os.path.join(os.path.expanduser('~'), 
                            'Documents', 
                            'notebook.ipynb'))

os.path.exists(os.path.join(os.path.expanduser('~'), 
                            'Documents', 
                            'notebook.ipynb'))
```

![img_100](./images/img_100.png)

The same file ```os.path.samefile``` can be used to check whether two paths are to the same file:

```
os.path.samefile(os.path.expanduser(r'~\Documents\notebook.ipynb'), 
                 r'..\notebook.ipynb')
```

![img_101](./images/img_101.png)

Now that the most common path related identifiers have been examined, directory operations can be used. The current working directory may be examined and changed to the Documents folder using:

```
os.getcwd()
os.chdir(os.path.expanduser(r'~\Documents'))
os.getcwd()
```

![img_103](./images/img_103.png)

![img_104](./images/img_104.png)

To check for the existance of the ```'SubDirectory'```, the absolute path or relative path can be used:

```
os.path.exists(os.path.join(os.getcwd(), 'SubDirectory'))
os.path.exists('SubDirectory')
```

![img_105](./images/img_105.png)

The remove directory ```os.rmdir``` can be used to remove an empty directory.

```
os.rmdir('SubDirectory')
```

![img_106](./images/img_106.png)

![img_107](./images/img_107.png)

The make directory ```os.mkdir``` can be used to make a directory or a new file:

```
os.mkdir('SubDirectoryA')
```

![img_108](./images/img_108.png)

![img_109](./images/img_109.png)

This function operates one level at a time:

```
os.mkdir(r'SubDirectoryA\SubDirectoryB')
```

![img_110](./images/img_110.png)

![img_111](./images/img_111.png)

Now that the directory is made, the ```open``` command with ```mode=xt``` can be used to touch the directory:

```
with open(r'SubDirectoryA\SubDirectoryB\textfile.txt', mode='xt') as file:
    file.write('Hello World!\n')
```

![img_112](./images/img_112.png)

![img_113](./images/img_113.png)

![img_114](./images/img_114.png)

The make directories function ```makedirs``` is more powerful and can create a series of nested subdirectories:

![img_115](./images/img_115.png)

```
os.makedirs(r'SubDirectory1\SubDirectory2')
```

![img_116](./images/img_116.png)

![img_117](./images/img_117.png)

![img_118](./images/img_118.png)

Now that the directory is made, the ```open``` command with ```mode=at``` can be used to touch the directory as before:

```
with open(r'SubDirectory1\SubDirectory2\textfile2.txt', mode='xt') as file:
    file.write('Hello World!!\n')
```

![img_119](./images/img_119.png)

![img_120](./images/img_120.png)

![img_121](./images/img_121.png)

Generally the procedure to remove a file and an empty directories is to use ```os.remove``` to remove the file, ```os.rmdir``` to remove the empty directory and ```os.listdir``` to check the contents at each stage:

```
os.listdir(r'SubDirectory1\SubDirectory2')
os.remove(r'SubDirectory1\SubDirectory2\textfile2.txt')
os.listdir(r'SubDirectory1\SubDirectory2')
os.rmdir(r'SubDirectory1\SubDirectory2')
os.listdir(r'SubDirectory1')
os.rmdir(r'SubDirectory1')
```

![img_122](./images/img_122.png)

![img_123](./images/img_123.png)

The more powerful remove directories ```os.removedirs``` can remove a series of empty directories. This function flags up an ```OSError``` if the directories have files in them:

```
os.removedirs(r'SubDirectoryA\SubDirectoryB')
```

![img_124](./images/img_124.png)

```
os.remove(r'SubDirectoryA\SubDirectoryB\textfile.txt')
os.removedirs(r'SubDirectoryA\SubDirectoryB')
```

![img_125](./images/img_125.png)

![img_126](./images/img_126.png)

The replace function ```os.replace``` can be used to replace the source directory of a file to a destination directory. Its dostring can be viewed by inputting ```os.replace()``` followed by a shift ```⇧``` and tab ```↹```:

![img_127](./images/img_127.png)

![img_128](./images/img_128.png)

```
os.mkdir('SubDirectory')
os.replace('textfile.txt', r'SubDirectory\textfile.txt')
```

![img_129](./images/img_129.png)

![img_130](./images/img_130.png)

![img_131](./images/img_131.png)

This can also be used to rename a file:

```
os.replace(r'SubDirectory\textfile.txt', 
           r'SubDirectory\baabaablacksheep.txt')
```

![img_132](./images/img_132.png)

![img_133](./images/img_133.png)

Supposing a number of subdirectories and files are added to ```SubDirectory```:

```
os.makedirs(r'SubDirectory\SubDirectoryA\SubDirectoryB')
os.makedirs(r'SubDirectory\SubDirectory1\SubDirectory2')

with open(r'SubDirectory\SubDirectory1\hello_world.txt', mode='xt') as file:
    file.write('Hello World!\n')

with open(r'SubDirectory\SubDirectoryA\hello_world2.txt', mode='xt') as file:
    file.write('Hello World!!\n')

with open(r'SubDirectory\SubDirectoryA\SubDirectoryB\hello_world3.txt', mode='xt') as file:
    file.write('Hello World!!!\n')

```


![img_134](./images/img_134.png)

The folders can be explored in Windows Explorer:

![img_135](./images/img_135.png)
![img_136](./images/img_136.png)
![img_137](./images/img_137.png)
![img_138](./images/img_138.png)
![img_139](./images/img_139.png)
![img_140](./images/img_140.png)

A generator that walks through all file paths can be created using the function ```os.walk```:

```
forward = os.walk('SubDirectory')
forward
```

![img_141](./images/img_141.png)

```
next(forward)
next(forward)
next(forward)
next(forward)
```

![img_142](./images/img_142.png)

Once exhaused, a ```StopIteratorError``` displays:

```
next(forward)
```

![img_143](./images/img_143.png)

The ```tuple``` returned in each iteration has three elements, the first element is the directory being walked through presented as a string and in this case a relative paths is used. The second element is a list of subdirectories each presented as a string. The third element is a list of files in the subdirectories presented as a string. This can be cast into a ```tuple``` so it can be viewed on the Variable Explorer:

```
walked_dir = tuple(os.walk('SubDirectory'))
```

![img_144](./images/img_144.png)

![img_145](./images/img_145.png)

![img_146](./images/img_146.png)

## Stat Module

If the list of identifiers from ```os``` is examined by inputting ```os.``` followed by a tab ```↹```:

![img_147](./images/img_147.png)

There is a ```stat``` function and a ```st``` module. The ```st``` module is an alias to the seperate module ```stat```:

```
import stat
os.st is stat
```

![img_148](./images/img_148.png)

Typically the ```os.stat``` function is used to access details about a file:

```
info = os.stat(r'SubDirectory/baabaablacksheep.txt')
info
```

![img_149](./images/img_149.png)

![img_150](./images/img_150.png)

![img_151](./images/img_151.png)

These details revolve around the index node (inode) data structure used with Unix file systems.

These details roughly are similar to when a file is right clicked and properties are selected:

![img_152](./images/img_152.png)

![img_153](./images/img_153.png)

![img_158](./images/img_158.png)

![img_159](./images/img_159.png)

If the identifiers in the ```stat``` module are examined by inputting ```stat.``` followed by a tab ```↹```:

![img_154](./images/img_154.png)

Most of the identifiers are integers. The 10 starting with ```ST``` are indexes for the ```os.stat``` function:

```
stat.ST_MODE # Inode protection mode (integer corresponding to combination of read, write, execute permissions).
stat.ST_INO # Inode number (integer unique identifier).
stat.ST_DEV # Device inode resides on (integer).
stat.ST_NLINK # Number of links to the inode (integer).
stat.ST_UID # User id of the owner (integer).
stat.ST_GID # Group id of the owner (integer).
stat.ST_SIZE # Size in Bytes (integer)
stat.ST_ATIME # Access Time (integer timestamp)
stat.ST_MTIME # Modified Time (integer timestamp)
stat.ST_CTIME # Creation Time (integer timestamp)
```

![img_155](./images/img_155.png)

These integers can be used to index into the ```list``` returned from ```os.stat```. For example ```ST_SIZE``` returns the size in bytes and is index ```6```:

```
stat.ST_SIZE 
info[stat.ST_SIZE]
info[6]
```

![img_156](./images/img_156.png)

The three times are given as timestamps which, recall is the time in milliseconds using 00:00:00 1 January 1970 as a reference. This can be converted into a date using the datetime class:

```
import datetime as dt
dt.datetime.fromtimestamp(info[stat.ST_CTIME])
```

![img_157](./images/img_157.png)

There is an associated file descriptor stat ```os.fstat``` and file stat without symbolic links ```os.lstat```. The ```stat``` module has associated identifiers beginning with ```SF``` for use with the file descriptor. The file can be opened with ```os.open``` to return a file descriptor. Opening a file as a file descriptor requires a flag, which is normally assigned to one of the constants in the ```os``` module:

```
fd = os.open(r'SubDirectory/baabaablacksheep.txt', os.O_RDONLY)
fd

info = os.fstat(fd)
info
```

![img_160](./images/img_160.png)

Most of the file properties available in the ```stat``` module are for advanced use case and therefore requires a look through the documentation for a specific use case.

## The Shell Utilities Module

The Shell Utilities Module ```shutil``` is used to perform high level file and directory operations and generally supplements the Operating System Module ```os```. The most commonly used high level file operation not present in ```os``` is ```shutil.copy``` and ```shutil.copy2``` which attempt to copy a file without and with metadata respectively and ```shutil.copytree``` which copies a directory including all its contents. Note that the ```copy``` module previously examined is geared towards copying Python objects and not copying files or directories. The module can be imported using:

```
import shutil
```

A list of identifiers can be seen by inputting ```shutil.``` followed by a tab ```↹```:

![img_161](./images/img_161.png)

```
shutil.copy(src=r'SubDirectory/baabaablacksheep.txt',
            dst=r'SubDirectory/baabaablacksheep2.txt')
```

![img_162](./images/img_162.png)

![img_163](./images/img_163.png)

To copy a directory, ```shutil.copytree``` can be used:

```
shutil.copytree(src=r'SubDirectory',
                dst=r'SubDirectory2')
```

![img_164](./images/img_164.png)

![img_165](./images/img_165.png)

![img_166](./images/img_166.png)

[Home Python Tutorials](https://github.com/PhilipYip1988/python-tutorials/blob/main/readme.md)
