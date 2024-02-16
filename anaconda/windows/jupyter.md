# Jupyter

Previously interactive Python ipython was examined and seen to contain Python code in addition to the bash based ipython magics. In addition ipython was seen to carry out syntax highlighting for Python code. The Jupyter project is a loose acronym for three programming languages **Ju**lia, **Pyt**hon and **R**, although this guide will only focus on Python where it is most commonly used. For Python, Jupyter essentially is an ecosystem around ipython. There are four versions:

* Jupyter Console
* Jupyter QTConsole
* Jupyter Notebook
* JupyterLab

## Jupyter QTConsole

Jupyter QTConsole is very similar to ipython and is Shell based. It can be launched from its tile in the Anaconda Navigator or from the Anaconda PowerShell Prompt using the PowerShell command:

```
jupyter-qtconsole
```

<img src='images_jupyter/img_001.png' alt='img_001' width='450'/>

The main difference between Jupyter QTconsole and ipython is how graphics are handled. Notice that the following matplotlib plot is nested as a static image in an ipython cell output instead of plotted in a seperate window using a GUI backend:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})
plt.plot(df['x'], df['y'])
```

<img src='images_jupyter/img_002.png' alt='img_002' width='450'/>

The Anaconda PowerShell Prompt will be busy while the Jupyter QTConsole is running in a seperate Shell. When the Jupyter QTConsole is closed, the next prompt in the Anaconda PowerShell Prompt will be available:

<img src='images_jupyter/img_003.png' alt='img_003' width='450'/>

## Jupyter Notebook

Jupyter Notebook is a browser based application that revolves mainly around an **in**teractive **Py**thon **n**ote**b**ook (.ipynb file extension).

Jupyter notebook can be launched by using its tile on the Anaconda Navigator, its shortcut in the start menu or by inputting the following in the Anaconda PowerShell Prompt:

```
jupyter notebook
```

<img src='images_jupyter/img_004.png' alt='img_004' width='450'/>

Jupyter Notebook opens in the default browser. A browser based file explorer displays opening by default in %USERPROFILE%:

<img src='images_jupyter/img_005.png' alt='img_005' width='450'/>

Navigate to Documents:

<img src='images_jupyter/img_006.png' alt='img_006' width='450'/>

Use new to create a new text file:

<img src='images_jupyter/img_007.png' alt='img_007' width='450'/>

A Python file is a text file which has a different file extension. The file above can be renamed:

<img src='images_jupyter/img_008.png' alt='img_008' width='450'/>

Changing the .txt extension to the .py file extension:

<img src='images_jupyter/img_009.png' alt='img_009' width='450'/>

Once the file extension is correct, syntax highlighting for Python code is applied:

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

Unfortunately when using Jupyter Notebook as a script editor there is no code completion as no Python interpretter is running in the background. 

The file should be saved using the file menu:

<img src='images_jupyter/img_010.png' alt='img_010' width='450'/>

A PowerShell Terminal can be opened in Jupyter Notebook by selecting New → Terminal:

<img src='images_jupyter/img_011.png' alt='img_011' width='450'/>

Because the file location was in Documents, the Terminal opens in the Documents folder. The PowerShell command can be used to execute the Python script file using:

```
python script.py
```

<img src='images_jupyter/img_012.png' alt='img_012' width='450'/>

The plot opens in a seperate window, using the TkAgg GUI Backend:

<img src='images_jupyter/img_013.png' alt='img_013' width='450'/>

A **m**ark**d**own file is a text file with a .md file extension. Unlike a text file which has no formatting, a markdown file allows basic formatting using the characters #, * and ~ for example:  

```
# Title (H1)
## Section (H2)

