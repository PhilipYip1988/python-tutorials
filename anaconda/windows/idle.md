# IDLE

IDLE is an abbreviation for the **i**ntegrated **d**evelopment **l**earner **e**nvironment. 

IDLE is a preinstalled Python IDE that is written using the Python standard library tkinter. tkinter is a Python standard library which is used for graphical user interfaces.

## IDLE Shell

The IDLE Shell can be launched from the Anaconda PowerShell Prompt using the PowerShell command:

```
idle
```

<img src='images_idle/img_001.png' alt='img_001' width='450'/>

The IDLE Shell looks similar to a PowerShell Prompt running Python and can be used to input Python code:

<img src='images_idle/img_002.png' alt='img_002' width='450'/>

Notice that when IDLE is launched, the Anaconda PowerShell Prompt will be busy. Essentially a while loop is running in the Anaconda PowerShell Prompt to keep idle open. It will remain busy until IDLE is closed:

<img src='images_idle/img_003.png' alt='img_003' width='450'/>

## Code Completion and Docstrings

If ```p``` is input followed by a ```↹```, a list of Python builtins identifiers displays:

<img src='images_idle/img_004.png' alt='img_004' width='450'/>

And if a function is input with open parenthesis for example ```print(``` a docstring will display:

<img src='images_idle/img_005.png' alt='img_005' width='450'/>

If a Python standard module is imported such as:

```
import builtins
```

And if ```builtins.``` is input followed by a ```↹```, a list of Python identifiers from that module displays:

<img src='images_idle/img_006.png' alt='img_006' width='450'/>

If the following object instance is instantiated:

```
obj1 = object()
```

Inputting ```obj1.``` followed by a ```↹```, shows a list of Python object based data model identifiers:

<img src='images_idle/img_007.png' alt='img_007' width='450'/>

If the following string instance is instantiated:

```
str1 = 'hello'
```

Inputting ```str1.``` followed by a ```↹```, shows a list of Python str identifiers:

<img src='images_idle/img_008.png' alt='img_008' width='450'/>

Inputting ```str1._``` followed by a ```↹```, shows a list of Python object based data model identifiers that the str class also has:

<img src='images_idle/img_009.png' alt='img_009' width='450'/>

If a third-party data science library such as numpy is imported using the alias np:

```
import numpy as np
```

Inputting ```np.``` followed by a ```↹```, shows a list of identifiers from the numpy library:

<img src='images_idle/img_010.png' alt='img_010' width='450'/>

## IDLE Doc

The IDLE Doc is essentially an equivalent to Notepad that shows code completion.

To open IDLE Doc, select File → New File in the IDLE Shell:

<img src='images_idle/img_011.png' alt='img_011' width='450'/>

This will open up IDLE Doc in a seperate Window. Select File → Save As...

<img src='images_idle/img_012.png' alt='img_012' width='450'/>

Then save the file as a Python Script file (.py file extension):

<img src='images_idle/img_013.png' alt='img_013' width='450'/>

Code completion will now work in a similar manner to seen in the IDLE Shell:

<img src='images_idle/img_014.png' alt='img_014' width='450'/>

<img src='images_idle/img_015.png' alt='img_015' width='450'/>

<img src='images_idle/img_016.png' alt='img_016' width='450'/>

<img src='images_idle/img_017.png' alt='img_017' width='450'/>

Code completion with the IDLE Doc will only work with third-party libraries and instances of classes from third-party libraries if they are previously imported in the IDLE Shell. If a script file includes

```
import numpy as np
```

And ```np.``` is input followed by a ```↹``` the completions display:

<img src='images_idle/img_019.png' alt='img_019' width='450'/>

If the same is done with pandas which is imported in the script file but not in the Shell, inputting ```pd.``` followed by a ```↹``` does not display any identifiers:

<img src='images_idle/img_020.png' alt='img_020' width='450'/>

Importing pandas in the Shell:

<img src='images_idle/img_021.png' alt='img_021' width='450'/>

Now allows identifiers to display in the script editor:

<img src='images_idle/img_022.png' alt='img_022' width='450'/>

<img src='images_idle/img_023.png' alt='img_023' width='450'/>

A simple script file:

```
print('Hello World!')
```

can be created:

<img src='images_idle/img_024.png' alt='img_024' width='450'/>

It can be run by selecting, run → run module:

<img src='images_idle/img_025.png' alt='img_025' width='450'/>

The print statement created in the script file will now be seen in the Shell:

<img src='images_idle/img_026.png' alt='img_026' width='450'/>

A script file which uses the data science libraries can be created:

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

<img src='images_idle/img_027.png' alt='img_027' width='450'/>

This script file can be run:

<img src='images_idle/img_028.png' alt='img_028' width='450'/>

IDLE uses the TkAgg backend for Matplotlib and the plot displays in a seperate window. The console will remain busy until the plot is closed:

<img src='images_idle/img_029.png' alt='img_029' width='450'/>

When IDLE is closed, the Anaconda PowerShell Prompt will no longer be busy and a new Prompt will appear:

<img src='images_idle/img_030.png' alt='img_030' width='450'/>

[Return to Anaconda Tutorial](./readme.md)