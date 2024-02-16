# PyCharm

PyCharm is an advanced Python IDE used for Python script files (.py file extension). It does not have ipython magic commands or support interactive Python notebooks (.ipynb file extension). 

## WinGet

PyCharm can be installed using Winget using the command:

```
WinGet install JetBrains.PyCharm.Community
```

## Customising PyCharm

Launch PyCharm from the Start Menu shortcut:

<img src='images_pycharm/img_011.png' alt='img_011' width='450'/>

Select customise and choose your color scheme:

<img src='images_pycharm/img_012.png' alt='img_012' width='450'/>

## Selecting the Python Interpreter

Like VSCode Pycharm expects a project (folder). Select projects and select New Project:

<img src='images_pycharm/img_013.png' alt='img_013' width='450'/>

In location select the Documents folder and create a new project folder:

<img src='images_pycharm/img_014.png' alt='img_014' width='450'/>

Select previously configured interpretter → Add Interpreter → Add Local Interpreter:

<img src='images_pycharm/img_015.png' alt='img_015' width='450'/>

Select conda environment and then Use Existing conda environment. Then use the dropdown box to select the base Python environment (if its not already selected). Select OK:

<img src='images_pycharm/img_016.png' alt='img_016' width='450'/>

Select Create:

<img src='images_pycharm/img_017.png' alt='img_017' width='450'/>

Pycharm will look at all the libraries in the Python environment and index their docstrings. This can take a very long time with the Anaconda (base) Python environment and a low end computer as the Anaconda (base) environment has a large number of packages.

Pycharm will give information about Microsoft Defender slowing down its indexing:

<img src='images_pycharm/img_018.png' alt='img_018' width='450'/>

To change Microsoft Defender settings. Right click the Start Button and select Settings:

<img src='images_pycharm/img_019.png' alt='img_019' width='150'/>

Select the Privacy & Security tab to the left and Virus & Threat protection to the right:

<img src='images_pycharm/img_020.png' alt='img_020' width='450'/>

Under Virus & Threat protection settings, select manage settings:

<img src='images_pycharm/img_021.png' alt='img_021' width='450'/>

Scroll down until Manage Exclusions and select Add an exclusion and specify a folder:

<img src='images_pycharm/img_022.png' alt='img_022' width='450'/>

Select the project folder:

<img src='images_pycharm/img_023.png' alt='img_023' width='450'/>

Repeat the procedure, going to %APPDATA%:

<img src='images_pycharm/img_024.png' alt='img_024' width='450'/>

Then selecting JetBrains:

<img src='images_pycharm/img_025.png' alt='img_025' width='450'/>

Then selecting PyCharmCE2023.2 and select Selcet Folder:

<img src='images_pycharm/img_026.png' alt='img_026' width='450'/>

The two exclusions should now be added:

<img src='images_pycharm/img_027.png' alt='img_027' width='450'/>

PyCharm should now index faster:

<img src='images_pycharm/img_028.png' alt='img_028' width='450'/>

Once indexing is complete you can use PyCharm:

<img src='images_pycharm/img_029.png' alt='img_029' width='450'/>

## The Welcome Script

A welcome script displays by default. To simply it create a script that has:

```
identifiers = dir()
print(identifiers)
```

Notice the data model identifiers ```__name__``` and ```__file__``` which are included in every Python module.

<img src='images_pycharm/img_030.png' alt='img_030' width='450'/>

```__name__``` and ```__file__``` are the name of the script file and the location of the file in Windows Explorer. These can be printed and display in the console:

```
print(__name__)
print(__file__)
```

Notice the name is ```'__main__'``` and not ```main``` which is the file name:

<img src='images_pycharm/img_031.png' alt='img_031' width='450'/>

If a new script file is created by right clicking in the project file explorer and selecting New → Python File:

<img src='images_pycharm/img_032.png' alt='img_032' width='450'/>

And called ```script.py```:

<img src='images_pycharm/img_033.png' alt='img_033' width='450'/>

The same code can be added:

```
print(__name__)
print(__file__)
```

<img src='images_pycharm/img_034.png' alt='img_034' width='450'/>

