# Installing Python on Linux/Mac

This tutorial will configure Python 3.11 on a Linux/Mac computer using Mambaforge.

[YouTube Video](https://www.youtube.com/watch?v=BOTfBW3KQh8)

## System Requirements

The PC should match or exceed the following system requirements:

* Modern Distribution e.g. Ubuntu 22.10, Fedora 37 or Ubuntu 22.04 LTS/Mint 21.1
* 6th Generation Intel i5 Processor or Later
* 8 GB RAM or Superior
* 250 GB SSD or Superior
* Chromium or Google Chrome Browser
The performance will be very poor if these system requirements are not satisfied.

Alternatively a Mac with equivalent hardware specifications can be used.

## Uninstall

Before proceeding remove any Python distributions such as Anaconda, Miniconda, Mambaforge or Miniforge. These distributions are typically found as subfolders in the Home ```~``` folder:

![img_001](./images/img_001.png)

They can be deleted by deleting the corresponding folder. Open the Terminal. The prompt should look like the following ```philip@pc~``` where ```philip``` is the user name, ```pc``` is the ```pc``` name and ```~``` is an abbreviation for the Home folder. There should be no ```(base)``` prefix:

![img_002a](./images/img_002a.png)

If there is a ```(base)``` prefix, then select Show Hidden Files:

![img_002](./images/img_002.png)

Open the ```.bashrc``` file in text editor:

![img_003a](./images/img_003a.png)

Search for ```conda```. Remove the conda initialization section and save the ```.bashrc``` file:

![img_003](./images/img_003.png)

Close any Terminal windows and relauch the Terminal. The ```(base)``` prefix should now be removed.

## Mambaforge Install

Mambaforge can be downloaded from the Mambaforge GitHub repository:

[Mambaforge](https://github.com/conda-forge/miniforge#mambaforge)

Make sure to download Mambaforge and not Miniforge (which excludes the Mamba package manager).

Make sure the correct Architecture is selected. For Ubuntu or Fedora use the Linux x86_64 Architecture. For Mac OS X use the x86_64 architecture.

![img_004](./images/img_004.png)

Go to the Downloads folder and right click it selecting Open in Terminal:

![img_005](./images/img_005.png)

Notice the path in the Terminal is now ```~/Downloads```:

![img_006](./images/img_006.png)

Right click the Mambaforge installer and select Rename:

![img_007](./images/img_007.png)

Highlight the file name, including the file extension:

![img_008](./images/img_008.png)

Select Copy:

![img_009](./images/img_009.png)

The Linux Terminals programming language is called bash which is an abbreviation for Bourne Again Shell. It has a command ```bash``` which can be used to launch a shell file ```.sh``` file extension. Input ```bash``` and then a space and then paste in the file name:

![img_010](./images/img_010.png)

Note the copy and paste shortcuts differ in the Linux Terminal. ```Ctrl``` + ```c``` is used to close a currently running command. ```Ctrl``` + ```⇧``` + ```c``` is used to copy and ```Ctrl``` + ```⇧``` + ```v``` is used to paste.

This gives something similar to:

```
bash Mambaforge-Linux-x86_64.sh
```

![img_011](./images/img_011.png)

Hold down ```↵``` to scroll through the license agreement: 

![img_012](./images/img_012.png)

Until ```(END)``` displays, then press ```q``` to quit this prompt:

![img_013](./images/img_013.png)

Input ```yes``` to accept the license agreement

![img_014](./images/img_014.png)

Select the default location:

![img_015](./images/img_015.png)

The next screen will prompt you for Mambaforge initialization. **Do not press ```↵``` here as the default option is no.***

![img_016](./images/img_016.png)

Initialization will modify the hidden ```.bashrc``` file found in the Home directory ```~```:

![img_017](./images/img_017.png)

This file can be opened in the Text Editor:

![img_018](./images/img_018.png)

Without intialization, there is no ```conda``` section:

![img_019](./images/img_019.png)

In the terminal input ```yes```:

![img_020](./images/img_020.png)

The installation is now complete and any Terminal windows should now be closed. Any new Terminals will now reference the modified ```.bashrc``` file:

![img_021](./images/img_021.png)

This modified ```.bashrc``` file now has a ```conda``` paragraph:

![img_022](./images/img_022.png)

When the Terminal is reopened, it will now prefix ```(base)``` to the Linux Prompt, which indicates that the ```(base)``` Python environment is selected. The current working directory by default is Home ```~```@

![img_023](./images/img_023.png)

## Exploring the base Python Environment

The ```base``` Python environment is minimal, containing Python and the ```mamba``` package manager. Its contents can be viewed in Windows Explorer by navigating to:

```
~/mambaforge
```

![img_024](./images/img_024.png)

The ```lib``` subfolder contains the ```(base)``` Python environment:

```
~/mambaforge/lib
```

![img_025](./images/img_025.png)

There is a subfolder displaying the Python version. In this case:

```
~/mambaforge/lib/python3.10
```

![img_026](./images/img_026.png)

This is the folder where all the Standard Python Modules are installed (Modules preinstalled with Python). 

For example the ```datetime``` module which exists as a single Python script file ```datetime.py```:

![img_027](./images/img_027.png)

When the following is input in a Python program:

```
import datetime
```

the contents of this ```datetime.py``` file are imported.

Another example is the ```email``` module which exists as a folder of Python script files.

![img_028](./images/img_028.png)

![img_029](./images/img_029.png)

One of the Python Script Files is called ```__init__.py```. When the following is input in a Python program:

```
import email
```

the contents of this ```__init__.py``` file are imported. The other Python Script files can be accessed from the folder using dot ```.``` notation. For example the Python Script File ```charset.py``` can be accessed using:

```
email.charset
```

There is also a site-packages folder:

```
~/mambaforge/lib/python3.10/site-packages
```

![img_030](./images/img_030.png)

This folder contains all the third-party libraries. The Mambaforge ```base``` Python environment is relatively clean and doesn't contain too many third-party libraries.

![img_031](./images/img_031.png)

The third party libraries are the Python Package Managers ```mamba```, ```conda``` and ```pip```. This guide is focused only on the ```mamba``` package manager but ```mamba``` under the hood builds upon the other two package managers ```pip``` and ```conda```. Because ```pip``` and ```conda``` are required for ```mamba``` to run correctly, these are known as dependencies. 

## List Packages

Notice for each subfolder in site-packages, there is a corresponding folder with the version number. These versions can also be seen by inputting the following command in the Mambaforge Prompt:

```
mamba list
```

![img_032](./images/img_032.png)

The package Name, Version, Build and Channel will be shown:

![img_033](./images/img_033.png)

By default the Channel is ```conda-forge``` which is the community channel.

![img_034](./images/img_034.png)

To clear this, use the command:

```
clear
```

![img_035](./images/img_035.png)

![img_036](./images/img_036.png)

## Updating the base Python Environment

Before making any changes to packages the ```base``` Python environment should be updated as this will make sure the latest version of the ```mamba``` package manager is installed. Use the command:

```
mamba update --all
```

```--all``` instructs the ```mamba``` package manager to update all packages.

![img_037](./images/img_037.png)

When looking for packages the following displays in the Mambaforge Prompt:

![img_038](./images/img_038.png)

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

![img_039](./images/img_039.png)

Alongside details of new packages that will be installed, changed and updated. Usually the packages that change i.e. retain the same version have equivalent versions for different Python versions or different operating systems.

![img_040](./images/img_040.png)

Input ```y``` in order to proceed with the changes:

![img_041](./images/img_041.png)

You will be informed when the transaction is done. This will take you to a new prompt:

![img_042](./images/img_042.png)

The changes will now be reflected in site-packages folder, for example the mamba folder with the old version is removed and replaced with an equivalent folder with the new version number:

![img_043](./images/img_043.png)

```clear``` can be used to clear the screen and ```mamba list``` can be used to view the updated changes:

![img_044](./images/img_044.png)
![img_045](./images/img_045.png)

Mambaforge is now up to date.

## Running Python from the Terminal

So far only the bash Programming Language has been used in the Terminal. This is a scripting language inbuilt into the Linux/Macs Operating System optimised for file operations. Python is also a scripting language.

The programming language can be switched to Python by inputting:

```
python
```

![img_046](./images/img_046.png)

Notice the bash Prompt ```(base) philip@pc:~``` change to the Python Prompt ```>>>```:

![img_047](./images/img_047.png)

A variable can be created using:

```
var = 'Hello World'
```

![img_048](./images/img_048.png)

Once input a new Python Prompt ```>>>``` displays:

![img_049](./images/img_049.png)

Once input a new Python Prompt ```>>>``` displays:

![img_044](./images/img_044.png)

The ```print``` function can be used to print the variable:

```
print(var)
```

![img_050](./images/img_050.png)

To exit the Python Prompt and the Python Program, forgetting all variables. Use the Python function:

```
exit()
```

![img_051](./images/img_051.png)

The Python Prompt disappears now that Python is exited. The bash Prompt now appears:

![img_052](./images/img_052.png)

To exit the Terminal, use the command:

```
exit
```

![img_053](./images/img_053.png)

Both bash and Python are scripting languages. They have some similarities in some of their commands but the syntax may differ slightly. This was demonstrated using the ```exit``` function in Python and the ```exit``` command in bash.

## Running Interactive Python from the Terminal

Interactive Python can also be ran in the Terminal by using:

```
ipython
```

![img_054](./images/img_054.png)

If bash does not recognise the command ```ipython``` it is because ```ipython``` is not installed:

![img_055](./images/img_055.png)

It can be installed using:

```
mamba install ipython
```

![img_056](./images/img_056.png)

Once again details about the packages being downloaded and installed will display. Input ```y``` in order to download the additional packages:

![img_057](./images/img_057.png)

A new prompt will display after the packages are downloaded. To clear the screen use ```clear```:

Now input:

```
ipython
```

![img_058](./images/img_058.png)

Notice that the prompt changes to a numeric prompt:

![img_059](./images/img_059.png)

The Python code is color coded. This makes it easier to identify what text is part of the string and what text corresponds to the object name when inputting:

```
var = 'Hello World'
```

![img_060](./images/img_060.png)

If the string object ```var.``` is input followed by a tab ```↹```, a list of identifiers available from the object display:

![img_061](./images/img_061.png)

A docstring of a function, for example the ```print``` function can be displayed using:

```
? print
```

![img_062](./images/img_062.png)

The ```print``` function can be used to print the variable ```var``` as before:

```
print(var)
```

![img_063](./images/img_063.png)

To exit the IPython Prompt and the Python Program, forgetting all variables. Use the Python function:

![img_064](./images/img_064.png)

The bash Prompt reappears:

![img_065](./images/img_065.png)

## Running a Python Script File from the Terminal

A Python Script File is essentially a text file with a ```.py``` file extension opposed to a ```.txt``` file extension. A new Python Script File can be created in the Text Editor:

![img_066](./images/img_066.png)

It should be saved as ```script0.py``` in Documents noting the file extension:

![img_067](./images/img_067.png)

With the correct File Extension, the text editor will apply syntax highlighting to the Python code. Input:

```
var = 'Hello World'
print(var)
```

![img_068](./images/img_068.png)

The file can now be seen in the Documents folder:

![img_069](./images/img_069.png)

The Text Editor, Files and Terminal are all core components of a Python Integrated Development Environment:

![img_070](./images/img_070.png)

To change directory in the Terminal use the command ```cd```. To change to Documents use:

```
cd ~/Documents
```

where ```~``` is the Home folder:

![img_071](./images/img_071.png)

Notice the Documents directory on the next prompt:

![img_072](./images/img_072.png)

To execute the Python Script file input:

```
python script0.py
```

![img_073](./images/img_073.png)

## Editting a Python Script File from the Terminal

The Linux Terminal comes with an inbuilt text editor called ```nano```. To open a script file in ```nano``` use:

```
nano script0.py
```

It is also possible to open ```nano``` with a new file by not specifying any file.

![img_074](./images/img_074.png)

The arrow keys can be used to navigate through the text file and Python code can be added:

![img_075](./images/img_075.png)

An exclamation amrk will be added to the end of the string. The shortcut keys display at the bottom. The ```^``` represents the ```Ctrl``` key. Input ```Ctrl``` + ```x``` to exit nano:

![img_076](./images/img_076.png)

Input ```y``` to save the file:

![img_077](./images/img_077.png)

The file name will be displayed at the bottom. In this case the existing file will be updated so ```↵``` will be pressed, exiting nano. In other cases, a new file name can be created before pressing ```↵```: 

![img_078](./images/img_078.png)

The next bash prompt will display:

![img_079](./images/img_079.png)

Python can be run on this updated file:

![img_081](./images/img_081.png)

## Integrated Development Learning Environment (IDLE)

The Integrated Development Learner Environment (IDLE) can be launched from the Mambaforge Prompt using:

```
idle3
```

In Windows the command ```idle``` is used. In Linux ```3``` still needs to be used, this is a hangover from a time when it was common to have Python2 and Python3 installed. 

![img_082](./images/img_082.png)

Notice that the Terminal is running IDLE. While IDLE is running, the Linux Terminal is busy and cannot be used to input any other commands. An infinite loop is running to keep IDLE open:

![img_083](./images/img_083.png)
![img_084](./images/img_084.png)

The text is sometimes too small in IDLE, select Options → Configure IDLE:

![img_085](./images/img_085.png)

Then change the size and select Apply until the sample is easy to read:

![img_086](./images/img_086.png)

Commands can be input in IDLE similar to the Python console. For example:

```
var = 'Hello World'
```

![img_087](./images/img_087.png)

If the string object is input followed by a dot ```.``` and tab ```↹```, a list of identifiers which can be called from the object displays:

![img_088](./images/img_088.png)

If a function such as ```print``` is input with open parenthesis, the functions docstring, detailing the input arguments will display:

![img_089](./images/img_089.png)

Closing down IDLE using the x in the top right corner or the function ```exit()``` will release the Terminal.

![img_090](./images/img_090.png)

If IDLE or any other process running in the Mambaforge Prompt is hung up. The keyboard shortcut ```Ctrl``` + ```c``` can be used to close any command.

Copy uses the shortcut ```Ctrl``` + ```⇧``` + ```c``` and paste uses the shortcut
```Ctrl``` + ```⇧``` + ```v```.

The IDLE shell can also be used to create a Python Script File and Run a Python Script File. Select File → New File:

![img_091](./images/img_091.png)

Then press ```Ctrl``` + ```s``` and save the script file in Documents with a ```.py``` extension. In this case the file will be called ```script1.py```:

![img_092](./images/img_092.png)

![img_093](./images/img_093.png)

Input the following code and save:

```
var = 'Hello World'
print(var)
```

Select Run → Run Module:

![img_094](./images/img_094.png)

The Code will be executed in the IDLE Shell:

![img_095](./images/img_095.png)

## Python Environments

As you become more proficient in Python, you will need the features and capabilities of other Python IDEs and need to use a number of third-party libraries. It is generally a good practice to install these IDEs in seperate Python environments. A Python Environment is essentially a subinstallation of Python. A Python Environment will be created for the Spyder IDE. This IDE is written in Python and Python Libraries and therefore has a large number of dependencies.

In the mambaforge folder, there is a subfolder called ```envs```:

```
~/mambaforge/envs
```

![img_096](./images/img_096.png)

This folder is empty because no Python Environments have been created:

![img_097](./images/img_097.png)

To create a Python Environment open up the Terminal and use the command:

```
mamba create -n spyder
```

![img_098](./images/img_098.png)

Details about the ```spyder``` Python Environment will display:

![img_099](./images/img_099.png)

![img_100](./images/img_100.png)

![img_101](./images/img_101.png)


To change packages in the ```spyder``` Python environment activate the Python environment using the command:

```
mamba activate spyder
```

![img_102](./images/img_102.png)

The prompt now begins with ```(spyder)``` opposed to ```(base)``` reflecting the change in the selected Python environment:

![img_103](./images/img_103.png)

The ```mamba``` package manager may be used to search for a package on the conda-forge channel such as ```spyder``` using:

```
mamba search spyder
```

![img_104](./images/img_104.png)

Each version on the conda-forge channel will be displayed from earliest to newest:

![img_105](./images/img_105.png)

As multiple versions of Python are supported by Spyder, there are multiple listings for Spyder. These can be installed using the install command. A specific version can be specified using the assignment operator. 

```
mamba install python=3.11 spyder=5.4.1
```

If no version is selected, the latest version of Spyder is installed but you may get an older version of Python.

Spyder will be installed with its mandatory dependencies however it is recommended to install it alongside its optional dependencies for complete functionality:

```
mamba install python=3.11 spyder=5.4.1 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

Installing ```seaborn``` will give the other scientific libraries such as ```numpy```, ```pandas```, ```matplotlib``` and ```scipy```. The ```openpyxl```, ```xlrd```, ```xlsxwriter```, ```lxml``` and ```sqlalchemy``` are used by ```pandas``` to read and write to common file formats:

![img_106](./images/img_106.png)

A large number of libraries will be installed, select ```y``` in order to proceed:

![img_107](./images/img_107.png)

Spyder will now be installed:

![img_108](./images/img_108.png)

Spyder can be launched from the Terminal using the command:

```
spyder
```

![img_110](./images/img_110.png)

![img_109](./images/img_109.png)

If the Terminal is closed and reopened, the default ```(base)``` Python environment will be selected. If ```spyder``` is input. The error message ```'spyder' is not recognized``` will display because the ```(base)``` environment has no Spyder installation:

![img_111](./images/img_111.png)

The Spyder Python Environment must be activated and then Spyder can be launched:

```
mamba activate spyder
spyder
```

![img_112](./images/img_112.png)

The Spyder environment folder now has files in it:

```
~/mambaforge/envs/spyder
```

It has its own lib folder:

```
~/mambaforge/envs/spyder/lib
```

![img_113](./images/img_113.png)

This contains its Python subinstallation:

```
~/mambaforge/envs/spyder/lib/python3.11
```

![img_114](./images/img_114.png)

This folder contains the Python standard modules for this version of Python. Recall:

```
import datetime
```

references this file:

```
~/mambaforge/envs/spyder/lib/python3.11/datetime.py
```

![img_115](./images/img_115.png)

There is an ```email``` subfolder. 

![img_116](./images/img_116.png)

![img_117](./images/img_117.png)

Recall:

```
import email
```

references this file:

```
~/mambaforge/envs/spyder/lib/python3.11/email/__init__.py
```

And

```
import email.charset
```

references this file:

```
~/mambaforge/envs/spyder/lib/python3.11/email/charset.py
```

The commonly used third-party data science libraries are found in the ```site-packages``` folder:

```
~/mambaforge/envs/spyder/lib/python3.11/site-packages
```

![img_118](./images/img_118.png)

For example there is a ```numpy``` and ```matplotlib``` subfolder:

![img_119](./images/img_119.png)

Looking at the numpy folder:

```
import numpy as np
```

references this file:

```
~/mambaforge/envs/spyder/lib/python3.11/site-packages/numpy/__init__.py
```

![img_121](./images/img_121.png)

```numpy``` is a large library and has additional subfolders such as linalg:```numpy``` is a large library and has additional subfolders such as linalg:

![img_122](./images/img_122.png)

This ```linalg``` folder has its own Python Modules including a ```__init__.py```

```
np.linalg
```

references this file:

```
~/mambaforge/envs/spyder/lib/python3.11/site-packages/numpy/linalg/__init__.py
```

![img_123](./images/img_123.png)

For ```matplotlib``` there is a ```__init__.py``` which would be referenced if ```import matplotlib``` was input:

However it is more common to use the ```pyplot.py``` module opposed to the entire library:

```
import matplotlib.pyplot
```

references this file:

```
~/mambaforge/envs/spyder/lib/python3.11/site-packages/matplotlib/pyplot.py
```

![img_124](./images/img_124.png)

Once Python environments have been created. They can be listed using:

```
mamba env list
```

![img_126](./images/img_126.png)

The environments will be listed and the currently selected one will be indicated with a ```*```. 

For completeness, another Python Environment called ```deleteme``` will be created:

```
mamba create -n deleteme
mamba env list
```

To remove this Python environment the following command can be used:

```
mamba env remove -n deleteme
```

This Python environment is now removed:

![img_127](./images/img_127.png)

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

![img_128a](./images/img_128a.png)

The Spyder Dependencies can be checked using Help from the Menu Bar and then Dependencies:

![img_128](./images/img_128.png)

The mandatory and optional dependencies should be satisfied:

![img_129](./images/img_129.png)

To save the Python Script file select File → Save As or ```Ctrl```, ```⇧```  and ```s```. Select your Documents folder and save the file as ```script2.py```:

![img_130](./images/img_130.png)

![img_131](./images/img_131.png)

The tab in the script editor will be updated to reflect the file name and the location of the file will be shown in the top left. The file location shown in the File tab to the right is the current working directory and will not update until the script is run:

![img_132](./images/img_132.png)

The script can be run using the run key:

![img_133](./images/img_133.png)

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

The top cell can be highlighted and the Run Current Cell button can be selected. Its output shows in the IPython Console and this cell is still selected:

![img_134](./images/img_134.png)

The top cell can be highlighted and the Run Current Cell button can be selected. Its output shows in the IPython Console and this cell is still selected:

![img_135](./images/img_135.png)

Alternately a line or multiple lines may be selected and the Run Selection button can be selected, their outyput show in the IPython Console:

![img_136](./images/img_136.png)

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

![img_137](./images/img_137.png)

Variables can be examined in more detail by clicking into them:

![img_138](./images/img_138.png)

The Kernel can be restarted by going to Consoles → Restart Kernel.

![img_139](./images/img_139.png)

Accept the Warning to proceed:

![img_140](./images/img_140.png)

hen the Kernel is Restarted the IPython Console reverteds back to 0, All Variables are erased and the imported libraries are no longer imported.

![img_141](./images/img_141.png)

Another test script can be made to test plotting:

```
#%% Importing Data Science Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
#%% Pandas DataFrame
data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 
                     'y': [2, 4, 6, 8, 10]})
