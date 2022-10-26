# Working with Custom Modules

## Script File

A python script file called ```script0.py``` will be created in the same folder otherwise known as directory as the interactive notebook file. For simplicity this script file will contain two lines of code to create a variable and a function:

```
greeting = "Hello"
row_number_to_str = lambda number: "r" + str(number)
print(greeting)
```

![img_000](./images/img_000.png)

### import

The ```import``` command can be used to import the script. The import command is followed by the name of the script which acts as an input argument in this context:

```
import script0
```

Note when the import command is used, there is no ```.py``` file extension provided for the input script.

![img_001](./images/img_001.png)

Notice that when the ```script0``` is imported, the code within ```script0``` is executed. The variable ```greeting``` and the function ```row_number_to_str``` are defined within the namespace of the module and the print statement is executed which is why ```hello``` is shown in the cell output.

The file extension is dropped because the dot ```.``` is used in Python to indicate that an object is contained within another object. Think of the syntax ```container.item``` as taking an ```item``` out of a ```container```. If ```script0.``` is typed followed by tab ```↹```:

![img_002](./images/img_002.png)

then a list of all the objects contained within ```script0``` display. The variable and function contained in ```script0``` can be used by inputting:

```
script0.greeting
script0.row_number_to_str(100)
```

![img_003](./images/img_003.png)

### import as alias

If a script file is widely used, throughout an interactive notebook, it can be useful to import the script file as an alias. Typically the alias is a shorter name than the name of the script file. For example the alias ```s0``` can be used:

```
import script0 as s0
```

![img_004](./images/img_004.png)

If ```s0.``` is typed followed by tab ```↹```, a list of all the objects contained within ```s0``` display. The variable and function can be used by inputting:

```
script0.greeting
script0.row_number_to_str(100)
```

![img_005](./images/img_005.png)

### from Script File import object

Alternatively an individual object can be directly imported from the script. Inputting:

```
from script0 import
```

followed by a tab ```↹``` reveals a list of all the objects that can be imported from ```script0```:

![img_006](./images/img_006.png)

For example the object ```greeting``` can be imported using:

```
from script0 import greeting
```

This object is now directly in the namespace of the interactive notebook and can therefore be referenced directly:

```
greeting
```

![img_007](./images/img_007.png)

Multiple objects can be imported at once using a comma ```,``` as a delimiter:

```
from script0 import greeting, row_number_to_str
```

These can be referenced or called directly:

```
greeting
row_number_to_str(100)
```

![img_008](./images/img_008.png)

It is possible to import all objects using a ```*```, although this practice is generally frowned upon as it makes it harder to diagnose where an object name came from when reading through the notebook.

```
from script0 import *
```

## Library (Directory)

A collection of script files can be placed together in a folder (also known as a directory). A directory called ```directory``` will be created in the same parent folder as the interactive notebook:

![img_009](./images/img_009.png)

Within this directory an **init**ialisation script file will be created with the file name ```__init__.py```. i.e. ```init``` is enclosed in a set of double underscores:

![img_010](./images/img_010.png)

Once again the code in this script file will be relatively simple:

```
farewell = "Goodbye" 
col_number_to_str = lambda number: "c" + str(number)
```

When the folder is imported, this initialisation script file ```__init__.py``` will be imported:

```
import directory
```

![img_011](./images/img_011.png)

The contents can viewed by inputting the director name followed by a dot ```.``` and tab ```↹```:

![img_012](./images/img_012.png)

Objects are referenced in an identical manner to an individual script file outside a directory:

```
directory.farewell
directory.col_number_to_str(200)
```

![img_013](./images/img_013.png)

## Module (Script File)

Additional Python script files can be placed in the directory. Each individual script file in the directory is known as a Python ```module``` and the directory containing all the script files is known as a ```library```. A module can be accessed from the folder using the syntax ```library.module```.

![img_014](./images/img_014.png)

In this case, an example ```module``` is called ```mod.py``` and has the basic contents:

