## Viewing Notebook Files

### GitHub

These markdown and notebook files are stored on GitHub. When a markdown file or notebook file is opened in GitHub, the markdown preview should show in the browser. However GitHub has limitations...

* Unfortunately GitHub is case sensitive to the file extension of an image file .png vs .PNG and images may not render correctly unless the correct file extension is used.Lowercase .png is used for each in this GitHub repository.
* On markdown files or notebooks with lots of images, the browser may time out and not render the image correctly.
* Only part of a large notebooks, may display.
* Scrolling cell outputs display as non-scrolling outputs. These notebooks often look up docstrings for a reference and use the scrolling output to take the emphasis away from the docstring. Unfortunately when the cell output is set to scrolling this is ignored by GitHub and the output of a docstring for example therefore takes more of an emphasis than it does nested as a code block.

![img_035](./images/img_035.png)

### NBViewer

nbviewer should be used:

```html
https://nbviewer.org/
```

![img_037](./images/img_037.png)

Copy and paste the URL of a Notebook File into the search box. For example:

```html
https://github.com/PhilipYip1988/python-notebooks/blob/main/plotly_library/notebook.ipynb
```

![img_038](./images/img_038.png)

nbviewer should display the notebook properly in the browser, addressing ,ost of the issues mentioned above opening the notebook using GitHub.com directly however scrolling cell outputs display as non-scrolling outputs:

![img_039](./images/img_039.png)

## Downloading and Running Notebook Files

It is recommended to download the repository using GitHub Desktop as seen in the previous tutorial.

Alternatively to download via the browser, select Code and then Download Zip:

![img_001](./images/img_001.png)

Note you may not see the Download button if viewing a subfolder and need to go on the root page. [Python Notebooks Root](https://github.com/PhilipYip1988/python-notebooks)

### JupyterLab

In JupyterLab, select the ```readme.md``` file in the root directory:

![img_002](./images/img_002.png)

Right click it and select show markdown preview:

![img_003](./images/img_003.png)

The markdown preview opened to the side. The table of contents can be opened to the left. Unfortunately the links on the table of contents will only navigate to a position on the currently selected window and the markdown editor and markdown preview tab are not linked. This makes it a bit cumbersome to modify a markdown file and view the output side by side:

![img_004](./images/img_004.png)

If the markdown file is closed and only the markdown preview is open, a link to a notebook file can be selected:

![img_005](./images/img_005.png)

The notebook file will open:

![img_006](./images/img_006.png)

Select Kernel and Restart Kernel and Clear Outputs of All Cells:

![img_007](./images/img_007.png)

Select Restart:

![img_008](./images/img_008.png)

Highlight a cell and select the Run button or press ```Ctrl``` + ```⇧``` to run the cell:

![img_009](./images/img_009.png)

The ipython prompt beside the cell will display:

![img_010](./images/img_010.png)

Alternatively Restart Kernel and Restart All Cells can be selected:

![img_011](./images/img_011.png)

Select Restart:

![img_012](./images/img_012.png)

JupyterLab has improvements in the way it renders large notebooks and will take a moment to execute all the code:

![img_013](./images/img_013.png)

The notebook renders as expected:

![img_014](./images/img_014.png)

A cells output can be changed by right clicking it and selecting Enable Scrolling for all Outputs:

![img_015](./images/img_015.png)

This setting is maintained after the kernel is restarted.

### VSCode

In VSCode open the root folder as a project and select the ```readme.md``` file in the root directory:

![img_016](./images/img_016.png)

Right click the markdown file and select Open Preview:

![img_017](./images/img_017.png)

The table of contents can be used in the markdown file. The markdown editor and preview are linked which makes it easier to edit the markdown file and view the output:

![img_018](./images/img_018.png)

If the markdown file is closed and only the markdown preview is open, a link to a notebook file can be selected:

![img_019](./images/img_019.png)

This opens the notebook file. In VSCode, the kernel needs to be selected:

![img_020](./images/img_020.png)

Select Python Environments:

![img_021](./images/img_021.png)

Select the Anaconda (base) Python environment or custom (vscode-env) Python environment:

![img_022](./images/img_022.png)

Select Clear All Outputs:

![img_023](./images/img_023.png)

The Cell Outputs will be cleared:

![img_024](./images/img_024.png)

Highlight a cell and select the Run button or press ```Ctrl``` + ```⇧``` to run the cell:

![img_025](./images/img_025.png)

The ipython prompt beside the cell will display:

![img_026](./images/img_026.png)

VSCode uses an older protocol to render notebooks and has issues running large notebooks:

![img_027](./images/img_027.png)

It will take a very long time to run a notebook and the warning ```The Window is not responding``` displays:

![img_028](./images/img_028.png)

VSCode does not remember the cell output setting and all the cells will revert to a truncated output by default. For long docstrings, this can be changed to a scrolling output.

[Return to Python Tutorials](../readme.md)