#%% Plot
plt.plot(data['x'], data['y'])
plt.show()
```

Spyder can be configured to display plots as interactive plots or as static inline plots docked to the plots pane:

![img_142](./images/img_142.png)

To change the plot backend select Tools→Preferences:

![img_143](./images/img_143.png)

Then to the left select IPython Console. To the right select the Graphics Tab and select the desired Backend:

![img_144](./images/img_144.png)

The screenshots in this guide use Spyder with the Spyder (light) appearance. This can be selected from the Appearance Tab:

![img_145](./images/img_145.png)

The Editor settings can be changed to Show Indent Guides and Show Blank Spaces:

![img_146](./images/img_146.png)

The plot now displays as a static image in the plots pane:

![img_147](./images/img_147.png)

Spyder will display code completions as code is input:

![img_148](./images/img_148.png)

And docstrings when function names are input:

![img_149](./images/img_149.png)


Spyder should also have the ability to inspect an object and display its documentation in the Help Pane. This does not appear to work properly in Linux:

![img_151](./images/img_151.png)

The IPython console behaves slightly differently to the Script Editor. Help can be output in the console using the ```?```. For example:

```
? print
```

![img_152](./images/img_152.png)

Inputting an object name followed by a dot ```.```displays a list of identifiers that can be referenced from the object: 

![img_153](./images/img_153.png)

This feature has in the past worked better for Python and Inbuilt Modules than Scientific Modules which has a slower response time. The latest version made improvements in the response time but unfortunately there is a slight reversion and now one character needs to be typed past the ```.``` in order for any identifiers to display.

![img_154](./images/img_154.png)

The code completion on the IPython console is more responsive but less detailed. In IPython Console press ```↹``` after the ```.``` to view the list of identifiers.

## JupyterLab

Jupyter is a loose acronym meaning Julia, Python, and R. The JupyterLab IDE is a browser based IDE and for Python can be used with the same Scientific Libraries as Spyder. Because it is browser based, its functionality can be extended with interactive Python widgets ```ipywidgets``` and the browser based ```plotly``` plotting library. The browser based functionality is written in nodejs and extensions require ```nodejs``` as a dependency. An optional Variable Inspector is also available.

Another Python environment will be created for JupyterLab.  Open the Terminal and input:

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
mamba install jupyterlab python=3.11 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs ipywidgets plotly jupyterlab-variableinspector
jupyter lab build
```

