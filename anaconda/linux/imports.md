# Importing Libraries

The Linux Terminal opens in the Home DIrectory by default which is represented shorthand by ```~```

<img src='images_imports/img_001.png' alt='img_001' width='450'/>

<img src='images_imports/img_002.png' alt='img_002' width='450'/>

The prefix (base) means the base Python environment is selected:

<img src='images_imports/img_003.png' alt='img_003' width='450'/>

This is found in the anaconda3 folder within Home:

<img src='images_imports/img_004.png' alt='img_004' width='450'/>

The Python program itself is found in the bin subfolder:

<img src='images_imports/img_005.png' alt='img_005' width='450'/>

And there is a python, python3 and python3.11 program (all three of these are alias to one another):

<img src='images_imports/img_006.png' alt='img_006' width='450'/>

So far the programming language bash an abbreviation for bourne again shell has been used. It has the syntax:

```
command option -p parametervalue1
command option --parametername2 parametervalue2
command option --parametername3
```

The bash command python launches the python program from the bin folder:

```
python
```

As mentioned it has two alias:

```
python3
python3.11
```

The first of these two alias is used to distinguish between Python 3 and Python 2 (in the past both of these were commonly preinstalled on Linux but Python 2 is now at end of life and not preinstalled on new distributions):

<img src='images_imports/img_007.png' alt='img_007' width='450'/>

Notice the prompt change from the bash prompt with the ```$``` to the python prompt with ```>>>```. Do not confuse these two programming languages.

Python uses syntax similar to bash for library imports and statements but functional programming otherwise. A function is called using parenthesis and these parenthesis can optionally contain input arguments:

```
fun()
fun(val1)
fun(val1, arg2=val2)
```

In the anaconda3 subfolder there is a lib subfolder:

<img src='images_imports/img_008.png' alt='img_008' width='450'/>

This has a subfolder with the Python Version:

<img src='images_imports/img_009.png' alt='img_009' width='450'/>

This subfolder contains all the Python Standard Modules. The email module is a folder:

<img src='images_imports/img_010.png' alt='img_010' width='450'/>

This folder contains an initialisation data model file ```__init__.py```, also known colloquially as dunder (**d**ouble **under**score file or special file):

<img src='images_imports/img_011.png' alt='img_011' 
width='450'/>

When the email module is imported using:

```
import email
```

The data model attribute (dunder file) can be used to check the location of the file. It can be seen to be this ```__init__.py``` file:

```
email.__file__
```

<img src='images_imports/img_012.png' alt='img_012' width='450'/>

Other script files within this folder such as ```charset.py``` can be imported with reference to this folder using a ```.``` for example:

```
import email.charset
email.charset.__file__
```

<img src='images_imports/img_013.png' alt='img_013' width='450'/>


Some of the standard modules are standalone such as ```datetime.py```:

<img src='images_imports/img_014.png' alt='img_014' width='450'/>

And are imported using:

```
import datetime
```

The file can be checked using the data model attribute dunder file:

```
datetime.__file__
```

<img src='images_imports/img_015.png' alt='img_015' width='450'/>


Third-party libraries are found in the site-packages subfolder:

<img src='images_imports/img_016.png' alt='img_016' width='450'/>

The most commonly used third-party library is numpy. There is a folder for the library alongside a folder which states the version:

<img src='images_imports/img_017.png' alt='img_017' width='450'/>

In this folder is once again the data model file, dunder init:

<img src='images_imports/img_018.png' alt='img_018' width='450'/>

The library can be imported using:

```
import numpy as np
```

Because numpy is so commonly used, it is imported with a 2 letter alias. The data model attribute dunder file can be checked:

```
np.__file__
```

<img src='images_imports/img_019.png' alt='img_019' width='450'/>

The numpy library is large and has its own modules. Some of these modules are large and have their own subfolder for example the numpy random module:

<img src='images_imports/img_020.png' alt='img_020' width='450'/>

Notice it has its own data model file dunder init:

<img src='images_imports/img_021.png' alt='img_021' width='450'/>

This can be imported using:

```
import numpy.random as random
```

And its version can be checked using:

```
random.__file__
```

<img src='images_imports/img_022.png' alt='img_022' width='450'/>

Another commonly used library is matplotlib. There is once again a folder for the library alongside a folder which states the version:

<img src='images_imports/img_023.png' alt='img_023' width='450'/>

This folder contains a data model file dunder init:

<img src='images_imports/img_024.png' alt='img_024' width='450'/>

If the library is imported using:

```
import matplotlib
```

The file can be checked using the data model attribute dunder file:

```
matplotlib.__file__
```

<img src='images_imports/img_025.png' alt='img_025' width='450'/>

It is far more common to use the pyplot module of this library instead of the full library. This module is in a single file ```pyplot.py```:

<img src='images_imports/img_026.png' alt='img_026' width='450'/>

It is commonly imported using the 3 letter alias ```plt``` using:

```
import matplotlib.pyplot as plt
```

Its file can be checked using the data model attribute dunder file:

<img src='images_imports/img_027.png' alt='img_027' width='450'/>

To exit python, use the function:

```
exit()
```

<img src='images_imports/img_028.png' alt='img_028' width='450'/>

To exit bash use the command:

```
exit
```

<img src='images_imports/img_029.png' alt='img_029' width='450'/>

Once again noticing the difference in syntax between these two programming languages.

[Return to Anaconda Tutorial](./readme.md)