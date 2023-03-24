# The Python Ecosystem

The Python ecosystem is pretty vast and a consequence there are a multitude of ways to install and use Python, offering great flexibility. On the other hand due to this flexibility, the process of installation appears fragmented and can become very confusing for a begineer. 

## Package Managers and Distributions

There are three package managers commonly used to install Python and Python packages. 

|Installer Name|Package Manager|Python Base Environment|Python Base Environment Channel|Python Version in Base Environment|
|:-:|:-:|:-:|:-:|:-:|
|Python|pip|minimal|pip|3.11|
|Mambaforge|mamba|minimal|conda-forge|3.10|
|Miniforge|conda|minimal|conda-forge|3.10|
|Anaconda|conda|data science distribution|conda (older packages)|3.10|
|Miniconda|conda|minimal|conda (older packages)|3.10|

**In this guide Mambaforge will be used as it is the most reliable solution.** Seperate Python 3.11 environments will be made for each IDE. Anaconda has been updated to include a recent version of JupyterLab and a recent version of Spyder. The version of Spyder 5.4.1 unfortuantely lacks the code completion fixes of Spyder 5.4.2.

Python Version Numbers are of the format X.Y.Z for example version 3.11.2 where X is the major version 3, Y is the minor version 11 and Z is the patch version 2. 

A new minor version of Python 3 is developed each year. Python 3.12.0 for example is currently in development. It is recommended to wait for a patch number of at least version 1, which usually indicates that the most significant bug fixes have been addressed. In addition it also means that the developers of popular Python libraries have had enough time to update their libraries allowing them to run on this new minor version. Python libraries are installed as Python packages which follow the same X.Y.Z format.

## Integrated Development Environments (IDEs)

Once Python is installed, it can be used with the Mambaforge Prompt/Terminal, a text editor and a file explorer. These three components are typically inbuilt into the Operating System. These three components also form the basis of a Python Integrated Development Environment often abbreviated as an IDE.

Python has numerous IDEs. This guide will configure four of common IDEs and outline their features:

* IDLE
* Spyder
* JupyterLab
* Visual Studio Code

## Detailed Installation Instructions

A begineer should install Mambaforge using the detailed guides:

[Mambaforge Install on Windows](./001_windows_install/)

[Mambaforge Install on Linux/Mac](./002_linux_install/)

## Brief Installation Instructions

An experienced user may wish to use only the brief installation instructions:

### Mambaforge

The Mambaforge Installer needs to be downloaded. It can be installed in Windows using the application. In Linux/Mac, it needs to be installed using the Terminal:

[Mambaforge installer](https://github.com/conda-forge/miniforge#mambaforge) 

### Updating the base env

To update the Python base environment use:

```
mamba update --all
```

### Spyder env

To create a new Python environment for the latest version of the Spyder IDE including its optional dependencies use:

```
mamba create -n spyder
mamba activate spyder
mamba install spyder=5.4.2 python=3.11 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

To launch Spyder use:

```
mamba activate spyder
spyder
```

### JupyterLab env

To create a new Python environment for the latest version of the JupyterLab IDE including its optional dependencies use:

```
mamba create -n jupyterlab
mamba activate jupyterlab
mamba install jupyterlab python=3.11 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs ipywidgets plotly jupyterlab-variableinspector ipympl pyqt
jupyter lab build
```

To launch JupyterLab use:

```
mamba activate jupyterlab
jupyter lab
```

### VSCode env

To create a new Python environment for the latest version of the Visual Studio Code IDE use:

```
mamba create -n vscode
mamba activate vscode
mamba install -c  python=3.11 notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs ipywidgets plotly ipympl pyqt
```

[Visual Studio Code](https://code.visualstudio.com/#alt-downloads) needs to be installed seperately using the appropriate package for your Operating System.

Once installed, launch Visual Studio Code using the start menu shortcut. Alternatively laubnch it from the Mambaforge Prompt (Windows)/Terminal (Linux) using:

```
mamba activate vscode-cf
code
```

The Python extension should be installed within Visual Studio Code. 

The Python Interpretter should be selected. In Visual Studio Code press ```ctrl```, ```⇧``` and ```p``` to open up the command palette. Search for interpretter and select Python: Select Interpretter. Change the interpretter to the ```vscode``` Python environment.

[Home Python Tutorials](https://github.com/PhilipYip1988/python-tutorials/blob/main/readme.md)
