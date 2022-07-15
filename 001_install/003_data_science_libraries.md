# Python packages

Data Science Libraries are in the form of Python Packages.

Anaconda is the Python Data Science Distribution and the Anaconda base environment includes the most commonly used data science libraries.

On a Windows installation the data science libraries are contained in the following folders:

```%UserProfile%\anaconda3\Lib\site-packages\numpy```

```%UserProfile%\anaconda3\Lib\site-packages\pandas```

```%UserProfile%\anaconda3\Lib\site-packages\matplotlib```

You can copy and paste the above into Windows Explorer to view the contents.

These folders are known as Python packages and the folder name is the same as the package name. 

Python packages contain a number of Python script files, that is files containing Python code ending with the .py extension. 

# \_\_init\_\_.py

In the parent folder of the Python package there will be a ```__init__.py``` file. 

This file is imported when the package is imported.

Using:

```import numpy```

```import numpy```


Imports:

```%UserProfile%\anaconda3\Lib\site-packages\numpy\__init__.py```

```%UserProfile%\anaconda3\Lib\site-packages\pandas\__init__.py```


# module from a Python package

A module from a Python package can be accessed using the ```.``` syntax in the form ```package.module```.

#### module.py in package Parent Folder

The module can either be physically contained in the parent folder of the Python package.

Using:

```import matplotlib.pyplot```

Imports:

```%UserProfile%\anaconda3\Lib\site-packages\numpy\pyplot.py```

In this case ```pyplot.py``` is found in the parent folder ```matplotlib``` and we are importing this module instead of the entire library.

## module as subfolder

Or more complicated modules can be contained in their own subfolder. The name of the subfolder will be the name of the module and this subfolder has to contain its own ```__init__.py``` file.

Using:

```import numpy.linalg```

Imports:

```%UserProfile%\anaconda3\Lib\site-packages\numpy\linalg\__init__.py```

## as alias

Typically the libraries numpy and pandas and the module pyplot from the library matplotlib are extensively used so they are imported using a 2-3 letter word alias.

```np```

```pd```

```plt```
