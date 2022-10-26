## System Requirements

The PC should match or exceed the following system requirements:

* Ubuntu 22.10, Fedora 37 or Ubuntu 22.04 LTS/Mint 21
* 6th Generation Intel i5 Processor or Later
* 8 GB RAM or Superior
* 250 GB SSD or Superior
* Chromium or Google Chrome Browser

The performance will be very poor if these system requirements are not satisfied.

Alternatively a Mac with equivalent hardware specifications can be used.

## Mambaforge Shell Script Install

Mambaforge can be downloaded from the Miniforge GitHub repository, which lists Mambaforge and Miniforge installers for each Operating System. Both products are almost identical, however only the Mambaforge installer includes the ```mamba``` package manager which will be used in this guide. For Ubuntu, use the installer ending in ```Linux-x86_64.sh```. 

Alternatively for Arch Linux use the ```Linux-aarch64.sh``` and for Mac use use the ```MacOSX-x86_64.sh```. Instructions for installation on these Operating Systems is otherwise more or less identical.

![img_000](./images/img_000.png)

[Mambaforge](https://github.com/conda-forge/miniforge#mambaforge)

The ```Mambaforge-x.xx.x-x-Linux-x86_64.sh``` is a shell script that is run in the terminal. 

![img_001](./images/img_001.png)

Notice when the Terminal is open, there is a prompt of the following form

```
username@pcname:filepath$
```

In this example ```username = philip```, ```pcname = pc``` and the ```filepath = ~```.

![img_002](./images/img_002.png)

```~``` in Linux is a shortcut for the users ```Home``` folder. The installer is in the Downloads subfolder of this directory.

![img_003](./images/img_003.png)

The filepath can be changed using the command ```cd``` an abbreviation for change directory. To change to ```Home/Downloads``` use.

```
cd ~/Downloads
```

Alternatively, right click blank space in the Downloads folder and select Open in Terminal.

![img_004](./images/img_004.png)

![img_005](./images/img_005.png)

The ```.sh``` file is a shell file, it can be executed using the command ```bash```, followed by the name of the shell script, including the ```.sh``` file extension. ```bash``` is an abbreviation for "bourne again shell". Born again was used as a differenciation of modern shell scripts from ancient legacy shell scripts when they were first implemented.

```
bash shellscript.sh
```

To get the name of the shell script quickly, the file can be right clicked and renamed. 

![img_006](./images/img_006.png)

Instead of renaming the file, at the rename dialog. The file name can be copied using the keyboard shortcut ```Ctrl``` + ```c```.

![img_007](./images/img_007.png)

The file name can be pasted into the terminal.

![img_008](./images/img_008.png)

By using the right click context menu.

![img_009](./images/img_009.png)

Note the standard keyboard shortcuts for copy and paste do not work in the terminal as ```Ctrl``` + ```c``` is instead used to close a process. The keyboard shortcuts for copy in the command is ```Ctrl``` + ```⇧``` + ```c``` and for paste is ```Ctrl``` + ```⇧``` + ```v```.

![img_010](./images/img_010.png)

The license agreement will now display. Hold down ```↵``` to quickly scroll through it.

![img_011](./images/img_011.png)

At the end of the license agreement ```(END)``` will display. To quit this end statement input ```q```

![img_012](./images/img_012.png)

You will be asked if you want to accept the license agreement, input ```yes```

![img_013](./images/img_013.png)

Mambaforge will be installed in the default location ```~/mambaforge```. Input ```↵``` to use the default location.

![img_014](./images/img_014.png)

The mambaforge folder will be created and display within ```~```

![img_015](./images/img_015.png)
![img_016](./images/img_016.png)

The base installation will be complete. The next screen will prompt for initialisation **but unfortunately has the default option set at no**.

![img_017](./images/img_017.png)

Initialisation modifies the hidden ```.bashrc``` file, adding Mambaforge functionality. This file is referenced for available commands when opening a new Terminal.

![img_019](./images/img_019.png)

If Hidden FIles are not shown. Select File Options and then Show Hidden Files.

![img_018](./images/img_018.png)

By default there is no entry for Mambaforge.

![img_020](./images/img_020.png)

Input ```yes```.

![img_021](./images/img_021.png)

The ```.bashrc``` file will now be updated to include:

![img_134](./images/img_134.png)

```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/philip/mambaforge/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/philip/mambaforge/etc/profile.d/conda.sh" ]; then
        . "/home/philip/mambaforge/etc/profile.d/conda.sh"
    else
        export PATH="/home/philip/mambaforge/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/home/philip/mambaforge/etc/profile.d/mamba.sh" ]; then
    . "/home/philip/mambaforge/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<
```
My username ```philip``` appears 6 times. If manually initialising the install copy and paste the above into the ```.bashrc``` file and replace these 6 instances with your username.

The updated ```bashrc``` will only be referenced when invoking a new instance of the Terminal, so close any Terminal Windows and reopen the Terminal.

![img_022](./images/img_022.png)

## Exploring the base Environment

Mambaforge contains a default Python environment named ```base```. The prompt will be prefixed with ```(base)``` indicating that this is the currently selected Python environment.

![img_023](./images/img_023.png)

The physical location of this can be found by going to.

```
~/mambaforge
```

![img_024](./images/img_024.png)

```
~/mambaforge/lib
```

![img_025](./images/img_025.png)

```
~/mambaforge/lib/pythonx.xx
```

![img_026](./images/img_026.png)

This folder contains Python and its inbuilt modules such as ```email```:

![img_027](./images/img_027.png)

When the command:

```
import email
```

is used, the ```__init__.py``` within the ```email``` folder is imported.

![img_028](./images/img_028.png)


If the command:

```
import email.charset as charset
```

is used, the ```charset.py``` within the ```email``` folder is imported.

Some of the other inbuilt modules are simpler and only have a single Python script file. 

![img_029](./images/img_029.png)

When the command:

```
import datetime
```

is used, the ```datetime.py``` file is imported.

There is a subfolder called ```site-packages``` which contains the third-party libraries.

```~/mambaforge/lib/pythonx.xx/site-packages```

![img_030](./images/img_030.png)

The installed ```base``` Python environment, by default has minimal changes over the conventional installer from Python.org. There are however three folders ```pip```, ```conda``` and ```mamba``` which correspond to the three package managers most commonly used with Python. 

![img_031](./images/img_031.png)

```mamba``` is the most functional package manager and any package installation commands that involve the legacy package managers ```pip``` or ```conda``` should be replaced by an equivalent ```mamba``` command.

To list the packages installed use the command:

```mamba list```

![img_032](./images/img_032.png)

The name, version and channel of each package will be listed. The default channel for Mambaforge is ```conda-forge``` which is the community channel. The community channel is usually the most up to date channel and is open source. The community channel ```conda-forge``` should be used in preference to the commercial channel ```conda``` which is maintained by the Anaconda company, for their commercial data science distribution.

![img_035](./images/img_035.png)
![img_036](./images/img_036.png)

## Updating the base Environment

In the example above ```mamba``` has a version of 0.25.0, the latest version of Python and this package managers can be updated using the command.

```
mamba update -c conda-forge --all
```

![img_037](./images/img_037.png)

It is optional but recommended to specify the community channel using ```-c conda-forge```. Mambaforge should default to the community channel by default.

```--all``` is used to search for the latest version of all the packages in the Python environment.

![img_038](./images/img_038.png)

A list of proposed changes will be displayed. For example, the old version of mamba ```0.25.0``` will be replaced by the current version ```0.26.0```.

To proceed with the changes input ```y```:

![img_039](./images/img_039.png)
![img_040](./images/img_040.png)

The packages will be downloaded and extracted.

![img_041](./images/img_041.png)

Notice that the version number of the mamba dist-info folder has changed.

![img_042](./images/img_042.png)

The ```base``` Python environment and ```mamba``` package manager are now up to date.

## Running Python from the Terminal

The Text Editor preinstalled with Ubuntu can be launched from the Start Screen:

![img_135](./images/img_135.png)

The Text Editor can be used to make a Python Script File:

![img_136](./images/img_136.png)

Input:

```
print("Hello World!")
```

![img_137](./images/img_137.png)

Save the file using the shortcut key ```Ctrl``` + ```s```. Select the location as Documents and name the file ```script0.py``` changing the file extension from ```.txt``` to ```.py```:

![img_138](./images/img_138.png)

The file should now show in Documents:

![img_139](./images/img_139.png)

Open up the Terminal. The MambaForge is opened in ```~``` (home) by default. Input:

```
cd ~/Documents
```

cd is a Linux command which is an abbreviation for change directory (change folder).

![img_140](./images/img_140.png)

To use Python to run the Python script file input python3 (lower case) followed by the name of the script file including the file extension:

```
python3 script0.py
```

![img_141](./images/img_141.png)

The print statement included in the Python Script file will be displayed on the terminal:

![img_142](./images/img_142.png)

Bringing this together, there is a terminal (Mambaforge Prompt), a script file editor (Text Editor) and the file explorer (Nautilus):

![img_148](./images/img_148.png)

If ```python3``` is input into the Mambaforge Prompt without any script file. The Python interpretter will display:

```
python3
```

![img_143](./images/img_143.png)

Notice the prompt change from ```(base)``` to ```>>>```. When the Python interpretter is invoked, individual lines of Python can be executed. Input:

```
print("Hello World!")
```

![img_145](./images/img_145.png)

To exit the Python interpretter type in the command:

```
exit()
```

![img_147](./images/img_147.png)

Notice the prompt change back to ```(base)``` from ```>>>```.

## Integrated Development Environment¶

Python has a large number of Integrated Development Environments often abbreivated as IDEs. These are essentially a GUI which includes a console, script editior and file explorer.

## The IDLE IDE

Python comes preinstalled with the Integrated Development Learner Environment (IDLE). IDLE is found in:

```
~/mambaforge/lib/python3.xx/idlelib
```

![img_148](./images/img_148.png)

![img_149](./images/img_149.png)

![img_150](./images/img_150.png)

It can be launched using the ```idle.py``` module:

![img_151](./images/img_151.png)

Right click empty space in the folder and select Open in Terminal:

![img_153](./images/img_153.png)

Input:

```
python3 idle.py
```

![img_154](./images/img_154.png)

IDLE can also be launched directly from the terminal irrespective of the file path the terminal is open in by using the command:

```
idle3
```

![img_155](./images/img_155.png)

The first component of IDLE is the IDLE Shell which is essentially a Console. The prompt displays ```>>>``` indicating the Python interpretter is invoked. Individual lines of Python can be input directly as seen before:

![img_156](./images/img_156.png)

The File menu can be used to create a new file or open an existing file:

![img_157](./images/img_157.png)

In this case a new file is selected and the script editor displays. Before adding contents to the file, select File → Save As...:

![img_158](./images/img_158.png)

Save the file with a ```.py``` extension:

![img_159](./images/img_159.png)

The tab ```↹``` key can be pressed after inputting some code prefix. This will display completion options available that have the code prefix. In this case the code prefix was p and the command print has this code prefix:

![img_160](./images/img_160.png)

When a function name is input with open parenthesis, a docstring popup displays giving details about the functions input arguments. In this case the positional input value is going to be the string that is printed.

![img_161](./images/img_161.png)

Once again input:

```
print("hello world!")
```

![img_162](./images/img_162.png)

A Python Script File is also known as a Module. Once the Python Script File is saved, it can be run by selecting Run → Run Module:

![img_163](./images/img_163.png)

The print statement is observed on the IDLE Shell as expected:

![img_164](./images/img_164.png)

## Python Environments

It is possible to install all packages directly to the ```base``` Python environment. However it is generally good practice to create seperate Python environments, that is sub-installations for each Integrated Development Environment (IDE) or a major project.

An IDE is an application used by a developer to interface with the Python programming language. This guide will instruct in creating a Python Environment for the Spyder IDE and another one for the JupyterLab IDE.

Returning to:

```
~/mambaforge
```

![img_043](./images/img_043.png)

There is an ```envs``` subfolder which is empty by default.

```
~/mambaforge/envs
```

![img_044](./images/img_044.png)

## The Spyder IDE

A new environment can be created for the Spyder IDE using the command:

```
mamba create spyder-cf
```

where ```spyder-cf``` is the name of the Python environment.

![img_045](./images/img_045.png)

The Python environment will now be created.

![img_046](./images/img_046.png)

Physically this displays as:

```
~/mambaforge/envs/spyder-cf
```

![img_047](./images/img_047.png)

This folder is empty because no additional packages have been added.

![img_048](./images/img_048.png)

Currently the ```base``` Python environment is activated as indicated by the prompts prefix ```(base)```. This means any command used to manipulate packages will change the packages in the ```base``` environment.

![img_049](./images/img_049.png)

To instead make changes to the Python environment ```spyder-cf```, the ```spyder-cf``` environment needs to be activated using the command:

```
mamba activate spyder-cf
```

![img_050](./images/img_050.png)

Notice that the prompts prefix is now ```(spyder-cf)```. Now any package manipulation commands will change the packages in ```spyder-cf```.

![img_051](./images/img_051.png)

Note when the Terminal is closed and reopened, the default Python environment ```base``` will be reselected.

A package can be searched for using the command:

```
mamba search -c conda-forge packagename
```

For example, the Spyder IDE has the package name ```spyder```:

```
mamba search -c conda-forge spyder
```

For the search, once again it is recommended to explicitly reference the community channel ```-c conda-forge```.

![img_052](./images/img_052.png)

The search results will display, from earliest to latest version:

![img_053](./images/img_053.png)
![img_054](./images/img_054.png)

To install the package use the syntax:

```
mamba install -c conda-forge packagename=x.x.x
mamba install -c conda-forge packagename
```

If the version number is not stated, the latest version will be installed.

To install the latest version of Spyder use:

```
mamba install -c conda-forge spyder
```

![img_056](./images/img_056.png)

Or to install specifically version 5.3.3 use:

```
mamba install -c conda-forge spyder=5.3.3
```

![img_055](./images/img_055.png)

Since the Spyder IDE is written in Python and uses Python libraries, it requires a large number of mandatory dependencies to work and is why it is recommended to install an IDE in its own Python environment:

![img_057](./images/img_057.png)
![img_058](./images/img_058.png)
![img_059](./images/img_059.png)
![img_060](./images/img_060.png)
![img_061](./images/img_061.png)
![img_062](./images/img_062.png)
![img_063](./images/img_063.png)

These dependencies include Python itself and then the Python libraries for creating a user interface such as PyQt and Python Libraries for code completion such as Jedi. 

Input ```y``` in order to proceed.

The cached libraries exist in the Python ```base``` environment and are copied across, the remaining libraries are downloaded and installed:

![img_064](./images/img_064.png)

Now the ```spyder-cf``` folder has its own ```lib``` subfolder.

```
~/mambaforge/envs/spyder-cf/lib
```

![img_065](./images/img_065.png)

Which has its own ```pythonx.xx``` folder:

```
~/mambaforge/envs/spyder-cf/lib/pythonx.xx
```

![img_066](./images/img_066.png)

This folder has its own inbuilt modules such as ```email``` and ```datetime```.

![img_067](./images/img_067.png)
![img_068](./images/img_068.png)
![img_069](./images/img_069.png)

This Python installation and these inbuilt modules are selected when this Python environment is activated.

This folder also has its own ```site-packages``` subfolder:

```
~/mambaforge/envs/spyder-cf/lib/pythonx.xx/site-packages
```

![img_070](./images/img_070.png)

The Spyder IDE and all of it's other third-party library dependencies are found within ```site-packages```. Specifically for the Spyder IDE, there is the folder

```
~/mambaforge/envs/spyder-cf/lib/pythonx.xx/site-packages/spyder
```

![img_071](./images/img_071.png)
![img_072](./images/img_072.png)

To launch Spyder use the command:

```
spyder
```

![img_073](./images/img_073.png)

Note the following script file is executed in the terminal when Spyder is run:

```
~/mambaforge/envs/spyder-cf/pythonx.xx/site-packages/spyder/__init__.py
```

This file runs executes an infinite while loop within the terminal while the Spyder IDE runs. Another Terminal instance can be opened in order to carry out other commands simultaneously.

The Terminal window running Spyder will display some information. The Wayland warning can be ignored.

![img_074](./images/img_074.png)

The Spyder IDE will open:

![img_076](./images/img_076.png)

And you can take the optional tour to familarise yourself with the IDE:

![img_075](./images/img_075.png)

Spyder will display a module not found error if any of the data science libraries are attempted to be used. This is because only the mandatory dependencies are installed and none of the optional dependencies are. The dependencies can be checked by selecting Help → Dependencies

![img_080](./images/img_080.png)

The mandatory dependcies are all installed:

![img_077](./images/img_077.png)

But the optional ones are missing:

![img_078](./images/img_078.png)

Closing down Spyder will end, the infinite loop. If not the shortcut key ```Ctrl``` + ```c``` can be used to close any processes running in the Terminal:

![img_081](./images/img_081.png)

The optional dependencies can be installed using:

```
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

Note multiple packages are being installed here and each package name is seperated by a space. seaborn will install a compatible version of numpy, pandas and matplotlib as dependencies. sympy openpyxl xlrd xlsxwriter lxml sqlachemy are file format converters commonly used by libraries such as pandas.


![img_082](./images/img_082.png)

Once again the ```mamba``` package manager will look for the packages.

![img_083](./images/img_083.png)

And display a number of proposed changes. Input ```y``` in order to proceed.

![img_086](./images/img_086.png)
![img_087](./images/img_087.png)

The optional dependencies are now installed.

![img_088](./images/img_088.png)

Now there is a numpy, pandas, matplotlib and seaborn folder.

![img_089](./images/img_089.png)

In the numpy folder there is a ```__init__.py``` file. When the command:

```
import numpy as np
```

is used, the following file is imported.

```
~/mambaforge/envs/spyder-cf/lib/pythonx.xx/site-packages/numpy/__init__.py
```

![img_090](./images/img_090.png)

The numpy folder also has a number of modules such as random. The random folder has its own ```__init__.py``` file.

![img_091](./images/img_091.png)
![img_092](./images/img_092.png)

When the command:

```
import numpy.random as random
```

is used, the following file is imported.

```
~/mambaforge/envs/spyder-cf/lib/pythonx.xx/site-packages/numpy/random/__init__.py
```


In the case of matplotlib, it is more common to use the pyplot module opposed to the entire library.

![img_093](./images/img_093.png)
![img_094](./images/img_094.png)

When the command:

```
import matplotlib.pyplot as plt
```

is used, the following file is imported.

```
~/mambaforge/envs/spyder-cf/lib/pythonx.xx/site-packages/matplotlib/pyplot.py
```

Spyder can be relaunced using:

```
spyder
```

![img_095](./images/img_095.png)

Now the standard module imports work as expected:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

![img_096](./images/img_096.png)

To the left hand side is the script editor, the current blank script file can be saved to ```~/Documents``` using File, Save As:

![img_097](./images/img_097.png)

The script can be saved with a ```.py``` extension:

![img_098](./images/img_098.png)

In Python prefixing a line with a ```#``` turns it into a comment. In Spyder prefixing a line with ```#%%``` turns it into a new cell. A script file can be run using the run button or each cell can be run individually using the run cell or run cell and move onto the next cell button:

![img_099](./images/img_099.png)

At first launch, there will be a dialog for Run options. Select Run:

![img_100](./images/img_100.png)

The Files Pane will be updated to select the current working directory, which is the folder the script file is saved in:

![img_101](./images/img_101.png)

Variables will be displayed in the Variable Explorer and can be clicked for more detail:

![img_102](./images/img_102.png)

Plots will display as static images in the plots pane, by default:

![img_103](./images/img_103.png)

Plot preferences can be changed by going to, Tools → Preferences:

![img_104](./images/img_104.png)

Then selecting the Ipython console in the left tab and the Graphics top tab. In this menu, the plot backend can be changed from the static inline to the interactive automatic backend:

![img_105](./images/img_105.png)

For the change to take place, the kernel needs to be restarted. Select Consoles → Restart Kernel:

![img_106](./images/img_106.png)

Select Yes:

![img_107](./images/img_107.png)

Now relaunching the script, gives the plot in a seperate interactive window:

![img_108](./images/img_108.png)

The Spyder preferences file ```spyder.ini``` can be found in the hidden ```.config``` folder:

```
~/.config/spyder-py3/config
```

![img_109](./images/img_109.png)
![img_110](./images/img_110.png)
![img_111](./images/img_111.png)
![img_112](./images/img_112.png)

This is a text file that can be changed or copied from computer to computer:

![img_113](./images/img_113.png)

Spyder uses a dark theme by default. It can be changed to a light theme by going to Tools → Preferences and then selecting the Appearances tab. Within the Appearance Tab, change the Syntax highlighting scheme from Spyder Dark to Spyder. Select Apply:

![img_114](./images/img_114.png)

Select Yes to Restart Spyder:

![img_115](./images/img_115.png)

Spyder now uses the light theme:

![img_116](./images/img_116.png)

When a terminal is opened, the default Python environment ```base``` is selected. If the following command is attempted, there is a search for:

```
~/mambaforge/envs/spyder-cf/lib/pythonx.xx/site-packages/spyder/__init__.py
```

This file does not exist, so the error message is displayed.

![img_117](./images/img_117.png)

When instead, the ```spyder-cf``` environment is activated, the following file is searched for:

```
~/mambaforge/envs/spyder-cf/lib/pythonx.xx/site-packages/spyder/__init__.py
```

This file exists and therefore Spyder launches.

Similar to IDLE, the tab ```↹``` key can be pressed after inputting some code prefix. This will display completion options available that have the code prefix. In this case the code prefix was p and the command print has this code prefix:

![img_202](./images/img_202.png)

When a function name is input with open parenthesis, a docstring popup balloon displays giving details about the functions input arguments. In this case the positional input value is going to be the string that is printed.

![img_203](./images/img_203.png)

The code-completion in Spyder works well with Python and Python Standard Modules. For example a list of identifiers displays when the standard module ```datetime``` is imported using the alias ```dt``` and ```dt.``` followed by a tab ```↹```:

![img_204](./images/img_204.png)

The code-completion on the script editor has some limitations when it comes to third-party modules such as the datascience libraries. For example the list of identifiers displays when the ```numpy``` library is imported using the alias ```np``` and ```np.``` followed by a tab ```↹```:

![img_205](./images/img_205.png)

Typically, the line of code importing the third party library needs to be run in the console:

![img_206](./images/img_206.png)

The list of identifiers still does not display when the ```numpy``` library is imported using the alias ```np``` and ```np.``` followed by a tab ```↹```:

![img_207](./images/img_207.png)

However if a function from the numpy library is input with open parenthesis, its docstring will display as a pop-up balloon:

![img_208](./images/img_208.png)

The console uses slightly different code completion to the script editor. The list of identifiers does displays when the ```numpy``` library is imported using the alias ```np``` and ```np.``` followed by a tab ```↹``` however there is no distinction to what each identifier is i.e. whether it is a variable, function or class.

![img_209](./images/img_209.png)

The docstring popup balloon also looks slightly different between the console and the editor:

![img_210](./images/img_210.png)

## The JupyterLab IDE

A similar Python environment can be setup for JupyterLab, the browser based IDE using:

```
mamba create -n jupyterlab-cf
mamba activate jupyterlab-cf
mamba install -c conda-forge jupyterlab
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
mamba install -c conda-forge nodejs ipywidgets 
mamba install -c conda-forge plotly dash jupyter-dash
mamba install -c conda-forge jupyterlab-variableinspector
```

JupyterLab is browser based and has a number of browser based extensions. Additional HTML based plotting libraries such as plotly work particularly well with JupyterLab.

To launch JupyterLab, activate the ```jupyterlab-cf``` Python environment and use the command:

```
jupyter-lab
```

Note there is a dash here.

![img_118](./images/img_118.png)

Similar to Spyder, the following script file is executed in the terminal when JupyterLab is run:

```
~/mambaforge/envs/jupyterlab-cf/pythonx.xx/site-packages/jupyterlab/__init__.py
```

This file runs executes an infinite while loop within the terminal while the JupyterLab IDE runs. 

![img_119](./images/img_119.png)

The IDE should open in a default tab in your default browser. If it does not, copy the address from the terminal either by using the right context menu or the shortcut key ```Ctrl```, ```⇧``` + ```c```.

Since an extension was installed, select build:

![img_120](./images/img_120.png)

Select Save and Reload when prompted:

![img_121](./images/img_121.png)
![img_122](./images/img_122.png)

The build is up to date and JupyterLab is ready to use. 

![img_123](./images/img_123.png)

![img_124](./images/img_124.png)

To close JupyterLab, close any open browser windows. Then press ```Ctrl``` + ```c``` in the Terminal to close the server:

![img_126](./images/img_126.png)

![img_127](./images/img_127.png)

A JupyterLab config file can be generated using the command:
```
jupyter server --generate-config
```
![img_128](./images/img_128.png)

The location of this file will be displayed:

![img_129](./images/img_129.png)

Typically in:

```
~/.jupyter
```

![img_130](./images/img_130.png)
![img_131](./images/img_131.png)

The redirect bool can be changed from the default bool of ```True``` to ```False``` if the browser fails to load JupyterLab:

![img_132](./images/img_132.png)

The default browser can be changed to ```"chromium"``` if it is opening in FireFox instead of Chromium:

![img_133](./images/img_133.png)

JupyterLab has a file explorer to the left hand side where you can navigate to your Documents folder.

![img_165](./images/img_165.png)

The Terminal can be invoked to run an existing Python Script file:

![img_166](./images/img_166.png)

Using the same command as before:

```
python script0.py
```

Displays Hello World on the Terminal.

![img_167](./images/img_167.png)

A Python file can be created from the launcher:

![img_168](./images/img_168.png)

The file can be renamed by right clicking it on the file explorer and selecting rename or right clicking on the open tab at the top which displays the file name:

![img_169](./images/img_169.png)

![img_170](./images/img_170.png)

To get code completion options to display while editing the file, right click blank space within the file and select Create Console for Editor:

![img_171](./images/img_171.png)

Select the default Kernel.

Code completion will work in a similar manner as IDLE. The tab ↹ key can be pressed after inputting some code prefix. This will display completion options available that have the code prefix. In this case the code prefix was p and the command print has this code prefix:

![img_172](./images/img_172.png)

A docstring will display if a function is input with open parenthesis and the shift ```⇧``` and tab ```↹``` are pressed:

![img_173](./images/img_173.png)

A list of all the identifiers within a standard Python module will be displayed after the module is imported and the module name is input followed by a dot ```.``` and ```↹```:

![img_174](./images/img_174.png)

For a third-party module such as a datascience library, no code completion options display.

![img_175](./images/img_175.png)

The library generally needs to be imported into the console for its code completion to be recognised. The line of code (lines of code) with the data science library imports can be selected:

![img_176](./images/img_176.png)

Then Run and Run Code can be selected:

![img_177](./images/img_177.png)

The list of all the identifiers within the numpy module should now display after the module is imported and the module name is input followed by a dot ```.``` and ```↹```. 

This doesn't seem to work correctly in a script editor but works correctly in the Console.

*This problem occurs on IDLE, Spyder and JupyterLab and is likely a bug in the IPython console that needs to be addressed.*


![img_178](./images/img_178.png)

![img_179](./images/img_179.png)

A docstring will display if a function is input with open parenthesis and the shift ```⇧``` and tab ```↹``` are pressed:

![img_180](./images/img_180.png)

Additional test code can be added to make a plot:

onen
Now all the code can be run by selecting Run→Run All Code:

![img_182](./images/img_182.png)

The script file is executed and the print statement and plot are displayed in the console:

![img_183](./images/img_183.png)

The plot backend can be changed from the default inline to automatic using:

![img_184](./images/img_184.png)

![img_185](./images/img_185.png)

The JupyterLab IDE lacks some features available in Spyder when it comes to editting Python Script Files:

* It has no Variable Inspector or Variable Explorer
* It has no way of running cells within a Python Script File.

The JupyterLab IDE has more of a focus on Interactive Python Notebooks which have the .ipynb extension:

![img_186](./images/img_186.png)

The notebook can be renamed using the file explorer or the top tab of the open notebook:

![img_187](./images/img_187.png)

The notebook consists of cells. The cells can be:

* markdown - for markdown syntax: The Markdown display will be shown when the code is run.
* python - for Python code: Python code will be executed when the cell is run.
* raw - The notebook itself is written in nodejs, another programming language used for web development.

![img_188](./images/img_188.png)

A markdown heading can be created and then the cell can be run:

![img_189](./images/img_189.png)

The heading will now display under the notebooks bookmarks:

![img_190](./images/img_190.png)

A code cell can now be created:

![img_191](./images/img_191.png)

The shortcut key ```esc``` and ```m``` will change the current cell to a markdown cell.

The shortcut key ```esc``` and ```y``` will change the current cell to a code cell.

The shortcut key ```⇧``` and ```↵``` will run a cell.

The shortcut key ```alt``` and ```↵``` will run a cell and insert a blank cell below it.

To get to Keyboard Shortcuts. Select the Settings menu to the top and then select Advanced Settings Editor. To the left select Command Palette and then select keyboard shortcuts.

Code completion works better in a notebook file. A third-party data science module needs to be imported in a previously cell. Once this cell is run typing in the module name or module alias followed by a ```.```, pressing the tab ```↹``` key will display the list of identifiers from the module:

![img_192](./images/img_192.png)

When code cells are run, a number displays to the left hand side of the cell (this number is analogous to the numbers shown in the console when running Python code or a Python script file) and indicates the number of cells ran in the Python kernel:

![img_193](./images/img_193.png)

JupyterLab has a Variable Inspector extension that can be viewed in an interactive notebook by right clicking blank space in the notebook file and selecting open Variable Inspector:

![img_194](./images/img_194.png)

This opens in a new tab which can be repositioned:

![img_195](./images/img_195.png)

![img_196](./images/img_196.png)

To close JupyterLab, close the tab in the browser. In the Terminal you will notice that the server is still running.

![img_197](./images/img_197.png)

The server runs in an infinite loop. To end it press Ctrl + c:

![img_198](./images/img_198.png)

If the .ipynb file is opened in notepad. The nodejs script can be viewed directly.

![img_199](./images/img_199.png)

![img_200](./images/img_200.png)

The nodejs code can be seen to enclose the Python code. Plotting libraries such as plotly take Python syntax from the user and output nodejs code which is used to display the interactive plot.

![img_201](./images/img_201.png)

Return to:

[Home](../../../../)
