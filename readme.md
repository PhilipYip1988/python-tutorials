# Python Tutorials

This is a repository of Python tutorials that give an overview of the Python programming language, commonly used Python standard libraries, commonly used datascience libraries numpy, pandas and matplotlib as well as Anaconda/Miniconda and the conda package manager. The tutorials will also cover IPython and the Jupyter ecosystem, particularly focusing on the JupyterLab 4 IDE. The tutorials are in the form of markdown files or interactive Python notebooks. Please feel free to star, share and fork this repository.

## Python Installation

The Anaconda 2023-09 Data Science Python Distribution contains Python and Python Standard Modules, the conda package manager, relatively modern versions of the datascience libraries such as numpy, pandas and matplotlib, Python IDEs such as Spyder and JupyterLab. It also includes Python linters such as pylint, flake8 and pyflakes and Python formatters such as autopep8, isort and black which can greatly help improve code quality. 

Miniconda is a bootstrap version of Anaconda and allows the use of the conda package manager to create Python Environments. The instructions below will equally apply to Miniconda.

### Concise Installation

Anaconda or Miniconda should be installed, updated and initialised for the Windows or Linux Terminal. A conda environment should be created for the newest version of JupyterLab:

```powershell
conda create -n jupyter-env -c conda-forge python jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt isort autopep8 ruff black ipympl jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker ghostscript nbconvert 
```

Follow the detailed installation instructions below if unfamiliar with Anaconda/Miniconda.

### Windows Installation

* [Installing Anaconda or Miniconda](./anaconda/windows/install.md)
* [Using the Conda Package Manager and Managing Conda Python Environments to Install the Latest Version of Spyder and JupyterLab](./anaconda/windows/conda.md)
* [Installing VSCode, Selecting a Python Environment and Configuring Extensions](./anaconda/windows/vscode.md)

### Linux/Mac Installation

* [Installing Anaconda or Miniconda](./anaconda/linux/install.md)
* [Using the Conda Package Manager and Managing Conda Python Environments to Install the Latest Version of Spyder and JupyterLab](./anaconda/linux/conda.md)
* [Installing VSCode, Selecting a Python Environment and Configuring Extensions](./anaconda/linux/vscode.md)

For Linux, Ubuntu will be used as an example distro but the procedure is the same on most other distros. The Mac Terminal and File System are Linux Based and therefore installation on Mac should therefore be more or less identical to Linux.

## Markdown

Markdown uses simple syntax to format text and is commonly used on GitHub and within Interactive Python Notebooks. For mathematical equations it is supplemented using TeX:

* [Markdown and TeX Syntax](./markdown/readme.md)

## Viewing Markdown Files and Notebook Files

These tutorials use markdown and notebook files and can be viewed in the browser or in an IDE such as JupyterLab or VSCode:

* [Viewing and Running Files](./viewing_notebooks/viewing.md)

## Builtins Module

The builtins module is automatically imported. It contains Pythons fundamental classes. These classes are based around the object class and the builtins module contains the functions which are used to invoke object based datamodel methods:

* [Object Class](./builtins_module_object/notebook.ipynb)
* [Immutable String Class](./builtins_module_str/notebook.ipynb)
* [Immutable Bytes Class](./builtins_module_bytes/notebook.ipynb)
* [Mutable ByteArray Class](./builtins_module_bytearray/notebook.ipynb)
* [Immutable Integer Class](./builtins_module_int/notebook.ipynb)
* [Immutable Floating Point Class](./builtins_module_float/notebook.ipynb)
* [Immutable Boolean Class](./builtins_module_bool/notebook.ipynb)
* [Immutable Tuple Class](./builtins_module_tuple/notebook.ipynb)
* [Mutable List Class](./builtins_module_list/notebook.ipynb)
* [Immutable FrozenSet Class](./builtins_module_frozenset/notebook.ipynb)
* [Mutable Set Class](./builtins_module_set/notebook.ipynb)
* [Mutable Dictionary Class](./builtins_module_dict/notebook.ipynb)

## IPython Magics

The Interactive Python Shell has a number of enhancements over the regular Python Shell. It can be used to run Python code and commonly used Shell commands that have been reimplemented as IPython magics. The Shell used for these commands will differ depending on the Operating System:

* [IPython Magics on Windows](./ipython_magics/notebook_windows.ipynb)
* [IPython Magics on Linux/Mac](./ipython_magics/notebook_linux.ipynb)

## Formatters

Python has a number of formatters that can be used to format code:

* [Code Formatters on Windows (AutoPEP8, ISort, Black and Ruff)](./formatters/notebook_windows.ipynb)
* [Code Formatters on Linux/Mac (AutoPEP8, ISort, Black and Ruff)](./formatters/notebook_linux.ipynb)
* [JupyterLab Code Formatter Extension (AutoPEP8, ISort and Black)](./formatters/notebook_jupyterlab_code_formatter_extension.ipynb)