Check the latest version of JupyterLab is being installed. If not cancel the operation and assign JupyterLab to the latest version using a modifying the above command. 

JupyterLab is browser based and will open in the Linux default Browser. This can be changed to Chromium in Settings:

![img_155](./images/img_155.png)

There is no Start Menu Shortcut for JupyterLab. To launch JupyterLab, use the Terminal, activate the ```jupyterlab``` Python environment and use:

```
jupyter lab
```

![img_156](./images/img_156.png)

JupyterLab launches in the browser. To the left hand side is a file explorer:

![img_157](./images/img_157.png)

Compatible files can be opened by double clicking them. For example the ```script0.py``` file:

![img_158](./images/img_158.png)

To run a Python Script File, it will require an IPython Console. Right click the file and select Create Console for Editor:

![img_159](./images/img_159.png)

Select Python 3 (ipkernel) and select Select:

![img_160](./images/img_160.png)

Select Run and then Run All Code:

![img_161](./images/img_161.png)

It is also possible here to make a selection within the Python Script File and select Run.

The code will run and the output from the script file will be shown in an IPython console cell:

![img_162](./images/img_162.png)

It is also possible to run a script file using a Terminal. Select Terminal from the launcher:

![img_163](./images/img_163.png)

The Terminal will show in the launchers tab:

![img_164](./images/img_164.png)

This tab can be repositioned. The code in the script file can be run by changing to the Documents folder and using Python to execute the script file:

```
cd ~/Documents
python script0.py
```

![img_165](./images/img_165.png)

If instead ```script2.py``` is opened alongside an IPython Console:

![img_166](./images/img_166.png)

![img_167](./images/img_167.png)

The plot displays inline as an IPython cell output:

![img_168](./images/img_168.png)

Although JupyterLab can be used with Python Script Files (```.py``` file extension). It is typically used with Interactive Python Notebook Files (```.ipynb``` file extension). A new Notebook can be created in the Launcher:

![img_169](./images/img_169.png)

It displays on the File Explorer and can be renamed by right clicking it and selecting Rename:

![img_170](./images/img_170.png)

![img_171](./images/img_171.png)

The notebook file consists of a series of cells. The default code, is a code cell:

![img_172](./images/img_172.png)

It can be switched to a ```markdown``` cell. Markdown uses a simple syntax for formatting text:

![img_173](./images/img_173.png)

The syntax highlighting changes and running the markdown cell will display the formatted markdown text:

![img_174](./images/img_174.png)

The Code cells behave similar to an IPython Console however existing cells can however be edited and then rerun

![img_175](./images/img_175.png)

