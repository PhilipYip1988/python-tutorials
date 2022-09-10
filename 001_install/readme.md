# The Python Ecosystem

The Python ecosystem is pretty vast and a consequence there are numerous ways to install and use Python. There are five common ways:

|Installer|Package Manager|Channel|Base|
|:-:|:-:|:-:|:-:|
|Python|pip|pip|minimal|
|Anaconda|conda|conda|data science distribution|
|Miniconda|conda|conda|minimal|
|Miniforge|conda|conda-forge|minimal|
|Mambaforge|mamba|conda-forge|minimal|

## Package Manager

Before going ahead with the install, it is worthwhile taking the time to understand the differences in the above methods, which fundamentally relate to the package manager, utility used to install Python Packages.

### pip

The most simple package manager is ```pip``` which is an abbreviation for Python Install Package. This is the most flexible package manager but does not check for library dependencies or compatible versions. 

In short you can install anything but there is a good chance that a beginner will install a combination of packages that are incompatible with each other or do not have their required dependencies to run. Then as a result will encounter a large number of error messages, when attempting to use data science libraries for example. 

### conda 

The next package manager is ```conda``` which performs a number of dependency checks and looks for compatibility between packages. The ```conda``` package manager uses two channels:
* ```conda``` the channel maintained by the Anaconda Company
* ```conda-forge``` the community channel

Both the package manager and company channel are called ```conda```. In theory, a user should be able to install Anaconda and use the ```base```Python environment which is populated with the most commonly used data science libraries. However in practice, due to the vast size of the Python ecosystem, the Anaconda company are struggling to keep up with all the developments for even the most popular Python packages and as a result their ```conda``` channel is often months or even years behind the  community ```conda-forge``` channel. There are also many developments in niche areas that the Anaconda has not incorporated into their ```base``` Python environment. 

The conda package manager also has a number of drawbacks, it can be quite slow to solve a Python environment (check for compatibility of Python packages) and usually hangs when attepting to solve environments which use packages from multiple channels such as ```conda``` and ```conda-forge```.

Due to the above, there is a high level of confusion when users try and install the latest version of a package, and the latest version on the ```conda``` channel is several releases behind the ```conda-forge``` channel (or if more niche, not available at all on the ```conda``` channel). This results in problems when the ```conda``` package manager is unable to solve the Python environment, particularly when a package from ```conda-forge``` is attempted to be added to the vast ```base``` Python environment in Anaconda which uses the ```conda``` channel. The solution is normally to create a seperate Python environment (sub-installation) which defeats the purpose of using Anaconda over Miniconda which has a lightweight ```base``` Python environment. Miniforge is essentially Miniconda with the base environment configured to use packages in the ```conda-forge``` channel by default.

### mamba

The ```mamba``` package manager has been developed by the Python community to address many of the issues behind the ```conda``` package manager and the ```mambaforge``` installer is configured to use the ```mamba``` package manager and uses packages in the ```conda-forge``` by default.

### Package Managers Syntax:

When using the mamba package manager, you should avoid use of commands which invoke the ```pip``` or ```conda``` package manager as use of multiple package managers in a single Python environment can result in instability. For example when you see installation commands to install packages:

```
pip install packagename
conda install packagename
conda install -c conda-forge packagename
```

Replace them with:

```
mamba install -c conda-forge packagename
```

Where possible explicitly specify, the ```conda-forge``` channel opposed to the ```conda``` channel. Note some larger developers such as ```pytorch``` use their own channel and you should continue to use their channel when instructed.

# Installation

In this set of tutorials we will use Mambaconda to create a new Python environment and install the latest version of JupyterLab IDE from the ```conda-forge``` channel, its dependencies and the most commonly used datascience libraries. Installation instructions are available for Windows and Linux:

[Mambaforge Install on Windows](./001_windows_install/)

[Mambaforge Install on Ubuntu](./002_ubuntu_install/)


