# The Matrix Plotting Library

## Importing the pyplot Module from the Library matplotlib

```matplotlib``` is an abbreviation for the matrix plotting library. For most use cases, the Python Plot module ```pyplot``` is used. The ```pyplot``` module is usually imported from the library ```matplotlib``` using the 3 letter abbreviation ```plt```. This is typically imported subsequent to the Numeric Python library as ```matplotlib``` is part of the ```numpy``` stack and ```ndarrays``` are typically used to store data to plot:

```
import numpy as np
import matplotlib.pyplot as plt
```

![img_001](./images/img_001.png)

## ndarray Recap

The following numpy arrays can be created:

```
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])
```

![img_002](./images/img_002.png)

These can be viewed in the Spyder Variable Explorer:

![img_003](./images/img_003.png)

This array has a single dimension. When viewed in the Variable Explorer it displays as a row. When expanded in the Variable Explorer it displays as a column for convenience:

![img_004](./images/img_004.png)

![img_005](./images/img_005.png)

Most of the plotting functions in ```matplotlib``` that expect data in the form of a 1d array, will also accept a 2d array configured as a column or row respectively.

For the sake of clarity column vectors will be shown:

```
x = np.array([0, 1, 2, 3, 4], ndmin=2).T
y = np.array([0, 1, 4, 9, 16], ndmin=2).T
```

![img_006](./images/img_006.png)

![img_007](./images/img_007.png)

Notice the ```x``` and ```y``` data are the same length, i.e. for every ```x``` value, there is a corresponding ```y``` value:

![img_008](./images/img_008.png)

## Plot Backends

### Magic Commands

JupyterLab uses an Interactive Python (IPython) Console for an interactive notebook and can optionally use an IPython Console for a Python Script. The IPython Console has a number of magic commands which begin with a ```%```. Note magic commands are only available for an IPython Console and are not available for a Python Console.

Details about these can be seen by inputting:

```
%magic
```

![img_009](./images/img_009.png)

This is a long docstring, scrolling down until the ```%matplotlib``` is mentioned:

![img_010](./images/img_010.png)

Gives details about the backends:

![img_011](./images/img_011.png)

### List Backends

For ```matplotlib```, compatible backends can be listed:

```
%matplotlib --list
```

![img_012](./images/img_012.png)

### Inline Backend

The default plot backend is ```inline``` which displays the plot as a static image in the cells output. This can be manually specified using:

```
%matplotlib inline
```

![img_013](./images/img_013.png)

A basic line plot can be created using:

```
plt.plot(x, y)
```

![img_014](./images/img_014.png)

Notice information about the last object is returned in the cell output ```[<matplotlib.lines.Line2D]```. This can be suppressed by use of a semi-colon ```;``` for example:

```
plt.plot(x, y);
```

![img_015](./images/img_015.png)

### qt5 Backend

```qt5``` is a General User Interface (GUI) framework. The plot backend can be changed to ```qt5``` using:

```
%matplotlib qt5
```

![img_016](./images/img_016.png)

A new plot can be created using:

```
plt.plot(x, y)
```

![img_017](./images/img_017.png)

Notice that information about the last object displays in the cell output ```[<matplotlib.lines.Line2D]``` as it was not suppressed using a semi-colon. The plot itself displays in a seperate interactive window. This window has a window title ```Figure 1``` and on windows the three standard minimize, maximize and close buttons. On Linux the windows title bar will match the style of the desktop environment. In GNOME for example, the title bar can be right clicked to reveal these options.

![img_018](./images/img_018.png)

Under the titlebar is a Home, back, forward, pan, zoom, axes options, figure options and save button. The behaviour behind all these buttons under the hood invokes Python code. 

The zoom button can be used to zoom into a region of interest:

![img_019](./images/img_019.png)

![img_020](./images/img_020.png)

The pan tool can be used to reposition the data within the current window size and zoom setting: 

![img_021](./images/img_021.png)

The back and forward button may be used to go back to the previous view or next view:

![img_022](./images/img_022.png)

![img_023](./images/img_023.png)

The home button returns to the default view:

![img_024](./images/img_024.png)

The save button can be used to save an image to .png:

![img_025](./images/img_025.png)

![img_026](./images/img_026.png)

### ipympl Backend

The interactive python matplotlib ```ipympl``` backend is supposed to bridge the two strengths of the other backends; allowing an interactive figure nested in the cell output:

```
%matplotlib ipympl
```

![img_027](./images/img_027.png)

