# Spyder IDE Ubuntu Setup

## Linux Terminal

The Linux Terminal can be opened from the Start Menu or using the shortcut `Ctrl`, `Alt` + `t`:

<img src='./images/img_001.png' alt='img_001' width='600'/>

The Linux Terminal uses the `bash` programming language by default. The bash prompt begins with:

```bash
user@pcname
```

<img src='./images/img_002.png' alt='img_002' width='600'/>

Followed by the current working directory:

```bash
~
```

Followed by a:

```bash
$
```

<img src='./images/img_003.png' alt='img_003' width='600'/>

Where `~` means the Home directory:

<img src='./images/img_004.png' alt='img_004' width='600'/>

If Other Locations are selected:

<img src='./images/img_005.png' alt='img_005' width='600'/>

there is a `usr` folder:

<img src='./images/img_006.png' alt='img_006' width='600'/>

Which contains a binary `bin` folder:

<img src='./images/img_007.png' alt='img_007' width='600'/>

This contains the binaries that can be ran from the Terminal. On Ubuntu, which is Debian based there is the package manager `apt`:

<img src='./images/img_008.png' alt='img_008' width='600'/>

When:

```bash
apt
```

is input, this binary is executed:

<img src='./images/img_009.png' alt='img_009' width='600'/>

the binary `clear` may be used to clear the Terminal:

```bash
clear
```

<img src='./images/img_010.png' alt='img_010' width='600'/>

<img src='./images/img_011.png' alt='img_011' width='600'/>

There is also a `bin` folder on the root of the drive, which is the binaries used by the system:

<img src='./images/img_012.png' alt='img_012' width='600'/>

To install packages, system wide using `apt`, the prefix `sudo` is used, which stands for super user do:

```bash
sudo apt
```

<img src='./images/img_013.png' alt='img_013' width='600'/>

Switching to a super user will prompt for authentication. Input your account password in order to proceed:

<img src='./images/img_014.png' alt='img_014' width='600'/>

<img src='./images/img_015.png' alt='img_015' width='600'/>

<img src='./images/img_016.png' alt='img_016' width='600'/>

Details about commands available to use with the `apt` binary are shown. the `install` command can be used to install a number of TeX fonts (which will later be used by matplotlib):

```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic cm-super dvipng
```

To copy and paste in the terminal, use the right click or keyboard shortcut keys `Ctrl`, `⇧` + `c` or `Ctrl`, `⇧` + `v`:

<img src='./images/img_017.png' alt='img_017' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_018.png' alt='img_018' width='600'/>

The packages will be downloaded and installed:

<img src='./images/img_019.png' alt='img_019' width='600'/>

Returning to the `usr` folder:

<img src='./images/img_020.png' alt='img_020' width='600'/>

The user `bin` folder can be examined:

<img src='./images/img_021.png' alt='img_021' width='600'/>

Notice there is the programming languages `bash` and `python3`:

<img src='./images/img_022.png' alt='img_022' width='600'/>

<img src='./images/img_023.png' alt='img_023' width='600'/>

If a new Terminal is opened without super user privileges, `python3` can be launched using:

```bash
python3
```

Notice the prompt changes as a different programming language is now used:

<img src='./images/img_024.png' alt='img_024' width='600'/>

if the `datetime` module is imported, its `__file__` attribute can be examined:

```python
>>> import datetime
>>> datetime.__file__
'/usr/lib/python3.12/datetime.py'
```
<img src='./images/img_025.png' alt='img_025' width='600'/>

Note the Python standard library is found in the `lib ` subfolder, this can be examined:

<img src='./images/img_026.png' alt='img_026' width='600'/>

There is a `python3.12` subfolder:

<img src='./images/img_027.png' alt='img_027' width='600'/>

Which contains the standard modules such as`datetime.py`:

<img src='./images/img_028.png' alt='img_028' width='600'/>

Some standard modules have multiple script files and are contained in a folder. This folder has the data model initialisation file `__init__` which is imported when the folder is imported:

```python
>>> import email
>>> email.__file__
'/usr/lib/python3.12/email/__init__.py'
```

<img src='./images/img_029.png' alt='img_029' width='600'/>

<img src='./images/img_030.png' alt='img_030' width='600'/>

<img src='./images/img_031.png' alt='img_031' width='600'/>

Note the absence of the `site-packages` subfolder:

<img src='./images/img_032.png' alt='img_032' width='600'/>

This means no third-party libraries are installed. Therefore if `numpy` is attempted to be imported::

