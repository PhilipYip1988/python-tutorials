# Python Tutorials

This set of tutorials goes through basic to intermediate concepts of the Python Programming Language using the markdown and notebook aspects of the JupyterLab IDE, supplemented with the Variable Explorer of the Spyder IDE. The tutorials themselves are written in markdown, and therefore can be downloaded as a zip file, extracted and opened in JupyterLab if GitHub doesn't render images or equations correctly. Pleae star the tutorials on GitHub and share with friends if you have found them useful.

## Installation

The Python ecosystem is very large and has multiple package managers for third-party libraries and numerous IDEs available for writing Python code. This installation tutorial is very detailed as it explains how to use Python from the Terminal, the IDLE IDE, the Spyder IDE, the JupyterLab IDE and the Visual Code IDE and how to use the Mamba package manager to create Python Environments, examining what is going on behind the scenes in the file explorer.

[Mambaforge Installation](https://github.com/PhilipYip1988/python-tutorials/blob/main/001_install/readme.md)

## Markdown

The JupyterLab IDE has the ability to write formatted notes in a Markdown file. This tutorial will cover the basics of Markdown syntax. All of these tutorials are written using this basic Markdown syntax. It is also possible to use this knowledge in an Interactive Python Notebook File which has Markdown cells.  

[Markdown Tutorial](https://github.com/PhilipYip1988/python-tutorials/blob/main/002_markdown/readme.md)

## Terminal

When running Python code from the Terminal, two programming languages are used. In Linux and Mac there is the inbuilt programming language bash and in Windows there is PowerShell which closely resembles bash. The bash programming language is optimised for basic file operations within the operating system and is commonly used in conjunction with Python. bash however uses a different programming syntax to Python and this tutorial will cover basic file operating systems using bash. Familarity with bash before delving into Python will prevent later confusion when using the terminal with Python commands.

[Terminal Commands](https://github.com/PhilipYip1988/python-tutorials/blob/main/003_terminal/readme.md)

## Fundamental Data Types

There are 3 fundamental text data types, the unicode string, the bytes string and the bytearray. The Unicode string is the most widely used text data type in Python, however it is useful to know about the other two data types and establish a concept behind encoding:

[Text Data Types: str, bytes, bytearray](https://github.com/PhilipYip1988/python-tutorials/tree/main/004_text_datatypes/readme.md)

There are 6 fundamental numeric datatypes used in Python. The ```int``` class (whole number), ```bool``` class (```True``` or ```False```), the ```float``` class (number with a decimal point), the ```complex``` class (number with imaginary component $j=\sqrt{-1}$), the ```float``` class (number displayed with a decimal point but encoded in binary), ```Decimal``` class (higher accuracy number with decimal point encoded in decimal) and the ```Fraction``` class:

[Numeric Data Types: int, bool, float, complex, Decimal, Fraction](https://github.com/PhilipYip1988/python-tutorials/blob/main/005_numeric_datatypes/readme.md)

## Collections

Python has four collections the immutable tuple, which can be conceptualised as an archive of references. The mutable list, which can be conceptualised as being active current working directory of references. The set which can be conceptualised as a collection of unique references. And the dictionary which can be conceptualised as a mapping of immutable keys to values:

[Collections; tuple, list, set, dict](https://github.com/PhilipYip1988/python-tutorials/blob/main/006_collections/readme.md)

## Programming Constructs

Indentation and spacing is very important in Python and code is often grouped into a code block. Code blocks are used to direct code in response to a condition, to repeat an operation multiple times, to error handle and to create custom functions:

[Programming Constructs using Code Blocks](https://github.com/PhilipYip1988/python-tutorials/blob/main/007_programming_constructs_with_code_blocks/readme.md)

The builtins module contains the ```str```, ```list```, ```tuple```, ```set``` and ```dict``` collections. The collections module includes a number of additional collections which supplement these such as the ```NamedTuple``` which is a ```tuple``` subclass that has field names, ```deque``` (double ended queue) that is list like, ```defaultdict``` which is a ```dict``` subclass with default behaviour when new keys that don't exist are indexed, and ```Counter``` which is a ```dict``` subclass used for counting. A number of these collections almost became inbuilt identifiers themselves and therefore this is one of the closest modules to Python ```builtins```. Learning this module at this stage will build an understanding for subclassing:

[Collections Module](https://github.com/PhilipYip1988/python-tutorials/blob/main/008_collections_module/readme.md) 

The concept of an iterators was covered briefly when looking at programming constructs using code blocks. The ```builtins``` module contains commonly used iterators such as the ```zip```, ```filter``` and ```map``` iterator classes. Python also has an iterator module ```itertools``` that contains ```zip_longest```, ```filterfalse```, and ```starmap``` iterator classes which complement their similar counterpart in ```builtins```. The itertools module also has a ```cycle```, ```repeat``` and ```count``` iterator classes which are endless iterators. The ```cycle``` iterator can be used to continuously index around a collection, returning to the top after reaching the bottom. Like the collections module, the itertools module is one of the closest modules to Python builtins. Effective use of these two modules simplifies common programming tasks and generally makes the code more Pythonic and easier to read:

[Iterator Tools Module](https://github.com/PhilipYip1988/python-tutorials/blob/main/009_itertools_module/readme.md) 

## Math and Statistics

The ```math``` module is used to carry out common mathematical operations on scaler numeric data. Learning how to use this module and reinforcing the underlying mathematics is a perquisite when it comes to any data science tasks. There is an associated complex math module ```cmath``` which is designed to handle complex numbers:

[Math and Complex Math Modules](https://github.com/PhilipYip1988/python-tutorials/blob/main/010_math_module/readme.md) 

The ```random``` module is a pseudo random number generator which can be used to select a choice or choices from a list which are operations done with replacement. Alternatively it may be used to select a sample from a list which is done without replacement or to mutate the existing list by shuffling it. There are also a number of statistical distributions that a number can be generated from including the commonly used uniform, normal and exponential distributions:

[Random Module](https://github.com/PhilipYip1988/python-tutorials/blob/main/011_random_module/readme.md)

The ```datetime``` module is a module for working with dates and times. The associated ```zoneinfo``` module is for dealing with timezones. The ```time``` module is a module written in C and exists mainly for advanced use timing applications. There are a couple of the functions from the ```time``` module that are commonly used such as ```time``` which retrieves the time from the system hardware and ```sleep``` which is used to delay execution of a Python script:

[DateTime, ZoneInfo and Time Modules](https://github.com/PhilipYip1988/python-tutorials/blob/main/012_datetime_module/readme.md)

The ```statistics``` module is a module for working with basic statistics:

[Statistics Module](https://github.com/PhilipYip1988/python-tutorials/blob/main/013_statistics_module/readme.md)

## Programming Constructs Continued

The system module ```sys``` gives details about objects used or maintained by the Python interpreter. This gives details about the builtin modules, the standard modules and third-party modules. Custom user modules can also be added:

[The System Module and Working with Custom Modules](https://github.com/PhilipYip1988/python-tutorials/blob/main/014_system_module_custom_modules/readme.md)

This tutorial will look at the concept of a class, a subclass, an Abstract Base Class (ABC) and ultimately creating a custom class where each instance has data attributes and instance methods:

[Abstract Base Classes and Custom Classes](https://github.com/PhilipYip1988/python-tutorials/blob/main/015_abc_custom_classes/readme.md)