Unfortunately changing to this backend when an Interactive Python Notebook has existing plots that use other backends gives the following warning ```Warning: Cannot change to a different GUI toolkit```. To get around this, the kernel needs to be restarted.

![img_029](./images/img_029.png)

 This plot backend needs to be selected before any plots are created. For this reason the backend is normally changed at the top of the Interactive Python Notebook File after the library imports:

```
import numpy as np
import matplotlib.pyplot as plt

%matplotlib ipympl

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

plt.plot(x, y);
```

![img_028](./images/img_028.png)

### Inline Backend (Spyder IDE)

The Spyder IDE plots inline by default, the plots are static images and are shown in the plots pane:

![img_030](./images/img_030.png)

### qt5 Backend (Spyder IDE)

To change the backend select Tools → Preferences:

![img_031](./images/img_031.png)

Select the IPython Console left tab and then the Graphics top tab. Change the Backend to Qt5 and select Apply:

![img_032](./images/img_032.png)

Select Consoles → Restart Kernel:

![img_033](./images/img_033.png)

Plotting will now show a plot using the qt5 backend in its own window:

![img_034](./images/img_034.png)

### plt.show

Some other IDEs such as VSCode will create plots but not show them. The ```show``` function from the ```pyplot``` module needs to be called to view the plots:

```
plt.show()
```

## Changing a Plot via GUI

Before looking at any code, it is worthwhile exploring the most common changes in the UI to get a feel for the plot. The following plot will be created using the ```qt5``` backend:

```
import numpy as np
import matplotlib.pyplot as plt

%matplotlib qt5

x = np.arange(start=0, stop=101, step=5)
y = x ** 2

plt.plot(x, y);
```

![img_035](./images/img_035.png)

![img_036](./images/img_036.png)

### Labels and LaTeX (MathJax)

In Axes there is a Title, X-Axis Label and Y-Axis Label which are blank by default. 

![img_037](./images/img_037.png)

These can be changed to ```length $x$ vs area $y$```, ```length $x$ (m)``` and ```area $y$ (m$^{2}$)```. Selecting Apply updates the plot to the following:

![img_038](./images/img_038.png)

Enclosing text in ```$ $``` allows a basic subset of inline LaTeX, powered by MathJax which was previously discussed when markdown syntax was examined.

LaTeX Text (MathJax)

|description|LaTeX|output|
|---|---|---|
|math text|```$x$```|$x$|
|normal text|```$\text{x}$```|$\text{x}$|
|bold text|```$\textbf{x}$```|$\textbf{x}$|
|math text with dot|```$\dot{x}$```|$\dot{x}$|
|math text with double dot|```$\ddot{x}$```|$\ddot{x}$|
|math text with triple dot|```$\dddot{x}$```|$\dddot{x}$|
|math text with bar|```$\bar{x}$```|$\bar{x}$|
|math text with hat|```$\hat{x}$```|$\hat{x}$|
|math text with arrow vector|```$\vec{x}$```|$\vec{x}$|
|math text with tilde|```$\tilde{x}$```|$\tilde{x}$|
|math text with wide tilde|```$\widetilde{xx}$```|$\widetilde{xx}$|
|math text with check|```$\check{x}$```|$\check{x}$|
|math text with acute|```$\acute{x}$```|$\acute{x}$|
|math text with grave|```$\grave{x}$```|$\grave{x}$|
|math text with breve|```$\breve{x}$```|$\breve{x}$|
|subscript|```$x_{2}$```|$x_{2}$|
|superscript|```$x^{3}$```|$x^{3}$|
|subscript and superscript|```$x_{2}^{3}$```|$x_{2}^{3}$|
|square root|```$\sqrt{x}$```|$\sqrt{x}$|
|sin|```$\sin{x}$```|$\sin{x}$|
|cos|```$\cos{x}$```|$\cos{x}$|
|tan|```$\tan{x}$```|$\tan{x}$|
|log|```$\log{x}$```|$\log{x}$|
|exp|```$\exp{x}$```|$\exp{x}$|

LaTeX Mathematical Symbols (MathJax)