```python
>>> import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

<img src='./images/img_033.png' alt='img_033' width='600'/>

The python shell can be exited using the `exit` function:

```python
exit()
```

<img src='./images/img_034.png' alt='img_034' width='600'/>

This returns to the bash shell:

<img src='./images/img_035.png' alt='img_035' width='600'/>

This can be cleared using:

```bash
clear
```

<img src='./images/img_036.png' alt='img_036' width='600'/>

If text editor is opened:

<img src='./images/img_037.png' alt='img_037' width='600'/>

<img src='./images/img_038.png' alt='img_038' width='600'/>

The file can be saved using File → Save As:

<img src='./images/img_039.png' alt='img_039' width='600'/>

The file is saved in Documents:

<img src='./images/img_040.png' alt='img_040' width='600'/>

Using the file name `script.py` with the `.py` file extension. This means the text editor, will apply Python syntax highlighting:

<img src='./images/img_041.png' alt='img_041' width='600'/>

The following Python code can be input:

```python
print('Hello World!')
```

<img src='./images/img_042.png' alt='img_042' width='600'/>

The Documents folder can be opened in the Terminal, by right clicking empty space in the folder and selecting Open in Terminal:

<img src='./images/img_043.png' alt='img_043' width='600'/>

Notice the path is now `~/Documents`:

<img src='./images/img_044.png' alt='img_044' width='600'/>

The path can be changed using the binary `cd` which stands for change directory. `..` means the parent folder:

```bash
cd ..
```

<img src='./images/img_045.png' alt='img_045' width='600'/>

<img src='./images/img_046.png' alt='img_046' width='600'/>

`.` means in the same folder as. In this case `Downloads` is a subfolder of `~`:

```bash
cd ./Downloads
```

<img src='./images/img_047.png' alt='img_047' width='600'/>

To go back to Documents, the parent folder can be accessed and `Documents` selected from is:

```bash
cd ../Documents
```

<img src='./images/img_048.png' alt='img_048' width='600'/>

The `~` means Home:

```bash
cd ~
```

<img src='./images/img_049.png' alt='img_049' width='600'/>

And Documents can be selected frm Home using:

```bash
cd ~/Documents
```

<img src='./images/img_050.png' alt='img_050' width='600'/>

The binary `ls` will list all the files and folders in the current working directory:

```bash
ls

