# Uninstall

For best results Anaconda should be installed on a clean computer without any previous Python or Python Distributions. 

## Uninstall

To Uninstall, right click the Start Button and select Installed Apps:

<img src='images_uninstall/img_001.png' alt='img_001' width='150'/>

Uninstall:

* Anaconda
* Miniconda
* Miniforge
* Mambaforge
* Python
* PyCharm
* Spyder
* Thonny
* VSCode
  
if present. 

<img src='images_uninstall/img_002.png' alt='img_002' width='450'/>

To uninstall an Anaconda based installer right click the options ... beside it and select uninstall:

<img src='images_uninstall/img_003.png' alt='img_003' width='350'/>

Select Uninstall:

<img src='images_uninstall/img_004.png' alt='img_004' width='350'/>

Select yes:

<img src='images_uninstall/img_005.png' alt='img_005' width='300'/>

Select next:

<img src='images_uninstall/img_006.png' alt='img_006' width='350'/>

Select Finish:

<img src='images_uninstall/img_007.png' alt='img_007' width='350'/>

## Windows Environmental Variables Path

Right click the Start button and select System:

<img src='images_uninstall/img_008.png' alt='img_008' width='150'/>

Select Advanced system Settings:

<img src='images_uninstall/img_009.png' alt='img_009' width='350'/>

Select Environmental Variables:

<img src='images_uninstall/img_010.png' alt='img_010' width='350'/>

Then select Path and Edit:

<img src='images_uninstall/img_011.png' alt='img_011' width='350'/>

The default path looks like the following:

<img src='images_uninstall/img_012.png' alt='img_012' width='350'/>

A semicolon can be added at the end:

<img src='images_uninstall/img_013.png' alt='img_013' width='350'/>

Once OK is selected and Edit is pressed again, it should display as a list:

<img src='images_uninstall/img_014.png' alt='img_014' width='350'/>

Remove any entries that contain Python, Anaconda, Miniconda, Miniforge or Mambaforge.

## Purging Configuration Files

The default locations for Anaconda installers are in ```%USERPROFILE%``` if installed as a single user (default) or ```%PROGRAMDATA%``` if installed for all users.

Anaconda is typically installed for a single user in:

```
%USERPROFILE%
```

For all users it is installed in:

```
%PROGRAMDATA%
```

Open the locations in Windows Explorer:

<img src='images_uninstall/img_015.png' alt='img_015' width='350'/>

Delete the folders:

* .conda
* .continuum
* .idlerc
* .ipython
* .jupyter
* .matplotlib
* .spyder-py3
* .vscode
* anaconda3
* miniconda3
* miniforge
* mambaforge

And the file:

* .condarc

<img src='images_uninstall/img_016.png' alt='img_016' width='350'/>

Open up File Explorer. In the addressbar type in:

```
%APPDATA%
```

<img src='images_uninstall/img_017.png' alt='img_017' width='350'/>


Delete the folders:

* .anaconda
* Code
* JetBrains
* jupyter
* Thonny

<img src='images_uninstall/img_018.png' alt='img_018' width='350'/>

Open up File Explorer. In the addressbar type in:

```
%LOCALAPPDATA%
```

<img src='images_uninstall/img_019.png' alt='img_019' width='350'/>

Delete the folders:

* conda
* Jedi
* pip
* scikit-image
* Spyder
* thonny

<img src='images_uninstall/img_020.png' alt='img_020' width='350'/>

Start Menu shortcuts for a single user are found in:

```
%APPDATA%\Microsoft\Windows\Start Menu\Programs
```

For all users:

```
%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs
```

Open the locations in Windows Explorer:

<img src='images_uninstall/img_021.png' alt='img_021' width='350'/>

Delete any Anaconda3 folders and names of old Python Environments:

<img src='images_uninstall/img_022.png' alt='img_022' width='350'/>

[Return to Python Tutorials](../../readme.md)