```
saying = "Hi"
cr_number_to_str = lambda number: "cr" + str(number)
```

If ```import directory.``` is input, followed by a tab ```↹```, the list of objects that can be referenced from the directory called ```directory``` will display:

![img_015](./images/img_015.png)

The module can be imported as:

```
import directory.mod as m1
```

Now if ```m1.``` is input, followed by a tab ```↹```, the list of objects that can be referenced from the module called ```mod``` with alias ```m1``` will display:

![img_016](./images/img_016.png)

These objects can be used with:

```
m1.saying
m1.cr_number_to_str(300)
```

![img_017](./images/img_017.png)


## Module (Directory)

It is also possible in some cases, to create a module as a subdirectory (subfolder). In this example, a subdirectory (subfolder) called ```mod2``` is created:

![img_018](./images/img_018.png)

Within this subdirectory (subfolder) another initialisation ```__init__.py``` script file is created and has the basic contents:

```
word = "Python"
x_number_to_str = lambda number: "x" + str(number)
```

This initialisation script file will once again be referenced when this subdirectory (subfolder) is imported:

![img_019](./images/img_019.png)

The subdirectory (subfolder) is also a module and can be imported using the same syntax as before:

```
import directory.mod2 as m2
```

Now if ```m2.``` is input, followed by a tab ```↹```, the list of objects that can be referenced from the module called ```mod``` with alias ```m2``` will display:


![img_020](./images/img_020.png)

![img_021](./images/img_021.png)

These objects can be used with:

```
m2.word
m1.x_number_to_str(500)
```

![img_022](./images/img_022.png)

## Datamodel Attributes

Returning to the original ```script0.py```:

```
greeting = "Hello"
row_number_to_str = lambda number: "r" + str(number)
```

The inbuilt function ```dir``` which is an abbreviation for directory can be used to view the directory of the module:

![img_023](./images/img_023.png)

In this list, the variable ```greeting``` and the function ```row_number_to_str``` display. In addition to the above a number of datamodel attributes display.

The ```__name__``` datamodel attribute will return the name of the module in the form of a string.

```
import script0
script0.__name__
```

In this example the string ```"script0"```:

![img_024](./images/img_024.png)

which is the name of the module. The name does not change if the module is imported using an alias:

```
import script0 as s0
s0.__name__
```

![img_025](./images/img_025.png)

The datamodel attribute ```__name__``` can also be accessed as a variable within the Python script file.

```
greeting = "Hello"
row_number_to_str = lambda number: "r" + str(number)

print(__name__)
```

![img_030](./images/img_030.png)

Notice that when the module is imported, the code in the module is executed so the print statement displays the ```__name___``` of the script file. In this example the ```__name__``` is the name of the script file ```"script0"```.

When a Python script file is ran directly in Python, for example using the terminal the ```__name__``` of the main script file is instead assigned to ```"__main__"```:

![img_031](./images/img_031.png)

This can be used to check if the script file is the main script file being executed using if, else code blocks:

```
if __name__ == "__main__":
    print("I am the main module")
else:
    print("I am not the main module")
```    

The if code block is carried out when the script file is the main module:

![img_032](./images/img_032.png)

The else code block is carried out when the script file is not the main module:

![img_033](./images/img_033.png)

The ```__file__``` datamodel attribute gives the physical location of the file:

```
import script0
script0.__file__
```

![img_026](./images/img_026.png)

The ```__doc__``` datamodel attribute gives the docstring of the module:

```
import script0
script0.__doc__
```

![img_027](./images/img_027.png)

In this example, the module has no docstring, so the output of the cell is None. A docstring can be added by providing a multiple line string at the top of the module.

```
"""
This module contains a variable and a function.
"""

greeting = "Hello"
row_number_to_str = lambda number: "r" + str(number)
```

Notice the docstring now displays with the datamodel attribute ```__doc__``` or by using ```?```

```
import script0
script0.__doc__
? script0
```

![img_028](./images/img_028.png)

The datamodel attribute ```__doc__``` can also be accessed as a variable within the script file:

```
"""
This module contains a variable and a function.
"""

greeting = "Hello"
row_number_to_str = lambda number: "r" + str(number)

print(__doc__)
```

![img_034](./images/img_034.png)


The datamodel attribute ```__package__``` displays the name of the package for a package with multiple modules. This can be examined by looking at the module ```mod``` from the package ```directory```:

```
import directory.mod as mod
mod.__package__
```

![img_029](./images/img_029.png)

The ```__init__.py``` within the folder directory can be modified to include a docstring and the datamodel attributes can be accessed as variables within the script file and printed using formatted strings:

```
"""
This module contains a variable and a function.
"""

farewell = "Goodbye" 
col_number_to_str = lambda number: "c" + str(number)

print(f"name: {__name__}")
print(f"file: {__file__}")
print(f"package: {__package__}")
print(f"doc: {__doc__}")
print(f"loader: {__loader__}")
print(f"spec: {__spec__}")
```

The ```__loader__``` datamodel attribute gives details about how the module was loaded, such as where it stored in module and the spec gives details about a module that is imported:

![img_035](./images/img_035.png)

This is ```None``` when the module is ```"__main__"```

![img_036](./images/img_036.png)

Python has a number of standard modules. The ```builtins``` module provides direct access to all the built-in identifiers of Python. It can be imported using:

```
import builtins
```

Inputting ```builtins.``` followed by a ```↹``` can be used to view the list of builtin-in identifiers:

![img_037](./images/img_037.png)

These objects can be accessed explicitly from the builtins module however are usually accessed directly:

```
? builtins.str
```

```
? str
```

![img_038](./images/img_038.png)

When a script file is ran, behind the scenes, the following command is executed, making all the inbuilt items available:

```
from builtins import *
```

![img_039](./images/img_039.png)

The datamodel attribute ```__builtins__``` is a dictionary. This can be printed using:

```
print(__builtins__)
```

![img_040](./images/img_040.png)

The builtin ```print``` function isn't optimised for printing the output of a dictionary. The standard module ```pprint``` an abbreviation for pretty print has a function ```pprint``` and this can be used in place of print:

```
from pprint import pprint
pprint(__builtins__)
```

![img_041](./images/img_041.png)

An in-built identifier can be accessed by indexing into the dictionary using the name of the identifier as a key. For example the str class can be accessed using:

```
__builtins__["str"]
```

print and help can be used to print the docstring of this class as the module is executed or imported:

```
print(help(__builtins__["str"]))
```

![img_042](./images/img_042.png)

All identifier included in a module can be accessed using the attribute ```__dict__``` which outputs a dictionary. The first entry in the dictionary is a nested dictionary with the key ```__builtins__```:

```
import directory
from pprint import pprint
pprint(directory.__dict__)
```

![img_043](./images/img_043.png)

The other keys in the dictionary can be used to access the other datamodel attributes in addition to the user defined variables and functions:

![img_044](./images/img_044.png)

# Python Standard Modules

The mostly used identifiers in Python are in the builtins module which has been essentially already been explored in great detail. Outwith these most commonly used objects, Python is grouped by application area into a number standard modules. Some of the most important modules are mentioned below alongside the location of their physical script file (where applicable). These script files can be opened in JupyterLab and inspected and serve as example files of high quality modules. Most of the modules will only be mentioned in brief and be covered in more detail in other guides. The ```os``` and ```sys``` module will however be mentioned here in a bit more detail as they can be used to access additional locations to run Python modules from.

## builtins

The attributes ```__name__``` and ```__doc__``` can be used with the builtins module. The attribute ```__file__``` is not available as there is no physical script file, because builtin objects are written in C++:

![img_047](./images/img_047.png)

## pprint

The module ```pprint``` was used earlier. It can be imported and the attributes ```__name__``` and ```__file__``` can be used to access the name and file of the module.

![img_045](./images/img_045.png)

This script file can be opened and examined. The docstring can also be output using the attribute ```__doc__```:

![img_046](./images/img_046.png)

## math

```math``` is a module that contains mathematical functions. Once again the attribute ```__file__``` is not available as the module is written in C++.

![img_050](./images/img_050.png)

## collections

The module ```collections``` is used to supplement Python's inbuilt collections. It can be imported and the attributes ```__name__```, ```__doc__``` and ```__file__``` can be used to access the name and file of the module. The attribute ```__all__``` is also defined in the file as a list containing all the objects defined in the module:

![img_049](./images/img_049.png)

## random

The module ```random``` is used for generation of random numbers.

![img_063](./images/img_063.png)

## statistics

The module ```statistics``` is used for statistical functions.

![img_064](./images/img_064.png)

## datetime

The module ```datetime``` is used to specify a date and time as well as a time difference:

![img_048](./images/img_048.png)

## calendar

The module ```calendar``` has some additional calendar operations:

![img_066](./images/img_066.png)

## time

The module ```time``` is used more in line with runtime. This module is written in C++ and has no file available. 

![img_065](./images/img_065.png)

## os

The module ```os``` is used for interactions with the operating system. For example folder manipulation. 

![img_051](./images/img_051.png)

The attribute ```environ``` is a dictionary of the Operating System Environmental Variables. The user profile can be accessed using the key ```"UserProfile"```. The ```os``` attribute ```path``` contains a collection of functions which can be used to manipulate a path, and ```join``` can be used to join a subfolder to a path:

```
user_profile = os.environ["UserProfile"]
downloads = os.path.join(user_profile, "Downloads")
```

![img_055](./images/img_055.png)

## glob

The module ```glob``` is usually used to glob a set of file patterns within a root directory.

![img_061](./images/img_061.png)

For example if the file pattern is ```"*.py"``` any Python Script will be selected and in this case ```*``` represents any other combination of valid characters used within a file name:

```
import os
import glob
user_profile = os.environ["UserProfile"]
documents = os.path.join(user_profile, "Documents")
glob.glob("*.py", root_dir=documents)
```

![img_062](./images/img_062.png)

## sys

The module ```sys``` system is used for interactions with the interpretter. It is once again written in C++ and has no ```__file__``` attribute:

![img_052](./images/img_052.png)

The attribute ```path``` is a list which includes all the locations Python will look for a module. At the top of the ```path``` is ```"C:\Users\Phili\Documents"``` which is the current working directory.

![img_053](./images/img_053.png)

To search for modules in other locations the list method append can be used to append another location to this list. This is typically done in conjunction with the os module:

![img_054](./images/img_054.png)

The attribute ```argv``` is a list of all the command line arguments used when running a Python script from the terminal. For example if the following is added to the script file:

```
import sys
from pprint import pprint
pprint(sys.argv)
```

And the script file is ran using the command:

```
python script0.py
```

Then the only command line argument used with the command ```python``` was ```"script0.py"``` which is available as a string.

Note the output is the same when the file is specified using a string.

```
python "script0.py"
```

![img_056](./images/img_056.png)

If an additional string is added after the script file, there will now be two command line arguments:

```
python "script0.py" "hello"
```

![img_057](./images/img_057.png)

If the string of the second command line argument is also a Python script file, it won't be executed. Only the first file will be executed.

```
python "script0.py" "script1.py"
```

![img_058](./images/img_058.png)

The list ```sys.argv``` can be indexed into to get one of the command line arguments. For example ```sys.argv[1]``` will be the string ```"hello"```:

![img_059](./images/img_059.png)

If the module is expected to be called with a specific number of input arguments a check can be placed to check if the list of input arguments is the correct length:

```
import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("not enough command line arguments provided")
```

![img_060](./images/img_060.png)

## csv

The module ```csv``` is used to manipulate data which is stored in a comma seperated values (csv) file:

![img_068](./images/img_068.png)

## json

The module ```json``` is used to manipulate data which uses Javascript object notation (json):

![img_067](./images/img_067.png)


Return to:
[Home](../../../)
