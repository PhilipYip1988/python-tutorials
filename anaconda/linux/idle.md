# IDLE

IDLE is an abbreviation for the **i**ntegrated **d**evelopment **l**earner **e**nvironment. 

IDLE is a preinstalled Python IDE that is written using the Python standard library tkinter. tkinter is a Python standard library which is used for graphical user interfaces.

## IDLE Shell

In the ```anaconda3\bin``` there is a ```idle3``` and alias ```idle3.11``` program. The 3 was used to distinguish idle for Python 2 and idle for Python 3. 

Although Python 2 has reached end of life and therefore the alias ```python``` can be used for ```python3``` and ```python3.11```, at current there is no alias ```idle```:

<img src='images_idle/img_001.png' alt='img_001' width='450'/>


The IDLE Shell can be launched from the Linux Terminal using the bash command:

```
idle3
```

Or its alias:

```
idle3.11
```

<img src='images_idle/img_002.png' alt='img_002' width='450'/>

The terminal will be busy while idle is running:

<img src='images_idle/img_003.png' alt='img_003' width='450'/>

Notice the IDLE Shell looks similar to Python when it is ran directly in the Terminal and displays a similar Python Prompt ```>>>```. If text is input followed by a tab ```↹``` a list of identifiers displays:

<img src='images_idle/img_004.png' alt='img_004' width='450'/>

If a function is input with open parenthesis, the docstring displays as a popup balloon:

<img src='images_idle/img_005.png' alt='img_005' width='450'/>

To view all identifiers for the builtins module which are automatically imported, the builtins module can explicitly be imported:

```
import builtins
```

Then ```builtins.``` followed by a ```↹``` can be input. These identifiers are automatically in the scripts name space using the data model attribute duner builtins. Therefore ```__builtins__.``` followed by a ```↹``` can also be input:

<img src='images_idle/img_006.png' alt='img_006' width='450'/>

An object instance obj1 can be instantiated using:

```
obj1 = object()
```

The object based data model identifiers dunder identifiers can be viewed by inputting ```obj1.``` followed by a ```↹```:

<img src='images_idle/img_007.png' alt='img_007' width='450'/>

A str instance str1 can be instantiated using:

```
str1 = 'Hello World!'
```

The str identifiers can be viewed by inputting ```str1.``` followed by a ```↹```:

<img src='images_idle/img_008.png' alt='img_008' width='450'/>

The object based data model identifiers dunder identifiers are also present for a str instance and an instance of any other class and can be viewed by inputting ```str1._``` followed by a ```↹```:

<img src='images_idle/img_009.png' alt='img_009' width='450'/>

A third-party data science library such as numpy can be imported using:

```
import numpy as np
```

Identifiers from it can be seen by inputting ```np.``` followed by a ```↹```:

<img src='images_idle/img_010.png' alt='img_010' width='450'/>

Docstrings of numpy functions can be viewed as a popup balloon by inputting the function name with open parenthesis:

<img src='images_idle/img_011.png' alt='img_011' width='450'/>

## IDLE Doc

To open IDLE Doc, select File → New File in the IDLE Shell:

<img src='images_idle/img_012.png' alt='img_012' width='450'/>

This will open up IDLE Doc in a seperate Window. Select File → Save As...

<img src='images_idle/img_013.png' alt='img_013' width='450'/>

Then save the file as a Python Script file (.py file extension):

<img src='images_idle/img_014.png' alt='img_014' width='450'/>

Syntax highlighting will now be carried out in IDLE Doc.

Inputting ```p``` followed by a ```↹``` will display identifers from builtins with the prefix ```p```:

<img src='images_idle/img_015.png' alt='img_015' width='450'/>

And if one of the builtins functions is input with open parenthesis, its docstring will display as a popup balloon:

<img src='images_idle/img_016.png' alt='img_016' width='450'/>

If an object instance is created in the script for example:

```
obj2 = object()
```

Notice no identifiers display.

<img src='images_idle/img_017.png' alt='img_017' width='450'/>

If an object instance is created in the script for example:

```
obj1 = object()
```

Notice identifiers display, this is because the code completions are reliant on the IDLE Shell. obj1 is instantiated in the IDLE Shell while obj2 is not instantiated in the IDLE Shell which is why identifiers display for the former and not the latter:

<img src='images_idle/img_018.png' alt='img_018' width='450'/>

A script file, also known as a module can be ran in the IDLE Shell:

```
print('Hello World!')
```

<img src='images_idle/img_019.png' alt='img_019' width='450'/>

By selecting Run → Run Module:

<img src='images_idle/img_020.png' alt='img_020' width='450'/>

Notice the print statement displays in the IDLE Shell:

<img src='images_idle/img_021.png' alt='img_021' width='450'/>

Test code to import the data science libraries, create data structures and plot a graph can be input into the Python script:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x),
                   'y': y})

plt.plot(df['x'], df['y'])
plt.show()
```

<img src='images_idle/img_022.png' alt='img_022' width='450'/>

This module can be ran by selecting Run → Run Module:

<img src='images_idle/img_023.png' alt='img_023' width='450'/>

The plot will be displayed using the TkAgg interactive backend and the IDLE Shell will hang so long as the plot is open:

<img src='images_idle/img_024.png' alt='img_024' width='450'/>

Closing the plot will free up the IDLE Shell which will now display a new prompt:

<img src='images_idle/img_025.png' alt='img_025' width='450'/>

Closing the IDLE shell will in turn free up the Terminal which will also display a new prompt:

<img src='images_idle/img_026.png' alt='img_026' width='450'/>

[Return to Anaconda Tutorial](./readme.md)