# Python Tutorials for Scientists


**Comprehensive Python tutorials designed for beginners and scientists.**  

These tutorials cover:  
- Python installation and setup  
- Object-oriented programming (OOP) and the Python data model  
- The scientific Python stack: **NumPy, pandas, Matplotlib, Seaborn**  
- IDEs geared towards scientific use: **Spyder, JupyterLab, VSCode**  

My background is in **biophysics**, where Python is becoming increasingly important for **data analysis, visualisation, and simulation**. This repository is designed to help both beginners and scientists build strong foundations in Python while also learning how to apply it in **research and practical problem-solving**.  

⭐ **Please star and share this repository** if you’ve found it useful — it will help others discover it too!  

## Viewing Markdown Files

### GitHub Website 

These tutorials are in markdown format and GitHub displays the markdown as a webpage. Note some of the guides are screenshot intensive and on slow connections, the browser may timeout before all the images are downloaded. The browser caches downloaded images, refresh the page a couple of times to allow the browser to download the remaining images and the page should display correctly.

### Cloning the GitHub Repository and Opening in VSCode

The GitHub repository can also be cloned using GitHub Desktop. This essentially downloads the markdown tutorials to a folder. The folder contains the markdown files in the form of `readme.md` and all the images. The readme.md when opened in notepad or text editor will display everything as unformatted text. To view the formatted content open the markdown file in VSCode and use the markdown preview. Some of the styling in the markdown tables is ignored on GitHub and renders better in VSCode. This styling more closely resembles the Variable Explorer of the Spyder IDE. Since all the images are local there should be less issues displaying content.

* [Windows: GitHub Desktop Setup + Cloning this Repository](./github_install_windows/readme.md)
* [Ubuntu: GitHub Desktop Setup + Cloning this Repository](./github_install_ubuntu/readme.md)

The Ubuntu instructions can be modified slightly for another Linux distribution and should closely resemble installation on a Mac.

## Development Environment Setup

Python has a large number of development environments and installers which often confuses beginners. Beginners often have problems setting up a Python environment because they use the wrong installer or do not use the package manager as expected. This guide will use the standalone Spyder installer and the `conda` package manager in Miniforge to create Python environments for Spyder, JupyterLab and VSCode.

### Other Python Installers 

Optional information is provided about other installers below:

<details>
  <summary>Python Installer</summary>
  
    The basic installer from Python.org only contains Python, Python standard libraries and a very basic IDE, called IDLE. It includes the Python package manager `pip` but does not include the `conda` package manager. `conda` is a package manager that can be used to install Python packages and additional non-Python dependencies and is generally recommended for the scientific libraries.

</details>

<details>
  <summary>Anaconda Python Distribution</summary>
  
    The Anaconda Python distribution is a large collection of Python packages of specific versions that have been tested for interoperability. The Anaconda base Python environment includes Spyder, JupyterLab and the numeric Python stack. 

    Although Anaconda includes the `conda` package manager and uses the commercial channel by default. It should be noted that Anaconda is a distribution designed to be used "as is". Anaconda will become unstable if community channel packages are installed. 

    Unfortunately the latest version of Anaconda is from 2024 and has Spyder 5 instead of Spyder 6 and numpy 1 instead of numpy 2 which can result in issues:

    * The older version of Spyder in Anaconda has many issues which have since been addressed in more recent versions of Spyder.
    * There are also substantial changes in numpy 2, giving a good cleanup of the API. 

    Likely there will be a 2025 release of Anaconda that is updated to Spyder 6 and has numpy 2. In the meantime the standalone `conda`-based Spyder installer is recommended alongside Miniforge.

</details>

<details>
  <summary>Spyder (Standalone Installer)</summary>
  
    Spyder 6 has a standalone `conda`-based installer which installs Spyder and its most common optional dependencies such as the numeric Python stack.

    The number of packages included in the Spyder installer isn't as exhaustive as those in Anaconda. To install additional packages an additional `conda` Python environment with community channel packages is required (typically Miniconda is used for this).

