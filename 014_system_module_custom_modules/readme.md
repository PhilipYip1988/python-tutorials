# The sys Module and Working with Custom Modules

Pythons ```builtins``` is supplied by Python standard modules. A module contains compartmentalised, classes, functions and variables. The following modules have already been examined:

* builtins
* string
* fractions
* decimal
* collections
* itertools
* functools
* math
* cmath
* datetime
* zoneinfo
* time
* random
* statistics

This guide will look at importing modules in more detail and creating simple custom modules.

## The sys Module

The system module ```sys``` gives details about objects used or maintained by the Python interpreter. It can be imported using:

```
import sys
```

![img_001](./images/img_001.png)

Its docstring can be accessed by inputting:

```
? sys
```

![img_002](./images/img_002.png)

It has the following static objects, note that these are immutable data types:

* ```builtin_module_names``` is a tuple of module names built into Python.
* ```sys.stdlib_module_names``` is a frozenset of module names built into Python.
* ```version``` is the Python version as a string.
* ```copyright``` is a copyright string.

It has the following dynamic objects, note these are mutable data types and can be updated:

* ```path``` is a list of the module search path.
* ```modules``` is a dictionary of loaded modules.
* ```argv``` is a list of command line arguments. The value at index 0 correponds to the script path file.

The follwoing strings can be viewed which mainly give details about the Python version:

```
sys.winver
sys.version_info
sys.version
sys.copyright
```

![img_054](./images/img_054.png)

The following can be assigned to object names

```
# path
path = sys.path

# builtin modules
builtin_module_names = sys.builtin_module_names

# standard modules including builtin modules
standard_module_names = tuple(sys.stdlib_module_names)

# standard modules excluding builtin modules
standard_modules_lib = tuple(set(sys.stdlib_module_names) - set(sys.builtin_module_names))

# loaded modules
loaded_modules = sys.modules
```

![img_004](./images/img_004.png)

This can be viewed in the Variable Explorer in Spyder:

![img_005](./images/img_005.png)

Notice that there are 67 builtin modules (written in C) and 305 standard modules. 240 of these standard modules and physical files are in the ```Lib``` folder. The number of modules loaded is 1731, Spyder is an IDE written using Python and a multitude fo third-party modules.

### sys.path

The ```sys.path``` is a ```list``` of ```str```. The ```list``` is mutable meaning other file paths can be appended:

![img_006](./images/img_006.png)

#### builtin modules

Index 0 shows the location of the Python ```builtins``` module and other builtin modules. These are written in C. Although a python311.zip file is mentioned, essentially these are contained within the python.exe:

![img_007](./images/img_007.png)

#### standard modules

Index 1 shows the location of the remaining Python standard modules which are essentially available in the ```Lib``` folder:

![img_008](./images/img_008.png)

Smaller standard modules such as ```datetime.py``` are shown directly here:

![img_009](./images/img_009.png)

```
import datetime
```

refers to this physical file.

Larger standard modules have are in a subfolder that has the same name as the module for example ```email```:

![img_010](./images/img_010.png)

Within such a subfolder is an ```__init__.py``` file. This is the file that is imported when the name of a folder is imported:

![img_011](./images/img_011.png)

```
import email
```

refers to this physical file.

#### third-party packages

Index 5 is the site-packages subfolder. This folder contains all the third-party packages downloaded using a package manager:

![img_006](./images/img_006.png)

![img_012](./images/img_012.png)

The most commonly used third-party package with Python is ```numpy```. A package is also known as a library. There are two folders in site-packages, the one ending in dist-info details about the version number and the numpy folder. The numpy folder contains multiple Python script files, which are also known as modules:

![img_013](./images/img_013.png)

Within the numpy folder is an ```__init__.py``` file. This is the file that is imported when the name of a folder in this case, the name of the library is imported:

![img_014](./images/img_014.png)

```
import numpy
```

refers to this physical file.

Because this package is so commonly used it is normally imported with a 2 letter alias:

