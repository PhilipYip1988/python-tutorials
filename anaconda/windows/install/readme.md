# Anaconda Install (Windows)

This guide looks at installing Anaconda 2024-06.1 on Windows 11.

## Removing Previous Installations

Anaconda should be installed on a Windows PC that has no previous Python installations. Note that uninstalling Anaconda leaves behind a large number of configuration files and the presence of these files often results in problematic settings persisting after a reinstall. For best results it is recommended to delete all these configuration files. For more details see [Uninstallation Instructions](../uninstall/readme.md).

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

Using Anaconda as an example, Windows 11 can be selected:

<img src='./images/img_001.png' alt='img_001' width='450'/>

Select the 64 Bit Graphical Installer:

<img src='./images/img_002.png' alt='img_002' width='450'/>

The download will be save in Downloads by default:

<img src='./images/img_003.png' alt='img_003' width='450'/>

## Install

Double click it to launch the installer:

<img src='./images/img_004.png' alt='img_004' width='450'/>

Select Next:

<img src='./images/img_005.png' alt='img_005' width='450'/>

Then I Agree:

<img src='./images/img_006.png' alt='img_006' width='450'/>

Anaconda should be installed for a single user. Select Just Me (recommended) and then Next:

<img src='./images/img_007.png' alt='img_007' width='450'/>

The default install location is a subfolder of the user profile:

<img src='./images/img_008.png' alt='img_008' width='450'/>

This is accessed in Windows Explorer using the environmental variable:

```powershell
%USERPROFILE%
```

<img src='./images/img_009.png' alt='img_009' width='450'/>

<img src='./images/img_010.png' alt='img_010' width='450'/>

If the Start button is right clicked and the Terminal launched:

<img src='./images/img_011.png' alt='img_011' width='200'/>

The Terminal opens in the default location which is the User Profile:

<img src='./images/img_012.png' alt='img_012' width='450'/>

In the Terminal, the User Profile can be accessed using:

```powershell
~
```

<img src='./images/img_013.png' alt='img_013' width='450'/>

Select Next:

<img src='./images/img_014.png' alt='img_014' width='450'/>

Use the default options and select Install:

<img src='./images/img_015.png' alt='img_015' width='450'/>

Select Next:

<img src='./images/img_016.png' alt='img_016' width='450'/>

Select Next:

<img src='./images/img_017.png' alt='img_017' width='450'/>

Select Finish:

<img src='./images/img_018.png' alt='img_018' width='450'/>

## Python

Anaconda or Miniconda are installed in

```powershell
%USERPROFILE%\anaconda3
%USERPROFILE%\miniconda3
```

<img src='./images/img_019.png' alt='img_019' width='450'/>

This folder contains the base ```python.exe```:

<img src='./images/img_020.png' alt='img_020' width='450'/>

In the Start Menu, there is an Anaconda3 folder, there are two shells:

* Anaconda PowerShell Prompt
* ~~Anaconda CMD Prompt~~

This is because Windows has two shells, the modern PowerShell and legacy CMD. PowerShell is more feature rich and should be preferentially used:

<img src='./images/img_021.png' alt='img_021' width='450'/>

The Anaconda PowerShell Prompt has ```(base)``` as a prefix which means it will look in the locations associated with the base Python environment for an application. The ```python.exe``` for example can be run. Note the ```.exe``` file extension is not typically specified so it is run using:

```powershell
python
```

<img src='./images/img_022.png' alt='img_022' width='450'/>

The Windows Terminal is not initialised and does not look in the base Python environment:

<img src='./images/img_023.png' alt='img_023' width='450'/>

It therefore cannot find the ```python.exe``` and prompts for installation of a system Python via the Microsoft Store. This shouldn't be installed as it'll create confusion.

<img src='./images/img_024.png' alt='img_024' width='450'/>

The ```python.exe``` from base can be used by specifying the full path:

```powershell
~\anaconda3\python
```

<img src='./images/img_025.png' alt='img_025' width='450'/>

## Python Libraries

The python installation has an associated:

```powershell
~\anaconda3\Lib
```

folder where Python Libraries are stored.

<img src='./images/img_026.png' alt='img_026' width='450'/>

This contains the standard libraries such as email:

<img src='./images/img_027.png' alt='img_027' width='450'/>

Note that this folder has a datamodel initialisation file ```__init__.py``` which is reference when the module is imported.

