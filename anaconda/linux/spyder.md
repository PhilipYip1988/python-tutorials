# Spyder

Spyder is an abbreviation for the **S**cientific **Py**thon **D**evelopment **E**nvi**r**onment and is a Python IDE similar to MATLAB or R-Studio.

## Launching Spyder

Spyder is preinstalled in the Anaconda (base) Python environment. To launch it use the Spyder tile in the Anaconda Navigator or input the following bash command:

```
spyder
```

<img src='images_spyder/img_001.png' alt='img_001' width='450'/>

## Spyder Preferences

Spyder will display using the dark theme by default. On systems with High DPI Screens, the buttons may also appear tiny as High DPI Scaling is not enabled by default. To change these settings select Tools → Preferences:

<img src='images_spyder/img_002.png' alt='img_002' width='450'/>

On a high DPI screen select Application and Enable Auto high DPI scaling:

<img src='images_spyder/img_003.png' alt='img_003' width='450'/>

Select Appearance and select the desired Syntax Highlighting Theme Spyder or Spyder Dark:

<img src='images_spyder/img_004.png' alt='img_004' width='450'/>

Once Apply is selected to one of the options above. Select Yes to restart Spyder and apply the changes:

<img src='images_spyder/img_005.png' alt='img_005' width='250'/>

Spyder will now launch with the syntax highlighting theme. select Tools → Preferences:

<img src='images_spyder/img_006.png' alt='img_006' width='450'/>

In Editor optionally select Show blank spaces and indent guides and select Apply:

<img src='images_spyder/img_007.png' alt='img_007' width='450'/>

## Script Editor

To the left is the script editor. To save the current script select File → Save As... 

<img src='images_spyder/img_008.png' alt='img_008' width='450'/>

Navigate to Documents and save the script file with a .py file extension:

<img src='images_spyder/img_009.png' alt='img_009' width='450'/>

## Code Completion and Help Pane

Spyder should show code completions as a popup balloon in the script editor as you type. These can be selected using the arrow keys:

<img src='images_spyder/img_010.png' alt='img_010' width='450'/>

When a function is selected its docstring will display:

<img src='images_spyder/img_011.png' alt='img_011' width='450'/>

If an identifier is input and right clicked, it can be inspected by using Inspect Current Object:

<img src='images_spyder/img_012.png' alt='img_012' width='450'/>

This displays its documentation in the Help pane:

<img src='images_spyder/img_013.png' alt='img_013' width='450'/>

## Console and Files

If the test code is addded to the script file:

```
print('Hello World!')
```

The File Panes shows the current working directory which is ```~``` by default.

The script file ```script.py``` in ```~/Documents``` can be run:

<img src='images_spyder/img_014.png' alt='img_014' width='450'/>

Select Run file with default configuration and then Run:

<img src='images_spyder/img_015.png' alt='img_015' width='300'/>

The print statement from the script file will display in the Console. Notice also that the current working directory will be changed to the location of the script file:

<img src='images_spyder/img_016.png' alt='img_016' width='450'/>

## Code Completion and Help Pane Continued

The code completion should work for Python standard libraries for example the datetime module. 

Unfortunately for the datetime module, there is some confusion between the datetime module and datetime class and the docstring doesn't display:

<img src='images_spyder/img_017.png' alt='img_017' width='450'/>

These can be distinguished using Inspect:

<img src='images_spyder/img_018.png' alt='img_018' width='450'/>

<img src='images_spyder/img_019.png' alt='img_019' width='450'/>

The docstring for the timedelta class in the datetime standard module does not have this confusion and is displayed as a popup balloon:

<img src='images_spyder/img_020.png' alt='img_020' width='450'/>

Identifiers also display for third-party data science libraries such as numpy, pandas and matplotlib:

<img src='images_spyder/img_021.png' alt='img_021' width='450'/>

And the docstrings for functions in these libraries show when the function is input with open parenthesis:

<img src='images_spyder/img_022.png' alt='img_022' width='450'/>

## Variable Explorer

Spyder has a very powerful Variable Explorer, some Python test code can be added to the script and it can be run:

```
string = 'hello'
bytestring = b'hello'
bytearraystring = bytearray(b'hello')
integer = 1
floatingpoint = 3.14
boolean = True
archive = (string, string, integer, floatingpoint)
active = [string, string, integer, floatingpoint]
unique = {string, string, integer, floatingpoint}
mapping = {'r': 'red', 'g': 'green', 'b': 'blue'}
```

The Variables display on the Variable Explorer:

<img src='images_spyder/img_023.png' alt='img_023' width='450'/>

Notice if an error is introduced such as an incomplete bracket or quotation, a warning will display beside the line number giving details about the error when highlighted. The syntax highlighting on the last line showing the closing bracket as part of the string can also be used to help identify the error.

Variables can be double clicked in the Variable Explorer. Supported collections can be viewed in more detail such as the tuple:

<img src='images_spyder/img_024.png' alt='img_024' width='250'/>

On GNOME, the titlebar of the window can be highlighted and Always on Top can be used:

<img src='images_spyder/img_025.png' alt='img_025' width='270'/>

The tuple is immutable and all its elements are greyed out. The list is mutatable and its elements can be modified:

<img src='images_spyder/img_026.png' alt='img_026' width='250'/>

The dict is also mutatable and has an index of keys opposed to a numeric index. This index displays the keys in alphabetical order opposed to the insertion order which is normally the default for a dict:

<img src='images_spyder/img_027.png' alt='img_027' width='250'/>

Some of the less commonly used classes such as the bytearray class just display as bytearray object instead of using the repr for that bytearray object.