|description|LaTeX|output|
|---|---|---|
|equal to|```$=$```|$=$|
|equivalent to|```$\equiv$```|$\equiv$|
|not equal to|```$\ne$```|$\ne$|
|similar to|```$\sim$```|$\sim$|
|approximate to|```$\approx$```|$\approx$|
|tilde|```$\textasciitilde$```|$\textasciitilde$|
|approximately equal to|```$\cong$```|$\cong$|
|plus|```$+$```|$+$|
|minus|```$-$```|$-$|
|plus minus|```$\pm$```|$\pm$|
|minus plus|```$\mp$```|$\mp$|
|dash|```$\text{-}$```|$\text{-}$|
|circumflex|```$\textasciicircum$```|$\textasciicircum$|
|asterisk|```$\ast$```|$\ast$|
|star|```$\text{\*}$```|$\text{\*}$|
|times|```$\times$```|$\times$|
|centre dot|```$\cdot$```|$\cdot$|
|period|```$.$```|$.$|
|bullet|```$\bullet$```|$\bullet$|
|colon|```$\colon$```|$\colon$|
|centre dots|```$\cdots$```|$\cdots$|
|vertical dots|```$\vdots$```|$\vdots$|
|therefore|```$\therefore$```|$\therefore$|
|division slash|```$/$```|$/$|
|division sign|```$\div$```|$\div$|
|less than|```$<$```|$<$|
|less than or equal to|```$\leq$```|$\leq$|
|greater than|```$>$```|$>$|
|greater than or equal to|```$\geq$```|$\geq$|
|factorial|```$!$```|$!$|
|degree|```$\degree$```|$\degree$|
|infinity|```$\infty$```|$\infty$|
|proportional to|```$\propto$```|$\propto$|
|partial|```$\partial$```|$\partial$|
|hbar|```$\hbar$```|$\hbar$|
|union|```$\cup$```|$\cup$|
|intersection|```$\cap$```|$\cap$|
|emptyset|```$\emptyset$```|$\emptyset$|
|exists|```$\exists$```|$\exists$|
|in|```$\in$```|$\in$|
|not in|```$\notin$```|$\notin$|
|ni|```$\ni$```|$\ni$|
|left arrow|```$\leftarrow$```|$\leftarrow$|
|right arrow|```$\rightarrow$```|$\rightarrow$|
|left right arrow|```$\leftrightarrow$```|$\leftrightarrow$|
|up arrow|```$\uparrow$```|$\uparrow$|
|down arrow|```$\uparrow$```|$\downarrow$|
|up down arrow|```$\updownarrow$```|$\updownarrow$|

LaTeX Greek Letters (MathJax)

|description|LaTeX|output|
|---|---|---|
|alpha|```$\alpha$```|$\alpha$|
|beta|```$\beta$```|$\beta$|
|Gamma|```$\Gamma$```|$\Gamma$|
|gamma|```$\gamma$```|$\gamma$|
|Delta|```$\Delta$```|$\Delta$|
|delta|```$\delta$```|$\delta$|
|nabla|```$\nabla$```|$\nabla$|
|epsilon|```$\epsilon$```|$\epsilon$|
|epsilon|```$\varepsilon$```|$\varepsilon$|
|zeta|```$\zeta$```|$\zeta$|
|eta|```$\eta$```|$\eta$|
|kappa|```$\kappa$```|$\kappa$|
|Lambda|```$\Lamba$```|$\Lambda$|
|mu|```$\mu$```|$\mu$|
|Xi|```$\Xi$```|$\Xi$|
|xi|```$\xi$```|$\xi$|
|Pi|```$\Pi$```|$\Pi$|
|pi|```$\pi$```|$\pi$|
|rho|```$\rho$```|$\rho$|
|Sigma|```$\Sigma$```|$\Sigma$|
|sigma|```$\sigma$```|$\sigma$|
|sigma|```$\varsigma$```|$\varsigma$|
|tau|```$\tau$```|$\tau$|
|Upsilon|```$\Upsilon$```|$\Upsilon$|
|upsilon|```$\upsilon$```|$\upsilon$|
|Phi|```$\Phi$```|$\Phi$|
|phi|```$\phi$```|$\phi$|
|chi|```$\chi$```|$\chi$|
|Psi|```$\Psi$```|$\Psi$|
|psi|```$\psi$```|$\psi$|
|Omega|```$\Omega$```|$\Omega$|
|omega|```$\omega$```|$\omega$|

Note the Greek letters A, B, E, Z, H, I, i, K, M, N, O, o and P that are the same as Latin letters are therefore just represented using the Latin letters.

LaTeX Fractions (MathJax)

|description|LaTeX|output|
|---|---|---|
|inline fraction|```$\frac{a}{b}$```|$\frac{a}{b}$|

LaTeX Brackets (MathJax)

