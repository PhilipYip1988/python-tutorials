# VSCode

Visual Studio Code (VSCode) is a general purpose code editor maintained by Microsoft.

## WinGet

VSCode can be installed on Windows using the command:

```powershell
WinGet install Microsoft.VisualStudioCode
```

Or on Linux using the command:

```bash
sudo snap install code --classic
```

## conda Environment

In order to use VSCode with Python a Python environment needs to be setup.

The Anaconda (base) Python environment can be used. Alternatively a Python environment can be setup for VSCode using:

```powershell
conda create -n vscode-env -c conda-forge python jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly ipympl pyqt autopep8 isort black pylint flake8 ruff miktex ghostscript
```

## Launching VSCode

VSCode can be launched using its Start Menu shortcut or from the Terminal using the command:

```powershell
code
```

## Selecting the Color Theme

The VSCode welcome screen will allow you to change the color scheme from Dark Modern (default):

<img src='./images/img_001.png' alt='img_001' width='450'/>

To Light Modern:

<img src='./images/img_002.png' alt='img_002' width='450'/>

This setting can be changed later using File → Preferences → Theme → Color Theme and then selecting Dark Modern or Light Modern.

## Python Extensions

VSCode is a general purpose code editor and appropriate extensions need to be installed for each programming language. Select the extension tab, search for Python, select the Python extension and install it. If extensions do not show or fail to install press the refresh button and try again:

Installing the Python Extension:

<img src='./images/img_003.png' alt='img_003' width='450'/>

Will also install Pylance:

<img src='./images/img_004.png' alt='img_004' width='450'/>

For Python development the following extensions are commonly installed.

|Extension Name|Developer|Purpose|Details|
|---|---|---|---|
|Python|Microsoft|Python|Support for Python Script files .py|
|*Pylance*|Microsoft|Code Completion|Installed with the Python extension|
|Jupyter|Microsoft|Python Notebooks|Support for Python Notebook files .ipynb|
|*Jupyter Cell Tags*|Microsoft|Notebook cell tags|Installed with the Jupyter extension|
|*Jupyter Keymap*|Microsoft|Jupyter Shortcut Keys|Installed with the Jupyter extension|
|*Jupyter Notebook Renderer*|Microsoft|Renders a Notebook File|Installed with the Jupyter extension|
|*Jupyter Slide Show*|Microsoft|Switch Slide Type Notebook Cell Option|Installed with the Jupyter extension|
|IntelliCode|Microsoft|Intelligent Code Suggestions||
|Code Spell Checker|Street Side Software|Code Spell Checker|English spell checker.|
|pylint|Microsoft|Linter: code is linted using pylint|Through but slow linter.|
|flake8|Microsoft|Linter: code is linted using flake8|Relatively fast but less through linter.|
|autopep8|Microsoft|Formatter: PEP8|Formats code spacing to make the code PEP8 compliant for a Script and Notebook file. Additionally moves imports to the top of a Script file but does not sort them alphabetically.|
|isort|Microsoft|Formatter: import organizer|Formats code to organize imports into standard and non-standard modules at the top of a script file and groups these alphabetically.|
|black|Microsoft|Formatter: opinionated|Formats code further with black opinionated formatting preferring double quotations for str instances.|
|ruff|Astral Software|Formatter and Linter: Rust Enhanced Fast Formatter and Linter|Formats code further with black opinionated formatting (default). A ruff.toml file can be used to specify preferences such as single quotations for str instances. Applies linting using pyflakes.|
|indent-rainbow|oderwat|Highlights Indention Levels|This makes it easier to visualise the indentation levels in code blocks.|

The installed extensions in my setup look as follows:

<img src='./images/img_005.png' alt='img_005' width='450'/>

<img src='./images/img_006.png' alt='img_006' width='450'/>

## Project

A project folder should be created. In this example an empty folder called project will be created in Documents:

<img src='./images/img_007.png' alt='img_007' width='450'/>

Once created it can be opened in VSCode from the files tab by selecting Open Folder (alternatively select File → Open Folder...):

<img src='./images/img_008.png' alt='img_008' width='450'/>

Select the folder:

<img src='./images/img_009.png' alt='img_009' width='450'/>

To have the ability to execute code, select Yes I trust the authors:

<img src='./images/img_010.png' alt='img_010' width='450'/>

