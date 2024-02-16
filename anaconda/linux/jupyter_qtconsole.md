# Jupyter QtConsole

Jupyter QtConsole is very similar to ipython and is Shell based. It can be launched from its tile in the Anaconda Navigator or from the Linux Terminal using the bash command:

```
jupyter qtconsole
```

<img src='images_jupyter_qtconsole/img_001.png' alt='img_001' width='450'/>

QtConsole is written in Qt which is a C++ library for graphical user interfaces (GUI) and Pyside/PyQt are Python libraries that are bindings for Qt. While the QtConsole is open, the Linux Terminal will be busy. In the base Python environment, there is a LibGL mesa iris driver error due to the use of older drivers than Wayland on Ubuntu 23.04:

<img src='images_jupyter_qtconsole/img_002.png' alt='img_002' width='450'/>

QtConsole looks like the Terminal:

<img src='images_jupyter_qtconsole/img_003.png' alt='img_003' width='450'/>

If ```__builtins.__``` is input followed by a ```↹``` all the identifiers from builtins are displayed:

<img src='images_jupyter_qtconsole/img_004.png' alt='img_004' width='450'/>

QtConsole will display the docstring of the initialisation signature of a class or the docstring of a functions when the class or function name are input with open parenthesis:

<img src='images_jupyter_qtconsole/img_005.png' alt='img_005' width='450'/>

<img src='images_jupyter_qtconsole/img_006.png' alt='img_006' width='450'/>

QtConsole has ipython magics. These can be viewed by inputting a ```%``` followed by a ```↹``` will display all the ipython magics:

<img src='images_jupyter_qtconsole/img_007.png' alt='img_007' width='450'/>

Multiple lines can be input in an ipython cell by ending a line with ```Ctrl```+```↵``` instead of ```↵``` which executes the code in the ipython cell. This allows the three data science library imports in a single cell:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

The docstrings display for functions and classes found in these data science libraries:

<img src='images_jupyter_qtconsole/img_008.png' alt='img_008' width='450'/>

<img src='images_jupyter_qtconsole/img_009.png' alt='img_009' width='450'/>

The followjgn instances can be instantiated:

```
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])

df = pd.DataFrame(['x': x, 'y': y])
```

QtConsole lacks a variable inspector or explorer like Thonny or Spyder. However the ipython cell can be used to view an existing variable:

```
x
```

```
df
```

<img src='images_jupyter_qtconsole/img_010.png' alt='img_010' width='450'/>

A plot can be made using the pyplot function plot, notice the docstring displays when this is input with open parenthesis:

<img src='images_jupyter_qtconsole/img_011.png' alt='img_011' width='450'/>

A simple plot can be made using:

```
plot(df['x'], df['y'])
```

Notice that the plot displays as a static image in an ipython cell. This is known as the inline plotting backend:

<img src='images_jupyter_qtconsole/img_012.png' alt='img_012' width='450'/>

A QTConsole session can be saved to HTML/XHTML allowing the code and output to be read (read only) in a browser:

<img src='images_jupyter_qtconsole/img_013.png' alt='img_013' width='450'/>

This session can be saved in Documents and opened:

<img src='images_jupyter_qtconsole/img_014.png' alt='img_014' width='300'/>

Each image can be saved as inline attachment or as an external attachment:

<img src='images_jupyter_qtconsole/img_015.png' alt='img_015' width='200'/>

The ipython.html file is created:

<img src='images_jupyter_qtconsole/img_016.png' alt='img_016' width='450'/>

In Gnome settings, the default browser can be selected. Normally a Chromium based browser gives best results:

<img src='images_jupyter_qtconsole/img_017.png' alt='img_017' width='250'/>

The file can be opened in the browser:

<img src='images_jupyter_qtconsole/img_018.png' alt='img_018' width='450'/>

<img src='images_jupyter_qtconsole/img_019.png' alt='img_019' width='450'/>

The QtConsole can be exited using the python function:

```
exit()
```

<img src='images_jupyter_qtconsole/img_020.png' alt='img_020' width='450'/>

Once QtConsole is closed, a new prompt displays in the Linux Terminal:

<img src='images_jupyter_qtconsole/img_021.png' alt='img_021' width='450'/>

[Return to Jupyter Tutorial](./jupyter.md)

[Return to Anaconda Tutorial](./readme.md)