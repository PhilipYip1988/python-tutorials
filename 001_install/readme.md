# Python vs Anaconda

Python is a programming language that is under continuous development. One of the most powerful features of the Python ecosystem is it has numerous third-party libraries for data science. The Python programming language also has numerous **I**ntegrated **D**evelopment **E**nvironments (**IDE**s) which are essentially user interfaces for the programmer to interact with the Python programming language.

The flexibility of the Python ecosystem, causes some difficulty for the perspective begineer programmer and suffers some fragmentation as each tutorial recommends use of a different IDE, resulting in begineers spending more time IDE-hopping opposed to learning the Python Programming Language itself.

This is analogous to the problem of distro-hopping in Linux where begineers spend more time configuring the desktop environment than using Linux. For this reason the Ubuntu distribution is more stable but less flexible and tailored towards beginner. Ubuntu is maintained by the company Canonical. 

For Python there is a similar story with the Anaconda Python Distribution maintained by the company Anaconda.

The Python installer from python.org contains:
* The Python Programming Language
* A limited set of inbuilt modules 
* The **pip** package manager (**p**ython **i**nstall **p**ackage)
* The IDLE (Integrated Development **L**earner Environment)

The Anaconda installer from Anaconda.com in the base conda environment contains:
* The Python Programming Language
* Numerous Data Science Libraries such as:
    * numpy
    * pandas
    * matplotlib
    * seaborn
    * scipy
    * scikit-learn
    * scikit-image
* The conda package manager
* The Spyder and JupyterLab IDEs

## Package Managers: pip vs conda

Installing Python from python.org will give you the latest version of Python. Python is a programming language that is under continuous development... 

A Python library can be thought of as a collection of Python code. Therefore when functions from a Python library are called, under the hood some Python code will be executed. As a consequence a compatible version of Python is a required for the Python library and is known as a dependency.

When Python is updated the core functionality of the Python programming language may change. When a Python library is configured to use the old core functionality, an error may occur. The Python library will have to be updated in order to be compatible with the newest Python version. 

In the case of the datascience libraries, numpy can be thought of as the primary datascience library; pandas is built upon numpy and therefore has Python and numpy as dependencies. matplotlib has Python, numpy and pandas as dependencies and seaborn has Python, numpy, pandas and matplotlib as dependencies. It therefore takes time for the developers of these datascience libraries to update the libraries to be compatible with the latest version of Python and to be compatible with each other. This means there is a drawback for the standard user when using the latest version of Python.

pip - python install package can theoretically be used to install any version of a Python library and gives the greatest flexibility. However this flexibility comes at the compromise of possible broken functionality i.e. conflicts if any of the dependencies haven't yet been updated to support the latest version of Python.

The conda package manager is more stringent, essentially only allowing the user to install compatible packages and therefore having more stable functionality. For the conda-package manager there are two channels, the ```conda``` channel which is maintained by the Anaconda company and gets updated approximately annually and the ```conda-forge``` channel which is the community channel which gets directly updated by developers directly. 

When using Anaconda:

```conda install package```

Should be used in preference to:

```pip install package```

Where ```package``` is the name of the package.

## Anaconda vs Miniconda

The Anaconda Individual Python distribution contains a *base conda environment* which has stable versions of a large number of data science libraries. It also has commercial licensing restrictions which constrict it to Individual use.

Small packages from the ```conda-forge``` channel can be installed into the *base* conda environment however this practice is generally frowned upon. Instead a seperate *conda environment* should be created which is essentially a sub-installation. This is usually required when trying to install the latest version of an IDE as the IDE has numerous dependencies.

Miniconda is a stripped version of Anaconda, containing a minimal *base* conda environment and the conda package manager. It is also free of commercial licensing restrictions.

In this set of tutorials we will use Miniconda to create a conda environment and install the latest version of JupyterLab from the ```conda-forge``` channel. Anaconda installation is very similar and can be used in place of Miniconda for these tutorials.