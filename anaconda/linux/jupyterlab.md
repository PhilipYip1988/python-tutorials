# JupyterLab

JupyterLab is the next generation of Jupyter Notebook and has additional functionality. It was originally meant to supersede Jupyter Notebook however Jupyter Notebook continues to be relatively popular and therefore both products are maintained.

## Launching JupyterLab

JupyterLab can be launched using its tile in the Anaconda Navigator or using the bash command:

```
jupyter lab
```

<img src='images_jupyterlab/img_001.png' alt='img_001' width='450'/>

The Terminal runs a Jupyter server:

<img src='images_jupyterlab/img_002.png' alt='img_002' width='450'/>

And JupyterLab opens in a new tab in the default browser, in this case Chromium:

<img src='images_jupyterlab/img_003.png' alt='img_003' width='450'/>

To the left is the navigation pane, a browser based version of file explorer. To the right is a launcher. The launcher has tiles which create a new:

* Text File
* Markdown File
* Python File
* bash Terminal
* IPython Terminal
* Notebook

## Text File

In the current location selected from the navigation pane. If the Documents folder is selected:

<img src='images_jupyterlab/img_004.png' alt='img_004' width='450'/>

The text file created earlier using Jupyter Notebook can be examined:

<img src='images_jupyterlab/img_005.png' alt='img_005' width='450'/>

## Markdown File

The markdown file created in Jupyter Notebook can be examined. JupyterLab has the option to Show the Markdown Preview:

<img src='images_jupyterlab/img_006.png' alt='img_006' width='450'/>

This is displayed in a seperate tab which can be snapped to the right. JupyterLab also has a table of contents tab within the navigation pane. This table of contents uses the headings in the navigation pane:

<img src='images_jupyterlab/img_007.png' alt='img_007' width='450'/>

Unfortunately at present the table of contents does not work with both the markdown and mardown preview, acting only on the last selected tab.

## Python Script

When a Python script file is opened, Python syntax highlighting but no code completions or docstrings display. For the latter a new Console can be opened for the Editor. Right click the Editor and select Create Console for Editor:

<img src='images_jupyterlab/img_008.png' alt='img_008' width='450'/>

Select Python3:

<img src='images_jupyterlab/img_009.png' alt='img_009' width='150'/>

Now a list of identifiers will display from a prefix when a ```↹``` is pressed. There are improvements in JupyterLab over other IDEs as identifiers are colour-coded by type making it easier to distinguish a function and an object:

<img src='images_jupyterlab/img_010.png' alt='img_010' width='450'/>

Docstrings display for a funcion, when the functions name followed by open parenthesis and ```⇧``` + ```↹``` are pressed:

<img src='images_jupyterlab/img_011.png' alt='img_011' width='450'/>

Code completion is dependent on the ipython console, no identifiers from an imported third-party library will display:

<img src='images_jupyterlab/img_012.png' alt='img_012' width='450'/>

However they will display for an imported Python standard module:

<img src='images_jupyterlab/img_013.png' alt='img_013' width='450'/>

Code from the script can be highlighted and Run → Run Code can be selected. Alternatively all the code in the script file can be run by selecting Run → Run All Code:

<img src='images_jupyterlab/img_014.png' alt='img_014' width='450'/>

<img src='images_jupyterlab/img_015.png' alt='img_015' width='450'/>

<img src='images_jupyterlab/img_016.png' alt='img_016' width='450'/>

Code completion and function docstrings should now display both in the script and in an ipython cell. For JupyterLab3 this is more reliable in the ipython cell:

<img src='images_jupyterlab/img_017.png' alt='img_017' width='450'/>

The following code can be input:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})

plt.plot(df['x'], df['y'])
```

<img src='images_jupyterlab/img_018.png' alt='img_018' width='450'/>

All this code can be run:

<img src='images_jupyterlab/img_019.png' alt='img_019' width='450'/>

Which displays the plot in the ipython cell output:

<img src='images_jupyterlab/img_020.png' alt='img_020' width='450'/>

JupyterLab by default has no Variable Inspector or Explorer equivalent to those seen in Thonny and Spyder. Variables can be viewed in more detail using the ipython cell output.

A third-party Variable Inspector is available but generally this should be installed using a seperate Python environment from conda-forge:

<img src='images_jupyterlab/img_021.png' alt='img_021' width='450'/>

Docstrings can be examined in a cell output using ```?```:

<img src='images_jupyterlab/img_022.png' alt='img_022' width='450'/>

## Terminal

The pyplot show function has to be added to the script for the plot to display when the script is ran from the Linux Terminal:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})

plt.plot(df['x'], df['y'])
plt.show()
```

<img src='images_jupyterlab/img_023.png' alt='img_023' width='450'/>

If a new launcher is opened by pressing the ```+``` button on the navigation pane, the Terminal tile can be used to open a browser based terminal. The Terminal will use te current working directory of the file explorer on the navigation pane when launched. The python script file can therefore be run using:

```
python script.py
```

<img src='images_jupyterlab/img_024.png' alt='img_024' width='450'/>

## Notebook

The notebook created in Jupyter Notebook can be opened in JupyterLab. A cell can be toggled between from Code (default) to Markdown using the shortcut keys ```Esc```+```m```. A cell can be toggled between from Markdown to Code using the shortcut keys ```Esc```+```y```:

<img src='images_jupyterlab/img_025.png' alt='img_025' width='450'/>

The table of contents in the navigation pane works with any markdown headings in the notebook:

<img src='images_jupyterlab/img_026.png' alt='img_026' width='450'/>

The cell output of an ipython cell can be used to view variables:

<img src='images_jupyterlab/img_027.png' alt='img_027' width='450'/>

A list of identifiers will display from a prefix when a ```↹``` is pressed. Identifiers are colour-coded by type making it easier to distinguish a function and an object:

<img src='images_jupyterlab/img_028.png' alt='img_028' width='450'/>

Docstrings display for a function, when the functions name followed by open parenthesis and ```⇧``` + ```↹``` are pressed:

<img src='images_jupyterlab/img_029.png' alt='img_029' width='450'/>

Docstrings can also be displayed in an ipython cell output by use of ```?``` followed by the functions name. Instead of having a large cell output, the cell can be right clicked and Enabling Scrolling for Outputs can be selected:

<img src='images_jupyterlab/img_030.png' alt='img_030' width='450'/>

This allows the full output of a docstring for exmaple, without making it the primary focus of the notebook file:

<img src='images_jupyterlab/img_031.png' alt='img_031' width='450'/>

## Closing JupyterLab

JupyterLab can be closed by closing down the JupyterLab tabs in the default browser. The JupyterLab server will however remain active in the Linux Terminal:

<img src='images_jupyterlab/img_032.png' alt='img_032' width='450'/>

Press ```Ctrl```+```c``` to close then press ```y``` when prompted:

<img src='images_jupyterlab/img_033.png' alt='img_033' width='450'/>

A new prompt in the Linux Terminal will now display:

<img src='images_jupyterlab/img_034.png' alt='img_034' width='450'/>

[Return to Jupyter Tutorial](./jupyter.md)

[Return to Anaconda Tutorial](./readme.md)