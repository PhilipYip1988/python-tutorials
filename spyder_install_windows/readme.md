# Spyder IDE Windows Setup

## Downloading and Installing Spyder

Spyder is developed on GitHub and the latest release is on the [GitHub Spyder Releases Page](https://github.com/spyder-ide/spyder/releases). Select the Windows Installer:

<img src='./images/img_001.png' alt='img_001' width='600'/>

Microsoft Edge may block the download, select the download and then select Keep:

<img src='./images/img_002.png' alt='img_002' width='600'/>

<img src='./images/img_003.png' alt='img_003' width='600'/>

Select Show More:

<img src='./images/img_004.png' alt='img_004' width='600'/>

Select Keep Anyway:

<img src='./images/img_005.png' alt='img_005' width='600'/>

Double click the Windows application to begin the install:

<img src='./images/img_006.png' alt='img_006' width='600'/>

Select Next:

<img src='./images/img_007.png' alt='img_007' width='600'/>

Select I Agree:

<img src='./images/img_008.png' alt='img_008' width='600'/>

Select Just Me and Next:

<img src='./images/img_009.png' alt='img_009' width='600'/>

Spyder will be installed in:

```
%LOCALAPPDATA%\spyder-6
```

Select Next:

<img src='./images/img_010.png' alt='img_010' width='600'/>
<img src='./images/img_011.png' alt='img_011' width='600'/>
<img src='./images/img_012.png' alt='img_012' width='600'/>

Select Install:

<img src='./images/img_013.png' alt='img_013' width='600'/>

Select Next:

<img src='./images/img_014.png' alt='img_014' width='600'/>

Select Finish:

<img src='./images/img_015.png' alt='img_015' width='600'/>

Spyder 6 will display a Start Menu shortcut, right click it and select Pin to Start:

<img src='./images/img_016.png' alt='img_016' width='600'/>

## Spyder IDE Basics

When Spyder is first launched, a prompt to begin a tour will display:

<img src='./images/img_017.png' alt='img_017' width='600'/>

To the bottom right is the IPython Console, where commands can be input individually. Notice the cells are numbered, by execution oder. The code can be input:

```python
In [1]: 'hello'
Out[1]: 'hello'
```

<img src='./images/img_018.png' alt='img_018' width='600'/>

This value was input and returned as an output. the value can also be assigned to an object name using the `=` operator:

```python
In [2]: text = 'hello'
```

<img src='./images/img_019.png' alt='img_019' width='600'/>

This object name `text` displays on the Variable Explorer. It has the type `str`. The identifiers from the `str` class can  be accessed from `text` by typing in `text.` followed by a `↹`:

<img src='./images/img_020.png' alt='img_020' width='600'/>

If part of an identifier is input for example `text.cap` followed by a `↹`, the identifier `text.capitalize` will display:

<img src='./images/img_021.png' alt='img_021' width='600'/>

<img src='./images/img_022.png' alt='img_022' width='600'/>

When this is input, the method is referenced and the output displays where the method is defined, in this case, in the `str` class:

```python
In [3]: text.capitalize
Out[3]: <function str.capitalize()>
```

<img src='./images/img_023.png' alt='img_023' width='600'/>

A method is called using parenthesis, the docstring displays, which provided details about any input parameters:

<img src='./images/img_024.png' alt='img_024' width='600'/>

A new `str` instance is returned to the console:

```python
In [4]: text.capitalize()
Out[4]: 'Hello'
```

<img src='./images/img_025.png' alt='img_025' width='600'/>

Note `text` remains assigned to the original `str` instance `'hello'`. This new `str` instance can be assigned to `text` which reassigns the value of `text`. The right hand side is carried out first (using the original value of `text` which was `hello`)

```python
In [5]: text.capitalize()
```

This is then reassigned to the `object` name on the right hand side

```python
In [5]: text = text.capitalize()
```

The value of the new instance now displays under `text` in the Variable Explorer:

<img src='./images/img_026.png' alt='img_026' width='600'/>

Other methods such as `replace` can be examined. A docstring displays showing the mandatory positional parameters `old` (position `0`) and `new` (position `1`). This is followed by the optional parameter `value` (position `2`) which has a default value `-1`, meaning all replacements of the old substring will be replaced with the new substring. Any parameter provided before the `/` must be supplied positionally only:

<img src='./images/img_027.png' alt='img_027' width='600'/>

```python
In [6]: text.replace('ll', '7')
Out[6]: 'He7o'
```

Using named parameters:

```python
In [7]: text.replace(old='ll', new='7')
```

is not allowed because these parameters occur before the `/` in the docstring

<img src='./images/img_028.png' alt='img_028' width='600'/>

If the following is input:

```python
In [8]: text.replace
```

And `replace` is right clicked, it can be inspected (shortcut key `Ctrl` + `i`):

<img src='./images/img_029.png' alt='img_029' width='600'/>

This opens more detailed help, in the help pane:

<img src='./images/img_030.png' alt='img_030' width='600'/>

Spyder has a script editor.

<img src='./images/img_031.png' alt='img_031' width='600'/>

The script file can be saved in Documents as `script.py`:

<img src='./images/img_032.png' alt='img_032' width='600'/>

<img src='./images/img_033.png' alt='img_033' width='600'/>

<img src='./images/img_034.png' alt='img_034' width='600'/>

In a Python script the `#` means a comment:

```python
# Import Libraries
import numpy as np # numeric python library
import matplotlib.pyplot as plt # matrix plotting library
```

<img src='./images/img_035.png' alt='img_035' width='600'/>

Using `#%%` creates a cell:

```python
#%% Import Libraries
import numpy as np 
import matplotlib.pyplot as plt 
```

Cells can be collapsed:

<img src='./images/img_036.png' alt='img_036' width='600'/>

<img src='./images/img_037.png' alt='img_037' width='600'/>

Other cells can be created: 

```python
#%% Import Libraries
import numpy as np 
import matplotlib.pyplot as plt 
#%% Create Data
x = np.array([0, 1, 2, 3, 4,])
y = 2 * x
#%% Plot Data
plt.plot(x, y)
```

A cell from a script file can be ran using the run cell button:

<img src='./images/img_038.png' alt='img_038' width='600'/>

This cell is still highlighted after execution. The cell and advance to the next cell button is more useful when running through each cell in a script file:

<img src='./images/img_039.png' alt='img_039' width='600'/>

<img src='./images/img_040.png' alt='img_040' width='600'/>

The Variables `x` and `y` display in the Variable Explorer:

<img src='./images/img_041.png' alt='img_041' width='600'/>

The plot displays as a static image using the `inline` backend. This static images displays on the plots pane:

<img src='./images/img_042.png' alt='img_042' width='600'/>

The plotting backend can be changed to an interactive plot using the `qtagg` backend:

<img src='./images/img_043.png' alt='img_043' width='600'/>

If the last line is selected, the currently selected selection can be run:

<img src='./images/img_044.png' alt='img_044' width='600'/>

The plot now displays in its own window:

<img src='./images/img_045.png' alt='img_045' width='600'/>

The kernel can be restarted, removing all variables and imports by selecting Consoles → Restart Kernel and then selecting Yes. Alternatively typing `exit` into the console restarts the kernel:

<img src='./images/img_046.png' alt='img_046' width='600'/>

All variables and imports are lost and the cell execution number returns to `1`:

<img src='./images/img_047.png' alt='img_047' width='600'/>

the script editor will display a list of identifiers from an `object` name after a `.`:

<img src='./images/img_048.png' alt='img_048' width='600'/>

The figure can be saved using:

```python
#%% Import Libraries
import numpy as np 
import matplotlib.pyplot as plt 
#%% Create Data
x = np.array([0, 1, 2, 3, 4,])
y = 2 * x
#%% Plot Data
plt.plot(x, y)
#%% Save Figure
plt.savefig('fig1.png')
```

<img src='./images/img_049.png' alt='img_049' width='600'/>

The entire Script file can be run, using Run File:

<img src='./images/img_050.png' alt='img_050' width='600'/>

the files pane displays the current working directory, which is the same folder, that the `script.py` file is stored in. Note `fig1.png` is also saved here:

<img src='./images/img_051.png' alt='img_051' width='600'/>

It can be opened externally:

<img src='./images/img_052.png' alt='img_052' width='600'/>

<img src='./images/img_053.png' alt='img_053' width='600'/>

The Variable `x` is a `ndarray` and can be expanded in the Variable Explorer:

<img src='./images/img_054.png' alt='img_054' width='600'/>

<img src='./images/img_055.png' alt='img_055' width='600'/>

If a deliberate mistake is made in the code, that would introduce a `SyntaxError` notice that the script editor displays a warning:

<img src='./images/img_056.png' alt='img_056' width='600'/>

The following code will run, but is not formatted correctly:

<img src='./images/img_057.png' alt='img_057' width='600'/>

Spacing issues can be corrected using the autopep8 formatter. Select format file or extension with autopep8:

<img src='./images/img_058.png' alt='img_058' width='600'/>

Notice the spacing is fixed:

<img src='./images/img_059.png' alt='img_059' width='600'/>

Spyder also has the opinionated formatter black, however black's opinionated formatting gives string quotations that are inconsistent to Python and Python standard libraries. Ruff integration with a ruff.toml file which can be used to specify a preferred quote option such as single quotes isn't available but is a planned feature:

<img src='./images/img_060.png' alt='img_060' width='600'/>

The Edit Menu can be used to Comment/Uncomment several lines of code:

<img src='./images/img_061.png' alt='img_061' width='600'/>

Notice an error is highlighted because the Variables `x` and `y` are used but not assigned:

<img src='./images/img_062.png' alt='img_062' width='600'/>

A custom function can be created:

```python
def greet_user(user_name):
    print(f'Hello {user_name}')
```

Note every line of code belonging to the code block is indented by 4 spaces:

<img src='./images/img_063.png' alt='img_063' width='600'/>

Blank spaces can be shown on the script editor by selecting source → show blank spaces:

<img src='./images/img_064.png' alt='img_064' width='600'/>

<img src='./images/img_065.png' alt='img_065' width='600'/>

A docstring template can be autogenerated for the function by inputting:

```python
def greet_user(user_name):
    """
    print(f'Hello {user_name}')
```

<img src='./images/img_066.png' alt='img_066' width='600'/>

<img src='./images/img_067.png' alt='img_067' width='600'/>

```python
def greet_user(user_name):
    """
    

    Parameters
    ----------
    user_name : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    print(f'Hello {user_name}')
```

This template can be filled out:

<img src='./images/img_068.png' alt='img_068' width='600'/>

```python
def greet_user(user_name):
    """
    greets the user

    Parameters
    ----------
    user_name : str
        The name of the user.

    Returns
    -------
    None.

    """
    print(f'Hello {user_name}')
```

Note code not part of the function is not indented:

```python
def greet_user(user_name):
    """
    greets the user

    Parameters
    ----------
    user_name : str
        The name of the user.

    Returns
    -------
    None.

    """
    print(f'Hello {user_name}')


print('Code not part of the function')
```

<img src='./images/img_069.png' alt='img_069' width='600'/>

Another cell can be made to call the function:

<img src='./images/img_070.png' alt='img_070' width='600'/>

The cell where the function was defined, will be collapsed, in order to optimise space:

<img src='./images/img_071.png' alt='img_071' width='600'/>

<img src='./images/img_072.png' alt='img_072' width='600'/>

Notice that when the function name is input:

```python
greet_user
```

that the docstring created displays:

<img src='./images/img_073.png' alt='img_073' width='600'/>

This function can be called and provided with the input string `'Philip'`:

```python
greet_user('Philip')
```

<img src='./images/img_074.png' alt='img_074' width='600'/>

When this script file is run, the function is called and the `print` function in the functions body is used to print `'Hello Philip'` which is shown in the cell output:

<img src='./images/img_075.png' alt='img_075' width='600'/>

In the above script file, the function is defined and called:

<img src='./images/img_076.png' alt='img_076' width='600'/>

If this script file is saved as another script file called `module.py`:

<img src='./images/img_077.png' alt='img_077' width='600'/>

<img src='./images/img_078.png' alt='img_078' width='600'/>

Both `script.py` and `module.py` can be viewed, side by side by selecting split horizontally:

<img src='./images/img_079.png' alt='img_079' width='600'/>

Both `script.py` and `module.py` are found in the same folder:

<img src='./images/img_080.png' alt='img_080' width='600'/>

This means that `module.py` can be imported in `script.py` using:

```python
import module # no file extension
```

<img src='./images/img_081.png' alt='img_081' width='600'/>

Identifiers from the module can be accessed using a `.`:

```python
import module 
module.
```

<img src='./images/img_082.png' alt='img_082' width='600'/>

If the panel with `module.py` is closed, code can be input in `script.py`:

<img src='./images/img_083.png' alt='img_083' width='600'/>

The function `greet_user` can be accessed from the imported `module`:

```python
import module 
module.greet_user('Philip')
```

When run, the print statement displays in the console:

<img src='./images/img_084.png' alt='img_084' width='600'/>

Alternatively an `object` such as a function can be imported from the `module`:

<img src='./images/img_085.png' alt='img_085' width='600'/>

```python
from module import user_greeting
```

<img src='./images/img_086.png' alt='img_086' width='600'/>

`exit` will be input to restart the kernel which prevents some issues such as reloading modules. Essentially when an instruction is made to reload a module, it will be skipped as there is a performance loss by loading the same module twice. This is problematic when working on the module as changes aren't reflected.

The function can be imported and called as before:

```python
from module import user_greeting
user_greeting('Philip')
```

<img src='./images/img_087.png' alt='img_087' width='600'/>

If the module `module.py` is copied into a subfolder `subfolder`. The module can be accessed from the subfolder by use of a `.` in this case:

```python
from subfolder.module import user_greeting
user_greeting('Philip')
```

<img src='./images/img_088.png' alt='img_088' width='600'/>

`module.py` can be copied to `__init__.py`. `__init__.py` is known as the initialisation file, that is imported when the folder is imported:


```python
from subfolder import user_greeting
user_greeting('Philip')
```

<img src='./images/img_089.png' alt='img_089' width='600'/>

Identifiers beginning with a **d**ouble **under**score `__` and ending in `__` are part of the Python datamodel, colloquially they are sometimes called dunder identifiers. These can be accessed from the `str` instance text by inputting:

```python
text = 'hello'
text.__
```

<img src='./images/img_090.png' alt='img_090' width='600'/>

In the console the data model identifiers can be viewed by inputting:

```python
text.__
```

followed by a `↹`:


<img src='./images/img_091.png' alt='img_091' width='600'/>

If the `__add__` data model identifier for example is selected and input with open parenthesis, the docstring displays:

```python
text.__add__(
```

Note the return value instructs the preferred `builtins` function or operator to use, in this case `+`:

```python
text + text
```

<img src='./images/img_092.png' alt='img_092' width='600'/>

The operator behind the scenes uses:

```python
text.__add__(text)
```

Where the `text` instance before the `.` is the `str` instance the method is called from known as `self`. The second instance provided in the function is known as `value`:

<img src='./images/img_093.png' alt='img_093' width='600'/>

This method is defined in the `str` class. Note when called from the `str` class, the instance `self` must be provided, in addition to the instance `value`:

```python
str.__add__(text, text)
```

There are a number of data model identifiers in the script file which can be accessed using `__` In this case the data model identifiers `__file__` and `__name__` will be examined:

<img src='./images/img_094.png' alt='img_094' width='600'/>

These can be printed in the script file:

```python
print(__file__)
print(__name__)
```

Note when this file is run, i.e. is the first input argument to the ipython magic `%runfile`, it is regarded as the main script file being executed and has the data model `__name__` as `'__main__'`:

<img src='./images/img_095.png' alt='img_095' width='600'/>

`module.py` and `script.py` can be opened side by side. If the following code is in `module`:

```python
print(__file__)
print(__name__)
```

And if the following code is in `script`:

```python
import module
```

<img src='./images/img_096.png' alt='img_096' width='600'/>

When `script.py` is run, the code in the `module` is run as it is imported. Notice that `__name__` is now `'module'` and not `'__main__'`. This is because the first input argument `%runfile` is `script.py` and this is the main script known as `'__main__'`:

<img src='./images/img_097.png' alt='img_097' width='600'/>

If `module.py` is updated to: 

```python
text = 'hello'

if __name__ == '__main__':
    print('Diagnostic Code')
```

<img src='./images/img_098.png' alt='img_098' width='600'/>

Note when `module` is run, the instance `text` is instantiated and is shown on the Variable Explorer. It is the `'__main__'` module and the diagnostic code prints:

<img src='./images/img_099.png' alt='img_099' width='600'/>

If the module is imported in `script.py`:

```python
import module
```

 the condition to the `if` code block is `False` because this is not the `'__main__'` module, so the diagnostic code does not run. The variable `module.text` is instantiated and can be accessed in the console:

<img src='./images/img_100.png' alt='img_100' width='600'/>

## ModuleNotFoundError

If Help → Dependencies is selected:

<img src='./images/img_101.png' alt='img_101' width='600'/>

A number of mandatory and optional dependencies are listed, which are include libraries from the scientific stack `numpy`, `pandas` and `matplotlib`:

<img src='./images/img_102.png' alt='img_102' width='600'/>

Notice `seaborn` is not listed. If it is attempted to be imported:

```python
import seaborn
```

There is a `ModuleNotFoundError`:

<img src='./images/img_103.png' alt='img_103' width='600'/>

`seaborn` is not installed.

## spyder-runtime Environment

Spyder uses its own `spyder-runtime` environment that is conda based (conda is a package manager that is closely associated with Python but is general purpose and can be used to install Python and non-Python data science packages). Spyder is installed in local application data:

```
%LOCALAPPDATA%
```

<img src='./images/img_104.png' alt='img_104' width='600'/>

There is a `spyder-6` subfolder:

<img src='./images/img_105.png' alt='img_105' width='600'/>

This folder contains the `base`, environment. In the scripts subfolder there is a `conda.exe`:

<img src='./images/img_106.png' alt='img_106' width='600'/>

<img src='./images/img_107.png' alt='img_107' width='600'/>

The Spyder installer is `conda` based, the purpose of the base environment is for use of the `conda.exe` which is a package manager that is used to install packages and create Python environments. There is an `envs` folder which contains (conda) Python environments:

<img src='./images/img_111.png' alt='img_111' width='600'/>

The (conda) Python environment `spyder-runtime` is in its own subfolder:

<img src='./images/img_112.png' alt='img_112' width='600'/>

The (conda) Python environment `spyder-runtime` environment has its own contains its `python.exe`. It has its own `Scripts` folder which contains the `spyder.exe` and it also has its own `Lib` subfolder which contains Python libraries associated with the `python.exe`:

<img src='./images/img_113.png' alt='img_113' width='600'/>

The root of the `Lib` folder containts the standard modules such as `datetime.py` which is a single script file:

<img src='./images/img_114.png' alt='img_114' width='600'/>

Or `email` which is a folder of script files, including the `__init__.py` which recall is imported when the folder is imported:

<img src='./images/img_115.png' alt='img_115' width='600'/>

The `site-packages` folder contains third-party libraries:

<img src='./images/img_116.png' alt='img_116' width='600'/>

This has the subfolder folder `numpy`:

<img src='./images/img_117.png' alt='img_117' width='600'/>

Which has its `__init__.py` file:

<img src='./images/img_118.png' alt='img_118' width='600'/>

There is also the subfolder `matplotlib`. This also has a `__init__.py` file. Typically for `matplotlib`, a module within the library is imported called `pyplot` opposed to the entire library:

<img src='./images/img_119.png' alt='img_119' width='600'/>

<img src='./images/img_120.png' alt='img_120' width='600'/>

Note that there is no `seaborn` subfolder as it is not preinstalled with Spyder.

The Spyder installer is `conda` based, the (conda) base Python environment is used to update `conda.exe`, which is in turn is used to update the `spyder-runtime` environment when there is a Spyder update available. This `conda.exe` is not intended to be used by the end user.

## Miniforge Installation

Miniforge is a minimal installer for `conda.exe` which uses the community channel `conda-forge` by default. The Miniforge (conda) base Python environment is used only for the `conda.exe` package manager and other packages are typically installed in separate Python environments, where they can be compartmentalised. Compartmentalisation allows installation of a set of packages without alteration to the (conda) base Python environment and therefore does not risk breaking the functionality of the conda package manager itself. 

There are a number of conda based installers:

|Installer|base environment|default channel|
|---|---|---|
|Miniforge|minimal (conda package manager)|conda-forge (community)|
|Mambaforge|minimal (conda + mamba package manager)|conda-forge (community)|
|Miniconda|minimal (conda package manager)|anaconda (commercial)|
|Anaconda|data science distribution (conda package manager)|anaconda (commercial)|

Mambaforge was a developmental version of Miniforge where the package manager `mamba.exe` was used in place of `conda.exe`. `mamba.exe` used a faster C++ solver offering a significant performance boost and increased reliability. The solver for `conda.exe` was updated to `lib-mamba` and now takes advantage of these developments. Miniforge now contains both the `conda.exe` (used by default and recommended for general use) and `mamba.exe` (which should essentially be thought of as a developmental version of `conda.exe`). Since Miniforge contains both these package managers, Mambaforge is now considered obsolete.

Anaconda/Miniconda use a tainted repository `anaconda` by default which has commercial restrictions and has significantly older package versions than on the community channel `conda-forge`. Anaconda is a data science distribution and Anaconda groups a large number of popular data science packages and tests them for stability with one another. This includes an odler version of the Spyder IDE and JupyterLab IDE. The Anaconda distribution is generally designed to be used "as is" and the stability is broken when other packages from the community channel are added. Using these significantly older packages result with the current version of Spyder results in incompatibilities because the current version of Spyder requires up to date packages.

Miniforge is developed on GitHub and the latest release is on the [GitHub Miniforge Releases Page](https://github.com/conda-forge/miniforge/releases). Note Mambaforge is considered obsolete and therefore the Mambaforge installers listed at the top should be avoided. 

For Windows the `Miniforge3-x.xx.x-x-Windows-x86_64.exe` or `Miniforge3-Windows-x86_64.exe` should be selected (these are the same installer):

<img src='./images/img_121.png' alt='img_121' width='600'/>

<img src='./images/img_122.png' alt='img_122' width='600'/>

Microsoft Edge may block the download, select the download and then select Keep:

<img src='./images/img_123.png' alt='img_123' width='600'/>

<img src='./images/img_124.png' alt='img_124' width='600'/>

<img src='./images/img_125.png' alt='img_125' width='600'/>

Launch the Miniforge setup:

<img src='./images/img_126.png' alt='img_126' width='600'/>

Select Next:

<img src='./images/img_127.png' alt='img_127' width='600'/>

Select I Agree:

<img src='./images/img_128.png' alt='img_128' width='600'/>

Select Just Me and Next:

<img src='./images/img_129.png' alt='img_129' width='600'/>

Install in the default location and select Next. This will be within:

```
%USERPROFILE%
```

<img src='./images/img_130.png' alt='img_130' width='600'/>

<img src='./images/img_131.png' alt='img_131' width='600'/>

<img src='./images/img_132.png' alt='img_132' width='600'/>

Select Install, using only the recommended options:

<img src='./images/img_133.png' alt='img_133' width='600'/>

During installation is not recommended to add the (conda) base Python environment to the Windows Environmental Variables Path as this locks a single environment to the Terminal and is less flexible than initialising the conda package manager which allows activation of different (conda) Python environments.

Select next:

<img src='./images/img_134.png' alt='img_134' width='600'/>

Select Finish:

<img src='./images/img_135.png' alt='img_135' width='600'/>

Miniforge will display in the Start Menu:

<img src='./images/img_136.png' alt='img_136' width='600'/>

When launched it displays `(base)`, indicating the `(base)` environment:

<img src='./images/img_137.png' alt='img_137' width='600'/>

Going to:

```
%USERPROFILE%
```

<img src='./images/img_138.png' alt='img_138' width='600'/>

<img src='./images/img_139.png' alt='img_139' width='600'/>

Then `Miniforge3`

<img src='./images/img_140.png' alt='img_140' width='600'/>

Shows the `python.exe` and associated `scripts` folder:

<img src='./images/img_141.png' alt='img_141' width='600'/>

The `conda.exe` is found here:

<img src='./images/img_142.png' alt='img_142' width='600'/>

## Initialising conda with the Windows Terminal

Right click the Start Button and select Terminal (Admin):

<img src='./images/img_143.png' alt='img_143' width='400'/>

Select Yes at the User Account Control:

<img src='./images/img_144.png' alt='img_144' width='400'/>

Notice the Windows Terminal has no `(base)` because it is not initialised:

<img src='./images/img_145.png' alt='img_145' width='600'/>

To initialise conda, the Windows Terminal script execution policy should be changed, to `RemoteSigned`. The Windows Terminal script execution policy has the following options:

* Restricted (default): Disables script execution entirely.
* RemoteSigned: Allows digitally signed remote scripts to be executed and local scripts to be executed.
* Unrestricted: Allows all scripts to run, but prompts for confirmation for remote scripts.
* AllSigned: Requires all scripts (local and remote) to be digitally signed.

To change the execution policy input:

```powershell
Set-ExecutionPolicy RemoteSigned
```

Note this lowers the default security level of the Windows Terminal to `RemoteSigned` which is often chosen as a middle ground between security and usability. `RemoteSigned` means scripts downloaded from the internet require a trusted digital signature in order to execute, an example of this is the `conda.exe` initialisation script. Scripts created locally by the current user can be run without a digital signature.

<img src='./images/img_146.png' alt='img_146' width='600'/>

Then the `conda.exe` can be initialised by inputting:

```powershell
.\miniforge3\Scripts\conda init --all
```

<img src='./images/img_147.png' alt='img_147' width='600'/>

Details about the changes will be listed, close the Terminal:

<img src='./images/img_148.png' alt='img_148' width='600'/>

Right click the Start button and select Terminal (Non-Admin). The Admin version was required previously to change the Execution Policy, in this case the Windows Terminal is being used by the user for use within the `%UserProfile%`:

<img src='./images/img_149.png' alt='img_149' width='400'/>

Notice it now has the `(base)` prefix, indicating that the base (conda) Python environment is activated:

<img src='./images/img_150.png' alt='img_150' width='600'/>

## Creating a Custom spyder-env Environment (conda)

Before using the package manager `conda.exe` it should be updated to the latest version using:

```python
conda update conda
```

<img src='./images/img_151.png' alt='img_151' width='600'/>

Since Miniforge is used, the channel will be `conda-forge` by default:

<img src='./images/img_152.png' alt='img_152' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_153.png' alt='img_153' width='600'/>

The `conda.exe` package manager is now updated:

<img src='./images/img_154.png' alt='img_154' width='600'/>

Inputting:

```powershell
cls
```

will **cl**ear the **s**creen:

<img src='./images/img_155.png' alt='img_155' width='600'/>

A new environment can be created using:

```powershell
conda create -n spyder-env spyder-kernels python seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt ffmpeg ruff
```

This has `spyder-kernels` which is required for Spyder to use the environment. `seaborn` which has `numpy`, `pandas` and `matplotlib` as dependencies. `scikit-learn` for machine learning. `pyarrow`, `openpyxl`, `xlrd`, `xlsxwriter`, `lxml`, `sqlalchemy`, `tabulate` for various file pandas formats. `pyqt` for matplotlib's interactive backend and `ffmpeg` for saving matplotlib animations.

`-n` means name and `spyder-env` is the name of the Python environment. Specifying an environment using `-n` means changes to that environment will be made opposed to `base` which is the currently activate environment.

<img src='./images/img_156.png' alt='img_156' width='600'/>

These packages will all be installed from the `conda-forge` channel and installed compartmentalised in the (conda) Python environment `spyder-env`. `spyder-env` is a subfolder which is found in the `envs` subfolder of the `base` Miniforge installation `%UserProfile%/Miniforge3`:

<img src='./images/img_157.png' alt='img_157' width='600'/>

Details about packages to be downloaded will be shown:

<img src='./images/img_158.png' alt='img_158' width='600'/>

Details about packages to be installed will be shown:

<img src='./images/img_159.png' alt='img_159' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_160.png' alt='img_160' width='600'/>

The packages are installed in the environment but it is not activated:

<img src='./images/img_161.png' alt='img_161' width='600'/>

To activate it use:

```powershell
conda activate spyder-env
```

<img src='./images/img_162.png' alt='img_162' width='600'/>

Notice the prefix is now `(spyder-env)` meaning the (conda) Python environment `spyder-env` is activated:

<img src='./images/img_163.png' alt='img_163' width='600'/>

An `ipython` shell can be launched:

<img src='./images/img_164.png' alt='img_164' width='600'/>

Notice two programming languages are used, highlighted is PowerShell using the programming language PowerShell and below is the ipython shell using the python programming language:

<img src='./images/img_165.png' alt='img_165' width='600'/>

If `email`, `datetime`, `numpy`, `matplotlib`, `pandas` and `seaborn` are imported, their `__file__` can be checked. Notice these are found in the `spyder-env` environment: 

<img src='./images/img_166.png' alt='img_166' width='600'/>

## Selecting the Custom spyder-env Environment (conda)

In Spyder, the default (conda) Python nvironment `spyder-runtime` is selected:

<img src='./images/img_167.png' alt='img_167' width='600'/>

Go to Tools → Preferences:

<img src='./images/img_168.png' alt='img_168' width='600'/>

Select IPython Interpretter:

<img src='./images/img_169.png' alt='img_169' width='600'/>

Select Use the Following Interpretter and select `spyder-env` (conda) from the dropdown list:

<img src='./images/img_170.png' alt='img_170' width='600'/>

Select Apply:

<img src='./images/img_171.png' alt='img_171' width='600'/>

Close Spyder and relaunch. `spyder-env` should be shown at the bottom and now seaborn can be imported:

```python
import seaborn as sns
```

<img src='./images/img_172.png' alt='img_172' width='600'/>

## MikTek Installation

MikTex is required in order to use TeX in matplotlib. MikTex can be downloaded from its software download page [MikTeX Downloads](https://miktex.org/download):

<img src='./images/img_173.png' alt='img_173' width='600'/>

<img src='./images/img_174.png' alt='img_174' width='600'/>

Launch the installer:

<img src='./images/img_175.png' alt='img_175' width='600'/>

Accept the License Agreement and select Next:

<img src='./images/img_176.png' alt='img_176' width='600'/>

Select Install only for me and select Next:

<img src='./images/img_177.png' alt='img_177' width='600'/>

Use the default file location in:

```
%LOCALAPPDATA%
```

and select Next:

<img src='./images/img_178.png' alt='img_178' width='600'/>

Select Next:

<img src='./images/img_179.png' alt='img_179' width='600'/>

Select Start:

<img src='./images/img_180.png' alt='img_180' width='600'/>

Select Next:

<img src='./images/img_181.png' alt='img_181' width='600'/>

Select Next:

<img src='./images/img_182.png' alt='img_182' width='600'/>

Select Close:

<img src='./images/img_183.png' alt='img_183' width='600'/>

MikTeX will display in the notification tray, select it:

<img src='./images/img_184.png' alt='img_184' width='400'/>

Select Updates and select Update Now:

<img src='./images/img_185.png' alt='img_185' width='600'/>

Close the MikTeX Console to update the MikTex Console:

<img src='./images/img_186.png' alt='img_186' width='600'/>

Select Packages and search for `type1cm`, select Install:

<img src='./images/img_187.png' alt='img_187' width='600'/>

Select OK:

<img src='./images/img_188.png' alt='img_188' width='600'/>

Repeat for `cm-super`, `geometry`, `underscore`, and `zhmetrics`.

## Changing Default Plot Backend

The default plot backend can be changed, by selecting Tools → Preferences:

<img src='./images/img_189.png' alt='img_189' width='600'/>

Then IPython Console → Graphics and changing the backend to Qt:

<img src='./images/img_190.png' alt='img_190' width='600'/>

If the following is plotted:

```python
#%% Import Libraries
import numpy as np 
import matplotlib.pyplot as plt 
#%% Create Data
x = np.array([0, 1, 2, 3, 4,])
y = 2 * np.pi * np.sin(x)
#%% Plot Data
plt.plot(x, y)
plt.xlabel(R'$x$', usetex=True)
plt.ylabel(R'$2 \pi \sin{x}$', usetex=True)
```

<img src='./images/img_191.png' alt='img_191' width='600'/>

Tex will render in the figure labels. This may take a couple of minutes for the first plot with TeX, while matplotlib configures the system fonts.

## PowerToys

The automatic backend does not stay on top, when Spyder is selected, the plot is behind Spyder:

<img src='./images/img_192.png' alt='img_192' width='600'/>

This can be changed using PowerToys. PowerToys is developed on GitHub and the latest release is on the [GitHub Spyder Releases Page](https://github.com/microsoft/PowerToys/releases). Select the Per User Installer:

<img src='./images/img_193.png' alt='img_193' width='600'/>

<img src='./images/img_194.png' alt='img_194' width='600'/>

Launch the installer:

<img src='./images/img_195.png' alt='img_195' width='600'/>

Select I Agree to the License Terms and Conditions:

<img src='./images/img_196.png' alt='img_196' width='600'/>

Select Close:

<img src='./images/img_197.png' alt='img_197' width='400'/>

The shortcut key `⊞`, `Alt` + `t` can be usd to toggle on/of Always On Top:

<img src='./images/img_198.png' alt='img_198' width='600'/>

<img src='./images/img_199.png' alt='img_199' width='600'/>

This allows modification and visualisation of the plot using the console.

Other useful tools are available such as a color picker which is activated using `⊞`, `⇧` + `c`:

<img src='./images/img_200.png' alt='img_200' width='600'/>

<img src='./images/img_201.png' alt='img_201' width='600'/>

<img src='./images/img_202.png' alt='img_202' width='400'/>

## Updating

There is a new release of Spyder, approximately every month. When available a prompt for the upgrade should display and Spyder should update using packages from `conda-forge` using its internal `conda` package manager:



If an external conda environment was created, it will also need to be updated, with a compatible version of `spyder-kernels`. Open up the Windows Terminal and update the `conda.exe` package manager to the latest version, recall this is found in the (codna) base Python environment:

```powershell
conda update conda
```

Then activate the (conda) Python environment `spyder-env` and search for updates to all packages using `--all`:

```powershell
conda activate spyder-env
conda update --all
```

[Return to Python Tutorials](../readme.md)