A project consists of markdown and code files. Select New File in the File Explorer:

<img src='./images/img_011.png' alt='img_011' width='450'/>

A markdown file has the file extension ```.md```. A project should have a ```readme.md``` which can be created by selecting the new file icon. ```readme.md``` is a markdown file which contains details about the project:

<img src='./images/img_012.png' alt='img_012' width='450'/>

A markdown file is essentially a text file which can be formatted like a Word Document using a simple markdown language:

<img src='./images/img_013.png' alt='img_013' width='450'/>

The formatted output can be viewed by right clicking the ```readme.md``` and selecting Open Preview:

<img src='./images/img_014.png' alt='img_014' width='450'/>

The Markdown Preview tab can be snapped to the right. The Markdown and Markdown Preview panes are linked. Therefore scrolling down using the left scrollbar will also scroll the content on the right and clicking a heading from the table of contents on the left will move to the heading on both panes:

<img src='./images/img_015.png' alt='img_015' width='450'/>

A Python script file can be created and has the file extension ```.py```. In order for code completion to work properly, a Python interpreter (Python environment) should be selected. Press ```Ctrl``` + ```⇧``` + ```p``` to open the command palette and search for Python: Select Interpreter:

<img src='./images/img_016.png' alt='img_016' width='450'/>

Select the ```vscode-env``` or ```base``` Python environments:

<img src='./images/img_017.png' alt='img_017' width='450'/>

Now inputting a prefix such as ```p``` should invoke Pylance and display identifiers that begin with the prefix:

<img src='./images/img_018.png' alt='img_018' width='450'/>

When a function name is input followed by open parenthesis, Pylance will display the docstring:

<img src='./images/img_019.png' alt='img_019' width='450'/>

The test ```print``` statement can be added:

```python
print('Hello World!')
```

<img src='./images/img_020.png' alt='img_020' width='450'/>

The code can be run using the run button. This shows a new Terminal.

On Windows the following displays:

```powershell
(vscode-env) PS ~\OneDrive\Documents\project> & ~\Anaconda3\envs\vscode-env\python.exe ~\OneDrive\Documents\project\script.py
Hello World!
(vscode-env) PS ~\OneDrive\Documents\project> 
```

* ```(vscode-env)``` means the ```vscode-env``` Python environment is selected. 
* ```ps``` means the Terminal is using PowerShell as a programming language.
* ```~\OneDrive\Documents\project``` is the current working directory. Note the default current working directory in VSCode is the project folder opened and not necessarily the folder of the Python script file itself. 
* ```~\Anaconda3\envs\vscode-env\python.exe``` is the location of the ```python.exe``` being executed.
* ```~\OneDrive\Documents\project\script.py``` is the full file path of the Python script file.

On Linux the following displays:

```ps
(vscode-env) (base) username@pc ~/Documents/project$ ~/anaconda3/envs/vscode-env/bin/python ~/Documents/project/script.py
Hello World!
(vscode-env) (base) PS ~/Documents/project$ 
```

* ```(vscode-env)``` means the ```vscode-env``` Python environment is selected. 
* ```username@pc``` means the Terminal is using bash as a programming language.
* ```~/Documents/project``` is the current working directory. Note the default current working directory in VSCode is the project folder opened and not necessarily the folder of the Python script file itself. 
* ```~/Anaconda3/envs/vscode-env/bin/python``` is the location of the ```python``` binary (application) being executed.
* ```~/Documents/project/script.py``` is the full file path of the Python script file.

The print statement then displays and then a new PS prompt:

<img src='./images/img_021.png' alt='img_021' width='450'/>

A linter is essentially a grammar checker for code. When bad code grammar is detected by the linter, it will underlined. More details about the code grammar can be seen in the popup balloon which displays when the mouse is hovered above the underlined code. 

Python has 2 commonly used linters, pylint and flake8. pylint is a more through linter but it is slow as it takes time to examine the code and therefore linting is not dynamic. flake8 is a faster linter allowing some dynamic suggestions. Therefore it is common to install both linters:

<img src='./images/img_022.png' alt='img_022' width='450'/>

Notice if the text in the print statement is highlighted, the Code Spell Check also highlights the word ```Hwllo``` which is not recognised as an English word:

```python
print('Hwllo World!')
```

<img src='./images/img_023.png' alt='img_023' width='450'/>

