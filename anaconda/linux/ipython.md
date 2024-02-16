# Interactive Python

Previously bash and Python were used in the Linux Terminal. bash is a scripting language used to navigate throughout the operating system, essentially a Terminal based version of Nautilus File Explorer. The disadvantage of this setup is the Python program needs to be exited in order to return to the bash prompt which means all variables created in the Python program will be cleared. 

ipython is an abbreviation for **i**nteractive **Python** and incorporates all the functionality of Python. ipython also incorporates ipython magics which are equivalent to the most commonly used commands from bash. 

ipython also includes similar code-completion to that seen in the IDLE shell however the docstrings do not display as popup balloons and have to be outputted to an ipython cell.

To launch ipython from the Python environment ipython use:

```
ipython
```

<img src='images_ipython/img_001.png' alt='img_001' width='450'/>

```↑``` and ```↓``` can be used to navigate through previously used commands. Inputting a prefix for example ```p``` followed by the ```↹``` key displays all the identifiers beginning with the prefix ```p```:

<img src='images_ipython/img_002.png' alt='img_002' width='450'/>

The last line of code used starting with that prefix may display and ```→``` can be used to select this completion.

Alternatively a list of identifiers display. Press the ```↹``` key to go to the first identifier. The four arrow keys ```→```, ```←```, ```↑``` and ```↓``` can be used to navigate through the identifiers. 

<img src='images_ipython/img_003.png' alt='img_003' width='450'/>

If a function is highlighted concise details about its input arguments will display along a single line:

<img src='images_ipython/img_004.png' alt='img_004' width='450'/>

Note some of the identifiers start with a ```%```, these are known as ipython magics and are essentially bash commands for example to print the working directory:

```
%pwd
```

<img src='images_ipython/img_005.png' alt='img_005' width='450'/>

Some of the ipython magics begin with %% for example:

```
%%python3
```

This indicates that the command runs over multiple lines:

<img src='images_ipython/img_006.png' alt='img_006' width='450'/>

The ```?``` can be used to output the docstring of a python function for example:

```
? print
```

Alternatively it can be used similar to a question mark in the English language:

```
print?
```

<img src='images_ipython/img_007.png' alt='img_007' width='450'/>

<img src='images_ipython/img_008.png' alt='img_008' width='450'/>

The screen can be cleared using the ipython magic:

```
%clear
```

<img src='images_ipython/img_009.png' alt='img_009' width='450'/>

The builtins module is automatically imported using the data model attribute dunder builtins, therefore all builtin identifiers can be viewed by inputting ```__builtins__.``` followed by a ```↹```:

<img src='images_ipython/img_010.png' alt='img_010' width='450'/>

This excludes the ipython magics which can be viewed by inputting ```%``` followed by a ```↹```:

<img src='images_ipython/img_011.png' alt='img_011' width='450'/>

The bash commands **p**rint **w**orking **d**irectory and **c**hange **d**irectory can be used:

```
%pwd
%cd
```

The directory can be changed to ```~/Documents``` using:

```
%cd ~/Documents
```

A new directoy can be made using the bash command:

```
%mkdir 'new directory'
```

<img src='images_ipython/img_012.png' alt='img_012' width='450'/>

<img src='images_ipython/img_013.png' alt='img_013' width='450'/>

The bash command:

```
%clear
```

can be used to clear the terminal. Although the terminal is cleared, the kernel is still active, meaning previously instantiated variables and library imports are still available. This is indicated by the prompt; notice the continues from the next integer:

<img src='images_ipython/img_014.png' alt='img_014' width='450'/>

The command ```%%writefile``` is a multiline command:

```
%%writefile.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})

plt.show()
```

Notice that a new line of code are added to this script file every time ```↵``` is used:

<img src='images_ipython/img_015.png' alt='img_015' width='450'/>

The command will exit when two blank lines are added:

<img src='images_ipython/img_016.png' alt='img_016' width='450'/>

The bash command **l**i**s**t is:

```
%ls
```

<img src='images_ipython/img_017.png' alt='img_017' width='450'/>

Both the directory ```new directory``` and the ```script.py``` are shown:

<img src='images_ipython/img_018.png' alt='img_018' width='450'/>

<img src='images_ipython/img_019.png' alt='img_019' width='450'/>

The script can be run using the command ```%run```:

```
%run script.py
```

<img src='images_ipython/img_020.png' alt='img_020' width='450'/>

The plot displays in a new interactive window. Notice that the terminal is busy while the plot is open: 

<img src='images_ipython/img_021.png' alt='img_021' width='450'/>

When the plot is closed, the new prompt displays:

<img src='images_ipython/img_022.png' alt='img_022' width='450'/>

The directory ```new directory``` and the ```script.py``` can be **r**e**m**oved using:

```
%rmdir 'new directory'
%rm script.py
```

<img src='images_ipython/img_023.png' alt='img_023' width='450'/>

<img src='images_ipython/img_024.png' alt='img_024' width='450'/>

Inputting a prefix for example ```c``` displays the previously used command that begins with that prefix. 