## Collections and Code Blocks

A Python code block can be used to direct Python code in response to a condition, loop a series of operations again and again, perform error handling and to create custom functions:

* [Code Blocks](./programming_constructs/notebook.ipynb)

## Collections Module

The collections module contains a number of supplementary collections based around the collections seen in the Python builtins module. This includes the ```namedtuple```, ```deque```, ```Counter``` and ```defaultdict``` classes:

* [Collections Module](./collections_module/notebook.ipynb)

## Itertools Module

The itertools module contains supplementary iterators that are closely related to and extend those found in Python builtins:

* [Itertools Module](./itertools_module/notebook.ipynb)

## Math and Complex Math Modules

The math and complex math modules contain commonly used mathematical functions typically returning scalar values:

* [Math and Complex Math Modules](./math_module/notebook.ipynb)

## Statistics Module

The statistics module is a functional module covering basic statistics:

* [Statistics Module](./statistics_module/notebook.ipynb)

## Random Module

The random module is used to generate a random scalar number, often from a distribution:

* [Random Module](./random_module/notebook.ipynb)

## Datetime Module

The datetime module is used to generate scalar date, times, datetimes and timedeltas (time differences):

* [Datetime Module](./datetime_module/notebook.ipynb)

## File Formats

The Input Output (IO) module is used for reading and writing text files .txt and binary files .bin. The IO module is commonly used with the Comma Separated Values (CSV) Module for reading and writing comma separated files .csv, printed format files .prn and text delimited files .tab. The IO module is also commonly used with the JavaScript Object Notation (JSON) module for reading and writing JavaScript object notation files .json. The above are all examples of high level human-readable formats. Data can also be serialised using the pickle module which uses pickle files .pkl and serialised data can be stored in a database using the shelve module:

* [File Formats Windows](./io_module/notebook_windows.ipynb)
* [File Formats Linux](./io_module/notebook_linux.ipynb)

## Operating System Module

The Operating System module is essentially a Python implementation of the Shell programming languages and contains commands to navigate around the Operating System:

* [Operating System Module Windows](./os_module/notebook_windows.ipynb)
* [Operating System Module Linux](./os_module/notebook_linux.ipynb)

## Path Library Module

The Path and Library module is similar to the Operating System Module however uses an Object Orientated Programming (OOP) approach to file paths and libraries within the user profile or home directory. File paths are returned as instances of the Path class which have a number of useful attributes and the ```/``` operator can be used for folder and file concatenation:

* [Path and Library Windows](./pathlib_module/notebook_windows.ipynb)
* [Path and Library Linux](./pathlib_module/notebook_linux.ipynb)

## System Module

The System module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter:

* [System Module](./sys_module/notebook.ipynb)

## The Numeric Python Library

The Numeric Python library is based upon the data structure of the NDimensional Array. This is a datastructure that is a collection however unlike ```builtins``` collections, all the datamodel methods are configured for numeric operations. numpy also broadcasts the functions found in the math, datetime and random modules to an ndarray:

* [NDimensional Array Class](./numpy_library/notebook.ipynb)

## The Python and Data Analysis Library

The Python and Data Analysis library builds upon the data structure of the ndarray, creating a Series which is a 1D Array (1D) with a column name and a DataFrame which is a grouping of Series analogous in form to an Excel SpreadSheet. The Python and Data analysis library can be used to programmatically manipulate the data stored in the DataFrame analogous to any data operations that would be carried out manually in Excel:

* [Index, Series and DataFrame Classes](./pandas_library/notebook.ipynb)

## The Matrix Plotting Library

The matrix plotting library encompasses a large group of modules compartmentalising objects used for visual elements in a plot. As a user generally only the Python Plot Module is used which allows manipulation of the above objects using a simplified functional and object-orientated programming syntax:

* [Python Plot Module](./matplotlib_library/notebook.ipynb)
* [Plot Backends Comparison](./matplotlib_library/notebook_backends.ipynb)

## The Data Visualisation Library

seaborn is a wrapper library for matplotlib which greatly simplifies the code required to create plots that are commonly used for data visualisation of data stored in a DataFrame:

* [Data Visualisation Library](./seaborn_library/notebook.ipynb)

## The Plotly Library

plotly is a Python plotting library that creates plots using nodejs. This allows plots to be displayed interactively in the cell output of an interactive Python notebook:

* [Plotly Library](./plotly_library/notebook.ipynb)

## The Python Imaging Library

The Python Imaging Library contains the Image module which contains the Image data structure. This module is used for Image construction from an ndarray or an image file taken from another image manipulation program or camera:

* [The Python Imaging Library](./pillow_library/notebook.ipynb)