</details>

<details>
  <summary>Miniconda</summary>
  
    Miniconda is a minimal `conda` based installer that uses the commercial channel by default. It is more common to create Python environments using the community channel and therefore typically Miniforge is typically preferred. However Miniconda should be used when one needs to create one Python environment using packages using the commercial channel and another from the community channel.

</details>

<details>
  <summary>Miniforge</summary>
  
    Miniforge is a minimal `conda` based installer that uses the community channel by default. These tutorials use the standalone Spyder installer and Miniforge to get the latest packages and the latest version of the IDEs, which normally give the best results as each IDE and Python package is under continuous development. 

</details>

### **S**cientific **Py**thon **D**evelopment **E**nvi**r**onment (Spyder)

Spyder is tailored for scientists and engineers and has the most commonly used packages from the scientific stack preinstalled, a conda environment can be used to install additional packages. This makes it very beginner friendly. This installation guide will also cover installation of additional packages using Miniforge to create a `conda-forge` (community channel) environment. Additional dependencies such as TeX (commonly used in plots), which do not have a `conda-forge` package. 

<img src='./images/img_001.png' alt='img_001' width='600'/>

* [Windows: Spyder Setup + Miniforge Setup + TeX Setup](./spyder_install_windows/readme.md)
* [Ubuntu: Spyder Setup + Miniforge Setup + Tex Setup](./spyder_install_ubuntu/readme.md)

### JupyterLab (**Ju**lia, **Pyt**hon **e**t **R** **Lab**oratory)

JupyterLab is installed via a separate `conda-forge` (community channel) environment and is a browser-based IDE which is based around the interactive python notebook.

<img src='./images/img_002.png' alt='img_002' width='600'/>

* [Windows: JupyterLab Setup](/jupyter_install_windows/readme.md)
    * [Windows: Markdown](./markdown/readme.md)
* [Ubuntu: JupyterLab Setup](./jupyter_install_ubuntu/readme.md)
    * [Ubuntu: Markdown](./markdown/readme.md)

### VSCode (**V**isual **S**tudio **Code**)

VSCode is a general purpose code editor and can be used with Python, when the Python related extensions are installed and a separate `conda-forge` (community channel) environment is selected as the Python interpreter and initialised with the Terminal. Beginners often struggle to get started with VScode, because they do not perform a perquisite step incorrectly or miss a perquisite step out entirely.

<img src='./images/img_003.png' alt='img_003' width='600'/>

* [Windows: VSCode Setup for Python](./vscode_install_windows/readme.md)
* [Ubuntu: VSCode Setup for Python](./vscode_install_ubuntu/readme.md)

Preference of a specific Python IDE is somewhat subjective and each IDE has its strengths and weaknesses. I routinely use the 3 IDEs above for different purposes. The remaining markdown tutorials can be used with any of the above 3 IDEs or another IDE that has an ipython console. 

## Python and Standard Libraries

These tutorials cover the `object` orientated design pattern of `builtins` classes, focusing on text datatypes, numeric datatypes and collection datatypes. The `object` orientated design pattern is known as the Python data model:

* [Object Orientated Programming (OOP) and the Python Data Model](./the_python_datamodel/readme.md)
* [Text Datatypes](./text_datatypes/readme.md)
* [Numeric Datatypes](./numeric_datatypes/readme.md)
* [Collection Datatypes](./collection_datatypes/readme.md)
* [Iterator Datatypes](./iterator_datatypes/readme.md)

## Numeric Python Stack

These tutorials cover the numeric Python stack, which bridge a numeric design pattern with a collection design pattern:

* [Numeric Python Library (numpy)](./numpy_library/readme.md)
* [Matrix Plotting Library (matplotlib)](./matplotlib_library/readme.md)
* [Python and Data Analysis Library (pandas)](./pandas_library/readme.md)
* [Data Visualisation Library (seaborn)](./seaborn_library/readme.md)
