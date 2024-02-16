# PowerShell

## PowerShell Basics

When the Anaconda PowerShell Prompt is open by default, it defaults to %USERPROFILE%:

<img src='images_powershell/img_001.png' alt='img_001' width='350'/>

<img src='images_powershell/img_002.png' alt='img_002' width='350'/>

<img src='images_powershell/img_003.png' alt='img_003' width='350'/>

The current directory can be changed using the command **c**hange **d**irectory because Documents is a subfolder of the current working directory it can be specified directly:

```
cd Documents
```

<img src='images_powershell/img_004.png' alt='img_004' width='350'/>
<img src='images_powershell/img_005.png' alt='img_005' width='350'/>

Using ~ in the Anaconda PowerShell Prompt is equivalent to using %USERPROFILE% in Windows Explorer:

```
cd ~
```

<img src='images_powershell/img_006.png' alt='img_006' width='350'/>

A . is used to represent the same folder:

```
cd .\
```

A .. is used to represent a folder up a level:

```
cd ..\
```

To go up two more levels:

```
cd ..\..\
```

To go to Documents directly:

```
cd ~\Documents
```

<img src='images_powershell/img_007.png' alt='img_007' width='350'/>

The command **cl**ear **s**creen can be used to clear the screen:

```
cls
```

<img src='images_powershell/img_008.png' alt='img_008' width='350'/>

To create a Python script file the command **n**ew **i**tem can be used alongside the name of the script file, including the file extension. It will be placed in Documents, because it is the current working directory:

```
ni script.py
```

<img src='images_powershell/img_009.png' alt='img_009' width='350'/>

<img src='images_powershell/img_010.png' alt='img_010' width='350'/>

Details about the directory can be viewed using the command **l**i**s**t:

```
ls
```

<img src='images_powershell/img_011.png' alt='img_011' width='350'/>

The script file can be opened in notepad using the command notepad followed by the name of the file:

```
notepad script.py
```

other commands such as calc and mspaint can be used to open other Windows applications:

<img src='images_powershell/img_012.png' alt='img_012' width='350'/>

The script file can be updated to include some Python code:

```
print('Hello World!')
```

<img src='images_powershell/img_013.png' alt='img_013' width='350'/>

This can be executed using python followed by the name of the script file:

```
python script.py
```

<img src='images_powershell/img_014.png' alt='img_014' width='350'/>

Notice the code just runs and there is no Python prompt like in the case when python is ran without a script file.

<img src='images_powershell/img_015.png' alt='img_015' width='350'/>

If the command type is input followed by the script file, it will type the contents of the script file in the console:

```
type script.py
```

<img src='images_powershell/img_016.png' alt='img_016' width='350'/>

If the code in the script file is modified to:

```
import time
time.sleep(5000)
```

<img src='images_powershell/img_017.png' alt='img_017' width='350'/>

Then the Python being ran by the Anaconda PowerShell Prompt will hang:

<img src='images_powershell/img_018.png' alt='img_018' width='350'/>

Ctrl+c can be pressed to cancel the currently running operation:

<img src='images_powershell/img_019.png' alt='img_019' width='350'/>

To copy Ctrl+⇧+c is used and to paste Ctrl+⇧+v is used.

The command **m**a**k**e **dir**ectory can be used to make a new directory followed by the name of the directory:

```
mkdir directory
```

<img src='images_powershell/img_020.png' alt='img_020' width='350'/>

Note directory names can include spaces. When directories include spaces they should be enclosed in double quotations. 

```
mkdir "new directory"
```

<img src='images_powershell/img_021.png' alt='img_021' width='350'/>

Without spaces two directories ```new``` and ```directory``` would be created.

Single quotations cannot be used for a directory as they are reconised as part of the directory name ```'new``` and ```directory'``` would be created.

A directory can be removed using the command **r**e**m**ove **dir**ectory:

<img src='images_powershell/img_022.png' alt='img_022' width='350'/>

<img src='images_powershell/img_023.png' alt='img_023' width='350'/>

To recap:

|command|command description|
|---|---|
|cd|**c**hange **dir**ectory|
|cls|**cl**ears the **s**creen|
|mkdir|**m**a**k**e **dir**ectory|
|rmdir|**r**e**m**oves **dir**ectory|
|type|**type**s the contents of a text file|
|notepad|launches notepad|
|calc|launches calculator|
|mspaint|launches paint|

## Launching Python IDEs

The Anaconda (base) Python environment also includes the following PowerShell Commands:

|command|command description|
|---|---|
|python|launches python|
|conda|conda package manager|
|anaconda-navigator|launches the Anaconda Navigator|
|idle|Launches IDLE|
|ipython|launches interactive python|
|jupyter lab|Launches JupyterLab (lab gives the option lab)|
|jupyter|Launches Jupyter Notebook (legacy)|
|spyder|Launches Spyder|
|code|Launches VSCode (if installed)|

For example inputting:

```
conda
```

gives details about the conda package manager which will be covered in more detail later:

<img src='images_powershell/img_024.png' alt='img_024' width='350'/>

Inputting:

```
anaconda-navigator
```

launches the Anaconda-Navigator:

<img src='images_powershell/img_025.png' alt='img_025' width='350'/>

This contains tiles for most of the applications available from the (base) Python environment:

<img src='images_powershell/img_026.png' alt='img_026' width='350'/>

When running the Anaconda PowerShell Prompt will hang as it is running a process that is busy:

<img src='images_powershell/img_027.png' alt='img_027' width='350'/>

The Anaconda Navigator is also a GUI version of the conda package manager.

<img src='images_powershell/img_028.png' alt='img_028' width='350'/>

When closed, the Anaconda PowerShell Prompt displays the next Prompt as the process that was busy has now stopped:

<img src='images_powershell/img_029.png' alt='img_029' width='350'/>

[Return to Anaconda Tutorial](./readme.md)