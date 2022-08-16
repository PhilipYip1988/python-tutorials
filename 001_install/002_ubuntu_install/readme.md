# JupyterLab IDE Setup on Ubuntu 22.04 LTS

## System Requirements

To install Miniconda you will need a PC that satisfies the following system requirements:

* Modern Linux Kernel Version 5.8 or Later: Ubuntu 22.04 LTS (Kernel 5.15), Mint 21 (Kernel 5.15), Fedora 36 (Kernel 5.17)
* 6th Generation Intel i5 Processor or Later
* 8 GB DDR3 RAM or Superior
* 250 GB SSD or Superior
* Chromium should be installed from the Distros Software Store

The performance will be very poor if these system requirements are not satisfied.

## Miniconda Installation

Download the Linux 64 Bit Shell Script (.sh file extension) from the Miniconda website:

[Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Open up the Downloads folder and right click empty space and select Open in Terminal:

![001_terminal](./images/001_terminal.PNG)

Right click the .sh file and select rename:

![002_bash_install](./images/002_bash_install.PNG)

Copy the file name including the .sh extension:

![003_bash_install](./images/003_bash_install.PNG)

Input:

```
bash 
```

Then paste in the file name:

![004_bash_install](./images/004_bash_install.PNG)

This should look like:

```
bash Miniconda3-latest-linux-x86_64.sh
```

![005_bash_install](./images/005_bash_install.PNG)

Hold down enter ```↵``` to scroll through the license agreement:

![006_bash_install](./images/006_bash_install.PNG)

To proceed you will need to accept the license agreement:

![007_bash_install](./images/007_bash_install.PNG)

Input

```
yes
```

![008_bash_install](./images/008_bash_install.PNG)

Press enter ```↵``` to install Miniconda in the default location:

![009_bash_install](./images/009_bash_install.PNG)

**In the next screen no is automatically selected. Pressing ```↵``` will install Miniconda without initializing it. This means there is no entry in the ```.bashrc``` file making Miniconda unusable.**

![010_bash_install](./images/010_bash_install.PNG)

Instead input:

```
yes
```

![011_bash_install](./images/011_bash_install.PNG)

Miniconda will now be installed and initialized. Close down the terminal and reopen it. This will refresh the Terminal with the updated ```conda``` commands from the ```.bashrc``` file.


## Updating conda base env

When the terminal is opened. It will be prefixed with ```(base)``` which means the conda *base* environment is selected. The *base* environment is a special conda environment which contains the ```conda``` package manager. On Anaconda the ```base``` conda environment also contains a Python distribution containing Python, a multitude of IDEs and a multitude of data science libraries. On Miniconda the ```base``` conda environment is otherwise empty:

![013_conda_base](./images/013_conda_base.PNG)

Use the command:

```
conda update --all
```

to update the conda package manager and all packages in the conda base environment from the official ```conda``` channel. This is the channel maintained by the Anaconda company.

![014_conda_base_update](./images/014_conda_base_update.PNG)

A list of changes will be displayed:

![015_conda_base_update](./images/015_conda_base_update.PNG)

Input: 
```
y
```
to proceed.

![016_conda_base_update](./images/016_conda_base_update.PNG)

The conda base environment will then be updated.

## Creating a jupyterlab-cf conda environment
### creating a conda environment
We will now use the command:
```
conda create -n jupyterlab-cf

```
to create a new conda environment to install the latest version of JupyterLab from the conda-forge community channel.

![017_create_conda_env](./images/017_create_conda_env.PNG)

Details about the conda environment will be given:

![018_create_conda_env](./images/018_create_conda_env.PNG)

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

![019_activate_conda_env](./images/019_activate_conda_env.PNG)

Now the *jupyterlab-cf* conda environment is activated as indicated by the prompt beginning with ```(jupyterlab-cf)```:

![020_activate_conda_env](./images/020_activate_conda_env.PNG)

This means any package manipulation will now be carried out in the conda environment *jupyterlab-cf* and the *base* conda environment will be uninfluenced.

### install jupyterlab

To install the latest version of JupyterLab from the community conda-forge channel use:

```
conda install -c conda-forge jupyterlab
```

The ```-c conda-forge``` means the *conda-forge* community channel is selected opposed to the *conda* channel maintained by the Anaconda company.

![021_installing_packages](./images/021_installing_packages.PNG)

The packages for JupyterLab and its mandatory dependencies will be listed.

![022_installing_packages](./images/022_installing_packages.PNG)

Input:

```
y
```
in order to proceed.

![023_installing_packages](./images/023_installing_packages.PNG)

The packages will be downloaded and installed to the *jupyterlab-cf* conda environment:

![024_installing_packages](./images/024_installing_packages.PNG)

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

![025_launching_jupyterlab](./images/025_launching_jupyterlab.PNG)

Unfortunately on Ubuntu as the browser opens you may get:

![026_launching_jupyterlab](./images/026_launching_jupyterlab.PNG)

This error message displays dueto the elevated security permissions of a browser snap package.

You can copy and paste the address from the terminal to your browser address bar to open JupyterLab.

![027_launching_jupyterlab](./images/027_launching_jupyterlab.PNG)

![028_launching_jupyterlab](./images/028_launching_jupyterlab.PNG)

![029_launching_jupyterlab](./images/029_launching_jupyterlab.PNG)

To the left hand side you have the Files tab where you can open a file. Files created in JupyterLab should always be opened in the Files tab within JupyterLab and not the File Explorer within Linux:

![030_jupyterlab_files](./images/030_jupyterlab_files.PNG)

Once a file is open you can use the navigation pane to have a look at its headings/bookmarks.

![031_jupyterlab_navigation_pane](./images/031_jupyterlab_navigation_pane.PNG)

You can use the launcher button on the left to open a new launcher and from the launcher, create a new text, markdown or notebook file:

![032_jupyterlab_launcher](./images/032_jupyterlab_launcher.PNG)

A JupyterLab server will run using an infinite loop in the terminal. You can however open another instance of a Terminal to do something else whiole running JupyterLab. 

To close down JupyterLab, close all open JupyterLab windows within the browser and then in the terminal press:

```Ctrl``` + ```c```

Then input:

```y```

to confirm you want to shut down the JupyterLab server.

![033_jupyterlab_close](./images/033_jupyterlab_close.PNG)

The prompt will return and you can close the Terminal:

![034_jupyterlab_close](./images/034_jupyterlab_close.PNG)

Return to:

[Home](../../../../)