```

<img src='./images/img_051.png' alt='img_051' width='600'/>

The binary `python3` can be run supplying the script file as a command line input argument:

```bash
python3 script.py
```

<img src='./images/img_052.png' alt='img_052' width='600'/>

The print statement displays:

<img src='./images/img_053.png' alt='img_053' width='600'/>

If another file is created in the text editor, this time with the extension `.sh`:

<img src='./images/img_054.png' alt='img_054' width='600'/>

<img src='./images/img_055.png' alt='img_055' width='600'/>

<img src='./images/img_056.png' alt='img_056' width='600'/>

bash is a slightly different scripting language to Python, optimised for navigation around the operating system. If the following is input:

```bash
echo "Hello World!"
```

<img src='./images/img_057.png' alt='img_057' width='600'/>

The binary `ls` can be used to view all the files:

```bash
ls
```

<img src='./images/img_058.png' alt='img_058' width='600'/>

The binary `bash` can be run supplying the script file as a command line input argument:

```bash
bash script.sh
```

<img src='./images/img_059.png' alt='img_059' width='600'/>

## Downloading and Installing Spyder

Spyder is developed on GitHub and the latest release is on the [GitHub Spyder Releases Page](https://github.com/spyder-ide/spyder/releases). Select the Linux Installer:

<img src='./images/img_060.png' alt='img_060' width='600'/>

Notice that this is `.sh` Shell Script:

<img src='./images/img_061.png' alt='img_061' width='600'/>

<img src='./images/img_062.png' alt='img_062' width='600'/>

Right click the Downloads folder and select Open in Terminal:

<img src='./images/img_063.png' alt='img_063' width='600'/>

This script can be ran using `bash`:

<img src='./images/img_064.png' alt='img_064' width='600'/>

Input:

```bash
bash S↹
```

And the file name should auto-complete:

<img src='./images/img_065.png' alt='img_065' width='600'/>


```bash
bash Spyder-Linux-x86_64.sh
```

Press `↵` to execute the script:

<img src='./images/img_066.png' alt='img_066' width='600'/>

Press `↵` to begin scrolling through the license agreement:

<img src='./images/img_067.png' alt='img_067' width='600'/>

Press `q` to quit scrolling:

<img src='./images/img_068.png' alt='img_068' width='600'/>

To accept the license agreement input `yes` and press `↵`:

<img src='./images/img_069.png' alt='img_069' width='600'/>

To install in the default location press `↵`:

<img src='./images/img_070.png' alt='img_070' width='600'/>

Spyder is now installed and a Start Menu shortcut is now created:

<img src='./images/img_071.png' alt='img_071' width='600'/>

## Spyder IDE Basics

When Spyder is first launched, a prompt to begin a tour will display:

<img src='./images/img_072.png' alt='img_072' width='600'/>

To the bottom right is the IPython Console, where commands can be input individually. Notice the cells are numbered, by execution oder. The code can be input:

```python
In [1]: 'hello'
Out[1]: 'hello'
```

<img src='./images/img_073.png' alt='img_073' width='600'/>

This value was input and returned as an output. the value can also be assigned to an object name using the `=` operator:

```python
In [2]: text = 'hello'
```

<img src='./images/img_074.png' alt='img_074' width='600'/>

This object name `text` displays on the Variable Explorer. It has the type `str`. The identifiers from the `str` class can  be accessed from `text` by typing in `text.` followed by a `↹`:

<img src='./images/img_075.png' alt='img_075' width='600'/>

If part of an identifier is input for example `text.cap` followed by a `↹`, the identifier `text.capitalize` will display:

<img src='./images/img_076.png' alt='img_076' width='600'/>

<img src='./images/img_077.png' alt='img_077' width='600'/>

When this is input, the method is referenced and the output displays where the method is defined, in this case, in the `str` class:

```python
In [3]: text.capitalize
Out[3]: <function str.capitalize()>
```

<img src='./images/img_078.png' alt='img_078' width='600'/>

A method is called using parenthesis, the docstring displays, which provided details about any input parameters:

<img src='./images/img_079.png' alt='img_079' width='600'/>

A new `str` instance is returned to the console:

```python
In [4]: text.capitalize()
Out[4]: 'Hello'
```

<img src='./images/img_080.png' alt='img_080' width='600'/>

Note `text` remains assigned to the original `str` instance `'hello'`. This new `str` instance can be assigned to `text` which reassigns the value of `text`. The right hand side is carried out first (using the original value of `text` which was `hello`)

```python
In [5]: text.capitalize()
```

This is then reassigned to the `object` name on the right hand side

```python
In [5]: text = text.capitalize()
```

The value of the new instance now displays under `text` in the Variable Explorer:

<img src='./images/img_081.png' alt='img_081' width='600'/>

<img src='./images/img_082.png' alt='img_082' width='600'/>

Other methods such as `replace` can be examined. A docstring displays showing the mandatory positional parameters `old` (position `0`) and `new` (position `1`). This is followed by the optional parameter `value` (position `2`) which has a default value `-1`, meaning all replacements of the old substring will be replaced with the new substring. Any parameter provided before the `/` must be supplied positionally only:

<img src='./images/img_083.png' alt='img_083' width='600'/>

The identifier can be inspected, by right clicking the identifier and pressing inspect or `Ctrl` + `i`:

<img src='./images/img_084.png' alt='img_084' width='600'/>

This displays documentation in the `help` pane:

<img src='./images/img_085.png' alt='img_085' width='600'/>

```python
In [6]: text.replace('ll', '7')
Out[6]: 'He7o'
```

Using named parameters:

```python
In [7]: text.replace(old='ll', new='7')
```

is not allowed because these parameters occur before the `/` in the docstring

<img src='./images/img_086.png' alt='img_086' width='600'/>

The a new `str` instance is returned which ahs the specified replacement:

<img src='./images/img_087.png' alt='img_087' width='600'/>

Spyder has a script editor.

<img src='./images/img_088.png' alt='img_088' width='600'/>

The script file can be saved in Documents as `script.py`:

<img src='./images/img_089.png' alt='img_089' width='600'/>

<img src='./images/img_090.png' alt='img_090' width='600'/>

<img src='./images/img_091.png' alt='img_091' width='600'/>

<img src='./images/img_092.png' alt='img_092' width='600'/>

In a Python script the `#` means a comment:

```python
# Import Libraries
import numpy as np # numeric python library
import matplotlib.pyplot as plt # matrix plotting library
```

<img src='./images/img_093.png' alt='img_093' width='600'/>

Using `#%%` creates a cell:

```python
#%% Import Libraries
import numpy as np 
import matplotlib.pyplot as plt 
```

Cells can be collapsed:

<img src='./images/img_094.png' alt='img_094' width='600'/>

<img src='./images/img_095.png' alt='img_095' width='600'/>

Identifiers display if a `.` is used following an `object` name. If the identifier is a docstring, the docstring will display:

<img src='./images/img_096.png' alt='img_096' width='600'/>

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
<img src='./images/img_097.png' alt='img_097' width='600'/>

A cell from a script file can be ran using the run cell button:

<img src='./images/img_098.png' alt='img_098' width='600'/>

This cell is still highlighted after execution. The cell and advance to the next cell button is more useful when running through each cell in a script file:

<img src='./images/img_099.png' alt='img_099' width='600'/>

<img src='./images/img_100.png' alt='img_100' width='600'/>

The Variables `x` and `y` display in the Variable Explorer:

<img src='./images/img_101.png' alt='img_101' width='600'/>

The plot displays as a static image using the `inline` backend. This static images displays on the plots pane:

<img src='./images/img_102.png' alt='img_102' width='600'/>

