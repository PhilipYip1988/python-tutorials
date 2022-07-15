# Interactive Python Notebook File

The **I**nteractive **Py**thon **N**ote**b**ook file with the extension ```.ipynb``` consists of a series of cells. Each cell can be designated as a markdown cell, using the same syntax as a markdown file or a code cell which can be used to execute Python code.

In this set of tutorials the JupyterLab IDE will be used.

The following markdown cell:

![001_markdown_cell](./images/001_markdown_cell.PNG)

When run, shows an output similar to the markdown preview of a markdown file:

![002_markdown_cell](./images/002_markdown_cell.PNG)

When a code cell is run:

![003_code_cell](./images/003_code_cell.PNG)

The code is executed and any output is shown below the cell. Once a code cell is run, a number displays to the left indicating the order the code cell was run. In this case ```1```:

![004_code_cell](./images/004_code_cell.PNG)

If another code block is run, it will display ```2```:

![005_code_cell](./images/005_code_cell.PNG)

A highlighted code cell may be switched to markdown using the ```Esc``` and ```m``` keyboard shortcut. A highlighted markdown cell my be switched to a code cell using the ```Esc``` and ```y``` keyboard shortcut.

The shortcut key shift ```⇧``` and enter ```↵``` can be used to run a currently selected cell:

![006_code_cell](./images/006_code_cell.PNG)

If a code cell that has previously been run is reselected and run again. It will only display a single number, indicating the order at the last time the cell was run, in this case the number is now ```3```: 

![007_code_cell](./images/007_code_cell.PNG)

The shortcut key alt ```alt``` and enter ```↵``` can be used to run a currently selected cell and insert an empty cell below it:

![008_code_cell](./images/008_code_cell.PNG)

Notice that the number of the cell is now ```4``` and there is a blank cell below:

![009_code_cell](./images/009_code_cell.PNG)

A docstring of a function or class can be displayed as a popup balloon by typing in the function name followed by open parenthesis and using the shortcut key shift ```⇧``` and tab ``` ↹``` for example the ```print``` function:

![010_docstring](./images/010_docstring.PNG)

We can also output the full docstring to a cell by using ```?``` before the fubnction or class. In the case, we should only use the function or class name to reference the function or class and not include any parenthesis following the function to call it. For example we can have a look at the ```print``` function using:

```
? print
```

![011_docstring](./images/011_docstring.PNG)

We see the docstring as the cell output:

![012_docstring](./images/012_docstring.PNG)

For long docstrings or long outputs ineneral, we can right click the output cell and select Enable Scrolling for outputs:

![013_docstring_scrolling](./images/013_docstring_scrolling.PNG)

This allows us to quickly view the docstring without it being the main focus of the interactive notebook file:

![014_docstring_scrolling](./images/014_docstring_scrolling.PNG)

Python objects (instances of classes) may have a number of other objects (classes, instances, attributes and modules) that can be called from them. Let's use the example of the inbuilt ```datatime``` module. Let's import it using the alias ```dt```:

```
import datetime as dt
```

![015_modules](./images/015_modules.PNG)

Now if we type in the name of the object, in this case the alias ```dt``` followed by a dot ```.``` and ```↹``` we see a list of objects:

![016_modules](./images/016_modules.PNG)

In this case we see the class ```datetime``` and we can once again have a look at it's docstring using the shortcut key shift ```⇧``` and tab ```↹```:

![017_modules](./images/017_modules.PNG)

When opening a notebook created by someone else, sometimes you may want to restart the kernel. To do this select the Kernel tab and then select Restart Kernel and Clear All Outputs... or one of the other options:

![018_kernel](./images/018_kernel.PNG)

Select Restart:

![019_kernel](./images/019_kernel.PNG)

Now all the Cell outputs are blank and there is no number beside any of the cells, indicatingthat none of the cells are ran:

![020_kernel](./images/020_kernel.PNG)

An example notebook file can be opened in JupyterLab:

[Example Notebook File](./001_example_notebook_file.ipynb)
