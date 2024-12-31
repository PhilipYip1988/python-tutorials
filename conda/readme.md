# Python Package Managers

## conda vs pip

`pip` is the default Python package manager and `conda` is a system package manager. `conda` is closely associated with Python and in particular, Python for use in the field of data science.

The main advantages of using conda, is it can install Python and non-Python packages. The Jupyter project for example is an abbreviation of Julia, Python et R. A conda environment can be created with Python and the R kernel [irkernel - conda-forge](https://anaconda.org/conda-forge/r-irkernel) and therefore Python and R packages, allowing both programming languages to be used in JupyterLab. This is more difficult to achieve using pip. On Linux, the third programming language Julia [conda-forge julia](https://anaconda.org/conda-forge/julia) can also be installed using conda, although the developers as far as I know never managed to add Julia to conda for Windows. The general idea was to add a way to installed other dependencies used by data science in conda such as TeX [miktex - conda-forge](https://anaconda.org/conda-forge/miktex) and codecs [conda-forge ffmpeg](https://anaconda.org/conda-forge/ffmpeg) which are used for example in some matplotlib plots and animations. There is a limited degree of success in such areas.

Some data science IDEs such as Spyder [Spyder Release Notes](https://github.com/spyder-ide/spyder/releases) recommend their standalone installer or a conda environment with specific dependencies in order to work properly. The developers state that there is support for pip but that:

>>> please be aware that pip installations are for advanced users with good knowledge of all Spyder dependencies. Because of that, all installation problems you encounter are expected to be solved by you.

## conda Channels

One area of confusion when it comes to using conda is that there are multiple channels:

* `-c conda-forge` (open source community channel)
* `-c anaconda` (tainted commercial channel)

`-c conda-forge` is the community channel which is open source and has the latest version of packages and the largest number of packages. In general `-c conda-forge` should be used for creating custom environments.

`-c anaconda` is a tainted commercial channel which has a more limited set of packages and general older "more stable" versions of packages which the Anaconda company use as part of their Anaconda Python distribution which they charge for commercial use.

## conda Installers

There are three conda based installers. One is open source:

* [Miniforge](https://github.com/conda-forge/miniforge) which has a bootstrap base Python environment which contains the conda package manager and uses the community channel `-c conda-forge` by default. The `base` Python environment should be used only to update the `conda` package manager and other `-c conda-forge` environments should be made for other projects.

Generally you would create an environment using only packages from `-c conda-forge`. There are some additional specialised channels that you can use such as `-c bio-conda`, a channel used to group life-science packages. The `-c bio-conda` channel is designed for compatibility with the `-c conda-forge` channel.

Two are tainted by Anacondas licensing agreements:

* [Miniconda](https://docs.anaconda.com/miniconda/) which has a bootstrap base Python environment which contains the `conda` package manager and uses the commercial channel `-c anaconda` by default. The `base` Python environment should be used only to update the `conda` package manager and other `-c anaconda` or `-c conda-forge` channel environments should be made for other projects. **Do not mix channels per project as it results in an unstable environment.**

* [Anaconda](https://www.anaconda.com/) which has a large number of data science packages installed in the `base` Python environment and generally should be used "as is". The `base` Python environment also contains the `conda` package manager and uses the commercial channel `-c anaconda` by default. In the `base` Python environment you should only look to update the `conda` package manager (and `anaconda-navigator`). Updating the `conda` package manager using the `-c anaconda` should in turn update the Anaconda distribution. Although, often it is more reliable to uninstall Anaconda and reinstall Anaconda using the latest standalone installer. The `conda` package manager can be used to create other `-c anaconda` or `-c conda-forge` environments for other projects. **Do not mix channels per project as it results in an unstable environment.**

Mixing channels generally results in packages from the `-c conda-forge` channel being downgraded to "more stable" packages from `-c anaconda` channel. Generally this results in an unstable environment.

## Miniforge Installation (Windows)


## Miniforge Installation (Linux)


## Spyder IDE

## JupyterLab IDE
