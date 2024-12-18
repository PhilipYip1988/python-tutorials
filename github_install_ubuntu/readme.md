# Viewing Markdown Files

## Downloading and Installing GitHub Desktop

Instructions to install GitHub Desktop on Ubuntu are given on the [GitHub Gist Page GitHub Desktop](https://gist.github.com/berkorbay/6feda478a00b0432d13f1fc0a50467f1). The How to Install link on this page, will give commands for other distributions such as Fedora. For Mac, the installer listed on the [GitHub Desktop Download Page](https://desktop.github.com/download/) should be used.

For the Ubuntu install, the first command adds an apt repository:

<img src='./images/img_001.png' alt='img_001' width='600'/>

Copy and paste it into the terminal:

<img src='./images/img_002.png' alt='img_002' width='600'/>

As the command is prefixed with `sudo`, super user do, authentication is required, input your user account password to proceed:

<img src='./images/img_003.png' alt='img_003' width='600'/>

For the Ubuntu install, the second command updates apt so it refreshes its repositories and installs GitHub Desktop:

<img src='./images/img_004.png' alt='img_004' width='600'/>

Copy and paste it into the terminal:

<img src='./images/img_005.png' alt='img_005' width='600'/>

GitHub Desktop is now installed:

<img src='./images/img_006.png' alt='img_006' width='600'/>

And is available on the Start Screen:

<img src='./images/img_007.png' alt='img_007' width='600'/>

Select Sign In to GitHub.com:

<img src='./images/img_008.png' alt='img_008' width='600'/>

Log in on the web browser:

<img src='./images/img_009.png' alt='img_009' width='600'/>

Select Continue:

<img src='./images/img_010.png' alt='img_010' width='600'/>

Select Authorise Desktop:

<img src='./images/img_011.png' alt='img_011' width='600'/>

Check, always allow links and select Open Link: 

<img src='./images/img_012.png' alt='img_012' width='600'/>

Select Finish:

<img src='./images/img_013.png' alt='img_013' width='600'/>

You will now be logged in:

<img src='./images/img_014.png' alt='img_014' width='600'/>

## Cloning Repository

Select File → Clone Repository:

<img src='./images/img_015.png' alt='img_015' width='600'/>

Select URL and paste:

```
https://github.com/PhilipYip1988/python-tutorials
```

Select Clone:

<img src='./images/img_016.png' alt='img_016' width='600'/>

Once cloned, the repository will show:

<img src='./images/img_017.png' alt='img_017' width='600'/>

It is saved within `Documents`, `GitHub`:

<img src='./images/img_018.png' alt='img_018' width='600'/>

<img src='./images/img_019.png' alt='img_019' width='600'/>

The `readme.md` displays:

<img src='./images/img_020.png' alt='img_020' width='600'/>

## Downloading and Installing VSCode

To view the formatted markdown, VSCode should be installed. VSCode is a general purpose code editor and has native markdown support. Open up Ubuntu Software and search for VSCode. Select Code:

<img src='./images/img_021.png' alt='img_021' width='600'/>

Select Install:

<img src='./images/img_022.png' alt='img_022' width='600'/>

Installation requires use of a super and an authentication prompt will display. Insert your user password and select Authenticate:

<img src='./images/img_023.png' alt='img_023' width='600'/>

VSCode is now installed and there is a Start Menu shortcut. Select Open:

<img src='./images/img_024.png' alt='img_024' width='600'/>

## Viewing Markdown Files

VSCode will launch, select File → Open Folder:

<img src='./images/img_025.png' alt='img_025' width='600'/>

<img src='./images/img_026.png' alt='img_026' width='600'/>

<img src='./images/img_027.png' alt='img_027' width='600'/>

<img src='./images/img_028.png' alt='img_028' width='600'/>

Select yes I Trust the Authors:

<img src='./images/img_029.png' alt='img_029' width='600'/>

Right click the `readme.md` file and select Open Preview:

<img src='./images/img_030.png' alt='img_030' width='600'/>

unfortunately the outline which displays the table of contents only displays for the raw file these can eb viewed side by side:

<img src='./images/img_031.png' alt='img_031' width='600'/>

The file tab can be collapsed and the raw file tab closed, allowing more screen space for the content:

<img src='./images/img_032.png' alt='img_032' width='600'/>

It is recommended to read these tutorials using two screens. On one screen launch the Spyder IDE and on the other screen, use VSCode for the markdown preview.

Note it is possible to code with Python in VSCode but this requires installation of extensions and setup of a Python environment.

[Return to Python Tutorials](../readme.md)