# Installing Anaconda

## About Anaconda

The Anaconda Python distribution comes with its own base (otherwise known as an alternative root) Python environment that contains:

* **Python**
* **Python Standard Libraries**
* **The conda Package Manager**
* Third Party Libraries:
  * numpy
  * pandas
  * matplotlib
  * seaborn
  * ⁝
* Third-party IDEs:
  * Spyder
  * Jupyter
    * JupyterLab
    * Jupyter Notebook
    * Jupyter QTConsole
    * Jupyter Console
* Third-party formatters:
  * autopep8
  * isort
  * black

Miniconda is a stripped down version of Anaconda containing only the components above highlighted in bold, in its (base) Python environment. 

## About Python Environments

Anaconda can be used to create a custom Python environment. A Python environment is essentially a subinstallation of Python where a custom set of packages can be installed, without breaking the functionality of the (base) Python environment.

The Miniconda (base) Python environment has the bare essentials required for creating Python environments. Typically it is used to create custom Python environments for IDEs. 

## About Package Managers

Python has its own package manager Python Install Package (pip) which is strictly for Python packages. 

For datascience projects, the more powerful conda package manager is preferred as it can be used to install the Python packages used for datascience projects, in addition to their non-Python dependencies. These include example codecs as well as dependencies for hardware acceleration. 

conda can also be used to install packages from other programming languages which are often used directly or indirectly in conjunction with Python. The popular **Jupyter** project for example is an abbreviation for **Ju**lia **Pyt**hon **e**t **R**.

For a conda Python environment:

```powershell
conda install package
``` 

Should be used in preference of 

```python
pip install  package
```

where possible.

winget is a general purpose Windows Package Manager that is Windows only and will be used to install Anaconda on Windows. winget and conda are both package managers and should not be confused with one another. conda is a cross-platform package manager specialised for datascience packages.

## About Channels

The ```conda``` package manager has two channels:

* ```anaconda```
* ```conda-forge``` (community)

The "default" channel for Anaconda and Miniconda is the ```anaconda``` channel by default.

Historically the ```anaconda``` channel was called "conda" which created a small level of confusion with the channel and the package manager and the term "main" was used instead of "default".

The ```anaconda``` channel is maintained by the Anaconda company.

The ```conda-forge``` channel is maintained directly by developers from the Python community (a better name for the channel would be "community").

The Anaconda company only test a subset of the more commonly used Python packages for stability with the Anaconda Python Distribution and because it takes time to test these packages further, the versions they offer may be older than the latest versions on the ```conda-forge``` community channel. 

## Avoid

The ```base``` Python environment should only use packages from the ```anaconda``` channel and will become unstable when packages from the ```conda-forge``` community channel are installed. 

For packages only available on the ```conda-forge``` channel it is recommended to use the ```conda``` package manager to create a Python environment for custom configurations.

## Removing Old Installations

Anaconda should be installed on a Windows 11 PC that has no previous Python installations. 

If Python installations are present they should be uninstalled. Note that uninstallation leaves behind a large number of configuration files that often results in problematic setting persisting after a reinstall. For best results it is recommended to purge these configuration files. For more details see [Uninstall](./uninstall.md).

## WinGet

On a clean install of Windows 11, Anaconda can be installed using the Windows Package Manager WinGet. 

Before using WinGet, the Microsoft Store, App Installer and Windows Terminal should be updated. Open up the Microsoft Store, select Library and then select Get Updates:

<img src='images_install/img_001.png' alt='img_001' width='450'/>

Note: When WinGet is used with Terminal (Non-Admin) it will install a Program for the Current User. When WinGet is used with Terminal (Admin) it will install a Program for All Users which is not recommended for Anaconda.

Right click the Start Menu and select Terminal (Non-Admin):

<img src='images_install/img_002.png' alt='img_002' width='200'/>

The Terminal uses the PowerShell programming language by default.

<img src='images_install/img_003.png' alt='img_003' width='350'/>

The Prompt gives details about the programming language and current working directory:

```powershell
PS ~>
```

The environmental variable %USERPROFILE% (used within file explorer) maps to the location of your User Profile, in this case C:\\Users\\Phili and this is often represented using ```~``` in PowerShell.

Enter the command:

```powershell
WinGet search Anaconda
```

This should return:

<img src='images_install/img_004.png' alt='img_004' width='350'/>

This gives details about the programs available from Anaconda that can be installed on WinGet.

```
PS ~> winget search anaconda
Name       Id                  Version     Source
--------------------------------------------------
Miniconda3 Anaconda.Miniconda3 py39_4.10.3 winget
Anaconda3  Anaconda.Anaconda3  2023.09     winget
PS ~>
```