The *quick* **brown** ***fox*** ~~jumped~~ over the lazy dog.
```

Jupyter Notebook will modify the markdown text but not display a full formatted output:

<img src='images_jupyter/img_014.png' alt='img_014' width='450'/>

The main strength of Jupyter Notebook is an interactive Python notebook. Select new Python 3 (ipykernel):

<img src='images_jupyter/img_015.png' alt='img_015' width='450'/>

A notebook file consists of cells; code cells and markdown cells:

<img src='images_jupyter/img_016.png' alt='img_016' width='450'/>

The following markdown and code cells can be added:

```
# Notebook
```

```
## Import Libraries
```

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

```
## Create Data
```

```
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})
```

```
## Plot Data
```

```
plt.plot(df['x'], df['y'])
```

<img src='images_jupyter/img_017.png' alt='img_017' width='450'/>

Each Markdown Cell when run, displays the fully formatted output when run. Running a Python cell is essentially equivalent to running an ipython cell, notice the numeric value of the prompt displays beside each code cell. 

<img src='images_jupyter/img_018.png' alt='img_018' width='450'/>

The notebook file should be renamed and saved:

<img src='images_jupyter/img_019.png' alt='img_019' width='450'/>

Jupyter Notebook unfortunately has no Variable Inspector/Explorer however the cell output can be quite powerful when it comes to visualising variables:

```
df
```

<img src='images_jupyter/img_020.png' alt='img_020' width='450'/>

The plots are nested as static images in the cell output as seen when using the QTConsole.

A list of identifiers can be seen after inputting a ```↹``` after a prefix in a code cell:

<img src='images_jupyter/img_021.png' alt='img_021' width='450'/>

Docstrings can be seen as a popup balloon by typing in a function with open parenthesis followed by a ```⇧```+```↹```:

<img src='images_jupyter/img_022.png' alt='img_022' width='450'/>

The docstring can also be seen in the cell output by using ```?``` followed by the function name:

```
? plt.plot
```

<img src='images_jupyter/img_023.png' alt='img_023' width='450'/>

<img src='images_jupyter/img_024.png' alt='img_024' width='450'/>

To close down Jupyter Notebook, close down the tab in the browser. The terminal may still be busy running the server:

<img src='images_jupyter/img_025.png' alt='img_025' 
width='450'/>

Press ```Ctrl``` + ```c``` to close the currently runnign server which will give a new prompt in the Anaconda PowerShell:

<img src='images_jupyter/img_026.png' alt='img_026' width='450'/>

## JupyterLab

JupyterLab is the next generation of Jupyter Notebook and has additional functionality. It was originally meant to supersede Jupyter Notebook however Jupyter Notebook continues to be relatively popular and therefore both products are maintained.

JupyterLab can be launched using its tile in the Anaconda Navigator but unfortunately has no Start Menu shortcut. It can be launched from the Anaconda PowerShell Prompt using the PowerShell command:

```
jupyter lab
```

<img src='images_jupyter/img_027.png' alt='img_027' width='450'/>

A file explorer opens to the left hand side similar to that seen in Jupyter Notebook. It once again opens in %USERPROFILE% by default. To the right is a tab with a launcher. The + button on the left (under file) or the new tab button on the right beside the currently open launcher will open a launcher in a new tab. Note there are tabs within JupyterLab under the File Menu and these should not be confused with tabs within the Chromium based browser at the very top:

<img src='images_jupyter/img_028.png' alt='img_028' width='450'/>

The file explorer can be collapsed giving more screenspace for the launcher:

<img src='images_jupyter/img_029.png' alt='img_029' width='450'/>

The launcher has:

* Text File
* Markdown File
* Python File
* Notebook File
* Windows Terminal (PowerShell Prompt)
* ipkernel (ipython console)

<img src='images_jupyter/img_030.png' alt='img_030' width='450'/>

The markdown previously created in Jupyter Notebook can be opened:

<img src='images_jupyter/img_031.png' alt='img_031' width='450'/>

JupyterLab has a markdown preview which can be accessed by from the right click context menu by right clicking some blank space on the markdown file and selecting Show Markdown Preview:

<img src='images_jupyter/img_032.png' alt='img_032' width='450'/>

The headings tab to the left can be used to navigate through the markdown and markdown preview tabs although this feature has some issues with dedicated markdown files (working better with notebook files):

<img src='images_jupyter/img_033.png' alt='img_033' width='450'/>

The headings tab can be collapsed for more screen space:

<img src='images_jupyter/img_034.png' alt='img_034' width='450'/>

The notebook file previously created can be opened. When a notebook file is opened, generally the Kernel should be reestarted by going to the Kernel tab and selecting Restart Kernel and Run All Cells or one of the other Restart Kernel options:

<img src='images_jupyter/img_035.png' alt='img_035' width='450'/>

JupyterLab will display the full output of a large docstring in a cell. To make it more concise, the cell output can be right clicked and Enabling Scrolling for Outputs can be selected from the right click context menu:

<img src='images_jupyter/img_036.png' alt='img_036' width='450'/>

This makes the docstring readible but does not make it the main focus of a notebook:

<img src='images_jupyter/img_037.png' alt='img_037' width='450'/>

The script file can also be opened in JupyterLab. Recall that when the script file was open in Jupyter Notebook, there was no code completions as there was no Python interpretter running. In JupyterLab, the right click context menu can be used to create a console for the editor:

<img src='images_jupyter/img_038.png' alt='img_038' width='450'/>

Select Python 3 (ipykernel):

<img src='images_jupyter/img_039.png' alt='img_039' width='250'/>

Now code completion will work for Python builtins and standard modules identifiers in the script editor aswell as any instances created from builtins classes of classes from standard modules:

<img src='images_jupyter/img_040.png' alt='img_040' width='450'/>

For a third-party data science library, code completion will not display:

<img src='images_jupyter/img_041.png' alt='img_041' width='450'/>

The third-party library is imported in the ipython console and the instance from a class in the third-party library is also instantiated in the console. This can be down by highlighting a selection and selecting Run → Run Code:

<img src='images_jupyter/img_042.png' alt='img_042' width='450'/>

<img src='images_jupyter/img_043.png' alt='img_043' width='450'/>

Notice that the identifiers now display in the Console:

<img src='images_jupyter/img_044.png' alt='img_044' width='450'/>

They should also display in the script editor however this did not work with numpy in JupyterLab 3. 

This does work with the newer version JupyterLab 4. At present JupyterLab 4 is only available on the community channel and is not included in the Anaconda channel or Anaconda Python distribution. JupyterLab by default has no variable inspector or explorer. A third-party extension called JupyterLab Variable Inspector is only available on the community channel conda-forge and is not included in the Anaconda channel or Anaconda Python distribution. Details how to install these will be covered later in Python environments.

[Return to Anaconda Tutorial](./readme.md)