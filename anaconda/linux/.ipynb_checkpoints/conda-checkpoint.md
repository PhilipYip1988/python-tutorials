# The conda Package Manager

The purpose of the conda package manager is to allow cross-platform installation of Python packages and non-Python dependences related to a datascience project in a Python environment. This can include other programming languages such as R.

The conda package manager has two main channels:

|channel name|channel description|
|---|---|
|conda-forge|community channel maintained by developers|
|main|channel maintained by the Anaconda company|

The main channel also known as conda or anaconda is the channel maintained by the Anaconda company. These packages are tested by the Anaconda company for compatibility with the Anaconda Python distribution. As the Anaconda company only test commonly used datascience libraries and it takes time for testing, there are less packages available in the main channel and the package that they have may not be the latest version.

## The base Python Environment

In Anaconda the base Python environment is a Python distribution and should not be modified outwith the standard conda images available from Anaconda. The reason for this is the Python distribution has a large number of packages and changing a package that is a dependency for the other packages will normally result in a number of these packages being removed leading to an unstable Python environment.

To recap the base Python environment is found in:

```
~/anaconda3
```

<img src='images_conda/img_001.png' alt='img_001' width='450'/>

There is a bin subfolder and a lib subfolder:

```
~/anaconda3/bin
~/anaconda3/lib
```

<img src='images_conda/img_002.png' alt='img_002' width='450'/>

The bin subfolder which contains binary applications installed in the (base) Python environment. This includes python which has the alias python3.11 and python3 alias:

<img src='images_conda/img_003.png' alt='img_003' width='450'/>

The lib subfolder contains a python3.11 subfolder which contains the Python standard modules:

<img src='images_conda/img_004.png' alt='img_004' width='450'/>

When the module is a single file the name of the file corresponds to the name of the module. When the module is a folder, the folder name corresponds to the name of the module and there is a datamodel initialisation script file called ```__init__.py``` which is imported.

For example the ```datetime``` module is an individual script file:

<img src='images_conda/img_006.png' alt='img_006' width='450'/>

And the ```email``` module which is a folder of multiple Python script files:

<img src='images_conda/img_005.png' alt='img_005' width='450'/>

This folder contains third-party modules also known as libraries. Common libraries are numpy, pandas and matplotlib. 

<img src='images_conda/img_007.png' alt='img_007' width='450'/>

For example ```numpy```:

<img src='images_conda/img_008.png' alt='img_008' width='450'/>

These modules can be imported and the datamodel attribute ```__file__``` can be printed to view the location of the file:

```
(base) username@pc:~$ jupyter-console
Jupyter console 6.6.3

Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import datetime
   ...: import email

In [2]: print(datetime.__file__)
   ...: print(email.__file__)
~/anaconda3/lib/python3.11/datetime.py
~/anaconda3/lib/python3.11/email/__init__.py

In [3]: import numpy as np
   ...: import pandas as pd
   ...: import matplotlib.pyplot as plt

In [4]: print(np.__file__)
   ...: print(pd.__file__)
   ...: print(plt.__file__)
~/anaconda3/lib/python3.11/site-packages/numpy/__init__.py
~/anaconda3/lib/python3.11/site-packages/pandas/__init__.py
~/anaconda3/lib/python3.11/site-packages/matplotlib/pyplot.py

In [5]:
```

## The envs folder

The (base) Python environment also contains an envs folder which is used for Python environments:

```
~\anaconda3\envs
```

<img src='images_conda/img_009.png' alt='img_009' width='450'/>

By default there are no additional Python environments and this folder is empty:

<img src='images_conda/img_010.png' alt='img_010' width='450'/>

A Python environment is essentially a sub-installation of Python. Each Python environment will therefore a substructure similar to the (base) Python environment and will have their own:

* python binary in bin folder
* bin folder
* lib folder
* site-packages subfolder within lib

The use of Python environments for example allows installation of the latest version of each IDE without breaking the functionality of the (base) Python environment.

## conda Package Manager

### Overview

An overview about the conda package manager can be seen by opening up the Terminal and inputting the bash command:

```bash
conda
```

This gives the following output:

```
(base) username@pc:~$ conda
usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...

conda is a tool for managing and deploying applications, environments and packages.

options
```
|flag or option|purpose|
|---|---|
|-h, --help|Show this help message and exit.|
|-v, --verbose|Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.|
|--no-plugins|Disable all plugins that are not built into conda.|
|-V, --version|Show the conda version number and exit.|
```
commands:
  The following built-in and plugins subcommands are available.
```
|command|description|
|---|---|
|activate|Activate a conda environment.|
|build|Build conda packages from a conda recipe.|
|clean|Remove unused packages and caches.|
|compare|Compare packages between conda environments.|
|config|Modify configuration values in .condarc.|
|create|Create a new conda environment from a list of specified packages.|
|doctor|Display a health report for your environment.|
|info|Display information about current conda install.|
|init|Initialize conda for shell interaction.|
|install|Install a list of packages into a specified conda environment.|
|list|List installed packages in a conda environment.|
|notices|Retrieve latest channel notifications.|
|package|Create low-level conda packages.|
|remove|Remove a list of packages from a specified conda environment.|
|rename|Rename an existing environment.|
|run|Run an executable in a conda environment.|
|search|Search for packages and display associated information using the MatchSpec format.|
|update|Update conda packages to the latest compatible version.|
|build|See conda build --help.|
|content-trust|See conda content-trust --help.|
|convert|See conda convert --help.|
|debug|See conda debug --help.|
|develop|See conda develop --help.|
|env|See conda env --help.|
|index|See conda index --help.|
|inspect|See conda inspect --help.|
|metapackage|See conda metapackage --help.|
|pack|See conda pack --help.|
|render|See conda render --help.|
|repo|See conda repo --help.|
|server|See conda server --help.|
|skeleton|See conda skeleton --help.|
|token|See conda token --help.|
|verify|See conda verify --help.|
```bash
(base) username@pc:~$
```

### Create

A Python environment can be created using the syntax:

```bash
conda create -n notbase
```

where "notbase" is the environment name. The longer ```--name``` can also be used in place of the ```-n```.

The following will be output:

```
(base) username@pc:~$ conda create -n notbase
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase



Proceed ([y]/n)?
```