Notice if a docstring is added for the module and a blank line added at the end of the module, the code grammar problems previously linted are now addressed:

```python
"""This is a test script file that prints Hello World!"""
print('Hello World!')
```

<img src='./images/img_024.png' alt='img_024' width='450'/>

In order for Intellicode to work correctly some settings need to be changed. Select the Settings option and then select Settings:

<img src='./images/img_026.png' alt='img_026' width='450'/>

VSCode settings can be viewed using the categories on the left:

<img src='./images/img_027.png' alt='img_027' width='450'/>

Search for Python Language Server:

<img src='./images/img_028.png' alt='img_028' width='450'/>

Change the Python Language Server to Pylance:

<img src='./images/img_029.png' alt='img_029' width='450'/>

Then close the Settings tab:

<img src='./images/img_030.png' alt='img_030' width='450'/>

If the following is input:

```python
print('Hello World!')
import numpy as np
x = np.array([0, 1, 2, 3, 4])
y = np.a
```

Pylance shows a list of identifiers in response to the ```np.a``` prefix. IntelliSense shows a combination of previously used identifiers or popularly used identifiers above the list of identifiers ★. The top identifier can be selected with a ```↹``` key. Other identifiers can be viewed using the ```↓``` and ```↑``` arrows and pressing ```↵```:

<img src='./images/img_031.png' alt='img_031' width='450'/>

