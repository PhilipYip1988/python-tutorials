# The Python Ecosystem

The Python ecosystem is pretty vast and a consequence there are numerous ways to install and use Python. There are five common ways:

|Installer Name|Package Manager|Python Base Environment|Python Base Environment Channel|
|:-:|:-:|:-:|:-:|
|Python|pip|minimal|pip|
|Anaconda|conda|data science distribution|conda|
|Miniconda|conda|minimal|conda|
|Miniforge|conda|minimal|conda-forge|
|Mambaforge|mamba|minimal|conda-forge|

## Package Manager

Before going ahead with the install, it is worthwhile taking the time to understand the differences in the above methods, which fundamentally relate to the package manager, which is the utility used to install Python Packages.

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

Due to the above, there is a high level of confusion when users try and install the latest version of a package, and the latest version on the ```conda``` channel is several releases behind the ```conda-forge``` channel (or if more niche, not available at all on the ```conda``` channel). This results in problems when the ```conda``` package manager is unable to solve the Python environment, particularly when a package from ```conda-forge``` is attempted to be added to the vast ```base``` Python environment in Anaconda which uses the ```conda``` channel. The solution is normally to create a seperate Python environment (sub-installation) includingonly packages from the ```conda-forge``` channel which generally defeats the purpose of using Anaconda over Miniconda. Miniconda is a stripped Anaconda with a lightweight ```base``` Python environment. Miniforge is essentially the same as Miniconda however the packages in the base environment are from the ```conda-forge``` channel by default instead of the ```conda``` channel.

Finally, the Anaconda Python Datascience Distribution and packages in Anacondas ```conda``` channel have some licensing restrictions when it comes to commercial use. These licensing restrictions are not present for packages in the open-source ```conda-forge``` channel.

### mamba

The ```mamba``` package manager has been developed by the Python community to address many of the issues behind the ```conda``` package manager. The Mambaforge installer is essentially the same as the Miniforge installer but includes the ```mamba``` package manager. The rest of this guide will focus only on Mambaforge which is the most reliable solution.

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

Where possible explicitly specify, the ```conda-forge``` channel opposed to the ```conda``` channel. Note some larger developers such as ```pytorch``` use their own channel and you should continue to use their channel when instructed.

For example, to update the Python base environment using packages from the ```conda-forge``` channel use:

```
mamba update -c conda-forge --all
```

To create a new Python environment for the latest version of the Spyder IDE including its optional dependencies use:

```
mamba create -n spyder-cf
conda activate spyder-cf
mamba install -c conda-forge spyder
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

To create a new Python environment for the latest version of the JupyterLab IDE including its optional dependencies use:

```
mamba create -n jupyterlab-cf
mamba activate jupyterlab-cf
mamba install -c conda-forge jupyterlab
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
mamba install -c conda-forge nodejs ipywidgets 
mamba install -c conda-forge plotly dash jupyter-dash
mamba install -c conda-forge jupyterlab-variableinspector
```

To launch Spyder use:

```
conda activate spyder-cf
spyder
```

To launch JupyterLab use:

```
conda activate jupyterlab-cf
jupyter-lab
```

For those unexperienced with Python environments, the installation guides below explain the use of the above commands in a lot more detail and reveal what is physically happening using the file explorer.

# Installation

In this set of tutorials we will use Mambaconda to create a new Python environment and install the latest version of the Spyder and JupyterLab IDE from the ```conda-forge``` channel, its dependencies and the most commonly used datascience libraries. Installation instructions are available for Windows and Ubuntu Linux. The Mac Installation procedure is almost identical to Ubuntu Linux installation because the Mac Terminal and File structure are based upon their Linux counterparts:

[Mambaforge Install on Windows](./001_windows_install/)

[Mambaforge Install on Ubuntu](./002_ubuntu_install/)

