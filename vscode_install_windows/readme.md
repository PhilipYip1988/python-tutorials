# VSCode IDE Windows Setup

VSCode is a general purpose code editor that can be configured for Python development. 

## Install VSCode

VSCode can be downloaded from the VSCode website:

* [VScode](https://code.visualstudio.com/download)

Select the Windows Installer (this will default to the User Installer):

<img src='./images/img_001.png' alt='img_001' width='650'/>

Launch the setup:

<img src='./images/img_002.png' alt='img_002' width='650'/>

Accept the License Agreement and select nxt:

<img src='./images/img_003.png' alt='img_003' width='650'/>

Select next:

<img src='./images/img_004.png' alt='img_004' width='650'/>

Select next:

<img src='./images/img_005.png' alt='img_005' width='650'/>

Select next:

<img src='./images/img_006.png' alt='img_006' width='650'/>

Select install:

<img src='./images/img_007.png' alt='img_007' width='650'/>

Select finish:

<img src='./images/img_008.png' alt='img_008' width='650'/>

## Miniforge Installation and Setup

In VSCode to develop in Python, a `conda-forge` environment is required. In order to use conda, Miniforge needs to be installed and in order for the `conda-forge` environment to be activated within VSCode correctly, `conda` needs to be initialised with the Terminal. This was previously covered in:

[Miniforge Install and Initialisation](../spyder_install_windows/readme.md#miniforge-installation)

In order to use TeX in matplotlib plots, MikTeX needs to be installed system wide and added to the Windows path which was also previously covered int he tutorial above.

## Updating the conda Package Manager

Open the Windows Terminal (if this has been initialised, the) The purpose of the `base` environment is to use the conda package manager to install packages in other Python environments. Before using the conda package manager, the conda package manager should be updated to the latest version:

```powershell
conda update conda
```

<img src='./images/img_009.png' alt='img_009' width='650'/>

Since Miniforge is used, the default channel will be the community channel `conda-forge` and since Windows 11 is used, the platform is `win-64`:

<img src='./images/img_010.png' alt='img_010' width='650'/>

Input `y` to proceed:

<img src='./images/img_011.png' alt='img_011' width='650'/>

The conda package manager is now up to date:

<img src='./images/img_012.png' alt='img_012' width='650'/>

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

## Creating a VSCode conda-forge Environment

To create a new environment for VSCode the following command can be used:

```powershell
conda create -n vscode-env notebook jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter pytables lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt ipympl isort autopep8 ruff black
```

<img src='./images/img_013.png' alt='img_013' width='650'/>

Once again since Miniforge is used, the default channel will be the community channel `conda-forge` and since Windows 11 is used, the platform is `win-64`:

<img src='./images/img_014.png' alt='img_014' width='650'/>

Input `y` to proceed:

<img src='./images/img_015.png' alt='img_015' width='650'/>

The environment will be created:

<img src='./images/img_016.png' alt='img_016' width='650'/>

The powerShell Terminal can be closed:

## Installing VSCode Extensions

VSCode is a general purpose code editor and has a variety of extensions for different programming languages:

<img src='./images/img_017.png' alt='img_017' width='650'/>

Install the Python Extension:

<img src='./images/img_018.png' alt='img_018' width='650'/>

Installing this extension, will also install Pylance for code completion and the Python Debugger for debugging:

<img src='./images/img_019.png' alt='img_019' width='650'/>

For interactive Python notebooks, install the Jupyter extension:

<img src='./images/img_020.png' alt='img_020' width='650'/>

This extension will automatically install Jupyter Slide Show, Jupyter Notebook Renderers, Jupyter Keymap and Jupyter Cell Tags:

<img src='./images/img_021.png' alt='img_021' width='650'/>

The IntelliCode extension will give additional code completion:

<img src='./images/img_022.png' alt='img_022' width='650'/>

The isort extension is a formatter which supports imports:

<img src='./images/img_023.png' alt='img_023' width='650'/>

The Code Spell Checker is an English Language Spell checker (similar to spell check in a Word Processor):

<img src='./images/img_024.png' alt='img_024' width='650'/>

In Python, indentation is important and the Python indent extension can make it easier to correctly indent Python code:

<img src='./images/img_025.png' alt='img_025' width='650'/>

The autodocstring is used to quickly generate a template for a Python docstring:

<img src='./images/img_026.png' alt='img_026' width='650'/>

In Python, indentation is important and the indent-rainbow extension can make it easier to visualise indentation levels:

<img src='./images/img_027.png' alt='img_027' width='650'/>

The Black Formatter extension, formats code to comply with PEP8 and adds additional formatting compliant with the black style guide but this style guide differs from the default style used in Python itself:

<img src='./images/img_028.png' alt='img_028' width='650'/>

The Autopep8 Formatter extension, formats code to comply with PEP8 but isn't as through as the black formatter: 

<img src='./images/img_029.png' alt='img_029' width='650'/>

The Pylint extension, is a linter, which is essentially a "grammar and punctuation" checker for code:

<img src='./images/img_030.png' alt='img_030' width='650'/>

Ruff is an improved formatter and linter which has been rewritten in Rust for fast performance:

<img src='./images/img_031.png' alt='img_031' width='650'/>

The Flake8 extension, is another linter, which carries out additional "grammar and punctuation" checks for code:

<img src='./images/img_032.png' alt='img_032' width='650'/>

The Data Wrangler extension is used for viewing Variables in more detail:

<img src='./images/img_033.png' alt='img_033' width='650'/>

Installing the above gives 19 extensions:

<img src='./images/img_034.png' alt='img_034' width='650'/>

It is recommended to refresh VSCode by closing and relaunching to refresh the extensions.

## Project

VSCode is project based. A project is essentially a folder of code, markdown and notebook files. The previous files examined can be copied to a folder called project:

<img src='./images/img_035.png' alt='img_035' width='650'/>

In VSCode select the file explorer to the left and select Open Folder (alternatively select File → Open Folder):

<img src='./images/img_036.png' alt='img_036' width='650'/>

VSCode has a file explorer to the left:

<img src='./images/img_037.png' alt='img_037' width='650'/>

Select Open Folder:

<img src='./images/img_038.png' alt='img_038' width='650'/>

Select the project folder and select, Select Folder:

<img src='./images/img_039.png' alt='img_039' width='650'/>

Select Yes I Trust the Authors:

<img src='./images/img_040.png' alt='img_040' width='650'/>

## Selecting the Python Interpretter 

Selecting the Python Interpretter, is essentially selecting the `python.exe` and the conda-forge environment associated with that `python.exe`. To select the interpretter, press `Ctrl+⇧+p` to open up the command palette:

<img src='./images/img_041.png' alt='img_041' width='650'/>

Search for Python Select Interpretter:

<img src='./images/img_042.png' alt='img_042' width='650'/>

Select the `vscode-env`, (conda) Python environment which has the `~\miniforge3\envs\vscode-env\python.exe`:

<img src='./images/img_043.png' alt='img_043' width='650'/>

It is recommended to refresh VSCode by closing and relaunching to refresh the extensions and Python Interpretter.

## Python Script and Python Shell

To the left hand side the Python Script file can be opened:

<img src='./images/img_044.png' alt='img_044' width='650'/>

Notice Syntax highlighting displays, as well as code linting and spell check:

<img src='./images/img_045.png' alt='img_045' width='650'/>

The script file can be run:

<img src='./images/img_046.png' alt='img_046' width='650'/>

Notice that a PowerShell Terminal displays at the bottom and displays the location of the `python.exe` and the location of the script file. The Terminal Hangs until the plot is closed and the plot is plotting using the QtAgg by default. In other words this is the same behaviour as when a script is run in the Windows terminal using python:

<img src='./images/img_047.png' alt='img_047' width='650'/>

When the plot is closed, the next prompt displays in the Terminal. VSCode has Pylance and IntelliSense installed showing identifiers and docstrings as code is typed:

<img src='./images/img_048.png' alt='img_048' width='650'/>

<img src='./images/img_049.png' alt='img_049' width='650'/>

<img src='./images/img_050.png' alt='img_050' width='650'/>

## Python Script and IPython Shell

Selecting the Run Cell button will instead run the Script file using an IPython Shell:

<img src='./images/img_051.png' alt='img_051' width='650'/>

A kernel may need to be selected when running the first IPython session:

<img src='./images/img_052.png' alt='img_052' width='650'/>

Select, select Another Kernel:

<img src='./images/img_053.png' alt='img_053' width='650'/>

Select Python Environments:

<img src='./images/img_054.png' alt='img_054' width='650'/>

Select the `vscode-env`, (conda) Python environment which has the `~\miniforge3\envs\vscode-env\python.exe`:

<img src='./images/img_055.png' alt='img_055' width='650'/>

Note if there is a prompt to install Python. Close down VSCode to refresh the extensions and Python environments and retry.

Each cell can be ran interactively:

<img src='./images/img_056.png' alt='img_056' width='650'/>

Plots are shown using the inline backend by default:

<img src='./images/img_057.png' alt='img_057' width='650'/>

Variables can be seen by selecting Jupyter Variables:

<img src='./images/img_058.png' alt='img_058' width='650'/>

The `ndarray` can be explored in the Data Wrangler extension:

<img src='./images/img_059.png' alt='img_059' width='650'/>

Select Allow:

<img src='./images/img_060.png' alt='img_060' width='650'/>

The Data Wrangled Variable displays in a seperate tab:

<img src='./images/img_061.png' alt='img_061' width='650'/>

## Notebook

VSCode can also be used to run a Notebook and the layout is similar to the layout previously examined in JupyterLab. Select Run All to run all the cells:

<img src='./images/img_062.png' alt='img_062' width='650'/>

When the first notebook is run, a prompt for a Python Environment will be displayed, select Python Environments:

<img src='./images/img_063.png' alt='img_063' width='650'/>

Select the `vscode-env`, (conda) Python environment which has the `~\miniforge3\envs\vscode-env\python.exe`:

<img src='./images/img_064.png' alt='img_064' width='650'/>

Note if there is a prompt to install Python. Close down VSCode to refresh the extensions and Python environments and retry.

<img src='./images/img_065.png' alt='img_065' width='650'/>

The notebook displays similarly to how it displays in JupyterLab:

<img src='./images/img_066.png' alt='img_066' width='650'/>

In VSCode, docstrings are truncated by default:

<img src='./images/img_067.png' alt='img_067' width='650'/>

However they can be viewed as scrollable elements:

<img src='./images/img_068.png' alt='img_068' width='650'/>

<img src='./images/img_069.png' alt='img_069' width='650'/>

Plots are displayed by default using the `inline` backend, however the backend can be changed using `%matplotlib` in the same way as previously seen when using JupyterLab:

<img src='./images/img_070.png' alt='img_070' width='650'/>

## Formatters and Linters

Press `Ctrl+⇧+p` to open up the command palette:

<img src='./images/img_071.png' alt='img_071' width='650'/>

Search for organize imports:

<img src='./images/img_072.png' alt='img_072' width='650'/>

Select isort or Ruff (which also uses isort):

<img src='./images/img_073.png' alt='img_073' width='650'/>

The imports are now grouped alphabetically into groups (standard modules and third-party modules):

<img src='./images/img_074.png' alt='img_074' width='650'/>

Press `Ctrl+⇧+p` to open up the command palette and search for Format Document With...:

<img src='./images/img_075.png' alt='img_075' width='650'/>

Select autopep8:

<img src='./images/img_076.png' alt='img_076' width='650'/>

This corrects the spacing around the assignment `=` and around `,` delimiters but other operators are not spaced out as expected:

<img src='./images/img_077.png' alt='img_077' width='650'/>

Press `Ctrl+⇧+p` to open up the command palette and search for Format Document With...and select the black formatter:

<img src='./images/img_078.png' alt='img_078' width='650'/>

The spacing around other operators is now corrected but unfortunately black changed all string quotations from single to double, differing from the default Python style:

<img src='./images/img_079.png' alt='img_079' width='650'/>

The Ruff formatter uses the black formatter by default. However it can be customised with a `ruff.toml` file which is placed within the project folder. For more details see [Configuring Ruff](https://docs.astral.sh/ruff/configuration/#__tabbed_1_2):

```python
[format]
# Use single quotes in `ruff format`.
quote-style = "single"
```

<img src='./images/img_080.png' alt='img_080' width='650'/>

Press `Ctrl+⇧+p` to open up the command palette and search for Format Document With...and select the Ruff formatter:

<img src='./images/img_081.png' alt='img_081' width='650'/>

Now the quote style is single as desired, more closely matching the formatting used within Python itself. The underlined code is flagged up by either the spell checker or code linters:

<img src='./images/img_082.png' alt='img_082' width='650'/>

If the pandas import is examined, there is a complaint that the module is imported but never used which unnecessarily slow down the code run time:

<img src='./images/img_083.png' alt='img_083' width='650'/>

Many of the identifiers or input parameters will be flagged as spelling mistakes. View problem can be selected and this input parameter option can be added to the user settings:

<img src='./images/img_084.png' alt='img_084' width='650'/>

Once this input parameter is added to the user settings, it is recognised by the linter and the input parameter option will no longer be aligned.

## Other Extensions

If a `.csv` file is opened, there will be details about the Rainbow Extension, select Install:

<img src='./images/img_085.png' alt='img_085' width='650'/>

<img src='./images/img_086.png' alt='img_086' width='650'/>

Each column in the `.csv` is now colour-coded making it easier to read:

<img src='./images/img_087.png' alt='img_087' width='650'/>

If the `.xlsx` file is attempted to be opened, there is a warning:

<img src='./images/img_088.png' alt='img_088' width='650'/>

The Excel Viewer Extension can be installed:

<img src='./images/img_089.png' alt='img_089' width='650'/>

Now the Excel File can be viewed in VSCode:

<img src='./images/img_090.png' alt='img_090' width='650'/>

VSCode has additional extensions to enhance markdown capabilities. Also because VSCode is cross-programming language, it also has numerous other extensions for other programming languages, making it suitable for cross-programming language development. These will not be further discussed as this installation guide is for Python development only.

[Return to Python Tutorials](../readme.md)