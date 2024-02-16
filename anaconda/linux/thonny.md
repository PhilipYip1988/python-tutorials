# Thonny

The previous tutorial looked at ID**L**E which as the name suggests is a popular Learner IDE. Another popular learner IDE is Thonny and is the Python IDE preinstalled on a Raspberry Pi for example.

## Installing Thonny

Thonny is not preinstalled using conda as it has no package on the anaconda or conda-forge channels. It can be installed on Ubuntu using the snap package from Software. 

Note other Linux distros use different package managers which may be outdated. Ensure the version is 4.1.2 or later.

Select Install:

<img src='images_thonny/img_001.png' alt='img_001' width='400'/>

Once installed, a shortcut to Thonny will be seen on the All Apps screen:

<img src='images_thonny/img_002.png' alt='img_002' width='400'/>

When Thonny is first launched you will be prompted for your language, and initial settings. Select Let's go:

<img src='images_thonny/img_003.png' alt='img_003' width='250'/>

## Selecting the Python Interpretter

Thonny has its own inbuilt Python environment:

<img src='images_thonny/img_004.png' alt='img_004' width='400'/>

And has a GUI utility to install packages based upon pip:

<img src='images_thonny/img_005.png' alt='img_005' width='400'/>

This Python environment is very basic and lacks the commonly used third-party data science libraries and lacks the conda package manager.

For best results, the Python environment should be changed. Select Tools → Options:

<img src='images_thonny/img_006.png' alt='img_006' width='400'/>

In interpreter select the dropdown or ... to browse using file explorer:

<img src='images_thonny/img_007.png' alt='img_007' width='450'/>

Navigate to the anaconda3 folder and select the python3.11 program then select OK:

<img src='images_thonny/img_008.png' alt='img_008' width='250'/>

Select OK:

<img src='images_thonny/img_009.png' alt='img_009' width='450'/>

The conda Python environment will be selected:

<img src='images_thonny/img_010.png' alt='img_010' width='400'/>

## Thonny Shell and Script Editor

Thonny has a Script Editor and a Shell similar to IDLE. 

If ```p``` is input followed by a ```↹``` a list of identifiers display. The arrow keys ```↑``` and ```↓``` can be used to move up and down through this list and the docstring displays when the currently selected identifier is a function:

<img src='images_thonny/img_011.png' alt='img_011' width='400'/>

Thonny has a script editor and a shell similar to IDLE. Select File → Save As:

<img src='images_thonny/img_012.png' alt='img_012' width='400'/>

Save the file as a Python Script File (.py extension):

<img src='images_thonny/img_013.png' alt='img_013' width='450'/>

A test script file containing the code:

```
print('Hello World!')
```

can be run by selecting Run current script:

<img src='images_thonny/img_014.png' alt='img_014' width='400'/>

The print statement displays in the Shell:

<img src='images_thonny/img_015.png' alt='img_015' width='400'/>

The Kernel can be restarted by using Stop/Restart backend:

<img src='images_thonny/img_016.png' alt='img_016' width='400'/>

This will clear the history in the Shell, all variables instantiated and close all libraries imported:

<img src='images_thonny/img_017.png' alt='img_017' width='400'/>

Some Python test code can be added to the script and it can be saved:

```
string = 'hello'
bytestring = b'hello'
bytearraystring = bytearray(b'hello')
integer = 1
boolean = True
floatingpoint = 3.14
archive = (string, string, integer, boolean)
active = [string, string, integer, boolean]
unique = {string, string, integer, boolean}
mapping = {'r': 'red', 'g': 'green', 'b': 'blue'}
```

<img src='images_thonny/img_018.png' alt='img_018' width='400'/>

If an error is deliberately introduced such as an unmatched bracket and the code is run an Error displays in the Shell and the IDLE Assistant gives more details:

<img src='images_thonny/img_019.png' alt='img_019' width='400'/>

If this is error is fixed and the code is rerun:

<img src='images_thonny/img_020.png' alt='img_020' width='400'/>

The Assistant will say the code in the script looks good:

<img src='images_thonny/img_021.png' alt='img_021' width='400'/>

One of Thonnys strengths is it has has an option to view variables. Select View → Variables:

<img src='images_thonny/img_022.png' alt='img_022' width='400'/>

Code completion for Thonny only works in the Shell. The workflow for Thonny is usually to use the Shell line by line to test each line of code and then for each successful line of code to be added to the Python script.

A simple test can be put together which uses the third-party data science libraries:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
df = pd.DataFrame({'x': x,
                   'y': y})

plt.plot(df['x'], df['y'])
plt.show()
```

Thonny seems unable to access the TkAgg backend for Matplotlib in my case and does not show any plots.

<img src='images_thonny/img_023.png' alt='img_023' width='400'/>

[Return to Anaconda Tutorial](./readme.md)