|description|LaTeX|output|
|---|---|---|
|inline fraction parenthesis|```$(\frac{a}{b})$```|$(\frac{a}{b})$|
|inline fraction square|```$[\frac{a}{b}]$```|$[\frac{a}{b}]$|
|inline fraction braces|```$\lbrace\frac{a}{b}\rbrace$```|$\lbrace\frac{a}{b} \rbrace$|

Prefixing ```\left``` and ```\right``` to a set of brackets will automatically resize the brackets.

The ```{``` and ```}``` are reserved so ```\lbrace``` and ```\rbrace``` need to be used.

The figure typically assigns limited space for labels and normally simple inline expressions such as the above are used.

Enclosing text in ```$$ $$``` is used for display LaTeX. I a figure however display equations show as inline equations i.e. there seems to be no difference enclosing in single ```$ $``` or double ```$$ $$```.

Some more complicated mathematical expressions can be added. In my personal testing, I couldn't get a matrix or column vector to properly display, this seems to be an issue with MathJax rendering as previously discussed when looking at markdown.

Large equations will typically be cut off at the bottom of the figure by default.

### Axes Scales




Selecting the Axes options, the Tight Layout button can be pressed:



Going back to Figure Options the X-Axis Min and X-Axis Max values can be altered, these are automatically selected from the limits ofthe x data but can be changed to ```-2``` and ```6```respectively:




















In JupyterLab a warning sometimes displays when attempting to change backend.



For this reason the backend is normally changed at the top of the Interactive Python Notebook File after the library imports:

```
import numpy as np
import matplotlib.pyplot as plt

%matplotlib qt5

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])

plt.plot(x, y);
```


In JupyterLab the default backend is inline, which 


## Functional Programming Overview

The ```pyplot``` module is imported from the ```matplotlib``` library using:

```
import matplotlib.pyplot as plt
```



The docstring of the ```pyplot``` module can be viewed by using ```?``` on its alias ```plt```:

```
? plt
```



T





















The identifiers from the ```pyplot``` module can be viewed by inputting its alias ```plt.``` followed by a tab ```↹```:



|function|description|
|---|---|
|figure|Create a new figure, or activate an existing figure.|
|axes|Add an axes to the current figure and make it the current axes.|
|plot|Plot y versus x as lines and/or markers.|
|xlabel|Set the label for the x-axis.|
|ylabel|Set the label for the y-axis.|
|title|Set a title for the Axes.|
|legend|Place a legend on the Axes.|
|grid|Configure the grid lines.|
|minorticks_on|Display minor ticks on the Axes.|
|minorticks_off|Remove minor ticks from the Axes.|
|xlim|Get or set the x limits of the current axes.|
|ylim|Get or set the y-limits of the current axes.|
|xscale|Set the x-axis scale.|
|yscale|Set the y-axis scale.|
|xticks|Get or set the current tick locations and labels of the x-axis.|
|yticks|Get or set the current tick locations and labels of the y-axis.|
|tight_layout|Adjust the padding between and around subplots.|
|subplot|Add an Axes to the current figure or retrieve an existing Axes.|






grid	Configure the grid lines.
minorticks_on	Display minor ticks on the Axes.
minorticks_off	Remove minor ticks from the Axes.
xlim	Get or set the x limits of the current axes.
ylim	Get or set the y-limits of the current axes.
xscale	Set the x-axis scale.
yscale	Set the y-axis scale.
xticks	Get or set the current tick locations and labels of the x-axis.
yticks	Get or set the current tick locations and labels of the y-axis.
tight_layout	Adjust the padding between and around subplots.
subplot	Add an Axes to the current figure or retrieve an existing Axes.
















plt.get_plot_commands()

list(plt.get_plot_commands())


The ```plt.plotting``` function is essentially a documentation string outlining the most commonly used plotting functions of the ```pyplot``` module.






```
fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```




ax.yaxis.set_tick_params(labelsize=30, labelcolor='red',
                         direction='out', which='major')
ax.yaxis.get_tick_params(which='major')



    ax.set_aspect(aspects[i], adjustable='datalim')
aspects = ('auto', 'equal', 'equalxy', 'equalyz', 'equalxz')



fig.colorbar(im, cax=ax.inset_axes([0, 1.05, 1, 0.05]),
             location='top')





fig, axd = plt.subplot_mosaic(
    "AB;CD",
    per_subplot_kw={
        "A": {"projection": "polar"},
        ("C", "D"): {"xscale": "log"},
        "B": {"projection": "3d"},
    },
)