JupyterLab has a basic Variable Inspector:

![img_176](./images/img_176.png)

It opens in a new tab, that can be repositioned:

![img_177](./images/img_177.png)

The Variable Inspector is very basic compared to Spyders Variable Explorer. The cell output of an Interactive Notebook is more typically used to view a Variable in more detail.

![img_178](./images/img_178.png)

Matplotlib Plots use the inline backend by default and display as static images in the cell output.

![img_179](./images/img_179.png)

Markdown Headings act as bookmarks and can be used with the navigation pane:

![img_180](./images/img_180.png)

The Left Side Menu can be minimised for more screen space:

![img_181](./images/img_181.png)

A list of identifiers can be seen from an object by typing in the objects name followed by a dot ```.``` and tab ```↹```:

![img_182](./images/img_182.png)

A functions docstring can be displayed in a popup balloon by typing in the functions name with open parenthesis and pressing the shift ```⇧``` and tab ```↹``` keys:

![img_183](./images/img_183.png)

The docstring can also be viewed as a cell output. If the cell output is long, the cell can be right clicked and Enabling Scrolling for Outputs can be selected.

![img_184](./images/img_184.png)

![img_185](./images/img_185.png)

![img_186](./images/img_186.png)

Interactive plots can be made using plotly:

![img_187](./images/img_187.png)

