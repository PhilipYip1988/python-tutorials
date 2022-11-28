# Python Tutorials

This set of tutorials will look at the Python Programming Language using the markdown and notebook aspects of the JupyterLab IDE. All the tutorials are written in markdown with a large number of screenshots to help demonstrate the programming concepts and highlight interaction with the JupyterLab IDE. The code snippets can be copied and pasted or better typed into your own interactive notebook which you can open on your second monitor while reading through these markdown tutorials.

## Installation

The Python ecosystem is very large and has multiple package managers for third-party libraries and numerous IDEs available for writing Python code. This installation tutorial is very detailed as it explains how to use Python from the Terminal, the IDLE IDE, the Spyder IDE, the JupyterLab IDE and the Visual Code IDE and how to use the Mamba package manager to create Python Environments, examining what is going on behind the scenes in the file explorer.

[Mambaforge Installation](./001_install/)

## Markdown

The JupyterLab IDE has the ability to write formatted notes in a Markdown file. This tutorial will cover the basics of Markdown syntax. All of these tutorials are written using this basic Markdown syntax. It is also possible to use this knowledge in a Notebook with Markdown cells.  

[Markdown Tutorial](./002_markdown/)

## Terminal

When running Python code from the Terminal, two programming languages are used. In Linux and Mac there is the inbuilt programming language bash and in Windows there is PowerShell which closely resembles bash. The bash programming language is optimised for basic file operations within the operating system and is commonly used in conjunction with Python. bash however uses a different programming syntax to Python and this tutorial will cover basic file operating systems using bash. Familarity with bash before delving into Python will prevent later confusion when using the terminal with Python commands.

[Terminal Commands](./003_terminal/)

## Python Builtins

Data is stored fundamentally as a text or as a number. This tutorial will examine the three types of number data types, boolean values which are True or False, whole numbers known as integers and floating point numbers in addition to the fundamental text data type, the string. The builtin identifiers for each of these datatypes will be examined:

[Fundamental Datatypes int, float, str, bool](./004_python_fundamental_datatypes/)

This tutorial looks at the practical applications of using numeric and text data types. It also examines how these data types are used with hardware to communicate with a user and highlights the differences in numbering systems used by humans versus the numbering systems used by computers and some important consequences when dealing with both these numbering systems:

[Understanding Numbering Systems](./005_numbering_systems/)

So far, only single text or numeric values have been considered. A collection can be used to group data. The string itself behaves as a collection as it is a collection of characters. This tutorial will examine the collection properties of the string, before moving onto the list, tuple, set and dictionary collections.

[Collections; str, list, tuple, set, dict](./006_collections/)

Indentation and spacing is very important in Python and code is often grouped into a code block. An analogy to not using indentation in Python, is not not use a steering wheel in a car. All the code so far has been run in a straight line going from start to finish. Indentation with a code block can be used to repeat code multiple times in a loop or to direct code in response to a condition. 

[Code Blocks; for loops, if-elif-else, match-case, while loops, try-except-else-finally](./007_code_blocks/)

The behaviour of functions in inbuilt identifiers has been explored. Functions have been observed to have no, one or multiple input arguments and to return or not return a value. To understand this syntax better, custom functions will be explored. Under the hood these use a code block and therefore this tutorial builds upon the knowledge of previous tutorial. Custom functions are a very powerful tool.

[Functions](./008_functions/)

Previously for loops and functions were explored. A loop is commonly used to construct a new list or dictionary from an existing list or dictionary and Python has a very powerful one line convention known as a comprehension to carry this out. A simple function can also be created on a single line using a lambda expression. Use of comprehensions and lambda expressions can make the code more succinct and more readible.

[Comprehensions (list and dict) and Lambda Functions](./009_comprehensions_and_lambda_expressions/)

The concept of a Python Module was previously explored during installation. A Python Module is used to compartmentalise code into a seperate often reusable file. This tutorial looks at the creation of a custom Module or a group of custom Modules known as a library. 

[Modules](./010_modules/)

Previously inbuild classes such as the int, bool, float, str, list, tuple, set and dict were explored. Each instance of a class had instance data attributes and functions which were designed to operate on this instance data. The template for this data and the function definition for these definitions are given in the class itself. This tutorial looks at the concept of a Python object and the use of it to create a custom class.

[Classes](./011_classes/)

## Python Standard Modules

Python standard modules are inbuilt modules included with the Python installation. Each standard module is compartmentalised for a specific purpose, that is common but not as common as the builtin identifiers which have previously been used.

The builtins module contains the str, list, tuple, set and dict collections. The collections module includes a number of additional collections which supplement these such as the deque (double ended queue that is list like), defaultdict (dictionary with default behaviour for new keys), NamedTuple (tuple with named fields) and Counter (dictionary of counts) collection. A number of these collections almost became inbuilt identifiers themselves and therefore this is one of the closest modules to python builtins.

[Collections Module](./012_collections/) 

This guide looks at the use of the Operating System module and the shell utilities shutil module. These modules are used to carry out file operations within Python and behave similar to the equivalent commands in bash. This tutorial will examine how to read and write data to a text file:

[File and Directory Operations with the os and shutil Modules](./013_os_module/)

The previous guide looked at working with text data. Another common data type is the Comma Seperated Values (CSV) which as the name suggests uses a comma as a delimiter to seperate data into columns. The CSV Module can be used to read or write data from or to a CSV file. The Pickle module can be used to pickle a variable into a byte stream or unpickle a variable into a Python object which is useful for data tranfer over a serial port for example. This byte stream can also be saved to file so a variable can be loaded in a later session opposed to being recreated. The pickled data is easy for a computer to read but not very human readible. Another common datatype is the JavaScript Object Notation (JSON) which is a more complicated data stream that is more user readible than pickled data. The JSON syntax originated from JavaScript but is similar to a Python dictionary with some subtle differences. Despite originating from JavaScript, the JSON data stream has become a commonly used standard data stream used to store data for all programming languages and most data on a website is stored in JSON for example. The JSON Module can be used to convert between a JSON syntax and a Python dictionary. 

[CSV, Pickle and JSON Modules](./014_csv_pickle_json/)

The math module is used to carry out common mathematical operations on scaler numeric data. Learning how to use this module and reinforcing the underlying mathematics is a perquisite when it comes to any data science tasks. There is an associated complex math module cmath which is designed to handle complex numbers.

[Math and Complex Math Modules](./015_math/)

Random Module

DateTime Module

Fraction Module

Statistics Module


