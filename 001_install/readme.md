# Python Integrated Development Environments (IDEs)

The Python ecosystem is pretty vast and a consequence there are a multitude of ways to install and use Python, offering great flexibility. On the other hand due to this flexibility, the process of installation appears fragmented and can become very confusing for a begineer. 

Once Python is installed, it can be used with the Windows/Linux Terminal, a text editor and a file explorer and these three components are inbuilt into the Operating System. These three components also form the basis of a Python Integrated Development Environment often abbreviated as an IDE.

Python has numerous IDEs which offer additional features such as code-completion. Four of the most common IDEs are:

* IDLE
* Spyder
* JupyterLab
* Visual Studio Code

Detailed installation guides for these four IDEs using the ```mamba``` package manager are available for Windows and Linux. For other Linux distributions and Mac OS, use the Ubuntu Linux guide as the procedure is essentially identical:

[Mambaforge Install on Windows](./001_windows_install/)

[Mambaforge Install on Ubuntu](./002_ubuntu_install/)

Brief installation instructions and a comparison of the package managers are available for those already experienced with Python below. It is recommended for begineers to glance through the comparison of the package managers below and take steps to ensure they use and stick to only using the ```mamba``` package manager.

## Package Manager

There are three package managers commonly used to install Python and Python packages. One of the package managers is included in three slightly different Python distributions:

|Installer Name|Package Manager|Python Base Environment|Python Base Environment Channel|
|:-:|:-:|:-:|:-:|
|Python|pip|minimal|pip|
|Anaconda|conda|data science distribution|conda|
|Miniconda|conda|minimal|conda|
|Miniforge|conda|minimal|conda-forge|
|Mambaforge|mamba|minimal|conda-forge|

### pip

The most simple package manager is ```pip``` which is an abbreviation for Python Install Package. This is the most flexible package manager but does not check for library dependencies or compatible versions. 

In short you can install anything but there is a good chance that a beginner will install a combination of packages that are incompatible with each other or do not have their required dependencies to run. Then as a result will encounter a large number of error messages, when attempting to use data science libraries for example. 

### conda 

The next package manager is ```conda``` which performs a number of dependency checks and looks for compatibility between packages. The ```conda``` package manager uses two main channels:

* ```conda``` the channel maintained by the Anaconda Company
* ```conda-forge``` the community channel

Note that both the package manager and the Anaconda maintained channel are called ```conda```. 

### Anaconda Python Distribution Issues

In theory, a user should be able to install Anaconda and use the ```base``` Python environment which is populated with the most commonly used data science libraries. However in practice, due to the vast size of the Python ecosystem, the Anaconda company are struggling to keep up with all the developments for even the most popular Python packages and as a result their ```conda``` channel is often months or even years behind the  community ```conda-forge``` channel. For example, the ```conda``` channel usually has older versions of popular IDEs such as Spyder and JupyterLab and these older versions contain issues that have been rapidly addressed by developers of the IDEs in newer versions. These versions are only available on the ```conda-forge``` channel because the Anaconda company have not reissued them on the ```conda``` channel. Moreover, there are also many developments in slightly more niche areas that the Anaconda Company has not added to the ```conda``` channel. 

The conda package manager also has a number of drawbacks, it can be quite slow to solve a Python environment (check for compatibility of Python packages) and usually hangs when attempting to solve environments which use packages from multiple channels such as ```conda``` and ```conda-forge```.

Due to the above, there is a high level of confusion when users try and install the latest version of a package, and the latest version on the ```conda``` channel is several releases behind the ```conda-forge``` channel (or if more niche, not available at all on the ```conda``` channel). This results in problems when the ```conda``` package manager is unable to solve the Python environment, particularly when a package from ```conda-forge``` is attempted to be added to the vast ```base``` Python environment in Anaconda which uses the ```conda``` channel. The solution is normally to create a seperate Python environment (sub-installation) including only packages from the ```conda-forge``` channel which generally defeats the purpose of using Anaconda over Miniconda. Miniconda is a stripped Anaconda with a lightweight ```base``` Python environment. Miniforge is essentially the same as Miniconda however the packages in the base environment are from the ```conda-forge``` channel by default instead of the ```conda``` channel.

Finally, the Anaconda Python Datascience Distribution and packages in Anacondas ```conda``` channel have some licensing restrictions when it comes to commercial use. These licensing restrictions are not present for packages in the open-source ```conda-forge``` community channel.

### mamba

The ```mamba``` package manager has been developed by the Python community to address many of the issues behind the ```conda``` package manager. The [Mambaforge installer](https://github.com/conda-forge/miniforge#mambaforge) is essentially the same as the Miniforge installer but includes the ```mamba``` package manager. The rest of this guide will focus only on Mambaforge. 

### Package Managers Syntax:

When using the mamba package manager, you should avoid use of commands which invoke the ```pip``` or ```conda``` package managers, as use of multiple package managers in a single Python environment can result in issues. For example when you see installation commands to install packages:

```
pip install packagename
conda install packagename
conda install -c conda-forge packagename
```

Replace them with:

```
mamba install -c conda-forge packagename
```

The default channel for mambaforge is ```conda-forge```. It is however good practice to explicitly specify, the ```conda-forge``` channel when installing packages. Where possible ensure that the ```conda-forge``` channel is used opposed to the ```conda``` channel. Note some larger developers such as ```pytorch``` use their own channel and you should continue to use their channel when instructed.

## base env

To update the Python base environment using packages from the ```conda-forge``` channel use:

```
mamba update -c conda-forge --all
```

The Python base environment includes IDLE. 

To launch IDLE in Windows use:

```
idle
```

To launch IDLE in Ubuntu Linux use:

```
idle3
```

## Spyder env

To create a new Python environment for the latest version of the Spyder IDE including its optional dependencies use:

```
mamba create -n spyder-cf
mamba activate spyder-cf
mamba install -c conda-forge spyder
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

To launch Spyder use:

```
mamba activate spyder-cf
spyder
```

## JupyterLab env

To create a new Python environment for the latest version of the JupyterLab IDE including its optional dependencies use:

```
mamba create -n jupyterlab-cf
mamba activate jupyterlab-cf
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
mamba install -c conda-forge jupyterlab
mamba install -c conda-forge nodejs ipywidgets 
mamba install -c conda-forge plotly dash jupyter-dash
mamba install -c conda-forge jupyterlab-variableinspector
jupyter lab build
```

To launch JupyterLab use:

```
mamba activate jupyterlab-cf
jupyter lab
```

## VSCode env

To create a new Python environment for the latest version of the Visual Studio Code IDE use:

```
mamba create -n vscode-cf
mamba activate vscode-cf
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
mamba install -c conda-forge notebook nodejs ipywidgets 
mamba install -c conda-forge plotly dash
```

Visual Studio Code needs to be installed seperately using the Windows ```.exe``` or Ubuntu ```.deb``` or Ubuntu ```.snap``` package. 

Once installed, launch Visual Studio Code using:

```
mamba activate vscode-cf
code
```

The Python extension should be installed within Visual Studio Code. 

The Python Interpretter should be selected. In Visual Studio Code press ```ctrl```, ```⇧``` and ```p``` to open up the command palette. Search for interpretter and select Python: Select Interpretter. Change the interpretter to the ```vscode-cf``` ```mamba``` environment.

[Home](../../../)
