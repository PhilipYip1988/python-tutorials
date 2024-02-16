# Jupyter Notebook

Jupyter QtConsole was seen to essentially be a variation of IPython that is written in Qt. The main advantages of Qt are the display of function docstrings as popup balloons and the nesting of plots in ipython cells. 

The IPython session of the Jupyter QTConsole can be saved to HTML and is read-only. Jupyter Notebook is a browser based equivalent that revolves around the concept of an interactive Python notebook (.ipynb). The ipynb has code cells and markdown cells. Code cells are essentially IPython cells.

## Launching Jupyter Notebook

Jupyter Notebook can be launched from the Linux Terminal using:

```
jupyter notebook
```

<img src='images_jupyter_notebook/img_001.png' alt='img_001' width='450'/>

The Linux Terminal runs a server in the background:

<img src='images_jupyter_notebook/img_002.png' alt='img_002' width='450'/>

This server should display visual elements in a new tab of the default browser. A files tab displays which is a browser based representation of file explorer. By default it is open in ```~``` which is the default folder. The Documents folder can be selected:

<img src='images_jupyter_notebook/img_003.png' alt='img_003' width='450'/>

## Text File

The New dropdown list can be used to create a new file for example a text file. Select New → Text File:

<img src='images_jupyter_notebook/img_004.png' alt='img_004' width='450'/>

This is called ```untitled.txt``` and can be renamed:

<img src='images_jupyter_notebook/img_005.png' alt='img_005' width='450'/>

For example to ```text.txt```:

<img src='images_jupyter_notebook/img_006.png' alt='img_006' width='450'/>

And text (without formatting) can be added to this:

<img src='images_jupyter_notebook/img_007.png' alt='img_007' width='450'/>

It can be saved using File → Save as...

<img src='images_jupyter_notebook/img_008.png' alt='img_008' width='450'/>


<img src='images_jupyter_notebook/img_009.png' alt='img_009' width='450'/>

## Markdown File

Jupyter Notebook has limited support for python script files (.py file extension) and markdown files (.md file extension) which are essentially text files (.txt file extension) which have a different file extension. 

To create a new markdown file, select New → Text File. Then rename the file and change the file extension to ```.md```:

<img src='images_jupyter_notebook/img_010.png' alt='img_010' width='450'/>

Text can be formatting using characters such as ```#```, ```*``` and ```~```. Jupyter Notebook will indicate the formatting changes but displays the file only in editting mode:

<img src='images_jupyter_notebook/img_011.png' alt='img_011' width='450'/>

Select File → Save:

<img src='images_jupyter_notebook/img_012.png' alt='img_012' width='450'/>

## Python Script File

To create a new python file, select New → Text File. Then rename the file and change the file extension to ```.py```:

<img src='images_jupyter_notebook/img_013.png' alt='img_013' width='450'/>

<img src='images_jupyter_notebook/img_014.png' alt='img_014' width='450'/>

Basic Python code can be added to the script such as:

```
print('Hello World!')
```

Jupyter Notebook will display syntax highlighting for Python code however will not display a list of Python identifiers or docstrings for Python functions as there is no ipython kernel being run in the background for the script file.

<img src='images_jupyter_notebook/img_015.png' alt='img_015' width='450'/>

Select File → Save:

<img src='images_jupyter_notebook/img_016.png' alt='img_016' width='450'/>

## Terminal

A browser based version of the Linux Terminal can be opened by selecting New → Terminal:

<img src='images_jupyter_notebook/img_017.png' alt='img_017' width='450'/>

The default location of the Terminal is ```~``` and can be changed to ```~/Documents``` using:

```
cd ~/Documents
```

<img src='images_jupyter_notebook/img_018.png' alt='img_018' width='450'/>

The python script can be launched by using:

```
python script.py
```

<img src='images_jupyter_notebook/img_019.png' alt='img_019' width='450'/>

<img src='images_jupyter_notebook/img_020.png' alt='img_020' width='450'/>

## Notebook

Select New → Python 3 (ipykernel):