If this script file is ran directly:

<img src='images_pycharm/img_035.png' alt='img_035' width='450'/>

Notice the file location has changed and points to ```script.py```. name has not changed and is still ```'__main__'``` and not ```script```:

<img src='images_pycharm/img_036.png' alt='img_036' width='450'/>

If the code is modified so the main module is imported:

```
print(__name__)
print(__file__)

import main
```

<img src='images_pycharm/img_037.png' alt='img_037' width='450'/>

Notice that the name of the module executed directly is ```'__main__'``` and the name of the module imported is ```'main'```. In other words the module executed directly is always called ```'main'``` and the modules imported use the file name of the module. 


Essentially the following:

```
if __name__ == '__main__':
    pass
    # the file is executed directly
else:
    pass
    # the file has been imported 
```

is a check to see if the module is executed directly or imported. Sometimes additional diagnostic code is added when a script file is executed directly.

<img src='images_pycharm/img_038.png' alt='img_038' width='450'/>

## Code Completion

PyCharm has indexed all the libraries in the (base) Python Environment and uses this indexed information for code completion.

Inputting p shows a list of all the identifiers beginning with the prefix p:

<img src='images_pycharm/img_039.png' alt='img_039' width='450'/>

The builtins module can be imported and identifiers from it can be viewed:

<img src='images_pycharm/img_040.png' alt='img_040' width='450'/>

The datetime module can be imported and a one-line docstring displays when the datetime class is input with open parenthesis:

<img src='images_pycharm/img_041.png' alt='img_041' width='450'/>

Pressing ```Ctrl```+```q``` will display a more detailed docstring as a pop up balloon:

<img src='images_pycharm/img_042.png' alt='img_042' width='450'/>

Code completion works for the numpy library and all other third-party libraries in the (base) Python environment as its contents have been indexed:

<img src='images_pycharm/img_043.png' alt='img_043' width='450'/>

## Debugger and Variables

The following variables can be instantiated in a Python Script:

```
string = 'hello'
bytestring = b'hello'
bytearraystring = bytearray(b'hello')
wholenum = 1
floatingpointnum = 3.14
boolean = True
archive = (string, string, wholenum, floatingpointnum)
active = [string, string, wholenum, floatingpointnum]
unique = {string, string, wholenum, floatingpointnum}
mapping = {'r': 'red', 'g': 'green', 'b': 'blue'}
```

PyCharm does not show Variables outwith the debugger. A breakpoint can be added to line number 1 and another breakpoint can be added to line number 10. The file can be debugged using the debug button:

<img src='images_pycharm/img_044.png' alt='img_044' width='450'/>

Threads & Variables can be selected. The script data model attributes display as special variables:

<img src='images_pycharm/img_045.png' alt='img_045' width='450'/>

If resume program is selected the builtins instances instantiated in the script will display as variables:

<img src='images_pycharm/img_046.png' alt='img_046' width='450'/>

A collection such as the list active can be expanded to view its elements in more detail:

<img src='images_pycharm/img_047.png' alt='img_047' width='450'/>

This also works for instances of classes in the third-party data science libraries:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

array = np.array([1, 2, 3, 4])
df = pd.DataFrame({'x': np.array([1, 2, 3, 4, 5]),
                   'y': np.array([2, 4, 6, 8, 10])})

plt.plot(df['x'], df['y'])
plt.show()
```

<img src='images_pycharm/img_048.png' alt='img_048' width='450'/>

The array and the DataFrame instance can be viewed in more detail:

<img src='images_pycharm/img_049.png' alt='img_049' width='450'/>

<img src='images_pycharm/img_050.png' alt='img_050' width='300'/>

<img src='images_pycharm/img_051.png' alt='img_051' width='450'/>

<img src='images_pycharm/img_052.png' alt='img_052' width='300'/>

## Plots

Plots don't display in debug mode:

<img src='images_pycharm/img_053.png' alt='img_053' width='450'/>

They display interactively by default using the QtAgg backend when the script is ran normally:

<img src='images_pycharm/img_054.png' alt='img_054' width='450'/>

[Return to Anaconda Tutorial](./readme.md)