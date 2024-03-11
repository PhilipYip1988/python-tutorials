# Anaconda Install (Ubuntu)

This guide looks at installing Anaconda 2024-02.1 on Ubuntu 24.04.

## Removing Previous Installations

Anaconda should be installed on a Linux PC that has no previous Python installations outwith the system Python. The system Python is preinstalled as part of the Linux Operating system and should be considered as part of the Operating System and not modified by the user.

If an old Anaconda Installation or an Anaconda based installation such as Miniconda or is present these should be removed by deleting their perspective folders. Note that deletion of these folders leaves behind a large number of configuration files and the presence of these files often results in problematic settings persisting after a reinstall. For best results it is recommended to delete all these configuration files. For more details see [Uninstallation Instructions](../uninstall/readme.md).

## System Python

Linux has a preinstalled version of Python which is known as the system Python. The system Python only contains standard libraries and should be considered as part of the Operating System and should not be modified by the end user as doing so may make the Operating System unstable.

When Files is opened, the User directory Home is selected:

<img src='./images/img_001.png' alt='img_001' width='450'/>

The System Python is in Other Locations and in the Root:

```bash
/
```

<img src='./images/img_002.png' alt='img_002' width='450'/>

In particular it is in the root bin folder and bin is an abbreviation for binaries:

```bash
/bin/
```

<img src='./images/img_003.png' alt='img_003' width='450'/>

This is a development version of Ubuntu 24.04 LTS and has two Python versions 3.11 and 3.12: 

<img src='./images/img_004.png' alt='img_004' width='450'/>

When the Terminal is opened, the ```~``` indicates the current working directory. The terminal by default also searches the ```/bin/``` folder for binaries:

<img src='./images/img_005.png' alt='img_005' width='450'/>

To access the latest Python the ```python3``` binary can be used (this is an alias to python3.12). The 3 exists because Linux used to ship with the latest version of Python 2 and Python 3 and it was used to distinguish these two versions. Python 2 has reached end of life and is no longer preinstalled:

<img src='./images/img_006.png' alt='img_006' width='450'/>

In the:

```bash
/lib/
```

folder are a number of libraries.

<img src='./images/img_007.png' alt='img_007' width='450'/>

The ones for Python 3.12 are found in the python3.12 folder:

```bash
/lib/python3.12
```

<img src='./images/img_008.png' alt='img_008' width='450'/>

For example the standard library email:

```bash
/lib/python3.12/email
```

<img src='./images/img_009.png' alt='img_009' width='450'/>

Has a ```__init__.py``` file which is imported when the folder is imported:

<img src='./images/img_010.png' alt='img_010' width='450'/>

<img src='./images/img_011.png' alt='img_011' width='450'/>

Some modules are single files, for example ```datetime.py```:

<img src='./images/img_012.png' alt='img_012' width='450'/>

<img src='./images/img_013.png' alt='img_013' width='450'/>

The system Python does not contain third-party libraries such as the scientific stack, numpy, pandas and matplotlib. If these are attempted to be used, a ModuleNotFoundError displays:

<img src='./images/img_014.png' alt='img_014' width='450'/>

Note two programming languages have been used so far bash and Python. The highlighted code is running in the Python shell and the code not highlighted is the bash shell. In this case bash, the default language of the terminal was used to run a Python session:

<img src='./images/img_015.png' alt='img_015' width='450'/>

## Anaconda vs Miniconda 

Anaconda is a Python distribution that has a base Python environment that is designed to be used *as is*. The base Python environment has the conda package manager that can be used to create a separate Python environment (subinstallation of Python) for a custom configuration of packages. 

Miniconda is a bootstrap version of Anaconda, that only contains the conda package manager and can likewise be used to create Python environments.

Anaconda should be preferenced when, the user required a preconfigured (base) Python environment to be used *as is*. When the user plans to only create custom Python environments, Miniconda should be preferenced.

### Anaconda Python Distribution

The Anaconda Python distribution comes with its own base Python environment that contains:

* Python
* Python Standard Libraries
* The conda Package Manager
* The Anaconda Navigator
* Third Party Libraries:
  * numpy
  * pandas
  * matplotlib
  * seaborn
  * plotly
  * pillow
  * scikit-learn
  * scikit-image
  * ⁝
* Third-party IDEs:
  * Spyder
  * Jupyter
    * JupyterLab
    * Jupyter Notebook
    * Jupyter QTConsole
    * Jupyter Console
* Third-party formatters:
  * autopep8
  * isort
  * black

### Miniconda

