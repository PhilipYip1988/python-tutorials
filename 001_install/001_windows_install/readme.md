# Installing Python on Windows 11

This tutorial will configure Python 3.11 on a Windows 11 computer using Mambaforge. For Linux/Mac see [Linux/Mac Install](https://github.com/PhilipYip1988/python-tutorials/blob/main/001_install/002_linux_install/readme.md)

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
mamba install python=3.11 spyder=5.4.2
```

If no version is selected, the latest version of Spyder is installed but you may get an older version of Python.

Spyder will be installed with its mandatory dependencies however it is recommended to install it alongside its optional dependencies for complete functionality:

```
mamba install python=3.11 spyder=5.4.2 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
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

To recap Spyder is installed in its own Python environment using:

```
mamba create -n spyder
mamba activate spyder
mamba install python=3.11 spyder cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

Spyder can be launched using:

```
spyder
```

The Spyder IDE looks like the following. To the left hand side is the Script Editor which is similar to Notepad.

To the bottom right there is an IPython console. Below this in the status bar there is details about the Python environment. In this case the Python environment shows as ```conda: spyder (Python 3.11.0)```. The Python environments is called ```spyder``` and Python environments created by conda and mamba are identical, the only difference is in the package manager used to create the environment.

To the top right are 4 tabs Help, Variable Explorer, Plot and Files:

![img_115](./images/img_115.png)

The Spyder Dependencies can be checked using Help from the Menu Bar and then Dependencies:

![img_116](./images/img_116.png)

The mandatory and optional dependencies should be satisfied:

![img_117](./images/img_117.png)

To save the Python Script file select File → Save As or ```Ctrl```, ```⇧```  and ```s```. Select your Documents folder and save the file as ```script2.py```:

![img_118](./images/img_118.png)

The tab in the script editor will be updated to reflect the file name and the location of the file will be shown in the top left. The file location shown in the File tab to the right is the current working directory and will not update until the script is run:

![img_119](./images/img_119.png)

The script can be run using the run key:

![img_120](./images/img_120.png)

Now the Current Working Directory is updated to the location of the Main Script file.

In Python ```#``` is used to denote that a line of code is a comment. In Spyder ```#%%``` can be used to compartmentalise a Python Script File into cells. This can be demonstrated with the example code:

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

The Data Science libraries can be imported using:

```
#%% Importing Data Science Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%% Builtin DataTypes
str_1 = 'Hello'
int_1 = 1
float_1 = 3.14
boot_1 = True
list_1 = ['Hello', 'Hello', 1, 3.14, True]
tuple_1 = ('Hello', 'Hello', 1, 3.14, True)
set_1 = {'Hello', 'Hello', 1, 3.14, True}
dict_1 = {'r': 'red', 'b': 'blue', 'g': 'green'}
#%% Numeric Array
list_x = [1, 2, 3, 4, 5]
x = np.array(list_x)
list_y = [2, 4, 6, 8, 10]
y = np.array(list_y)
#%% Pandas DataFrame
data = pd.DataFrame({'x': x, 'y': y})
```

Builtin datatypes and Data Science datatypes can be seen on the variable explorer:

![img_125](./images/img_125.png)

Variables can be examined in more detail by clicking into them:

![img_126](./images/img_126.png)

The Kernel can be restarted by going to Consoles → Restart Kernel. 

![img_127](./images/img_127.png)

Accept the Warning to proceed:

![img_128](./images/img_128.png)

When the Kernel is Restarted the IPython Console reverteds back to 0, All Variables are erased and the imported libraries are no longer imported.

![img_129](./images/img_129.png)

Another test script can be made to test plotting:

```
#%% Importing Data Science Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
# %% Pandas DataFrame
data = pd.DataFrame({"x": [1, 2, 3, 4, 5], 
                     "y": [2, 4, 6, 8, 10]})
# %% Plot
plt.plot(data.x, data.y)
plt.show()
```

Spyder can be configured to display plots as interactive plots or as static inline plots docked to the plots pane:

![img_130](./images/img_130.png)

To change the plot backend select Tools→Preferences:

![img_131](./images/img_131.png)

Then to the left select IPython Console. To the right select the Graphics Tab and select the desired Backend:

![img_132](./images/img_132.png)

The screenshots in this guide use Spyder with the Spyder (light) appearance. This can be selected from the Appearance Tab:

![img_133](./images/img_133.png)

The Editor settings can be changed to Show Indent Guides and Show Blank Spaces:

![img_134](./images/img_134.png)

The plot now displays as a static image in the plots pane:

![img_135](./images/img_135.png)

Spyder has a Help Pane. The documentation of a function can be viewed by selecting the object of interest and pressing ```Ctrl``` and ```i```. This feature works better for Python and Inbuilt Modules than Scientific Modules. If used on a Scientific Libraries, the docstring of the Library shows instead of the docstring of the object of interest:

![img_136](./images/img_136.png)

A brief docstring will also display as a popup balloon when typed with open parenthesis:

![img_137](./images/img_137.png)

The docstring can also be output to the IPython console using a ```?```. For example:

```
? print
```

![img_138](./images/img_138.png)

![img_139](./images/img_139.png)

Inputting an object name followed by a dot ```.```displays a list of identifiers that can be referenced from the object: 

![img_140](./images/img_140.png)

This feature has in the past worked better for Python and Inbuilt Modules than Scientific Modules which has a slower response time. The latest version made improvements in the response time but unfortunately there is a slight reversion and now one character needs to be typed past the ```.``` in order for any identifiers to display.

![img_141](./images/img_141.png)

The code completion on the IPython console is more responsive but less detailed. In IPython Console press ```↹``` after the ```.``` to view the list of identifiers.

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

Check the latest version of JupyterLab is being installed. If not cancel the operation and assign JupyterLab to the latest version using a modifying the above command. 

There is no Start Menu Shortcut for JupyterLab. To launch JupyterLab, use the Mambaforge Prompt, activate the ```jupyterlab``` Python environment and use:

```
jupyter lab
```

![img_146](./images/img_146.png)

JupyterLab launches in the browser. To the left hand side is a file explorer:

![img_147](./images/img_147.png)

Compatible files can be opened by double clicking them. For example the ```script0.py``` file:

![img_148](./images/img_148.png)

To run a Python Script File, it will require an IPython Console. Right click the file and select Create Console for Editor:

![img_149](./images/img_149.png)

Select Python 3 (ipkernel) and select Select:

![img_150](./images/img_150.png)

The interactive Python Console Kernel will show in its own tab:

![img_151](./images/img_151.png)

Select Run and then Run All Code:

![img_152](./images/img_152.png)

It is also possible here to make a selection within the Python Script File and select Run.

The code will run and the output from the script file will be shown in an IPython console cell:

![img_153](./images/img_153.png)

It is also possible to run a script file using a Terminal. Select Terminal from the launcher:

![img_154](./images/img_154.png)

The Terminal will show in the launchers tab:

![img_155](./images/img_155.png)

This tab can be repositioned:

![img_156](./images/img_156.png)

The code in the script file can be run by changing to the Documents folder and using Python to execute the script file:

```
cd Documents
python script0.py
```

Note ```cd %UserProfile%\Documents``` did not work here as the Terminal is using an odler version of PowerShell to the Mambaforge Prompt.

![img_157](./images/img_157.png)

If instead ```script2.py``` is opened alongside an IPython Console:

![img_158](./images/img_158.png)

When all the code is Run:

![img_159](./images/img_159.png)

The plot displays inline as an IPython cell output:

![img_160](./images/img_160.png)

Although JupyterLab can be used with Python Script Files (```.py``` file extension). It is typically used with Interactive Python Notebook Files (```.ipynb``` file extension). A new Notebook can be created in the Launcher:

![img_161](./images/img_161.png)

It displays on the File Explorer and can be renamed by right clicking it:

![img_162](./images/img_162.png)

And selecting Rename:

![img_163](./images/img_163.png)

The notebook file consists of a series of cells. The default code, is a code cell:

![img_164](./images/img_164.png)

It can be switched to a ```markdown``` cell. Markdown uses a simple syntax for formatting text:

![img_165](./images/img_165.png)

The syntax highlighting changes and running the markdown cell will display the formatted markdown text:

![img_166](./images/img_166.png)

The Code cells behave similar to an IPython Console:

![img_167](./images/img_167.png)

Existing cells can however be edited and then rerun:

![img_168](./images/img_168.png)

JupyterLab has a basic Variable Inspector:

![img_169](./images/img_169.png)

It opens in a new tab, that can be repositioned:

![img_170](./images/img_170.png)

![img_171](./images/img_171.png)

The Variable Inspector is very basic compared to Spyders Variable Explorer. The cell output of an Interactive Notebook is more typically used to view a Variable in more detail.

![img_172](./images/img_172.png)

Matplotlib Plots use the inline backend by default and display as static images in the cell output.

Markdown Headings act as bookmarks:

![img_173](./images/img_173.png)

A list of identifiers can be seen from an object by typing in the objects name followed by a dot ```.``` and tab ```↹```:

![img_174](./images/img_174.png)

A functions docstring can be displayed in a popup balloon by typing in the functions name with open parenthesis and pressing the shift ```⇧``` and tab ```↹``` keys:

![img_175](./images/img_175.png)

The docstring can also be viewed as a cell output. If the cell output is long, the cell can be right clicked and Enabling Scrolling for Outputs can be selected.

![img_176](./images/img_176.png)

Interactive plots can be made using plotly:

![img_177](./images/img_177.png)

The ```ipynb``` files are typically opened by JupyterLab after JupyterLab is launched by the Mambaforge prompt. However it is insightful to view a file in notepad:

![img_178](./images/img_178.png)

The code is nodejs code. The nodejs code wraps around the Python or Markdown code for each cell:

![img_179](./images/img_179.png)

The notebook consists of cells. The cells can be:

* markdown - for markdown syntax: The Markdown display will be shown when the code is run.
* python - for Python code: Python code will be executed when the cell is run.
* raw - The notebook itself is written in nodejs, another programming language used for web development. 

The shortcut key ```esc``` and ```m``` will change the current cell to a markdown cell.

The shortcut key ```esc``` and ```y``` will change the current cell to a code cell.

The shortcut key ```⇧``` and ```↵``` will run a cell.

The shortcut key ```alt``` and ```↵``` will run a cell and insert a blank cell below it.

To get to Keyboard Shortcuts. Select the Settings menu to the top and then select Advanced Settings Editor. To the left select Command Palette and then select keyboard shortcuts.

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
