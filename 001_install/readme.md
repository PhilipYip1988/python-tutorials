# The Python Ecosystem

Python is a programming language that is under continuous development:
* Python has numerous third-party libraries for data science 
* Python has numerous **I**ntegrated **D**evelopment **E**nvironments (**IDE**s) 

An IDE is essentially a program with a user interfaces for the programmer to interact with the Python programming language.

Installing Python for a begineer can be tricky as the Python ecosystem is so flexible. Installation of Python directly and installation of Python libraries using ```pip``` often results in the installation of Python libraries that are not compatible with each other and therefore lots of error messages! Take a moment to understand the Python ecosystem before installing!

There are essentially three main ways to install Python.

The Python installer:
* The Python Programming Language
* A limited set of inbuilt modules
* The **pip** package manager (**p**ython **i**nstall **p**ackage)
* The IDLE (Integrated Development **L**earner Environment)
Note: ```pip``` is usually too flexible for beginners as it usually installs incompatible versions of packages. 

The Anaconda installer base conda environment contains:
* The Python Programming Language
* The conda package manager
* The Spyder and JupyterLab IDEs
* Numerous Data Science Libraries such as:
    * numpy
    * pandas
    * matplotlib
    * seaborn
    * scipy
    * scikit-learn
    * scikit-image
In theory you should be able to install Anaconda directly and use a preinstalled IDE alongside the inbuilt data science libraries directly from the default (base) conda environment. Note however that the Anaconda installer includes annual versions of the IDEs and data science libraries. These annual versions often contain bugs that have been previously been addressed by developers. The Anaconda installer also has some commercial restrictions. In addition, you will have to eventually use a library not preinstalled, so should learn how to create a conda environment (subinstallation) to install packages in. conda environments can also be created with Miniconda. 

The Miniconda installer base conda environment contains:
* The Python Programming Language
* The conda package manager
Miniconda is essentially a lightweight version of Anaconda without commercial restrictions and has only the bare essentials in the default (base) conda environments. The ```conda``` package manager performs checks to ensure that the packages being installed are compatible. 

# Package Managers: pip vs conda

A Python library can be thought of as a collection of Python code. Therefore when functions from a Python library are called, under the hood some Python code will be executed. As a consequence a compatible version of Python is a required for the Python library and is known as a dependency. When Python is updated the core functionality of the Python programming language may change. When a Python library is configured to use the old core functionality, an error may occur. The Python library will therefore have to be updated in order to be compatible with the newest Python version. In the case of the datascience libraries, numpy can be thought of as the primary datascience library; pandas is built upon numpy and therefore has Python and numpy as dependencies. matplotlib has Python, numpy and pandas as dependencies and seaborn has Python, numpy, pandas and matplotlib as dependencies. It therefore takes time for the developers of these datascience libraries to update the libraries to be compatible with the latest version of Python and to be compatible with each other. This means a standard user will run into issues when using the latest version of Python.

```pip``` - python install package can theoretically be used to install any version of a Python library and gives the greatest flexibility. However this flexibility comes at the compromise of possible broken functionality i.e. conflicts if any of the dependencies haven't yet been updated to support the latest version of Python.

The ```conda``` package manager is more stringent, essentially only allowing the user to install compatible packages and therefore having more stable functionality. For the ```conda``` package manager there are two channels, the ```conda``` channel which is maintained by the Anaconda company and gets updated approximately annually and the ```conda-forge``` channel which is the community channel and gets directly updated by the developers. 

Note when using Anaconda or Miniconda:

```conda install package```
```conda install -c conda-forge package```

Should be used in preference to:

```pip install package```

Where ```package``` is the name of the package. The ```pip``` command should only be used when the package is not found on available on the ```conda``` or ```conda-forge``` channel which is quite rare. 

# Installation

In this set of tutorials we will use Miniconda to create a new ```conda``` environment and install the latest version of JupyterLab IDE from the ```conda-forge``` channel, its dependencies and the most commonly used datascience libraries. Installation instructions are available for Windows and Linux:

[Miniconda Install on Windows](./001_windows_install/)

[Miniconda Install on Ubuntu](./002_ubuntu_install/)

The instructions above will also work with Anaconda, as we are in any case creating a seperate ```conda``` environment.
