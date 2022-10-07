# YouTube Tutorial Video

[Installing Mambaforge on Windows 11 YouTube](https://www.youtube.com/watch?v=W1KQl3_VFF8)

# System Requirements

The PC should match or exceed the following system requirements:

* Windows 11 (22H2) or Windows 10 (22H2) 64 Bit
* 6th Generation Intel i5 Processor or Later
* 8 GB DDR3 RAM or Superior
* 250 GB SSD or Superior
* Google Chrome or Microsoft Edge Browser

The performance for Python will be very poor if these system requirements are not satisfied.

# Mambaforge Install

Mambaforge can be downloaded from the Mambaforge GitHub repository. Make sure to download Mambaforge and not Miniforge:

[Mambaforge](https://github.com/conda-forge/miniforge/releases)

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

**Mambaforge can optionally be added to the Windows Environment Variable Path.** This makes the ```base``` Python environment accessible via the Windows Terminal. This allows third party applications to accessing Python from the Windows Terminal. Such a use case is normally more advanced, for example a C++ IDE that is configured by default to access the Windows Terminal will also be able to invoke a Python Script if Mambaforge is added to the WIndows Environmental Variables Path.

Note that in most regular use scenarios the Mambaforge Prompt should be preferentially used to interact with Python instead of the Windows Terminal. The Mambaforge Prompt is similar to the Windows Terminal but is optimised to work with multiple Python environments and not hard coded to the single base environment provided in the Windows Environmental Variables Path like in the case of the Windows Terminal. The Mambaforge Prompt can be used to install packages in Python environments and launch IDEs installed in the Python environments. 

![006_mambaforge_install](./images/006_mambaforge_install.png)

![007_mambaforge_install](./images/007_mambaforge_install.png)

Once the decision to add Mambaforge to the Windwos Environmental Path or not is configured. Select Install:

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

# Python Environments

It is generally advised to create seperate Python environment from ```base``` which is essentially a subinstallation. In the mambaforge folder, there is a subfolder called ```envs```:

```
%UserProfile\mambaforge\envs
```

![025_envs](./images/025_envs.png)

By default this is empty:

![026_envs](./images/026_envs.png)

## Installing the Spyder IDE

To create a Python Environment use the command:

```
mamba create -n spyder-cf
```

![027_envs](./images/027_envs.png)

Where ```-n``` is an abbreviation for name and ```spyder-cf``` is the name of the Python environment. In this case the name is spyder-c indicating we are going to install the latest version of spyder from the ```conda-forge``` channel.

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

## Installing the Data Science Libraries

Currently the installation contains only mandatory dependencies, allowing Spyder to work with Python and lacks the data science libraries commonly used with Spyder. These can be installed using:

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

## Launching the Spyder

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

# Understanding Datascience Library Imports

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

# The Spyder IDE Overview

In Python prefixing a line with a ```#``` turns it into a comment. In Spyder prefixing a line with ```#%%``` turns it into a new cell. A script file can be run using the run button or each cell can be run individually using the run cell or run cell and move onto the next cell button:

![059_envs](./images/059_envs.png)

The variables created ```x``` and ```y``` are displayed in Spyders Variable Explorer. The value can be double clicked and collections such as the arrays created above can be explored to view them in more detail.

![060_envs](./images/060_envs.png)

A basic command can be used to create a plot. By default plots display in the Plots pane as a static image however the backend can be changed to Automatic to enable an itneractive plot in its own window. 

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

An individual line of code from a script can be highlighted and ran in the console by selcting run seleciton or current line:

![066_envs](./images/066_envs.png)

# JupyterLab IDE Overview

Another Python environment will be created for the JupyterLab IDE. The JupyterLab IDE is a browser based IDE and has the same optional dependencies as Spyder. because it is browser based, its functionality can be extended with interactive Python widgets ```ipywidgets``` and the browser based ```plotly``` plotting library. These extensions require ```nodejs```. An optional variable inspector is also available however is limited in comparison to Spyder.

```
mamba create -n jupyterlab-cf
mamba activate jupyterlab-cf
mamba install -c conda-forge jupyterlab
mamba install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
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

Whhen first launched, there will be a prompt to build JupyterLab, select Build:

![068_jupyterlab](./images/068_jupyterlab.png)

This will take a while. When finished select Save and Reload:

![069_jupyterlab](./images/069_jupyterlab.png)

JupyterLab has a file explorer to the left hand side where you can navigate to your Documents folder. A series of tabs are available to the right. A new tab can be opened using the plus button. A new tab displays the launcher which can be used to create a new Interactive Python Notebook (```.ipynb``` file extension):

![070_jupyterlab](./images/070_jupyterlab.png)

To the left in the file explorer, right click the file and select rename. Once again the file name should be named following the rules of Python object names.

![071_jupyterlab](./images/071_jupyterlab.png)

The notbook consists of a series of cells:

![072_jupyterlab](./images/072_jupyterlab.png)

These can be markdown cells or code cells:

![073_jupyterlab](./images/073_jupyterlab.png)

We can create a markdown heading and run the cell:

![074_jupyterlab](./images/074_jupyterlab.png)

The heading will now display under the notebooks bookmarks:

![075_jupyterlab](./images/075_jupyterlab.png)

We can now create a code cell:

![076_jupyterlab](./images/076_jupyterlab.png)

When code cells are run, a number displays to the left hand side of the cell (this number is analogous to the numbers shown in the Spyder console) and indicates the number of cells ran in the Python kernel:

![077_jupyterlab](./images/077_jupyterlab.png)

To close JupyterLab, close the tab in the browser. In the mambaforge prompt you will notice that the server is still running.

![078_jupyterlab](./images/078_jupyterlab.png)

The server runs in an infinite loop. To end it press ```Ctrl``` + ```c```:

![079_jupyterlab](./images/079_jupyterlab.png)

# Python Environments Continued

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