<img src='images_jupyter_notebook/img_021.png' alt='img_021' width='450'/>

The notebook can be renamed:

<img src='images_jupyter_notebook/img_022.png' alt='img_022' width='450'/>

Using the ```.ipynb``` file extension:

<img src='images_jupyter_notebook/img_023.png' alt='img_023' width='450'/>

The following markdown and code cells can be added:

Markdown
```
# Notebook
```
Markdown
```
## Import Libraries
```
Code
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
Markdown
```
## Create Data
```
Code
```
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})
```
Markdown
```
## Plot Data
```
Code
```
plt.plot(df['x'], df['y'])
```

<img src='images_jupyter_notebook/img_024.png' alt='img_024' width='450'/>

Each of these cells is Run by pressing the Run button. 

Notice the markdown cells show the formatted markdown headings and the code cells are essentially ipython cells:

<img src='images_jupyter_notebook/img_025.png' alt='img_025' width='450'/>

<img src='images_jupyter_notebook/img_026.png' alt='img_026' width='450'/>

A list of identifiers can be viewed after a prefix by pressing ```↹```:

<img src='images_jupyter_notebook/img_027.png' alt='img_027' width='450'/>

The docstring of a function can be examined by typing in the function name with open parenthesis and pressing shift ```⇧``` and tab ```↹```:

<img src='images_jupyter_notebook/img_028.png' alt='img_028' width='450'/>

Jupyter Notebook has no Variable Inspector or Explorer like previously seen in Thonny and Spyder. The ipython cells are however useful for visualisation of individual variables:

```
x
```

```
df
```

<img src='images_jupyter_notebook/img_029.png' alt='img_029' width='450'/>

A docstring can be viewed in more detail by using ```?```:

```
? str
```

<img src='images_jupyter_notebook/img_030.png' alt='img_030' width='450'/>

The docstring displays in a pane at the bottom of the screen:

<img src='images_jupyter_notebook/img_031.png' alt='img_031' width='450'/>

This can be expanded to a new tab, however looses the syntax highlighting:

<img src='images_jupyter_notebook/img_032.png' alt='img_032' width='450'/>

## Kernel

When a Notebook is opened and closed, generally the Kernel needs to be Restarted. Select Restart & Clear Output:

<img src='images_jupyter_notebook/img_033.png' alt='img_033' width='450'/>

Select Restart & Clear All Outputs:

<img src='images_jupyter_notebook/img_034.png' alt='img_034' width='250'/>

## Shortcut Keys

A cell can be toggled between from Code (default) to Markdown using the shortcut keys ```Esc```+```m```. A cell can be toggled between from Markdown to Code using the shortcut keys ```Esc```+```y```:

<img src='images_jupyter_notebook/img_035.png' alt='img_035' width='450'/>

The keyboard shortcut ```⇧```+```↵``` will run a cell. The keyboard shortcut ```Alt```+```↵``` will run a cell and insert an empty cell below it.

The keyboard shortcut ```Ctrl```+```s``` can be used to save the Notebook:

<img src='images_jupyter_notebook/img_036.png' alt='img_036' width='450'/>

## Closing Jupyter Notebook

Close all tabs in the Chromium Browser:

<img src='images_jupyter_notebook/img_037.png' alt='img_037' width='450'/>

Although Jupyter Notebook is closed in the browser, the Jupyter Notebook server will continue to run in the Terminal. Press ```Ctrl```+```c``` to close the Terminal:

<img src='images_jupyter_notebook/img_038.png' alt='img_038' width='450'/>

The new Prompt displays in the Terminal:

<img src='images_jupyter_notebook/img_039.png' alt='img_039' width='450'/>

The files created in Jupyter Notebook can be seen in File Explorer. If these files are double clicked they will open in text editor. Usually Jupyter Notebook is relaunched and they are opened in Jupyter Notebook:

<img src='images_jupyter_notebook/img_040.png' alt='img_040' width='450'/>

[Return to Jupyter Tutorial](./jupyter.md)

[Return to Anaconda Tutorial](./readme.md)