# VSCode Ubuntu Setup

VSCode is a general purpose code editor that can be configured for Python development. 

## Install VSCode

Open up Ubuntu Software and search for code:

<img src='./images/img_001.png' alt='img_001' width='600'/>

Select Install:

<img src='./images/img_002.png' alt='img_002' width='600'/>

VSCode is now installed:

<img src='./images/img_003.png' alt='img_003' width='600'/>

## Miniforge Installation and Setup

To develop in Python, a `conda-forge` environment is required. In order to use conda, Miniforge needs to be installed and in order for the `conda-forge` environment to be activated within VSCode correctly, `conda` needs to be initialised with the Terminal. This was previously covered in:

[Miniforge Install and Initialisation](../spyder_install_ubuntu/readme.md#miniforge-installation)

In order to use TeX in matplotlib plots. TeX needs to be installed system wide using the operating systems package manager (which was also previously covered in the above):

```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic cm-super dvipng
```

## Updating the conda Package Manager

The purpose of the `base` environment is to use the conda package manager to install packages in other Python environments. Before using the conda package manager, the conda package manager should be updated to the latest version:

```bash
conda update conda
```

<img src='./images/img_004.png' alt='img_004' width='600'/>

Since Miniforge is used, the default channel will be the community channel `conda-forge`:

<img src='./images/img_005.png' alt='img_005' width='600'/>

Input `y` in order to proceed with any changes. In this example the `conda` package manager is already up to date:

<img src='./images/img_006.png' alt='img_006' width='600'/>

<img src='./images/img_007.png' alt='img_007' width='600'/>

Note there is an issue going from `conda` 24 to 25 where it doesn't update properly and says:

```
==> WARNING: A newer version of conda exists <==
current version: 24.w.w
latest version: 25.x.x

Please update conda by running:

conda update -n base -c conda-forge conda
```

And inputting the command listed takes you back to the same screen. To bypass this use:

```bash
conda install conda=25.x.x
```

Where `25.x.xx` should be replaced by the latest version number.

## Creating a VSCode conda-forge Environment

To create a new environment for VSCode the following command can be used:

```bash
conda create -n vscode-env notebook jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter pytables lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt ipympl isort autopep8 ruff black
```

<img src='./images/img_008.png' alt='img_008' width='600'/>

Since Miniforge is used, the default channel will be the community channel `conda-forge`:

<img src='./images/img_009.png' alt='img_009' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_010.png' alt='img_010' width='600'/>

The Python environment is created:

<img src='./images/img_011.png' alt='img_011' width='600'/>

## Installing Extensions

VSCode is a general purpose code editor and can be configured with extensions. To the left hand side select extensions:

<img src='./images/img_012.png' alt='img_012' width='600'/>

<img src='./images/img_013.png' alt='img_013' width='600'/>

For Python development, the Python extension needs to be installed:

<img src='./images/img_014.png' alt='img_014' width='600'/>

Installing this extension will also install Pylance which is used for Python code completion and the Python debugger which is used for debugging. These three extensions are listed under the installed category:

<img src='./images/img_015.png' alt='img_015' width='600'/>

For interactive Python notebooks, the Jupyter extension can be installed:

<img src='./images/img_016.png' alt='img_016' width='600'/>

This installs Jupyter Keymaps, Notebook renderers, Cell Tags and Slideshow:

<img src='./images/img_017.png' alt='img_017' width='600'/>

Intellicode is additional code completion:

<img src='./images/img_018.png' alt='img_018' width='600'/>

isort is a formatter that sorts imports in Python:

<img src='./images/img_019.png' alt='img_019' width='600'/>

Code spell checker is an English spell checker:

<img src='./images/img_020.png' alt='img_020' width='600'/>

Python indent is used to help structure indented Python code:

<img src='./images/img_021.png' alt='img_021' width='600'/>

Python autodocstring is used to generate a template for docstrings:

<img src='./images/img_022.png' alt='img_022' width='600'/>

Indent rainbow is used to highlight indented Python code:

<img src='./images/img_023.png' alt='img_023' width='600'/>

Black is the black formatter:

<img src='./images/img_024.png' alt='img_024' width='600'/>

AutoPEP8 is the autopep8 formatter:

<img src='./images/img_025.png' alt='img_025' width='600'/>

Pylint gives additional Python linting:

<img src='./images/img_026.png' alt='img_026' width='600'/>

Ruff is the Ruff formatter and linter:

<img src='./images/img_027.png' alt='img_027' width='600'/>

Flake8 gives additional Python linting:

<img src='./images/img_028.png' alt='img_028' width='600'/>

Data wrangler is used to help visualise variables:

<img src='./images/img_029.png' alt='img_029' width='600'/>

It is recommended to close and reopen VSCode once installing the above extensions

## Project

When using VSCode, markdown files (normally a readme.md), script files and notebook files are grouped together in a folder, known as the project folder. Select Open Folder:

<img src='./images/img_030.png' alt='img_030' width='600'/>

In this case, the project folder is the Documents folder:

<img src='./images/img_031.png' alt='img_031' width='600'/>

Select open:

<img src='./images/img_032.png' alt='img_032' width='600'/>

Select Yes I trust the authors:

<img src='./images/img_033.png' alt='img_033' width='600'/>

## Selecting the Python Interpreter

To use Python with VSCode, the Python interpreter needs to be selected. This is similar to activating the conda environment. Press `Ctrl`+`⇧`+`p` to open the command palette:

<img src='./images/img_034.png' alt='img_034' width='600'/>

Search for Python select interpreter: 

<img src='./images/img_035.png' alt='img_035' width='600'/>

Select the vscode-env created earlier:

<img src='./images/img_036.png' alt='img_036' width='600'/>

## Python Script and Python Shell

To the left hand side the Python Script file can be opened:

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
plt.show()
```

<img src='./images/img_037.png' alt='img_037' width='600'/>

It displays in its own tab and can be run using the run button:

<img src='./images/img_038.png' alt='img_038' width='600'/>

Since this has the instruction `plt.show()`, the plot displays. Notice that the terminal is still busy while the plot displays, because it is waiting for the main window of the Qt application to close (the plot backend is qtagg):

<img src='./images/img_039.png' alt='img_039' width='600'/>

When this is closed, the new prompt displays. If the terminal in VSCode, is examined, note that the base Python environment is activated, however when the run button is used, the currently selected Python interpreter is used, which is the python binary in `vscode-env`. The full path to this Python binary is displayed in the terminal alongside the script file that was run:

<img src='./images/img_040.png' alt='img_040' width='600'/>

VSCode has Pylance and IntelliSense installed showing identifiers and docstrings as code is typed:

<img src='./images/img_041.png' alt='img_041' width='600'/>

<img src='./images/img_042.png' alt='img_042' width='600'/>

<img src='./images/img_043.png' alt='img_043' width='600'/>

## Python Script and IPython Shell

Selecting the Run Cell button will instead run the Script file using an IPython Shell:

<img src='./images/img_044.png' alt='img_044' width='600'/>

<img src='./images/img_045.png' alt='img_045' width='600'/>

<img src='./images/img_046.png' alt='img_046' width='600'/>

Variables can be seen by selecting Jupyter Variables:

<img src='./images/img_047.png' alt='img_047' width='600'/>

The `ndarray` can be explored in the Data Wrangler extension:

<img src='./images/img_048.png' alt='img_048' width='600'/>

Select Allow:

<img src='./images/img_049.png' alt='img_049' width='600'/>

The Data Wrangled Variable displays in a seperate tab:

<img src='./images/img_050.png' alt='img_050' width='600'/>

Plots are shown using the inline backend by default:

<img src='./images/img_051.png' alt='img_051' width='600'/>

## Notebook

VSCode can also be used to run a Notebook and the layout is similar to the layout previously examined in JupyterLab. Select Run All to run all the cells and then select Python Environments:

<img src='./images/img_052.png' alt='img_052' width='600'/>

Select the `vscode-env`, (conda) Python environment which has the binary `~/miniforge3/envs/vscode-env/bin/python`:

<img src='./images/img_053.png' alt='img_053' width='600'/>

The notebook displays similarly to how it displays in JupyterLab:

<img src='./images/img_054.png' alt='img_054' width='600'/>

<img src='./images/img_055.png' alt='img_055' width='600'/>

In VSCode, docstrings are truncated by default:

<img src='./images/img_056.png' alt='img_056' width='600'/>

However they can be viewed as scrollable elements:

<img src='./images/img_057.png' alt='img_057' width='600'/>

<img src='./images/img_058.png' alt='img_058' width='600'/>

Plots are displayed by default using the `inline` backend, however the backend can be changed using `%matplotlib` in the same way as previously seen when using JupyterLab:

<img src='./images/img_059.png' alt='img_059' width='600'/>

## Formatters and Linters

Returning the the Python Script file. Press `Ctrl+⇧+p` to open up the command palette. Select Format Document With...:

<img src='./images/img_061.png' alt='img_061' width='600'/>

Select autopep8:

<img src='./images/img_062.png' alt='img_062' width='600'/>

This corrects the spacing around the assignment `=` and around `,` delimiters but other operators are not spaced out as expected:

<img src='./images/img_063.png' alt='img_063' width='600'/>

Press `Ctrl+⇧+p` to open up the command palette and search for organize imports, select organize imports:

<img src='./images/img_064.png' alt='img_064' width='600'/>

Then select isort:

<img src='./images/img_065.png' alt='img_065' width='600'/>

The imports are now grouped alphabetically into groups (standard modules and third-party modules, in this case no standard modules aren't used so only one list of third-party modules displays):

<img src='./images/img_066.png' alt='img_066' width='600'/>

Press `Ctrl+⇧+p` to open up the command palette and search for Format Document With...:

<img src='./images/img_067.png' alt='img_067' width='600'/>

Select the Black Formatter:

<img src='./images/img_068.png' alt='img_068' width='600'/>

The spacing around other operators is now corrected but unfortunately black changed all string quotations from single to double, differing from the default Python style:

<img src='./images/img_069.png' alt='img_069' width='600'/>

The Ruff formatter uses the black formatter by default. However it can be customised with a `ruff.toml` file which is placed within the project folder. For more details see [Configuring Ruff](https://docs.astral.sh/ruff/configuration/#__tabbed_1_2):

```python
[format]
# Use single quotes in `ruff format`.
quote-style = "single"
```

<img src='./images/img_070.png' alt='img_070' width='600'/>

<img src='./images/img_071.png' alt='img_071' width='600'/>

Press `Ctrl+⇧+p` to open up the command palette and search for Format and select Ruff or Format Document With... and select Ruff:

<img src='./images/img_072.png' alt='img_072' width='600'/>

Now the quote style is single as desired, more closely matching the formatting used within Python itself. The underlined code is flagged up by either the spell checker or code linters:

<img src='./images/img_073.png' alt='img_073' width='600'/>

Formatting can also be carried out on a Notebook. Before using Format Notebook, the default Formatter should be selected. Press `Ctrl+⇧+p` to open up the command palette and search for Format and select Ruff or Format Document With... 

<img src='./images/img_074.png' alt='img_074' width='600'/>

Select Configure Default Formatter...

<img src='./images/img_075.png' alt='img_075' width='600'/>

Select Ruff:

<img src='./images/img_076.png' alt='img_076' width='600'/>

Now select the notebook file. Press `Ctrl+⇧+p` to open up the command palette and search for Format Notebook:

<img src='./images/img_077.png' alt='img_077' width='600'/>

The notebook wil now be formatted:

<img src='./images/img_078.png' alt='img_078' width='600'/>

The underlined code is flagged up by either the spell checker or code linters:

<img src='./images/img_079.png' alt='img_079' width='600'/>

In this case, it is by the spell checker selecting View Problem gives spelling suggestions:

<img src='./images/img_080.png' alt='img_080' width='600'/>

Many identifiers and parameter options will not be recognised. Select add to user settings:

<img src='./images/img_081.png' alt='img_081' width='600'/>

The linting will disappear now that this parameter is recognised:

<img src='./images/img_082.png' alt='img_082' width='600'/>

Other linters will identify other problems with the code which can usually be addressed in a similar way:

<img src='./images/img_083.png' alt='img_083' width='600'/>

## Other Extensions

If a `.csv` file is opened, there will be details about the Rainbow Extension, select Install. Each column in the `.csv` is now colour-coded making it easier to read:

<img src='./images/img_084.png' alt='img_084' width='600'/>

The Excel Viewer Extension can be installed:

<img src='./images/img_085.png' alt='img_085' width='600'/>

Now the Excel File can be viewed in VSCode:

<img src='./images/img_086.png' alt='img_086' width='600'/>

VSCode has additional extensions to enhance markdown capabilities. Also because VSCode is cross-programming language, it also has numerous other extensions for other programming languages, making it suitable for cross-programming language development. These will not be further discussed as this installation guide is for Python development only.

[Return to Python Tutorials](../readme.md)