## Restarting the Kernel

The Kernel can be restarted using Consoles → Restart Kernel:

<img src='images_spyder/img_028.png' alt='img_028' width='450'/>

Select Yes:

<img src='images_spyder/img_029.png' alt='img_029' width='200'/>

All variables instantiated will be removed from the Variable Explorer and all libraries imported will be closed:

<img src='images_spyder/img_030.png' alt='img_030' width='450'/>

## Run Selection and Run Cells

A selection in the Script can be highlighted and Run Selection can be selected:

<img src='images_spyder/img_032.png' alt='img_032' width='450'/>

<img src='images_spyder/img_033.png' alt='img_033' width='450'/>

In Python a line beginning with ```#``` is a comment and a line beginning with ```#%%``` is recognised in some IDEs such as Spyder as a new cell. The currently selected cell is highlighted in yellow. The Run current cell button can be selected:

<img src='images_spyder/img_034.png' alt='img_034' width='450'/>

<img src='images_spyder/img_035.png' alt='img_035' width='450'/>

Alternatively Run Cell and go to the next one can be selected:

<img src='images_spyder/img_036.png' alt='img_036' width='450'/>

<img src='images_spyder/img_037.png' alt='img_037' width='450'/>

Several lines of code can be highlighted:

<img src='images_spyder/img_038.png' alt='img_038' width='450'/>

And uncommented by going to Edit ```→``` Comment/Uncomment:

<img src='images_spyder/img_039.png' alt='img_039' width='450'/>

Notice later lines which were dependent on this code now display errors on the line number as they are referencing undefined objects:

<img src='images_spyder/img_040.png' alt='img_040' width='450'/>

## Plotting

The script can be updated to:

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

<img src='images_spyder/img_041.png' alt='img_041' width='450'/>

When the script is run, the Variables will be displayed on the Variable Explorer. 

<img src='images_spyder/img_042.png' alt='img_042' width='450'/>

Notice the array instance has a colormap which can be used to visualise the trend of the numeric data:

<img src='images_spyder/img_043.png' alt='img_043' width='250'/>

The DataFrame instance also has the same colormap:

<img src='images_spyder/img_045.png' alt='img_045' width='450'/>

The plot of this data is shown as a static image on the plots pane:

<img src='images_spyder/img_046.png' alt='img_046' width='450'/>

The backend for matplotlib can be changed for example to the gui library pyqt5 using tools → preferences:

<img src='images_spyder/img_047.png' alt='img_047' width='450'/>

Then IPython console, graphics and then changing the backend:

<img src='images_spyder/img_048.png' alt='img_048' width='300'/>

The Kernel needs to be restarted by going to Console → Restart Kernel.

<img src='images_spyder/img_049.png' alt='img_049' width='450'/>

When the Script is rerun, the plot displays interactively in its own window. Note this window does not hang the Console and can be kept open. A LibGL mesa iris driver error displays in the Consoles due to the use of older drivers in the base Python environment than Wayland on Ubuntu 23.04:

<img src='images_spyder/img_050.png' alt='img_050' width='450'/>

## Debugging

The Spyder IDE has a powerful debugger. If the following code is input in the Script Editor:

```
a = 1
b = 1

def fun(a, b):
    c = a + b
    return c

d = fun(3, 4)

print('End')
```

Breakpoints can be added on lines 1 and 10, this is inclusive of line 1 and up to and exclusive of line 10:

<img src='images_spyder/img_051.png' alt='img_051' width='450'/>

Debug file can be selected:

<img src='images_spyder/img_052.png' alt='img_052' width='450'/>

Run current line can be clicked repeatedly to run each line of code individually:

<img src='images_spyder/img_053.png' alt='img_053' width='450'/>

When clicked twice, the two variables are instantiated and display on the Variable Explorer:

<img src='images_spyder/img_054.png' alt='img_054' width='450'/>

When the function is defined, it does not display on the Variable Explorer but is available in the main script files name space:

<img src='images_spyder/img_055.png' alt='img_055' width='450'/>

Finally the function can be called and the result is returned to d:

<img src='images_spyder/img_056.png' alt='img_056' width='450'/>

If the kernel is restart and the debugger run line by line until the function call (line 8):

<img src='images_spyder/img_057.png' alt='img_057' width='450'/>

The function cn be stepped into:

<img src='images_spyder/img_058.png' alt='img_058' width='450'/>

This will show the local namespace of the function which has the local variables ```a = 3``` and ```b = 4``` opposed to the global variables ```a = 1``` and ```b = 1```:

<img src='images_spyder/img_059.png' alt='img_059' width='450'/>

The code within the function code block can then be run line by line:

<img src='images_spyder/img_060.png' alt='img_060' width='450'/>

<img src='images_spyder/img_061.png' alt='img_061' width='450'/>

Alternatively it can be run until the current function returns:

<img src='images_spyder/img_062.png' alt='img_062' width='450'/>

Which will return the value to the variable d in the main namespace:

<img src='images_spyder/img_063.png' alt='img_063' width='450'/>

If multiple breakpoints are added. The file can be debugged and can be run up to and excluding the line of the next breakpoint by using continue execution until the next breakpoint:

<img src='images_spyder/img_064.png' alt='img_064' width='450'/>

<img src='images_spyder/img_065.png' alt='img_065' width='450'/>

When Spyder is closed, a new prompt in the Terminal should display. If it does not it can be closed using ```Ctrl```+```c```:

<img src='images_spyder/img_066.png' alt='img_066' width='450'/>

[Return to Anaconda Tutorial](./readme.md)