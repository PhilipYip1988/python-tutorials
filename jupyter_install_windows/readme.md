# JupyterLab IDE Windows Setup

JupyterLab is a browser based IDE.

## Miniforge Installation and Setup

The conda package manager will be used to create a new environment for JupyterLab. In order to use conda, Miniforge needs to be installed and preferably initialised. This was previously covered in:

[Miniforge Install and Initialisation](../spyder_install_windows/readme.md#miniforge-installation)

In order to use TeX in matplotlib plots. MikTeX needs to be installed and added to the system path (which was also previously covered in the above).

## Update conda

The purpose of the `base` environment is to use the conda package manager to install packages in other Python environments. Before using the conda package manager, the conda package manager should be updated to the latest version:

```powershell
conda update conda
```

<img src='./images/img_001.png' alt='img_001' width='600'/>

Since Miniforge is used, the default channel will be the community channel `conda-forge`:

<img src='./images/img_002.png' alt='img_002' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_003.png' alt='img_003' width='600'/>

The conda package manager is now up to date:

<img src='./images/img_004.png' alt='img_004' width='600'/>

Note there is an issue going from `conda` 24 to 25 where it doesn't update properly and says:

```
==> WARNING: A newer version of conda exists <==
current version: 24.w.w
latest version: 25.x.x

Please update conda by running:

conda update -n base -c conda-forge conda
```

And inputting the command listed takes you back to the same screen. To bypass this use:

```powershell
conda install conda=25.x.x
```

Where `25.x.xx` should be replaced by the latest version number.

The terminal can be cleared by inputting:

```powershell
clear
```

(conda) Python environments can be listed by inputting:

```powershell
conda env list
```

<img src='./images/img_005.png' alt='img_005' width='600'/>

## Creating a JupyterLab conda-forge Environment

JupyterLab is mainly used with Python. To create a new environment for JupyterLab which includes the Python kernel, the following command can be used:

```powershell
conda create -n jupyter-env jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt ipympl isort autopep8 ruff black jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker jupyterlab-spreadsheet-editor
```

<img src='./images/img_006.png' alt='img_006' width='600'/>

`jupyterlab` is the IDE itself. `seaborn` has `numpy`, `pandas` and `matplotlib` as dependencies and are the scientific libraries. `scikit-learn` is used for machine learning. `pyarrow`, `openpyxl`, `xlrd`, `xlsxwriter`, `lxml`, `sqlalchemy`, `tabulate` are for various file pandas formats. `pyqt` is for matplotlib's interactive backend, `ipympl` is used for the widget backend and `ffmpeg` is for saving matplotlib animations.

`jupyterlab-variableinspector`, `jupyterlab_code_formatter`, `jupyterlab-spellchecker`, `jupyterlab-spreadsheet-editor` are common extensions for JupyterLab. In order for extensions to be installed, nodejs needs to be installed. The JupyterLab IDE and extensions are written in nodejs, which is a programming language used for web content. Knowledge of nodejs is not required to use Python with JupyterLab.

`-n` means name and `jupyter-env` is the name of the Python environment. Specifying an environment using `-n` means changes to that environment will be made opposed to `base` which is the currently activate environment.

The environment location will be listed, along with details about the packages to be installed:

<img src='./images/img_007.png' alt='img_007' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_008.png' alt='img_008' width='600'/>

## Updating JupyterLab

There is a new release of JupyterLab, approximately every month. To keep it up to date. Open up the Terminal, the `base` environment will be updated, use the following command to update `conda` to the latest version:

```powershell
conda update conda
```

Note there is an issue going from `conda` 24 to 25 where it doesn't update properly and says:

```
==> WARNING: A newer version of conda exists <==
current version: 24.w.w
latest version: 25.x.x

Please update conda by running:

conda update -n base -c conda-forge conda
```

And inputting the command listed takes you back to the same screen. To bypass this use:

```powershell
conda install conda=25.x.x
```

Where `25.x.xx` should be replaced by the latest version number.

Then activate `jupyter-env` and search for updates to all packages:

```powershell
conda activate jupyter-env
conda update --all
```

If there are troubles updating the environment, it can be removed and recreated from scratch using:

```powershell
conda env remove -n jupyter-env
```

You may need to manually delete the residual `jupyter-env` folder after removing this environment:

```powershell
conda create -n jupyter-env jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt ipympl isort autopep8 ruff black jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker jupyterlab-spreadsheet-editor
```

## Launching JupyterLab

The `base` (conda) Python environment is selected:

<img src='./images/img_009.png' alt='img_009' width='600'/>

The `jupyter-env` environment can be activated. To activate `jupyterlab-env` input:

```powershell
conda activate jupyter-env
```

<img src='./images/img_010.png' alt='img_010' width='600'/>

If the environments are listed:

```powershell
conda env list
```

Notice that the (conda) Python environment `jupyter-lab` has a \* indicating it is activated. The directory is also shown:

<img src='./images/img_011.png' alt='img_011' width='600'/>

This can be exploed in Windows Explorer by going to:

```
%UserProfile%\Miniforge3
```

<img src='./images/img_012.png' alt='img_012' width='600'/>

Then looking at the `envs` subfolder which contains the (conda) Python environments:

<img src='./images/img_013.png' alt='img_013' width='600'/>

`jupyter-env` can be examined:

<img src='./images/img_014.png' alt='img_014' width='600'/>

Because it is activated, this folder will be preferenced alongside its associated script folders when looking for an application in the Windows Terminal. If the scripts folder is examined:

<img src='./images/img_015.png' alt='img_015' width='600'/>

Notice that there is a `juptyer-lab.exe`. This can be pinned to the Start Menu:

<img src='./images/img_016.png' alt='img_016' width='600'/>

More typically JupyterLab is opened in the terminal by inputting:

```powershell
jupyter-lab
```

Note the `.exe` is typically dropped:

<img src='./images/img_017.png' alt='img_017' width='600'/>

JupyterLab is a browser based IDE. The server is ran in the terminal, which will remain busy while the JupyterLab application is running:

<img src='./images/img_018.png' alt='img_018' width='600'/>

While the visual elements display in the browser:

<img src='./images/img_019.png' alt='img_019' width='300'/>

<img src='./images/img_020.png' alt='img_020' width='600'/>

## File Explorer

To the left hand side is a file explorer which displays the current working directory in the terminal. The current working directory in the terminal is the home the directory `%UserProfile%`. The Documents folder can be selected:

<img src='./images/img_021.png' alt='img_021' width='600'/>

And script.py can be opened:

<img src='./images/img_022.png' alt='img_022' width='600'/>

## Script Editor and Terminal

The terminal is equivalent to a new session of the Windows terminal, using Powershell:

<img src='./images/img_023.png' alt='img_023' width='600'/>

Notice it starts with base, the default (conda) Python environment:

<img src='./images/img_024.png' alt='img_024' width='600'/>

(conda) Python environment `jupyter-env` can be activated using:

```powershell
conda activate jupyter-env
```

<img src='./images/img_025.png' alt='img_025' width='600'/>

The `python.exe` in the currently activated (conda) Python environment `jupyter-env` can be used to run the `script.py` from the currently selected folder using:

```powershell
python script.py
```

Note that the `.exe` extension for `python.exe` is not required while the first input argument being provided to the `python.exe` requires its file extension `script.py`:

<img src='./images/img_026.png' alt='img_026' width='600'/>

The script runs and the terminal moves onto the next prompt but the plot does not show:

<img src='./images/img_027.png' alt='img_027' width='600'/>

The following command:

```python
plt.show()
```

can be added to `script.py`:

<img src='./images/img_028.png' alt='img_028' width='600'/>

This `script.py` file can be saved using the file menu:

<img src='./images/img_029.png' alt='img_029' width='600'/>

When this script is rerun, notice the plot displays in a separate plot window, this plot window using the QtAgg backend:

<img src='./images/img_030.png' alt='img_030' width='600'/>

## IPython Console

Code completion does not display for Python code, unless it is run in an interactive python console. Right click empty space in the script and select create console for editor:

<img src='./images/img_031.png' alt='img_031' width='600'/>

Select IPython kernel:

<img src='./images/img_032.png' alt='img_032' width='600'/>

Code can be highlighted:

<img src='./images/img_033.png' alt='img_033' width='600'/>

The selection can be run by selecting run → run selected code:

<img src='./images/img_034.png' alt='img_034' width='600'/>

This code shows as the input to `In [1]` which has no `Out[1]`:

<img src='./images/img_035.png' alt='img_035' width='600'/>

Now the libraries are imported, identifiers can be accessed from numpy by inputting:

```python
np.↹
```

<img src='./images/img_036.png' alt='img_036' width='600'/>

Data model identifiers can be accessed using:

```python
np.__↹
```

<img src='./images/img_037.png' alt='img_037' width='600'/>

The identifier `__file__` is an instance and can be returned to an ipython cell output:

<img src='./images/img_038.png' alt='img_038' width='600'/>

The `print` function can be used to process the escape characters in the Windows path. To view a docstring, an identifier should be input with open parenthesis and `⇧+↹` should be pressed:

```python
print(⇧+↹
```

<img src='./images/img_039.png' alt='img_039' width='600'/>

A docstring can also be printed to a cell output using:

```python
print?
```

<img src='./images/img_040.png' alt='img_040' width='600'/>

A longer docstring can be examined:

```python
plt.plot(⇧+↹
```

<img src='./images/img_041.png' alt='img_041' width='600'/>

And printed to an ipython cell output:

```python
plt.plot?
```

<img src='./images/img_042.png' alt='img_042' width='600'/>

All the code can be run by selecting run → run all code:

<img src='./images/img_043.png' alt='img_043' width='600'/>

Notice that the plot is displayed using the inline backend where it is essentially nested as a static image in the ipython cell output:

<img src='./images/img_044.png' alt='img_044' width='600'/>

## Interactive Python Notebook

A Python Script file `.py` is essentially a text file which can be displayed in a text editor. 

Code can also be written in an Interactive Python Notebook file `.ipynb`. The interactive Python notebook is written using nodejs which is a programming language used by the browser to display visual content, essentially as a website. 

Open a new launcher and select new notebook:

<img src='./images/img_045.png' alt='img_045' width='600'/>

Rename the notebook using the file explorer:

<img src='./images/img_046.png' alt='img_046' width='600'/>

<img src='./images/img_047.png' alt='img_047' width='600'/>

A notebook consists of cells which can either be Python code (the default) or markdown which is essentially used to document around the code:

<img src='./images/img_048.png' alt='img_048' width='600'/>

Markdown can be used to create a title:

<img src='./images/img_049.png' alt='img_049' width='600'/>

A heading can be added using:

```markdown
# JupyterLab Test
```

<img src='./images/img_050.png' alt='img_050' width='600'/>

When it is run using the run button, notice the formatted markdown displays showing the text as Heading 1:

<img src='./images/img_051.png' alt='img_051' width='600'/>

Double clicking the heading returns to the raw markdown:

<img src='./images/img_052.png' alt='img_052' width='600'/>

Inputting `Esc+y` toggles the cell to a code cell, notice the syntax highlighting changes as the `#` in Python code means a comment:

<img src='./images/img_053.png' alt='img_053' width='600'/>

`Esc+m` toggles the cell back to a markdown cell, notice the syntax highlighting changes as the `#` means Heading 1:

<img src='./images/img_054.png' alt='img_054' width='600'/>

The markdown cell can be run using the shortcut key `↹+↵` and another Heading 2 can be added:

```markdown
## Import Libraries
```

and run using `↹+↵`:

<img src='./images/img_055.png' alt='img_055' width='600'/>

JupyterLab has a navigation pane which displays the table of contents in a notebook file:

<img src='./images/img_056.png' alt='img_056' width='600'/>

To run a cell, the shortcut key `↹+↵` can be used. To run a cell and insert a blank one below it instead use `Alt+↵`:

<img src='./images/img_057.png' alt='img_057' width='650'/>

The `+` button will also add a blank cell:

<img src='./images/img_058.png' alt='img_058' width='650'/>

The shortcuts to run the selected cell, run selected cell and insert below and run selected cell and do not advance can be seen on the run menu:

<img src='./images/img_059.png' alt='img_059' width='650'/>

The cell can be deleted by pressing the delete button or using the shortcut key `Ctrl+d`:

<img src='./images/img_060.png' alt='img_060' width='650'/>

Code can be added to a cell:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

<img src='./images/img_061.png' alt='img_061' width='650'/>

Identifiers can be viewed by inputting a prefix e.g. `np.` followed by a `↹`:

<img src='./images/img_062.png' alt='img_062' width='650'/>

A docstring can be examined by inputting a function with open parenthesis and pressing `⇧+↹`, for example:

```
np.arange(⇧+↹
```

<img src='./images/img_063.png' alt='img_063' width='650'/>

The following cells can be added:

```markdown
## Set Style
```

```python
sns.set_style('whitegrid')
```

```markdown
## Create Data
```

```python
x = np.array([0, 1, 2, 3, 4, 5])
y = 2 * np.pi * np.sin(x)
```

<img src='./images/img_064.png' alt='img_064' width='650'/>

The variables `x` and `y` can be displayed on the Variable Inspector, right click blank space in the notebook and select open Variable Inspector:

<img src='./images/img_065.png' alt='img_065' width='650'/>

The Variable Inspector opens in another tab which can be repositioned:

<img src='./images/img_066.png' alt='img_066' width='650'/>

<img src='./images/img_067.png' alt='img_067' width='650'/>

Some variables that are Collections can be further examined:

<img src='./images/img_068.png' alt='img_068' width='650'/>

A plot can be added using:

```markdown
## Plot Data
```

```python
plt.plot(x, y)
plt.xlabel(R'$x$', usetex=True)
plt.ylabel(R'$2 \pi \sin(x)$', usetex=True)
```

<img src='./images/img_069.png' alt='img_069' width='650'/>

By default the plot displays inline, in the cell output as a static image:

<img src='./images/img_070.png' alt='img_070' width='650'/>

The backend can be changed to interactive python matplotlib:

```markdown
## Plot Data Widget
```

```python
%matplotlib ipympl
```

```python
plt.plot(x, y)
plt.xlabel(R'$x$', usetex=True)
plt.ylabel(R'$2 \pi \sin(x)$', usetex=True)
```

which gives limited interactivity:

<img src='./images/img_071.png' alt='img_071' width='650'/>

<img src='./images/img_072.png' alt='img_072' width='650'/>

To use another backend, the kernel needs to be restarted. Select Kernel → Restart Kernel and all Cell Outputs of all Cells:

<img src='./images/img_073.png' alt='img_073' width='650'/>

Select restart:

<img src='./images/img_074.png' alt='img_074' width='650'/>

The backend can be changed to Qt, which displays the plot in a seperate interactive window which gives more interactivity:

```markdown
## Plot Data Qt

```python
%matplotlib qtagg
```

```python
plt.plot(x, y)
plt.xlabel(R'$x$', usetex=True)
plt.ylabel(R'$2 \pi \sin(x)$', usetex=True)
```

<img src='./images/img_075.png' alt='img_075' width='650'/>

Note the TeX added to the plot can also be used in markdown cell:

```markdown
$2 \pi \sin(x)$
```

<img src='./images/img_076.png' alt='img_076' width='650'/>

Additional markdown such as a table can be added:

```markdown
|num|number|
|---|---|
|1|one|
|2|two|
|3|three|
```

<img src='./images/img_077.png' alt='img_077' width='650'/>

<img src='./images/img_078.png' alt='img_078' width='650'/>

The `\*` is a special character in markdown and can be used to make bold and italic text as well as list of bullet points:

```markdown
**bold**, *italic*, ***bold-italic***, ~~strike-through~~
```

```markdown
* one
* two 
* three
```

It can be inserted as an escape character using:

```markdown
\*
```

<img src='./images/img_079.png' alt='img_079' width='650'/>

<img src='./images/img_080.png' alt='img_080' width='650'/>

A docstring can be displayed in a cell output:

```python
plt.plot?
```

<img src='./images/img_081.png' alt='img_081' width='650'/>

Often scrolling outputs are enabled for such cells. Allowing the docstring to be seen without taking too much emphasis in the overall notebook. Right click the Cell Output and select Enable Scrolling for Outputs:

<img src='./images/img_082.png' alt='img_082' width='650'/>

<img src='./images/img_083.png' alt='img_083' width='650'/>

The file menu can be used to save the notebook:

<img src='./images/img_084.png' alt='img_084' width='650'/>

When a notebook is closed and JupyterLab is closed and then JupyterLab is relaunched and the notebook opened, the notebook will display output from the previous session. However the ipython console associated with the notebook will have ended:

<img src='./images/img_085.png' alt='img_085' width='650'/>

Select Kernel → Restart Kernel and all Cell Outputs of all Cells:

<img src='./images/img_086.png' alt='img_086' width='650'/>

<img src='./images/img_087.png' alt='img_087' width='650'/>

To run a cell one by one, the shortcut key `↹+↵` can be used:

<img src='./images/img_088.png' alt='img_088' width='650'/>

Variables can be viewed in cell outputs:

```python
x
```

```python
y
```

<img src='./images/img_089.png' alt='img_089' width='650'/>

A DataFrame can be constructed and viewed in a cell output using:

```python
df = pd.DataFrame({'x': x, 
                   'y': y})

df
```

<img src='./images/img_090.png' alt='img_090' width='650'/>

<img src='./images/img_091.png' alt='img_091' width='650'/>

This can be saved to a file using:

<img src='./images/img_092.png' alt='img_092' width='650'/>

```python
df.to↹
```

<img src='./images/img_093.png' alt='img_093' width='650'/>

And selecting the identifier `to_csv` and supplying a path to the file:

```python
df.to_csv('df.csv')
```

<img src='./images/img_094.png' alt='img_094' width='650'/>

This csv file can be opened in JupyterLab because the spreadsheet editor extension is installed:

<img src='./images/img_095.png' alt='img_095' width='650'/>

Unfortunately this extension has no support for Excel files:

<img src='./images/img_096.png' alt='img_096' width='650'/>

If the code in the following cell is formatted poorly such as:

```python 
x = np.array([0,1,2,3,4,5])
y=2* np.pi* np.sin(x)
```

<img src='./images/img_097.png' alt='img_097' width='650'/>

The format notebook button can be selected:

<img src='./images/img_098.png' alt='img_098' width='650'/>

Note the formatting is corrected however all the string quotations are changed to `""` instead of Python's default `''` because the black formatter is used by default.

This can be changed by selecting Settings → Settings Editor:

<img src='./images/img_099.png' alt='img_099' width='650'/>

Then selecting the Jupyter CCode Formatter:

<img src='./images/img_100.png' alt='img_100' width='650'/>

Often the JSON settings editor is more useful:

<img src='./images/img_101.png' alt='img_101' width='650'/>

The System Defaults JSON can be copied to the User Preferences and string_normalization can be assigned to False:

<img src='./images/img_102.png' alt='img_102' width='650'/>

Now formatting can be used without changing the single quotations to double quotations:

<img src='./images/img_103.png' alt='img_103' width='650'/>

<img src='./images/img_104.png' alt='img_104' width='650'/>

The following image can be examined:

<img src='./images/img_105.png' alt='img_105' width='650'/>

A link to it can be inserted using:

```markdown
[fig_1](./fig1.png)
```

<img src='./images/img_106.png' alt='img_106' width='650'/>

Clicking on this link opens the file:

<img src='./images/img_107.png' alt='img_107' width='650'/>

<img src='./images/img_108.png' alt='img_108' width='650'/>

Putting a `!` in front of the link will instead embed it:

```markdown
![fig_1](./fig1.png)
```

<img src='./images/img_109.png' alt='img_109' width='650'/>

<img src='./images/img_110.png' alt='img_110' width='650'/>

Show contextual help opens a contextual help pane which updates every time an identifier is selected:

<img src='./images/img_111.png' alt='img_111' width='650'/>

<img src='./images/img_112.png' alt='img_112' width='650'/>

To close JupyterLab, the close button can be used on the browser tab:

<img src='./images/img_113.png' alt='img_113' width='650'/>

Although the visual elements of JupyterLab are closed, the server is still running in the Windows Terminal. Press `Ctrl+c` to cancel tthe current operation:

<img src='./images/img_114.png' alt='img_114' width='650'/>

A new prompt displays:

<img src='./images/img_115.png' alt='img_115' width='650'/>


## Jupyter Acronym

Jupyter is an acronym for **Ju**lia, **Py**thon **et** **R** and as the name suggests supports the three programming languages Julia, Python and R.

Although `conda` is strongly associated with Python it is actually a general purpose data science package manager and supports the R programming language. 

Currently there is limited support for the Julia programming language supporting only Linux and Mac. The `conda-forge` package is a significantly older version of Julia. 

## R Kernel

If the (conda) Python environment `jupyter-env` is activated, the following R packages can be installed:

```powershell
conda install r-irkernel jupyter-lsp-r r-tidyverse r-ggthemes r-palmerpenguins r-writexl 
```

<img src='./images/img_116.png' alt='img_116' width='650'/>

The environment location will be listed, along with details about the packages to be installed:

<img src='./images/img_117.png' alt='img_117' width='650'/>

Input `y` in order tp proceed:

<img src='./images/img_118.png' alt='img_118' width='650'/>

When JupyterLab is launched using:

```powershell
jupyter-lab
```

<img src='./images/img_119.png' alt='img_119' width='650'/>

Notice that there is now an option for both a Python and R console:

<img src='./images/img_120.png' alt='img_120' width='650'/>

## Julia (Jupyter Kernel)

Unfortunately Julia isn't available on conda-forge for Windows and has to be installed using the Windows Store:

<img src='./images/img_121.png' alt='img_121' width='650'/>

<img src='./images/img_122.png' alt='img_122' width='650'/>

<img src='./images/img_123.png' alt='img_123' width='650'/>

Julia will be added to the system path. Open the Windows Terminal and input:

```powershell
julia
```

<img src='./images/img_124.png' alt='img_124' width='650'/>

To install the Julia Kernel input:

```powershell
using Pkg
Pkg.add("IJulia")
```

<img src='./images/img_125.png' alt='img_125' width='650'/>

Julia can be exited using:

```julia
exit()
```
<img src='./images/img_126.png' alt='img_126' width='650'/>

When JupyterLab is launched using:

```powershell
jupyter-lab
```

<img src='./images/img_127.png' alt='img_127' width='650'/>

The **Ju**lia, **Pyt**hon **et** **R** consoles are available:

<img src='./images/img_128.png' alt='img_128' width='650'/>

[Return to Python Tutorials](../readme.md)