Miniconda is a stripped down version of Anaconda containing only:

* Python
* Python Standard Libraries
* The conda Package Manager

## conda

Anaconda and Miniconda have the conda package manager which should be used in preference to the native Python package manager pip. 

* conda
* ~~pip~~

pip is strictly a package manager for Python packages. However many datascience projects under the hood, use code that is written in C++ for performance gains. The conda package manager manages both the Python and non-Python dependencies. The conda package manager has also been written in C++ for increased performance and reliability. This was separately developed as mamba and the conda package manager uses the libmamba (C++) solver by default.

The conda package manager uses two channels:

* conda-forge
* anaconda

The first channel community forge is the community channel and has the largest number of packages available.

The second channel is the channel maintained by Anaconda Inc. Anaconda Inc test packages for compatibility with the Anaconda Python Distribution. 

As a consequence the latest version of a package available on the anaconda channel may be dated with respect to the package on the conda-forge channel as it takes Anaconda Inc some time to test packages. Moreover Anaconda Inc only test the most commonly used datascience libraries and therefore more niche packages will only be available on conda-forge.

In the Anaconda base environment the following commands should never be used:

* ~~pip install package~~
* ~~conda install conda-forge::package~~
* ~~conda install -c conda-forge package~~

This is because use of multiple package managers and use of multiple channels will make the Anaconda base Python environment unstable.

Only packages available from the anaconda channel should be installed in base:

* conda install anaconda::package
* conda install -c anaconda package

The base Python environment is normally used *as is* and instead a custom Python environment is used to install a subinstallation of Python with custom packages, usually from the conda-forge community channel. More details about channels will be given later.

## Download Links

The latest Anaconda and Miniconda installer can be downloaded from:

* [Anaconda](https://www.anaconda.com/download)
* [Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)

Using Anaconda as an example, Linux can be selected:

<img src='./images/img_016.png' alt='img_016' width='450'/>

Then the 64 Bit Linux installer can be downloaded:

<img src='./images/img_017.png' alt='img_017' width='450'/>

The download will be save in Downloads by default:

<img src='./images/img_018.png' alt='img_018' width='450'/>

## Installing

Go to the Downloads folder and right click blank space and select Open in Terminal:

<img src='./images/img_019.png' alt='img_019' width='450'/>

Note instead of Home ```~```, the Downloads folder displays ```~/Downloads```:

<img src='./images/img_020.png' alt='img_020' width='450'/>

If another files instance is opened. We can return to:

```bash
/
```

<img src='./images/img_021.png' alt='img_021' width='450'/>

```bash
/bin
```

<img src='./images/img_022.png' alt='img_022' width='450'/>

Notice there is a ```bash``` binary. This can be used to execute a shell script:

<img src='./images/img_023.png' alt='img_023' width='450'/>

If the shell script is right clicked and renamed:

<img src='./images/img_024.png' alt='img_024' width='450'/>

Its file name and file extension can be copied:

<img src='./images/img_025.png' alt='img_025' width='450'/>

This can be pasted into the terminal so the bash command runs the script:

<img src='./images/img_026.png' alt='img_026' width='450'/>

For Anaconda input:

```bash
bash Anaconda3-2024.02-1-Linux-x86_64.sh
```

Or for Miniconda input:

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

<img src='./images/img_027.png' alt='img_027' width='450'/>

Press ```↵```:

<img src='./images/img_028.png' alt='img_028' width='450'/>

Press ```q``` to quit scrolling through the license agreement:

<img src='./images/img_029.png' alt='img_029' width='450'/>

Input ```yes``` to accept:

<img src='./images/img_030.png' alt='img_030' width='450'/>

Press ```↵``` to install in the default location:

<img src='./images/img_031.png' alt='img_031' width='450'/>

During installation you will be asked to initialise Anaconda, input ```yes``` to proceed:

<img src='./images/img_032.png' alt='img_032' width='450'/>

Anaconda is installed and initialised and all open Terminals should be closed. New Terminals will be initialised:

<img src='./images/img_033.png' alt='img_033' width='450'/>

Unfortunately the default option for initialisation is ```no```. If you have selected this by mistake. Anaconda or Miniconda can be manually initialised by changing directory to the anaconda3 or miniconda3 binary subdirectory:

```bash
cd ~/anaconda3/bin
cd ~/miniconda3/bin
```

And then running:

```bash
./conda init
```

<img src='./images/img_034.png' alt='img_034' width='450'/>

The ```./``` is an instruction to run a binary from the current working directory. Once again the Terminal will need to be closed.

Any new Terminal instances will be initialised. The prefix ```(base)``` shows in the Terminal:

<img src='./images/img_035.png' alt='img_035' width='450'/>

Going to the Home directory:

```bash
~
```

<img src='./images/img_036.png' alt='img_036' width='450'/>

There is now a

```bash
~/anaconda3
```

folder:

<img src='./images/img_037.png' alt='img_037' width='450'/>

This has a

```bash
~/anaconda3/bin
```

subfolder:

<img src='./images/img_038.png' alt='img_038' width='450'/>

In this subfolder are python binaries. Notice there is a ```python3``` which also has the alias ```python``` and these correspond to the current version of python in the base Python environment which in the case for Anaconda is ```python3.11```:

<img src='./images/img_039.png' alt='img_039' width='450'/>

Because Anaconda is initialised, a search for a binary is made in the ```~/anaconda3/bin``` folder before it is made in the ```/bin``` folder.

This means the ```python3``` binary from the Anaconda base Python environment is used opposed to the system Python. This can be seen by the different version number:

<img src='./images/img_040.png' alt='img_040' width='450'/>

There is an associated

```bash
~/anaconda3/lib
```

folder:

<img src='./images/img_041.png' alt='img_041' width='450'/>

The ```python3.11``` contains the Python libraries:

<img src='./images/img_042.png' alt='img_042' width='450'/>

When the standard module email is imported, it is imported from this folder:

<img src='./images/img_043.png' alt='img_043' width='450'/>

<img src='./images/img_044.png' alt='img_044' width='450'/>

When the standard module datetime is imported, it is imported from this folder:

<img src='./images/img_045.png' alt='img_045' width='450'/>
<img src='./images/img_046.png' alt='img_046' width='450'/>

There is a 

```bash
~/anaconda3/lib/site-packages
```

folder for third-party libraries.

<img src='./images/img_047.png' alt='img_047' width='450'/>

There are a handful of entries for Miniconda but this is large for Anaconda. Anaconda has a ```numpy``` folder:

<img src='./images/img_048.png' alt='img_048' width='450'/>

When the module is imported, this file is imported:

<img src='./images/img_049.png' alt='img_049' width='450'/>

<img src='./images/img_050.png' alt='img_050' width='450'/>

```numpy``` is a large library and has submodules. A submodule can be in a folder and when this submodule is accessed, the following file is accessed:

<img src='./images/img_051.png' alt='img_051' width='450'/>

<img src='./images/img_052.png' alt='img_052' width='450'/>

<img src='./images/img_053.png' alt='img_053' width='450'/>

Once again, the highlighted Python shell is ran within a bash shell:

<img src='./images/img_054.png' alt='img_054' width='450'/>

If the 

```bash
~/anaconda3/bin
```

folder is opened. 

<img src='./images/img_055.png' alt='img_055' width='450'/>

There is the binary ```clear``` which can be used to clear the bash shell:

<img src='./images/img_056.png' alt='img_056' width='450'/>

<img src='./images/img_057.png' alt='img_057' width='450'/>

<img src='./images/img_058.png' alt='img_058' width='450'/>

The ```conda``` binary is the conda package manager:

<img src='./images/img_059.png' alt='img_059' width='450'/>

Details about its commands can be seen by inputting 

```bash
conda
```

<img src='./images/img_060.png' alt='img_060' width='450'/>

For Anaconda or Miniconda, frequent checks should be made for the ```conda``` package manager:

```bash
conda update conda
```

as it is commonly updated to address bug fixes when new packages are released.

For Anaconda, updating the package manager will update the Anaconda Python distribution.

<img src='./images/img_061.png' alt='img_061' width='450'/>

In this case, the ```conda``` package manager is up to date.

<img src='./images/img_062.png' alt='img_062' width='450'/>

For Anaconda, the Anaconda Navigator is usually separately updated:

```bash
conda update anaconda-navigator
```

<img src='./images/img_063.png' alt='img_063' width='450'/>

In this case, there is an update that can be installed:

<img src='./images/img_064.png' alt='img_064' width='450'/>

<img src='./images/img_065.png' alt='img_065' width='450'/>

```conda``` is a cross-platform package manager used for installing packages related to datascience.

Ubuntu has its own specific package manager (```snap```) and because it is based on Debian also has (```apt```).

The native package manager is found in:

```bash
/bin
```

<img src='./images/img_066.png' alt='img_066' width='450'/>

<img src='./images/img_067.png' alt='img_067' width='450'/>

<img src='./images/img_068.png' alt='img_068' width='450'/>

Because there is no equivalent in ```conda/bin````, this binary will be used. TeX will be installed system wide:

```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic cm-super dvipng
```

Because changes are being made to the system, the command needs to be run as a super user. ```sudo``` means *superuser do*.

<img src='./images/img_069.png' alt='img_069' width='450'/>

You will need to provide your password to continue with the operation:

<img src='./images/img_070.png' alt='img_070' width='450'/>

Input ```y``` to proceed:

<img src='./images/img_071.png' alt='img_071' width='450'/>

<img src='./images/img_072.png' alt='img_072' width='450'/>

## Anaconda Navigator

The Anaconda Navigator is a GUI implementation of the ```conda``` package manager.

This is not available in Miniconda and not commonly installed in Miniconda.

Going back to 

```bash
~/anaconda3/bin
```

<img src='./images/img_073.png' alt='img_073' width='450'/>

<img src='./images/img_074.png' alt='img_074' width='450'/>

Is the ```anaconda-navigator``` binary, notice the ```-``` which needs to be supplied.

<img src='./images/img_075.png' alt='img_075' width='450'/>

The Anaconda Navigator can be launched using:

```bash
anaconda-navigator
```

<img src='./images/img_076.png' alt='img_076' width='450'/>

Notice that the Terminal will be busy as it is running the event loop required for the QT application window to show:

<img src='./images/img_077.png' alt='img_077' width='450'/>

The Anaconda Navigator contains a number of shortcuts to preinstalled IDEs:

<img src='./images/img_078.png' alt='img_078' width='450'/>

Its settings can be changed by going to File and Preferences:

<img src='./images/img_079.png' alt='img_079' width='450'/>

Unfortunately the Enable High DPI Scaling Setting doesn't always work well and on some screens, the following window will be outside the screen viewing area making it impossible to select the Apply button:

<img src='./images/img_080.png' alt='img_080' width='450'/>

There are settings to Edit the Navigator and Conda programmatically:

<img src='./images/img_081.png' alt='img_081' width='450'/>

<img src='./images/img_082.png' alt='img_082' width='450'/>

<img src='./images/img_083.png' alt='img_083' width='450'/>

If this does not display properly on your screen, Enable Hidden Files:

<img src='./images/img_084.png' alt='img_084' width='450'/>

Go to the 

```bash
~/.anaconda3/navigator
```

folder:

<img src='./images/img_085.png' alt='img_085' width='450'/>

<img src='./images/img_086.png' alt='img_086' width='450'/>

And edit the ```anaconda-navigator.ini``` file in the text editor:

<img src='./images/img_087.png' alt='img_087' width='450'/>

Set the ```enable_high_dpi_scaling```` to ```False```:

<img src='./images/img_088.png' alt='img_088' width='450'/>

Go to

```bash
~
```

The ```.condarc``` (conda recall parameters) should be automatically generated

<img src='./images/img_089.png' alt='img_089' width='450'/>

It should be configured to use the default settings:

<img src='./images/img_090.png' alt='img_090' width='450'/>

This can be updated to another channel for example the community channel. 

**However it is not recommended to change this as it may lead to an attempted update of base using the wrong channel which will result in an unstable base Python environment.**

<img src='./images/img_091.png' alt='img_091' width='450'/>

The Terminal is busy while the event loop for the QT MainWindow is open:

<img src='./images/img_092.png' alt='img_092' width='450'/>

When this Windows is closed:

<img src='./images/img_093.png' alt='img_093' width='450'/>

The Terminal should finish the process and move onto the next prompt. If it does not press ```Ctrl``` + ```c``` to close the currently running operation:

<img src='./images/img_094.png' alt='img_094' width='450'/>

Note to copy in the Terminal ```Ctrl```, ```⇧``` + ```c``` is used to copy and to paste in the Terminal ```Ctrl```, ```⇧``` + ```v``` is used.

## IPython

Interactive Python (ipython) is a modified ipython shell. It isn't included with Miniconda but is typically installed in a Python environment with an IDE that is powered by ipython.

When installed, there is an ```ipython``` and ```ipython3``` binary which are alias of one another. The ipython shell looks similar to the Python shell however the prompt is numeric:

<img src='./images/img_095.png' alt='img_095' width='450'/>

Pressing ```↹``` after a prefix will also show a list of identifiers that start with that prefix:

<img src='./images/img_096.png' alt='img_096' width='450'/>

The identifiers beginning with ```%``` are *ipython magics*. ipython magics are essentially reimplementations of common bash commands that are used when working with a Python script. For example ```%conda``` which can be sued to access the conda package manager. An ipython magic can be used in the middle of an ipython shell allowing the versatility of both shells without exiting the shell and losing all variables. 

The ```?``` can be used to print out a docstring:

<img src='./images/img_097.png' alt='img_097' width='450'/>

Notice also that syntax highlighting is also applied:

<img src='./images/img_098.png' alt='img_098' width='450'/>

The ipython shell can be exited:

<img src='./images/img_099.png' alt='img_099' width='450'/>

## Jupyter

Jupyter is an abbreviation for Julia, Python et R. There are four main binaries:

* ```jupyter-console```
* ```jupyter-qtconsole```
* ```jupyter-notebook```
* ```jupyter-lab```

The binary ```jupyter``` also accepts the command option:

* ```jupyter console```
* ```jupyter qtconsole```
* ```jupyter notebook```
* ```jupyter lab```

<img src='./images/img_100.png' alt='img_100' width='450'/>

In the Anaconda Python distribution only the Python Kernel is preinstalled. For Miniconda/Anaconda, the latest version of jupyter can be installed in a separate Python environment under the name ```jupyter-env``` using packages from the community channel ```conda-forge``` using:

```bash
conda create -n jupyter-env -c conda-forge python jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt isort autopep8 ruff black ipympl jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker ghostscript nbconvert julia r-irkernel jupyter-lsp-r r-tidyverse r-ggthemes r-palmerpenguins r-writexl
```

The following specifies the name of the environment and channel used to install packages from respectively:

```
-n jupyter-env 
-c conda-forge
```

<img src='./images/img_101.png' alt='img_101' width='450'/>

The package ```julia``` will install the Julia programming language and Julia kernel. Julia has its own package manager which should be used for its own libraries.

The package ```r-irkernel``` will install the R programming language and the R kernel. R has its own package manager however its use should be avoided in a conda environment and additional packages should be installed from the community channel ```conda-forge```.

Details about the packages to be installed will be listed, press ```y``` to proceed. Note if Julia and R are installed the latest version of Python may not be installed as ```conda``` will determine the latest version of Python compatible with the other programming languages:

<img src='./images/img_102.png' alt='img_102' width='450'/>

The Python environment is created with the list of packages:

<img src='./images/img_103.png' alt='img_103' width='450'/>

To use it, it needs to be activated:

```bash
conda activate jupyter-env
```

<img src='./images/img_104.png' alt='img_104' width='450'/>

Notice the ```(base)``` prefix is now replaced by ```(jupyter-env)```. This means changes to packages will occur in this environment when ```conda``` is used and ```-n``` isn't specified. In addition binaries will be preferentially searched for in the ```jupyter-env``` Python environment before looking in the ```base``` Python environment or the system Python environment:

<img src='./images/img_105.png' alt='img_105' width='450'/>

Python environments are found in the subfolder:

```bash
~/anaconda3/envs
~/miniconda3/envs
```

Now the three programming languages can be used:

<img src='./images/img_106.png' alt='img_106' width='450'/>

<img src='./images/img_107.png' alt='img_107' width='450'/>

<img src='./images/img_108.png' alt='img_108' width='450'/>

The kernels can be listed using:

```bash
jupyter kernelspec list
```

<img src='./images/img_109.png' alt='img_109' width='450'/>

The ```jupyter-console``` can be launched using. By default the Python (ipython) kernel is used:

```bash
jupyter-console
```

<img src='./images/img_110.png' alt='img_110' width='450'/>

Another kernel can be specified using the option ```--kernel```, for example R can be selected using:

```bash
jupyter-console --kernel=ir
```

<img src='./images/img_111.png' alt='img_111' width='450'/>

The QTConsole is a rewrite of the Terminal using QT:

```bash
jupyter-qtconsole
```

<img src='./images/img_112.png' alt='img_112' width='450'/>

The Terminal remains busy as the QT MainWindow application is running:

<img src='./images/img_113.png' alt='img_113' width='450'/>

The QTConsole is similar to the ipython console. Pressing ```↹``` after a prefix will display identifiers:

<img src='./images/img_114.png' alt='img_114' width='450'/>

A docstring will display as a popup when a recognised function is input with open parenthesis:

<img src='./images/img_115.png' alt='img_115' width='450'/>

The QTConsole will also nest the graphics:

<img src='./images/img_116.png' alt='img_116' width='450'/>

The session can be saved to HTML, which is the file format used for a static website:

<img src='./images/img_117.png' alt='img_117' width='450'/>

This can be saved to Documents:

<img src='./images/img_118.png' alt='img_118' width='250'/>

The images can be kept as Inline:

<img src='./images/img_119.png' alt='img_119' width='200'/>

This file can be opened:

<img src='./images/img_120.png' alt='img_120' width='450'/>

Which will display as a website that can be shared:

<img src='./images/img_121.png' alt='img_121' width='450'/>

The ```jupyter-lab``` binary can be launched using:

```bash
jupyter-lab
```

<img src='./images/img_122.png' alt='img_122' width='450'/>

JupyterLab runs a server in the Terminal and displays all the visual UI elements in the browser:

<img src='./images/img_123.png' alt='img_123' width='450'/>

It has a files tab which is a browser based version of files and a number of tiles which can be used to create new files. Additional options will be added if the Python environment with Julia and R is used instead of base. A new notebook file can be created:

<img src='./images/img_124.png' alt='img_124' width='450'/>

It can be renamed in files:

<img src='./images/img_125.png' alt='img_125' width='450'/>

Similar code to the QTConsole can be added. It is also possible to add markdown cells for formatted text: 

<img src='./images/img_126.png' alt='img_126' width='450'/>

The popup balloon for a docstring will only display if ```⇧``` + ```↹``` are pressed:

<img src='./images/img_127.png' alt='img_127' width='450'/>

Identifiers will only display if ```↹``` is pressed after a prefix:

<img src='./images/img_128.png' alt='img_128' width='450'/>

The prefix can be a datamodel identifier which is otherwise hidden by default:

<img src='./images/img_129.png' alt='img_129' width='450'/>

JupyterLab has a Variable Inspector which can be accessed by right clicking on the notebook and selecting Open Variable Inspector:

<img src='./images/img_130.png' alt='img_130' width='450'/>

<img src='./images/img_131.png' alt='img_131' width='450'/>

The notebook can be saved:

<img src='./images/img_132.png' alt='img_132' width='450'/>

If the notebook is examined in Ubuntu files:

<img src='./images/img_133.png' alt='img_133' width='450'/>

It is in the form of a JSON file. The browser uses these instructions to display the content. Note that a notebook is typically reopened within JupyterLab (with the Kernel restarted) and not using a text editor:

<img src='./images/img_134.png' alt='img_134' width='450'/>

Note when the tab is closed:

<img src='./images/img_135.png' alt='img_135' width='450'/>

The server is still running, in the Terminal:

<img src='./images/img_136.png' alt='img_136' width='450'/>

Press ```Ctrl``` + ```c``` to close the currently running operation, then press ```y``` when prompted:

<img src='./images/img_137.png' alt='img_137' width='450'/>

The server is closed and a new prompt displays:

<img src='./images/img_138.png' alt='img_138' width='450'/>

## Spyder

Another binary preinstalled by Anaconda is Spyder:

<img src='./images/img_139.png' alt='img_139' width='450'/>

The latest version for Anaconda/Miniconda can be installed in a separate Python environment using:

```bash
conda create -n spyder-env -c conda-forge python spyder cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt ruff ghostscript
```

Spyder can be launched (activating the appropriate Python environment if necessary) by using:

```bash
spyder
```

<img src='./images/img_140.png' alt='img_140' width='450'/>

This IDE has a script editor, that applies syntax highlighting, highlights syntax errors and has a number of tools to help improve code quality:

<img src='./images/img_141.png' alt='img_141' width='450'/>

The Source menu has the Format File or Selection with AutoPEP8 option:

<img src='./images/img_142.png' alt='img_142' width='450'/>

This will move imports to the top and address spacing issues:

<img src='./images/img_143.png' alt='img_143' width='450'/>

The autoformatter can be changed using Tools → Preferences:

<img src='./images/img_144.png' alt='img_1444' width='450'/>

Selecting the Code and Linting tab to the left and then switching to black:

<img src='./images/img_145.png' alt='img_145' width='450'/>

Now the Source menu has the Format File or Selection with Black option:

<img src='./images/img_146.png' alt='img_146' width='450'/>

This applies blacks opinionated formatting. At current there are some limitations as black won't organise the imports correctly before applying opinionated formatting and so black does not work unless autopep8 has previously been used:

<img src='./images/img_147.png' alt='img_147' width='450'/>

These options use the ```autopep``` and ```black``` applications found in the:

```bash
~\anaconda3\bin
```

folder. Spyder does not yet support ```isort``` which is used to sort the imports alphabetically in two groupings (by standard module and third-party modules).

Unfortunately, blacks opinionated formatting differs from Pythons default representation and therefore many Python developers dislike black. A new project ruff is a faster implementation of black which can be configured to match Pythons default representation. Ruff is not yet integrated in Anaconda or Spyder.

Spyder has a very powerful Variable Explorer which can be used to visualise variables:

<img src='./images/img_148.png' alt='img_148' width='450'/>

A variable that is a ```Collection``` can be expanded. By default GNOM will display the currently selected window on top, meaning if the Spyder IDE is selected, the Variable will be behind it. This can be prevented by right clicking the Variable and selecting Always on Top:

<img src='./images/img_149.png' alt='img_149' width='450'/>

Identifiers corresponding to a prefix will display as a popup, alongside the associated docstring for a function:

<img src='./images/img_150.png' alt='img_150' width='450'/>

The docstring can also be accessed by right clicking an object and selecting Inspect current object:

<img src='./images/img_151.png' alt='img_151' width='450'/>

This will open up the documentation in the Help pane:

<img src='./images/img_152.png' alt='img_152' width='450'/>

Plots are by default displayed as static images in the plots pane:

<img src='./images/img_153.png' alt='img_153' width='450'/>

The plot preferences can be changed by going to Tools → Preferences:

<img src='./images/img_154.png' alt='img_154' width='450'/>

Selecting the IPython Console tab to the left, the Graphics tab to the top right and changing the backend to Qt5 (Automatic is an alias for Qt5):

<img src='./images/img_155.png' alt='img_155' width='450'/>

To apply the new preferences select Consoles → Restart Kernel:

<img src='./images/img_156.png' alt='img_156' width='450'/>

Running the script will now display the plot in its own interactive window:

<img src='./images/img_157.png' alt='img_157' width='450'/>

A comment can be added to a Python script file using ```#```. If ```#%%``` is used, a new cell is created:

<img src='./images/img_158.png' alt='img_158' width='450'/>

The script file can be saved using File → Save As...:

<img src='./images/img_159.png' alt='img_159' width='450'/>

It can then be saved to the Documents folder:

<img src='./images/img_160.png' alt='img_160' width='450'/>

When this script is now rerun, the current working directory of the script file displays in the files tab:

<img src='./images/img_161.png' alt='img_161' width='450'/>

The script file can be viewed in file explorer:

<img src='./images/img_162.png' alt='img_162' width='450'/>

And opened in text editor. This applies syntax highlight but lacks other capabilities such as the ability to quickly look up identifiers or view a docstring:

<img src='./images/img_163.png' alt='img_163' width='450'/>

When Spyder is closed, a new prompt will display. If it doesn't, press ```Ctrl``` + ```c``` to close the currently running operation:

<img src='./images/img_164.png' alt='img_164' width='450'/>

## bioconda

So far two Python channels have been examined:

* ```conda-forge``` (community)
* ```anaconda``` (maintained by the Anaconda company and tested for the Anaconda Python distribution)

The packages installed have been limited to popular packages that are widely used and actively maintained. In essence the following packages are normally tested when a Python version is in an alpha or beta stage and therefore updated for a RTM release of Python.

When a package becomes more specialised, there are normally only a smaller number of developers. These developers do not have the time to test for the current version of Python but instead release packages for a stable version of Python. i.e. the version of Python that is only being issued bugfixes, which is currently 3.10. For more details see [Python Versions](https://devguide.python.org/versions/).

When attempting to install such niche libraries, these libraries should be specified during creation of a Python environment so that the ```conda``` package manager can look at the latest version of the niche library and examine its requirements and therefore determine the latest version of Python and numpy to install. This is more reliable than attempting to downgrade versions of Python and numpy from a currently existing environment which usually results in an unstable Python environment.

Many of the bioinformatics tools are only developed for Posix systems (Linux/Mac) and are on the separate channel:

* ```bioconda``` 

Details about the packages available for this channel are given in the [bioconda documentation](https://bioconda.github.io/).

The two channels are generally used together:

* ```conda-forge```
* ```bioconda```

The channels are specified using:

```bash
-c conda-forge -c bioconda
```

Which is an instruction to look for a package on the community channel first and the bioconda channel second.

Note that packages on the ```bioconda``` channel are not typically configured to work with packages on the ```anaconda``` channel. Attempting to mix these channels will result in an unstable Python environment which cannot be solved.

Therefore if the command is used, it will install packages from both channels:

```bash
conda create -n bioinformatics-env -c conda-forge -c bioconda python jupyterlab cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly jupyterlab-variableinspector ipympl pyqt r-irkernel jupyter-lsp-r r-tidyverse r-ggthemes r-palmerpenguins r-writexl samtools htslib pysam bcftools bedtools libdeflate blast bioconductor-iranges bioconductor-s4vectors bioconductor-biocgenerics bowtie2 bioconductor-biobase bioconductor-biostrings bioconductor-genomeinfodb bioconductor-genomicranges bioconductor-zlibbioc bioconductor-xvector bioconductor-biocparallel bwa bioconductor-summarizedexperiment
```

<img src='./images/img_165.png' alt='img_165' width='450'/>

The ```conda``` package manager will search each channel for each package specified and as well as the package dependencies. It will solve the environment until the latest compatible set is found:

<img src='./images/img_166.png' alt='img_166' width='450'/>

Details about each package will be specified:

<img src='./images/img_167.png' alt='img_167' width='450'/>

The latest "stable" version of Python:

<img src='./images/img_168.png' alt='img_168' width='450'/>

and ```numpy``` will be used:

<img src='./images/img_169.png' alt='img_169' width='450'/>

Input ```y``` in order to proceed:

<img src='./images/img_170.png' alt='img_170' width='450'/>

The Python environment is now created:

<img src='./images/img_171.png' alt='img_171' width='450'/>

## Environment File

The currently activate environment can be exported to a yml (yet another markdown file) file:

```bash
conda activate bioinformatics-env
conda env export > Documents/bioinformatic.yml
```

<img src='./images/img_172.png' alt='img_172' width='450'/>

If this file is opened in text editor:

<img src='./images/img_173.png' alt='img_173' width='450'/>

The channels and dependencies are shown. Note that a specific version of each package is specified:

<img src='./images/img_174.png' alt='img_174' width='450'/>

The environment can be removed by using:

```bash
conda deactivate
conda env remove -n bioinformatics-env
```

<img src='./images/img_175.png' alt='img_175' width='450'/>

In academic settings, an academic may issue a yml file which will reduce the liklihood of students encountering errors due to changes in newer versions of the libraries used.

The ```bioinformatics-env``` specified in the ```bioinformatic.yml``` file can be recreated using:

```bash
conda env create -f Documents/bioinformatic.yml
```

<img src='./images/img_176.png' alt='img_176' width='450'/>

Because all the packages are specified, they will be downloaded. Quite often, the yml files are platform agnostic, however because this yml uses the ```bioconda``` channel which only has packages for Posix systems (Linux/Mac) it won't work on Windows unless WSL is used:

<img src='./images/img_177.png' alt='img_177' width='450'/>

## Updating an Environment

The ```conda``` package manager can be used to update ```--all``` packages to the latest version.

**--all should never be used with base**, instead the ```conda``` package manager should be used to update ```conda``` which will collectively update the distribution.

**-c conda-forge or -c bioconda should never be used with base**, instead only the ```anaconda``` channel (also known as the default channel) should be used.

The ```hupyter-env``` can be updated using:

```bash
conda active jupyter-env
conda update -c conda-forge --all
```

<img src='./images/img_178.png' alt='img_178' width='450'/>

In this case, a small number of packages are found which can be upgraded but a package is substantially downgraded:

<img src='./images/img_179.png' alt='img_179' width='450'/>

Press ```y``` to proceed:

<img src='./images/img_180.png' alt='img_180' width='450'/>

Often with large Python environments, better results are achieved by deleted the Python environment and recreating it with all packages specified during the time of creation opposed to attempting to update an existing Python environment.

## Revision

The packages in a conda environment can be listed using the ```list``` command:

```bash
conda list
```

<img src='./images/img_181.png' alt='img_181' width='450'/>

The ```--revision``` option can be used to list packages for each revision:

```bash
conda list --revision
```

<img src='./images/img_182.png' alt='img_182' width='450'/>

<img src='./images/img_183.png' alt='img_183' width='450'/>

The ```install``` command can use the ```--revision``` option to revert to a previous revision:

```bash
conda install -c conda-forge --revision=0
```

<img src='./images/img_184.png' alt='img_184' width='450'/>

However the conda package manager, seems to hang for an extremely long time here for such a simple change. This command option will likely be optimized in a later version of conda. Unfortunately the conda env export command isn't configured to recognize ```--revision``` as an option so it is recommended to export an environment out to a yml files before updating it.

[Return to Python Tutorials](../../../readme.md)