```
import numpy as np
```

In the ```numpy``` folder are other script files such as ```version.py```. This is a module of the numpy package. Inputting ```import numpy.``` and pressing tab ```↹``` shows only the modules that can be imported (other identifiers are not shown):

![img_015](./images/img_015.png)

This module can be imported using:

```
import numpy.version as version
```

This module (script file) is very basic:

![img_016](./images/img_016.png)

It has a variable version.

For clarity, importing the package ```numpy```:

```
import numpy
numpy
```

![img_017](./images/img_017.png)

Importing the module ```version``` from the package ```numpy``` as an alias ```version```:

```
import numpy.version as version
version
```

![img_018](./images/img_018.png)

And accessing the variable ```version``` from the module ```version``` from the package ```numpy```:

```
version.version
```

![img_019](./images/img_019.png)

Often a simple object like this is imported directly using:

```
from numpy.version import version
```

![img_020](./images/img_020.png)

The numpy package has larger modules that have their own subfolders such as ```linalg```:

![img_021](./images/img_021.png)

Within this ```linalg``` subfolder is another ```__init__.py```:

![img_022](./images/img_022.png)

Using:

```
import numpy.linalg as linalg
```

references this file.

Returning to ```site-packages``` a commonly used module is ```pyplot.py``` that belongs in the ```matplotlib``` package:

![img_023](./images/img_023.png)

![img_024](./images/img_024.png)

Inputting:

```
import matplotlib.pyplot as plt
```

references this file.

The entire package is not commonly imported but can be with its own ```__init__.py``` file:

![img_025](./images/img_025.png)

```
import matplotlib
```

references this file.

## A custom module

### Imported from Notebook

A custom module also known as a script (.py) file can be created in the same folder as the interactive Python Notebook (.ipynb) file:

![img_026](./images/img_026.png)

Its file name should follow Python object names, that is be all lower case without special characters except for the underscore in this case the file is called ```script``` or ```script.py``` including the file extension:

![img_027](./images/img_027.png)

A simple variable and function will be added to the script file:

```
text = 'hello world!'
print_text = lambda : print(text.upper()) 
```

![img_028](./images/img_028.png)

Because it is in the same folder as the interactive Python notebook, it can be imported using:

```
import script
```

![img_029](./images/img_029.png)

A list of identifiers can be accessed by inputting ```script.``` followed by a tab ```↹```:

![img_030](./images/img_030.png)

The str variable can then be accessed using:

```
script.text
```

The function can be called using:

```
script.print_text()
```

![img_031](./images/img_031.png)

The objects can also be imported directly into the interactive Python notebooks main namespace:

```
from script import text, print_text
text
print_text()
```

![img_032](./images/img_032.png)

If the directory of the script file is examined:

```
dir(script)
```

![img_033](./images/img_033.png)

Notice the 2 objects created display but the file also has a number of data model identifiers.

```__builtins__``` merely means the file has access to everything from the ```builtins``` module, every Python script file and interactive notebook can access ```builtins```.

The other identifiers can be examined:

```
script.__doc__
script.__name__
script.__loader__
script.__file__
script.__spec__
script.__package__
```

![img_034](./images/img_034.png)

The docstring retrieved by ```__doc__``` is empty as none was provided. A multiline string can be added to the top of the script. The ```__name__``` is the name of the script file when it is imported. The ```__loader__``` gives details about how the file is loaded.The ```__file__``` is the physical file. The ```__spec__``` combines all the information above. The ```__package__``` can be used to define the package.

All of these identifiers can be accessed directly in the script file and the contents of the ```script.py``` file can be updated to:

```
"""This is a custom script file which contains the str text = 'hello world!' and has a function print_text that prints it."""

print(__doc__)
print(__name__)
print(__loader__)
print(__file__)
print(__spec__)
print(__package__)

text = 'hello world!'
print_text = lambda : print(text.upper()) 
```

![img_035](./images/img_035.png)

Now when imported in the interactive Python notebook file, all the print statements will be executed as the script file is run during an import:

![img_036](./images/img_036.png)

Notice the docstring now displays. Notice also the name of the script file is ```script```.

### Executed Directly

If a new terminal is launched:

![img_037](./images/img_037.png)

The Python script file can be launched by activating the jupyterlab Python environment and running the Python script:

```
mamba activate jupyterlab
python script.py
```

![img_038](./images/img_038.png)

Notice that the name is now ```__main__``` instead of ```script```:

![img_039](./images/img_039.png)

When a script file is ran directly ```__name__``` is equal to ```'__main__'``` and when it is imported ```__name__``` is the string of the script file name (excluding the file extension). This is often used as a condition to change the behaviour of a script file when it is ran directly versus when it is imported. Usually more code is ran when the script file is ran directly for diagnostic purposes. In this example the print statement will change::

```
"""This is a custom script file which contains the str text = 'hello world!' and has a function print_text that prints it."""

if __name__ == '__main__':
    print(f'Executed Directly as {__name__}')
else:
    print(f'Imported as {__name__}')

text = 'hello world!'
print_text = lambda : print(text.upper()) 
```

When ran directly:

![img_040](./images/img_040.png)

When imported:

![img_041](./images/img_041.png)

### sys.argv

```sys.argv``` is a list of command line arguments, the value at index 0 correponds to the script path file. This can be seen clearly by creating the following script file:

```
"""This file will examine the command line arguments"""

import sys
if __name__ == '__main__':
    argv = sys.argv
    print(f'type: {type(argv)}')
    print(f'length: {len(argv)}')
    print()
    for idx, arg in enumerate(argv):
        print(f'idx {idx}: arg {arg}: type {type(arg)}')

        
```

When the script file is ran using:

```
python script.py
```

![img_042](./images/img_042.png)

Notice the only command line argument in this ```argv``` list is the str corresponding to the name of the script file itself. This is always at index ```0```. This command line argument was supplied after the command python in the terminal. A space is used to seperate out command line arguments.

Other command line arguments can be added, these will all be of the type str:

```
python script.py 1 2 3 4
```

![img_043](./images/img_043.png)

This can be used to print a customised greeting in response to a command line argument. For example:

```
"""This file will print a greeting using the 2nd command line arguments"""

import sys
if __name__ == '__main__':
    argv = sys.argv
    if len(argv) > 1:
        username = argv[1]
        print(f'Hello {username}')
    else:
        print(f"Hi, I don't know your name")

        
```

Running this script without and with the additional command line argument shows:

```
python script.py
python script.py Philip
```

![img_044](./images/img_044.png)

### Appending to sys.path

The module can be moved to a custom folder:

![img_045](./images/img_045.png)

If the module is moved into a different folder, it won't be found when attempting to import giving a ```ModuleNotFoundError```:

```
import script
```

![img_046](./images/img_046.png)

If this path is appended to ```sys.path``` it will be found:

```
sys.path.append(r'C:\Users\Philip\Documents\custom_modules')
import script
```

![img_047](./images/img_047.png)

![img_048](./images/img_048.png)

### Custom Package

If the script file is moved to a subfolder called ```custom_package``` and renamed ```__init__.py```. 

![img_049](./images/img_049.png)

It can be imported using:

```
import custom_package
```

![img_050](./images/img_050.png)

Another script file can be created called ```script```:

```
"""This is a custom script file which prints its identifiers"""

print(__doc__)
print(__name__)
print(__loader__)
print(__file__)
print(__spec__)
print(__package__)
```

![img_051](./images/img_051.png)

If ```import custom_package.``` is input followed by a tab ```↹``` then ```script``` displays as a module:

![img_052](./images/img_052.png)

It can be imported using:

```
import custom_package.module
```

![img_053](./images/img_053.png)

Notice that the identifier ```__package__``` now has the value ```'custom_package'```.

[Home Python Tutorials](https://github.com/PhilipYip1988/python-tutorials/blob/main/readme.md)



















