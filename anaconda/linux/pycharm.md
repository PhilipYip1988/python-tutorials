# PyCharm

PyCharm is an advanced Python IDE used for Python script files (.py file extension). It does not have ipython magic commands or support interactive Python notebooks (.ipynb file extension). 

## Installing PyCharm

On Ubuntu, PyCharm should be installed from the Ubuntu App Centre. Search for PyCharm Community and select Install:

<img src='images_pycharm/img_001.png' alt='img_001' width='450'/>

PyCharm is now installed:

<img src='images_pycharm/img_002.png' alt='img_002' width='450'/>

Launch PyCharm from the Start Menu shortcut. Accept the license agreement in order to proceed:

<img src='images_pycharm/img_003.png' alt='img_003' width='350'/>

And optionally supply anonymous statistics:

<img src='images_pycharm/img_004.png' alt='img_004' width='350'/>

## Customising PyCharm

Select customise and choose your colour scheme:

<img src='images_pycharm/img_005.png' alt='img_005' width='450'/>

## Selecting the Python Interpreter

Like VSCode Pycharm expects a project (folder). Select projects and select New Project:

<img src='images_pycharm/img_006.png' alt='img_006' width='450'/>

In location select the Documents folder and create a new project folder:

<img src='images_pycharm/img_007.png' alt='img_007' width='450'/>

Select previously configured interpretter → Add Interpreter → Add Local Interpreter:

<img src='images_pycharm/img_008.png' alt='img_008' width='450'/>

Select conda environment and then Use Existing conda environment. Then use the dropdown box to select the base Python environment (if its not already selected). Select OK:

<img src='images_pycharm/img_009.png' alt='img_009' width='450'/>

Select Create:

<img src='images_pycharm/img_010.png' alt='img_010' width='450'/>

Pycharm will look at all the libraries in the Python environment and index their docstrings. This can take a very long time with the Anaconda (base) Python environment and a low end computer as the Anaconda (base) environment has a large number of packages.

<img src='images_pycharm/img_011.png' alt='img_011' width='450'/>

## The Welcome Script

A welcome script displays by default. To simply it create a script that has:

```
identifiers = dir()
print(identifiers)
```

Notice the data model identifiers ```__name__``` and ```__file__``` which are included in every Python module.


<img src='images_pycharm/img_012.png' alt='img_012' width='450'/>

```__name__``` and ```__file__``` are the name of the script file and the location of the file in Windows Explorer. These can be printed and display in the console:

```
print(__name__)
print(__file__)
```

Notice the name is ```'__main__'``` and not ```main``` which is the file name:


<img src='images_pycharm/img_013.png' alt='img_013' width='450'/>

If a new script file is created by right clicking in the project file explorer and selecting New → Python File:

<img src='images_pycharm/img_014.png' alt='img_014' width='450'/>

And called ```script.py```:

<img src='images_pycharm/img_015.png' alt='img_015' width='450'/>

The same code can be added:

```
print(__name__)
print(__file__)
```

<img src='images_pycharm/img_016.png' alt='img_016' width='450'/>

If this script file is ran directly. Notice the file location has changed and points to ```script.py```. name has not changed and is still ```'__main__'``` and not ```script```.

If the code is modified so the ```main.py``` module is imported:

```
print('Code from this module:')
print(__name__)
print(__file__)
print('Imported module:')
import main
```

<img src='images_pycharm/img_017.png' alt='img_017' width='450'/>

Notice that the name of the module executed directly is ```'__main__'``` and the name of the module imported is ```'main'```. In other words the module executed directly is always called ```'main'``` and the modules imported use the file name of the module. 

Essentially the following:

```
if __name__ == '__main__':
    print(f'file {__file__} executed directly and named {__name__}')
else:
    print(f'file {__file__} imported as {__name__}')
```

is a check to see if the module is executed directly or imported. Sometimes additional diagnostic code is added when a script file is executed directly.

<img src='images_pycharm/img_018.png' alt='img_018' width='450'/>

<img src='images_pycharm/img_019.png' alt='img_019' width='450'/>

## Code Completion

