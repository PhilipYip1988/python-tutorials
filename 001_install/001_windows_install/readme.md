# Installing Python on Windows 11 (Mambaforge, IDLE, Spyder, JupyterLab, VSCode)

[YouTube Tutorial](https://www.youtube.com/watch?v=O-WZedLq_sE)

## System Requirements

The PC should match or exceed the following system requirements:

* Windows 11 (22H2) or Windows 10 (22H2) 64 Bit
* 6th Generation Intel i5 Processor or Later
* 8 GB RAM or Superior
* 250 GB SSD or Superior
* Google Chrome or Microsoft Edge Browser

The performance for Python will be very poor if these system requirements are not satisfied.

## Mambaforge Install

Mambaforge can be downloaded from the Mambaforge GitHub repository. Make sure to download Mambaforge and not Miniforge (which excludes the Mamba package manager):

[Mambaforge](https://github.com/conda-forge/miniforge#mambaforge)

Double click to launch the installer:

![001_mambaforge_install](./images/001_mambaforge_install.png)

Select Next:

![002_mambaforge_install](./images/002_mambaforge_install.png)

Select Just Me (recommended):

![003_mambaforge_install](./images/003_mambaforge_install.png)

Install in the default directory. In Windows this will be in 

```
%UserProfile%\mambaforge
``` 

which in my case maps to 

```
C:\Users\Philip\mambaforge
```

![004_mambaforge_install](./images/004_mambaforge_install.png)

In the next screen, select the default options to register Mambaforge as my default Python and create start menu shortcuts.

![005_mambaforge_install](./images/005_mambaforge_install.png)

**Mambaforge can optionally be added to the Windows Environment Variable Path.** This makes the ```base``` Python environment accessible via the Windows Terminal. This allows third party applications to accessing Python from the Windows Terminal. Such a use case is normally more advanced, for example a C++ IDE that is configured by default to access the Windows Terminal will also be able to invoke a Python Script if Mambaforge is added to the Windows Environmental Variables Path.

Note that in most regular use scenarios the Mambaforge Prompt should be preferentially used to interact with Python instead of the Windows Terminal. The Mambaforge Prompt is similar to the Windows Terminal but is optimised to work with multiple Python environments and not hard coded to the single base environment provided in the Windows Environmental Variables Path like in the case of the Windows Terminal. The Mambaforge Prompt can be used to install packages in Python environments and launch IDEs installed in the Python environments. 

![006_mambaforge_install](./images/006_mambaforge_install.png)

![007_mambaforge_install](./images/007_mambaforge_install.png)

Once the decision to add Mambaforge to the Windows Environmental Path or not is configured. Select Install:

![008_mambaforge_install](./images/008_mambaforge_install.png)

Select Next:

![009_mambaforge_install](./images/009_mambaforge_install.png)

Select Finish:

![010_mambaforge_install](./images/010_mambaforge_install.png)

# The Windows Environment Variable Path

The Windows Environmental Varables Path can be checked by right clicking the Start Button and selecting System:

![011_path](./images/011_path.png)

Then selecting Advanced System Settings:

![012_path](./images/012_path.png)

Then Advancd and Environmental variables:

![013_path](./images/013_path.png)

Select Path and then Edit:

![014_path](./images/014_path.png)

If Mambaforge has been added to the path the following 5 entries will display:

```
%UserProfile%\mambaforge
%UserProfile%\mambaforge\Library\mingw-w64\bin
%UserProfile%\mambaforge\Library\usr\bin
%UserProfile%\mambaforge\Library\bin
%UserProfile%\mambaforge\Scripts
```

![015_path](./images/015_path.png)

# Launching the Mambaforge Prompt

Launch the Mambaforge prompt:

![016_miniforge_prompt](./images/016_miniforge_prompt.png)

By default the ```base``` Python environment will be selected, this is minimal, containing Python and the ```mamba``` package manager:

![017_miniforge_prompt](./images/017_miniforge_prompt.png)

In Windows Explorer, navigate to:

```
%UserProfile\mambaforge
```

Notice there is a python.exe in this folder. This is the default Python executable.

![018_miniforge_prompt](./images/018_miniforge_prompt.png)

Notice that there is also a Lib subfolder:

```
%UserProfile\mambaforge\lib
```

This is the folder where all the builtin Python Modules are installed, for example the datetime module (which exists as datetime.py) and email module (which exists as a subfolder called email, this subfolder contains a ```__init__.py``` file):

![019_miniforge_prompt](./images/019_miniforge_prompt.png)

In this Lib subfolder there is also a site-packages folder:

```
%UserProfile\mambaforge\lib\site-packages
```

where third party data science libraries are installed (if they are installed to the base Python environment):

![020_miniforge_prompt](./images/020_miniforge_prompt.png)

# Updating the base Python Environment

Before making any changes to packages the base conda environment should be updated as this will make sure the latest version of the ```mamba``` package manager is installed. Use the command:

```
mamba update -c conda-forge --all
```

Where ```-c``` is an abbreviation for channel and ```conda-forge``` is the community channel ```conda-forge```. ```--all``` instructs the ```mamba``` package manager to update all packages.

![021_miniforge_prompt](./images/021_miniforge_prompt.png)

Details will display outlining the proposed changes to the base Python environment:

![022_miniforge_prompt](./images/022_miniforge_prompt.png)

![023_miniforge_prompt](./images/023_miniforge_prompt.png)

![024_miniforge_prompt](./images/024_miniforge_prompt.png)

To proceed input:

```y```

The following command is used to search for a package:

```
mamba search -c conda-forge packagename
```

To install a package use the command:

```
mamba install -c conda-forge packagename
```

To install a package of specific version use the command:

```
mamba install -c conda-forge packagename=1.2.3
```

## Running Python from the Mambaforge Prompt

Python is now installed and it can be used to execute code in a Python Script File. Go to the Documents folder and right click the empty space and select New → Text Document:

![084_img](./images/084_img.png)

Name the file ```script0.py``` changing the file extension from ```.txt``` to ```.py``` and select Yes at the warning to change the file extension:

![085_img](./images/085_img.png)

Right click the file and select Open With... and then select Notepad:

![086_img](./images/086_img.png)

Input:

```
print("Hello World!")
```

and save the file.

![087_img](./images/087_img.png)

Open the Mambaforge Prompt:

![088_img](./images/088_img.png)

Input:

```
cd Documents
```

cd is a PowerShell command which is an abbreviation for change directory (change folder). Because the MambaForge opened in ```%UserProfile```, ```Documents``` could directly be selected as a subfolder.

![089_img](./images/089_img.png)

To use Python to run the Python script file input python (lower case) followed by the name of the script file including the file extension:

```
python script0.py
```

![090_img](./images/090_img.png)

The print statement included in the Python Script file will be displayed on the console:

![091_img](./images/091_img.png)

Bringing this together, there is a console (Mambaforge Prompt), a script file editor (Notepad) and the file explorer (Windows Explorer):

![092_img](./images/092_img.png)

If Notepad++ is used in place of Notepad as the script editor, there are some code completion options displayed as code is input:

![093_img](./images/093_img.png)

If ```python``` is input into the Mambaforge Prompt without any script file. The Python interpretter will display:

```
python
```

![094_img](./images/094_img.png)

Notice the prompt change from ```(base) %UserProfile%``` to ```>>>```. When the Python interpretter is invoked, individual lines of Python can be executed. Input:

```
print("Hello World!")
```

![095_img](./images/095_img.png)

To exit the Python interpretter type in the command:

```
exit()
```

![096_img](./images/096_img.png)

Notice the prompt change back to ```(base) %UserProfile%``` from ```>>>```. 

## Integrated Development Environment

Python has a large number of Integrated Development Environments often abbreivated as IDEs. These are essentially a GUI which includes a console, script editior and file explorer.

## The IDLE IDE

Python comes preinstalled with the Integrated Development Learner Environment (IDLE). IDLE is found in:

```
%UserProfile%/mambaforge/Lib/idlelib
```

![097_img](./images/097_img.png)

![098_img](./images/098_img.png)

And can be launched using the ```idle.bat```:

![099_img](./images/099_img.png)

More commonly it is launched from the mabaforge prompt by inputting:

```
idle
```

The first component of IDLE is the IDLE Shell which is essentially a Console. The prompt displays ```>>>``` indicating the Python interpretter is invoked. Individual lines of Python can be input directly as seen before:

![100_img](./images/100_img.png)

The File menu can be used to create a new file or open an existing file:

![101_img](./images/101_img.png)

In this case a new file is selected and the script editor displays. Before adding contents to the file, select File → Save As...:

![102_img](./images/102_img.png)

Save the file with a ```.py``` extension:

![103_img](./images/103_img.png)

The tab ```↹``` key can be pressed after inputting some code prefix. This will display completion options available that have the code prefix. In this case the code prefix was ```p``` and the command ```print``` has this code prefix:

![104_img](./images/104_img.png)

When a function name is input with open parenthesis, a docstring popup balloon displays giving details about the functions input arguments. In this case the positional input ```value``` is going to be the string that is printed. 

![105_img](./images/105_img.png)


Once again input:

```
print("hello world!")
```

![106_img](./images/106_img.png)

A Python Script File is also known as a Module. Once the Python Script File is saved, it can be run by selecting Run → Run Module:

![107_img](./images/107_img.png)

The print statement is observed on the IDLE Shell as expected:

![108_img](./images/108_img.png)

## Python Environments

Other Python IDEs generally need to be installed. Because these IDEs are typically large programs, with a large number of dependencies, it is generally advised to create a seperate Python environment for each IDE. A Python environment is essentially a subinstallation. Up until this point the default Python environment has been used ```base```. 

In the mambaforge folder, there is a subfolder called ```envs```:

```
%UserProfile\mambaforge\envs
```

![025_envs](./images/025_envs.png)

By default this is empty:

![026_envs](./images/026_envs.png)

## The Spyder IDE

To create a Python Environment use the command:

```
mamba create -n spyder-cf
```

![027_envs](./images/027_envs.png)

Where ```-n``` is an abbreviation for name and ```spyder-cf``` is the name of the Python environment. In this case the name is spyder-cf denotes an install of the latest version of spyder from the ```conda-forge``` channel.

The following folder appears:

```
%UserProfile\mambaforge\envs\spyder-cf
```

![028_envs](./images/028_envs.png)

It is mainly empty by default:

![029_envs](./images/029_envs.png)

Notice the prompt is prefixed with ```(base)``` which means the ```base``` Python environment is selected and any commands to change packages will therefore operate on this environment. 

![030_envs](./images/030_envs.png)

To activate (select) the new environment use:

```
conda activate spyder-cf
```

![031_envs](./images/031_envs.png)

Notice after activation (selection) the prompt now begins with ```spyder-cf``` indicating that any commands to change packages will operate on the ```spyder-cf``` Python environment (leaving the ```base``` Python environment untouched).

![032_envs](./images/032_envs.png)

**Closing the Mambaforge Prompt and relaunching will automatically reselect the ```base``` Python Environment. Reactivate the desired Python environment before amending packages or attempting to launch an IDE from the Python Environment.**

To look at the packages installed in the Python environment use:

```
mamba list
```

![033_envs](./images/033_envs.png)

In this case, this is an empty Python environment as expected:

![034_envs](./images/034_envs.png)

For other Python environments revisions made to the environment can be examined using:

```
mamba list --revision
```

To search for spyder use:

```
mamba search -c conda-forge spyder
```

![035_envs](./images/035_envs.png)

Numerous versions of the Spyder IDE spyder package are listed:

![036_envs](./images/036_envs.png)

Install the latest version using:

```
mamba install -c conda-forge spyder
```

![037_envs](./images/037_envs.png)

Spyder is an Integrated Development Environment (IDE) which is a user interface for interacting with Python, as a result it has alot of mandatory dependencies including Python itself.

![038_envs](./images/038_envs.png)

To proceed input

```
y
```

Spyder will now be installed with its mandatory dependencies. 

![039_envs](./images/039_envs.png)

The mandatory dependencies essentially only allow use of Spyder with the Python programing language itself and none of the commonly used data science libraries are available. Notice that in the folder there is now a python application, which is associated with this Python environment. This Python application will be launched when using a Python command while this Python environment is selected: 

```
%UserProfile\mambaforge\envs\spyder-cf
```

![040_envs](./images/040_envs.png)

This Python environment also has a Lib subfolder containing the inbuilt python modules such as datetime and email. These will be used if these modules are imported within a Python script that is ran while this Python environment is selected:

```
%UserProfile\mambaforge\envs\spyder-cf\Lib
```

![041_envs](./images/041_envs.png)

There is also a site-packages folder which is the location for data-science libraries to be installed:

![042_envs](./images/042_envs.png)

Currently the installation contains only mandatory dependencies, allowing Spyder to work with Python and lacks the data science libraries which are commonly used with Spyder. These can be installed using:

```
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

Note multiple packages are being installed here and each package name is seperated by a space. seaborn will install a compatible version of numpy, pandas and matplotlib as dependencies. sympy openpyxl xlrd xlsxwriter lxml sqlachemy are file format converters commonly used by libraries such as pandas.

![043_envs](./images/043_envs.png)

To proceed input:

```
y
```

![044_envs](./images/044_envs.png)

These data science libaries will now be installed:

![045_envs](./images/045_envs.png)

To launch spyder, ensure the ```spyder-cf``` Python environment is activated and use the command:

```
spyder
```

![046_envs](./images/046_envs.png)

Spyder will now launch:

![047_envs](./images/047_envs.png)

In the bottom right of the Spyder IDE is the console, where an individual command can be executed. To the left is the script editor where a Python Script File ```.py``` extension can be created.

Before starting with a script file, it is recommended to save it using file save as:

![048_envs](./images/048_envs.png)

Script files should use the Python rules of variable names, using lower case characters and no special characters with exception to the underscore. 

Numbers can be included in the file name but the file name should not begin with numbers. File names should not match inbuilt objects or the names of common Python libraries. 

Calling a script ```numpy.py``` for example will lead to errors as it will be imported instead of the ```numpy``` library. In this example, we will save the script file to documents and call it ```spyder_test.py```:

![049_envs](./images/049_envs.png)

Let's now ```import numpy```. This will first look for a script file in the current working directory which is the documents folder called ```numpy.py``` which it won't find:

![050_envs](./images/050_envs.png)

It will then look within:

```
%UserProfile\mambaforge\envs\spyder-cf\Lib
```

And search for an inbuilt module called ```numpy.py``` or a subfolder called ```numpy``` which it won't find. 

And then finally look within the site-packages subfolder:

```
%UserProfile\mambaforge\envs\spyder-cf\Lib\site-packages
```

For a file called ```numpy.py``` (which it won't find) or a folder called ```numpy``` which it will find:

![051_envs](./images/051_envs.png)

```
%UserProfile\mambaforge\envs\spyder-cf\Lib\site-packages\numpy
```

A module is a Python Script file with a ```.py``` extension and follows Python naming conventions for objects. A library is a grouping of associated script files in a folder. The name of the folder once again follows Python naming conventions of objects and indicates the name of the library. Within the folder is a Python Script file called ```__init__.py``` and this file is selected if the folder is imported. Inputting:

```
import numpy
```

references the folder ```numpy``` and specifically reads the contents of the ```__init__.py``` script file:

```
%UserProfile\mambaforge\envs\spyder-cf\Lib\site-packages\numpy\__init__.py
```

```
import numpy as np
```

The ```as np``` gives a 2 letter alias ```np```. This library is commonly used and the 2 letter alias is used to simplify the code made in the script editor as objects are continuously referenced from this library.

Other modules can be imported using the dot ```.``` syntax. In the ```numpy``` folder there is a ```random``` folder which contains another grouping of associated Python script files. This module can be imported using:

```
import numpy.random as random
```

where once again the alias ```random``` is used to simplify imports from this module:

![052_envs](./images/052_envs.png)

Note within this random folder is another ```__init__.py``` and this is the specific script file being referenced in the line of code above. 

```
%UserProfile\mambaforge\envs\spyder-cf\Lib\site-packages\numpy\random\__init__.py
```

![053_envs](./images/053_envs.png)

The next most commonly imported library is ```pandas``` which is imported using the alias ```pd```:

```
import pandas as pd
```

![054_envs](./images/054_envs.png)

This imports the objects defined in the file:

```
%UserProfile\mambaforge\envs\spyder-cf\Lib\site-packages\pandas\__init__.py
```

![055_envs](./images/055_envs.png)

The next most commonly used Python library is ```matplotlib```. It is more common to use a module within this library opposed to the entire library itself:

```
import matplotlib.pyplot as plt
```

![056_envs](./images/056_envs.png)

The matplotlib folder contains an ```__init__.py``` file:

![057_envs](./images/057_envs.png)

```
%UserProfile\mambaforge\envs\spyder-cf\Lib\site-packages\matplotlib\__init__.py
```

And a ```pyplot.py``` file:

![058_envs](./images/058_envs.png)

```
%UserProfile\mambaforge\envs\spyder-cf\Lib\site-packages\matplotlib\pyplot.py
```

It is this file that is referenced with the import command above.

Note that file extensions (```.py```) are not specified when using the import command.

In Python prefixing a line with a ```#``` turns it into a comment. In Spyder prefixing a line with ```#%%``` turns it into a new cell. A script file can be run using the run button or each cell can be run individually using the run cell or run cell and move onto the next cell button:

![059_envs](./images/059_envs.png)

The variables created ```x``` and ```y``` are displayed in Spyders Variable Explorer. The value can be double clicked and collections such as the arrays created above can be explored to view them in more detail.

![060_envs](./images/060_envs.png)

A basic command can be used to create a plot. By default plots display in the Plots pane as a static image however the backend can be changed to Automatic to enable an interactive plot in its own window. 

This can be done by going to Tools and Preferences:

![061_envs](./images/061_envs.png)

Then IPython Console and Graphics and changing the Backend to Automatic.

![062_envs](./images/062_envs.png)

The change requires a restart of the kernel which will remove all objects created on the variable explorer and all other objects imported. To do this select Consoles and Restart Kernel. 

![063_envs](./images/063_envs.png)

Select Yes at the warning to proceed:

![064_envs](./images/064_envs.png)

Rerunning the script now displays an automatic plot:

![065_envs](./images/065_envs.png)

An individual line of code from a script can be highlighted and ran in the console by selecting run selection or current line:

![066_envs](./images/066_envs.png)

Similar to IDLE, the tab ```↹``` key can be pressed after inputting some code prefix. This will display completion options available that have the code prefix. In this case the code prefix was p and the command print has this code prefix:

![142_img](./images/142_img.png)

When a function name is input with open parenthesis, a docstring popup balloon displays giving details about the functions input arguments. In this case the positional input value is going to be the string that is printed.

![143_img](./images/143_img.png)

The code-completion in Spyder works well with Python and Python Standard Modules. For example a list of identifiers displays when the standard module ```datetime``` is imported using the alias ```dt``` and ```dt.``` followed by a tab ```↹```:

![144_img](./images/144_img.png)

The code-completion on the script editor has some limitations when it comes to third-party modules such as the datascience libraries. For example the list of identifiers displays when the ```numpy``` library is imported using the alias ```np``` and ```np.``` followed by a tab ```↹```:

![145_img](./images/145_img.png)

Typically, the line of code importing the third party library needs to be run in the console:

![146_img](./images/146_img.png)

The list of identifiers still does not display when the ```numpy``` library is imported using the alias ```np``` and ```np.``` followed by a tab ```↹```:

![147_img](./images/147_img.png)

However if a function from the numpy library is input with open parenthesis, its docstring will display as a pop-up balloon:

![148_img](./images/148_img.png)

The console uses slightly different code completion to the script editor. The list of identifiers does displays when the ```numpy``` library is imported using the alias ```np``` and ```np.``` followed by a tab ```↹``` however there is no distinction to what each identifier is i.e. whether it is a variable, function or class.

![149_img](./images/149_img.png)

The docstring popup balloon also looks slightly different between the console and the editor:

![150_img](./images/150_img.png)

## The JupyterLab IDE

Another Python environment will be created for the JupyterLab IDE. The JupyterLab IDE is a browser based IDE and has the same optional dependencies as Spyder. because it is browser based, its functionality can be extended with interactive Python widgets ```ipywidgets``` and the browser based ```plotly``` plotting library. These extensions require ```nodejs```. An optional variable inspector is also available however is limited in comparison to Spyder.

```
mamba create -n jupyterlab-cf
mamba activate jupyterlab-cf
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
mamba install -c conda-forge jupyterlab
mamba install -c conda-forge nodejs ipywidgets 
mamba install -c conda-forge plotly dash jupyter-dash
mamba install -c conda-forge jupyterlab-variableinspector
```

To launch JupyterLab, activate the Python environment and use:

```
jupyter-lab
```

Note this is the only place where a ```-``` is used between Jupyter and Lab:

![067_jupyterlab](./images/067_jupyterlab.png)

When first launched, there will be a prompt to build JupyterLab, select Build:

![068_jupyterlab](./images/068_jupyterlab.png)

This will take a while. When finished select Save and Reload:

![069_jupyterlab](./images/069_jupyterlab.png)

JupyterLab has a file explorer to the left hand side where you can navigate to your Documents folder. 

![109_img](./images/109_img.png)

The Terminal can be invoked to run an existing Python Script file:

![131_img](./images/131_img.png)

Using the same command as before:

```
python script0.py
```

Displays Hello World on the Terminal.

![132_img](./images/132_img.png)

A Python file can be created from the launcher:

![110_img](./images/110_img.png)

The file can be renamed by right clicking it on the file explorer and selecting rename or right clicking on the open tab at the top which displays the file name:

![111_img](./images/111_img.png)

![112_img](./images/112_img.png)

To get code completion options to display while editing the file, right click blank space within the file and select Create Console for Editor:

![113_img](./images/113_img.png)

Select the default Kernel and select Select:

![114_img](./images/114_img.png)

![115_img](./images/115_img.png)

Code completion will work in a similar manner as IDLE. The tab ```↹``` key can be pressed after inputting some code prefix. This will display completion options available that have the code prefix. In this case the code prefix was ```p``` and the command ```print``` has this code prefix:

![116_img](./images/116_img.png)

A docstring will display if a function is input with open parenthesis and the shift ```⇧``` and tab ```↹``` are pressed:

![117_img](./images/117_img.png)

A list of all the identifiers within a standard Python module will be displayed after the module is imported and the module name is input followed by a dot ```.``` and ```↹```:

![119_img](./images/119_img.png)

For a third-party module such as a datascience library, no code completion options display. 

![120_img](./images/120_img.png)

The library generally needs to be imported into the console for its code completion to be recognised. The line of code (lines of code) with the data science library imports can be selected:

![121_img](./images/121_img.png)

Then Run and Run Code can be selected:

![122_img](./images/122_img.png)

The list of all the identifiers within the numpy module should now display after the module is imported and the module name is input followed by a dot ```.``` and ```↹```. 

This doesn't seem to work correctly in a script editor but works correctly in the Console.

*This problem occurs on IDLE, Spyder and JupyterLab and is likely a bug in the IPython console that needs to be addressed.*

![123_img](./images/123_img.png)

![154_img](./images/154_img.png)

A docstring will display if a function is input with open parenthesis and the shift ```⇧``` and tab ```↹``` are pressed:

![124_img](./images/124_img.png)

Additional test code can be added to make a plot:

![125_img](./images/125_img.png)

Now all the code can be run by selecting Run→Run All Code:

![126_img](./images/126_img.png)

The script file is executed and the print statement and plot are displayed in the console:

![127_img](./images/127_img.png)

The plot backend can be changed from the default inline to automatic using:

![130_img](./images/130_img.png)

The JupyterLab IDE lacks some features available in Spyder when it comes to editting Python Script Files:

* It has no Variable Inspector or Variable Explorer
* It has no way of running cells within a Python Script File.

The JupyterLab IDE has more of a focus on Interactive Python Notebooks which have the ```.ipynb``` extension:

![133_img](./images/133_img.png)

The notebook can be renamed using the file explorer or the top tab of the open notebook:

![134_img](./images/134_img.png)

The notebook consists of cells. The cells can be:

* markdown - for markdown syntax: The Markdown display will be shown when the code is run.
* python - for Python code: Python code will be executed when the cell is run.
* raw - The notebook itself is written in nodejs, another programming language used for web development. 

![073_jupyterlab](./images/073_jupyterlab.png)

A markdown heading can be created and then the cell can be run:

![074_jupyterlab](./images/074_jupyterlab.png)

The heading will now display under the notebooks bookmarks:

![075_jupyterlab](./images/075_jupyterlab.png)

A code cell can now be created:

![076_jupyterlab](./images/076_jupyterlab.png)

The shortcut key ```esc``` and ```m``` will change the current cell to a markdown cell.

The shortcut key ```esc``` and ```y``` will change the current cell to a code cell.

The shortcut key ```⇧``` and ```↵``` will run a cell.

The shortcut key ```alt``` and ```↵``` will run a cell and insert a blank cell below it.

To get to Keyboard Shortcuts. Select the Settings menu to the top and then select Advanced Settings Editor. To the left select Command Palette and then select keyboard shortcuts.

Code completion works better in a notebook file. A third-party data science module needs to be imported in a previously cell. Once this cell is run typing in the module name or module alias followed by a ```.```, pressing the tab ```↹``` key will display the list of identifiers from the module:

![139_img](./images/139_img.png)

The tab ```↹``` key can be pressed after inputting some code prefix. This will display completion options available that have the code prefix. In this case the code prefix was np.a and the command np.array has this code prefix:

![141_img](./images/141_img.png)

Inputting a function name with open parenthesis and pressing shift ```⇧``` and the tab ```↹``` key will display the functions docstring as a popup balloon:

![140_img](./images/140_img.png)

When code cells are run, a number displays to the left hand side of the cell (this number is analogous to the numbers shown in the console when running Python code or a Python script file) and indicates the number of cells ran in the Python kernel:

![077_jupyterlab](./images/077_jupyterlab.png)

The Kernel can be restarted in an interactive notebok by selecting Kernel. Then Restart Kernel and Run All Cells:

![151_img](./images/151_img.png)

Then select Restart:

![152_img](./images/152_img.png)

Notice now each cell is ran in numeric order:

![153_img](./images/153_img.png)

JupyterLab has a Variable Inspector extension that can be viewed in an interactive notebook by right clicking blank space in the notebook file and selecting open Variable Inspector:

![135_img](./images/135_img.png)

This opens in a new tab which can be repositioned:

![136_img](./images/136_img.png)

![137_img](./images/137_img.png)

This Variable Inspector is quite limited with respect to the Variable Explorer found within Spyder.

To close JupyterLab, close the tab in the browser. In the mambaforge prompt you will notice that the server is still running.

![078_jupyterlab](./images/078_jupyterlab.png)

The server runs in an infinite loop. To end it press ```Ctrl``` + ```c```:

![079_jupyterlab](./images/079_jupyterlab.png)

If the ```.ipynb``` file is opened in notepad. The nodejs script can be viewed directly.

![138_img](./images/138_img.png)

The nodejs code can be seen to enclose the Python code. Plotting libraries such as plotly take Python syntax from the user and output nodejs code which is used to display the interactive plot.

## The Visual Studio Code IDE

A similar Python environment can be setup for Visual Studio Code:


```
mamba create -n vscode-cf
mamba activate vscode-cf
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
mamba install -c conda-forge nodejs ipywidgets 
mamba install -c conda-forge plotly dash
mamba install -c conda-forge notebook
```

Visual Studio Code can then be installed either from the Windows Application (```.exe```) available on the [Visual Studio Code website](https://code.visualstudio.com/download). It is also available as a snap package in the Ubuntu Store:

![155_img](./images/155_img.png)

Launch the Windows Installer:

![156_img](./images/156_img.png)

Accept the License Agreement and select Next:

![157_img](./images/157_img.png)

Install in the default location and select Next:

![158_img](./images/158_img.png)

Select Next:

![159_img](./images/159_img.png)

Select Next:

![160_img](./images/160_img.png)

Select Install:

![161_img](./images/161_img.png)

Select Finish:

![162_img](./images/162_img.png)

Once installed, launch Visual Studio Code from the Start Screen or the mambaforge prompt by inputting:

```
mamba activate vscode-cf
code
```

![163_img](./images/163_img.png)

Select your desired colour scheme:

![164_img](./images/164_img.png)

To the left select extensions and then select the Python Extension and select Install:

![165_img](./images/165_img.png)

![166_img](./images/166_img.png)

Visual Studio Code requires a folder for each project. Open file explorer and create a new folder:

![167_img](./images/167_img.png)

In Visual Studio Code, select the files tab and select Open Folder. Select the folder just created:

![168_img](./images/168_img.png)

![169_img](./images/169_img.png)

You will be asked for permissions. Select Yes, I trust the authors:

![170_img](./images/170_img.png)

Select New File and create a Python Script file with the ```.py``` file extension:

![171_img](./images/171_img.png)

Open the file. To the bottom right you will see your Python interpretter. In this case the correct Python interpretter was selected.

![172_img](./images/172_img.png)

In other cases you may need to change the Python interpretter. To change this to the ```vscode-cf``` press ```ctrl```, ```⇧``` and ```p``` to open up the command palette. Search for interpretter and select Python: Select Interpretter:

![173_img](./images/173_img.png)

Select the ```vscode-cf``` mamba environment:

![174_img](./images/174_img.png)

Code auto-completion works better in Visual Code than in the other IDEs with an out of the way popup balloon displaying a list of identifiers with the prefix typed:

![175_img](./images/175_img.png)

A docstring popup balloon also displays when a function is input with open parenthesis:

![176_img](./images/176_img.png)

This also works correctly with Python inbuilt modules:

![177_img](./images/177_img.png)

![178_img](./images/178_img.png)

And third-party datascience libraries:

![179_img](./images/179_img.png)

![180_img](./images/180_img.png)

A script file can be run by selecting the run script button:

![181_img](./images/181_img.png)

To the bottom a Terminal should display. In the Python Terminal, Hello World displays. Multiple Terminals can be opened for Windows PowerShell and other programming languages. The Terminal can be resized vertically using the horizontal slider.

![182_img](./images/182_img.png)

For an automatic plot to display when executing a script, the script must include the function 

```
plt.show
```

![183_img](./images/183_img.png)

Visual Studio Code also has a Variables tab. This is unfortunately only available when the script file is ran using Interactive Mode:

![184_img](./images/184_img.png)

Selecting run cells within a script file opens an interactive window to the right hand side:

![185_img](./images/185_img.png)

Plots display inline in the interactive mode:

![186_img](./images/186_img.png)

The Variables can be clicked into to be explored in more detail:

![187_img](./images/187_img.png)

Visual Studio Code can also be used to work with an Interactive Python Notebook. Select New File and create an Interactive Python Notebook file with the ```.ipynb``` file extension:

![188_img](./images/188_img.png)

![189_img](./images/189_img.png)

![190_img](./images/190_img.png)

![191_img](./images/191_img.png)

## Removing a Python Environment

Now multiple Python environments have been created. They can be listed using:

```
mamba env list
```

The environments are listed and the currently selected one is indicated with a ```*```:

![080_jupyterlab](./images/080_jupyterlab.png)

Another environment called ```corrupted``` can be created and once it is created the Python environments can be relisted:

```
mamba create -n corrupted
mamba env list
```

![081_jupyterlab](./images/081_jupyterlab.png)

The corrupted environment can be removed using:

```
mamba env remove -n corrupted
```

![082_jupyterlab](./images/082_jupyterlab.png)

This corrupted Python environment is now removed:

![083_jupyterlab](./images/083_jupyterlab.png)

Return to:

[Home](../../../../)
