# JupyterLab IDE Ubuntu Setup

JupyterLab is a browser based IDE.

## Miniforge Installation and Setup

The conda package manager will be used to create a new environment for JupyterLab. In order to use conda, Miniforge needs to be installed and preferably initialised. This was previously covered in:

[Miniforge Install and Initialisation](../spyder_install_ubuntu/readme.md#miniforge-installation)

In order to use TeX in matplotlib plots. TeX needs to be installed system wide using the operating systems package manager (which was also previously covered in the above):

```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic cm-super dvipng
```

## Updating the conda Package Manager

The purpose of the base (conda) Python environment is to use the conda package manager to install packages, that are compartmentalised in other (conda) Python environments. Before using the conda package manager, the conda package manager should be updated to the latest version using:

```bash
conda update conda
```

<img src='./images/img_001.png' alt='img_001' width='600'/>

Since Miniforge is used, the default channel will be the community channel `conda-forge`:

<img src='./images/img_002.png' alt='img_002' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_003.png' alt='img_003' width='600'/>

The conda package manager is now up to date:

<img src='./images/img_004.png' alt='img_004' width='600'/>

The terminal can be cleared by inputting:

```bash
clear
```

And (conda) Python environments can be listed by inputting:

```bash
conda env list
```

<img src='./images/img_005.png' alt='img_005' width='600'/>#

## Creating a JupyterLab conda-forge Environment

JupyterLab is mainly used with Python. To create a new (conda) Python environment for JupyterLab which includes the Python kernel, the following command can be used:

```bash
conda create -n jupyter-env jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt ipympl isort autopep8 ruff black jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker jupyterlab-spreadsheet-editor
```

<img src='./images/img_006.png' alt='img_006' width='600'/>

`jupyterlab` is the IDE itself. `seaborn` has `numpy`, `pandas` and `matplotlib` as dependencies and are the scientific libraries. `scikit-learn` is used for machine learning. `pyarrow`, `openpyxl`, `xlrd`, `xlsxwriter`, `lxml`, `sqlalchemy`, `tabulate` are for various file pandas formats. `pyqt` is for matplotlib's interactive backend, `ipympl` is used for the widget backend and `ffmpeg` is for saving matplotlib animations.

`jupyterlab-variableinspector`, `jupyterlab_code_formatter`, `jupyterlab-spellchecker`, `jupyterlab-spreadsheet-editor` are common extensions for JupyterLab. In order for extensions to be installed, nodejs needs to be installed. The JupyterLab IDE and extensions are written in nodejs, which is a programming language used for web content. Knowledge of nodejs is not required to use Python with JupyterLab.

`-n` means name and `jupyter-env` is the name of the (conda) Python environment. Specifying an environment using `-n` means changes to that environment will be made opposed to `base` which is the currently activated environment.

The environment location will be listed, along with details about the packages to be installed:

<img src='./images/img_007.png' alt='img_007' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_008.png' alt='img_008' width='600'/>

## Updating JupyterLab

There is a new release of JupyterLab, approximately every month. To keep it up to date. Open up the Terminal and update the conda package manager in the base Python environment using:

```bash
conda update conda
```

Then activate `jupyter-env` and search for updates to all packages using `--all`:

```bash
conda activate jupyter-env
conda update --all
```

If there are troubles updating the (conda) Python environment, it can be removed and recreated from scratch using:

```bash
conda env remove -n jupyter-env
```

You may need to manually delete the residual `jupyter-env` folder after removing this environment:

```bash
conda create -n jupyter-env jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt ipympl isort autopep8 ruff black jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker jupyterlab-spreadsheet-editor
```

## Launching JupyterLab

To activate the (conda) Python environment `jupyterlab-env` input:

```bash
conda activate jupyter-env
```

<img src='./images/img_009.png' alt='img_009' width='600'/>

The prefix will now show `(jupyter-env)` instead of `(base)`:

<img src='./images/img_010.png' alt='img_010' width='600'/>

This means that instead of searching the bin folder in  the base (conda) Python environment which is the `miniforge3` folder:

<img src='./images/img_011.png' alt='img_011' width='600'/>

The equivalent bin folder is used for the currently activated (conda) Python environment `jupyter-env`.

The `envs` folder contains the environments:

<img src='./images/img_012.png' alt='img_012' width='600'/>

The `jupyter-env` folder is currently activated:

<img src='./images/img_013.png' alt='img_013' width='600'/>

And therefore the bin and lib folders are preferentially searched for binaries and programs:

<img src='./images/img_014.png' alt='img_014' width='600'/>

The binary of interest is `jupyter-lab`:

<img src='./images/img_015.png' alt='img_015' width='600'/>

And can be launched in the terminal by inputting:

```bash
jupyter-lab
```

<img src='./images/img_016.png' alt='img_016' width='600'/>

JupyterLab is a browser based IDE. The server is ran in the terminal:

<img src='./images/img_017.png' alt='img_017' width='600'/>

<img src='./images/img_018.png' alt='img_018' width='600'/>

While the visual elements display in the browser:

<img src='./images/img_019.png' alt='img_019' width='600'/>

## File Explorer

To the left hand side is a file explorer which displays the current working directory in the terminal. The current working directory in the terminal was `~`, the home the directory:

<img src='./images/img_020.png' alt='img_020' width='600'/>

The Documents folder can be selected. JupyterLab can be used to open `.py` files, these display in a script editor which applies syntax highlighting:

<img src='./images/img_021.png' alt='img_021' width='600'/>

## Launcher

To the right hand side, a new launcher can be selected, this can be used to start a new terminal. 

<img src='./images/img_022.png' alt='img_022' width='600'/>

## Script Editor and Terminal

The terminal is equivalent to a new session of the Linux terminal and starts with `(base)`, indicating the (conda) base Python environment:

<img src='./images/img_023.png' alt='img_023' width='600'/>

The `jupyterlab-env` can be activated and the script executed:

```python
#%% Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%% Set Style
sns.set_style('whitegrid')
#%% Create Data
x = np.array([0, 1, 2, 3, 4])
y = 2 * np.pi * np.sin(x)
#%% Plot
plt.plot(x, y)
plt.xlabel(R'$x$', usetex=True)
plt.ylabel(R'$x2 \pi x \sin{x}$', usetex=True)
```

```bash
conda activate jupyter-env
python3 script.py
```

<img src='./images/img_024.png' alt='img_024' width='600'/>

The plot in the script won't show unless the command:

```python
plt.show()
```

is added.

<img src='./images/img_025.png' alt='img_025' width='600'/>

The file menu can be used to save the script:

<img src='./images/img_026.png' alt='img_026' width='600'/>

The plot now displays in an interactive window:

<img src='./images/img_027.png' alt='img_027' width='600'/>

## IPython Console

Code completion does not display for Python code, unless it is run in an interactive python console. Right click empty space in the script and select create console for editor:

<img src='./images/img_028.png' alt='img_028' width='600'/>

Select IPython kernel:

<img src='./images/img_029.png' alt='img_029' width='600'/>

A selection can be highlighted:

<img src='./images/img_030.png' alt='img_030' width='600'/>

And run using, run selected code:

<img src='./images/img_031.png' alt='img_031' width='600'/>

Now the libraries are imported, identifiers can be accessed from numpy by inputting:

```python
np.↹
```

<img src='./images/img_032.png' alt='img_032' width='600'/>

Data model identifiers can be accessed using:

```python
np.__↹
```

<img src='./images/img_033.png' alt='img_033' width='600'/>

The data model identifier `__file__` is an instance and can be returned to an ipython cell output:

<img src='./images/img_034.png' alt='img_034' width='600'/>

The IPython console is equivalent to opening an IPython console from the Linux terminal. Because the Linux the `jupyter-env` was activated when the `jupyter-lab` binary was launched, `jupyter-env` is the currently selected environment. To view a docstring, an identifier should be input with open parenthesis and `⇧`+ `↹` should be pressed:

```python
np.arange(⇧+↹
```

<img src='./images/img_035.png' alt='img_035' width='600'/>

A docstring can also be returned to an ipython cell:

```python
np.arange?
```

<img src='./images/img_036.png' alt='img_036' width='600'/>

<img src='./images/img_037.png' alt='img_037' width='600'/>

## Interactive Python Notebook

A Python Script file `.py` is essentially a text file which can be displayed in a text editor. 

Code can also be written in an Interactive Python Notebook file `.ipynb`. The interactive Python notebook is written using nodejs which is a programming language used by the browser to display visual content, essentially as a website. 

<img src='./images/img_038.png' alt='img_038' width='600'/>

Although nodejs is used to display the contents of the `.ipynb` file in the browser. The user can create code cells which are written using Python or markdown cells are written using markdown. If a markdown cell is selected:

<img src='./images/img_039.png' alt='img_039' width='600'/>

A title (H1) can be added using:

```markdown
# JupyterLab Test
```

<img src='./images/img_040.png' alt='img_040' width='600'/>

When this cell is run, by selecting the run button or pressing `⇧`+`↵`:

<img src='./images/img_041.png' alt='img_041' width='600'/>

The formatted markdown displays. (It can be edited again by double clicking it). Note to the left hand side, the table of contents tab displays the title:

<img src='./images/img_042.png' alt='img_042' width='600'/>

A heading (H2) can be added using:

```markdown
## Import Libraries
```

<img src='./images/img_043.png' alt='img_043' width='600'/>

The libraries can be imported in a code cell using:

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

<img src='./images/img_044.png' alt='img_044' width='600'/>

Now that the libraries are imported, identifiers from them can be viewed:

```python
np.↹
```

<img src='./images/img_045.png' alt='img_045' width='600'/>

A new cell, will default to a Python cell, notice the markdown text has the wrong syntax highlighting:

<img src='./images/img_046.png' alt='img_046' width='600'/>

A number of keyboard shortcuts are available, these can be viewed by selecting Help → Show Keyboard Shortcuts:

<img src='./images/img_047.png' alt='img_047' width='600'/>

<img src='./images/img_048.png' alt='img_048' width='600'/>

The keyboard shortcut `Esc`+`m` will toggle a cell to markdown. It can be run using `⇧`+`↵`:

<img src='./images/img_049.png' alt='img_049' width='600'/>

## JupyterLab Variable Inspector

If the following three code cells are run:

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

x = np.array([0, 1, 2, 3, 4])
y = 2 * np.pi * np.sin(x)
```

The variables `x` and `y` are created. Variables can be seen by right clicking some blank space in the notebook and selecting open variable inspector:

<img src='./images/img_050.png' alt='img_050' width='600'/>

<img src='./images/img_051.png' alt='img_051' width='600'/>

Since `x` and `y` are `ndarray` instances they can be inspected further by selecting the magnify icon:

<img src='./images/img_052.png' alt='img_052' width='600'/>

<img src='./images/img_053.png' alt='img_053' width='600'/>

<img src='./images/img_054.png' alt='img_054' width='600'/>

## Plotting

If the code to plot is added:

```python
plt.plot(x, y)
plt.xlabel(R'$x$', usetex=True)
plt.ylabel(R'$x2 \pi x \sin{x}$', usetex=True)
```

Notice the plot is returned to the cell output as a static image:

<img src='./images/img_055.png' alt='img_055' width='600'/>

Plot backends can be selected using the ipython magic. 

`inline` is the default backend, displaying the plot as a static image:

```
%matplotlib inline
```

`qtagg` is the default backend used by a Python script, displaying the plot in its own interactive window:

```
%matplotlib qtagg
```

`widget` displays the plot interactively in a cell output:

```
%matplotlib widget
```

## TeX

The TeX used in the figure, can be added to markdown:

```markdown
'$2 \pi x \sin{x}$'
```

<img src='./images/img_056.png' alt='img_056' width='600'/>

<img src='./images/img_057.png' alt='img_057' width='600'/>

<img src='./images/img_058.png' alt='img_058' width='600'/>

## Cell Output Options

A docstring can be returned to a cell output using:

```python
plt.plot?
```

Since this is a long docstring, the cell output can be right clicked:

<img src='./images/img_059.png' alt='img_059' width='600'/>

And enable scrolling for output can be selected:

<img src='./images/img_060.png' alt='img_060' width='600'/>

<img src='./images/img_061.png' alt='img_061' width='600'/>

## Cell Execution Order

If the code in first cell is modified to also import pandas and rerun, notice it is now updated from `In [1]` to `In [6]`:

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
```

<img src='./images/img_062.png' alt='img_062' width='600'/>

The `ndarray` instances `x` and `y` can also be returned to a cell output:

<img src='./images/img_063.png' alt='img_063' width='600'/>

The `DataFrame` class is a commonly used data structure within a notebook and can be returned to a cell output:

```python
df = pd.DataFrame({'x': x, 'y': y})
df
```

<img src='./images/img_064.png' alt='img_064' width='600'/>

Or displayed in the variable inspector:

<img src='./images/img_065.png' alt='img_065' width='600'/>

<img src='./images/img_066.png' alt='img_066' width='600'/>

<img src='./images/img_067.png' alt='img_067' width='600'/>

## JupyterLab Spreadsheet Editor

If the `DataFrame` is exported to a `csv` file and `xlsx` file:

<img src='./images/img_068.png' alt='img_068' width='600'/>

<img src='./images/img_069.png' alt='img_069' width='600'/>

Notice that the csv file can be opened in JupyterLab because the spreadsheet editor extension is installed:

<img src='./images/img_070.png' alt='img_070' width='600'/>

This extension unfortunately doesn't support the `xlsx` file:

<img src='./images/img_071.png' alt='img_071' width='600'/>

The notebook file can be renamed in the file explorer. Notice the tab name is also updated, the tab name can also be used to rename the file:

<img src='./images/img_072.png' alt='img_072' width='600'/>

<img src='./images/img_073.png' alt='img_073' width='600'/>

<img src='./images/img_074.png' alt='img_074' width='600'/>

## Notebook and IPython Kernel

The notebook can be saved, using the file menu:

<img src='./images/img_075.png' alt='img_075' width='600'/>

If the notebook is closed:

<img src='./images/img_076.png' alt='img_076' width='600'/>

And reopened from the file explorer:

<img src='./images/img_077.png' alt='img_077' width='600'/>

It displays in the same state as before however the IPython console associated with the notebook file has been exited:

<img src='./images/img_078.png' alt='img_078' width='600'/>

The Kernel menu in the title bar can be used to Restart the Kernel and Clear All Cell Outputs:

<img src='./images/img_079.png' alt='img_079' width='600'/>

Select Restart:

<img src='./images/img_080.png' alt='img_080' width='600'/>

Now each cell can be run by selecting `⇧`+`↵`:

<img src='./images/img_081.png' alt='img_081' width='600'/>

<img src='./images/img_082.png' alt='img_082' width='600'/>

To run a cell and insert a new one below, `Alt`+`↵` can be used:

<img src='./images/img_083.png' alt='img_083' width='600'/>

There is also the option to Restart the Kernel and Run All Cells:

<img src='./images/img_084.png' alt='img_084' width='600'/>

Select Restart:

<img src='./images/img_085.png' alt='img_085' width='600'/>

Notice all the cells (with code) are now run from top to bottom:

<img src='./images/img_086.png' alt='img_086' width='600'/>

The run and the kernel menu have other options:

<img src='./images/img_087.png' alt='img_087' width='600'/>

## JupyterLab Code Formatter

The JupyterLab code formatter extension has been installed. If the code in `In [3]` is modified to have poor formatting. The cell can be right clicked and Format Cell can be selected:

<img src='./images/img_088.png' alt='img_088' width='600'/>

Notice that the spacing in `In [3]` is now PEP8 compliant. If `In [2]` is now selected and formatted:

<img src='./images/img_089.png' alt='img_089' width='600'/>

Notice the string quotations have been changed from `""` to `''`. This is because the formatting preference of black has been used, which differs from the formatting preference in the Python programming language itself:

<img src='./images/img_090.png' alt='img_090' width='600'/>

In Settings, the Settings editor can be examined:

<img src='./images/img_091.png' alt='img_091' width='600'/>

The JupyterLab Code Formatter extension can be selected. To the right the JSON settings editor can be selected:

<img src='./images/img_092.png' alt='img_092' width='600'/>

<img src='./images/img_093.png' alt='img_093' width='600'/>

If the system defaults are copied over to the user preferences, blacks, string_normalization (to double quotes) can be set to False:

<img src='./images/img_094.png' alt='img_094' width='600'/>

Now when Format Cell is used, the string quotations will remain unchanged:

<img src='./images/img_095.png' alt='img_095' width='600'/>

<img src='./images/img_096.png' alt='img_096' width='600'/>

Note cells can be formatted individually, or the format notebook button cna be selected to format all notebook cells:

<img src='./images/img_097.png' alt='img_097' width='600'/>

## Markdown

Images can be inserted in a markdown. Usually they are stored in the same folder ad the notebook or markdown file or a subfolder:

<img src='./images/img_098.png' alt='img_098' width='600'/>

JupyterLab can also be used to create or edit a markdown file. A new tab can be opened to display a new launcher and create a markdown file. It is common to have a `readme.md` in the folder of a Python project:

<img src='./images/img_099.png' alt='img_099' width='600'/>

The following heading and image can be added:

```markdown
# JupyterLab

## Insert Image

The *following* **figure** will be inserted:

![figure1](fig1.png)
```

Blank space in the markdown file can be right clicked and the Show Markdown Preview can be selected:

<img src='./images/img_100.png' alt='img_100' width='600'/>

The table of contents displays the markdown headings in the markdown file:

<img src='./images/img_101.png' alt='img_101' width='600'/>

## Contextual Help

A new tab can be created to display a new launcher:

<img src='./images/img_102.png' alt='img_102' width='600'/>

Contextual Help can be selected:

<img src='./images/img_103.png' alt='img_103' width='600'/>

This will display the help of the currently selected identifier:

<img src='./images/img_104.png' alt='img_104' width='600'/>

<img src='./images/img_105.png' alt='img_105' width='600'/>

## Exiting JupyterLab

To close JupyterLab, close all tabs and then the tab in the browser itself:

<img src='./images/img_106.png' alt='img_106' width='600'/>

The visual elements are now closed but the server ran in the terminal still displays:

<img src='./images/img_107.png' alt='img_107' width='600'/>

Press `Ctrl`+`c` to cancel the currently running operation in the terminal:

<img src='./images/img_108.png' alt='img_108' width='600'/>

<img src='./images/img_109.png' alt='img_109' width='600'/>

## Jupyter Acronym

Jupyter is an acronym for **Ju**lia, **Py**thon **et** **R** and as the name suggests supports the three programming languages Julia, Python and R.

Although `conda` is strongly associated with Python it is actually a general purpose data science package manager and supports the R programming language. 

Currently there is limited support for the Julia programming language supporting only Linux and Mac. The `conda-forge` package is a significantly older version of Julia. 

## R Kernel

If the (conda) Python environment `jupyter-env` is activated, the following R packages can be installed:

```bash
conda install r-irkernel jupyter-lsp-r r-tidyverse r-ggthemes r-palmerpenguins r-writexl 
```

<img src='./images/img_110.png' alt='img_110' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_111.png' alt='img_111' width='600'/>

Now when the `jupyter-lab` binary is launched:

```bash
jupyter-lab
```

<img src='./images/img_112.png' alt='img_112' width='600'/>

It has options for the R programming language:

<img src='./images/img_113.png' alt='img_113' width='600'/>

## Julia Kernel

The `conda` package manager has limited support for Julia. It is recommended to download the latest binary from [Julia](https://julialang.org/):

<img src='./images/img_114.png' alt='img_114' width='600'/>

This can be extracted:

<img src='./images/img_115.png' alt='img_115' width='600'/>

Giving a Julia subfolder:

<img src='./images/img_116.png' alt='img_116' width='600'/>

Which can be copied to Home:

<img src='./images/img_117.png' alt='img_117' width='600'/>

Notice it has its own bin and lib folder:

<img src='./images/img_118.png' alt='img_118' width='600'/>

Installing `julia` using the `conda-forge` package is not recommended at present, as it is significantly out of date:

```bash
conda activate jupyter-env
conda install julia
```

However installation of `julia` via the `conda-forge` package will integrate these folders with the existing folders in the (conda) Python environment `jupyter-env`. Checks need to be made to avoid naming conflicts, which is why the `conda-forge` package is out of date.

If blank space in the bin folder is right clicked and opened in the terminal:

<img src='./images/img_119.png' alt='img_119' width='600'/>

The Julia binary can be started by using:

```bash
./julia
```

where `./` is an instruction to look for the binary in the currently selected directory:

<img src='./images/img_120.png' alt='img_120' width='600'/>

This can be exited using:

```julia
exit()
```

<img src='./images/img_121.png' alt='img_121' width='600'/>

<img src='./images/img_122.png' alt='img_122' width='600'/>

In order to use Julia with JupyterLab, its binary folder needs to be added to the path. This can be done by modifying the `.bashrc` file. This is a hidden file within the Home directory `~`:

<img src='./images/img_123.png' alt='img_123' width='600'/>

Open this file in the text editor:

<img src='./images/img_124.png' alt='img_124' width='600'/>

Notice that a code block that has been added by Spyder to preferentially recognise the binary `spyder` as the standalone installer. 

Below this is the `conda` initialisation which means a search for a binary will preferentially be searched in the activated (conda) Python environment and then fallback to the `base` (conda) Python environment and then fallback to the system binaries. 

* `conda` for example is only installed in the base (conda) Python environment. A search for `conda` will search the currently selected (conda) Python environment `jupyter-env` and not find the binary `conda`. Therefore it will fallback and look for `conda` in the base (conda) Python environment.

* The `.bashrc` preferences the standalone `spyder` and this version of spyder will be preferenced over a spyder binary installed in an activated conda environment.

<img src='./images/img_125.png' alt='img_125' width='600'/>

The following block is added to the `.bashrc` file:

```bash
# >>> Added by Julia >>>
export PATH="$PATH:/path/to.<Julia directory>/bin
# <<< Added by Julia <<<
```

<img src='./images/img_126.png' alt='img_126' width='600'/>

Where in this case `/path/to.<Julia directory>` is `/home/philip/julia-1.11.2/bin`

<img src='./images/img_127.png' alt='img_127' width='600'/>

Now when the terminal is refreshed (closed and reopened). The binary `julia` is recognised:

```bash
julia
```

<img src='./images/img_128.png' alt='img_128' width='600'/>

The Julia Kernel package needs to be added:

```julia
using Pkg
Pkg.add("IJulia")
exit()
```

<img src='./images/img_129.png' alt='img_129' width='600'/>

<img src='./images/img_130.png' alt='img_130' width='600'/>

Now when the (conda) Python envionment `jupter-env` is activated and the `jupyter-lab` binary launched:

```bash
conda activate jupyter-env
jupyter-lab
```

<img src='./images/img_131.png' alt='img_131' width='600'/>

It has options for the Julia programming language:

<img src='./images/img_132.png' alt='img_132' width='600'/>

[Return to Python Tutorials](../readme.md)