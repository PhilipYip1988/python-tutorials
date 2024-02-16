# Spyder

Spyder is an abbreviation for the **S**cientific **Py**thon **D**evelopment **E**nvi**r**onment and is a Python IDE similar to MATLAB or R-Studio.

## Launching Spyder

Spyder is preinstalled in the Anaconda (base) Python environment. To launch it use the start menu shortcut, the Spyder tile in the Anaconda Navigator or inputting:

```
spyder
```

in the Anaconda PowerShell Prompt:

<img src='images_spyder/img_001.png' alt='img_001' width='450'/>

## Customisation

Spyder will display using the dark theme by default. On systems with High DPI Screens, the buttons may also appear tiny as High DPI Scaling is not enabled by default. To change these settings select Tools → Preferences:

<img src='images_spyder/img_002.png' alt='img_002' width='450'/>

Select Application and Enable Auto high DPI scaling:

<img src='images_spyder/img_003.png' alt='img_003' width='450'/>

Select Appearance and the Spyder Syntax Highlighting Theme:

<img src='images_spyder/img_004.png' alt='img_004' width='450'/>

In Editor select Show blank spaces and indent guides:

<img src='images_spyder/img_005.png' alt='img_005' width='450'/>

Select Apply and restart Spyder when prompted:

<img src='images_spyder/img_006.png' alt='img_006' width='450'/>

## Script Editor

To the left is the script editor. To save the current script select File → Save As... navigate to Documents and save the script file with a .py file extension:

<img src='images_spyder/img_007.png' alt='img_007' width='450'/>

## Code Completion and Help Pane

Spyder should show code completions as a popup balloon in the scropt editor as you type. These can be selected using the arrow keys. When a function is selected its docstring will display:

<img src='images_spyder/img_008.png' alt='img_008' width='450'/>

If an identifier is input and right clicked, it can be inspected:

<img src='images_spyder/img_009.png' alt='img_009' width='450'/>

This displays its documentation in the Help pane:

<img src='images_spyder/img_010.png' alt='img_010' width='450'/>

Pressing ```Ctrl```+```i``` will inspect an object opening its help in the help pane.

Code completion works for most identifiers in standard libraries:

<img src='images_spyder/img_011.png' alt='img_011' width='450'/>

The identifier datetime has some issues, likely there is confusion between the datetime module and the datetime class in the datetime module.

And third-party data science libraries:

<img src='images_spyder/img_012.png' alt='img_012' width='450'/>

<img src='images_spyder/img_013.png' alt='img_013' width='450'/>

<img src='images_spyder/img_014.png' alt='img_014' width='450'/>

<img src='images_spyder/img_015.png' alt='img_015' width='450'/>

## Files

The File Panes shows the current working directory which is %USERPROFILE% by default. 

The script file in %USERPROFILE%\Documents can be run:

<img src='images_spyder/img_016.png' alt='img_016' width='450'/>

Using the default Run settings:

<img src='images_spyder/img_017.png' alt='img_017' width='350'/>

The print statement from the script file will display in the Console. Notice also that the current working directory will be changed to the location of the script file:

<img src='images_spyder/img_018.png' alt='img_018' width='450'/>

## Variable Explorer

Spyder has a very powerful Variable Explorer, some Python test code can be added to the script and it can be run:

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

<img src='images_spyder/img_019.png' alt='img_019' width='450'/>

The Variable Explorer can be undocked and view in more detail. Notice each Variable is color-coded in accordance to its datatype:

<img src='images_spyder/img_020.png' alt='img_020' width='450'/>

Unlike Variables in Thonny which are static. The Variables in Spyder can be used to examine the data structures in more detail. This is particularly useful for the immutable tuple, because this collection consists of immutable references they are greyed out:

<img src='images_spyder/img_021.png' alt='img_021' width='350'/>

And mutable list which is color-coded by the object that the reference leads to:

<img src='images_spyder/img_022.png' alt='img_022' width='350'/>

The mutable dict is color-coded by the object that the mapping leads to for each key. Unfortunately at present the items are ordered alphabetically by the key instead of the insertion order which is the way a mapping is ordered:

<img src='images_spyder/img_023.png' alt='img_023' width='350'/>

Some of the less commonly used classes such as the bytearray class just display as bytearray object instead of using the repr for that bytearray object.

If Consoles → Restart Kernel is selected:

<img src='images_spyder/img_024.png' alt='img_024' width='450'/>

All Variables and any library imports should be removed. In this version of Spyder sometimes the Variables don't refresh after restarting the kernel, undocking and docking the Variable Explorer refreshes the Variable Explorer and old variables are removed:

<img src='images_spyder/img_025.png' alt='img_025' width='450'/>

The Variable Explorer also supports Variables from the commonly used third-party data science libraries. If the following code is run:

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

<img src='images_spyder/img_026.png' alt='img_026' width='450'/>

The ndarray instance can be explored:

<img src='images_spyder/img_027.png' alt='img_027' width='350'/>

Alongside the DataFrame instance:

<img src='images_spyder/img_028.png' alt='img_028' width='350'/>

## Plots

Plots are shown as static images in the plots pane by default:

<img src='images_spyder/img_029.png' alt='img_029' width='450'/>

The backend for matplotlib can be changed for example to the gui library pyqt5 using tools → preferences:

<img src='images_spyder/img_030.png' alt='img_030' width='450'/>

Then IPyhon console, graphics and then changing the backend:

<img src='images_spyder/img_031.png' alt='img_031' width='450'/>

The Kernel needs to be restarted by going to Console → Restart Kernel.

The plot now displays in a seperate window as an interactive plot:

<img src='images_spyder/img_032.png' alt='img_032' width='450'/>

Support for using ipython magics in the ipython console to change the plot backend is added in Spyder 6 which is currently in the alpha stage.

## Selection and Code Blocks

So far the Run button has been used to run a script file. Spyder also has the ability to run a selection:

<img src='images_spyder/img_033.png' alt='img_033' width='450'/>

In Python beginning a line with ```#``` begins a comment. Using ```#%%``` indicates the creation of a new cell. The run cell button will run the code in the cell. Notice the same cell is highlighted after this button is pressed:

<img src='images_spyder/img_034.png' alt='img_034' width='450'/>

The run cell and move onto the next cell button button can be pressed to run each cell, cell by cell:

<img src='images_spyder/img_035.png' alt='img_035' width='450'/>

## Code Analysis and Debugger

If the first three lines are selected and then the edit menu and Comment/Uncomment is selected:

<img src='images_spyder/img_036.png' alt='img_036' width='450'/>

Notice the warnings display at each line on the script editor:

<img src='images_spyder/img_037.png' alt='img_037' width='450'/>

<img src='images_spyder/img_038.png' alt='img_038' width='450'/>

If these are fixed and another mistake is made suc as the exclusion of one of the brackets, another warning displays:

<img src='images_spyder/img_039.png' alt='img_039' width='450'/>

Spyder has an inbuilt debugger. In the script editor breakpoints can be added beside line numbers. The file can be debugged instead of run:

<img src='images_spyder/img_040.png' alt='img_040' width='450'/>

Each line can be run using run current line:

<img src='images_spyder/img_041.png' alt='img_041' width='450'/>

Notice the variable explorer shows the global scope and the variables a and b display after running these two lines line:

<img src='images_spyder/img_042.png' alt='img_042' width='450'/>

When the function is defined, it is accessible in the global scope but does not display on the variable explorer.

In the following line, the function is called. To debug the code in more detail, the function can be stepped into using the step into function or method of the current line button:

<img src='images_spyder/img_043.png' alt='img_043' width='450'/>

The code in the function can then be run line by line. Notice the local scope of the function has variables a and b which have the values 3 and 4 and these are displayed in the Variable Explorer:

<img src='images_spyder/img_044.png' alt='img_044' width='450'/>

c is instantiated in the global scope of the function and shows in the variable explorer:

<img src='images_spyder/img_045.png' alt='img_045' width='450'/>

The function can be run until it returns using the run until the current function of method returns button:

<img src='images_spyder/img_046.png' alt='img_046' width='450'/>

Or the code can be run until the next breakpoint using the continue execution until next breakpoint button:

<img src='images_spyder/img_047.png' alt='img_047' width='450'/>

Notice that the value of c is returned to the global scope but not assigned to a variable name in the global scope:

<img src='images_spyder/img_048.png' alt='img_048' width='450'/>

Now that the functions local scope is exited, the variables a and b from the global scope display on the Variable Explorer:

[Return to Anaconda Tutorial](./readme.md)