PyCharm has indexed all the libraries in the (base) Python Environment and uses this indexed information for code completion.

Inputting p shows a list of all the identifiers beginning with the prefix p:

<img src='images_pycharm/img_020.png' alt='img_020' width='450'/>

All the ```builtins``` identifiers can be examined by inputting the prefix ```__builtins__.```:

<img src='images_pycharm/img_021.png' alt='img_021' width='450'/>

A one-line docstring displays when a function or class is input with open parenthesis:

<img src='images_pycharm/img_022.png' alt='img_022' width='450'/>

Pressing ```Ctrl```+```q``` will display a more detailed docstring as a pop up balloon:

<img src='images_pycharm/img_023.png' alt='img_023' width='450'/>

Code completion works for the numpy library and all other third-party libraries in the (base) Python environment as its contents have been indexed.

## Debugger and Variables

The following variables can be instantiated in a Python Script:

```
string = 'hello'
bytestring = b'hello'
bytearraystring = bytearray(b'hello')
integer = 1
floatingpointnum = 3.14
boolean = True
archive = (string, string, integers, floatingpointnum)
active = [string, string, integers, floatingpointnum]
unique = {string, string, integers, floatingpointnum}
mapping = {'r': 'red', 'g': 'green', 'b': 'blue'}
print()
```

PyCharm does not show Variables outwith the debugger. A breakpoint can be added to line number 1 and another breakpoint can be added to line number 11 (the debug point is up to but not including this line). The file can be debugged using the debug button:

<img src='images_pycharm/img_024.png' alt='img_024' width='450'/>

Threads & Variables can be selected. The script data model attributes display as special variables:

<img src='images_pycharm/img_025.png' alt='img_025' width='450'/>

If resume program is selected the builtins instances instantiated in the script will display as variables:

<img src='images_pycharm/img_026.png' alt='img_026' width='450'/>

A collection such as the list active can be expanded to view its elements in more detail:

<img src='images_pycharm/img_027.png' alt='img_027' width='450'/>

The dictionary mapping can also be expanded to view its elements in more detail:

<img src='images_pycharm/img_028.png' alt='img_028' width='450'/>

This also works for instances of classes in the third-party data science libraries:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Note when data science libraries are imported but not used they are greyed out:

<img src='images_pycharm/img_029.png' alt='img_029' width='450'/>

Identifiers show from the numpy library:

<img src='images_pycharm/img_030.png' alt='img_030' width='450'/>

Notice that because both numpy and pandas are used they are no longer greyed out:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

df = pd.DataFrame({'x': x,
                   'y': y})
```

<img src='images_pycharm/img_031.png' alt='img_031' width='450'/>

## Reformatting File

If the code is deliberately made sloppy in violation of PEP8:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y=np.array([2,4,6,8,10])

df = pd.DataFrame({'x':x,'y': y})
```

<img src='images_pycharm/img_032.png' alt='img_032' width='450'/>

The script file can be right clicked and Reformat Code selected:

<img src='images_pycharm/img_033.png' alt='img_033' width='450'/>

Select OK:

<img src='images_pycharm/img_034.png' alt='img_034' width='450'/>

Notice now that the spacing is automatically adjusted using autopep8:

<img src='images_pycharm/img_035.png' alt='img_035' width='450'/>

## Debugger and Variables Continued

The file can be debugged using the debug button:

<img src='images_pycharm/img_036.png' alt='img_036' width='450'/>

The array and the DataFrame instance can be viewed in more detail:

<img src='images_pycharm/img_037.png' alt='img_037' width='450'/>
<img src='images_pycharm/img_038.png' alt='img_038' width='450'/>
<img src='images_pycharm/img_039.png' alt='img_039' width='450'/>

## Plots

In PyCharm plots show as interactive windows. Plots only display when the script is run and not when the script is debugged:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

df = pd.DataFrame({'x': x,
                   'y': y})

plt.plot(df['x'], df['y'])
plt.show()
```

<img src='images_pycharm/img_040.png' alt='img_040' width='450'/>

[Return to Anaconda Tutorial](./readme.md)