The ```ipynb``` files are typically opened by JupyterLab after JupyterLab is launched by the Mambaforge prompt. However it is insightful to view a file in Text Editor:

![img_188](./images/img_188.png)

The code is nodejs code. The nodejs code wraps around the Python or Markdown code for each cell.

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
mamba install notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs ipywidgets plotly
```

Visual Studio Code can then be installed from the appropriate software packages which are available of the [Visual Studio Code website](https://code.visualstudio.com/download).

![img_189](./images/img_189.png)

Or from the Software Store:

![img_190](./images/img_190.png)

Once installed. Open VSCode. Select the Extension tab to the left aand select the Python Extension (it is the most popular extension, displayed at the top):

![img_191](./images/img_191.png)

Select Install:

![img_192](./images/img_192.png)

The extension is now installed, alongside other associated Python Extensions:

![img_193](./images/img_193.png)

An optional Markdown Extension can also be installed:

![img_194](./images/img_194.png)

Visual Code encourages setup of a folder for each Python Project. In File Explorer, create a new folder:

![img_195](./images/img_195.png)

This folder will be named ```project0```. It is good practice to not use any spaces or special characters for the folder name, following the same rules as Python object names:

![img_196](./images/img_196.png)

In Visual Studio Code, select the File Tab and then Open Folder. Select ```project0```:

![img_197](./images/img_197.png)

![img_198](./images/img_198.png)

Select Yes to trust the Author:

![img_199](./images/img_199.png)

Select New File:

![img_200](./images/img_200.png)

Open up the ```main.py``` file. In the bottom right on the status bar. Python is shown alongside the Python Interpretter (Python Environment). In this example the wrong Python Environment is selected:

![img_201](./images/img_201.png)

Press ```Ctrl```, ```⇧``` and ```p``` to open the command palette and search for ```Python Select Intepreter```: 

![img_202](./images/img_202.png)

Select the ```vscode``` Python Environment:

![img_203](./images/img_203.png)

![img_204](./images/img_204.png)

The Current Working Directory in VSCode will be the folder that was opened in VSCode. There is a new folder icon which can be used to create subfolders. If subfolders are created with script files. When the script file is run, the Current Working Directory will be the folder opened within Visual Studio Code and not the subfolder. The subfolder can be opened directly within VSCode to set it as the Current Working Directory.

Visual Code Studio uses Microsoft's IntelliSense giving code suggestions as you type:

![img_205](./images/img_205.png)

And the functions docstrings display as popup balloons:

![img_206](./images/img_206.png)

The Python Script file can be launched:

![img_207](./images/img_207.png)

And the plot displays in a seperate Window:

![img_208](./images/img_208.png)

It is possible to run the script file using individual cells in an IPython console:

![img_209](./images/img_209.png)

![img_210](./images/img_210.png)

Plots in this case display inline:

![img_211](./images/img_211.png)

VSCode can also work with Interactive Notebook files:

![img_212](./images/img_212.png)

Once again the cells can be Markdown or Code. VSCode can work with lots of other programming languages, so the cells also have the option to use other programming languages:

![img_213](./images/img_213.png)

The Interactive Python Notebook, also has a Variables button and an Outline Button:

![img_214](./images/img_214.png)

The Variables Button displays a Variable Explorer:

![img_215](./images/img_215.png)

The Variable Explorer opens in a net tab which can be repositioned:

![img_216](./images/img_216.png)

To view the data in the Variable, double click it. This will open the data viewer:

![img_217](./images/img_217.png)

The Outline button gives a table of contents of the markdown headings:

![img_218](./images/img_218.png)

Return to:

[Home](../../../../)