Note Windows uses ```\``` as a path separator and Python also uses ```\``` to insert an escape character into a ```str```. Therefore ```\\``` gives an instruction to ```\``` itself as an escape character. When the ```str``` is printed, the escape characters are processed:

<img src='./images/img_028.png' alt='img_028' width='450'/>

<img src='./images/img_029.png' alt='img_029' width='450'/>

Other standard modules are individual modules, such as datetime. These are referenced when these modules are imported:

<img src='./images/img_030.png' alt='img_030' width='450'/>

<img src='./images/img_031.png' alt='img_031' width='450'/>

Third-party libraries are found in the subfolder

```powershell
~\anaconda3\Lib\site-packages
```

<img src='./images/img_032.png' alt='img_032' width='450'/>

Anaconda has the most commonly used datascience libraries such as numpy (Miniconda doesn't have this library preinstalled). There is a folder for a library and another folder which details the version number:

<img src='./images/img_033.png' alt='img_033' width='450'/>

The ```__init__.py``` file is reference when this library is imported, using the alias ```np```:

<img src='./images/img_034.png' alt='img_034' width='450'/>

<img src='./images/img_035.png' alt='img_035' width='450'/>

numpy is a very large library and has submodules, the submodule random can also be imported:

<img src='./images/img_036.png' alt='img_036' width='450'/>

Notice it has its own associated ```__init__.py``` file:

<img src='./images/img_037.png' alt='img_037' width='450'/>

This file is referenced when this module is used:

<img src='./images/img_038.png' alt='img_038' width='450'/>

So far the Anaconda PowerShell Prompt has been used which as the name suggests uses PowerShell by default as a programming language. This has been used to run a Python Shell. 

All the code in the highlighted selection is Python code and has the prompt ```>>>```. The code outside the highlighted selection has a prompt ```(base) PS ~>``` where PS means PowerShell:

<img src='./images/img_039.png' alt='img_039' width='450'/>

## conda Package Manager

Other applications associated with the base Python environment are found in the 

```powershell
~\anaconda3\Scripts
```

folder. 

<img src='./images/img_040.png' alt='img_040' width='450'/>

This has the ```conda``` package manager:

<img src='./images/img_041.png' alt='img_041' width='450'/>

The Anaconda PowerShell Prompt can be cleared using:

```powershell
clear
```

<img src='./images/img_042.png' alt='img_042' width='450'/>

The ```conda``` package manager can be used:

```powershell
conda
```

<img src='./images/img_043.png' alt='img_043' width='450'/>

And an output of commands recognised by this application are listed:

<img src='./images/img_044.png' alt='img_044' width='450'/>

## Updating

The ```conda``` package manager is updated approximately monthly to address bugfixes with newer packages and should be updated to the newest version on Anaconda or Miniconda using:

```powershell
conda update conda
```

<img src='./images/img_045.png' alt='img_045' width='450'/>

The channel used shows defaults which is the ```anaconda``` channel and this is the only channel that should be used for base. Using another channel here will create an unstable base Python environment.

Updating the conda package manager on Anaconda will usually update some other components in the remaining Python distribution.

In this case, conda is already updated updated as the standalone installers have just been released:

<img src='./images/img_046.png' alt='img_046' width='450'/>

On Anaconda, the Anaconda Navigator is updated separately, so it can be independently updated when using the Anaconda Navigator GUI. It is normally more reliable to update it using:

```powershell
conda update anaconda-navigator
```

Input ```y``` to proceed with any changes:

<img src='./images/img_047.png' alt='img_047' width='450'/>

The Anaconda Navigator is now updated:

<img src='./images/img_048.png' alt='img_048' width='450'/>

## MikTeX

Anaconda doesn't contain all the TeX fonts which are required when exporting a notebook with TeX or creating a plot with TeX.

They can be installed using MikTex which can be downloaded from:

* [MikTex](https://miktex.org/download)

Select Download:

<img src='./images/img_049.png' alt='img_049' width='450'/>

When the Download is complete:

<img src='./images/img_050.png' alt='img_050' width='450'/>

Launch the GUI installer:

<img src='./images/img_051.png' alt='img_051' width='450'/>

Accept the License Agreement and select Next:

<img src='./images/img_052.png' alt='img_052' width='450'/>

MikTeX should be installed for a single user. Select the default Install MikTeX Only for Me and select Next:

<img src='./images/img_053.png' alt='img_053' width='450'/>

MikTeX is installed within a subfolder of Local Appdata:

<img src='./images/img_054.png' alt='img_054' width='450'/>

This is a special location and has the environmental variable:

```powershell
%LOCALAPPDATA%
```

<img src='./images/img_055.png' alt='img_055' width='450'/>

<img src='./images/img_056.png' alt='img_056' width='450'/>

Use the default install location and select Next:

<img src='./images/img_057.png' alt='img_057' width='450'/>

Select the default settings and select Next:

<img src='./images/img_058.png' alt='img_058' width='450'/>

Select Start:

<img src='./images/img_059.png' alt='img_059' width='450'/>

Select Next:

<img src='./images/img_060.png' alt='img_060' width='450'/>

Uncheck Check for Updates Now and select Next:

<img src='./images/img_061.png' alt='img_061' width='450'/>

Select Close:

<img src='./images/img_062.png' alt='img_062' width='450'/>

If the Start button is right clicked and System selected:

<img src='./images/img_063.png' alt='img_063' width='200'/>

The Advanced System Settings:

<img src='./images/img_064.png' alt='img_064' width='450'/>

And Environmental Variables can be examined:

<img src='./images/img_065.png' alt='img_065' width='450'/>

The Windows Path contains the locations the Windows Terminal looks for applications. Select Edit to view it in more detail:

<img src='./images/img_066.png' alt='img_066' width='450'/>

Notice the entry for MikTeX can be seen:

<img src='./images/img_067.png' alt='img_067' width='450'/>

The Windows Terminal will examine the entries in the path when launched. Any open Terminals will have to be closed and reopened.

This can be opened in the file explorer:

```powershell
%LOCALAPPDATA%\Programs\MikTeX\miktex\bin\x64\
```

<img src='./images/img_068.png' alt='img_068' width='450'/>

In this folder are a number of applications such as the ```miktex-console```:

<img src='./images/img_069.png' alt='img_069' width='450'/>

This can be launched in the Windows Terminal by using:

```powershell
miktex-console
```

<img src='./images/img_070.png' alt='img_070' width='450'/>

<img src='./images/img_071.png' alt='img_071' width='450'/>

Go to the Updates tab. Select Check for Updates:

<img src='./images/img_072.png' alt='img_072' width='450'/>

Select Update Now:

<img src='./images/img_073.png' alt='img_073' width='450'/>

Select OK when prompted to close the MikTeX Console:

<img src='./images/img_074.png' alt='img_074' width='250'/>

Launch the MikTex Console again:

```powershell
miktex-console
```

<img src='./images/img_075.png' alt='img_075' width='450'/>

Go to the Packages tab and sort by Installed On:

<img src='./images/img_076.png' alt='img_076' width='450'/>

Highlight the first package without an Installed on date and hold down ```⇧```:

<img src='./images/img_077.png' alt='img_077' width='450'/>

Then scroll down to the bottom which will highlight all uninstalled packages. Select + to install these:

<img src='./images/img_078.png' alt='img_078' width='450'/>

Select OK:

<img src='./images/img_079.png' alt='img_079' width='250'/>

These may take a while to download. Close the MikTeX console when it has finished:

<img src='./images/img_080.png' alt='img_080' width='450'/>

## Initialising

When Anaconda/Miniconda are installed. The option to add the base Python environment to the Windows Environmental Variables Path is not recommended, as this locks the Windows Terminal to a single Python Environment:

<img src='./images/img_081.png' alt='img_081' width='450'/>

The Windows Terminal can be initialised, which makes it behave equivalently to the Anaconda PowerShell Prompt, allowing use of multiple Python environments. Right click the Start button and select Terminal **(Admin)**:

<img src='./images/img_082.png' alt='img_082' width='200'/>

Input the following commands:

```powershell
Set-ExecutionPolicy RemoteSigned
```

For Anaconda input:

```powershell
anaconda3\Scripts\conda init powershell
```

For Miniconda input:

```powershell
miniconda3\Scripts\conda init powershell
```

<img src='./images/img_083.png' alt='img_083' width='450'/>

Details about the file changes will be listed and there is an instruction to close any open shells:

<img src='./images/img_084.png' alt='img_084' width='450'/>

Now when the Windows Terminal is launched:

<img src='./images/img_085.png' alt='img_085' width='200'/>

It will display the prefix (base) and behave identically to the Anaconda PowerShell Prompt:

<img src='./images/img_086.png' alt='img_086' width='450'/>

The command

```powershell
python
```

now works as expected:

<img src='./images/img_087.png' alt='img_087' width='450'/>

## Anaconda Navigator

Returning to:

```powershell
%USERPROFILE%\anaconda3\Scripts
```

<img src='./images/img_088.png' alt='img_088' width='450'/>

On Anacodna, the Anaconda Navigator is preinstalled, this is not preinstalled in Miniconda. The Anaconda Navigator is the ```anaconda-navigator``` application:

<img src='./images/img_089.png' alt='img_089' width='450'/>

And can be launched from the Terminal using:

```powershell
anaconda-navigator
```

<img src='./images/img_090.png' alt='img_090' width='450'/>

This will display a splash logo and the Terminal will remain busy while the main event loop for the QTMainWindow is running:

<img src='./images/img_091.png' alt='img_091' width='450'/>

The main window looks as follows and has a number of tiles which can be used to launch commonly used Python Shells or Integrated Development Environments (IDEs):

<img src='./images/img_092.png' alt='img_092' width='450'/>

The applications preferences can be changed by going to File → Preferences:

<img src='./images/img_093.png' alt='img_093' width='450'/>

Unfortunately the Enable High DPI Scaling setting often does not work and the preferences box is stretched off the screen making it impossible to click the close button, cancel button or apply button:

<img src='./images/img_094.png' alt='img_094' width='450'/>

The Configure Navigator button is a means to configure the Anaconda Navigator settings programmatically:

<img src='./images/img_095.png' alt='img_095' width='450'/>

The Configure Conda button is a means to configure the conda package manager recall parameters programmatically. It is recommended to leave these settings at the defaults which essentially means the default channel used is the ```anaconda``` channel and means the right channel is used when working with the base Python environment:

<img src='./images/img_096.png' alt='img_096' width='450'/>

As the Preferences window cannot be used when it displays offscreen, the two files above can be modified using notepad. For the Anaconda Navigator, open up file explorer and go to:

```powershell
%APPDATA%
```

<img src='./images/img_097.png' alt='img_097' width='450'/>

Select the ```.anaconda``` folder:

<img src='./images/img_098.png' alt='img_098' width='450'/>

Select the ```navigator``` folder:

<img src='./images/img_099.png' alt='img_099' width='450'/>

Open the ```anaconda-navigator``` file in notepad:

<img src='./images/img_100.png' alt='img_100' width='450'/>

Change ```enable_high_dpi_scaling``` to ```False```. Then close the Anaconda Navigator and relaunch it:

<img src='./images/img_101.png' alt='img_101' width='450'/>

For the conda package manager, go to:

```powershell
%USERPROFILE%
```

<img src='./images/img_102.png' alt='img_102' width='450'/>

Open the ```.condarc``` (conda recall parameters) file in notepad:

<img src='./images/img_103.png' alt='img_103' width='450'/>

The settings should be at the defaults:

<img src='./images/img_104.png' alt='img_104' width='450'/>

The Anaconda Navigator can be quit:

<img src='./images/img_105.png' alt='img_105' width='450'/>

When it is closed, a new prompt should display. If the process is still hanging press ```Ctrl``` + ```c``` to close the currently running operation:

<img src='./images/img_106.png' alt='img_106' width='450'/>

## IPython

Returning to:

```powershell
%USERPROFILE%\anaconda3\Scripts
```

<img src='./images/img_107.png' alt='img_107' width='450'/>

In Anaconda, the Interactive Python shell is preinstalled. This is not installed in Miniconda. The Interactive Python shell can be found as the ```ipython``` application which also has the alias ```ipython3```. In the past when Python Version 2 and 3 were installed, the 3 was used to distinguish between the versions. Now that Python 2 has reached end of life and is not installed, the alias without the 3 is typically used:

<img src='./images/img_108.png' alt='img_108' width='450'/>

To launch ```ipython``` open up the Terminal and input:

```powershell
ipython
```

Notice that it looks very similar to the Python shell however there are some key differences. The prompt is now a numeric integer. In addition when ```↹``` is pressed after a prefix, a list of identifiers beginning with the prefix displays:

<img src='./images/img_109.png' alt='img_109' width='450'/>

The identifiers beginning with ```%``` are ipython magics, which are Python implementations of commonly used shell commands. The ipython magics allow use of commonly used shell commands within the ipython shell, without exiting the ipython shell.

A functions docstring can be viewed in the ipython cell output. The other main improvement over the Python shell is that syntax highlighting is applied making it easier to read the Python code:

<img src='./images/img_110.png' alt='img_110' width='450'/>

On Windows there are two shell programming languages, the legacy CMD shell and the modern PowerShell. Although PowerShell is the modern standard, the legacy CMD shell is still widely used and is the basis of IPython magics. The main reason for this is the form of a CMD command versus a PowerShell command (known as a Cmdlet). The prevalence of ```-``` in a PowerShell ```Cmdlet``` results in confusion because the ```-``` is recognised by Python as an operator. 

<img src='./images/img_111.png' alt='img_111' width='450'/>

For example the PowerShell Cmdlet ```Set-Location``` has the CMD command ```cd``` available an alias. This is implemented as an ```IPython``` magic using ```%cd```. 

The IPython magic can also be used as ```cd``` without inclusion of the ```%```, although it is generally recommended to use the ```%``` with an IPython magic as it makes it clear that a Shell command is being used. In CMD, the command ```CD``` is normally uppercase but uppercase and lowercase are accepted. The IPython magic is always lowercase.

The Cmdlet ```%Set-Location``` is not available as an IPython Magic, because ```Set-Location``` without the ```%``` sign would result in Python looking for the variable ```Set``` and the variable ```Location``` and then attempt of the binary datamodel method ```-``` resulting in confusion. Note in PowerShell, the Cmdlet isn't case sensitive but it is better practice to use ```Pascal-Case``` which is consistent to Microsoft's documentation.

Note that when the Windows Terminal is initialised that it will search within the activated Python environments ```Scripts``` folder for applications. In other words the applicaion ```ipython.exe``` is essentially recognised as the Cmdlet ```ipython```.

## Jupyter

Jupyter is preinstalled in the Anaconda base Python environment. For Miniconda, a custom Python environment will need to be created (more details below).

<img src='./images/img_112.png' alt='img_112' width='450'/>

Jupyter is an abbreviation for Julia, Python et R. There are four main applications, available as the Cmdlets:

* ```jupyter-console```
* ```jupyter-qtconsole```
* ```jupyter-notebook```
* ```jupyter-lab```

The application ```jupyter``` is a Cmdlet that accepts a command option (specified after a space) which can be used to launch a Jupyter application:

* ```jupyter console```
* ```jupyter qtconsole```
* ```jupyter notebook```
* ```jupyter lab```

The ```jupyter-kernelspec``` application can be used with the command ```list``` to list kernels. By default only a Python kernel is listed:

<img src='./images/img_113.png' alt='img_113' width='450'/>

On Windows, Julia is not available as a ```conda-forge``` package and must be installed system wide using the Windows package manager winget using the following command:

```powershell
winget install julia -s msstore
```

Unfortunately, winget is not available as a Cmdlet by default on Windows 11, unless the Windows Store is opened, the library selected and Get Updates selected:

<img src='./images/img_114.png' alt='img_114' width='450'/>

The command can then be used to install Julia:

<img src='./images/img_115.png' alt='img_115' width='450'/>

The system Julia can be accessed by inputting:

```powershell
julia
```

<img src='./images/img_116.png' alt='img_116' width='450'/>

For Julia, the Julia package manager Pkg should be used to add the interactive Julia kernel:

```julia
using Pkg
Pkg.add("IJulia")
```

<img src='./images/img_117.png' alt='img_117' width='450'/>

The Julia application can then be exited:

```julia
exit()
```

<img src='./images/img_118.png' alt='img_118' width='450'/>

Now using:

```powershell
jupyter-kernelspec list
```

lists both julia-1.10 and python3 as kernels:

<img src='./images/img_119.png' alt='img_119' width='450'/>

When the application:

```powershell
jupyter-console
```

is launched, it uses the default kernel python3 and behaves essentially identical to ipython:

<img src='./images/img_120.png' alt='img_120' width='450'/>

The ```--kernel``` option can be added to select a different kernel:

```powershell
jupyter-console --kernelspec=julia-1.10
```

<img src='./images/img_121.png' alt='img_121' width='450'/>

Note the ```exit``` command will only exit the ijulia cell, to exit Julia, press ```Ctrl``` + ```d```:

<img src='./images/img_122.png' alt='img_122' width='450'/>

Input ```y``` to proceed:

<img src='./images/img_123.png' alt='img_123' width='450'/>

The conda-forge community channel has wide support for Python and R. Although Python and R each have their own perspective package managers, they should not be used in a conda environment. Instead conda should be used to install any packages.

Packages from the conda-forge community channel should not be installed in the base Python environment as it will make the base Python environment unstable.

Instead a new Python environment (Python subinstallation) should be created:

```powershell
conda create -n jupyter-env -c conda-forge python jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt isort autopep8 ruff black ipympl jupyterlab-variableinspector jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker r-irkernel jupyter-lsp-r r-tidyverse r-ggthemes r-palmerpenguins r-writexl
```

<img src='./images/img_124.png' alt='img_124' width='450'/>

In the above, ```conda``` is the Cmdlet.

```create``` is a command used by the Cmdlet.

Note the specification of the ```-n``` (```--name```), which is a commandline option that expects the environment name in the form of a string. Generally the environment name is in lowercase and uses ```-``` instead of spaces for example ```-n jupyter-env```. Specification of the name instructs the current operation to install packages into the Python environment ```jupyter-env``` opposed to the Python environment ```(base)```.

* Notice use of a lowercase environment name with ```-``` is consistent to ```jupyter-lab``` found in the ```Scripts``` folder.
* Using a space for example ```-n jupyter env``` will result in ```-n``` receiving two strings instead of one and result in confusion, as the commandline option ```-n``` does not know what to do with the second string.
* Double quotations can be used to enclose the string for example ```-n "jupyter env"``` and this will allow for a string with spaces, however this is bad practice as it makes subsequent commands involving the environment unnecessarily cumbersome.
* Mixed case for example ```-n Jupyter-Env``` is also not recommended as it can make subsequent commands involving the environment name more cumbersome.

The create ```command``` is used to create a Python environment and a channel to install packages from and number of initial packages can be specified.

Note the specification of the ```-c``` (```--channel```) which instructs the current operation to preferentially install packages from the community channel and is seen in the channels list below. 

* Each package can have their channel individually specified using ```conda-forge::python conda-forge::jupyterlab``` but this approach is cumbersome when all packages are being installed from the same channel. This approach is normally only used with a handful of additional packages are installed, from another channel.

The conda package manager, now that it has the modern libmamba solver by default will quickly solve the Python environment. It essentially checks the requirements for each library and solves a set of compatible versions:

<img src='./images/img_125.png' alt='img_125' width='450'/>

The environment location is listed, which is ```jupyter-env```:

<img src='./images/img_126.png' alt='img_126' width='450'/>

Details about the packages being downloaded, their version number, build number and channel are listed:

<img src='./images/img_127.png' alt='img_127' width='450'/>

Input ```y``` to proceed with the changes:

<img src='./images/img_128.png' alt='img_128' width='450'/>

The Python environment will be created:

<img src='./images/img_129.png' alt='img_129' width='450'/>

It will need to be activated to be used:

```powershell
conda activate jupyter-env
```

<img src='./images/img_130.png' alt='img_130' width='450'/>

Notice the prefix is now (jupyter-env) which mean the python application and its associated libraries and applications are preferentially used over their counterparts in base. 

Now when:

```powershell
jupyter-kernelspec list
```

is used, the three kernels julia-1.10, python3 and ir show:

<img src='./images/img_131.png' alt='img_131' width='450'/>

The R kernel can be selected using:

```powershell
jupyter-console --kernel=ir
```

<img src='./images/img_132.png' alt='img_132' width='450'/>

The Python environment can be deactivated using:

```powershell
conda deactivate
```

This returns to (base). (base) will remain the default Python environment for any new Terminal instances.

<img src='./images/img_133.png' alt='img_133' width='450'/>

Julia and R can be used in the remaining Jupyter applications. However these tutorials will stick only to Python.

The Jupyter QTConsole is essentially a rewrite of the Windows Terminal using the QT GUI framework.

It can be launched using:

```powershell
jupyter-qtconsole
```

The Terminal remains while the QTMainWindow is open:

<img src='./images/img_134.png' alt='img_134' width='450'/>

Rewriting the Terminal using QT allows the docstring to automatically populate as a popup balloon:

<img src='./images/img_135.png' alt='img_135' width='450'/>

It also allows the nesting of graphics:

<img src='./images/img_136.png' alt='img_136' width='450'/>

The output can be saved to a HTML file which is essentially a read only website. Select File → Save to HTML:

<img src='./images/img_137.png' alt='img_137' width='450'/>

Go to your Documents folder and save the file as ```ipython.html```:

<img src='./images/img_138.png' alt='img_138' width='450'/>

Select Inline:

<img src='./images/img_139.png' alt='img_139' width='250'/>

This HTML file shows as a website and can eb opened in a browser:

<img src='./images/img_140.png' alt='img_140' width='450'/>

<img src='./images/img_141.png' alt='img_141' width='450'/>

The QTConsole can be Quit:

<img src='./images/img_142.png' alt='img_142' width='250'/>

This should close the QTMainWindow and show the next prompt in the Terminal. If not press ```Ctrl``` + ```c``` to cancel the currently running operation.

So far various shells have been examined. Typically an IDE is used for more serious code editing which contains a console, and a means to manipulate a file or notebook.

JupyterLab is a browser based IDE and can be launched using:

```powershell
jupyter-lab
```

<img src='./images/img_143.png' alt='img_143' width='450'/>

The Terminal runs a server and remains busy while the server is running. The visual elements display in the browser:

<img src='./images/img_144.png' alt='img_144' width='450'/>

The JupyterLab IDE has a Files tab to the left which is a browser based implementation of File Explorer.

On Windows there are two Documents folders:

```powershell
%USERPROFILE%\Documents
%USERPROFILE%\OneDrive\Documents
```

The Documents shortcut on Windows File Explorer maps to the first folder if Windows 11 is installed and setup without OneDrive integration.

The Documents shortcut on Windows File Explorer maps to the second folder if Windows 11 is installed and setup with OneDrive integration.

You should navigate to the correct folder corresponding to your setup:

<img src='./images/img_145.png' alt='img_145' width='450'/>

To the right hand side is a launcher (a new tab begins a new launcher). The launcher can be used to create a new file, in this case a new Python 3 Notebook file:

<img src='./images/img_146.png' alt='img_146' width='450'/>

The Files tab can be used to rename a file by right clicking and selecting Rename:

<img src='./images/img_147.png' alt='img_147' width='450'/>

The notebook file consists of ipython cells and markdown cells which can be used to document the code:

<img src='./images/img_148.png' alt='img_148' width='450'/>

To run a cell, use the run button or press the keyboard shortcut key ```⇧``` and ```↵```. To run a cell and insert a blank one below use the keyboard shortcut key ```Alt``` and ```↵```.

To view a list of identifiers input ```↹``` after a prefix:

<img src='./images/img_149.png' alt='img_149' width='450'/>

To view a docstring press ```⇧``` + ```↹```:

<img src='./images/img_150.png' alt='img_150' width='450'/>

JupyterLab has a Variable Inspector, which can be accessed by right clicking the notebook file and selecting Open Variable Inspector:

<img src='./images/img_151.png' alt='img_151' width='450'/>

The tab can be repositioned:

<img src='./images/img_152.png' alt='img_152' width='450'/>

The table of contents can be selected which lists markdown headings and can be used to navigate through the notebook:

<img src='./images/img_153.png' alt='img_153' width='450'/>

A plot can be added to the cell output:

<img src='./images/img_154.png' alt='img_154' width='450'/>

The notebook can be saved, using File → Save Notebook. There is also the option to Save and Export the Notebook in various other outputs such as html and pdf:

<img src='./images/img_155.png' alt='img_155' width='450'/>

When the browser is closed:

<img src='./images/img_156.png' alt='img_156' width='450'/>

The JupyterLab server will remain running in the Terminal. To close it press ```Ctrl``` + ```c```:

<img src='./images/img_157.png' alt='img_157' width='450'/>

A new prompt will display:

<img src='./images/img_158.png' alt='img_158' width='450'/>

The notebook file can be viewed in File Explorer:

<img src='./images/img_159.png' alt='img_159' width='450'/>

When opened in notebook it displays in json format. This is used by the JupyterLab server and the browser to display the visual elements:

<img src='./images/img_160.png' alt='img_160' width='450'/>

Typically the notebook is not opened in Notepad. Instead JupyterLab is launched and the files tab is used to open the notebook. The notebooks kernel should also be restarted in order to continue editing the notebook.

Jupyter Notebook is a simplified version of JupyterLab and will not be covered in this tutorial.

When the Terminal is opened, the ```base``` Python environment is activated: 

<img src='./images/img_200.png' alt='img_200' width='450'/>

The ```jupyter-env``` can be activated using:

```powershell
conda activate jupyter-env
```

<img src='./images/img_201.png' alt='img_201' width='450'/>

If the ```conda``` Cmdlet is used with the command ```install``` or ```update```. It will install/update packages into ```jupyter-env``` instead of ```base```. When using the ```install``` or ```update``` command the channel to install the packages from ```-c conda-forge``` should be specified before specifying the packages to install. For example the package ```python-docx``` can be installed using:

```powershell
conda install -c python-docx
```

<img src='./images/img_202.png' alt='img_202' width='450'/>

The ```conda``` package manager will solve the environment:

<img src='./images/img_203.png' alt='img_203' width='450'/>

The proposed changes will be listed, listing the new packages to be installed, the packages to be updated and the packages to be downgraded (if applicable), input ```y``` in order to proceed:

<img src='./images/img_204.png' alt='img_204' width='450'/>

The proposed changes are now made:

<img src='./images/img_205.png' alt='img_205' width='450'/>

To update all packages in the Python environment ```--all``` can be used instead of a package name:

```powershell
conda update -c conda-forge --all
```

<img src='./images/img_206.png' alt='img_206' width='450'/>

The ```conda``` package manager will solve the environment:

<img src='./images/img_207.png' alt='img_207' width='450'/>

The proposed changes will be listed, listing the new packages to be installed, the packages to be updated and the packages to be downgraded (the downgrade in this case installs the same version number). Input ```y``` in order to proceed:

<img src='./images/img_208.png' alt='img_208' width='450'/>

The proposed changes are now made:

<img src='./images/img_209.png' alt='img_209' width='450'/>

Note it is advised to update the ```conda``` package manager in ```base``` periodically before using the ```conda``` package manager in another Python environment. Recall that ```base``` should always use the channel ```anaconda``` and only ```conda``` should be updated. 

Attempting to use the ```conda-forge``` channel or ```--all``` will attempt to make too many changes to the Anaconda ```base``` Python environment and ultimately make it unstable.

```powershell
conda update -c anaconda conda
```

<img src='./images/img_210.png' alt='img_210' width='450'/>

In this example, the ```conda``` package manager in base is already up to date:

<img src='./images/img_211.png' alt='img_211' width='450'/>

## Spyder

Returning to:

```powershell
%USERPROFILE%\anaconda3\scripts
```

<img src='./images/img_161.png' alt='img_161' width='450'/>

Another application is ```spyder``` which is an abbreviation for the Scientific Python Development Environment:

<img src='./images/img_162.png' alt='img_162' width='450'/>

Spyder is preinstalled in Anaconda. For Miniconda, a separate Python Environment can be created to install the latest version of Spyder using:

```powershell
conda create -n spyder-env -c conda-forge python spyder cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt ruff ghostscript
```

Spyder can be launched from the Terminal using:

```powershell
spyder
```

<img src='./images/img_163.png' alt='img_163' width='450'/>

This IDE has a script editor, that applies syntax highlighting, highlights syntax errors and has a number of tools to help improve code quality:

<img src='./images/img_164.png' alt='img_164' width='450'/>

The Source menu has the Format File or Selection with AutoPEP8 option:

<img src='./images/img_165.png' alt='img_165' width='450'/>

This will move imports to the top and address spacing issues:

<img src='./images/img_166.png' alt='img_166' width='450'/>

The autoformatter can be changed using Tools → Preferences:

<img src='./images/img_167.png' alt='img_167' width='450'/>

Selecting the Code and Linting tab to the left and then switching to black:

<img src='./images/img_168.png' alt='img_168' width='450'/>

Now the Source menu has the Format File or Selection with Black option:

<img src='./images/img_169.png' alt='img_169' width='450'/>

This applies blacks opinionated formatting. At current there are some limitations as black won't organise the imports correctly before applying opinionated formatting and so black does not work unless autopep8 has previously been used:

<img src='./images/img_170.png' alt='img_170' width='450'/>

These options use the ```autopep``` and ```black``` applications found in the:

```powershell
~\anaconda3\Scripts
```

folder. Spyder does not yet support ```isort``` which is used to sort the imports alphabetically in two groupings (by standard module and third-party modules).

Unfortunately, blacks opinionated formatting differs from Pythons default representation and therefore many Python developers dislike black. A new project ruff is a faster implementation of black which can be configured to match Pythons default representation. Ruff is not yet integrated in Anaconda or Spyder.

Spyder has a very powerful Variable Explorer which can be used to visualise variables:

<img src='./images/img_171.png' alt='img_171' width='450'/>

Identifiers corresponding to a prefix will display as a popup, alongside the associated docstring for a function:

<img src='./images/img_172.png' alt='img_172' width='450'/>

The docstring can also be accessed by right clicking an object and selecting Inspect current object:

<img src='./images/img_173.png' alt='img_173' width='450'/>

This will open up the documentation in the Help pane:

<img src='./images/img_174.png' alt='img_174' width='450'/>

Plots are by default displayed as static images in the plots pane:

<img src='./images/img_175.png' alt='img_175' width='450'/>

The plot preferences can be changed by going to Tools → Preferences:

<img src='./images/img_176.png' alt='img_176' width='450'/>

Selecting the IPython Console tab to the left, the Graphics tab to the top right and changing the backend to Qt5 (Automatic is an alias for Qt5):

<img src='./images/img_177.png' alt='img_177' width='450'/>

To apply the new preferences select Consoles → Restart Kernel:

<img src='./images/img_178.png' alt='img_178' width='450'/>

Running the script will now display the plot in its own interactive window:

<img src='./images/img_179.png' alt='img_179' width='450'/>

A comment can be added to a Python script file using ```#```. If ```#%%``` is used, a new cell is created:

<img src='./images/img_180.png' alt='img_180' width='450'/>

The script file can be saved using File → Save As...:

<img src='./images/img_181.png' alt='img_181' width='450'/>

It can then be saved to the Documents folder:

<img src='./images/img_182.png' alt='img_182' width='450'/>

The script file can be viewed in file explorer:

<img src='./images/img_183.png' alt='img_183' width='450'/>

And opened in notepad but notice that no Syntax Highlighting or other visual aids from the IDE are provided:

<img src='./images/img_184.png' alt='img_184' width='450'/>

When Spyder is closed, a new prompt will display. If it doesn't, press ```Ctrl``` + ```c``` to close the currently running operation:

<img src='./images/img_185.png' alt='img_185' width='450'/>

## Environmental File

If the custom ```jupyter-env``` is activated using: 

```powershell
conda activate jupyter-env
```

It can be exported to a yet another markdown language ```yml``` file in the Documents folder using:

```powershell
conda env export > ~\Documents\jupyter-env-file.yml
```

Or

```powershell
conda env export > ~\Documents\OneDrive\jupyter-env-file.yml
```

Recalling that there are two Documents folders depending on whether the system has or doesn't have OneDrive integration:

<img src='./images/img_186.png' alt='img_186' width='450'/>

This file can be viewd in File Explorer:

<img src='./images/img_187.png' alt='img_187' width='450'/>

And opened in notepad:

<img src='./images/img_188.png' alt='img_188' width='450'/>

Notice the env name, channels and each package alongside the package version and build number are shown:

<img src='./images/img_189.png' alt='img_189' width='450'/>

In academic settings, an academic may issue a yml file which will reduce the liklihood of students encountering errors due to changes in newer versions of the libraries used.

If the environment is deleted using:

```powershell
conda deactivate
conda env remove -n jupyter-env
```

<img src='./images/img_190.png' alt='img_190' width='450'/>

The ```jupyter-env``` specified in the ```jupyter-env-file.yml``` file can be recreated using:

```powershell
conda env create -f Documents\jupyter-env-file.yml
```

Or:

```powershell
conda env create -f OneDrive\Documents\jupyter-env-file.yml
```

<img src='./images/img_191.png' alt='img_191' width='450'/>

The environment is then recreated:

<img src='./images/img_192.png' alt='img_192' width='450'/>

## Revision

The packages in a conda environment can be listed using the ```list``` command:

```powershell
conda list
```

<img src='./images/img_194.png' alt='img_194' width='450'/>

<img src='./images/img_195.png' alt='img_195' width='450'/>

The ```--revision``` option can be used to list packages for each revision:

```powershell
conda list --revision
```

<img src='./images/img_196.png' alt='img_196' width='450'/>

<img src='./images/img_197.png' alt='img_197' width='450'/>

<img src='./images/img_198.png' alt='img_198' width='450'/>

The ```install``` command can theoerically be used with the ```--revision``` option to revert to a previous revision:

```powershell
conda install -c conda-forge --revision=0
```

<img src='./images/img_199.png' alt='img_199' width='450'/>

However the conda package manager, seems to hang for an extremely long time here for such a simple change. This command option will likely be optimized in a later version of conda. Unfortunately the conda env export command isn't configured to recognize ```--revision``` as an option so it is recommended to export an environment out to a yml files before updating it.

[Return to Python Tutorials](../../../readme.md)