If the following sloppy Python code that does not follow the [Python Style Guide PEP8](https://peps.python.org/pep-0008/) is input:

```python
'''This creates a simple plot.'''
print('Hello','World','!',sep='\t', end='\n\n\n')
import numpy as np
x =np.array([0, 1,2, 3,4])
y= np.array([0, 2,4, 6,8])
import pandas as pd
df = pd.DataFrame({'x':x, "y":y})
import matplotlib.pyplot as plt
plt.plot(df['x'], df["y"])
import collections
mapping = collections.Counter([0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5])
import datetime
current_time = datetime.datetime.now()
```

Notice that the linters find multiple problems:

<img src='./images/img_032.png' alt='img_032' width='450'/>

Press ```Ctrl``` + ```⇧``` + ```p``` to open the command palette and search for Format Document With...

<img src='./images/img_033.png' alt='img_033' width='450'/>

Then select autopep8:

<img src='./images/img_034.png' alt='img_034' width='450'/>

Notice that all the modules imported are placed at the top of the file grouped by standard modules and then third-party modules. Notice that all the spacing is now PEP8 compliant:

<img src='./images/img_035.png' alt='img_035' width='450'/>

The Imports can be organized alphabetically. Press ```Ctrl``` + ```⇧``` + ```p``` to open the command palette and search for Organize Imports:

<img src='./images/img_036.png' alt='img_036' width='450'/>

Select Ruff: Organize Imports:

<img src='./images/img_037.png' alt='img_037' width='450'/>

There is now spacing around the two import groups (standard and third-party) and the imports in these groups are sorted alphabetically:

<img src='./images/img_038.png' alt='img_038' width='450'/>

Press ```Ctrl``` + ```⇧``` + ```p``` to open the command palette and search for Format Document and select Ruff Format Document:

<img src='./images/img_039.png' alt='img_039' width='450'/>

Notice that the docstring now has triple double quotes and all the str instances have double quotations:

<img src='./images/img_040.png' alt='img_040' width='450'/>

The [Python Style Guide PEP8](https://peps.python.org/pep-0008/) does not implicitly state a preference for str quotations, stating that single and double quotations are seen as equivalent. However the Python Style Guide itself is written with a preference for single quotations. Moreover the Python interpreter also prefers single quotations, using double quotations only for str instances that contain str literals. As the docstring commonly includes str literals, it normally is provided using triple quotations. Triple quotations are used for the docstring even when the docstring doesn't contain str literals as the docstring normally gets expanded when working on a new Python module.

The ```ruff.toml``` file is a configuration file for ruff and the following option can be added:

```
[format]
quote-style = "single"
```

<img src='./images/img_041.png' alt='img_041' width='450'/>

Press ```Ctrl``` + ```⇧``` + ```p``` to open the command palette and search for Format Document and select Ruff Format Document:

<img src='./images/img_042.png' alt='img_042' width='450'/>

Notice that all quotations have single quotations because they contain no str literals. The docstring however uses triple double quotations:

<img src='./images/img_043.png' alt='img_043' width='450'/>

If the script is run:

<img src='./images/img_044.png' alt='img_044' width='450'/>

Notice that the print statement shows in the Terminal but it is busy while the plot is open in a separate window. Closing the plot will end the Python scripts execution and display a new PowerShell prompt:

<img src='./images/img_045.png' alt='img_045' width='450'/>

If a Python script a line beginning with a ```#``` is a comment. A line beginning with ```#%%``` is recognised as a command for a new IPython cell. Selecting Run Cell will run the cell using an IPython Shell (instead of running the entire script using a Python Shell):

<img src='./images/img_046.png' alt='img_046' width='450'/>

The cells in the script file can be run and the outputs of each cell are shown in the Interactive IPython window:

<img src='./images/img_047.png' alt='img_047' width='450'/>

When IPython is used, the Variables can be viewed:

<img src='./images/img_048.png' alt='img_048' width='450'/>

Commonly used instances of datastructures such as ```list```, ```ndarray``` and ```DataFrame``` can be expanded:

<img src='./images/img_049.png' alt='img_049' width='450'/>

An Interactive Python Notebook has the ```.ipynb``` file extension and consists of code and markdown cells. For code completion to work, a Python Kernel (Python Environment with IPython) must be selected using Select Kernel:

<img src='./images/img_050.png' alt='img_050' width='450'/>

Select Python Environments:

<img src='./images/img_051.png' alt='img_051' width='450'/>

Then select the ```vscode-env``` or ```base``` Python environment:

<img src='./images/img_052.png' alt='img_052' width='450'/>

Code completion using Pylance and Intellicode should work as before. Other IPython features such as Variables are available. 

For formatting, the command Format Document With... can be used with autopep8. The command Ruff: Format Imports and command Ruff: Format Documents can also be used. Formatting imports in a notebook will sort the imports in a single code cell out but will not move the code cells with imports to the top of the notebook.

Markdown cells and code cells can be run using the run button which displays to the left hand side of a cell, when the cell is selected. VSCode uses Jupyter shortcuts so ```Ctrl```+```↵``` can be used to run the currently selected cell and ```Alt``` + ```↵``` can be used to run the currently selected cell and insert a blank one after it.

All the code can be run using the button Run All at the top. The Kernel can also be restarted and the outputs can be cleared using Restart and Clear All Outputs respectively:

<img src='./images/img_053.png' alt='img_053' width='450'/>

The outputs of an Interactive Python Notebook are similar to the IPython interactive window seen previously however it is far easier to work with the notebook:

<img src='./images/img_054.png' alt='img_054' width='450'/>

There are some other options such as Export:

<img src='./images/img_055.png' alt='img_055' width='450'/>

Which can be used to export to a Python Script:

<img src='./images/img_056.png' alt='img_056' width='450'/>

Notice the Python Script file concerts all Markdown cells to cells that have comments. The Python script can be run in an IPython shell by selecting Run Cell or a Python shell by selecting run. Care should be taken in the later case because IPython code such as IPython magics and use of the ```?``` operator do not work in a Python shell:

<img src='./images/img_057.png' alt='img_057' width='450'/>

The notebook can also be exported to HTML and viewed as a static document in a web browser:

<img src='./images/img_058.png' alt='img_058' width='450'/>

TeX can also be added to matplotlib plots. To test it is working create a new notebook file and add the three cells:

```python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
%matplotlib qt5

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0.001, 2.001, 3.999, 5.999, 8.002, 10.001])

fig, ax = plt.subplots(num=1)
ax.plot(x, y, color='tomato')
ax.set_xlabel(r'$\dot{\alpha}$', usetex=True)
ax.set_ylabel(r'$\ddot{\beta}$', usetex=True)
ax.set_title(r'$\ddot{\beta}$=f$(\frac{\dot{\alpha}}{1})$', usetex=True);
```

The first TeX plot may take a while to create and the window will display not responding.

<img src='./images/img_060.png' alt='img_060' width='450'/>

Behind the scenes a number of cached text files will be copied to:

```bash
~/.matplotlib
```

Subsequent plots with TeX should render quicker.

A detailed overview of Markdown and TeX syntax is given in the next tutorial.

[Return to Python Tutorials](../readme.md)