<img src='images_ipython/img_025.png' alt='img_025' width='450'/>

```→``` can be used to select this completion:

<img src='images_ipython/img_026.png' alt='img_026' width='450'/>

```↑``` and ```↓``` can also be used to navigate through previously used commands. The bash command:

```
%conda
```

can be used to access the conda package manager:

<img src='images_ipython/img_027.png' alt='img_027' width='450'/>

<img src='images_ipython/img_028.png' alt='img_028' width='450'/>

If ```!``` is input followed by a ```↹``` all the Python and IPython commands will be listed:

<img src='images_ipython/img_029.png' alt='img_029' width='450'/>

<img src='images_ipython/img_030.png' alt='img_030' width='450'/>

Note that these commands should be used without prefixing with the ```!``` which is why the ```!``` isn't listed as a prefix in any of the identifiers listed.

Prefixing a command with ```!``` will attempt to use the bash command directly:

```
!cd ~\Documents
```

Opposed to the reimplementation of the bash command in the form of an IPython Magic:

```
%cd ~\Documents
```

The following warning will display when the Pbash command is used opposed to the IPython magic *UserWarning: You executed the system command !cd which may not work as expected. Try the IPython magic %cd instead.* In other words there are some improvements made in the IPython magic so that it doesn't just change the directory in the Terminal using bash but also changes the directory within IPython itself:

<img src='images_ipython/img_031.png' alt='img_031' width='450'/>

When a Python command is prefixed with the ```!``` code, it will instead attempt to use a bash command and not find it:

```
!str('Hello World!')
```

```
str('Hello World!')
```

<img src='images_ipython/img_032.png' alt='img_032' width='450'/>

```!``` can however be used to run a bash command that isn't available as an IPython magic. 

The bash command ```nano``` is not reimplemented as an IPython magic and the following therefore gives a command not found error:

```
%nano script2.py
```

However ```nano``` is useful to use in an ipython console and the bash command can be accessed using:

```
!nano script2.py
```

<img src='images_ipython/img_033.png' alt='img_033' width='450'/>

And the following "sloppy" Python code can be added and the file saved by pressing ```Ctrl```+```x``` to exit followed alongside the other prompts to save the file:

```
var1='Hello'
var2="World"
import numpy as np
x=np.array([0,1,2,3,4])
y=np.array([0,2,4,6,8])
import pandas as pd
df=pd.DataFrame({'x':x,"y":y})
import datetime
now=datetime.datetime(year=2023,month=12,day=1)
hour=datetime.timedelta(hours=1)
import collections
counts=collections.Counter([1,2,2,2,3,3])
import itertools
cycle=itertools.cycle([1,2,3])
```

<img src='images_ipython/img_034.png' alt='img_034' width='450'/>

This sloppy code does not follow the spacing guidelines in Pythons [PEP8](https://peps.python.org/pep-0008/). ```autopep8``` is a Python formatter that formats spacing in a Python script file in accordance to Pythons PEP8. It is preinstalled in the Anaconda base Python environment.

```autopep8``` is another bash command not reimplemented as an IPython magic and the following gives a command not found error:

```
%autopep8 script2.py
```

The bash command can be run directly using:

```
!autopep8 script2.py
```

To make the places in-place the command option ```--in-place``` can be added

```
!autopep8 --in-place script2.py
```

The changes inplace can be seen using:

```
!nano script2.py
```

<img src='images_ipython/img_035.png' alt='img_035' width='450'/>

<img src='images_ipython/img_036.png' alt='img_036' width='450'/>

```black``` is an opinionated formatter that carries out additional opinionated formatting inplace. It is also preinstalled in the Anaconda base Python environment:

```
!black script2.py
```

The changes can once again be seen by opening up the file using:

```
!nano script2.py
```

<img src='images_ipython/img_037.png' alt='img_037' width='450'/>

Notice that additional spacing has been added and that all the strings now consistently use double quotations:

<img src='images_ipython/img_038.png' alt='img_038' width='450'/>

Note ```autopep8``` and then ```black``` on a file seems to work better than using ```black``` directly.

Despite the python interpretter, Python ```builtins``` and other Python standard modules preferencing single quotations, PEP8 recognises that the wider Python community is somewhat divided over quotation preference. [PEP8](https://peps.python.org/pep-0008/) states: *In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this.* However PEP8 itself subtly recommends preferencing single-quote strings as all the content written in PEP8 preferences single-quote strings, consistent with Pythons official documentation.

```black``` on the other hand unfortunately preferences double quotations making it inconsistent with Pythons formal documentation. There is a complementary autoformatter ```blue``` which is based on ```black``` but adjusts the quotations to single quotations. Sadly this isn't included in the Anaconda base Python Environment and a seperate Python environment needs to be made with packages from the community channel ```conda-forge```.

To exit ipython use the python function:

```
exit()
```

<img src='images_ipython/img_039.png' alt='img_039' width='450'/>

<img src='images_ipython/img_040.png' alt='img_040' width='450'/>

[Return to Anaconda Tutorial](./readme.md)