Input ```y``` to proceed. The Python environment is now created:

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate notbase
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) username@pc:~$
```

Notice in envs, the notbase subfolder is created:

<img src='images_conda/img_022.png' alt='img_022' width='450'/>

<img src='images_conda/img_023.png' alt='img_023' width='450'/>

### Activate

The ```activate``` subcommand is used to active a Python environment. When a Python environment is activated the:

* python binary in bin folder
* bin folder
* lib folder
* site-packages subfolder within lib

associated with the Python environment will preferentially be used over their respective locations in (base).

The notbase Python environment can be activated using:

```bash
conda activate notbase
```

The output now looks like:

```
(base) username@pc:~$ conda activate notbase
(notbase) username@pc:~$
```

Notice that the prompt now has the (notbase) prefix indicating that the (notbase) Python is activated.

When the Terminal is closed and reopened, the default Python environment (base) will be activated. The Python environment notbase will have to be activated.

### Search

A package can be searched for using the ```search``` subcommand followed by the package name:

```bash
conda search package_name
```

The channel to search for packages in can be specified using ```-c``` or the long form ```--channel``` followed by the name of the channel. The default channel is ```main``` but it is more common to use the ```conda-forge``` community channel when creating a custom Python environment. 

```bash
conda search -c conda-forge package_name
```

or example a search of the package python:

```bash
conda search python
```

Outputs:

```
(notbase) username@pc:~$ conda search python
Loading channels: done
```
|Name|Version|Build|Channel|
|---|---|---|---|
|python|3.11.5|h7a1cb2a_0|pkgs/main|
|python|3.11.5|h955ad1f_0|pkgs/main|
|python|3.11.7|h955ad1f_0|pkgs/main|
|python|3.12.0|h996f2a0_0|pkgs/main|
```
(notbase) username@pc:~$
```

And if the channel is change to conda-forge:

```bash
conda search -c conda-forge python
```

Outputs:

```
(notbase) username@pc:~$ conda search -c conda-forge python
Loading channels: done
```
|Name|Version|Build|Channel|
|---|---|---|---|
|python|3.11.7|h955ad1f_0|pkgs/main|
|python|3.11.7|hab00c5b_0_cpython|conda-forge|
|python|3.11.7|hab00c5b_1_cpython|conda-forge|
|python|3.12.0rc3|rc3_hab00c5b_1_cpython|conda-forge|
|python|3.12.0|h996f2a0_0|pkgs/main|
|python|3.12.0|hab00c5b_0_cpython|conda-forge|
|python|3.12.1|hab00c5b_0_cpython|conda-forge|
|python|3.12.1|hab00c5b_1_cpython|conda-forge|
```
(notbase) username@pc:~$
```

Notice each Python has a version number of the format X.Y.Z where X is the major build, Y is the minor build and Z is the patch number. The build number consists of a hash followed by a revision. If prefixed with py it is a pure Python package.

The package ipython can be searched for using:

```bash
conda search -c conda-forge ipython
```

This outputs:

```
(notbase) username@pc:~$ conda search -c conda-forge ipython
Loading channels: done
```
|Name|Version|Build|Channel|
|---|---|---|---|
|ipython|8.19.0|pyh707e725_0|conda-forge|
|ipython|8.19.0|pyh7428d3b_0|conda-forge|
|ipython|8.20.0|py310h06a4308_0pyh707e725_0|pkgs/main|
|ipython|8.20.0|py311h06a4308_0|pkgs/main|
|ipython|8.20.0|py312h06a4308_0|pkgs/main|
|ipython|8.20.0|pyh707e725_0|conda-forge|
|ipython|8.20.0|pyh7428d3b_0|conda-forge|
```
(notbase) username@pc:~$
```

### Install

The subcommand ```install``` can be used to install a package:

```bash
conda install package_name
```

Multiple packages can be installed using the syntax:

```bash
conda install package_name1 package_name2
```

Once again the channel to install from should be specified:

```bash
conda install -c conda-forge package_name1 package_name2
```

The packages python and ipython can be installed from the community channel using:

```bash
conda install -c conda-forge python ipython
```

This outputs:

```
(notbase) username@pc:~$ conda install -c conda-forge python ipython
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase

  added / updated specs:
    - ipython
    - python


