# bash

The programming language of the Linux Terminal is called bash, an abbreviation for bourne again shell. This shell scripting language is essentially a terminal based equivalent of nautilus:

## bash Basics

The default directory for the terminal is ```~``` which is the Home folder i.e. the Linux equivalent to the Windows User Profile:

<img src='images_bash/img_001.png' alt='img_001' width='450'/>

The Home folder can be viewed in nautilus:

<img src='images_bash/img_002.png' alt='img_002' width='450'/>

The command **l**i**s**t:

```
ls
```

can be used to list all files and subdirectories:

<img src='images_bash/img_003.png' alt='img_003' width='450'/>

Because the Documents (capitalised) is a subfolder, the directory can be changed to Documents using the command **c**hange **d**irectory:

```
cd Documents
```

<img src='images_bash/img_004.png' alt='img_004' width='450'/>

Which is the following location in nautilus:

<img src='images_bash/img_005.png' alt='img_005' width='450'/>

It can be changed back to the Home folder using:

```
cd ~
```

<img src='images_bash/img_006.png' alt='img_006' width='450'/>

* ```./``` means in the same folder as
* ```../``` means up a level
* ```~/Documents``` will take you to the Documents subfolder of Home

To get from ```~/Documents``` to ```~/Downloads``` you can go up a level and then select Downloads ```../Downloads```

<img src='images_bash/img_007.png' alt='img_007' width='450'/>

The command clear can be used to clear the terminal:

```
clear
```

<img src='images_bash/img_008.png' alt='img_008' width='450'/>

<img src='images_bash/img_009.png' alt='img_009' width='450'/>

The command touch can be used to touch a directory with a file. A ```script.py``` can be created using:

```
touch script.py
```

<img src='images_bash/img_010.png' alt='img_010' width='450'/>

The script file appears in nautilus:

<img src='images_bash/img_011.png' alt='img_011' width='450'/>

A new directory can be created using the command **m**a**k**e **dir**ectory:

```
mkdir 'new folder'
```

Note that single quotations are used to enclose directory or file names with spaces:

<img src='images_bash/img_012.png' alt='img_012' width='450'/>

The new directory ```new folder``` displays in nautilus:

<img src='images_bash/img_013.png' alt='img_013' width='450'/>

The command **l**i**s**t can be used again:

<img src='images_bash/img_014.png' alt='img_014' width='450'/>

The directory ```new folder``` and ```script.py``` display:

<img src='images_bash/img_015.png' alt='img_015' width='450'/>

The script file can be opened in nano, the terminal based text editor using:

```
nano script.py
```

<img src='images_bash/img_016.png' alt='img_016' width='450'/>

Python test code can be added using:

```
print('Hello World!')
```

Press ```Ctrl``` + ```x``` to exit:

<img src='images_bash/img_017.png' alt='img_017' width='450'/>

Press ```y``` in order to save:

<img src='images_bash/img_018.png' alt='img_018' width='450'/>

Press ```↵``` to save overwriting the existing file:

<img src='images_bash/img_019.png' alt='img_019' width='450'/>

nano exits returning to the next prompt in the terminal:

<img src='images_bash/img_020.png' alt='img_020' width='450'/>

Python can be launched using:

```
python
```

and exited using the function:

```
exit()
```

<img src='images_bash/img_021.png' alt='img_021' width='450'/>

If a script file is supplied as an input argument, Python will run the script file:

```
python script.py
```

<img src='images_bash/img_022.png' alt='img_022' width='450'/>

This displays the print statement on the Terminal. Python automatically exits once the script file is complete and the terminal advances to the next prompt:

<img src='images_bash/img_023.png' alt='img_023' width='450'/>

The directory can be removed using ```r```e```m```ove ```dir```ectory and the script file can be removed using ```r```e```m```ove:

```
rmdir 'new folder'
rm script.py
```

<img src='images_bash/img_024.png' alt='img_024' width='450'/>

```l```i```s```t can be used to list the files:

```
ls
```

Note the folder is now empty:

<img src='images_bash/img_025.png' alt='img_025' width='450'/>

<img src='images_bash/img_026.png' alt='img_026' width='450'/>

The command ```clear``` can be used to clear the Terminal:

<img src='images_bash/img_027.png' alt='img_027' width='450'/>

A script file can be created and modified using:

```
touch script.py
nano script.py
```

<img src='images_bash/img_028.png' alt='img_028' width='450'/>

If the Python code is added:

```
import time
time.sleep(5000)
```

Once again press ```Ctrl```+```x``` to exit:

<img src='images_bash/img_029.png' alt='img_029' width='450'/>

Then ```y``` to save:

<img src='images_bash/img_030.png' alt='img_030' width='450'/>

Then ```↵``` to overwrite the file:

<img src='images_bash/img_031.png' alt='img_031' width='450'/>

If this scriptfile is executed using:

```
python script.py
```

It will hang the Terminal for 5000 seconds

<img src='images_bash/img_032.png' alt='img_032' width='450'/>

To cancel press ```Ctrl```+```c```:

<img src='images_bash/img_033.png' alt='img_033' width='450'/>

The shortcut key to copy is ```Ctrl```+```⇧```+```c```:

<img src='images_bash/img_034.png' alt='img_034' width='450'/>

And to paste is ```Ctrl```+```⇧```+```c```:

<img src='images_bash/img_035.png' alt='img_035' width='450'/>

The up ```↑``` and down ```↓``` arrow keys can also be used to access previously used commands in the Terminal:

<img src='images_bash/img_036.png' alt='img_036' width='450'/>

The following commands can be used to launch programs from the ```~\anaconda3\bin``` folder:

|command|command description|
|---|---|
|python|launches python|
|conda|conda package manager|
|anaconda-navigator|launches the Anaconda Navigator|
|idle3|Launches IDLE|
|ipython|launches interactive python|
|jupyter lab|Launches JupyterLab (lab gives the option lab)|
|jupyter|Launches Jupyter Notebook (legacy)|
|spyder|Launches Spyder|
|code|Launches VSCode (if installed)|

For example the command:

```
anaconda-navigator
```

<img src='images_bash/img_037.png' alt='img_037' width='450'/>

Launches the ANaconda Navigator:

<img src='images_bash/img_038.png' alt='img_038' width='450'/>

Note the Terminal is busy while one of these applications is running:

<img src='images_bash/img_039.png' alt='img_039' width='450'/>

[Return to Anaconda Tutorial](./readme.md)