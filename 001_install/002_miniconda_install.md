# Miniconda Conda Environment

In this guide we will install the latest version of JupyterLab using Miniconda.

## Miniconda Install

### Windows 11 or Windows 10

Download the 64 Bit Windows Application (.exe file extension) from:

[Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Install Anaconda or Miniconda using the setup wizard. During installation, select Just Me (recommended) and Install in the default destination folder. You can optionally Add Miniconda3 to my PATH environment variable.

In the Start Menu there will be a Miniconda folder and the Anaconda PowerShell Prompt. Do not use the Anaconda Prompt which uses the legacy CMD that is now depreciated. 

### Ubuntu 22.04 LTS

Download the 64 Bit shell script (.sh file extension) from:

[Miniconda](https://docs.conda.io/en/latest/miniconda.html)

Once downloaded, go to the Downloads folder and right click an empty area of the folder and select Open in Terminal.

The shell script can then be launched using the ```bash``` command followed by the name of the ```.sh``` file. In this case:

```bash Miniconda3-latest-Linux-x86_64.sh```

Hold down ```↵``` to scroll through the license agreement. Input ```yes``` and press ```↵``` in order to accept the license agreement. The default location will automatically be selected, press ```↵``` in order to install Miniconda here. **The next screen unfortunately will have ```No``` selected! Do not press ```↵``` as this will install Miniconda without initializing it, leaving it in an unusable state!** Input ```yes``` and then  press ```↵```. This will initialize Miniconda refreshing the .bashrc file. Close any open terminals and open a new terminal. This new terminal will reference the updated .bashrc file which has conda initialized and there will be a ```(base)``` prefix to the prompt.

```(base) user@pc:```

## JupyterLab Install

In Windows use the Anaconda PowerShell Prompt. The prompt will have the form:

```(base) PS C:\Users\UserName>```

In Ubuntu use the Anaconda PowerShell Prompt. The prompt will have the form:

```(base) user@pc:```

Otherwise, we can treat the above as identical.

```(base)``` means the *base* conda environment is selected.

### Creating a conda environment

In order to install JupyterLab. Create a conda environment called *jupyterlab-cf*:

```
conda create -n jupyterlab-cf
```

### Activating a conda environment

Activating the conda-environment means you are selecting the conda environment. Any commands to add/remove/update packages will now apply to the selected conda environment and any commands to launch an IDE will launch it from the selected conda environment. Activate the conda environment using:

```
conda activate jupyterlab-cf
```

Notice that now the the prompt is of the form:

```(jupyterlab-cf) PS C:\Users\UserName>```

```(jupyterlab-cf) user@pc:```

And ```(jupyterlab-cf)``` means the *jupyterlab-cf* conda environment is selected.

### Install JupyterLab

Install JupyterLab:

```
conda install -c conda-forge jupyterlab
```

Here ```-c conda-forge``` is an abbreviation for ```--channel conda-forge``` and indicates that we are installing JupyterLab from the community (developer) channel ```conda-forge``` opposed to the ```conda``` channel maintained by the Anaconda Company.

### Install Data Science Libraries

Install the Datascience libraries and commonly used libraries which are reference for reading/writing data from/to files:

```
conda install -c conda-forge cython seaborn scikit-learn scikit-image sympy openpyxl xlrd xlsxwriter lxml sqlalchemy
```

### Install Interactive Python Widgets

Install nodejs and interactive Python widgets:

```
conda install -c conda-forge nodejs ipywidgets 
```

### Install Optional Extensions

Install optional JupyterLab extensions:

```
conda install -c conda-forge jupyterlab-variableinspector ipympl plotly jupyterlab-drawio

```

### Update Packages

To later update this conda environment with the latest packages from conda-forge, activate the ```jupyterlab-cf``` conda environment and then use:

```
conda update -c conda-forge --all
```

### Launch JupyterLab

### Windows 
In Windows open the Anaconda PowerShell Prompt and activate the ```jupyterlab-cf``` conda environment. Then use:

```
jupyter-lab
```

This will launch JupyterLab in the Microsoft Edge Browser. You can change the default browser to Google Chrome to instead launch JupyterLab in this browser.

### Ubuntu

#### Configuration File

In Ubuntu, browsers are now sandboxed snap applications and JupyterLab is unfortunately configured by default to seek a hidden file that snap applications aren't allowed access to. We need to create a configuration file to bypass this. Input:

```
jupyter notebook --generate-config
```

The location of the file will be shown in the terminal. This should be ```~/.jupyter/jupyter_notebook_config.py``` which is a hidden folder. Enable hidden files to view this.

Remove the comment ```#``` in line 157 and update the line to:

```
c.NotebookApp.browser = 'Chromium'
```

Remove the comment ```#``` in line 543 and update the line to:

```
c.NotebookApp.use_redirect_file = False
```

#### Launching JupyterLab
In Ubuntu open the Terminal and activate the ```jupyterlab-cf``` conda environment. Then use:

```
jupyter-lab
```

This will launch JupyterLab in Chromium snap browser.