Anaconda is up to date however the version of Miniconda offered is outdated, an updated version should be added soon. [WinGet Packages GitHub #138230](https://github.com/microsoft/winget-pkgs/pull/138230). In the meantime better results will occur when using the latest installer which can be obtained from the Miniconda website [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/). 

Anaconda can be installed using:

```powershell
winget install Anaconda.Anaconda3
```

This will install Anaconda. The operation is only complete when a new prompt displays. This will display:

```
PS ~> winget install Anaconda.Anaconda3
Found Anaconda3 [Anaconda.Anaconda3] Version 2023.09
This application is licensed to you by its owner.
Microsoft is not responsible for, nor does it grant any licenses
to, third-party packages.
Successfully verified installer hash
Starting package install...
Successfully installed
PS ~>
```

The default install location will be in:

```
%USERPROFILE%\Anaconda3
```

<img src='images_install/img_005.png' alt='img_005' width='450'/>


Other Windows Environmental Variables include:

|Environmental Variable|Location
|---|---|
|%USERPROFILE%|C:\\Users\\Phili|
|%ONEDRIVE%|C:\\Users\\Phili\\OneDrive|
|%APPDATA%|C:\\Users\\Phili\\AppData\\Roaming|
|%LOCALAPPDATA%|C:\\Users\\Phili\\AppData\\Local|
|%TMP%|C:\\Users\\Phili\\AppData\\Local\\Temp|
|%PROGRAMDATA%|C:\\ProgramData|
|%PROGRAMFILES%|C:\\Program Files|
|%PROGRAMFILES(X86)%|C:\\Program Files (x86)|
|%WINDIR%|C:\\Windows|
|%SYSTEMDRIVE%|C:|

## Windows Environmental Variable Path

When Anaconda is installed using winget, it becomes the users default Python and is added to the Windows Environmental Variables Path. 

When Anaconda or Miniconda are installed using the standalone installer, the Windows Environmental Path is often not modified. This isn't an issue as this tutorial will go through Initialisation of Anaconda or Miniconda for the Windows Terminal.

The Windows Environmental Variables Path can be checked by right clicking the Start Button and selecting System:

<img src='images_install/img_006.png' alt='img_006' width='200'/>

Then Advanced System Settings:

<img src='images_install/img_007.png' alt='img_007' width='350'/>

Then selecting the Advanced tab and Environmental Variables:

<img src='images_install/img_008.png' alt='img_008' width='350'/>

Select Path and then Edit:

<img src='images_install/img_009.png' alt='img_009' width='350'/>

For Anaconda installed using winget the following 5 entries are automatically added. These can optionally be manually added if not present, although a better option is to initialise the Windows Terminal (see below):

```powershell
%USERPROFILE%\Anaconda3
%USERPROFILE%\Anaconda3\Library\mingw-w64\bin
%USERPROFILE%\Anaconda3\Libraryusr\bin
%USERPROFILE%\Anaconda3\Library\bin
%USERPROFILE%\Anaconda3\Scripts
```

For Miniconda:

```powershell
%USERPROFILE%\Miniconda3
%USERPROFILE%\Miniconda3\Library\mingw-w64\bin
%USERPROFILE%\Miniconda3\Libraryusr\bin
%USERPROFILE%\Miniconda3\Library\bin
%USERPROFILE%\Miniconda3\Scripts
```

## Anaconda PowerShell Prompt

The Anaconda3 folder on the Start Menu has two Terminal Based Entries:

* Anaconda PowerShell Prompt
* Anaconda (CMD Shell) Prompt

In general the PowerShell Prompt should be preferenced over the Legacy CMD Prompt:

<img src='images_install/img_025.png' alt='img_025' width='350'/>

Notice that the Anaconda PowerShell Prompt and Windows Terminal look almost identical:

<img src='images_install/img_026.png' alt='img_026' width='350'/>

The subtle difference is the title indicated in red. The prompt in orange is almost the same. However the Anaconda PowerShell Prompt prefixes ```(base)``` which is an indicator meaning the base Python environment is selected. 

Under the hood the Anaconda PowerShell Prompt essentially launches the Windows Terminal with a conda activation script. Note in order to run the script it bypasses a PowerShell Execution Policy. This can be seen if the shortcut location to the Anaconda PowerShell Prompt is examined:

```powershell
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& '~\anaconda3\shell\condabin\conda-hook.ps1' ; conda activate '~\anaconda3' "
```

## Initialising the Windows Terminal

Initialisation is often required for some IDEs that use the Windows Terminal to work correctly for example VSCode.

The Windows Terminal can be initialised directly by using a modified PowerShell Profile that runs the conda activation script. To use this modified profile, the PowerShell Script Execution Policy needs to be set to RemoteSigned which require use of the Anaconda PowerShell Prompt.

To initialise Anaconda in PowerShell. Right click the Windows 11 Start button and open up the **Windows Terminal (Admin)** and change the execution policy:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Then initialise Anaconda:

```powershell
Anaconda3\Scripts\conda init powershell
```

To initialise Miniconda instead use:

```powershell
Miniconda3\Scripts\conda init powershell
```

This will output:

```
(base) PS ~> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
(base) PS ~> Anaconda3\Scripts\conda init powershell
no change     ~\Anaconda3\Scripts\conda.exe
no change     ~\Anaconda3\Scripts\conda-env.exe
no change     ~\Anaconda3\Scripts\conda-script.py
no change     ~\Anaconda3\Scripts\conda-env-script.py
no change     ~\Anaconda3\condabin\conda.bat
no change     ~\Anaconda3\Library\bin\conda.bat
no change     ~\Anaconda3\condabin\_conda_activate.bat
no change     ~\Anaconda3\condabin\rename_tmp.bat
no change     ~\Anaconda3\condabin\conda_auto_activate.bat
no change     ~\Anaconda3\condabin\conda_hook.bat
no change     ~\Anaconda3\Scripts\activate.bat
no change     ~\Anaconda3\condabin\activate.bat
no change     ~\Anaconda3\condabin\deactivate.bat
modified      ~\Anaconda3\Scripts\activate
modified      ~\Anaconda3\Scripts\deactivate
modified      ~\Anaconda3\etc\profile.d\conda.sh
modified      ~\Anaconda3\etc\fish\conf.d\conda.fish
no change     ~\Anaconda3\shell\condabin\Conda.psm1
modified      ~\Anaconda3\shell\condabin\conda-hook.ps1
modified      ~\Anaconda3\Lib\site-packages\xontrib\conda.xsh
modified      ~\Anaconda3\etc\profile.d\conda.csh
modified      ~\OneDrive\Documents\WindowsPowerShell\profile.ps1

==> For changes to take effect, close and re-open your current shell. <==
```

Close the Windows Terminal (Admin) and open up a new Windows Terminal (Non-Admin). The Windows Terminal will now use the new PowerShell profile profile.ps1 found in Documents. It will show the prefix (base) indicating that the (base) Python environment is selected and use of the Windows Terminal and Anaconda PowerShell Prompt will now be equivalent. 

## Updating Anaconda

Open the Anaconda PowerShell Prompt or Windows Terminal. Input:

```powershell
conda deactivate
```

This will deactivate the ```base``` Python environment:

<img src='images_install/img_027.png' alt='img_027' width='350'/>

Then update the ```conda``` package manager using:

```powershell
conda update -c conda --solver=libmamba conda
```

For Anaconda updating the ```conda``` package manager will update the entire Anaconda Python distribution. 

```
(base) PS ~> conda update -c conda --solver=libmamba conda
Collecting package metadata (current_repodata.json): done
Solving environment: done
```

Details about proposed packages to be downloaded will then show:

```
## Package Plan ##

  environment location: ~\anaconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    aiobotocore-2.7.0          |  py311haa95532_0         153 KB
    aiohttp-3.9.0              |  py311h2bbff1b_0         773 KB
    anaconda-cloud-auth-0.1.4  |  py311haa95532_0          39 KB
    anyio-4.2.0                |  py311haa95532_0         238 KB
    astropy-5.3.4              |  py311hd7041d2_0         9.7 MB
    async-lru-2.0.4            |  py311haa95532_0          21 KB
    attrs-23.1.0               |  py311haa95532_0         165 KB
    black-23.11.0              |  py311haa95532_0         382 KB
    bokeh-3.3.4                |  py311h746a85d_0         5.6 MB
    boost-cpp-1.82.0           |       h59b6b97_2          11 KB
    botocore-1.31.64           |  py311haa95532_0         6.9 MB
    brotli-python-1.0.9        |  py311hd77b12b_7         310 KB
    c-blosc2-2.12.0            |       h2f4ed9d_0         222 KB
    ca-certificates-2023.12.12 |       haa95532_0         127 KB
    certifi-2024.2.2           |  py311haa95532_0         162 KB
    cffi-1.16.0                |  py311h2bbff1b_0         303 KB
    click-8.1.7                |  py311haa95532_0         222 KB
    conda-index-0.2.1          |             py_0         164 KB  conda
    constantly-23.10.4         |  py311haa95532_0          33 KB
    contourpy-1.2.0            |  py311h59b6b97_0         218 KB
    cookiecutter-2.5.0         |  py311haa95532_0         159 KB
    cryptography-41.0.7        |  py311h89fc84f_0         1.2 MB
    curl-8.5.0                 |       he2ea4bf_0         156 KB
    cytoolz-0.12.2             |  py311h2bbff1b_0         339 KB
    dal-2023.1.1               |   h59b6b97_48682        26.5 MB
    dask-2023.11.0             |  py311haa95532_0           6 KB
    dask-core-2023.11.0        |  py311haa95532_0         3.0 MB
    datashader-0.16.0          |  py311haa95532_0        17.1 MB
    distributed-2023.11.0      |  py311haa95532_0         1.7 MB
    filelock-3.13.1            |  py311haa95532_0          24 KB
    flask-2.2.5                |  py311haa95532_0         208 KB
    frozenlist-1.4.0           |  py311h2bbff1b_0          47 KB
    fsspec-2023.10.0           |  py311haa95532_0         359 KB
    gflags-2.2.2               |       hd77b12b_1         247 KB
    glog-0.5.0                 |       hd77b12b_1          93 KB
    gmpy2-2.1.2                |  py311h7f96b67_0         140 KB
    greenlet-3.0.1             |  py311hd77b12b_0         222 KB
    holoviews-1.18.2           |  py311haa95532_0         5.2 MB
    huggingface_hub-0.17.3     |  py311haa95532_0         471 KB
    hvplot-0.9.2               |  py311haa95532_0         1.9 MB
    icu-73.1                   |       h6c2663c_0        29.5 MB
    imageio-2.33.1             |  py311haa95532_0         645 KB
    imbalanced-learn-0.11.0    |  py311haa95532_1         383 KB
    importlib-metadata-7.0.1   |  py311haa95532_0          49 KB
    importlib_metadata-7.0.1   |       hd3eb1b0_0           8 KB
    intel-openmp-2023.1.0      |   h59b6b97_46320         2.7 MB
    ipykernel-6.28.0           |  py311haa95532_0         246 KB
    ipython-8.20.0             |  py311haa95532_0         1.5 MB
    jinja2-3.1.3               |  py311haa95532_0         354 KB
    jmespath-1.0.1             |  py311haa95532_0          51 KB
    jsonschema-4.19.2          |  py311haa95532_0         213 KB
    jsonschema-specifications-2023.7.1|  py311haa95532_0          16 KB
    jupyter-lsp-2.2.0          |  py311haa95532_0         107 KB
    jupyter_client-8.6.0       |  py311haa95532_0         252 KB
    jupyter_core-5.5.0         |  py311haa95532_0         112 KB
    jupyter_events-0.8.0       |  py311haa95532_0          58 KB
    jupyter_server-2.10.0      |  py311haa95532_0         596 KB
    jupyter_server_terminals-0.4.4|  py311haa95532_1          29 KB
    jupyterlab-4.0.11          |  py311haa95532_0         4.6 MB
    jupyterlab_server-2.25.1   |  py311haa95532_0         114 KB
    jupyterlab_widgets-3.0.9   |  py311haa95532_0         195 KB
    lazy_loader-0.3            |  py311haa95532_0          21 KB
    libboost-1.82.0            |       h3399ecb_2        23.1 MB
    libcurl-8.5.0              |       h86230a5_0         343 KB
    libdeflate-1.17            |       h2bbff1b_1         153 KB
    libmamba-1.5.6             |       hcd6fe79_0         3.9 MB
    libmambapy-1.5.6           |  py311h77c03ed_0         514 KB
    libpq-12.17                |       h906ac69_0         3.2 MB
    llvmlite-0.42.0            |  py311hf2fb9eb_0        18.6 MB
    markupsafe-2.1.3           |  py311h2bbff1b_0          28 KB
    matplotlib-3.8.0           |  py311haa95532_0           9 KB
    matplotlib-base-3.8.0      |  py311hf62ec03_0         7.6 MB
    mistune-2.0.4              |  py311haa95532_0         108 KB
    mkl-2023.1.0               |   h6b88ed4_46358       155.9 MB
    more-itertools-10.1.0      |  py311haa95532_0         107 KB
    mpc-1.1.0                  |       h7edee0f_1         260 KB
    mpfr-4.0.2                 |       h62dcd97_1         1.5 MB
    mpir-3.0.0                 |       hec2e145_1         1.3 MB
    multidict-6.0.4            |  py311h2bbff1b_0          54 KB
    nbclient-0.8.0             |  py311haa95532_0         137 KB
    nbconvert-7.10.0           |  py311haa95532_0         532 KB
    notebook-7.0.6             |  py311haa95532_0         3.4 MB
    notebook-shim-0.2.3        |  py311haa95532_0          27 KB
    numba-0.59.0               |  py311hf62ec03_0         5.8 MB
    numexpr-2.8.7              |  py311h1fcbade_0         160 KB
    numpy-1.26.3               |  py311hdab7c0b_0          11 KB
    numpy-base-1.26.3          |  py311hd01c5d8_0         7.3 MB
    openssl-3.0.13             |       h2bbff1b_0         7.4 MB
    overrides-7.4.0            |  py311haa95532_0          38 KB
    pandas-2.1.4               |  py311hf62ec03_0        13.6 MB
    panel-1.3.8                |  py311haa95532_0        15.6 MB
    param-2.0.2                |  py311haa95532_0         260 KB
    partd-1.4.1                |  py311haa95532_0          49 KB
    pillow-10.2.0              |  py311h2bbff1b_0         953 KB
    prompt-toolkit-3.0.43      |  py311haa95532_0         746 KB
    prompt_toolkit-3.0.43      |       hd3eb1b0_0           5 KB
    py-cpuinfo-9.0.0           |  py311haa95532_0          87 KB
    pycosat-0.6.6              |  py311h2bbff1b_0          82 KB
    pydantic-1.10.12           |  py311h2bbff1b_1         1.6 MB
    pyodbc-5.0.1               |  py311hd77b12b_0          66 KB
    pyqt-5.15.10               |  py311hd77b12b_0         4.1 MB
    pyqt5-sip-12.13.0          |  py311h2bbff1b_0          75 KB
    pyqtwebengine-5.15.10      |  py311hd77b12b_0         134 KB
    pytables-3.9.2             |  py311h91a9f6a_0         1.5 MB
    pytoolconfig-1.2.6         |  py311haa95532_0          36 KB
    pyviz_comms-3.0.0          |  py311haa95532_0          57 KB
    pywavelets-1.5.0           |  py311hd7041d2_0         3.6 MB
    pyyaml-6.0.1               |  py311h2bbff1b_0         185 KB
    pyzmq-25.1.2               |  py311hd77b12b_0         493 KB
    qt-main-5.15.2             |      h19c9488_10        59.4 MB
    qtpy-2.4.1                 |  py311haa95532_0         148 KB
    queuelib-1.6.2             |  py311haa95532_0          36 KB
    referencing-0.30.2         |  py311haa95532_0          78 KB
    regex-2023.10.3            |  py311h2bbff1b_0         389 KB
    rich-13.3.5                |  py311haa95532_0         566 KB
    rpds-py-0.10.6             |  py311h062c2fa_0         202 KB
    s3fs-2023.10.0             |  py311haa95532_0          77 KB
    safetensors-0.4.0          |  py311hcbdf901_0         289 KB
    scikit-learn-1.2.2         |  py311hd77b12b_1         7.6 MB
    scipy-1.11.4               |  py311hc1ccb85_0        20.9 MB
    semver-2.13.0              |     pyhd3eb1b0_0          16 KB
    send2trash-1.8.2           |  py311haa95532_0          81 KB
    sip-6.7.12                 |  py311hd77b12b_0         615 KB
    snappy-1.1.10              |       h6c2663c_1          92 KB
    sniffio-1.3.0              |  py311haa95532_0          18 KB
    soupsieve-2.5              |  py311haa95532_0          93 KB
    sqlalchemy-2.0.25          |  py311h2bbff1b_0         3.8 MB
    sympy-1.12                 |  py311haa95532_0        14.4 MB
    tabulate-0.9.0             |  py311haa95532_0          90 KB
    tokenizers-0.13.3          |  py311h49fca51_0         3.0 MB
    tornado-6.3.3              |  py311h2bbff1b_0         856 KB
    typing-extensions-4.9.0    |  py311haa95532_1          10 KB
    typing_extensions-4.9.0    |  py311haa95532_1          70 KB
    tzdata-2023d               |       h04d1e81_0         117 KB
    urllib3-1.26.18            |  py311haa95532_0         252 KB
    utf8proc-2.6.1             |       h2bbff1b_1          96 KB
    xz-5.4.5                   |       h8cc25b3_0         593 KB
    yaml-cpp-0.8.0             |       hd77b12b_0         2.0 MB
    yarl-1.9.3                 |  py311h2bbff1b_0         118 KB
    zeromq-4.3.5               |       hd77b12b_0         5.2 MB
    zict-3.0.0                 |  py311haa95532_0         119 KB
    zipp-3.17.0                |  py311haa95532_0          25 KB
    ------------------------------------------------------------
                                           Total:       532.2 MB
```

Then details about the new packages to be installed will be listed:

```
The following NEW packages will be INSTALLED:

  async-lru          pkgs/main/win-64::async-lru-2.0.4-py311haa95532_0
  brotli-python      pkgs/main/win-64::brotli-python-1.0.9-py311hd77b12b_7
  gmpy2              pkgs/main/win-64::gmpy2-2.1.2-py311h7f96b67_0
  jsonschema-specif~ pkgs/main/win-64::jsonschema-specifications-2023.7.1-py311haa95532_0
  jupyter-lsp        pkgs/main/win-64::jupyter-lsp-2.2.0-py311haa95532_0
  jupyter_server_te~ pkgs/main/win-64::jupyter_server_terminals-0.4.4-py311haa95532_1
  mpc                pkgs/main/win-64::mpc-1.1.0-h7edee0f_1
  mpfr               pkgs/main/win-64::mpfr-4.0.2-h62dcd97_1
  mpir               pkgs/main/win-64::mpir-3.0.0-hec2e145_1
  overrides          pkgs/main/win-64::overrides-7.4.0-py311haa95532_0
  referencing        pkgs/main/win-64::referencing-0.30.2-py311haa95532_0
  rich               pkgs/main/win-64::rich-13.3.5-py311haa95532_0
  rpds-py            pkgs/main/win-64::rpds-py-0.10.6-py311h062c2fa_0
  semver             pkgs/main/noarch::semver-2.13.0-pyhd3eb1b0_0
```

Then details about the packages to be removed will be listed, this should just be a small number of packages:

```
The following packages will be REMOVED:

  aiofiles-22.1.0-py311haa95532_0
  aiosqlite-0.18.0-py311haa95532_0
  async-timeout-4.0.2-py311haa95532_0
  backcall-0.2.0-pyhd3eb1b0_0
  brotlipy-0.7.0-py311h2bbff1b_1002
  datashape-0.5.4-py311haa95532_1
  glib-2.69.1-h5dc1a3c_2
  jinja2-time-0.2.0-pyhd3eb1b0_3
  jupyter_server_fileid-0.9.0-py311haa95532_0
  jupyter_server_ydoc-0.8.0-py311haa95532_1
  jupyter_ydoc-0.2.4-py311haa95532_0
  libwebp-1.3.2-hbc33d0d_0
  nbclassic-0.5.5-py311haa95532_0
  pcre-8.45-hd77b12b_0
  poyo-0.5.0-pyhd3eb1b0_0
  pyrsistent-0.18.0-py311h2bbff1b_0
  qtwebkit-5.212-h2bbfb41_5
  y-py-0.5.9-py311hb6bf4ef_0
  ypy-websocket-0.8.2-py311haa95532_0
```

Details about packages to be updated will now be listed, this should be the bulk of the packages:

```
The following packages will be UPDATED:

  aiobotocore                         2.5.0-py311haa95532_0 --> 2.7.0-py311haa95532_0
  aiohttp                             3.8.5-py311h2bbff1b_0 --> 3.9.0-py311h2bbff1b_0
  anaconda-cloud-au~                  0.1.3-py311haa95532_0 --> 0.1.4-py311haa95532_0
  anyio                               3.5.0-py311haa95532_0 --> 4.2.0-py311haa95532_0
  astropy                               5.1-py311h5bb9823_0 --> 5.3.4-py311hd7041d2_0
  attrs                              22.1.0-py311haa95532_0 --> 23.1.0-py311haa95532_0
  black                              23.3.0-py311haa95532_0 --> 23.11.0-py311haa95532_0
  bokeh                               3.2.1-py311h746a85d_0 --> 3.3.4-py311h746a85d_0
  boost-cpp                               1.82.0-h59b6b97_1 --> 1.82.0-h59b6b97_2
  botocore                          1.29.76-py311haa95532_0 --> 1.31.64-py311haa95532_0
  c-blosc2                                 2.8.0-hd77b12b_0 --> 2.12.0-h2f4ed9d_0
  ca-certificates                     2023.08.22-haa95532_0 --> 2023.12.12-haa95532_0
  certifi                         2023.7.22-py311haa95532_0 --> 2024.2.2-py311haa95532_0
  cffi                               1.15.1-py311h2bbff1b_3 --> 1.16.0-py311h2bbff1b_0
  click                               8.0.4-py311haa95532_0 --> 8.1.7-py311haa95532_0
  constantly                         15.1.0-py311haa95532_0 --> 23.10.4-py311haa95532_0
  contourpy                           1.0.5-py311h59b6b97_0 --> 1.2.0-py311h59b6b97_0
  cookiecutter       pkgs/main/noarch::cookiecutter-1.7.3-~ --> pkgs/main/win-64::cookiecutter-2.5.0-py311haa95532_0
  cryptography                       41.0.3-py311h89fc84f_0 --> 41.0.7-py311h89fc84f_0
  curl                                     8.1.1-h2bbff1b_0 --> 8.5.0-he2ea4bf_0
  cytoolz                            0.12.0-py311h2bbff1b_0 --> 0.12.2-py311h2bbff1b_0
  dal                               2023.1.1-h59b6b97_48681 --> 2023.1.1-h59b6b97_48682
  dask                             2023.6.0-py311haa95532_0 --> 2023.11.0-py311haa95532_0
  dask-core                        2023.6.0-py311haa95532_0 --> 2023.11.0-py311haa95532_0
  datashader                         0.15.2-py311haa95532_0 --> 0.16.0-py311haa95532_0
  distributed                      2023.6.0-py311haa95532_0 --> 2023.11.0-py311haa95532_0
  filelock                            3.9.0-py311haa95532_0 --> 3.13.1-py311haa95532_0
  flask                               2.2.2-py311haa95532_0 --> 2.2.5-py311haa95532_0
  frozenlist                          1.3.3-py311h2bbff1b_0 --> 1.4.0-py311h2bbff1b_0
  fsspec                           2023.4.0-py311haa95532_0 --> 2023.10.0-py311haa95532_0
  gflags                                   2.2.2-ha925a31_0 --> 2.2.2-hd77b12b_1
  glog                                     0.5.0-hd77b12b_0 --> 0.5.0-hd77b12b_1
  greenlet                            2.0.1-py311hd77b12b_0 --> 3.0.1-py311hd77b12b_0
  holoviews                          1.17.1-py311haa95532_0 --> 1.18.2-py311haa95532_0
  huggingface_hub                    0.15.1-py311haa95532_0 --> 0.17.3-py311haa95532_0
  hvplot                              0.8.4-py311haa95532_0 --> 0.9.2-py311haa95532_0
  icu                                       58.2-ha925a31_3 --> 73.1-h6c2663c_0
  imageio                            2.26.0-py311haa95532_0 --> 2.33.1-py311haa95532_0
  imbalanced-learn                   0.10.1-py311haa95532_1 --> 0.11.0-py311haa95532_1
  importlib-metadata                  6.0.0-py311haa95532_0 --> 7.0.1-py311haa95532_0
  importlib_metadata                       6.0.0-hd3eb1b0_0 --> 7.0.1-hd3eb1b0_0
  intel-openmp                      2023.1.0-h59b6b97_46319 --> 2023.1.0-h59b6b97_46320
  ipykernel                          6.25.0-py311h746a85d_0 --> 6.28.0-py311haa95532_0
  ipython                            8.15.0-py311haa95532_0 --> 8.20.0-py311haa95532_0
  jinja2                              3.1.2-py311haa95532_0 --> 3.1.3-py311haa95532_0
  jmespath           pkgs/main/noarch::jmespath-0.10.0-pyh~ --> pkgs/main/win-64::jmespath-1.0.1-py311haa95532_0
  jsonschema                         4.17.3-py311haa95532_0 --> 4.19.2-py311haa95532_0
  jupyter_client                      7.4.9-py311haa95532_0 --> 8.6.0-py311haa95532_0
  jupyter_core                        5.3.0-py311haa95532_0 --> 5.5.0-py311haa95532_0
  jupyter_events                      0.6.3-py311haa95532_0 --> 0.8.0-py311haa95532_0
  jupyter_server                     1.23.4-py311haa95532_0 --> 2.10.0-py311haa95532_0
  jupyterlab                          3.6.3-py311haa95532_0 --> 4.0.11-py311haa95532_0
  jupyterlab_server                  2.22.0-py311haa95532_0 --> 2.25.1-py311haa95532_0
  jupyterlab_widgets                  3.0.5-py311haa95532_0 --> 3.0.9-py311haa95532_0
  lazy_loader                           0.2-py311haa95532_0 --> 0.3-py311haa95532_0
  libboost                                1.82.0-hae598e9_1 --> 1.82.0-h3399ecb_2
  libcurl                                  8.1.1-h86230a5_0 --> 8.5.0-h86230a5_0
  libdeflate                                1.17-h2bbff1b_0 --> 1.17-h2bbff1b_1
  libmamba                                 1.5.1-hcd6fe79_0 --> 1.5.6-hcd6fe79_0
  libmambapy                          1.5.1-py311h77c03ed_0 --> 1.5.6-py311h77c03ed_0
  libpq                                    12.15-h906ac69_1 --> 12.17-h906ac69_0
  llvmlite                           0.40.0-py311hf2fb9eb_0 --> 0.42.0-py311hf2fb9eb_0
  markupsafe                          2.1.1-py311h2bbff1b_0 --> 2.1.3-py311h2bbff1b_0
  matplotlib                          3.7.2-py311haa95532_0 --> 3.8.0-py311haa95532_0
  matplotlib-base                     3.7.2-py311hf62ec03_0 --> 3.8.0-py311hf62ec03_0
  mistune                          0.8.4-py311h2bbff1b_1000 --> 2.0.4-py311haa95532_0
  mkl                               2023.1.0-h6b88ed4_46357 --> 2023.1.0-h6b88ed4_46358
  more-itertools     pkgs/main/noarch::more-itertools-8.12~ --> pkgs/main/win-64::more-itertools-10.1.0-py311haa95532_0
  multidict                           6.0.2-py311h2bbff1b_0 --> 6.0.4-py311h2bbff1b_0
  nbclient                           0.5.13-py311haa95532_0 --> 0.8.0-py311haa95532_0
  nbconvert                           6.5.4-py311haa95532_0 --> 7.10.0-py311haa95532_0
  notebook                            6.5.4-py311haa95532_1 --> 7.0.6-py311haa95532_0
  notebook-shim                       0.2.2-py311haa95532_0 --> 0.2.3-py311haa95532_0
  numba                              0.57.1-py311hf62ec03_0 --> 0.59.0-py311hf62ec03_0
  numexpr                             2.8.4-py311h1fcbade_1 --> 2.8.7-py311h1fcbade_0
  numpy                              1.24.3-py311hdab7c0b_1 --> 1.26.3-py311hdab7c0b_0
  numpy-base                         1.24.3-py311hd01c5d8_1 --> 1.26.3-py311hd01c5d8_0
  openssl                                 3.0.10-h2bbff1b_2 --> 3.0.13-h2bbff1b_0
  pandas                              2.0.3-py311hf62ec03_0 --> 2.1.4-py311hf62ec03_0
  panel                               1.2.3-py311haa95532_0 --> 1.3.8-py311haa95532_0
  param                              1.13.0-py311haa95532_0 --> 2.0.2-py311haa95532_0
  partd                               1.4.0-py311haa95532_0 --> 1.4.1-py311haa95532_0
  pillow                              9.4.0-py311hd77b12b_1 --> 10.2.0-py311h2bbff1b_0
  prompt-toolkit                     3.0.36-py311haa95532_0 --> 3.0.43-py311haa95532_0
  prompt_toolkit                          3.0.36-hd3eb1b0_0 --> 3.0.43-hd3eb1b0_0
  py-cpuinfo         pkgs/main/noarch::py-cpuinfo-8.0.0-py~ --> pkgs/main/win-64::py-cpuinfo-9.0.0-py311haa95532_0
  pycosat                             0.6.4-py311h2bbff1b_0 --> 0.6.6-py311h2bbff1b_0
  pydantic                           1.10.8-py311h2bbff1b_0 --> 1.10.12-py311h2bbff1b_1
  pyodbc                             4.0.34-py311hd77b12b_0 --> 5.0.1-py311hd77b12b_0
  pyqt                               5.15.7-py311hd77b12b_0 --> 5.15.10-py311hd77b12b_0
  pyqt5-sip                         12.11.0-py311hd77b12b_0 --> 12.13.0-py311h2bbff1b_0
  pyqtwebengine                      5.15.7-py311hd77b12b_0 --> 5.15.10-py311hd77b12b_0
  pytables                            3.8.0-py311h4671533_3 --> 3.9.2-py311h91a9f6a_0
  pytoolconfig                        1.2.5-py311haa95532_1 --> 1.2.6-py311haa95532_0
  pyviz_comms                         2.3.0-py311haa95532_0 --> 3.0.0-py311haa95532_0
  pywavelets                          1.4.1-py311h2bbff1b_0 --> 1.5.0-py311hd7041d2_0
  pyyaml                                6.0-py311h2bbff1b_1 --> 6.0.1-py311h2bbff1b_0
  pyzmq                              23.2.0-py311hd77b12b_0 --> 25.1.2-py311hd77b12b_0
  qt-main                                 5.15.2-h879a1e9_9 --> 5.15.2-h19c9488_10
  qtpy                                2.2.0-py311haa95532_0 --> 2.4.1-py311haa95532_0
  queuelib                            1.5.0-py311haa95532_0 --> 1.6.2-py311haa95532_0
  regex                            2022.7.9-py311h2bbff1b_0 --> 2023.10.3-py311h2bbff1b_0
  s3fs                             2023.4.0-py311haa95532_0 --> 2023.10.0-py311haa95532_0
  safetensors                         0.3.2-py311h062c2fa_0 --> 0.4.0-py311hcbdf901_0
  scipy                              1.11.1-py311hc1ccb85_0 --> 1.11.4-py311hc1ccb85_0
  send2trash         pkgs/main/noarch::send2trash-1.8.0-py~ --> pkgs/main/win-64::send2trash-1.8.2-py311haa95532_0
  sip                                 6.6.2-py311hd77b12b_0 --> 6.7.12-py311hd77b12b_0
  snappy                                   1.1.9-h6c2663c_0 --> 1.1.10-h6c2663c_1
  sniffio                             1.2.0-py311haa95532_1 --> 1.3.0-py311haa95532_0
  soupsieve                             2.4-py311haa95532_0 --> 2.5-py311haa95532_0
  sqlalchemy                         1.4.39-py311h2bbff1b_0 --> 2.0.25-py311h2bbff1b_0
  sympy                              1.11.1-py311haa95532_0 --> 1.12-py311haa95532_0
  tabulate                           0.8.10-py311haa95532_0 --> 0.9.0-py311haa95532_0
  tokenizers                         0.13.2-py311h49fca51_1 --> 0.13.3-py311h49fca51_0
  tornado                             6.3.2-py311h2bbff1b_0 --> 6.3.3-py311h2bbff1b_0
  typing-extensions                   4.7.1-py311haa95532_0 --> 4.9.0-py311haa95532_1
  typing_extensions                   4.7.1-py311haa95532_0 --> 4.9.0-py311haa95532_1
  tzdata                                   2023c-h04d1e81_0 --> 2023d-h04d1e81_0
  urllib3                           1.26.16-py311haa95532_0 --> 1.26.18-py311haa95532_0
  utf8proc                                 2.6.1-h2bbff1b_0 --> 2.6.1-h2bbff1b_1
  xz                                       5.4.2-h8cc25b3_0 --> 5.4.5-h8cc25b3_0
  yaml-cpp                                 0.7.0-hd77b12b_1 --> 0.8.0-hd77b12b_0
  yarl                                1.8.1-py311h2bbff1b_0 --> 1.9.3-py311h2bbff1b_0
  zeromq                                   4.3.4-hd77b12b_0 --> 4.3.5-hd77b12b_0
  zict                                2.2.0-py311haa95532_0 --> 3.0.0-py311haa95532_0
  zipp                               3.11.0-py311haa95532_0 --> 3.17.0-py311haa95532_0
```

Details about packages being installed from a higher-priority channel will be listed:

```
The following packages will be SUPERSEDED by a higher-priority channel:

  conda-index        pkgs/main/win-64::conda-index-0.3.0-p~ --> conda/noarch::conda-index-0.2.1-py_0
```

Details about packages being downgraded will be listed, this should be only a very small number of packages. Sometimes Anaconda downgrade a package to a more stable version:

```
The following packages will be DOWNGRADED:

  scikit-learn                        1.3.0-py311hf62ec03_0 --> 1.2.2-py311hd77b12b_1
```

You will be asked to proceed. Input ```y```:

```
Proceed ([y]/n)?
```

A new prompt will display when the update is complete:

```
Downloading and Extracting Packages

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(base) PS ~> 
```

For Miniconda, updating the ```conda``` package manger will update the bootstrap Python distribution.

The Anaconda Navigator can be checked for an update using:

```powershell
conda update -c conda --solver=libmamba anaconda-navigator
```

A similar output to before will be shown, input ```y``` in order to proceed:

```
(base) PS ~> conda update -c conda --solver=libmamba anaconda-navigator
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~\anaconda3

  added / updated specs:
    - anaconda-navigator


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    anaconda-navigator-2.5.2   |  py311haa95532_0         5.7 MB
    ------------------------------------------------------------
                                           Total:         5.7 MB

The following packages will be UPDATED:

  anaconda-navigator                  2.5.0-py311haa95532_0 --> 2.5.2-py311haa95532_0

Proceed ([y]/n)?
```

A new prompt will display when the update is complete:

```
Downloading and Extracting Packages

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(base) PS ~> 
```

Note the Anaconda-Navigator is not installed in Miniconda and therefore should not be updated.

Anaconda should now be updated.

The (base) Python environment can be reactivated using:

```powershell
conda activate base
```

## MikTeX Installation

A number of the datascience packages such as nbconvert and matplotlib can use TeX. Unfortunately the installation of TeX differs significantly for Windows and Linux and therefore the installation of TeX isn't included with the Anaconda Python Distribution. On Windows the MikTeX distribution contains the MikTeX console which is essentially the TeX package manager. The installer for it can be found on its home page [MikTeX](https://miktex.org/). 

winget can be used to search for MitTeX:

```
winget search miktex
```

The following output will display:

```
PS ~> winget search miktex
Name   Id            Version Match               Source
-------------------------------------------------------
MiKTeX MiKTeX.MiKTeX 23.10   ProductCode: miktex winget
```

It can be installed using:

```
PS ~> winget install MikTeX.MikTex
```

This will install MikTex. The operation is only complete when a new prompt displays. This will display:

```
PS ~> winget install MikTeX.MikTex
Found MikTex [MikTeX.MikTex] Version 23.10
This application is licensed to you by its owner.
Microsoft is not responsible for, nor does it grant any licenses
to, third-party packages.
Successfully verified installer hash
Starting package install...
Successfully installed
PS ~>
```

Default installation will add MikTex to the Windows Environmental Variables path which allows MikTeX to be found in the (base) Python environment and any other Python environment. After installation, the MikTeX console should be launched from the start menu:

<img src='images_install/img_041.png' alt='img_041' width='350'/>

A warning about updates will display:

<img src='images_install/img_042.png' alt='img_042' width='350'/>

Go to the Updates tab and select Check for Updates:

<img src='images_install/img_043.png' alt='img_043' width='350'/>

Then select Update Now:

<img src='images_install/img_044.png' alt='img_044' width='350'/>

### The (base) Python Environment

When Anaconda is added to the Windows Environmental Path, the Windows environmental path looks like the following. This is the order of directories that the Windows Terminal looks for applications: 

```powershell
%USERPROFILE%\Anaconda3
%USERPROFILE%\Anaconda3\Library\mingw-w64\bin
%USERPROFILE%\Anaconda3\Libraryusr\bin
%USERPROFILE%\Anaconda3\Library\bin
%USERPROFILE%\Anaconda3\Scripts
%LOCALAPPDATA%\Microsoft\WindowsApps
```

If the application is found in a directory it will be launched and there will be no further searches made for the application.

When Anaconda is initialised with the Windows Terminal, the Windows Environmental path may not be physically updated however the initialisation script will instruct the Windows Terminal to look in the 5 equivalent locations of the currently select Python environment:

```powershell
%USERPROFILE%\Anaconda3
%USERPROFILE%\Anaconda3\Library\mingw-w64\bin
%USERPROFILE%\Anaconda3\Libraryusr\bin
%USERPROFILE%\Anaconda3\Library\bin
%USERPROFILE%\Anaconda3\Scripts
```

The currently selected Python environment is (base) by default. When the Python environment is not (base), the five equivalent locations in the Python environment will be used to search for an application and then then five equivalent locations in (base) are searched.

If the application is not found in these directories. Then a search is made in the remaining entries in the Windows Environmental Path:

```powershell
%LOCALAPPDATA%\Microsoft\WindowsApps
```

Windows also has additional locations which are used to search for applications when an application is not found in the above directories:

```powershell
C:\Windows\System32
```

For example when the PowerShell command:

```powershell
python
```

is used then the a search is made in the folder ```~\Anaconda3``` for a ```python.exe```.

And therefore the following commands are equivalent:

```powershell
python
python.exe
~\Anaconda3\python
~\Anaconda3\python.exe
```

For Miniconda this is:

```powershell
python
python.exe
~\Miniconda3\python
~\Miniconda3\python.exe
```

<img src='images_install/img_011.png' alt='img_011' width='350'/>

In Windows Explorer, this is:

```powershell
%USERPROFILE%\Anaconda3\python.exe
```

<img src='images_install/img_012.png' alt='img_012' width='350'/>

Note because the Windows Terminal opens in ```%USERPROFILE%``` by default. The application can also be accessed from the relative path:

```powershell
Anaconda3\python.exe
```

In the Windows Terminal the ```%USERPROFILE%``` environmental variable can be accessed using ```~``` and therefore the application can also be accessed from the full path:

```powershell
~\Anaconda3\python.exe
```

<img src='images_install/img_013.png' alt='img_013' width='350'/>

It is more common to access the command using:

```powershell
python
```

The Scripts subfolder:

<img src='images_install/img_014.png' alt='img_014' width='450'/>

Contains a number of additional applications:

<img src='images_install/img_015.png' alt='img_015' width='450'/>

As Miniconda is a bootstrap version of Anaconda most of the applications are not preinstalled in the Miniconda base Python environment. Typically these applications only become available when they are installed, however this is usually in another custom Python environment (see next section).

Interactive Python (IPython) can be launched using:

```powershell
ipython
```

The output shown gives details about the Python and Interactive Python version and each Python cell has a numeric index. 

```
(base) PS ~> ipython
Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

IPython is similar to Python but has enhancements such as the application of Python syntax highlighting and the addition of the ```?``` operator which can be used to examine a Python objects docstring or ```??``` which can be used to output the file of a module. 

IPython also has IPython magics which begin with ```%``` and are equivalent to commonly ```bash``` commands. 

The popular Jupyter project for example is an abbreviation for Julia Python et (Latin for and) R.

<img src='images_install/img_031.png' alt='img_031' width='450'/>

This has the programs:

* jupyter-console
* jupyter-qtconsole
* jupyter-notebook
* jupyter-lab

The jupyter-console by default uses the Python Kernel and is identical to IPython however the kernel can be changed using the option ```--kernel```:

```
PS ~> jupyter-console --kernel=python3

Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

The available kernels can be viewed by using:

```powershell
jupyter kernelspec list
```

Because Anaconda is a Python Distribution by default it only has a Python kernel:

```
PS ~> jupyter kernelspec list
Available kernels:
  python3    ~\anaconda3\share\jupyter\kernels\python3
PS ~>
```

The QTConsole is essentially rewritten using the QT GUI Framework and has a number of additional enhancements for example automatically displaying a docstring as a popup balloon:

<img src='images_install/img_032.png' alt='img_032' width='450'/>

And nesting graphics:

<img src='images_install/img_033.png' alt='img_033' width='450'/>

It also has a File menu which can be used to save the file as a HTML file or a pdf.

The Jupyter Notebook and Jupyter Lab are NodeJS implementations of the Console with support for interactive Python Notebook Files. JupyterLab also has a script editor for Python scripts files and a markdown editor and markdown preview for files.

When either of the commands are run the Terminal is busy running a Jupyter server, logs will display in this server:

```
PS ~> jupyter-lab
[I 2023-12-25 09:09:43.024 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2023-12-25 09:09:43.060 ServerApp]

    To access the server, open this file in a browser:
        file:///C:/Users/phili/AppData/Roaming/jupyter/runtime/jpserver-13048-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/lab?token=6976ddcb2ac75fedf2b4ee684e8dc1b52011341ec7eef3a2
        http://127.0.0.1:8888/lab?token=6976ddcb2ac75fedf2b4ee684e8dc1b52011341ec7eef3a2
```

The visual elements will display in a browser:

<img src='images_install/img_034.png' alt='img_034' width='450'/>

To view identifiers beginning with a prefix, input ↹ after the prefix:

<img src='images_install/img_035.png' alt='img_035' width='450'/>

To view the docstring popup, input ⇧ + ↹:

<img src='images_install/img_036.png' alt='img_036' width='450'/>

The visual elements can be closed in the browser, however the server will continue to run in the Terminal until Ctrl + c is pressed to close the current operation.

Another important binary is the Scientific Python Development Environment (spyder) which can be launched using:

```powershell
spyder
```

The Terminal will display the following

```
PS ~> spyder
fromIccProfile: failed minimal tag size sanity
~\anaconda3\Lib\site-packages\paramiko\transport.py:219: CryptographyDeprecationWarning: Blowfish has been deprecated
  "class": algorithms.Blowfish,
```

<img src='images_install/img_037.png' alt='img_037' width='450'/>

The Anaconda Navigator is a program that contains shortcuts to most of Python applications. It can be launched using:

```powershell
anaconda-navigator
```

<img src='images_install/img_016.png' alt='img_016' width='450'/>

The Anaconda Navigator contains a number of shortcut to Python IDEs:

<img src='images_install/img_017.png' alt='img_017' width='450'/>

The scripts folder contains a number of Python formatters such as autopep8, isort, black, yapf and linters such as pylint and pyflakes. These can be run in the Terminal to format a Python file for example the Python script file with sloppy spacing in the code:

<img src='images_install/img_038.png' alt='img_038' width='450'/>

However are normally implemented in IDEs such as Spyder which has Autoformatters in the Source menu:

<img src='images_install/img_039.png' alt='img_039' width='450'/>

AutoPEP8 addresses the spacing making it PEP8 compliant. The opinionated formatter black can also be used to make quotation consistent (but inconsistent with the default single quotations used by the Python kernel):

<img src='images_install/img_040.png' alt='img_040' width='450'/>

[Return to Python Tutorials](../../readme.md)