# Installing Python on Windows 11

This tutorial will configure Python 3.11 on a Windows 11 computer using Mambaforge. For Linux/Mac see [Linux/Mac Install](https://github.com/PhilipYip1988/python-tutorials/blob/main/001_install/002_linux_install/readme.md)

## Tutorial Video

[Spyder IDE Setup and Overview](https://www.youtube.com/watch?v=fvQX0wRExCI&ab_channel=PhilipYip)

[JupyterLab IDE Setup and Overview](https://www.youtube.com/watch?v=r7o1eiwOhc4&ab_channel=PhilipYip)

## System Requirements

The PC should match or exceed the following system requirements:

* Windows 11 (22H2) or Windows 10 (22H2) 64 Bit
* 6th Generation Intel i5 Processor or Later
* 8 GB RAM or Superior
* 250 GB SSD or Superior
* Google Chrome or Microsoft Edge Browser

The performance for Python will be very poor if these system requirements are not satisfied.

## Uninstall

Before proceeding uninstall any version of Python or Python distributions you may have previously installed such as Anaconda, Miniconda, Mambaforge or Miniforge. Uninstall any standalone Spyder and any other Python IDEs. This will clean up your computer and prevent any confusion.

If you have two versions of one of these distributions installed and have uninstalled the latest version... the Windows 11 Installed Apps may still list the old version but have problems removing it. In such a scenario you may get better results by accessing the older Programs and Features. This can be accessed by pressing ```⊞``` and ```r``` to open up a run dialog. Input ```appwiz.cpl```.

## Mambaforge Install

Mambaforge can be downloaded from the Mambaforge GitHub repository. Make sure to download Mambaforge and not Miniforge (which excludes the Mamba package manager):

[Mambaforge](https://github.com/conda-forge/miniforge#mambaforge)

Double click to launch the installer:

![img_001](./images/img_001.png)

Select Next:

![img_002](./images/img_002.png)

Select Next:

![img_003](./images/img_003.png)

Select Just Me (recommended):

![img_004](./images/img_004.png)

In the next screen you will be asked where you want to install Mambaforge. Install in the default directory. In Windows this will be in 

```
%UserProfile%\mambaforge
``` 

![img_005](./images/img_005.png)

which in my case maps to 

```
C:\Users\Phili\mambaforge
```

![img_006](./images/img_006.png)

In the next screen, select the default options to register Mambaforge as my default Python and create start menu shortcuts.

![img_007](./images/img_007.png)

**Mambaforge can optionally be added to the Windows Environment Variable Path.** This makes the ```base``` Python environment accessible via the Windows Terminal. This allows third party applications to accessing Python from the Windows Terminal. Such a use case is normally more advanced, for example a C++ IDE that is configured by default to access the Windows Terminal will also be able to invoke a Python Script if Mambaforge is added to the Windows Environmental Variables Path.

Note that in most regular use scenarios the Mambaforge Prompt should be preferentially used to interact with Python instead of the Windows Terminal. The Mambaforge Prompt is similar to the Windows Terminal but is optimised to work with multiple Python environments and not hard coded to the single base environment provided in the Windows Environmental Variables Path like in the case of the Windows Terminal. The Mambaforge Prompt can be used to install packages in Python environments and launch IDEs installed in the Python environments. 

![img_008](./images/img_008.png)

Once the decision to add Mambaforge to the Windows Environmental Path or not is configured. Select Install:

![img_009](./images/img_009.png)

Select Next and Finish:

![img_010](./images/img_010.png)

![img_011](./images/img_011.png)

## The Windows Environment Variable Path

The Windows Environmental Varables Path can be checked by right clicking the Start Button and selecting System:

![img_012](./images/img_012.png)

Then selecting Advanced System Settings:

![img_013](./images/img_013.png)

Then Advanced and Environmental variables:

![img_014](./images/img_014.png)

Select Path and then Edit:

![img_015](./images/img_015.png)

If Mambaforge has been added to the path the following 5 entries will display:

```
%UserProfile%\mambaforge
%UserProfile%\mambaforge\Library\mingw-w64\bin
%UserProfile%\mambaforge\Library\usr\bin
%UserProfile%\mambaforge\Library\bin
%UserProfile%\mambaforge\Scripts
```

![img_016](./images/img_016.png)

Additional entries may be added for other programs and should be unmodfied.

## Launching the Mambaforge Prompt

Launch the Mambaforge Prompt from the Start Menu. Unfortunately when initially installed, it may display as Miniforge, this is a bug which will be addressed when the installation is updated.

![img_017](./images/img_017.png)

In the prompt you will see ```(base)``` which indicates the ```base``` Python environment is selected. You will also see the current working directory and by default the mambaforge prompt opens in ```%UserProfile%```.

![img_018](./images/img_018.png)

## Exploring the base Python Environment

The ```base``` Python environment is minimal, containing Python and the ```mamba``` package manager. Its contents can be viewed in Windows Explorer by navigating to:

```
%UserProfile%\mambaforge
```

Notice there is a python.exe in this folder. This is the default Python executable.

![img_019](./images/img_019.png)

Notice that there is also a ```Lib``` subfolder:

```
%UserProfile%\mambaforge\Lib
```

![img_020](./images/img_020.png)

This is the folder where all the Standard Python Modules are installed (Modules preinstalled with Python). 

For example the ```datetime``` module which exists as a single Python script file ```datetime.py```:

![img_021](./images/img_021.png)

When the following is input in a Python program:

```
import datetime
```

the contents of this ```datetime.py``` file are imported.

Another example is the ```email``` module which exists as a folder of Python script files.

![img_022](./images/img_022.png)

![img_023](./images/img_023.png)

One of the Python Script Files is called ```__init__.py```. When the following is input in a Python program:

```
import email
```

the contents of this ```__init__.py``` file are imported. The other Python Script files can be accessed from the folder using dot ```.``` notation. For example the Python Script File ```charset.py``` can be accessed using:

```
email.charset
```

In this Lib subfolder there is also a site-packages folder:

```
%UserProfile%\mambaforge\lib\site-packages
```

![img_024](./images/img_024.png)

This folder contains all the third-party libraries. The Mambaforge ```base``` Python environment is relatively clean and doesn't contain too many third-party libraries.

![img_025](./images/img_025.png)

The third party libraries are the Python Package Managers ```mamba```, ```conda``` and ```pip```. This guide is focused only on the ```mamba``` package manager but ```mamba``` under the hood builds upon the other two package managers ```pip``` and ```conda```. Because ```pip``` and ```conda``` are required for ```mamba``` to run correctly, these are known as dependencies. There are additional dependencies such as ```requests``` which is used by the package manager to send HTTP requests to the ```conda-forge``` community channel to retrieve the packages. 

## List Packages

Notice for each subfolder in site-packages, there is a corresponding folder with the version number. These versions can also be seen by inputting the following command in the Mambaforge Prompt:

```
mamba list
```

![img_026](./images/img_026.png)

The package Name, Version, Build and Channel will be shown:

![img_027](./images/img_027.png)

By default the Channel is ```conda-forge``` which is the community channel.

![img_028](./images/img_028.png)

To clear this, use the command clear screen:

```
cls
```

![img_029](./images/img_029.png)

![img_030](./images/img_030.png)

## Updating the base Python Environment

Before making any changes to packages the ```base``` Python environment should be updated as this will make sure the latest version of the ```mamba``` package manager is installed. Use the command:

```
mamba update --all
```

```--all``` instructs the ```mamba``` package manager to update all packages.

![img_031](./images/img_031.png)

When looking for packages the following displays in the Mambaforge Prompt:

![img_032](./images/img_032.png)

```Looking for ['brotlipy', 'bzip2', 'ca-certificates', 'certifi', 'cffi', 'charset-normalizer', 'colorama', 'conda', 'conda-package-handling', 'cryptography', 'fmt', 'idna', 'krb5', 'libarchive', 'libcurl', 'libffi', 'libiconv', 'libmamba', 'libmambapy', 'libsolv', 'libsqlite', 'libssh2', 'libxml2', 'libzlib', 'lz4-c', 'lzo', 'mamba', 'menuinst', 'miniforge_console_shortcut', 'openssl', 'pip', 'pybind11-abi', 'pycosat', 'pycparser', 'pyopenssl', 'pysocks', 'python', 'python_abi', 'reproc', 'reproc-cpp', 'requests', 'ruamel_yaml', 'setuptools', 'tk', 'toolz', 'tqdm', 'tzdata', 'ucrt', 'urllib3', 'vc', 'vs2015_runtime', 'wheel', 'win_inet_pton', 'xz', 'yaml', 'yaml-cpp', 'zstd']```

This means that the following:

```
mamba update --all
```

Is an abbrevation for:

```
mamba update brotlipy bzip2 ca-certificates certifi cffi charset-normalizer colorama conda conda-package-handling cryptography fmt idna krb5 libarchive, libcurl libffi libiconv libmamba libmambapy libsolv libsqlite libssh2 libxml2 libzlib lz4-c lzo mamba menuinst miniforge_console_shortcut openssl pip pybind11-abi pycosat pycparser pyopenssl pysocks python python_abi reproc, reproc-cpp requests ruamel_yaml setuptools tk toolz tqdm tzdata ucrt urllib3 vc, vs2015_runtime wheel win_inet_pton xz yaml yaml-cpp zstd
```

Once the latest version of each of the libraries has been found, updating specs displays:

![img_033](./images/img_033.png)

Alongside details of new packages that will be installed, changed and updated. Usually the packages that change i.e. retain the same version have equivalent versions for different Python versions or different operating systems.

![img_034](./images/img_034.png)

Input ```y``` in order to proceed with the changes:

![img_035](./images/img_035.png)

You will be informed when the transaction is done. This will take you to a new prompt:

![img_036](./images/img_036.png)

The changes will now be reflected in site-packages folder, for example the mamba folder with the old version is removed and replaced with an equivalent folder with the new version number:

![img_037](./images/img_037.png)

```cls``` can be used to clear the screen and ```mamba list``` can be used to view the updated changes:

![img_038](./images/img_038.png)

![img_039](./images/img_039.png)

Mambaforge is now up to date and should show correctly in the Start Menu as Mambaforge Prompt:

![img_040](./images/img_040.png)

## Running Python from the Mambaforge Prompt

So far only the PowerShell Programming Language has been used in the Mambaforge Prompt. This is a scripting language inbuilt into the Windows Operating System optimised for file operations. Python is also a scripting language.

The programming language can be switched to Python by inputting:

```
python
```

![img_041](./images/img_041.png)

Notice the PowerShell Prompt ```(base) %UserProfile%``` change to the Python Prompt ```>>>```:

![img_042](./images/img_042.png)

A variable can be created using:

```
var = 'Hello World'
```

![img_043](./images/img_043.png)

Once input a new Python Prompt ```>>>``` displays:

![img_044](./images/img_044.png)

The ```print``` function can be used to print the variable:

```
print(var)
```

![img_045](./images/img_045.png)

To exit the Python Prompt and the Python Program, forgetting all variables. Use the Python function:

```
exit()
```

![img_046](./images/img_046.png)

The Python Prompt disappears now that Python is exited. The PowerShell Prompt now appears:

![img_047](./images/img_047.png)

To exit the PowerShell Prompt and close Mambaforge, use the command:

```
exit
```

![img_048](./images/img_048.png)

Both PowerShell and Python are scripting languages. They have some similarities in some of their commands but the syntax may differ slightly. This was demonstrated using the ```exit``` function in Python and the ```exit``` command in PowerShell.

## Running Interactive Python from the Mambaforge Prompt

Interactive Python can also be ran in the Mambaforge Prompt by using:

```
ipython
```

![img_049](./images/img_049.png)

If PowerShell does not recognise the command ```ipython``` it is because ```ipython``` is not installed:

![img_050](./images/img_050.png)

It can be installed using:

```
mamba install ipython
```

![img_051](./images/img_051.png)

Once again details about the packages being downloaded and installed will display. Input ```y``` in order to download the additional packages:

![img_052](./images/img_052.png)

A new prompt will display after the packages are downloaded. To clear the screen use ```cls```:

![img_053](./images/img_053.png)

Now input:

```
ipython
```

![img_054](./images/img_054.png)

Notice that the prompt changes to a numeric prompt:

![img_055](./images/img_055.png)

The Python code is color coded. This makes it easier to identify what text is part of the string and what text corresponds to the object name when inputting:

```
var = 'Hello World'
```

![img_056](./images/img_056.png)

If the string object ```var.``` is input followed by a tab ```↹```, a list of identifiers available from the object display:

![img_057](./images/img_057.png)

A docstring of a function, for example the ```print``` function can be displayed using:

```
? print
```

![img_058](./images/img_058.png)

The ```print``` function can be used to print the variable ```var``` as before:

```
print(var)
```

![img_059](./images/img_059.png)

To exit the IPython Prompt and the Python Program, forgetting all variables. Use the Python function:

![img_060](./images/img_060.png)

The PowerShell Prompt reappears:

![img_061](./images/img_061.png)

## Running a Python Script File from the Mambaforge Prompt

A Python Script File is essentially a text file with a ```.py``` file extension opposed to a ```.txt``` file extension. A new Python Script File can be created in the File Explorer, in the Documents folder by right clicking and selecting New and then New Text Document:

![img_062](./images/img_062.png)

It should be renamed ```script0.py``` noting the file extension. Accept Yes at the warning to change the file extension:

![img_063](./images/img_063.png)

Ensure the text file is ```script0.py``` and not ```script0.py.txt```. The view options may need to be changed to view hidden file extensions:

![img_064](./images/img_064.png)

Once the file is created, open it with Notepad:

![img_065](./images/img_065.png)

Input:

```
var = 'Hello World'
print(var)
```

and save.

![img_066](./images/img_066.png)

In the Terminal, the directory needs to be changed to the location of the Script File. This can be done with the ```cd``` command followed by the folder. In this case to get to Documents:

```
cd %UserProfile%\Documents
```

![img_067](./images/img_067.png)

The file path displayed alongside the next Prompt should now be in the Documents folder:

![img_068](./images/img_068.png)

To execute the Python Script file input:

```
python script0.py
```

![img_069](./images/img_069.png)

The Notepad Text Editor, Windows File Explorer and Mambaforge Terminal are three components you'll find in almost every Python Integrated Development Environment (IDE):

![img_070](./images/img_070.png)

Swapping Notepad for Notepad++ will give some syntax highlighting as text is input and give some basic coce completion suggestions as you type:

![img_071](./images/img_071.png)

Code Completion options are one of the main reasons for using an IDE.

## Integrated Development Learning Environment (IDLE)

The Integrated Development Learner Environment (IDLE) can be launched from the Mambaforge Prompt using:

```
idle
```

![img_072](./images/img_072.png)

Notice that the Mambaforge Prompt now is running IDLE. While IDLE is running, the Mambaforge Prompt is busy and cannot be used to input any other commands. An infinite loop is running to keep IDLE open:

![img_073](./images/img_073.png)

The Mambaforge Prompt is running the IDLE Shell which displays in a seperate Window. Notice that it has a ```>>>``` Prompt similar to the Python sheel seen before:

![img_074](./images/img_074.png)

The text is sometimes too small in IDLE, select Options → Configure IDLE:

![img_075](./images/img_075.png)

Then change the size and select Apply until the sample is easy to read:

![img_076](./images/img_076.png)

Commands can be input in IDLE similar to the Python console. For example:

```
var = 'Hello World'
```

![img_077](./images/img_077.png)

If the string object is input followed by a dot ```.``` and tab ```↹```, a list of identifiers which can be called from the object displays:

![img_078](./images/img_078.png)

If a function such as ```print``` is input with open parenthesis, the functions docstring, detailing the input arguments will display:

![img_079](./images/img_079.png)

Closing down IDLE using the x in the top right corner or the function ```exit()``` will release the Mambaforge Prompt.

![img_080](./images/img_080.png)

If IDLE or any other process running in the Mambaforge Prompt is hung up. The keyboard shortcut ```Ctrl``` + ```c``` can be used to close any command.

Copy uses the shortcut ```Ctrl``` + ```⇧``` + ```c``` and paste uses the shortcut
```Ctrl``` + ```⇧``` + ```v```.

The IDLE shell can also be used to create a Python Script File and Run a Python Script File. Select File → New File:

![img_081](./images/img_081.png)

Then press ```Ctrl``` + ```s``` and save the script file in Documents with a ```.py``` extension. In this case the file will be called ```script1.py```:

![img_082](./images/img_082.png)

Input the following code and save:

```
var = 'Hello World'
print(var)
```

Select Run → Run Module:

![img_083](./images/img_083.png)

The Code will be executed in the IDLE Shell:

![img_084](./images/img_084.png)

## Python Environments

As you become more proficient in Python, you will need the features and capabilities of other Python IDEs and need to use a number of third-party libraries. It is generally a good practice to install these IDEs in seperate Python environments. A Python Environment is essentially a subinstallation of Python. A Python Environment will be created for the Spyder IDE. This IDE is written in Python and Python Libraries and therefore has a large number of dependencies.

In the mambaforge folder, there is a subfolder called ```envs```:

```
%UserProfile%\mambaforge\envs
```

![img_085](./images/img_085.png)

This folder is empty because no Python Environments have been created:

![img_086](./images/img_086.png)

To create a Python Environment open up the Mambaforge Prompt and use the command:

```
mamba create -n spyder
```

![img_087](./images/img_087.png)

Details about the ```spyder``` Python Environment will display:

![img_088](./images/img_088.png)

The following folder will display:

```
%UserProfile%\mambaforge\envs\spyder
```

![img_089](./images/img_089.png)

![img_090](./images/img_090.png)

To change packages in the ```spyder``` Python environment activate the Python environment using the command:

```
mamba activate spyder
```

![img_091](./images/img_091.png)

The prompt now begins with ```(spyder)``` opposed to ```(base)``` reflecting the change in the selected Python environment:

![img_092](./images/img_092.png)

The ```mamba``` package manager may be used to search for a package on the conda-forge channel such as ```spyder``` using:

```
mamba search spyder
```

![img_093](./images/img_093.png)

Each version on the conda-forge channel will be displayed from earliest to newest:

![img_094](./images/img_094.png)

As multiple versions of Python are supported by Spyder, there are multiple listings for Spyder. These can be installed using the install command. A specific version can be specified using the assignment operator. 

```
mamba install spyder=5.4.2 python=3.11 
```

If no version is selected, the latest version of Spyder is installed but you may get an older version of Python.

Spyder will be installed with its mandatory dependencies however it is recommended to install it alongside its optional dependencies for complete functionality:

```
mamba install spyder=5.4.2 python=3.11 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

Installing ```seaborn``` will give the other scientific libraries such as ```numpy```, ```pandas```, ```matplotlib``` and ```scipy```. The ```openpyxl```, ```xlrd```, ```xlsxwriter```, ```lxml``` and ```sqlalchemy``` are used by ```pandas``` to read and write to common file formats:

![img_095](./images/img_095.png)

A large number of libraries will be installed, select ```y``` in order to proceed:

![img_096](./images/img_096.png)

Spyder will now be installed:

![img_097](./images/img_097.png)

The Mambaforge Prompt will be found in a mambaforge folder alongside a start menu shortcut to Spyder:

![img_098](./images/img_098.png)

Spyder can be launched from this Start Menu shortcut or from the Mambforge Prompt. Using the command:

```
spyder
```

![img_099](./images/img_099.png)

![img_100](./images/img_100.png)

If the Mambaforge Prompt is closed and reopened, the default ```(base)``` Python environment will be selected. If ```spyder``` is input. The error message ```'spyder' is not recognized``` will display because the ```(base)``` environment has no Spyder installation:

![img_101](./images/img_101.png)

The Spyder Python Environment must be activated and then Spyder can be launched:

```
mamba activate spyder
spyder
```

![img_102](./images/img_102.png)

The Spyder environment folder has its own python.exe:

```
%UserProfile%\mambaforge\envs\spyder
```

![img_103](./images/img_103.png)

This folder has its own ```lib``` subfolder:

```
%UserProfile%\mambaforge\envs\spyder\lib
```

![img_104](./images/img_104.png)

This ```lib``` folder contains the Python standard modules for this version of Python. Recall:

```
import datetime
```

references this file:

```
%UserProfile%\mambaforge\envs\spyder\lib\datetime.py
```

![img_105](./images/img_105.png)

There is an ```email``` subfolder. 

![img_106](./images/img_106.png)

Recall:

```
import email
```

references this file:

```
%UserProfile%\mambaforge\envs\spyder\lib\email\__init__.py
```

And

```
import email.charset
```

references this file:

```
%UserProfile%\mambaforge\envs\spyder\lib\email\charset.py
```

![img_107](./images/img_107.png)

The commonly used third-party data science libraries are found in the ```site-packages``` folder:

```
%UserProfile%\mambaforge\envs\spyder\lib\site-packages
```

![img_108](./images/img_108.png)

For example there is a ```numpy``` and ```matplotlib``` subfolder:

![img_109](./images/img_109.png)

Looking at the numpy folder:

```
import numpy as np
```

references this file:

```
%UserProfile%\mambaforge\envs\spyder\lib\site-packages\numpy\__init__.py
```

```numpy``` is a large library and has additional subfolders such as linalg:

![img_101](./images/img_110.png)

This ```linalg``` folder has its own Python Modules including a ```__init__.py```.

![img_111](./images/img_111.png)

```
np.linalg
```

references this file:

```
%UserProfile%\mambaforge\envs\spyder\lib\site-packages\numpy\linalg\__init__.py
```

![img_112](./images/img_112.png)

For ```matplotlib``` there is a ```__init__.py``` which would be referenced if ```import matplotlib``` was input:

![img_113](./images/img_113.png)

However it is more common to use the ```pyplot.py``` module opposed to the entire library:

```
import matplotlib.pyplot
```

references this file:

```
%UserProfile%\mambaforge\envs\spyder\lib\site-packages\matplotlib\pyplot.py
```

![img_114](./images/img_114.png)

Once Python environments have been created. They can be listed using:

```
mamba env list
```

![img_143](./images/img_143.png)

The environments will be listed and the currently selected one will be indicated with a ```*```. 

For completeness, another Python Environment called ```deleteme``` will be created:

```
mamba create -n deleteme
mamba env list
```

![img_144](./images/img_144.png)

To remove this Python environment the following command can be used:

```
mamba env remove -n deleteme
```

This Python environment is now removed:

![img_145](./images/img_145.png)

## mamba, conda and pip Package Managers

**When using the ```mamba``` package manager, you should avoid use of commands which invoke the ```pip``` or ```conda``` package managers, as use of multiple package managers in a single Python environment can result in instability.**

That being said the documentation for the ```conda``` package manager is much more widespread. If you are unsure how to install a package search for ```conda install packagename``` and you'll likely find installation instructions.

The installation commands to install packages will be of the following form:

```
pip install packagename
conda install packagename
conda install -c conda-forge packagename
```

Modify them so they are instead:

```
mamba install packagename
```

The default channel for Mambaforge is the community ```conda-forge``` channel and the vast majority of the latest version of packages are available here.  You should avoid using the commercial ```conda``` channel which typically has older package versions. 

## The Scientific Python Development Environment (SPYDER)

### Install Summary

To recap Spyder is installed in its own Python environment using:

```
mamba create -n spyder
mamba activate spyder
mamba install spyder=5.4.2 python=3.11 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

Spyder can be launched using:

```
spyder
```

### Preferences

The Spyder IDE looks like the following:

![img_213](./images/img_213.png)

The preferences can be changed by selecting Tools → Preferences:

![img_214](./images/img_214.png)

The Appearance can be changed from Spyder Dark to Spyder:

![img_215](./images/img_215.png)

Applying will require a restart of Spyder:

![img_216](./images/img_216.png)

For a High DPI Screen, the High DPI Setting should be enabled. Select Tools → Preferences:

![img_218](./images/img_218.png)

Select Application and Enable Auto High DPI Setting:

![img_219](./images/img_219.png)

Spyder will relaunch with the light theme:

![img_217](./images/img_217.png)

### IPython Console

To the bottom right there is an IPython console. Below this in the status bar there is details about the Python environment. In this case the Python environment shows as ```conda: spyder (Python 3.11.0)```. The Python environments is called ```spyder``` and Python environments created by conda and mamba are identical, the only difference is in the package manager used to create the environment.

### Dependencies 

The Spyder Dependencies can be checked using Help from the Menu Bar and then Dependencies:

![img_116](./images/img_116.png)

The mandatory and optional dependencies should be satisfied:

![img_117](./images/img_117.png)

### Script Editor

To the left is the script editor. By default a temporary script file in the location ```$UserProfile$/.spyder-py``` is open. To the top right, the files tab can be selected, this opens by default in ```$UserProfile$```:

![img_220](./images/img_220.png)

The Script file can be saved using File → Save As:

![img_221](./images/img_221.png)

The Script File should be saved somewhere locally, normally within a subfolder within ```$UserProfile$/Documents```. In this example it will be saved directly within ```$UserProfile$/Documents``` as ```script1.py```:

![img_222](./images/img_222.png)

Notice the name of the tab updates, alongside the file location on the left address bar. To run the script select run:

![img_223](./images/img_223.png)

Select Run with Default Configuration and Run:

![img_224](./images/img_224.png)

### Files Pane

The current working directory changes on the right hand side, to the directory of the running script file:

![img_225](./images/img_225.png)

### Identifiers, Docstrings and Help Pane

A list of builtin identifiers displays as code is input:

![img_226](./images/img_226.png)

If a function is selected, its docstring will display as a popup:

![img_227](./images/img_227.png)

If click anywhere on this tootip for additional help is clicked, the full docstring displays in the Help Pane:

![img_228](./images/img_228.png)

The docstring for the function can also be opened in the Help Pane by right clicking the object and selecting Inspect:

![img_229](./images/img_229.png)

The docstring also displays if the function name is followed by open parenthesis:

![img_230](./images/img_230.png)

All of the identifiers from the ```builtins``` module iare included within every Python script file. However for convenience they can be viewed by importing the ```builtins``` module explicitly using ```import builtins``` and inputting ```builtins.```

![img_231](./images/img_231.png)

This works for other Python standard modules:

![img_232](./images/img_232.png)

The docstring of the ```datetime``` class within the ```datetime``` module does not populate however. It can be inspected in the Help Pane by right clicking it and selecting Inspect:

![img_233](./images/img_233.png)

Alternatively it can be imported into the IPython Console by selecting run the current selection:

![img_234](./images/img_234.png)

The IPython uses slightly different code completion. To view a list of identifiers press tab ```↹``` after the dot ```.```

![img_235](./images/img_235.png)

To view the docstring, type in a function name with open parenthesis:

![img_236](./images/img_236.png)

The docstring can be outputted to the IPython Console by use of the ```?```

![img_260](./images/img_260.png)

A list of identifiers displays if an object name is input followed by a ```.```:

![img_238](./images/img_238.png)

The docstring displays if the name of a function is input:

![img_239](./images/img_239.png)

The code completion has improvements for Scientific Libraries:

![img_237](./images/img_237.png)

![img_240](./images/img_240.png)

![img_241](./images/img_241.png)

![img_243](./images/img_243.png)

### Comments and Cells

In Python ```#``` is used to denote that a line of code is a comment. 

![img_244](./images/img_244.png)

Lines of code can be selected and options from the Edit Menu can be selected such as Comment/Uncomment or Indent or Unindent:

![img_245](./images/img_245.png)

![img_246](./images/img_246.png)

In Spyder ```#%%``` can be used to compartmentalise a Python Script File into cells. This can be demonstrated with the example code:

```
#%% Cell0
print('A')
print('B')
#%% Cell1
print('C')
print('D')
#%% Cell2
print('E')
print('F')
```

![img_121](./images/img_121.png)

The top cell can be highlighted and the Run Current Cell button can be selected. Its output shows in the IPython Console and this cell is still selected:

![img_122](./images/img_122.png)

The top cell can be highlighted and the Run Current Cell and Advance button can be selected. Its output shows in the IPython Console and the next cell is now selected:

![img_123](./images/img_123.png)

Alternately a line or multiple lines may be selected and the Run Selection button can be selected, their outyput show in the IPython Console:

![img_124](./images/img_124.png)

### Variable Explorer

Instances of common builtin classes can be created in the script editor. When the script is run, they will populate in the Variable Explorer:

```
str1 = 'Hello Worldd'
int1 = 1
float1 = 3.14
boot1 = True
list1 = ['Hello', 'Hello', 1, 3.14, True]
tuple1 = ('Hello', 'Hello', 1, 3.14, True)
set1 = {'Hello', 'Hello', 1, 3.14, True}
dict1 = {'r': 'red', 'b': 'blue', 'g': 'green'}
```

![img_247](./images/img_247.png)

A value can be double clicked to interact with the field. In this case, the following string of size 12, can be updated to remove the typo:

![img_248](./images/img_248.png)

It is now size 11:

![img_249](./images/img_249.png)

Collections, open up in another window. The list is mutable and all the fields are coloured. The tuple is immutable and is shown in grey. The set is also immutable and has no index as it is unordered. The dictionary is mutable and all the fields are coloured. It has keys opposed to a numeric index:

![img_250](./images/img_250.png)

![img_251](./images/img_251.png)

![img_252](./images/img_252.png)

![img_253](./images/img_253.png)

The data types of the scientific libraries can also be explored. A numeric array is normally constructed from a list of numeric values or a list of equally sized lists of numeric values. The series is essentially a numeric array with a name (column name). The dataframe is a collection of series, that have a matching index, similar to an Excel spreadsheet. A dataframe can be constructed from a dictionary where the keys are the column names and the values are the corresponding vectors of data:

```
import numpy as np
import pandas as pd

x = np.array(object=[1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

xy = np.array([[1, 2],
               [2, 4],
               [3, 6],
               [4, 8],
               [5, 10]])

xs = pd.Series(data=x, name='x')
ys = pd.Series(data=x, name='y')

data = pd.DataFrame({'x': x,
                     'y': y})
```

![img_254](./images/img_254.png)

Spyder applies a heatmap to the numeric data so the data can easily be visualised:

![img_255](./images/img_255.png)

![img_256](./images/img_256.png)

### Restarting the Kernel

The Kernel can be restarted by going to Consoles → Restart Kernel. 

![img_127](./images/img_127.png)

Accept the Warning to proceed:

![img_128](./images/img_128.png)

When the Kernel is Restarted the IPython Console reverteds back to 0, All Variables are erased and the imported libraries are no longer imported.

![img_129](./images/img_129.png)

### Plotting

Another test script can be made to test plotting:

```
#%% Importing Data Science Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
# %% Pandas DataFrame
data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 
                     'y': [2, 4, 6, 8, 10]})
# %% Plot
plt.plot(data.x, data.y)
plt.show()
```

Spyder can be configured to display plots as static ```inline``` plots (default). These are docked to the plots pane. Alternatively it can be set to output interactive plots which use the ```Qt5``` backed:

![img_257](./images/img_257.png)

To change the plot backend select Tools→Preferences:

![img_131](./images/img_131.png)

Then to the left select IPython Console. To the right select the Graphics Tab and select ```Qt5``` (```auto``` gives the same setting at ```Qt5```):

![img_258](./images/img_258.png)

The plot now displays as an interactive Window:

![img_259](./images/img_259.png)

### Debugger

Spyder has an inbuilt debugger. The simple code will be debugged:

```
x = 1
y = 2

def fun(y):
    x = 3
    x = 4
    return x + y

z = fun(y=3)
print('end')
```

Breakpoints can be added to the line numbers on the left:

![img_266](./images/img_266.png)

Once the breakpoints have been selected, Debug FIle can be selected:

![img_267](./images/img_267.png)

The Run Current Line button can be pressed to run throught the script line by line and debug:

![img_268](./images/img_268.png)

The variable ```x``` is assigned and displays on the variable explorer:

![img_269](./images/img_269.png)

The variable ```y``` is assigned and displays on the variable explorer:

![img_270](./images/img_270.png)

The function ```fun``` is assigned. This does not display on the variable explorer:

![img_271](./images/img_271.png)

However is accessible in the IPython COnsole. This can be seen by looking at the identifiers which begin with f:

![img_272](./images/img_272.png)

Now the debugger is on the function call. Selecting Next will call the function. Alternatively selecting step into will step into the function:

![img_273](./images/img_273.png)

Notice the arrow to the left is now on the first line of the function. The variable explorer displays the variables the function has access to which are the main ```x``` and instead of the main ```y```, the functions local variable ```y``` displays. This was provided as ```3``` when the function was called. This local variable can be thought of as reassignment of ```y``` but only in the functions local namespace, the main ```y``` outside the function is unchanged:

![img_274](./images/img_274.png)

Run current line can be used to run the function as it is called, line by line:

![img_275](./images/img_275.png)

The function has access to the main variable ```x```:

![img_276](./images/img_276.png)

In the function the local function variable ```x``` is created. This reassigns the value of ```x``` but only within the functions local namespace, leaving the main ```x``` outside the function unchanged. This local function variable ```x``` is now ```3```:

![img_277](./images/img_277.png)

This local function variable ```x``` is now ```4```:

![img_278](./images/img_278.png)

The return statement will compute the calculation ```x + y``` using the functions local variables gives ```7```:

![img_279](./images/img_279.png)

This value of ```7``` is then assigned to the main variable ```z``` (the function call was assigned to ```z```). In addition, the arrow is now pointing on the last line which is in the main namespace. The main ```x``` and main ```y``` display as ```1``` and ```2```:

![img_280](./images/img_280.png)

```--Return--``` displays indicating the functions return statement was carried out:

![img_281](./images/img_281.png)

This is the last line before the end breakpoint and all the code between the breakpoints have been executed. The prompt in the IPython console now shows the next number indicateing that the debugging has finished:

![img_282](./images/img_282.png)

## JupyterLab

Jupyter is a loose acronym meaning Julia, Python, and R. The JupyterLab IDE is a browser based IDE and for Python can be used with the same Scientific Libraries as Spyder. Because it is browser based, its functionality can be extended with interactive Python widgets ```ipywidgets``` and the browser based ```plotly``` plotting library. The browser based functionality is written in nodejs and extensions require ```nodejs``` as a dependency. An optional Variable Inspector is also available.

Another Python environment will be created for JupyterLab.  Open the Mambaforge Prompt and input:

```
mamba create -n jupyterlab
mamba activate jupyterlab
```

Search for the latest version of JupyterLab using:

```
mamba search jupyterlab
```

Install JupyterLab using:

```
mamba install jupyterlab python=3.11 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs ipywidgets plotly jupyterlab-variableinspector ipympl pyqt
jupyter lab build
```

Check the latest version of JupyterLab is being installed. If not cancel the operation and assign JupyterLab to the latest version using modifying the above command. 

### Launching JupyterLab

There is no Start Menu Shortcut for JupyterLab. To launch JupyterLab, use the Mambaforge Prompt, activate the ```jupyterlab``` Python environment and use:

```
jupyter lab
```

Note the space.

![img_146](./images/img_146.png)

### File Explorer

The JupyterLab IDE is browser based and has its own file explorer. This will open in the default loaction ```%UserProfile%```. The Documents folder can be selected:

![img_283](./images/img_283.png)

The Documents folder is now open:

![img_284](./images/img_284.png)

The right click context menu can be used to create a new file or folder or to paste a file or folder:

![img_285](./images/img_285.png)

### Launcher

To the right hand side is the Launcher. It can be used to create new files. A text file will be selected:

![img_286](./images/img_286.png)

### Text File

The text file displays in the file explorer. Its file name and extension (```.txt```) also display on the tab heading:

![img_287](./images/img_287.png)

This file will also display in Windows File Explorer:

![img_288](./images/img_288.png)

The File can be right clicked in the File Explorer and Renamed. This also works if the tab header is right clicked:

![img_289](./images/img_289.png)

The file is going to be renamed ```textfile.txt```:

![img_290](./images/img_290.png)

The File Explorer and Tab Heading now show the new file name:

![img_291](./images/img_291.png)

The file name is now updated in the File Explorer:

![img_292](./images/img_292.png)

A text file only allows basic text input and has no formatting:

![img_293](./images/img_293.png)

To make the changes select File→Save: 

![img_294](./images/img_294.png)

This file can also be opened in Windows File Explorer using Notepad:

![img_295](./images/img_295.png)
![img_296](./images/img_296.png)

### Markdown File

A Markdown file (``.md``` file extension) incorporates simple text formatting using Markdown syntax. A new launcher can be opened by selecting the + button on the file explorer. It opens in a new tab. Select Markdown File:

![img_297](./images/img_297.png)

The file can be renamed as seen earlier:

![img_298](./images/img_298.png)

JupyterLab will apply some basic syntax highlighting to markdown:

![img_299](./images/img_299.png)

The formatted file can be viewed by right clicking some blank whitespace in the markdown file and selecting Show Markdown Preview:

![img_300](./images/img_300.png)

This opens the Markdown Preview in a new pane to the right. Notice that the navigation pane shows the headings. This act as itnernal hyperlinks:

![img_301](./images/img_301.png)

**Unfortunately the Left Markdown Pane and Right Markdown Preview Pane are not linked.** So the links will only act on the last pane selected which causes some usability issues. Editting the Markdown Pane also usually results in the Markdown Preview Pane automatically returning to the top which can be quite annoying. 

The navigation pane can be collapsed for more screen space. As seen, the position of the Left Markdown Pane and Right Markdown Preview Pane are not linked:

![img_302](./images/img_302.png)

### Python Script File

A new launcher can be launched and this time a Python Script file (```.py``` file extension) can be selected:

![img_303](./images/img_303.png)

The file can be renamed as seen earlier:

![img_304](./images/img_304.png)

Unfortunately JupytewrLab won't apply any syntax highlighting or display any identifiers by default. Inputting ```p``` and pressing tab ```↹``` for example does nothing:

![img_305](./images/img_305.png)

An IPython Console is required. Right click the file and select Create COnsole for Editor:

![img_306](./images/img_306.png)

Select Python 3 and then select Select:

![img_307](./images/img_307.png)

### Identifiers and Docstrings

Inputting ```p``` and pressing tab ```↹``` now displays identifiers:

![img_308](./images/img_308.png)

To view the docstring of a function as a popup balloon, input the function with open parenthesis and then press shift ```⇧``` and tab ```↹```:

![img_309](./images/img_309.png)

The File Explorer can be minimised for more screen space. The IPython console displays in a new tab at the bottom, this can be repositioned:

![img_310](./images/img_310.png)

A list of inbuilt identifiers can be shown by inputting a character and pressing tab ```↹```. Alternatively builtins can be imported using:

```
import builtins
```

And all the inbuilt identifiers can be viewed by inputting ```builtins.``` and pressing tab ```↹```:

![img_311](./images/img_311.png)

Note the identifiers will not display if there is not enough space. This can happen if the IPython Console window for example is expanded upwards.

![img_312](./images/img_312.png)

Identifier can also be viewed from Python Standard Modules:

![img_313](./images/img_313.png)

It is generally recommended to import the module into the IPython Console. To do this highlight the import lines and select Run → Run Code:

![img_314](./images/img_314.png)

Doing so makes viewing a docstring from one of the modules identifiers easier. Recall to view the docstring of a function as a popup balloon, input the function with open parenthesis and then press shift ```⇧``` and tab ```↹```:

![img_315](./images/img_315.png)

The docstring can also be viewed in an IPython cell by inputting ```?``` followed by the functions object name. This is a reference to the function and should not include parenthesis which are used to call the function:

![img_316](./images/img_316.png)

JupyterLab also has Contextual Help. This can be launched from a new launcher:

![img_317](./images/img_317.png)

Unfortunately it does not work properly for a Python Script File:

![img_318](./images/img_318.png)
![img_319](./images/img_319.png)

Identifiers can also be viewed from instances of builtin classes:

![img_320](./images/img_320.png)

Third party modules should be imported in the IPython Console in order for their identifiers to display:

![img_321](./images/img_321.png)

### Run Code and Run All Code

The Python Script File only has the Run Code and Run All Code options. It does not recognise the ```#%%``` to create cells. A selection can be made and Run Code can be selected:

![img_322](./images/img_322.png)
![img_323](./images/img_323.png)

Alternatively Run All Code can be selected:

![img_324](./images/img_324.png)
![img_325](./images/img_325.png)

### Variable Inspector

JupyterLab has a Variable Inspector. It can be accesed by right clicking some space in the IPython Console and selecting Open Variable Inspector:

![img_326](./images/img_326.png)

This opens in a new tab and can be repositioned.

![img_327](./images/img_327.png)

Unfortunately the Variable Inspector is very basic and Variables are not color-coded or interactive like in Spyders Variable Explorer.

Variables of the data science libraries can also be added:

![img_328](./images/img_328.png)
![img_329](./images/img_329.png)

The IPython console can be used to address some of the shortcomings of the Variable Inspector:

![img_330](./images/img_330.png)

### Restarting the Kernel

The IPython Kernel can be Restarted and Cleared by selecting Kernel → Restart Kernel and Clear Console:

![img_331](./images/img_331.png)

Select Restart:

![img_332](./images/img_332.png)

The IPython Console is cleared:

![img_333](./images/img_333.png)

And all Variables are removed from the Variable Inspector:

![img_334](./images/img_334.png)

### Plotting

Plotting is by default inline. Which means a static image is output within the IPython Console:

![img_335](./images/img_335.png)

JupyterLab has so called magic commands which can be viewed by inputting % followed by a tab ```↹```: 

![img_336](./images/img_336.png)

The one that controls the plot backend is called ```%matplotlib``` and its options can be viewed by inputting the following into a IPython Console cell:

```
%matplotlib --list
```

![img_337](./images/img_337.png)

The default plot backend is ```inline```. This can be switched to ```qt5``` using:

```
%matplotlib qt5
```

![img_338](./images/img_338.png)

### Terminal

The magic commands are only recognised by IPython and not Python and should be commented out:

![img_339](./images/img_339.png)

Navigate to the folder you wish the Terminal to open in. Then select + to open a new launcher and then select Terminal:

![img_340](./images/img_340.png)

This is a PowerShell Terminal. Note the file path is shown in the Terminals Prompt:

![img_341](./images/img_341.png)

Input ```python``` followed by a space and then name of the script file with ```.py``` extension. In this case:

```
python scriptfile.py
```

The script file runs as expected and the plot displays as an interactive window:

![img_342](./images/img_342.png)

Note the Terminal will be running in an infinite loop while the plot is open:

![img_345](./images/img_345.png)

Closing the plot ends the loop and the next prompt displays:

![img_346](./images/img_346.png)

### Interactive Python Notebook

JupyterLab can be used to create an Interactive Python Notebook (```.ipynb``` file extension). Use the + to open a new launcher from the file explorer and then select Notebook:

![img_347](./images/img_347.png)

The file can be renamed as seen earlier:

![img_348](./images/img_348.png)

The Interactive Python Notebook is Cell based. Each Cell can be a Code Cell or a Markdown Cell:

![img_349](./images/img_349.png)

The first cell can be set to Markdown:

![img_350](./images/img_350.png)

A second cell can be added using the + Button. The default Cell Type is Code. Notice the difference in Syntax Highlighting for each cell:

![img_351](./images/img_351.png)

When a markdown cell is selected and the run button is pressed, it will display the equivalent seen on the Markdown Preview. When the Code Cell is selected and the Run button is pressed, it will Run the Code. Each Code cell is part of the Notebooks IPython Console and the number displayed indicated the order the Cells were ran in the IPython Console:

![img_352](./images/img_352.png)

The Navigation Pane can be opened:

![img_353](./images/img_353.png)

Any Markdown Headings will appear as hyperlinks:

![img_354](./images/img_354.png)

If a Markdown Cell that has been run, is double clicked, it will revert from the Markdown Preview to the Markdown Editor and can be modified. It is convenient to use shortcut keys for the Run button. The shortcut key ```⇧``` and ```↵``` will Run the Cell:

![img_355](./images/img_355.png)

Notice the Markdown Preview once again displays. If this is once again double clicked:

![img_356](./images/img_356.png)

The shortcut key ```Alt``` and ```↵``` will run a cell and insert a blank cell below it:

![img_357](./images/img_357.png)

The new Cell is a Code Cell by default:

![img_358](./images/img_358.png)

The shortcut key ```Esc``` and ```m``` will change the current cell to a markdown cell:

![img_359](./images/img_359.png)

The shortcut key ```Esc``` and ```y``` will change the current cell to a code cell:

![img_360](./images/img_360.png)

Supposing the following is input:

```
print('Hello')
print('Hello')
print('Hello')
```

![img_361](./images/img_361.png)

When it is executed the Cell now has a number of 2. This is the second cell in the IPython Console. This differs from the order of the Cells from top to bottom:

![img_362](./images/img_362.png)

If the ```Ctrl``` key is held down, the cursor can be positioned in multiple places using the mouse and left clicking:

![img_363](./images/img_363.png)

This allows multiple line editting and typing in ```World!``` will update the three print statements:

![img_364](./images/img_364.png)

These can be ran again. Note the Cell is now displayed with a 3 as the Cell has been Run again and the 2 has been superseded:

![img_365](./images/img_365.png)

If the Cell Output is right clicked, Enabling Scrolling for Outputs can be selected: 

![img_366](./images/img_366.png)

This view can be particularly useful if wanting to include a long docstring in the notebook:

![img_367](./images/img_367.png)

The up and down arrows can be used to reposition a cell to move the Cell up or down. If the blue bar to the left of the Cell is left clicked and the left click is held down, the Cell can be repositioned by dragging it up or down:

![img_368](./images/img_368.png)

The New Cell Below and New Cell Above Buttons can be used to insert a new Cell below or above respectively:

![img_369](./images/img_369.png)

The Delete Cell Button can be used to Delete a Cell:

![img_370](./images/img_370.png)

There are also the standard Save, Cut, Copy and Paste Buttons to the top left. Beside the Run button is the Stop Button. There is also the button to Reset the Kernel:

![img_371](./images/img_371.png)

Restarting the Kernel will restart the IPython Console and clear all Variables from the Variable Inspector. Select Restart:

![img_372](./images/img_372.png)

The previous Cell Outputs wil remain. Running the top Cell will now display 1:

![img_373](./images/img_373.png)

This can result in confusion as there are now 2 cells with 1. The Restart the Kernl and Run All Cells button can be pressed:

![img_374](./images/img_374.png)

Select Restart:

![img_375](./images/img_375.png)

Now all the Cells are ran from top to bottom:

![img_376](./images/img_376.png)

All the Python Code in the Python Script File can be used in the notebook. Markdown Headings and text can be used to supplement Python comments:

![img_377](./images/img_377.png)

The Cell Output can be sued to view a Variable or display a static inline Plot:

![img_378](./images/img_378.png)

The possible matplotlib magic backends can be listed in a cell output and another cell can be used to configure the backend to qt5:

![img_379](./images/img_379.png)

When the cell is ran with the plot, it now displays in its own iteractive window. The plot is tied to the cell it was Run from.Other Cells can be Run while this plot window is open:

![img_380](./images/img_380.png)

The backend can be changed to ```ipympl```:

![img_381](./images/img_381.png)

Doing so normally requires Restarting the Kernel:

![img_382](./images/img_382.png)

Select Kernel → Restart Kernel and Clear All Outputs:

![img_383](./images/img_383.png)

Select Restart:

![img_384](./images/img_384.png)

Select Run All Cells:

![img_385](./images/img_385.png)

The plot backend is now ```ipympl```:

![img_386](./images/img_386.png)

This gives a nested interactive Python plot in the Cell Output. Unfortunately at this time of writing the interactivity of this nested plot is limited compared to the Qt5 plot backend:

![img_387](./images/img_387.png)

The Interactive Python Notebook is browser based and can used browser based libraries such as plotly express. This can be imported:

![img_388](./images/img_388.png)

Its identifiers can be seen by inputting ```px.``` and pressing tab ```↹```:

![img_389](./images/img_389.png)

The docstring for the scatter function can be viewed in the Cell Output:

![img_390](./images/img_390.png)

And Enabling Scrolling for Outputs can be selected:

![img_391](./images/img_391.png)
![img_392](./images/img_392.png)

If the File Explorer is expanded. A new launcher can be made to Show Contextual Help:

![img_393](./images/img_393.png)

The Contextual Help Pane opens in a new tab and can be used to view the docstring of the currently selected object:

![img_394](./images/img_394.png)

The scatter plot can be used with the dataframe:

![img_395](./images/img_395.png)

The Interactive Python Notebook can be saved with the Save button. It is worthwhile examining the file in file explorer. It can be opened with Notepad:

![img_396](./images/img_396.png)
![img_397](./images/img_397.png)

The file contents is in the Javascript Object Notation (JSON) format which is similar to a Python dictionary:

![img_398](./images/img_398.png)

### Debugging

JupyterLab has a debugger which seems to work bettewr with a Python Script File or all the code in a single Cell within a Python Interactive notebook:

![img_399](./images/img_399.png)

Select the debug button on the IPython Console:

![img_400](./images/img_400.png)

The debugger displays to the right. The breakpoints should be set on the script editor:

![img_401](./images/img_401.png)

In my case, selecting Kernel → Restart Kernel and Debug:

![img_402](./images/img_402.png)

Then Restart:

![img_403](./images/img_403.png)

Did not enable any of the buttons on the Callstack:

![img_404](./images/img_404.png)

Instead selecting Run → Run All Code:

![img_405](./images/img_405.png)

Enabled the buttons on the Callstack:

![img_406](./images/img_406.png)

To the top is the option to view Local or Global Variables:

![img_407](./images/img_407.png)

The next button will be selected to run each line of code one by one:

![img_408](./images/img_408.png)

The variable ```x``` displays as a local variable. The local scope outwith any code block in the main script file is the global scope:

![img_409](./images/img_409.png)

The variable ```y``` is now displayed as a local variable:

![img_410](./images/img_410.png)

The function ```fun``` is displayed as a function variable:

![img_411](./images/img_411.png)

At the function call, there is an option to select next, which will perform the function call or step into, which will step into the function while its being called:

![img_412](./images/img_412.png)

WHen stepped into the functions own local scope is displayed. The local ```y``` is supplied as an input argument:

![img_413](./images/img_413.png)

The global scope has ```x``` and ```y``` which were assigned in the script file, outwith any code blocks:

![img_414](./images/img_414.png)

Selecting next, creates the local variable ```x```:

![img_415](./images/img_415.png)

Selecting next again updates the value of this local variable:

![img_416](./images/img_416.png)

Selecting next will use the return statement with the local variables ```x``` and ```y```:

![img_417](./images/img_417.png)

The result is returned to ```z``` which is shown in the global scope. The local scope is now the global scope as the line indicator is now in the main script file outwith the code block. The global variables ```x``` and ```y``` now display:

![img_418](./images/img_418.png)

Selecting next once again ends the debugging:

![img_419](./images/img_419.png)

## Visual Studio Code

Visual Studio Code is a general purpose Code Editor maintained by Microsoft. Because it is a general purpose editor, a number of steps need to be made to configure it for Python use. A seperate Python environment needs to be created using Mambaforge:


```
mamba create -n vscode
mamba activate vscode
mamba install notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs ipywidgets plotly ipympl pyqt
```

Visual Studio Code can then be installed from the Windows Application (```.exe```) available on the [Visual Studio Code website](https://code.visualstudio.com/download).

Select Windows User Installer x64:

![img_180](./images/img_180.png)

Launch the setup.exe:

![img_181](./images/img_181.png)

Accept the License Agreement and select Next:

![img_182](./images/img_182.png)

Use the default location and select Next:

![img_183](./images/img_183.png)

Use the default location and select Next:

![img_184](./images/img_184.png)

Leave the defaults checked and select Next:

![img_185](./images/img_185.png)

Select Install:

![img_186](./images/img_186.png)

Select Finish:

![img_187](./images/img_187.png)

Open VSCode. Select the Extension tab to the left aand select the Python Extension (it is the most popular extension, displayed at the top):

![img_188](./images/img_188.png)

Select Install:

![img_189](./images/img_189.png)

The extension is now installed, alongside other associated Python Extensions:

![img_190](./images/img_190.png)

An optional Markdown Extension can also be installed:

![img_191](./images/img_191.png)

Visual Code encourages setup of a folder for each Python Project. In File Explorer, create a new folder:

![img_192](./images/img_192.png)

This folder will be named ```project0```. It is good practice to not use any spaces or special characters for the folder name, following the same rules as Python object names:

![img_193](./images/img_193.png)

In Visual Studio Code, select the File Tab and then Open Folder. Select ```project0```:

![img_194](./images/img_194.png)

Select New File:

![img_195](./images/img_195.png)

Name the file ```main.py```:

![img_196](./images/img_196.png)

Open up the ```main.py``` file. In the bottom right on the status bar. Python is shown alongside the Python Interpretter (Python Environment). In this example the wrong Python Environment is selected:

![img_197](./images/img_197.png)

Press ```Ctrl```, ```⇧``` and ```p``` to open the command palette and search for ```Python Select Intepreter```: 

![img_198](./images/img_198.png)

Select the ```vscode``` Python Environment:

![img_199](./images/img_199.png)

The Current Working Directory in VSCode will be the folder that was opened in VSCode. There is a new folder icon which can be used to create subfolders. If subfolders are created with script files. When the script file is run, the Current Working Directory will be the folder opened within Visual Studio Code and not the subfolder. The subfolder can be opened directly within VSCode to set it as the Current Working Directory.

Visual Code Studio uses Microsoft's IntelliSense giving code suggestions as you type:

![img_200](./images/img_200.png)

And the functions docstrings display as popup balloons:

![img_201](./images/img_201.png)

The Python Script file can be launched:

![img_202](./images/img_202.png)

And the plot displays in a seperate Window:

![img_203](./images/img_203.png)

It is possible to run the script file using individual cells in an IPython console:

![img_204](./images/img_204.png)

![img_205](./images/img_205.png)

Plots in this case display inline:

![img_206](./images/img_206.png)

VSCode can also work with Interactive Notebook files:

![img_207](./images/img_207.png)

Once again the cells can be Markdown or Code. VSCode can work with lots of other programming languages, so the cells also have the option to use other programming languages:

![img_208](./images/img_208.png)

The Interactive Python Notebook, also has a Variables button:

![img_209](./images/img_209.png)

This displays a Variable Explorer:

![img_210](./images/img_210.png)

To view the data in the Variable, double click it. This will open the data viewer:

![img_211](./images/img_211.png)

Beside the Variables button is the Outline button. This gives a table of contents of the markdown headings:

![img_212](./images/img_212.png)

[Home Python Tutorials](https://github.com/PhilipYip1988/python-tutorials/blob/main/readme.md)
