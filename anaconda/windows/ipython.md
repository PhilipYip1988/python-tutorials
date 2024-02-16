# Interactive Python

Previously PowerShell and Python were used in the Anaconda PowerShell Prompt. PowerShell is a scripting language used to navigate throughout the operating system, essentially a Terminal based version of Windows Explorer. The disadvantage of this setup is the Python program needs to be exited in order to return to the PowerShell Prompt which means all variables created in the Python program will be cleared. 

ipython is an abbreviation for **i**nteractive **Python** and incorporates all the functionality of Python. ipython also incorporates ipython magics which are equivalent to the most commonly used commands from PowerShell. ipython magics use the same syntax as bash which it the open source PowerShell equivalent in Linux. PowerShell and Linux use a similar syntax.

ipython also includes similar code-completion to that seen in the IDLE shell however the docstrings do not display as popup balloons and have to be outputted to an ipython cell.

To launch ipython from the Python environment ipython use:

```
ipython
```

<img src='images_ipython/img_001.png' alt='img_001' width=450/>

Details about the Python version will display, alongside the integer based ipython prompt:

<img src='images_ipython/img_002.png' alt='img_002' width=450/>

A previously input line that matches the prefix input may display as a completion when inputting code. You can use the ```→``` to select this completion or use the ```↑``` and ```↓``` arrow keys to scroll through previous completions that match this prefix:

<img src='images_ipython/img_003.png' alt='img_003' width=450/>

Notice that when ```p``` is input the last command inputting beginning with p displays. The previous few commands can be cycled through using the ```↑``` and ```↓``` arrow keys:

<img src='images_ipython/img_004.png' alt='img_004' width=450/>

Alternatively builtin identifiers can be listed by pressing the ```↹``` key. These can be scrolled through by pressing the arrow keys ```→```, ```←```, ```↑``` and ```↓```. If a function is highlighted concise details about its input arguments will display along a single line:

<img src='images_ipython/img_005.png' alt='img_005' width=450/>

ipython magics are distingished from Python objects as they begin with a %:

<img src='images_ipython/img_006.png' alt='img_006' width=450/>

The ipython magics beginning with %% span over multiple lines:

<img src='images_ipython/img_007.png' alt='img_007' width=450/>

Using ? followed by a Python function will display the functions docstring:

```
? print
```

<img src='images_ipython/img_008.png' alt='img_008' width='450'/>

This also works using:

```
print?
```

<img src='images_ipython/img_041.png' alt='img_041' width='450'/>

A simple print statement can be executed using:

```
print('Hello World!')
```

<img src='images_ipython/img_009.png' alt='img_009' width='450'/>

To **cl**ear the **s**creen, the ipython magic %cls can be used:

```
%cls
```

<img src='images_ipython/img_010.png' alt='img_010' width='450'/>

clearing the screen does not reset the integer prompt back to 1.

<img src='images_ipython/img_011.png' alt='img_011' width='450'/>

Python identifiers available in the global scope are from the builtins module. To see these grouped together, the builtins module can explicitly be imported using:

```
import builtins
```

A list of identifiers can be seen by inputting ```builtins.``` followed by a ```↹```. There are a large number of identifiers and the arrow keys can be used to cycle through them:

<img src='images_ipython/img_012.png' alt='img_012' width='450'/>

The ipython magics can be viewed by inputting ```%``` followed by a ```↹```:

<img src='images_ipython/img_013.png' alt='img_013' width='450'/>

The ipython magics behave in a similar manner to their counterparts previously explored when using PowerShell:

```
%pwd
%cd 
%cd ~\Documents
%mkdir directory
```

The multiline ipython magic ```%%writefile``` is a multiline file. Notice that it ends after 2 blank lines:

```
%%writefile script.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})
plt.plot(df['x'], df['y'])
plt.show()
```

<img src='images_ipython/img_014.png' alt='img_014' width='450'/>

The ipython magic ```%ls``` behaves similarly to its PowerShell counterpart:

```
%ls
```

<img src='images_ipython/img_015.png' alt='img_015' width='450'/>

The Python script file can be run using the ipython magic ```%run```:

<img src='images_ipython/img_016.png' alt='img_016' width='450'/>

The ipython magic ```%edit``` replaces the PowerShell command notepad:

```
%edit script.py
```
<img src='images_ipython/img_017.png' alt='img_017' width='450'/>

<img src='images_ipython/img_018.png' alt='img_018' width='450'/>