The following packages will be downloaded:
```
|package|build|size|channel|
|---|---|---|---|
|exceptiongroup-1.2.0|pyhd8ed1ab_2|20 KB|conda-forge|
|ipython-8.20.0|pyh707e725_0|577 KB|conda-forge|
|setuptools-69.0.3|pyhd8ed1ab_0|460 KB|conda-forge|
|traitlets-5.14.1|pyhd8ed1ab_0|108 KB|conda-forge|
|wcwidth-0.2.13|pyhd8ed1ab_0|32 KB|conda-forge|
```
Total: 1.2 MB
The following NEW packages will be INSTALLED:
```
|package|details|
|---|---|
|_libgcc_mutex|conda-forge/linux-64::_libgcc_mutex-0.1-conda_forge|
|_openmp_mutex|conda-forge/linux-64::_openmp_mutex-4.5-2_gnu|
|asttokens|conda-forge/noarch::asttokens-2.4.1-pyhd8ed1ab_0|
|bzip2|conda-forge/linux-64::bzip2-1.0.8-hd590300_5|
|ca-certificates|conda-forge/linux-64::ca-certificates-2023.11.17-hbcca054_0|
|decorator|conda-forge/noarch::decorator-5.1.1-pyhd8ed1ab_0|
|exceptiongroup|conda-forge/noarch::exceptiongroup-1.2.0-pyhd8ed1ab_2|
|executing|conda-forge/noarch::executing-2.0.1-pyhd8ed1ab_0|
|ipython|conda-forge/noarch::ipython-8.20.0-pyh707e725_0|
|jedi|conda-forge/noarch::jedi-0.19.1-pyhd8ed1ab_0|
|ld_impl_linux-64|conda-forge/linux-64::ld_impl_linux-64-2.40-h41732ed_0|
|libexpat|conda-forge/linux-64::libexpat-2.5.0-hcb278e6_1|
|libffi|conda-forge/linux-64::libffi-3.4.2-h7f98852_5|
|libgcc-ng|conda-forge/linux-64::libgcc-ng-13.2.0-h807b86a_3|
|libgomp|conda-forge/linux-64::libgomp-13.2.0-h807b86a_3|
|libnsl|conda-forge/linux-64::libnsl-2.0.1-hd590300_0|
|libsqlite|conda-forge/linux-64::libsqlite-3.44.2-h2797004_0|
|libuuid|conda-forge/linux-64::libuuid-2.38.1-h0b41bf4_0|
|libxcrypt|conda-forge/linux-64::libxcrypt-4.4.36-hd590300_1|
|libzlib|conda-forge/linux-64::libzlib-1.2.13-hd590300_5|
|matplotlib-inline|conda-forge/noarch::matplotlib-inline-0.1.6-pyhd8ed1ab_0|
|ncurses|conda-forge/linux-64::ncurses-6.4-h59595ed_2|
|openssl|conda-forge/linux-64::openssl-3.2.0-hd590300_1|
|parso|conda-forge/noarch::parso-0.8.3-pyhd8ed1ab_0|
|pexpect|conda-forge/noarch::pexpect-4.8.0-pyh1a96a4e_2|
|pickleshare|conda-forge/noarch::pickleshare-0.7.5-py_1003|
|pip|conda-forge/noarch::pip-23.3.2-pyhd8ed1ab_0|
|prompt-toolkit|conda-forge/noarch::prompt-toolkit-3.0.42-pyha770c72_0|
|ptyprocess|conda-forge/noarch::ptyprocess-0.7.0-pyhd3deb0d_0|
|pure_eval|conda-forge/noarch::pure_eval-0.2.2-pyhd8ed1ab_0|
|pygments|conda-forge/noarch::pygments-2.17.2-pyhd8ed1ab_0|
|python|conda-forge/linux-64::python-3.12.1-hab00c5b_1_cpython|
|readline|conda-forge/linux-64::readline-8.2-h8228510_1|
|setuptools|conda-forge/noarch::setuptools-69.0.3-pyhd8ed1ab_0|
|six|conda-forge/noarch::six-1.16.0-pyh6c4a22f_0|
|stack_data|conda-forge/noarch::stack_data-0.6.2-pyhd8ed1ab_0|
|tk|conda-forge/linux-64::tk-8.6.13-noxft_h4845f30_101|
|traitlets|conda-forge/noarch::traitlets-5.14.1-pyhd8ed1ab_0|
|typing_extensions|conda-forge/noarch::typing_extensions-4.9.0-pyha770c72_0|
|tzdata|conda-forge/noarch::tzdata-2023d-h0c530f3_0|
|wcwidth|conda-forge/noarch::wcwidth-0.2.13-pyhd8ed1ab_0|
|wheel|conda-forge/noarch::wheel-0.42.0-pyhd8ed1ab_0|
|xz|conda-forge/linux-64::xz-5.2.6-h166bdaf_0|
```bash
Proceed ([y]/n)?
```

Input ```y``` in order to proceed. This outputs:

```
Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(notbase) username@pc:~$
```

A new prompt is available when the operation is finished.

```ipython``` can be used from this Python environment. Notice when the standard modules are imported, the modules from the perspective Python environment are used:

```
(base) username@pc:~$ conda activate notbase
(notbase) username@pc:~$ ipython
Python 3.12.1 | packaged by conda-forge | (main, Dec 23 2023, 08:03:24) [GCC 12.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.20.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import datetime
   ...: import email
   ...:
   ...: print(datetime.__file__)
   ...: print(email.__file__)
~/anaconda3/envs/notbase/lib/python3.12/datetime.py
~/anaconda3/envs/notbase/lib/python3.12/email/__init__.py

In [2]: import numpy as np
   ...: import pandas as pd
   ...: import matplotlib.pyplot as plt
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[2], line 1
----> 1 import numpy as np
      2 import pandas as pd
      3 import matplotlib.pyplot as plt

ModuleNotFoundError: No module named 'numpy'

In [3]:
```

Note attempting to import numpy, pandas and matplotlib gives a ```ModuleNotFoundError``` as they are not installed in this Python environment.

### Remove

The ```remove``` subcommand can be used to remove an installed package:

```bash
conda remove package_name1 package_name2
```

For example the package python can be removed using:

```bash
conda remove python
```

This outputs:

```
(notbase) username@pc:~$ conda remove python
Channels:
 - defaults
 - conda-forge
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase

  removed specs:
    - python


The following packages will be REMOVED:
```
|package|details|
|---|---|
|_libgcc_mutex|conda-forge/linux-64::_libgcc_mutex-0.1-conda_forge|
|_openmp_mutex|conda-forge/linux-64::_openmp_mutex-4.5-2_gnu|
|asttokens|conda-forge/noarch::asttokens-2.4.1-pyhd8ed1ab_0|
|bzip2|conda-forge/linux-64::bzip2-1.0.8-hd590300_5|
|ca-certificates|conda-forge/linux-64::ca-certificates-2023.11.17-hbcca054_0|
|decorator|conda-forge/noarch::decorator-5.1.1-pyhd8ed1ab_0|
|exceptiongroup|conda-forge/noarch::exceptiongroup-1.2.0-pyhd8ed1ab_2|
|executing|conda-forge/noarch::executing-2.0.1-pyhd8ed1ab_0|
|ipython|conda-forge/noarch::ipython-8.20.0-pyh707e725_0|
|jedi|conda-forge/noarch::jedi-0.19.1-pyhd8ed1ab_0|
|ld_impl_linux-64|conda-forge/linux-64::ld_impl_linux-64-2.40-h41732ed_0|
|libexpat|conda-forge/linux-64::libexpat-2.5.0-hcb278e6_1|
|libffi|conda-forge/linux-64::libffi-3.4.2-h7f98852_5|
|libgcc-ng|conda-forge/linux-64::libgcc-ng-13.2.0-h807b86a_3|
|libgomp|conda-forge/linux-64::libgomp-13.2.0-h807b86a_3|
|libnsl|conda-forge/linux-64::libnsl-2.0.1-hd590300_0|
|libsqlite|conda-forge/linux-64::libsqlite-3.44.2-h2797004_0|
|libuuid|conda-forge/linux-64::libuuid-2.38.1-h0b41bf4_0|
|libxcrypt|conda-forge/linux-64::libxcrypt-4.4.36-hd590300_1|
|libzlib|conda-forge/linux-64::libzlib-1.2.13-hd590300_5|
|matplotlib-inline|conda-forge/noarch::matplotlib-inline-0.1.6-pyhd8ed1ab_0|
|ncurses|conda-forge/linux-64::ncurses-6.4-h59595ed_2|
|openssl|conda-forge/linux-64::openssl-3.2.0-hd590300_1|
|parso|conda-forge/noarch::parso-0.8.3-pyhd8ed1ab_0|
|pexpect|conda-forge/noarch::pexpect-4.8.0-pyh1a96a4e_2|
|pickleshare|conda-forge/noarch::pickleshare-0.7.5-py_1003|
|pip|conda-forge/noarch::pip-23.3.2-pyhd8ed1ab_0|
|prompt-toolkit|conda-forge/noarch::prompt-toolkit-3.0.42-pyha770c72_0|
|ptyprocess|conda-forge/noarch::ptyprocess-0.7.0-pyhd3deb0d_0|
|pure_eval|conda-forge/noarch::pure_eval-0.2.2-pyhd8ed1ab_0|
|pygments|conda-forge/noarch::pygments-2.17.2-pyhd8ed1ab_0|
|python|conda-forge/linux-64::python-3.12.1-hab00c5b_1_cpython|
|readline|conda-forge/linux-64::readline-8.2-h8228510_1|
|setuptools|conda-forge/noarch::setuptools-69.0.3-pyhd8ed1ab_0|
|six|conda-forge/noarch::six-1.16.0-pyh6c4a22f_0|
|stack_data|conda-forge/noarch::stack_data-0.6.2-pyhd8ed1ab_0|
|tk|conda-forge/linux-64::tk-8.6.13-noxft_h4845f30_101|
|traitlets|conda-forge/noarch::traitlets-5.14.1-pyhd8ed1ab_0|
|typing_extensions|conda-forge/noarch::typing_extensions-4.9.0-pyha770c72_0|
|tzdata|conda-forge/noarch::tzdata-2023d-h0c530f3_0|
|wcwidth|conda-forge/noarch::wcwidth-0.2.13-pyhd8ed1ab_0|
|wheel|conda-forge/noarch::wheel-0.42.0-pyhd8ed1ab_0|
|xz|conda-forge/linux-64::xz-5.2.6-h166bdaf_0|
```bash
Proceed ([y]/n)?
```

Because Python is being removed which is a dependency for everything else, everything else is also removed. To proceed with the changes input ```y```. This outputs:

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(notbase) username@pc:~$
```

A new prompt is available when the operation is finished.

### Specifying Package Version and Build

During installation version numbers can be specified using assignment:

```bash
conda install -c conda-forge package_name=X.Y.Z
```

The build number can also be specified in some cases, although is more rare to specify this:

```bash
conda install -c conda-forge package_name=X.Y.Z=build_number
```

For example a specific version of ipython can be installed:

```bash
conda install -c conda-forge ipython=8.19.0=pyh707e725_0
```

This outputs:

```
(notbase) username@pc:~$ conda install -c conda-forge ipython=8.19.0=pyh707e725_0
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase

  added / updated specs:
    - ipython==8.19.0=pyh707e725_0


The following NEW packages will be INSTALLED:
```
|package|details|
|---|---|
|asttokens|conda-forge/noarch::asttokens-2.4.1-pyhd8ed1ab_0|
|bzip2|conda-forge/linux-64::bzip2-1.0.8-hd590300_5|
|decorator|conda-forge/noarch::decorator-5.1.1-pyhd8ed1ab_0|
|exceptiongroup|conda-forge/noarch::exceptiongroup-1.2.0-pyhd8ed1ab_2|
|executing|conda-forge/noarch::executing-2.0.1-pyhd8ed1ab_0|
|ipython|conda-forge/noarch::ipython-8.19.0-pyh707e725_0|
|jedi|conda-forge/noarch::jedi-0.19.1-pyhd8ed1ab_0|
|ld_impl_linux-64|conda-forge/linux-64::ld_impl_linux-64-2.40-h41732ed_0|
|libexpat|conda-forge/linux-64::libexpat-2.5.0-hcb278e6_1|
|libffi|conda-forge/linux-64::libffi-3.4.2-h7f98852_5|
|libnsl|conda-forge/linux-64::libnsl-2.0.1-hd590300_0|
|libsqlite|conda-forge/linux-64::libsqlite-3.44.2-h2797004_0|
|libuuid|conda-forge/linux-64::libuuid-2.38.1-h0b41bf4_0|
|libxcrypt|conda-forge/linux-64::libxcrypt-4.4.36-hd590300_1|
|libzlib|conda-forge/linux-64::libzlib-1.2.13-hd590300_5|
|matplotlib-inline|conda-forge/noarch::matplotlib-inline-0.1.6-pyhd8ed1ab_0|
|ncurses|conda-forge/linux-64::ncurses-6.4-h59595ed_2|
|parso|conda-forge/noarch::parso-0.8.3-pyhd8ed1ab_0|
|pexpect|conda-forge/noarch::pexpect-4.8.0-pyh1a96a4e_2|
|pickleshare|conda-forge/noarch::pickleshare-0.7.5-py_1003|
|pip|conda-forge/noarch::pip-23.3.2-pyhd8ed1ab_0|
|prompt-toolkit|conda-forge/noarch::prompt-toolkit-3.0.42-pyha770c72_0|
|ptyprocess|conda-forge/noarch::ptyprocess-0.7.0-pyhd3deb0d_0|
|pure_eval|conda-forge/noarch::pure_eval-0.2.2-pyhd8ed1ab_0|
|pygments|conda-forge/noarch::pygments-2.17.2-pyhd8ed1ab_0|
|python|conda-forge/linux-64::python-3.12.1-hab00c5b_1_cpython|
|readline|conda-forge/linux-64::readline-8.2-h8228510_1|
|setuptools|conda-forge/noarch::setuptools-69.0.3-pyhd8ed1ab_0|
|six|conda-forge/noarch::six-1.16.0-pyh6c4a22f_0|
|stack_data|conda-forge/noarch::stack_data-0.6.2-pyhd8ed1ab_0|
|tk|conda-forge/linux-64::tk-8.6.13-noxft_h4845f30_101|
|traitlets|conda-forge/noarch::traitlets-5.14.1-pyhd8ed1ab_0|
|typing_extensions|conda-forge/noarch::typing_extensions-4.9.0-pyha770c72_0|
|tzdata|conda-forge/noarch::tzdata-2023d-h0c530f3_0|
|wcwidth|conda-forge/noarch::wcwidth-0.2.13-pyhd8ed1ab_0|
|wheel|conda-forge/noarch::wheel-0.42.0-pyhd8ed1ab_0|
|xz|conda-forge/linux-64::xz-5.2.6-h166bdaf_0|
```
Proceed ([y]/n)?
```

Input ```y``` to proceed with the changes:

```
Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(notbase) username@pc:~$
```

A new prompt is available when the operation is finished.

### Update

The ```update``` subcommand can be used to update a package to the latest compatible version using the update subcommand:

```bash
conda update package_name
```

Once again the channel to update the package from should be specified:

```bash
conda update -c conda-forge package_name
```

The package ipython for example can be updated:

```bash
conda update -c conda-forge ipython
```

This outputs:

```
(notbase) username@pc:~$ conda update -c conda-forge ipython
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase

  added / updated specs:
    - ipython


The following packages will be UPDATED:
```
|package|old details||new details|
|---|---|---|---|
|ipython|8.19.0-pyh707e725_0|-->|8.20.0-pyh707e725_0|
```
Proceed ([y]/n)?
```

Notice that this finds an updated version of ipython. Input ```n``` to cancel outputs:

```bash
CondaSystemExit: Exiting.

(notbase) username@pc:~$
```

It is common to use the option ```--all``` instead of specifying a package, this will attempt to update all the packages in the Python environment to their latest versions:

```bash
conda update -c conda-forge --all
```

This command works well for small Python environments that have a small number of packages but the conda package manager often has difficulties solving large Python environments as a package that is a dependency for other packages gets updated to the latest version prompting from the removal of other packages that were dependent on the older version. Sometimes in such case deleting and recreating the Python environment leads to better results than updating. 

The output shows:

```
(notbase) username@pc:~$ conda update --all
Channels:
 - defaults
 - conda-forge
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase


The following packages will be downloaded:
```

|package|build|size|
|---|---|---|
|ipython-8.20.0|py312h06a4308_0|1.4 MB|
|matplotlib-inline-0.1.6|py312h06a4308_0|18 KB|
|prompt-toolkit-3.0.43|py312h06a4308_0|732 KB|
|prompt_toolkit-3.0.43|hd3eb1b0_0|5 KB|
|tzdata-2023d|h04d1e81_0|117 KB|
```
Total: 2.3 MB

The following NEW packages will be INSTALLED:
```
|package|details|
|---|---|
|libstdcxx-ng|pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1|
|prompt_toolkit|pkgs/main/noarch::prompt_toolkit-3.0.43-hd3eb1b0_0|
```
The following packages will be UPDATED:
```
|package|old details||new details|
|---|---|---|---|
|ca-certificates|   conda-forge::ca-certificates-2023.11.~|-->|pkgs/main::ca-certificates-2023.12.12-h06a4308_0|
|ipython|conda-forge/noarch::ipython-8.19.0-py~| -->|pkgs/main/linux-64::ipython-8.20.0-py312h06a4308_0|
|libffi|conda-forge::libffi-3.4.2-h7f98852_5|-->|pkgs/main::libffi-3.4.4-h6a678d5_0|
|pexpect|conda-forge::pexpect-4.8.0-pyh1a96a4e~|-->|pkgs/main::pexpect-4.8.0-pyhd3eb1b0_3|
|prompt-toolkit|conda-forge/noarch::prompt-toolkit-3.~|-->|pkgs/main/linux-64::prompt-toolkit-3.0.43-py312h06a4308_0|
|ptyprocess|conda-forge::ptyprocess-0.7.0-pyhd3de~|-->|pkgs/main::ptyprocess-0.7.0-pyhd3eb1b0_2|
|six|conda-forge::six-1.16.0-pyh6c4a22f_0|-->|pkgs/main::six-1.16.0-pyhd3eb1b0_1|
|xz|conda-forge::xz-5.2.6-h166bdaf_0|-->|pkgs/main::xz-5.4.5-h5eee18b_0|
```
The following packages will be SUPERSEDED by a higher-priority channel:
```
|package|old details||new details|
|---|---|---|---|
|bzip2|conda-forge::bzip2-1.0.8-hd590300_5|-->|pkgs/main::bzip2-1.0.8-h7b6447c_0|
|decorator|conda-forge::decorator-5.1.1-pyhd8ed1~| -->|pkgs/main::decorator-5.1.1-pyhd3eb1b0_0|
|matplotlib-inline|conda-forge/noarch::matplotlib-inline~|-->|pkgs/main/linux-64::matplotlib-inline-0.1.6-py312h06a4308_0|
|ncurses|conda-forge::ncurses-6.4-h59595ed_2|-->|pkgs/main::ncurses-6.4-h6a678d5_0|
|parso|conda-forge::parso-0.8.3-pyhd8ed1ab_0|-->|pkgs/main::parso-0.8.3-pyhd3eb1b0_0|
|pickleshare|conda-forge::pickleshare-0.7.5-py_1003|-->|pkgs/main::pickleshare-0.7.5-pyhd3eb1b0_1003|
|pure_eval|conda-forge::pure_eval-0.2.2-pyhd8ed1~|-->|pkgs/main::pure_eval-0.2.2-pyhd3eb1b0_0|
|readline|conda-forge::readline-8.2-h8228510_1|-->|pkgs/main::readline-8.2-h5eee18b_0|
|tzdata|               conda-forge::tzdata-2023d-h0c530f3_0|-->|pkgs/main::tzdata-2023d-h04d1e81_0|
```
Proceed ([y]/n)?
```

To proceed input ```y```:

```
Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(notbase) username@pc:~$
```

A new prompt is available when the operation is finished.

**The base Python environment is an example of a very large Python environment and using the above command should not be used in the base Python environment as it will result in an unstable base Python environment that will not work properly.** 

Recall to update the base Python environment use:

```bash
conda deactivate
conda update conda
conda update anaconda-navigator
```

This was seen when Anaconda was initially installed.

### List

The ```list``` subcommand can be used to list the packages in the Python environment:

```bash
conda list
```

This outputs:

```
(notbase) philip@pc:~$ conda list
# packages in environment at ~/anaconda3/envs/notbase:
```
|Name|Version|Build|Channel|
|---|---|---|---|
|_libgcc_mutex|0.1|conda_forge|conda-forge|
|_openmp_mutex|4.5|2_gnu|conda-forge|
|asttokens|2.4.1|pyhd8ed1ab_0|conda-forge|
|bzip2|1.0.8|h7b6447c_0||
|ca-certificates|2023.12.12|h06a4308_0||
|decorator|5.1.1|pyhd3eb1b0_0||
|exceptiongroup|1.2.0|pyhd8ed1ab_2|conda-forge|
|executing|2.0.1|pyhd8ed1ab_0|conda-forge|
|ipython|8.20.0|py312h06a4308_0||
jedi|0.19.1|pyhd8ed1ab_0|conda-forge|
|ld_impl_linux-64|2.40|h41732ed_0|conda-forge|
|libexpat|2.5.0|hcb278e6_1|conda-forge|
|libffi|3.4.4|h6a678d5_0||
|libgcc-ng|13.2.0|h807b86a_3|conda-forge|
|libgomp|13.2.0|h807b86a_3|conda-forge|
|libnsl|2.0.1|hd590300_0|conda-forge|
|libsqlite|3.44.2|h2797004_0|conda-forge|
|libstdcxx-ng|11.2.0|h1234567_1||
|libuuid|2.38.1|h0b41bf4_0|conda-forge|
|libxcrypt|4.4.36|hd590300_1|conda-forge|
|libzlib|1.2.13|hd590300_5|conda-forge|
|matplotlib-inline|0.1.6|py312h06a4308_0||
|ncurses|6.4|h6a678d5_0||
|openssl|3.2.0|hd590300_1|conda-forge|
|parso|0.8.3|pyhd3eb1b0_0||
|pexpect|4.8.0|pyhd3eb1b0_3||
|pickleshare|0.7.5|pyhd3eb1b0_1003||
|pip|23.3.2|pyhd8ed1ab_0|conda-forge|
|prompt-toolkit|3.0.43|py312h06a4308_0||
|prompt_toolkit|3.0.43|hd3eb1b0_0||
|ptyprocess|0.7.0|pyhd3eb1b0_2||
|pure_eval|0.2.2|pyhd3eb1b0_0||
|pygments|2.17.2|pyhd8ed1ab_0|conda-forge|
|python|3.12.1|hab00c5b_1_cpython|conda-forge|
|readline|8.2|h5eee18b_0||
|setuptools|69.0.3|pyhd8ed1ab_0|conda-forge|
|six|1.16.0|pyhd3eb1b0_1||
|stack_data|0.6.2|pyhd8ed1ab_0|conda-forge|
|tk|8.6.13|noxft_h4845f30_101|conda-forge|
|traitlets|5.14.1|pyhd8ed1ab_0|conda-forge|
|typing_extensions|4.9.0|pyha770c72_0|conda-forge|
|tzdata|2023d|h04d1e81_0||
|wcwidth|0.2.13|pyhd8ed1ab_0|conda-forge|
|wheel|0.42.0|pyhd8ed1ab_0|conda-forge|
|xz|5.4.5|h5eee18b_0||
```
(notbase) username@pc:~$
```

The subcommand option ```--revision``` can be used to list each revision of the Python environment:

```
conda list --revision
```

```
(notbase) username@pc:~$ conda list --revision
2024-01-12 08:54:07  (rev 0)

2024-01-13 01:53:46  (rev 1)
    +_libgcc_mutex-0.1 (conda-forge/linux-64)
    +_openmp_mutex-4.5 (conda-forge/linux-64)
    +asttokens-2.4.1 (conda-forge/noarch)
    +bzip2-1.0.8 (conda-forge/linux-64)
    +ca-certificates-2023.11.17 (conda-forge/linux-64)
    +decorator-5.1.1 (conda-forge/noarch)
    +exceptiongroup-1.2.0 (conda-forge/noarch)
    +executing-2.0.1 (conda-forge/noarch)
    +ipython-8.20.0 (conda-forge/noarch)
    +jedi-0.19.1 (conda-forge/noarch)
    +ld_impl_linux-64-2.40 (conda-forge/linux-64)
    +libexpat-2.5.0 (conda-forge/linux-64)
    +libffi-3.4.2 (conda-forge/linux-64)
    +libgcc-ng-13.2.0 (conda-forge/linux-64)
    +libgomp-13.2.0 (conda-forge/linux-64)
    +libnsl-2.0.1 (conda-forge/linux-64)
    +libsqlite-3.44.2 (conda-forge/linux-64)
    +libuuid-2.38.1 (conda-forge/linux-64)
    +libxcrypt-4.4.36 (conda-forge/linux-64)
    +libzlib-1.2.13 (conda-forge/linux-64)
    +matplotlib-inline-0.1.6 (conda-forge/noarch)
    +ncurses-6.4 (conda-forge/linux-64)
    +openssl-3.2.0 (conda-forge/linux-64)
    +parso-0.8.3 (conda-forge/noarch)
    +pexpect-4.8.0 (conda-forge/noarch)
    +pickleshare-0.7.5 (conda-forge/noarch)
    +pip-23.3.2 (conda-forge/noarch)
    +prompt-toolkit-3.0.42 (conda-forge/noarch)
    +ptyprocess-0.7.0 (conda-forge/noarch)
    +pure_eval-0.2.2 (conda-forge/noarch)
    +pygments-2.17.2 (conda-forge/noarch)
    +python-3.12.1 (conda-forge/linux-64)
    +readline-8.2 (conda-forge/linux-64)
    +setuptools-69.0.3 (conda-forge/noarch)
    +six-1.16.0 (conda-forge/noarch)
    +stack_data-0.6.2 (conda-forge/noarch)
    +tk-8.6.13 (conda-forge/linux-64)
    +traitlets-5.14.1 (conda-forge/noarch)
    +typing_extensions-4.9.0 (conda-forge/noarch)
    +tzdata-2023d (conda-forge/noarch)
    +wcwidth-0.2.13 (conda-forge/noarch)
    +wheel-0.42.0 (conda-forge/noarch)
    +xz-5.2.6 (conda-forge/linux-64)

2024-01-13 09:18:42  (rev 2)
    -asttokens-2.4.1 (conda-forge/noarch)
    -bzip2-1.0.8 (conda-forge/linux-64)
    -decorator-5.1.1 (conda-forge/noarch)
    -exceptiongroup-1.2.0 (conda-forge/noarch)
    -executing-2.0.1 (conda-forge/noarch)
    -ipython-8.20.0 (conda-forge/noarch)
    -jedi-0.19.1 (conda-forge/noarch)
    -ld_impl_linux-64-2.40 (conda-forge/linux-64)
    -libexpat-2.5.0 (conda-forge/linux-64)
    -libffi-3.4.2 (conda-forge/linux-64)
    -libnsl-2.0.1 (conda-forge/linux-64)
    -libsqlite-3.44.2 (conda-forge/linux-64)
    -libuuid-2.38.1 (conda-forge/linux-64)
    -libxcrypt-4.4.36 (conda-forge/linux-64)
    -libzlib-1.2.13 (conda-forge/linux-64)
    -matplotlib-inline-0.1.6 (conda-forge/noarch)
    -ncurses-6.4 (conda-forge/linux-64)
    -parso-0.8.3 (conda-forge/noarch)
    -pexpect-4.8.0 (conda-forge/noarch)
    -pickleshare-0.7.5 (conda-forge/noarch)
    -pip-23.3.2 (conda-forge/noarch)
    -prompt-toolkit-3.0.42 (conda-forge/noarch)
    -ptyprocess-0.7.0 (conda-forge/noarch)
    -pure_eval-0.2.2 (conda-forge/noarch)
    -pygments-2.17.2 (conda-forge/noarch)
    -python-3.12.1 (conda-forge/linux-64)
    -readline-8.2 (conda-forge/linux-64)
    -setuptools-69.0.3 (conda-forge/noarch)
    -six-1.16.0 (conda-forge/noarch)
    -stack_data-0.6.2 (conda-forge/noarch)
    -tk-8.6.13 (conda-forge/linux-64)
    -traitlets-5.14.1 (conda-forge/noarch)
    -typing_extensions-4.9.0 (conda-forge/noarch)
    -tzdata-2023d (conda-forge/noarch)
    -wcwidth-0.2.13 (conda-forge/noarch)
    -wheel-0.42.0 (conda-forge/noarch)
    -xz-5.2.6 (conda-forge/linux-64)

2024-01-13 09:37:42  (rev 3)
    +asttokens-2.4.1 (conda-forge/noarch)
    +bzip2-1.0.8 (conda-forge/linux-64)
    +decorator-5.1.1 (conda-forge/noarch)
    +exceptiongroup-1.2.0 (conda-forge/noarch)
    +executing-2.0.1 (conda-forge/noarch)
    +ipython-8.19.0 (conda-forge/noarch)
    +jedi-0.19.1 (conda-forge/noarch)
    +ld_impl_linux-64-2.40 (conda-forge/linux-64)
    +libexpat-2.5.0 (conda-forge/linux-64)
    +libffi-3.4.2 (conda-forge/linux-64)
    +libnsl-2.0.1 (conda-forge/linux-64)
    +libsqlite-3.44.2 (conda-forge/linux-64)
    +libuuid-2.38.1 (conda-forge/linux-64)
    +libxcrypt-4.4.36 (conda-forge/linux-64)
    +libzlib-1.2.13 (conda-forge/linux-64)
    +matplotlib-inline-0.1.6 (conda-forge/noarch)
    +ncurses-6.4 (conda-forge/linux-64)
    +parso-0.8.3 (conda-forge/noarch)
    +pexpect-4.8.0 (conda-forge/noarch)
    +pickleshare-0.7.5 (conda-forge/noarch)
    +pip-23.3.2 (conda-forge/noarch)
    +prompt-toolkit-3.0.42 (conda-forge/noarch)
    +ptyprocess-0.7.0 (conda-forge/noarch)
    +pure_eval-0.2.2 (conda-forge/noarch)
    +pygments-2.17.2 (conda-forge/noarch)
    +python-3.12.1 (conda-forge/linux-64)
    +readline-8.2 (conda-forge/linux-64)
    +setuptools-69.0.3 (conda-forge/noarch)
    +six-1.16.0 (conda-forge/noarch)
    +stack_data-0.6.2 (conda-forge/noarch)
    +tk-8.6.13 (conda-forge/linux-64)
    +traitlets-5.14.1 (conda-forge/noarch)
    +typing_extensions-4.9.0 (conda-forge/noarch)
    +tzdata-2023d (conda-forge/noarch)
    +wcwidth-0.2.13 (conda-forge/noarch)
    +wheel-0.42.0 (conda-forge/noarch)
    +xz-5.2.6 (conda-forge/linux-64)

2024-01-13 09:59:14  (rev 4)
     bzip2  {1.0.8 (conda-forge/linux-64) -> 1.0.8 (defaults/linux-64)}
     ca-certificates  {2023.11.17 (conda-forge/linux-64) -> 2023.12.12 (defaults/linux-64)}
     decorator  {5.1.1 (conda-forge/noarch) -> 5.1.1 (defaults/noarch)}
     ipython  {8.19.0 (conda-forge/noarch) -> 8.20.0 (defaults/linux-64)}
     libffi  {3.4.2 (conda-forge/linux-64) -> 3.4.4 (defaults/linux-64)}
     matplotlib-inline  {0.1.6 (conda-forge/noarch) -> 0.1.6 (defaults/linux-64)}
     ncurses  {6.4 (conda-forge/linux-64) -> 6.4 (defaults/linux-64)}
     parso  {0.8.3 (conda-forge/noarch) -> 0.8.3 (defaults/noarch)}
     pexpect  {4.8.0 (conda-forge/noarch) -> 4.8.0 (defaults/noarch)}
     pickleshare  {0.7.5 (conda-forge/noarch) -> 0.7.5 (defaults/noarch)}
     prompt-toolkit  {3.0.42 (conda-forge/noarch) -> 3.0.43 (defaults/linux-64)}
     ptyprocess  {0.7.0 (conda-forge/noarch) -> 0.7.0 (defaults/noarch)}
     pure_eval  {0.2.2 (conda-forge/noarch) -> 0.2.2 (defaults/noarch)}
     readline  {8.2 (conda-forge/linux-64) -> 8.2 (defaults/linux-64)}
     six  {1.16.0 (conda-forge/noarch) -> 1.16.0 (defaults/noarch)}
     tzdata  {2023d (conda-forge/noarch) -> 2023d (defaults/noarch)}
     xz  {5.2.6 (conda-forge/linux-64) -> 5.4.5 (defaults/linux-64)}
    +libstdcxx-ng-11.2.0 (defaults/linux-64)
    +prompt_toolkit-3.0.43 (defaults/noarch)

(notbase) username@pc:~$
```

Notice revision 0 has no packages in it. Revision 1 installs ipython, revision 2 removes ipython, revision 3 installs a specific version of ipython and revision 4 updates ipython.

### Install Revision

The ```install``` subcommand can be used with the option ```--revision``` that can be assigned to a revision number. For example a reversion to revision 3 can be made:

```bash
conda install -c conda-forge --revision=3
```

Note for some reason the conda package manager is inefficient here and it takes a while to solve the Python environment despite knowing all the previous package versions to install. Deleting the Python environment and recreating it with an exported yaml file is often faster.

Details about the changes will be output:

```
(notbase) username@pc:~$ conda install -c conda-forge --revision=3

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase

  added / updated specs:
    - ipython==8.20.0


The following packages will be REMOVED:
```
|details|
|---|
|libstdcxx-ng-11.2.0-h1234567_1|
|prompt_toolkit-3.0.43-hd3eb1b0_0|
```


The following packages will be UPDATED:

|package|old details||new details|
|---|---|---|---|
|bzip2|pkgs/main::bzip2-1.0.8-h7b6447c_0|-->|conda-forge::bzip2-1.0.8-hd590300_5|
|ncurses|pkgs/main::ncurses-6.4-h6a678d5_0|-->|conda-forge::ncurses-6.4-h59595ed_2|
|readline|pkgs/main::readline-8.2-h5eee18b_0|-->|conda-forge::readline-8.2-h8228510_1|

The following packages will be SUPERSEDED by a higher-priority channel:
```
|package|old details||new details|
|---|---|---|---|
|ca-certificates|pkgs/main::ca-certificates-2023.12.12~|-->|conda-forge::ca-certificates-2023.11.17-hbcca054_0|
|decorator|pkgs/main::decorator-5.1.1-pyhd3eb1b0~|-->|conda-forge::decorator-5.1.1-pyhd8ed1ab_0|
|ipython|pkgs/main/linux-64::ipython-8.20.0-py~|-->|conda-forge/noarch::ipython-8.19.0-pyh707e725_0|
|libffi|pkgs/main::libffi-3.4.4-h6a678d5_0|-->|conda-forge::libffi-3.4.2-h7f98852_5|
|matplotlib-inline|pkgs/main/linux-64::matplotlib-inline~|-->|conda-forge/noarch::matplotlib-inline-0.1.6-pyhd8ed1ab_0|
|parso|pkgs/main::parso-0.8.3-pyhd3eb1b0_0|-->|conda-forge::parso-0.8.3-pyhd8ed1ab_0|
|pexpect|pkgs/main::pexpect-4.8.0-pyhd3eb1b0_3|-->|conda-forge::pexpect-4.8.0-pyh1a96a4e_2|
|pickleshare|pkgs/main::pickleshare-0.7.5-pyhd3eb1~|-->|conda-forge::pickleshare-0.7.5-py_1003|
|prompt-toolkit|pkgs/main/linux-64::prompt-toolkit-3.~|-->|conda-forge/noarch::prompt-toolkit-3.0.42-pyha770c72_0|
|ptyprocess|pkgs/main::ptyprocess-0.7.0-pyhd3eb1b~|-->|conda-forge::ptyprocess-0.7.0-pyhd3deb0d_0|
|pure_eval|pkgs/main::pure_eval-0.2.2-pyhd3eb1b0~|-->|conda-forge::pure_eval-0.2.2-pyhd8ed1ab_0|
|six|pkgs/main::six-1.16.0-pyhd3eb1b0_1|-->|conda-forge::six-1.16.0-pyh6c4a22f_0|
|tzdata|pkgs/main::tzdata-2023d-h04d1e81_0|-->|conda-forge::tzdata-2023d-h0c530f3_0|
|xz|pkgs/main::xz-5.4.5-h5eee18b_0|-->|conda-forge::xz-5.2.6-h166bdaf_0|
```
Proceed ([y]/n)?
```

Input ```y``` in order to proceed and the proposed downgrade will be implemented:

```
Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(notbase) username@pc:~$
```

### Env Export

The currently activated Python environment can be exported to a **y**et another **m**arkdown **l**anguage yaml file using the ```env``` subcommand grouping followed by the subcommand ```export```. The Python environment can be exported to a yml file in the Documents folder using:

```bash
conda env export > Documents/notbase.yml
```

This outputs:

```
(notbase) username@pc:~$ conda env export > Documents/notbase.yml
(notbase) username@pc:~$
```

This creates a notbase.yml file in Documents:

<img src='images_conda/img_064.png' alt='img_064' width='450'/>

This can be opened in text editor:

```
name: notbase
channels:
  - conda-forge
  - defaults
dependencies:
  - _libgcc_mutex=0.1=conda_forge
  - _openmp_mutex=4.5=2_gnu
  - asttokens=2.4.1=pyhd8ed1ab_0
  - bzip2=1.0.8=hd590300_5
  - ca-certificates=2023.11.17=hbcca054_0
  - decorator=5.1.1=pyhd8ed1ab_0
  - exceptiongroup=1.2.0=pyhd8ed1ab_2
  - executing=2.0.1=pyhd8ed1ab_0
  - ipython=8.19.0=pyh707e725_0
  - jedi=0.19.1=pyhd8ed1ab_0
  - ld_impl_linux-64=2.40=h41732ed_0
  - libexpat=2.5.0=hcb278e6_1
  - libffi=3.4.2=h7f98852_5
  - libgcc-ng=13.2.0=h807b86a_3
  - libgomp=13.2.0=h807b86a_3
  - libnsl=2.0.1=hd590300_0
  - libsqlite=3.44.2=h2797004_0
  - libuuid=2.38.1=h0b41bf4_0
  - libxcrypt=4.4.36=hd590300_1
  - libzlib=1.2.13=hd590300_5
  - matplotlib-inline=0.1.6=pyhd8ed1ab_0
  - ncurses=6.4=h59595ed_2
  - openssl=3.2.0=hd590300_1
  - parso=0.8.3=pyhd8ed1ab_0
  - pexpect=4.8.0=pyh1a96a4e_2
  - pickleshare=0.7.5=py_1003
  - pip=23.3.2=pyhd8ed1ab_0
  - prompt-toolkit=3.0.42=pyha770c72_0
  - ptyprocess=0.7.0=pyhd3deb0d_0
  - pure_eval=0.2.2=pyhd8ed1ab_0
  - pygments=2.17.2=pyhd8ed1ab_0
  - python=3.12.1=hab00c5b_1_cpython
  - readline=8.2=h8228510_1
  - setuptools=69.0.3=pyhd8ed1ab_0
  - six=1.16.0=pyh6c4a22f_0
  - stack_data=0.6.2=pyhd8ed1ab_0
  - tk=8.6.13=noxft_h4845f30_101
  - traitlets=5.14.1=pyhd8ed1ab_0
  - typing_extensions=4.9.0=pyha770c72_0
  - tzdata=2023d=h0c530f3_0
  - wcwidth=0.2.13=pyhd8ed1ab_0
  - wheel=0.42.0=pyhd8ed1ab_0
  - xz=5.2.6=h166bdaf_0
prefix: ~/anaconda3/envs/notbase
```

<img src='images_conda/img_065.png' alt='img_065' width='450'/>

This is a very small file which can be shared on GitHub or emailed.

### Rename

The ```rename``` subcommand can be used to rename a Python environment. 

```bash
conda rename -n oldname newname
```

This effectively renames the folder:

```
~/anaconda3/envs/oldname
```

To:

```
~/anaconda3/envs/newname
```

The notbase Python environment can be renamed to reallynotbase using:

```bash
conda deactivate
conda rename -n notbase reallynotbase
```

This outputs:

```
(notbase) username@pc:~$ conda deactivate
(base) username@pc:~$ conda rename -n notbase reallynotbase
Source:      ~/anaconda3/envs/notbase
Destination: ~/anaconda3/envs/reallynotbase
Packages: 43
Files: 1

Downloading and Extracting Packages:


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(base) username@pc:~$
```

### Env Create

An environment can be created from a yml file using the ```env``` subcommand grouping followed by ```create```. Note that this differs from the ```create``` subcommand used directly by the ```conda``` package manager.

For example the notbase.yml Python environment in the Documents folder can be recreated using:

```bash
conda env create -f Documents/notbase.yml
```

Note that yml file specifies the channels used in addition to the version number and build number for each package so ```-c conda-forge``` is not necessary. The name of the Python environment is also specified so ```-n notbase``` is not necessary although can be used to change the name of the Python environment. This outputs:

```
(base) username@pc:~$ conda env create -f Documents/notbase.yml
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate notbase
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) username@pc:~$
```

### Env List

Python environments can be listed using the ```env``` subcommand grouping followed by the subcommand ```list```. Note that this differs from the subcommand ```list``` used directly from ```conda``` which lists Python environments instead.

```
conda env list
```

This outputs:

```
(base) username@pc:~$ conda env list
# conda environments:
```
|Environment Name|Selected|Location|
|---|---|---|
|base|*|~/anaconda3|
|notbase||~/anaconda3/envs/notbase|
|reallynotbase||~/anaconda3/envs/reallynotbase|
```
(base) username@pc:~$
```

### Env Remove

A Python environment can be removed using the ```env``` subcommand grouping and subcommand ```remove```. Once again this is different from the ```remove``` subcommand used directly by the ```conda``` package manager which instead removed Python packages:

An environment can be removed using the command:

```bash
conda env remove -n envname
```

For example the Python environment notbase can be removed using:

```bash
conda deactivate
conda env remove -n notbase
```

This outputs:

```
(base) username@pc:~$ conda env remove -n notbase

Remove all packages in environment ~/anaconda3/envs/notbase:

(base) username@pc:~$
```

### Clean

Anaconda downloads a package in the form of a tarball and then extracts the tarball to a Python environment. After extraction the tarball is not deleted and is instead cached. If another Python environment is created using that package version, the tarball will be extracted instead of being redownloaded making creation of the second Python environment faster.

When a Python environment is regularly updated, there will be multiple tarballs corresponding to the current release and all previous releases of a package and as a consequence this can occupy a large amount fo disk space.

The ```clean``` subcommand can be used to clean these:

```bash
conda clean --all
```

Input ```y``` to remove the tarballs, index cache and packages:

```
(base) username@pc:~$ conda clean --all
Will remove 1120 (2.29 GB) tarball(s).
Proceed ([y]/n)? y

Will remove 1 index cache(s).
Proceed ([y]/n)? y

Will remove 580 (5.21 GB) package(s).
Proceed ([y]/n)? y

There are no tempfile(s) to remove.
There are no logfile(s) to remove.
(base) username@pc:~$
```

## Python Environments for IDEs

Previously the subcommands ```create``` and ```install``` were used seperately and when the list of revisions was examined revision 0 had no packages. The ```create``` subcommand can be used to list a series of packages to be installed when creating a Python Environment. This command will be used to create a Python Environment suitable for the latest version of each Python IDE discussed.

### Jupyter

For Jupyter it is recommended to create a Python environment called ```jupyter-env``` with the following packages:

```bash
conda create -n jupyter-env -c conda-forge python jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt isort autopep8 ruff black ipympl jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker ghostscript nbconvert
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn. pandas needs pyarrow as a dependency.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

nodejs allows installation of JupyterLab extensions. ipywidgets and plotly can be used to create widgets and plots using Python code, under the hood JavaScript is used to display these in the browser. The variableinspector gives a variable inspector.

jupyterlab_code_formatter can be used with the formatters isort, autopep8 and black, ruff is not supported with this extension yet.

pyqt and ipympl are required for an interactive matplotlib plotting backends.

nbconvert is used for exporting notebooks to Python script files, html or pdf (which requires TeX).

ghostscript is required as a TeX dependency for nbconvert or matplotlib with TeX rendering. The TeX dependencies aren't added to the ```conda-forge``` channel and have to be installed system wide using the Debian based package manager ```apt```:

```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic cm-super dvipng
```

jupyterlab-spreadsheet-editor and jupyterlab-drawio are additional extensions that aren't yet updated to support the latest version of jupyterlab yet. For more details see [Extension Compatibility with JupyterLab 4.0](https://github.com/jupyterlab/jupyterlab/issues/14590).

Once the Python environment is created it can be activated using:

```bash
conda activate jupyter-env
```

And one of the jupyter applications can be launched using:

```bash
jupyter-console
jupyter-qtconsole
jupyter-notebook
jupyter-lab
```

### Spyder

For Spyder it is recommended to create a Python environment called ```spyder-env``` with the following packages:

```bash
conda create -n spyder-env -c conda-forge python spyder cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt ruff ghostscript
```

Once the Python environment is created it can be activated using:

```bash
conda activate spyder-env
```

And spyder can be launched using:

```bash
spyder
```

### JupyterLab with R

R can be used with JupyterLab. It is recommended to create a Python environment called r-env with the following packages:

```bash
conda create -n r-env -c conda-forge python jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt isort autopep8 ruff black ipympl jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker ghostscript nbconvert r-irkernel jupyter-lsp-r r-tidyverse r-ggthemes r-palmerpenguins r-writexl
```

This Python environment has the same packages as the ```jupyter-env``` but has the addition of the R Jernel and R Jupyter Language Server Protocol in addition to commonly used R packages.

Once the Python environment is created it can be activated using:

```bash
conda activate r-env
```

The kernels for the r-env Python environment can be listed using:

```bash
jupyter kernelspec list
```

This outputs:

```
(r-env) username@pc:~$ jupyter kernelspec list
Available kernels:
  ir         ~/anaconda3/envs/r-env/share/jupyter/kernels/ir
  python3    ~/anaconda3/envs/r-env/share/jupyter/kernels/python3
(r-env) username@pc:~$
```

One of the jupyter applications can be launched using the R kernel:

```bash
jupyter-console --kernel=ir
jupyter-qtconsole --kernel=ir
jupyter-notebook --kernel=ir
jupyter-lab --kernel=ir
```

### Spyder RC

Spyder is available as an alpha version. A Python environment with Python 3.11 from the conda-forge channel should be used:

```bash
conda create -n spyder-rc-env -c conda-forge python=3.11
```

This Python environment should be activated:

```bash
conda activate spyder-rc-env
```

Spyder 6 RC should then be installed from its own channel:

```bash
conda install -c conda-forge/label/spyder_dev -c conda-forge/label/spyder_kernels_rc -c conda-forge spyder=6.0.0a4
```

The datascience libraries commonly used with Spyder should be installed:

```bash
conda install -c conda-forge cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt ruff ghostscript
```

Once the Python environment is created it can be activated using:

```bash
conda activate spyder-rc-env
```

And spyder can be launched using:

```bash
spyder
```

Details about the latest Spyder version is outlined in [Spyders release notes](https://github.com/spyder-ide/spyder/releases). It is recommended to remove the old environment and create a new Python environment with the latest version of Spyder when a new pre-release is issued as updating packages using mixed channels may be problematic.

[Return to Python Tutorials](../../readme.md)
