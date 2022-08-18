# JupyterLab IDE Setup on Windows 10 or Windows 11

## System Requirements

To install Miniconda you will need a PC that satisfies the following system requirements:

* Windows 11 or Windows 10 64 Bit
* 6th Generation Intel i5 Processor or Later
* 8 GB DDR3 RAM or Superior
* 250 GB SSD or Superior

The performance will be very poor if these system requirements are not satisfied.

## Miniconda Installation

Download the Windows 64 Bit Application (.exe file extension) from the Miniconda website:

[Miniconda](https://docs.conda.io/en/latest/miniconda.html)

![001_Miniconda_Download](./images/001_Miniconda_Download.PNG)

Open up the Downloads folder and double click the Application to begin the installer:

![002_Miniconda_Install](./images/002_Miniconda_Install.PNG)

Select Next:

![003_Miniconda_Install](./images/003_Miniconda_Install.PNG)

Read the License Agreement and select I Agree:

![004_Miniconda_Install](./images/004_Miniconda_Install.PNG)

Select Just Me (recommended):

![005_Miniconda_Install](./images/005_Miniconda_Install.PNG)

Use the default path. This will be in ```%UserProfile$\Miniconda3```. Note that ```%UserProfile$``` maps to ```C:\Users\UserName```. In my case as my username is ```Philip``` it maps to ```C:\Users\Philip```:

![006_Miniconda_Install](./images/006_Miniconda_Install.PNG)

On the next screen you have the option to add the conda (base) environment to the Windows Environmental Variables Path. 

![007_Miniconda_Install](./images/007_Miniconda_Install.PNG)

Adding to the Windows Environmental Path will make the Miniconda conda (base) environment accessible from the Windows Terminal. This is useful when running Python from this (base) conda environment when using an external application. 

![008_Miniconda_Install](./images/008_Miniconda_Install.PNG)

The Windows Environmental Path can be accessed by right clicking the Start button and selecting System:

![009_Miniconda_Install](./images/009_Miniconda_Install.PNG)

Then selecting Advanced System Settings:

![010_Miniconda_Install](./images/010_Miniconda_Install.PNG)

Then selecting Environmental Variables:

![011_Miniconda_Install](./images/011_Miniconda_Install.PNG)

Then highlighting the Path and selecting Edit:

![012_Miniconda_Install](./images/012_Miniconda_Install.PNG)

The Windows Environmental Variables Path without the Miniconda (base) env added:

![013_Miniconda_Install](./images/013_Miniconda_Install.PNG)

The Windows Environmental Variables Path without the Miniconda (base) env added:

![014_Miniconda_Install](./images/014_Miniconda_Install.PNG)

Includes the following 5 entries:

```
%UserProfile%\miniconda3
%UserProfile%\miniconda3\Library\mingw-w64\bin
%UserProfile%\miniconda3\Library\usr\bin
%UserProfile%\miniconda3\Library\bin
%UserProfile%\miniconda3\Scripts
```

Select Next:

![015_Miniconda_Install](./images/015_Miniconda_Install.PNG)

And Finish:

![016_Miniconda_Install](./images/016_Miniconda_Install.PNG)

## Updating conda base env

A Start Menu Anaconda folder will be created:

![017_Anaconda_Powershell_Prompt](./images/017_Anaconda_Powershell_Prompt.PNG)

In this folder you will see the ```Anaconda Powershell Prompt``` and ```Anaconda Prompt```. You should use the ```Anaconda Powershell Prompt```, which uses Windows Powershell opposed to the ```Anaconda Prompt``` which uses the depreciated CMD.  

When the Anaconda Powershell Prompt is opened. It will be prefixed with ```(base)``` which means the conda *base* environment is selected. The *base* environment is a special conda environment which contains the ```conda``` package manager. 

* In Anaconda the ```base``` conda environment also contains a Python distribution containing Python, a multitude of IDEs and a multitude of data science libraries. 

* In Miniconda the ```base``` conda environment is otherwise empty.

![018_Anaconda_Powershell_Prompt](./images/018_Anaconda_Powershell_Prompt.PNG)

Use the command:

```
conda update --all
```

to update the conda package manager and all packages in the conda base environment from the official ```conda``` channel. This is the channel maintained by the Anaconda company.

![019_Anaconda_Powershell_Prompt](./images/019_Anaconda_Powershell_Prompt.PNG)

A list of changes will be displayed:

![020_Anaconda_Powershell_Prompt](./images/020_Anaconda_Powershell_Prompt.PNG)

Input: 
```
y
```
to proceed.

The conda base environment will then be updated.

## Creating a jupyterlab-cf conda environment
### creating a conda environment
We will now use the command:
```
conda create -n jupyterlab-cf

```
to create a new conda environment to install the latest version of JupyterLab from the conda-forge community channel.

![021_Setting_Up_conda_env](./images/021_Setting_Up_conda_env.PNG)

Details about the conda environment will be given:

![022_Setting_Up_conda_env](./images/022_Setting_Up_conda_env.PNG)

Input:

```
y
```
in order to proceed. The conda environment is now created and you can view details in the terminal about the conda environment such as its physical file location which you can explorer in Files.

### activating a conda environment

The conda environment is now created but the *base* conda environment is still selected as indicated by the prompt beginning with ```(base)```. To activate the *jupyterlab-cf* conda environment use:

```
conda activate jupyterlab-cf
```

![023_Setting_Up_conda_env](./images/023_Setting_Up_conda_env.PNG)

Now the *jupyterlab-cf* conda environment is activated as indicated by the prompt beginning with ```(jupyterlab-cf)```:

![024_Setting_Up_conda_env](./images/024_Setting_Up_conda_env.PNG)

This means any package manipulation will now be carried out in the conda environment *jupyterlab-cf* and the *base* conda environment will be uninfluenced.

### install jupyterlab

To install the latest version of JupyterLab from the community conda-forge channel use:

```
conda install -c conda-forge jupyterlab
```

The ```-c conda-forge``` means the *conda-forge* community channel is selected opposed to the *conda* channel maintained by the Anaconda company.

![025_Setting_Up_conda_env](./images/025_Setting_Up_conda_env.PNG)

The packages for JupyterLab and its mandatory dependencies will be listed.

![026_Setting_Up_conda_env](./images/026_Setting_Up_conda_env.PNG)

Input:

```
y
```
in order to proceed.

The packages will be downloaded and installed into the *jupyterlab-cf* conda environment.

![027_Setting_Up_conda_env](./images/027_Setting_Up_conda_env.PNG)

### Installing the Data Science Libraries

It is recommended to install the following data science libraries using:

```
conda install -c conda-forge cython seaborn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy scikit-learn scikit-image
```
You will get similar screens to the above showing the packages to be installed alongside a query prompt to install them.

Installing ```seaborn``` will install a comaptible version of ```numpy```, ```pandas``` and ```matplotlib```.

Installing ```openpyxl```, ```xlrd```, ```xlsxwriter```, ```lxml```, ```sqlalchemy``` will allow you to use the functions within ```pandas``` to read and write files.

Installing ```scikit-learn``` and ```scikit-image``` will give you commonly used machine learning libraries. Other libraries can be installed from the *conda-forge* channel if required.

### Installing JupyterLab Extensions

JupyterLab extensions are written using node javascript. The are also commonly built upon interactive widgets. Install the following:

```
conda install -c conda-forge nodejs ipywidgets 
```
Then the optional extensions can be installed:
```
conda install -c conda-forge jupyterlab-variableinspector ipympl plotly jupyterlab-drawio
```

```jupyterlab-variableinspector``` gives a basic variable explorer.

```ipympl``` gives the ability to use the ```%matplotlib widget``` backend giving interactive matplotlib plots nested as cells. This is still a bit experimental.

```plotly``` gives the ability to use the alternative plotly plotting library.

```jupyterlab-drawio``` gives the ability to create drawio diagrams in JupyterLab. Unfortunately you cannot nest these diagrams into a notebook cell however you can save these diagrams as a static image and display that in a markdown cell.

### Updating the conda environment

You may want to periodically check for any updates to packages in your *jupyterlab-cf* conda environment by first making sure the *jupyterlab-cf* conda environment is updated and then using the following command:

```
conda update -c conda-forge --all
```

## Launching JupyterLab

Ensure the *jupyterlab-cf* conda environment is selected and input:

```
jupyter-lab
```

![028_Launching_JupyterLab](./images/028_Launching_JupyterLab.PNG)

JupyterLab will now launch in your default browser:

![029_JupyterLab](./images/029_JupyterLab.PNG)

To the left hand side you have the Files tab which opens in ```%UserProfile$``` by default. You can use this File Explorer to open a file, create a new file or folder or rename or delete a new file or folder, similar to Windows Explorer. Note however that files created in JupyterLab particularly Markdown Files or Notebook Files should always be opened from the Files tab within JupyterLab and not the File Explorer within Windows:

![030_JupyterLab](./images/030_JupyterLab.PNG)

Once a file is open you can use the navigation pane to have a look at its headings/bookmarks.

![031_JupyterLab](./images/031_JupyterLab.PNG)

You can use the launcher button on the left to open a new launcher and from the launcher, create a new text, markdown or notebook file:

![032_JupyterLab](./images/032_JupyterLab.PNG)

A JupyterLab server will run using an infinite loop in the Anaconda Powershell Prompt. You can however open another instance of the Anaconda Powershell Prompt to do something else while running JupyterLab. 

![033_JupyterLab_Close](./images/033_JupyterLab_Close.PNG)

To close down JupyterLab, close all open JupyterLab windows within the browser and then in the Anaconda Powershell Prompt:

```Ctrl``` + ```c```

The prompt will return and you can close the Anaconda Powershell Prompt:

![034_JupyterLab_Close](./images/034_JupyterLab_Close.PNG)

Return to:

[Home](../../../../)