Code can be input into notepad:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})
plt.plot(df['x'], df['y'])
plt.show()
```

<img src='images_ipython/img_019.png' alt='img_019' width='450'/>

When notepad is closed the script will run:

<img src='images_ipython/img_020.png' alt='img_020' width='450'/>

If ```!``` is input followed by a ```↹``` all the Python and IPython commands will be listed:

<img src='images_ipython/img_042.png' alt='img_042' width='450'/>

<img src='images_ipython/img_043.png' alt='img_043' width='450'/>

<img src='images_ipython/img_044.png' alt='img_044' width='450'/>

Note that these commands should be used without prefixing with the ```!``` which is why the ```!``` isn't listed as a prefix in any of the identifiers listed.

Prefixing a command with ```!``` will attempt to use the PowerShell command directly:

```
!cd ~\Documents
```

Opposed to the reimplementation of the PowerShell command in the form of an IPython Magic:

```
%cd ~\Documents
```

The following warning will display when the PowerShell command is used opposed to the IPython magic *UserWarning: You executed the system command !cd which may not work as expected. Try the IPython magic %cd instead.* In other words there are some improvements made in the IPython magic so that it doesn't just change the directory in the Terminal using PowerShell but also changes the directory within IPython itself:

<img src='images_ipython/img_045.png' alt='img_045' width='450'/>

When a Python command is prefixed with the ```!``` code, it will instead attempt to use a PowerShell Command and not find it:

```
!str('Hello World!')
```

```
str('Hello World!')
```

<img src='images_ipython/img_046.png' alt='img_046' width='450'/>

```!``` can however be used to run a PowerShell command that isn't available as an IPython magic. 

If for example a new Python Script file is made using the IPython magic:

```
%edit script2.py
```

<img src='images_ipython/img_047.png' alt='img_047' width='450'/>

And yes is selected in notepad to create a new file:

<img src='images_ipython/img_048.png' alt='img_048' width='450'/>

And the following "sloppy" Python code is added and the file saved:

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

<img src='images_ipython/img_049.png' alt='img_049' width='450'/>

This sloppy code does not follow the spacing guidelines in Pythons [PEP8](https://peps.python.org/pep-0008/). ```autopep8``` is a Python formatter that formats spacing in a Python script file in accordance to Pythons PEP8. It is preinstalled in the Anaconda base Python environment.

This PowerShell command is not reimplemented as an IPython magic:

```
%autopep8 script2.py
```

And therefore the PowerShell command can be run directly using:

```
!autopep8 script2.py
```

To make the places in-place the command option ```--in-place``` can be added

```
!autopep8 --in-place script2.py
```

<img src='images_ipython/img_050.png' alt='img_050' width='450'/>

If opened in notepad the changes can be seen to be made inplace:

<img src='images_ipython/img_051.png' alt='img_051' width='450'/>

```black``` is an opinionated formatter that carries out additional opinionated formatting inplace. It is also preinstalled in the Anaconda base Python environment:

```
!black script2.py
```

<img src='images_ipython/img_052.png' alt='img_052' width='450'/>

Notice that additional spacing has been added and that all the strings now consistently use double quotations:

<img src='images_ipython/img_053.png' alt='img_053' width='450'/>

Note ```autopep8``` and then ```black``` on a file seems to work better than using ```black``` directly.

Despite the python interpretter, Python ```builtins``` and other Python standard modules preferencing single quotations, PEP8 recognises that the wider Python community is somewhat divided over quotation preference. [PEP8](https://peps.python.org/pep-0008/) states: *In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this.* However PEP8 itself subtly recommends preferencing single-quote strings as all the content written in PEP8 preferences single-quote strings, consistent with Pythons official documentation.

```black``` on the other hand unfortunately preferences double quotations making it inconsistent with Pythons formal documentation. There is a complementary autoformatter ```blue``` which is based on ```black``` but adjusts the quotations to single quotations. Sadly this isn't included in the Anaconda base Python Environment and a seperate Python environment needs to be made with packages from the community channel ```conda-forge```.

The default script editor on Windows is notepad. This is lightweight but has no syntax highlighting for Python code or code completions.

A common replacement is Notepad++ which has syntax highlighting by unfortunately no code completions.

Notepad++ can be installed using its installer

<img src='images_ipython/img_021.png' alt='img_021' width='450'/>

Select your language and select OK:

<img src='images_ipython/img_022.png' alt='img_022' width='250'/>

Select Next:

<img src='images_ipython/img_023.png' alt='img_023' width='350'/>

Select I agree:

<img src='images_ipython/img_024.png' alt='img_024' width='350'/>

Observer the installation folder and select next:

<img src='images_ipython/img_025.png' alt='img_025' width='350'/>

Select next:

<img src='images_ipython/img_026.png' alt='img_026' width='350'/>

Select install:

<img src='images_ipython/img_027.png' alt='img_027' width='350'/>

Select Finish:

<img src='images_ipython/img_028.png' alt='img_028' width='350'/>

To change the default editor used an environmental variable needs to be added. Right click the start button and select system:

<img src='images_ipython/img_029.png' alt='img_029' width='250'/>

Select Advanced System Settings:

<img src='images_ipython/img_030.png' alt='img_030' width='450'/>

Select Environmental Variables:

<img src='images_ipython/img_031.png' alt='img_031' width='450'/>

Select New:

<img src='images_ipython/img_032.png' alt='img_032' width='450'/>

Input ```EDITOR``` as the variable name:

<img src='images_ipython/img_033.png' alt='img_033' width='450'/>

The install location of Notepad++ can be viewed:

<img src='images_ipython/img_034.png' alt='img_034' width='450'/>

In Variable value input the file path to the .exe

```
"C:\Program Files\Notepad++\notepad++.exe"
```

Note quotations are required as there is a space between Program Files in the file path:

<img src='images_ipython/img_035.png' alt='img_035' width='450'/>

Select OK:

<img src='images_ipython/img_036.png' alt='img_036' width='450'/>

To refresh the Environmental Variables used by the Anaconda PowerShell Prompt close and relaunch the Anaconda PowerShell Prompt.

Change the directory to Documents:

```
%cd ~\Documents
```

Now edit the script file using the ipython magic:

```
%edit script.py
```

<img src='images_ipython/img_037.png' alt='img_037' width='450'/>

Now notepad++ will open:

<img src='images_ipython/img_038.png' alt='img_038' width='450'/>

When notepad++ is closed, the script will be executed:

<img src='images_ipython/img_039.png' alt='img_039' width='450'/>

Note having this environmental variable may result in some IDEs such as VSCode being unable to open up text files.

[Return to Anaconda Tutorial](./readme.md)