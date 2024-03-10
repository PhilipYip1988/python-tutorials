# GitHub Desktop

## Installation

### Windows Installation

To install GitHub Desktop on Windows use:

```powershell
winget install GitHub.GitHubDesktop
```

### Ubuntu Installation

To install GitHub Desktop on Ubuntu use the @shiftkey package needs to be added:

```bash
wget -qO - https://apt.packages.shiftkey.dev/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/shiftkey-packages.gpg > /dev/null
```

```bash
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/shiftkey-packages.gpg] https://apt.packages.shiftkey.dev/ubuntu/ any main" > /etc/apt/sources.list.d/shiftkey-packages.list'
```

Then GitHub Desktop can be installed:

```bash
sudo apt update && sudo apt install github-desktop
```

Installation instructions taken from the [ShiftKey Repository](https://github.com/shiftkey/desktop?tab=readme-ov-file)

## Cloning a Repository

Once GitHub is installed, launch it using its icon from the start menu:

<img src='images/img_001.png' alt='img_001' width='450'/>

Select sign in to GitHub.com:

<img src='images/img_002.png' alt='img_002' width='450'/>

This will take you to the GitHub website where you can sign in to your GitHub account:

<img src='images/img_003.png' alt='img_003' width='450'/>

Select open xdg-open:

<img src='images/img_004.png' alt='img_004' width='450'/>

Select use my GitHub account name and email address and select Finish:

<img src='images/img_005.png' alt='img_005' width='450'/>

Select Clone a Repository from the Internet:

<img src='images/img_006.png' alt='img_006' width='450'/>

If you have personal repositories they will be listed under the GitHub.com tab:

<img src='images/img_007.png' alt='img_007' width='450'/>

Alternatively select URL and then paste in the URL:

```html
https://github.com/PhilipYip1988/python-notebooks 
```

This will download the repository to a local path within ```Documents/GitHub```. Select Clone:

<img src='images/img_008.png' alt='img_008' width='450'/>

This will download all the files to the local folder:

<img src='images/img_009.png' alt='img_009' width='450'/>

The GitHub Desktop will list any changes you made to the repository:

<img src='images/img_010.png' alt='img_010' width='450'/>

The GitHub repository is in ```Documents``` or ```OneDrive/Documents```:

<img src='images/img_011.png' alt='img_011' width='450'/>

Then the GitHub subfolder:

<img src='images/img_012.png' alt='img_012' width='450'/>

Then the name of the repository:

<img src='images/img_013.png' alt='img_013' width='450'/>

## Forking a Repository

The readme.md file is normally opened in JupyterLab or VSCode however for this example it can be opened in text editor:

<img src='images/img_014.png' alt='img_014' width='450'/>

If a change is made and saved:

<img src='images/img_015.png' alt='img_015' width='450'/>
<img src='images/img_016.png' alt='img_016' width='450'/>

The GitHub Desktop will list the changes made. Since this is not your repository, you cannot Commit to Main. However you can create your own fork:

<img src='images/img_017.png' alt='img_017' width='450'/>

Select fork this repository:

<img src='images/img_018.png' alt='img_018' width='450'/>

Select for my own purposes:

<img src='images/img_019.png' alt='img_019' width='450'/>

Now give details about the update made and select Commit to Main:

<img src='images/img_020.png' alt='img_020' width='450'/>

Select Push Origin:

<img src='images/img_021.png' alt='img_021' width='450'/>

The changes will be made to your forked version of the repository:

<img src='images/img_022.png' alt='img_022' width='450'/>

This will show under your profile:

<img src='images/img_023.png' alt='img_023' width='450'/>

When working with a GitHub repository on multiple computers A and B. If you make changes to the repository on A, you will be able to push changes to the repository on A and then pull changes from the repository on B using GitHub Desktop.

[Return to Python Tutorials](../readme.md)