The plotting backend can be changed to an interactive plot using the `qtagg` backend:

<img src='./images/img_103.png' alt='img_103' width='600'/>

<img src='./images/img_104.png' alt='img_104' width='600'/>

If the last line is selected, the currently selected selection can be run:

<img src='./images/img_105.png' alt='img_105' width='600'/>

The plot now displays in its own window:

<img src='./images/img_106.png' alt='img_106' width='600'/>

The kernel can be restarted, removing all variables and imports by selecting Consoles → Restart Kernel and then selecting Yes. Alternatively typing `exit` into the console restarts the kernel:

<img src='./images/img_107.png' alt='img_107' width='600'/>

<img src='./images/img_108.png' alt='img_108' width='600'/>

All variables and imports are lost and the cell execution number returns to `1`:

<img src='./images/img_109.png' alt='img_109' width='600'/>

the script editor will display a list of identifiers from an `object` name after a `.`:

<img src='./images/img_110.png' alt='img_110' width='600'/>

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

<img src='./images/img_111.png' alt='img_111' width='600'/>

The entire Script file can be run, using Run File:

<img src='./images/img_112.png' alt='img_112' width='600'/>

the files pane displays the current working directory, which is the same folder, that the `script.py` file is stored in. Note `fig1.png` is also saved here:

<img src='./images/img_113.png' alt='img_113' width='600'/>

It can be opened externally:

<img src='./images/img_114.png' alt='img_114' width='600'/>

<img src='./images/img_115.png' alt='img_115' width='600'/>

If a deliberate mistake is made in the code, that would introduce a `SyntaxError` notice that the script editor displays a warning:

<img src='./images/img_116.png' alt='img_116' width='600'/>

The following code will run, but is not formatted correctly:

<img src='./images/img_117.png' alt='img_117' width='600'/>

Spacing issues can be corrected using the autopep8 formatter. Select format file or extension with autopep8:

<img src='./images/img_118.png' alt='img_118' width='600'/>

Spyder also has the opinionated formatter black, however black's opinionated formatting gives string quotations that are inconsistent to Python and Python standard libraries. Ruff integration with a ruff.toml file which can be used to specify a preferred quote option such as single quotes isn't available but is a planned feature:

<img src='./images/img_119.png' alt='img_119' width='600'/>

A custom function can be created:

```python
def greet_user(user_name):
    |
```

Note every line of code belonging to the code block is indented by 4 spaces:

<img src='./images/img_120.png' alt='img_120' width='600'/>

Blank spaces can be shown on the script editor by selecting source → show blank spaces:

<img src='./images/img_121.png' alt='img_121' width='600'/>

<img src='./images/img_122.png' alt='img_122' width='600'/>

The function can be completed:

```python
def greet_user(user_name):
    print(f'Hello {user_name}')
```

<img src='./images/img_123.png' alt='img_123' width='600'/>

A docstring template can be autogenerated for the function by inputting:

```python
def greet_user(user_name):
    """
    print(f'Hello {user_name}')
```

<img src='./images/img_124.png' alt='img_124' width='600'/>

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

<img src='./images/img_125.png' alt='img_125' width='600'/>

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

<img src='./images/img_126.png' alt='img_126' width='600'/>

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

<img src='./images/img_127.png' alt='img_127' width='600'/>

Another cell can be made to call the function:

<img src='./images/img_128.png' alt='img_128' width='600'/>

Notice that when the function name is input:

```python
greet_user
```

that the docstring created displays:

<img src='./images/img_129.png' alt='img_129' width='600'/>

This function can be called and provided with the input string `'Philip'`:

```python
greet_user('Philip')
```

<img src='./images/img_130.png' alt='img_130' width='600'/>

When this script file is run, the function is called and the `print` function in the functions body is used to print `'Hello Philip'` which is shown in the cell output:

<img src='./images/img_131.png' alt='img_131' width='600'/>

In the above script file, the function is defined and called. If this script file is saved as another script file called `module.py`:

<img src='./images/img_132.png' alt='img_132' width='600'/>

<img src='./images/img_133.png' alt='img_133' width='600'/>

Both `script.py` and `module.py` can be viewed, side by side by selecting split horizontally:

<img src='./images/img_134.png' alt='img_134' width='600'/>

Both `script.py` and `module.py` are found in the same folder:

<img src='./images/img_135.png' alt='img_135' width='600'/>

In `module.py` where the function is defined and called, the calling of the function can be commented out. Multiple lines of code can be commented out by highlighting them and selecting Edit → Comment/Uncomment:

<img src='./images/img_136.png' alt='img_136' width='600'/>

This prevents these lines of code from being executed but doesn't delete them, so they can be uncommented out later on:

<img src='./images/img_137.png' alt='img_137' width='600'/>

This means that `module.py` can be imported in `script.py` using:

```python
import module # no file extension
```

<img src='./images/img_138.png' alt='img_138' width='600'/>

Identifiers from the module can be accessed using a `.`:

```python
import module 
module.
```

<img src='./images/img_139.png' alt='img_139' width='600'/>

The function `greet_user` can be accessed from the imported `module`:

<img src='./images/img_140.png' alt='img_140' width='600'/>

If the panel with `module.py` is closed, code can be input in `script.py`:

<img src='./images/img_141.png' alt='img_141' width='600'/>

<img src='./images/img_142.png' alt='img_142' width='600'/>

If the panel with `module.py` is closed, code can be input in `script.py`:

```python
import module 
module.greet_user('Philip')
```

When run, the print statement displays in the console:

<img src='./images/img_143.png' alt='img_143' width='600'/>

`exit` will be input to restart the kernel which prevents some issues such as reloading modules. Essentially when an instruction is made to reload a module, it will be skipped as there is a performance loss by loading the same module twice. This is problematic when working on the module as changes aren't reflected:

<img src='./images/img_144.png' alt='img_144' width='600'/>

<img src='./images/img_145.png' alt='img_145' width='600'/>

An instruction can be made to import an identifier from a module, notice that the code completion displays the identifier `user_greeting`:

```python
from module import u
```

<img src='./images/img_146.png' alt='img_146' width='600'/>

```python
from module import user_greeting
```

<img src='./images/img_147.png' alt='img_147' width='600'/>

And the function can be called as before:

```python
from module import user_greeting
user_greeting('Philip')
```

<img src='./images/img_148.png' alt='img_148' width='600'/>

`exit` is used to restart the kernel. If the module `module.py` is copied into a subfolder `subfolder`. The module can be accessed from the subfolder by use of a `.` in this case:

```python
from subfolder.module import user_greeting
user_greeting('Philip')
```

<img src='./images/img_149.png' alt='img_149' width='600'/>

`exit` is used to restart the kernel. `module.py` can be copied and renamed to `__init__.py`. `__init__.py` is known as the initialisation file, that is imported when the folder is imported:

```python
from subfolder import user_greeting
user_greeting('Philip')
```

<img src='./images/img_150.png' alt='img_150' width='600'/>

Identifiers beginning with a **d**ouble **under**score `__` and ending in `__` are part of the Python datamodel, colloquially they are sometimes called dunder identifiers. These can be accessed from the `str` instance text by inputting:

```python
text = 'hello'
text.__
```

<img src='./images/img_151.png' alt='img_151' width='600'/>

In the console the data model identifiers can be viewed by inputting:

```python
text.__
```

followed by a `↹`:

<img src='./images/img_152.png' alt='img_152' width='600'/>

If the `__add__` data model identifier for example is selected and input with open parenthesis, the docstring displays:

```python
text.__add__(
```

Note the return value instructs the preferred `builtins` function or operator to use, in this case `+`:

```python
text + text
```

<img src='./images/img_153.png' alt='img_153' width='600'/>

<img src='./images/img_154.png' alt='img_154' width='600'/>

The operator behind the scenes uses:

```python
text.__add__(text)
```

Where the `text` instance before the `.` is the `str` instance the method is called from known as `self`. The second instance provided in the function is known as `value`:

<img src='./images/img_155.png' alt='img_155' width='600'/>

<img src='./images/img_156.png' alt='img_156' width='600'/>

This method is defined in the `str` class. Note when called from the `str` class, the instance `self` must be provided, in addition to the instance `value`:

```python
str.__add__(text, text)
```

<img src='./images/img_157.png' alt='img_157' width='600'/>

<img src='./images/img_158.png' alt='img_158' width='600'/>

There are a number of data model identifiers in the script file which can be accessed using `__` In this case the data model identifiers `__file__` and `__name__` will be examined:

<img src='./images/img_159.png' alt='img_159' width='600'/>

These can be accessed in the script file:

```python
__file__
__name__
```

However will not be shown in the console when the script file is run.

<img src='./images/img_160.png' alt='img_160' width='600'/>

To view these in the console, they can be printed in the script file:

```python
print(__file__)
print(__name__)
```

<img src='./images/img_161.png' alt='img_161' width='600'/>

Note when this file is run, i.e. is the first input argument to the ipython magic `%runfile`, it is regarded as the main script file being executed and has the data model `__name__` as `'__main__'`:

<img src='./images/img_162.png' alt='img_162' width='600'/>

`module.py` and `script.py` can be opened side by side. If the following code is in `module`:

```python
print(__file__)
print(__name__)
```

And if the following code is in `script`:

```python
import module
```

When `script.py` is run, the code in the `module` is run as it is imported. Notice that `__name__` is now `'module'` and not `'__main__'`. This is because the first input argument `%runfile` is `script.py` and this is the main script known as `'__main__'`:

<img src='./images/img_163.png' alt='img_163' width='600'/>

If `module.py` is updated to: 

```python
text = 'hello'

if __name__ == '__main__':
    print('Diagnostic Code')
```

When the kernel is restarted and `module` is run, the instance `text` is instantiated and is shown on the Variable Explorer. It is the `'__main__'` module and the diagnostic code prints:

<img src='./images/img_164.png' alt='img_164' width='600'/>

If the module is imported in `script.py`:

```python
import module
```

the condition to the `if` code block is `False` because this is not the `'__main__'` module, so the diagnostic code does not run. The variable `module.text` is instantiated and can be accessed in the console:


<img src='./images/img_165.png' alt='img_165' width='600'/>

## ModuleNotFoundError

The following standard modules can be imported and the `__file__` attribute of the modules can be checked:

```python
In [4]: import datetime
In [5]: datetime.__file__
Out[5]: '/home/philip/.local/spyder-6/envs/spyder-runtime/lib/python3.11/datetime.py'
```

```python
In [6]: import email
In [7]: email__file__
Out[7]: '/home/philip/.local/spyder-6/envs/spyder-runtime/lib/python3.11/email/__init__.py'
```

<img src='./images/img_166.png' alt='img_166' width='600'/>

The following third-party libraries can be imported and the `__file__` attribute of the modules can be checked:

```python
In [8]: import numpy as np
In [9]: np.__file__
Out[9]: '/home/philip/.local/spyder-6/envs/spyder-runtime/lib/python3.11/site-packages/numpy/__init__.py'
```

```python
In [10]: import matplotlib.pyplot as plt
In [11]: plt.__file__
Out[11]: '/home/philip/.local/spyder-6/envs/spyder-runtime/lib/python3.11/site-packages/matplotlib/pyplot.py'
```

Note that `pyplot` is a module in the library `matplotlib`.

<img src='./images/img_167.png' alt='img_167' width='600'/>

If Help → Dependencies is selected:

<img src='./images/img_168.png' alt='img_168' width='600'/>

A number of mandatory and optional dependencies are listed, which are include libraries from the scientific stack `numpy`, `pandas` and `matplotlib`:

<img src='./images/img_169.png' alt='img_169' width='600'/>

Notice `seaborn` is not listed. If it is attempted to be imported:

```python
import seaborn
```

There is a `ModuleNotFoundError`:

<img src='./images/img_170.png' alt='img_170' width='600'/>

## spyder-runtime Environment

If folder options are selected and Show Hidden Files is selected:

<img src='./images/img_171.png' alt='img_171' width='600'/>

The `.local` folder contains locally installed programs:

<img src='./images/img_172.png' alt='img_172' width='600'/>

The Spyder IDE is installed in the `spyder-6` subfolder:

<img src='./images/img_173.png' alt='img_173' width='600'/>

Notice it has its own `bin` folder:

<img src='./images/img_174.png' alt='img_174' width='600'/>

Which contains its own `conda` binary:

<img src='./images/img_175.png' alt='img_175' width='600'/>

And `python3` binary:

<img src='./images/img_176.png' alt='img_176' width='600'/>

It also has its own `lib` folder:

<img src='./images/img_177.png' alt='img_177' width='600'/>

Which has a `python3.11` folder:

<img src='./images/img_178.png' alt='img_178' width='600'/>

This contains the standard modules associated with the base Python environment. Notice there is a `site-packages` folder, this contains third-party libraries:

<img src='./images/img_179.png' alt='img_179' width='600'/>

The `conda` folder contains the conda package manager:

<img src='./images/img_180.png' alt='img_180' width='600'/>

The purpose of the `base` environment is use of the conda of the package manager. The conda package manager is used to create Python environments which are in the `envs` subfolder:

<img src='./images/img_181.png' alt='img_181' width='600'/>

The `spyder-runtime` environment is present:

<img src='./images/img_182.png' alt='img_182' width='600'/>

Notice `spyder-runtime` has its own `bin` subfolder:

<img src='./images/img_183.png' alt='img_183' width='600'/>

With its own `python3` binary:

<img src='./images/img_184.png' alt='img_184' width='600'/>

Notice `spyder-runtime` has its own `lib` subfolder:

<img src='./images/img_185.png' alt='img_185' width='600'/>

Which has a `python3.11` folder which contains the Python standard modules:

<img src='./images/img_186.png' alt='img_186' width='600'/>

And `site-packages` subfolder which contains third-party modules:

<img src='./images/img_187.png' alt='img_187' width='600'/>

The `numpy` library is found in the `numpy` folder:

<img src='./images/img_188.png' alt='img_188' width='600'/>

When imported the `__init__.py` is referenced:

<img src='./images/img_189.png' alt='img_189' width='600'/>

The `matplotlib` library is found in the `matplotlib` folder. When the library is imported the `__init__.py` is referenced:

