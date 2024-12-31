# JupyterLab IDE Windows Setup

JupyterLab is a browser based IDE:

## Miniforge Installation and Setup

The conda package manager will be used to create a new environment for JupyterLab. In order to use conda, Miniforge needs to be installed and preferably initialised. This was covered in:

[Miniforge Install and Initialisation](../spyder_install_windows/readme.md#miniforge-installation)

## Update conda

The purpose of the `base` environment is to use the conda package manager to install packages in other Python environments. Before using the conda package manager, the conda package manager should be updated to the latest version:

```powershell
conda update conda
```

## JupyterLab (Python Kernel)

JupyterLab is mainly used with Python. To create a new environment for JupyterLab which includes the Python kernel, the following command can be used:

```python
conda create -n jupyter-env jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt isort autopep8 ruff black jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker jupyterlab-spreadsheet-editor
```

`jupyterlab` is the IDE itself. `seaborn` has `numpy`, `pandas` and `matplotlib` as dependencies and are the scientific libraries. `scikit-learn` is used for machine learning. `pyarrow`, `openpyxl`, `xlrd`, `xlsxwriter`, `lxml`, `sqlalchemy`, `tabulate` are for various file pandas formats. `pyqt` is for matplotlib's interactive backend and `ffmpeg` is for saving matplotlib animations.

`jupyterlab-variableinspector`, `jupyterlab_code_formatter`, `jupyterlab-spellchecker`, `jupyterlab-spreadsheet-editor` are common extensions for JupyterLab. In order for extensions to be installed, nodejs needs to be installed. The JupyterLab IDE and extensions are written in nodejs, which is a programming language used for web content. Knowledge of nodejs is not required to use Python with JupyterLab.

`-n` means name and `jupyter-env` is the name of the Python environment. Specifying an environment using `-n` means changes to that environment will be made opposed to `base` which is the currently activate environment.

## JupyterLab (R Kernel)

Jupyter is a web based IDE designed for multiple data science programming languages. Jupyter is an acronym for Julia Python et R. The conda package manager, is a general purpose data science package manager and on Windows supports most Python packages and R packages. An environment with the Python and R kernels can be setup:

```powershell
conda create -n jupyter-r-env jupyterlab jupyter cython seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly pyqt isort autopep8 ruff black ipympl r-irkernel jupyter-lsp-r r-tidyverse r-ggthemes r-palmerpenguins r-writexl jupyterlab-variableinspector jupyterlab_code_formatter jupyterlab-spellchecker jupyterlab-spreadsheet-editor
```

```powershell
conda activate jupyter-r-env
```

```powershell
jupyter-lab --kernel=r
```

## Julia (Jupyter Kernel)

Unfortunately Julia isn't available on conda-forge and has to be installed using the Windows Store:

Many Linux/BSD/Unix package managers ship broken and/or significantly out of date versions of Julia. Please use juliaup or download the official binaries instead.

Once installed, open the Windows Terminal and input:

```powershell
julia
```

To install the Julia Kernel input:

```powershell
using Pkg
Pkg.add("IJulia")
```

Activate the environment using:

```powershell
conda activate jupyter-r-env
```

Launch JupyterLab using the Julia Kernel:

```powershell
jupyter-lab --kernel=julia
```

## Script Editor

## Markdown

## Interactive Python Notebook