<img src='./images/img_190.png' alt='img_190' width='600'/>

However normally the `pyplot` interface module is referenced:

<img src='./images/img_191.png' alt='img_191' width='600'/>

Note there is no `seaborn` subfolder as it is not preinstalled with Spyder.

The Spyder installer is `conda` based, the base environment is used to update `conda`, which is in turn is used to update the `spyder-runtime` environment when there is a Spyder update available. This `conda` is not intended to be used by the end user.

## Miniforge Installation

Miniforge is a minimal installer for `conda` which uses the community channel `conda-forge` by default. The Miniforge `base` environment is used only for the `conda` package manager and other packages are typically installed in separate Python environments. Note Anaconda/Miniconda are not recommended as they use a tainted repository `anaconda` by default which has commercial restrictions and older package versions which often result with incompatibilities with the current version of Spyder.

Miniforge is developed on GitHub and the latest release is on the [GitHub Miniforge Releases Page](https://github.com/conda-forge/miniforge/releases). Note Mambaforge is considered obsolete and therefore the installers listed at the top should be avoided. 

For Ubuntu the `Miniforge3-x.xx.x-x-Linux-x86_64.sh` or `Miniforge3-Linux-x86_64.sh` should be selected (these are the same installer):

<img src='./images/img_192.png' alt='img_192' width='600'/>

<img src='./images/img_193.png' alt='img_193' width='600'/>

<img src='./images/img_194.png' alt='img_194' width='600'/>

The Downloads folder can be opened in the Terminal:

<img src='./images/img_195.png' alt='img_195' width='600'/>

If:

```bash
bash M↹
```

is input:

<img src='./images/img_196.png' alt='img_196' width='600'/>

The file name will autocomplete:

```bash
bash Miniforge3-24.11.0-1-Linux-x86_64.sh
```

Press `↵` to execute the script:

<img src='./images/img_197.png' alt='img_197' width='600'/>

Press `↵` to begin scrolling through the license agreement:

<img src='./images/img_198.png' alt='img_198' width='600'/>

Press `q` to quit scrolling:

<img src='./images/img_199.png' alt='img_199' width='600'/>

To accept the license agreement input `yes` and press `↵`:

<img src='./images/img_200.png' alt='img_200' width='600'/>

To install in the default location press `↵`:

<img src='./images/img_201.png' alt='img_201' width='600'/>

A prompt to initialise `conda` will display. Note the default option if `↵` is input is `No`, which means `Miniforge` is installed but not initialised/

<img src='./images/img_202.png' alt='img_202' width='600'/>

Initialisation updates the `.bashrc` file which are the bash recall parameters used by the Linux Terminal:

<img src='./images/img_203.png' alt='img_203' width='600'/>

Note the Spyder installer has already updated this `.bashrc` file, so the binary `spyder` is recognised:

<img src='./images/img_204.png' alt='img_204' width='600'/>

To initialise `conda` with the Terminal, input `yes` and press `↵`:

<img src='./images/img_205.png' alt='img_205' width='600'/>

Miniforge is installed and initialised:

<img src='./images/img_206.png' alt='img_206' width='600'/>

The `.bashrc` file is updated. If it is refreshed:

<img src='./images/img_207.png' alt='img_207' width='600'/>

A `conda` initialisation block displays:

<img src='./images/img_208.png' alt='img_208' width='600'/>

When a new Terminal instance is opened, it will look at the recall parameters and add the prefix `(base)`, indicating the `base` Python environment (from Miniforge) is selected:

<img src='./images/img_209.png' alt='img_209' width='600'/>

## Initialising conda with the Linux Terminal Manually

If initialisation was not carried out, `(base)` will not display and the conda package manager cannot be used from the Terminal unless the directory containing the conda binary is manually input. This situation can be mimicked using:

```python            
conda init --reverse
```

<img src='./images/img_210.png' alt='img_210' width='600'/>

This means the following initialisation block is not present int he `.bashrc` file:

<img src='./images/img_211.png' alt='img_211' width='600'/>

<img src='./images/img_212.png' alt='img_212' width='600'/>

To initialise Miniforge manually, navigate to th `Home` folder and select the `Miniforge` subfolder:

<img src='./images/img_213.png' alt='img_213' width='600'/>

Then select the `bin` subfolder:

<img src='./images/img_214.png' alt='img_214' width='600'/>

Right click the folder and select, Open in Terminal:

<img src='./images/img_215.png' alt='img_215' width='600'/>

Input:

```bash
./conda init --all
```

The `./` means look in the same directory as the current working directory for the `conda` binary.

<img src='./images/img_216.png' alt='img_216' width='600'/>

Miniforge is installed and initialised. When a new Terminal instance is opened, it will look at the recall parameters and add the prefix `(base)`, indicating the `base` Python environment (from Miniforge) is selected.

<img src='./images/img_217.png' alt='img_217' width='600'/>

## Creating a Custom spyder-env Environment (conda)

The purpose of the `base` environment is to use the conda package manager. It is not recommended to install other packages in `base`:

<img src='./images/img_218.png' alt='img_218' width='600'/>

before using the `conda` package manager, it should be updated to the latest version using:

```bash
conda update conda
```

<img src='./images/img_219.png' alt='img_219' width='600'/>

The default channel is `conda-forge` which is the community channel:

<img src='./images/img_220.png' alt='img_220' width='600'/>

`conda` and `conda` dependencies will be updated. Input `y` in order to proceed:

<img src='./images/img_221.png' alt='img_221' width='600'/>

`conda` is now up to date:

<img src='./images/img_222.png' alt='img_222' width='600'/>

A new environment can be created using:

```bash
conda create -n spyder-env spyder-kernels python seaborn scikit-learn pyarrow sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt ffmpeg ruff
```

This has `spyder-kernels` which is required for Syder to use the environment. `seaborn` which has `numpy`, `pandas` and `matplotlib` as dependencies. `scikit-learn` for machine learning. `pyarrow`, `openpyxl`, `xlrd`, `xlsxwriter`, `lxml`, `sqlalchemy`, `tabulate` for various file pandas formats. `pyqt` for matplotlib's interactive backend and `ffmpeg` for saving matplotlib animations.

`-n` means name and `spyder-env` is the name of the Python environment. Specifying an environment using `-n` means changes to that environment will be made opposed to `base` which is the currently activate environment.

<img src='./images/img_223.png' alt='img_223' width='600'/>

These packages will all be installed from the `conda-forge` channel. In the `spyder-env` folder which is found in the `envs` subfolder of `base`:

<img src='./images/img_224.png' alt='img_224' width='600'/>

Details about packages to be downloaded will be shown:

<img src='./images/img_225.png' alt='img_225' width='600'/>

Input `y` in order to proceed:

<img src='./images/img_226.png' alt='img_226' width='600'/>

The packages are installed in the environment but it is not activated:

<img src='./images/img_227.png' alt='img_227' width='600'/>

To activate it use:

```bash
conda activate spyder-env
```

<img src='./images/img_228.png' alt='img_228' width='600'/>

Notice the prefix is now `(spyder-env)` meaning this environment is activated. An `ipython` shell can be launched. Imports of the standard modules and third-party libraries can be carried out, if the `__file__` attribute of these is checked, notice they are all found in the directory of `spyder-env`:

<img src='./images/img_229.png' alt='img_229' width='600'/>

<img src='./images/img_230.png' alt='img_230' width='600'/>

<img src='./images/img_231.png' alt='img_231' width='600'/>

<img src='./images/img_232.png' alt='img_232' width='600'/>

## Selecting the Custom spyder-env Environment (conda)

In Spyder, the default environment `spyder-runtime` is selected:

<img src='./images/img_233.png' alt='img_233' width='600'/>

Go to Tools → Preferences:

<img src='./images/img_234.png' alt='img_234' width='600'/>

Select IPython Interpretter:

<img src='./images/img_235.png' alt='img_235' width='600'/>

Select Use the Following Interpretter and select `spyder-env` (conda) from the dropdown list:

<img src='./images/img_236.png' alt='img_236' width='600'/>

Select Apply:

<img src='./images/img_237.png' alt='img_237' width='600'/>

Close Spyder and relaunch using the start menu shortcut or inputting:

```bash
spyder
```

in the Terminal. 

<img src='./images/img_238.png' alt='img_238' width='600'/>

`spyder-env` should be shown at the bottom and now seaborn can be imported:

```python
import seaborn as sns
```

<img src='./images/img_239.png' alt='img_239' width='600'/>

## Changing Default Plot Backend

The default plot backend can be changed, by selecting Tools → Preferences:

<img src='./images/img_240.png' alt='img_240' width='600'/>

Then IPython Console → Graphics and changing the backend to Qt:

<img src='./images/img_241.png' alt='img_241' width='600'/>

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

<img src='./images/img_242.png' alt='img_242' width='600'/>

In the GNOME desktop environment, when a Window title bar is right clicked, it can be set to always on top:

<img src='./images/img_243.png' alt='img_243' width='600'/>

This allows modification and visualisation of the plot using the console.

## Updating

There is a new release of Spyder, approximately every month. When available a prompt for the upgrade should display and Spyder should update using packages from `conda-forge` using its internal `conda` package manager:

If an external conda environment was created, it will need to be updated, with a compatible version of `spyder-kernels`. Open up the Windows Terminal an updte the `conda` package manager in base:

```powershell
conda update conda
```

Then activate `spyder-env` and searh for updates to all packages:

```powershell
conda activate spyder-env
conda update --all
```

[Return to Python Tutorials](../readme.md)