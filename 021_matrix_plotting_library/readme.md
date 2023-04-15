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

For more complicated plots, sometimes data is required that has $x$ in the form as a row, $y$ in the form as a column and $z$ in the form of a matrix with the same number of columns as $x$ and the same number of rows as $y$:

```
xrow = np.array([5, 6, 7, 8, 9])[np.newaxis, :]
ycol = np.array([1, 2, 3, 4])[:, np.newaxis]
zmat = np.array([[0, 1, 1, 1, 0],
                 [1, 2, 3, 2, 1],
                 [1, 2, 3, 2, 1],
                 [0, 1, 1, 1, 0]])
```

![img_205](./images/img_205.png)

![img_206](./images/img_206.png)

![img_207](./images/img_207.png)

Recall that the dimension of $x$ can be expanded by those of $y$ and the dimension of $y$ can be expanded by those of $x$ using the ```numpy``` function ```meshgrid``` giving matrices which have the same dimensions as $z$:

```
xmat, ymat = np.meshgrid(xrow, ycol)
```

![img_208](./images/img_208.png)

![img_209](./images/img_209.png)

![img_210](./images/img_210.png)

![img_211](./images/img_211.png)

![img_212](./images/img_212.png)

Example data often uses linearly spaced $x$ and $y$ data and a ```lambda``` expression with a mathematical function to determine $z$:

```
xrow = np.linspace(-2, 2, 10)[np.newaxis, :]
ycol = np.linspace(-2, 2, 10)[:, np.newaxis]
xmat, ymat = np.meshgrid(xrow, ycol)
zdata_fun = lambda x, y: x * np.exp(-x**2 - y**2)
zmat = zdata_fun(x=xrow, y=ycol)
```

![img_213](./images/img_213.png)

![img_214](./images/img_214.png)

![img_215](./images/img_215.png)

Sometimes the $x$, $y$ and $z$ are also required to be equally sized 1d ```ndarray```. To achieve this the arrays can be collapsed using the ```ndarray``` method ```flatten```:

```
xarray = xmat.flatten()
yarray = ymat.flatten()
zarray = zmat.flatten()
```

![img_216](./images/img_216.png)

![img_217](./images/img_217.png)

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

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

plt.plot(x, y);
```

![img_035](./images/img_035.png)

![img_036](./images/img_036.png)

### Labels and LaTeX (MathJax)

In the Axes Tab of Figure Options there is a Title (```title```), X-Axis Label (```xlabel```) and Y-Axis Label (```ylabel```) which are blank by default. 

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

The ```{``` and ```}``` are reserved so ```\lbrace``` and ```\rbrace``` need to be used.

In markdown enclosing text in ```$$ $$``` is used for display equations, this does not seem to be supported for the xlabel, ylabel or title. In my testing more complicated mathematical expressions such as vectors and matrices do not render. 

The figure typically assigns limited space for labels and normally simple inline expressions such as the above are used.

### Axes Scales

The x-axis min (xmin) and x-axis max (xmax) can be set to ```-1``` and ```5```, alongside the x-axis scale (xscale) which is linear by default. The y-axis min (ymin) and y-axis max (ymax) can be set to ```1``` and ```1000```, alongside the y-axis scale (yscale) to logarithimic (log).

![img_039](./images/img_039.png)

### Labels

In curves there is a dropdown menu of labels. By default each line is called ```_childN``` where ```N``` is an integer corresponding to the index indicating the order that the lines were plotted. In this case there is only index 0. 

![img_040](./images/img_040.png)

The individual label (```label```) can be assigned to a value for example ```area```.

### Line Properties

The Line Style (```linestyle``` or ```ls```) has a default value of Solid (```'solid'``` or ```'-'```), but can also be changed to Dotted (```'dotted'``` or ```':'```), Dashed (```'dashed'``` or ```'--'```) or Dashdot (```'dashdot'``` or ```'-.'```). In this case it will be changed to Dashed.

The Line Width (```linewidth``` or ```lw```) has a default floating point number value of ```1.5```. It can be changed to ```2.0```.

The Draw Style (```drawstyle``` or ```ds```) has a default value of default (```'default'```). It can be changed to Steps (Pre) (```'steps-pre'```), Steps (Mid) (```'steps-mid'```) or Steps (Post) (```'steps-post'```). This will be left at default.

### Color HTML Format

The Color (```color```) U.S. spelling exclusive of the u, is usually in the form #rrggbb (```'#rrggbb'```). 

![img_041](./images/img_041.png)

Physiologically, the human eye has red sensitive, green sensitive and blue sensitive receptors. The brain maps a color to the intensity ratio picked up by these three sensor types. In a screen each pixel consists of a red LED, green LED and blue LED (RGB LED). Each color in the RGB LED has 8 bit levels used to adjust the intensity ratio to create what the brain perceives as a color.

In the example above a color is selected from one of the options in the left. 

This color is shown in the Hue Saturation Value (HSV) plot to the right. This HSV plot is designed so visually it is easiest to select a color. In the HSV plot the Hue (decreases right along x) and Saturation (increases down along y). The Value is left constant as the cursor moves, however it can be increased using the associated Value box. 

The Red, Green and Blue (RGB) values are shown to the right. These are 8 bit values ranging from 0-255 (decimal). The 85, 170 and 127 (decimal) correspond to the 55, aa and 7f (hexadecimal). The HTML #55aa7f is the color selected.

The alpha channel also ranges from 0-255 (decimal) or 0-ff (hexadecimal) and corresponds to an overall brightness. In this case full brightness is selected giving a HTML of #55aa7fff.

This HTML value is as the name suggest quite commonly used with HTML, so many websites have color pickers that use a similar form, paint application such as Microsoft Paint and Office Programs such as Word, Excel and PowerPoint all exhibit similar color pickers.

![img_042](./images/img_042.png)

### Marker

Changing the Line Style to Dotted and the Draw Style to Steps (Pre) looks like the following:

![img_043](./images/img_043.png)

A plot also known as a lineplot, does not display markers by default. A Marker (```marker```) can be selected from the dropdown menu:

![img_044](./images/img_044.png)

|Marker Description|String|Integer or None|
|---|---|---|
|nothing|```''```|```None```|
|point|```'.'```||
|pixel|```','```||
|circle|```'o'```||
|triangle_down|```'v'```||
|triangle_up|```'^'```||
|triangle_left|```'<'```||
|triangle_right|```'>'```||
|tri_down|```'1'```||
|tri_up|```'2'```||
|tri_left|```'3'```||
|tri_right|```'4'```||
|octagon|```'8'```||
|square|```'s'```||
|pentagon|```'p'```||
|plus_filled|```'P'```||
|star|```'*'```||
|hexagon1|```'h'```||
|hexagon2|```'H'```||
|plus|```'+'```||
|x|```'x'```||
|X|```'X'```||
|vline|```'\|'```||
|hline|```'_'```||
|tickleft||```0```|
|tickright||```1```|
|caretleft||```2```|
|caretright||```3```|
|caretup||```4```|
|caretdown||```5```|
|caretleftbase||```6```|
|caretrightbase||```7```|
|caretupbase||```8```|
|caretdownbase||```9```|

The Marker Size (```markersize``` or ```ms```) can be changed from the default floating point value of ```6.0``` to ```15.0```.

The Marker Face Color (```markerfacecolor``` or ```mfc```) and Marker Edge Color (```markeredgecolor``` or ```mec```) can be selected. These take in the form ```#rrggbbaa``` as discussed previously and have a color selection. This can be updated to ```#aa55ffff``` and ```#55ffffff``` respectively.

![img_045](./images/img_045.png)

With markers shown, it is easier to understand what the draw style does. Steps (Pre), Steps (Mid) and Steps (Post):

![img_046](./images/img_046.png)

![img_047](./images/img_047.png)

![img_048](./images/img_048.png)

### CSS Colors

Colors are typically input using the HTML format #rrggbb. However for primary and secondary colors, there is an internal dictionary of color name keys and hexadecimal values. Black is regarded as the absence of color i.e. the RGB LED is off and white is when the RGB is ramped up to maximum for every color.

|base color key|HTML value|
|---|---|
|```'red'```|```'#ff0000'```|
|```'green'```|```'#00ff00'```|
|```'blue'```|```'#0000ff'```|
|```'yellow'```|```'#ffff00'```|
|```'cyan'```|```'#00ffff'```|
|```'magenta'```|```'#ff00ff'```|
|```'black'```|```'#000000'```|
|```'white'```|```'#ffffff'```|

![img_049](./images/img_049.png)

There is another internal dictionary of single letters for colors, this is typically the first letter in the color, with exception to black which uses its last letter k as b is already taken for blue.

|base color letter key|HTML value|
|---|---|
|```'r'```|```'#ff0000'```|
|```'g'```|```'#00ff00'```|
|```'b'```|```'#0000ff'```|
|```'y'```|```'#ffff00'```|
|```'c'```|```'#00ffff'```|
|```'m'```|```'#ff00ff'```|
|```'k'```|```'#000000'```|
|```'w'```|```'#ffffff'```|

![img_050](./images/img_050.png)

The default colormap for matplotlib is called tableau. It has the following color dictionary:

|tab color letter key|HTML value|
|---|---|
|```'tab:blue'```|```'#1f77b4'```|
|```'tab:orange'```|```'#ff7f0e'```|
|```'tab:green'```|```'#2ca02c'```|
|```'tab:red'```|```'#d62728'```|
|```'tab:purple'```|```'#9467bd'```|
|```'tab:brown'```|```'#8c564b'```|
|```'tab:pink'```|```'#e377c2'```|
|```'tab:gray'```|```'#7f7f7f'```|
|```'tab:olive'```|```'#bcbd22'```|
|```'tab:cyan'```|```'#17becf'```|

gray is spelt using U.S. spelling with the a opposed to the e.

![img_051](./images/img_051.png)

There is also another dictionary of CSS colors that essentially expands the base color dictionary of 8 items to 200 items.

![img_052](./images/img_052.png)

![img_053](./images/img_053.png)

More details about the Markers and Colors are available in matplotlibs documentation:

[Markers](https://matplotlib.org/stable/api/markers_api.html)

[Named Colors](https://matplotlib.org/stable/gallery/color/named_colors.html)

If Generate automatic Legend is selected, a legend displays in an area of the graph with the least data being obscured:

![img_054](./images/img_054.png)

The curves dropdown list then gets updated to the set labels:

![img_055](./images/img_055.png)

### Borders and Spacing

If the borders and spacing button is selected. The borders display.

The square box is the axes. The axes have a data co-ordinate system which in this case is ymin=1, ymax=100, xmin=-1 and xmax=5. They also have a normalised coordinate system ymin=0, ymax=1, xmin=0 and xmax=1.

The axes square box is also positioned on the figure canvas which has its own normalised coordinate system ymin=0, ymax=1, xmin=0 and xmax=1.

The values shown in the borders and spacing correspond to the figure canvas normalised coordinates. 

![img_056](./images/img_056.png)

Changing the top to 1 moves the top edge of the axes to the position 1 on the figure canvas which is the top of the figure canvas:

![img_057](./images/img_057.png)

Changing the bottom to 0 moves the bottom edge of the axes to the position 0 on the figure canvas which is the bottom of the figure canvas:

![img_058](./images/img_058.png)

Changing the left to 0 moves the left edge of the axes to the position 0 on the figure canvas which is the left of the figure canvas:

![img_059](./images/img_059.png)

Changing the right to 1 moves the right edge of the axes to the position 1 on the figure canvas which is the right of the figure canvas:

![img_060](./images/img_060.png)

Resetting the Axes repositions the limits to their original values i.e. the default values which correspond to the normalised co-ordinate system of the figure canvas:

![img_061](./images/img_061.png)

The tight layout is often used to more efficiently manage the spacing:

![img_062](./images/img_062.png)

Exporting the values gives values that can be used programmatically as input arguments:

![img_063](./images/img_063.png)

## Functional Programming Overview

The ```pyplot``` module is imported from the ```matplotlib``` library using:

```
import matplotlib.pyplot as plt
```

The docstring of the ```pyplot``` module can be viewed by using ```?``` on its alias ```plt```:

```
? plt
```

Notice that it outlines functional plot generation:

![img_064](./images/img_064.png)

And object-orientated plot generation:

![img_065](./images/img_065.png)

Let's import the ```numpy``` library and ```pyplot``` module, configure the plot backend to ```qt5``` and create basic ```x``` and ```y``` data:

```
import numpy as np
import matplotlib.pyplot as plt

%matplotlib qt5

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])
```

![img_066](./images/img_066.png)

A plot will be created similar to the one before, that was modified using the GUI. 

The ```pyplot``` function ```figure``` is used to create a new figure. The keyword argument ```num``` assigns a number to a figure. If the ```num``` already exists, the figure will be reselected. If it does not already exist, a new figure will be created. If it is not specified the next available figure number is taken and a new figure is selected:

```
plt.figure(num=1, figsize=None, dpi=None)
```

![img_067](./images/img_067.png)

Notice the figure number is 1 as specified and is a blank canvas:

![img_068](./images/img_068.png)

In JupyterLab in general all the commands used to create a figure are usually input in the same cell. Let's create another figure, with ```num=2``` and then use the ```pyplot``` function ```axes``` to add axes to the existing figure:

```
plt.figure(num=2, figsize=None, dpi=None)
plt.axes()
```

![img_069](./images/img_069.png)

Notice the set of blank axes on the figure canvas. There is no data so these just show normalised co-ordinates:

![img_070](./images/img_070.png)

Think of the figure as being a canvas and the axes as being an object that lies on top of the canvas i.e. belongs to the figure. A plot is in turn an object that belongs to the axes.

```
plt.figure(num=3, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y)
```

![img_071](./images/img_071.png)

The plot is created with default settings:

![img_072](./images/img_072.png)

The axes and title are unlabelled. The ```pyplot``` functions ```xlabel```, ```ylabel``` and ```title``` can be used to set these. Each label is a string. If LaTeX is used a raw string is usually preferred (prefixed by ```r```) as the ```\``` is used commonly within most LaTeX expressions. If a variable is to be inserted, this is normally done using a formatted string (prefixed by 'f'). String concatenation ```+``` is usually used to inserrt a variable within a LaTeX expression: 

```
plt.figure(num=4, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y)
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
```

![img_073](./images/img_073.png)

![img_074](./images/img_074.png)

If a legend is to be added, each plot is normally assigned a label in the form of a string, which can be a raw string containing latex or a formatted string containing a variable. The ```pyplot``` function ```legend``` can be used to add the legend to the axes. It uses the best location by default which inserts the legend in a graph location which minimises the obscuring of underlying data.

```
plt.figure(num=5, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, label='area')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend()
```

![img_075](./images/img_075.png)

![img_076](./images/img_076.png)

The keyword ```loc``` can be used to specify the position. Normally by concatenating a y position and x position with a space. If both the x and y position are  ```'center'```, it is only mentioned once.

|y position|x position|
|---|---|
|```'lower'```|```'left'```|
|```'center'```|```'center'```|
|```'upper'```|```'right'```|

The default value is ```'best'``` which will by default pick one of the locations above which obscures the underlying data the least. 

```
plt.figure(num=6, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, label='area')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(loc='lower right')
```

![img_077](./images/img_077.png)

![img_078](./images/img_078.png)

The ```pyplot``` function ```legend``` can also take in the keyword input argument ```labels``` which can be assigned to a list of strings where the length of the list is equal to the number of traces on the plot and each string is the respective label for each trace:

```
plt.figure(num=7, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y)
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(labels=['area'], loc='lower right')
```

![img_079](./images/img_079.png)

![img_080](./images/img_080.png)

This is not noramlly done when each single trace is individually specified.

The ```pyplot``` function ```plot``` accepts multiple positional input arguments each x, y pair received corresponds will be plotted out as a seperate line. In other words by default the line plot, outputs a list of lines:

```
plt.figure(num=8, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, x, y+1, x, y+2)
```

![img_081](./images/img_081.png)

![img_082](./images/img_082.png)

In this form, any keyword argument supplied to the plot function, applies to all traces, for example:

```
plt.figure(num=9, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, x, y+1, x, y+2, label='area')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(loc='lower right')
```

![img_083](./images/img_083.png)

![img_084](./images/img_084.png)

To get unique labels, ```labels``` must be supplied as a list of strings equal in length to the number of traces expected. The labels will be of the name of the color from the default palette tableau, this palette has ```10``` values:

```
plt.figure(num=10, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, 
         x, y+1, 
         x, y+2,
         x, y+3,
         x, y+4,
         x, y+5,
         x, y+6,
         x, y+7,
         x, y+8,
         x, y+9)
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(labels=['tab:blue', 'tab:orange', 'tab:green',
                  'tab:red', 'tab:purple', 'tab:brown',
                  'tab:pink', 'tab:gray', 'tab:olive',
                  'tab:cyan'], 
           loc='lower right')
```

![img_085](./images/img_085.png)

![img_086](./images/img_086.png)

This multiform can also be used with a color positional argument for each trace:

```
plt.figure(num=11, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, 'royalblue',
         x, y+1, 'gold',
         x, y+2, 'forestgreen',
         x, y+3, 'salmon',
         x, y+4, 'violet',
         x, y+5, 'peru',
         x, y+6, 'deeppink',
         x, y+7, 'slategray',
         x, y+8, 'lawngreen',
         x, y+9, 'darkturquoise')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(labels=['royalblue', 'gold', 'forestgreen',
                  'salmon', 'violet', 'peru',
                  'deeppink', 'slategray', 'lawngreen',
                  'darkturquoise'], 
           loc='lower right')
```

![img_087](./images/img_087.png)

![img_088](./images/img_088.png)

Returning to a single trace, the full keyword input arguments will be used to specify all the options that were changed for the trace in the GUI:

```
plt.figure(num=12, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, label='area',
         color='royalblue',
         drawstyle='default',
         linewidth=2.0, linestyle='dotted',
         marker='o', markersize=15.0,
         markerfacecolor='hotpink', 
         markeredgecolor='palegreen')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(loc='lower right')
```

![img_089](./images/img_089.png)

![img_090](./images/img_090.png)

There is also a shortform for most of these keyword input arguments:

```
plt.figure(num=13, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, label='area',
         c='royalblue',
         ds='default',
         lw=2.0, ls=':',
         marker='o', ms=15.0,
         mfc='hotpink', 
         mec='palegreen')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(loc='lower right')
```

![img_091](./images/img_091.png)

![img_092](./images/img_092.png)

The ```pyplot``` functions ```xlim``` and ```ylim``` can be used to specify the x and y limits taking the keyword input arguments ```left```, ```right``` and ```top```, ```bottom``` respectively. The ```pyplot``` functions ```xscale``` and ```yscale``` can be used to change the scale of the axis. These can be set to the string ```'linear'``` (default) or ```'log'``` respecitvely.

To view the values of the data more clearly, gridlines can be added using the ```pyplot``` function ```grid```. It has the keyword arguments ```visible``` which is assigned to a boolean value, ```which``` which is assigned to the string ```'major'```, ```'minor'``` or ```'both'```, ```axis``` which is assigned to the string ```'x'```, ```'y'``` or ```'both'```. This function shares has consistent keyword arguments to the ```pyplot``` function ```plot``` such as ```color```, ```linewidth``` and ```linestyle```. The short hand abbreviations ```c```,```lw``` and ```ls``` also work:

```
plt.figure(num=14, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, label='area', c='royalblue')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(loc='lower right')
plt.xlim(left=-1, right=5)
plt.ylim(top=100, bottom=1)
plt.xscale('linear')
plt.yscale('log')
plt.tight_layout()
plt.grid(visible=True, which='major', axis='both', 
         c='lightgray', lw=3.0, ls='-')
plt.grid(visible=True, which='minor', axis='y', 
         c='lightgray', lw=1.5, ls=':')
```

![img_093](./images/img_093.png)

![img_094](./images/img_094.png)

When the linear scale is used, the minor ticks are not turned on by default, they can be enabled using:

```
plt.figure(num=14, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, label='area', c='royalblue')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(loc='lower right')
plt.xlim(left=-1, right=5)
plt.ylim(top=100, bottom=1)
plt.xscale('linear')
plt.yscale('log')
plt.tight_layout()
plt.grid(visible=True, which='major', axis='both', 
         lw=3.0, ls='-', c='lightgray')
plt.grid(visible=True, which='minor', axis='y', 
         lw=1.5, ls=':', c='lightgray')
plt.minorticks_on()
plt.grid(visible=True, which='minor', axis='x', 
         lw=1.5, ls=':', c='lightgray')
```

![img_095](./images/img_095.png)

![img_096](./images/img_096.png)

The tight layout can be enabled using the ```pyplot``` function ```tight_layout```:

```
plt.figure(num=15, figsize=None, dpi=None)
plt.axes()
plt.plot(x, y, label='area', c='royalblue')
plt.xlabel(r'length $x$ (m)')
plt.ylabel(r'area $y$ (m$^{2}$)')
plt.title(r'length $x$ vs area $y$')
plt.legend(loc='lower right')
plt.xlim(left=-1, right=5)
plt.ylim(top=100, bottom=1)
plt.xscale('linear')
plt.yscale('log')
plt.tight_layout()
plt.grid(visible=True, which='major', axis='both', 
         lw=3.0, ls='-', c='lightgray')
plt.grid(visible=True, which='minor', axis='y', 
         lw=1.5, ls=':', c='lightgray')
plt.minorticks_on()
plt.grid(visible=True, which='minor', axis='x', 
         lw=1.5, ls=':', c='lightgray')
plt.tight_layout()
```

![img_097](./images/img_097.png)

![img_098](./images/img_098.png)

If the ```math``` module is imported the constant ```tau``` can be used. A linearly spaced array of 100 values between negative tau and positive tau can be created and assigned to the variable ```x```. The trigonmetric functions can be supplied this ```x``` array to create corresponding ```y``` arrays:

```
import math
x = np.linspace(start=-math.tau, stop=math.tau, num=100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
```

![img_099](./images/img_099.png)

The ```pyplot``` function ```subplot``` can be used to create a subplot. This function uses 1st order indexing instead of Pythons usual second order indexing. The first input argument is an integer that corresponds to the number of rows, the second input argument is an integer that coreesponds to the number of columns and the third input argument is the index itself. The ordering of the subplot indexes traverses each row. Since there is only 1 column; subplot index 1 is the plot on the first row and subplot index 2 is the subplot on the second row. Let's examine subplot index 1:

```
plt.figure(num=16, figsize=None, dpi=None)
plt.subplot(2, 1, 1)
```

![img_100](./images/img_100.png)

Notice the subplot only occupies the top half of the figure canvas:

![img_101](./images/img_101.png)

In functional programming data is usually added to it before working with any other subplots:

```
plt.figure(num=17, figsize=None, dpi=None)
plt.subplot(2, 1, 1)
plt.plot(x, y1, label=r'$y$=sin($x$)')
plt.plot(x, y2, label=r'$y$=cos($x$)')
```

![img_102](./images/img_102.png)

![img_103](./images/img_103.png)

Once data is added to the the first subplot index, the second subplot index can be created and data can be added to it:

```
plt.figure(num=18, figsize=None, dpi=None)
plt.subplot(2, 1, 1)
plt.plot(x, y1, label=r'$y$=sin($x$)')
plt.plot(x, y2, label=r'$y$=cos($x$)')
plt.subplot(2, 1, 2)
plt.plot(x, y3, label=r'$y$=tan($x$)')
```

![img_104](./images/img_104.png)

![img_105](./images/img_105.png)

Sometimes the default tick values are not what is desired. In this case, it is more convenient to show the xticks in relation to the circle constant tau. A linearly spaced array of xticks can be created:

```
xticks = np.linspace(start=-math.tau, stop=math.tau, num=9)
xticks
```

![img_106](./images/img_106.png)

The value of the xticks is as desired but a string format in relation to tau may be preferred:

```
xtickvalues = [f'{num/math.tau}' + r' $\tau$' 
               for num in xticks]
xtickvalues
```

![img_107](./images/img_107.png)

The ```pyplot``` function ```xticks``` can be used to place a list of ```labels``` for each location in a specified list of ```ticks```. The list of ticks should be numeric and the list of labels should be strings:

```
plt.figure(num=19, figsize=None, dpi=None)

plt.subplot(2, 1, 1)
plt.plot(x, y1, label=r'$y$=sin($x$)', c='royalblue')
plt.plot(x, y2, label=r'$y$=cos($x$)', c='olivedrab')
plt.legend(loc='lower left')
plt.xticks(ticks=xticks, labels=xtickvalues)

plt.subplot(2, 1, 2)
plt.plot(x, y3, label=r'$y$=tan($x$)', c='tomato')
plt.legend(loc='lower left')
plt.xticks(ticks=xticks, labels=xtickvalues)

plt.xlabel(r'$\alpha$ (radians)')

plt.tight_layout()
```

![img_108](./images/img_108.png)

![img_109](./images/img_109.png)

This can be extended to more subplots for example 4 subplots with 2 rows and 2 columns. The data being plotted will be the same trigonmetry data as before, in addition to the hyperbolic trigonmetric functions. The following data will be created seperately:

```
import math
x = np.linspace(start=-math.tau, stop=math.tau, num=100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

y4 = np.sinh(x)
y5 = np.cosh(x)
y6 = np.tanh(x)

xticks = np.linspace(start=-math.tau, stop=math.tau, num=5)
xtickvalues = [f'{num/math.tau}' + r' $\tau$' 
               for num in xticks]
```

![img_110](./images/img_110.png)

Now the plot can be examined:

```
plt.figure(num=20, figsize=None, dpi=None)

plt.subplot(2, 2, 1)
plt.plot(x, y1, label=r'$y$=sin($x$)', c='royalblue')
plt.plot(x, y2, label=r'$y$=cos($x$)', c='olivedrab')
plt.legend(loc='lower left')
plt.xticks(xticks, xtickvalues)

plt.subplot(2, 2, 3)
plt.plot(x, y3, label=r'$y$=tan($x$)', c='tomato')
plt.legend(loc='lower left')
plt.xticks(xticks, xtickvalues)

plt.xlabel(r'$\alpha$ (radians)')

plt.subplot(2, 2, 2)
plt.plot(x, y4, label=r'$y$=sinh($x$)', c='royalblue')
plt.plot(x, y5, label=r'$y$=cosh($x$)', c='olivedrab')
plt.legend(loc='lower right')
plt.xticks(xticks, xtickvalues)

plt.subplot(2, 2, 4)
plt.plot(x, y6, label=r'$y$=tanh($x$)', c='tomato')
plt.legend(loc='lower right')
plt.xticks(xticks, xtickvalues)

plt.xlabel(r'$\alpha$ (radians)')

plt.tight_layout()
```

![img_111](./images/img_111.png)

![img_112](./images/img_112.png)

Selecting Figure Options now displays a dropdown with an Axes for each subplot:

![img_116](./images/img_116.png)

![img_117](./images/img_117.png)

The Borders and Spacing hspace and vertical space may be set using a normalised floating point number between 0.0 and 1.0. If 0.0 is selected,there is no spacing and if 1.0 is selected, there is a large gap used to space the subplots:

![img_118](./images/img_118.png)

![img_119](./images/img_119.png)

The ```pyplot``` function ```savefig``` can be used to save the image to a ```.png``` file or other image format. The ```pyplot``` function ```plt.close``` will close the currently selected figure:

```
plt.figure(num=21, figsize=None, dpi=None)
plt.subplot(2, 2, 1)
plt.plot(x, y1, label=r'$y$=sin($x$)', c='royalblue')
plt.plot(x, y2, label=r'$y$=cos($x$)', c='olivedrab')
plt.legend(loc='lower left')
plt.xticks(xticks, xtickvalues)
plt.subplot(2, 2, 3)
plt.plot(x, y3, label=r'$y$=tan($x$)', c='tomato')
plt.legend(loc='lower left')/
plt.xticks(xticks, xtickvalues)
plt.xlabel(r'$\alpha$ (radians)')
plt.subplot(2, 2, 2)
plt.plot(x, y4, label=r'$y$=sinh($x$)', c='royalblue')
plt.plot(x, y5, label=r'$y$=cosh($x$)', c='olivedrab')
plt.legend(loc='lower right')
plt.xticks(xticks, xtickvalues)
plt.subplot(2, 2, 4)
plt.plot(x, y6, label=r'$y$=tanh($x$)', c='tomato')
plt.legend(loc='lower right')
plt.xticks(xticks, xtickvalues)
plt.xlabel(r'$\alpha$ (radians)')
plt.tight_layout()
plt.savefig('trigonmetricplots.png')
plt.close()
```

The following code runs, the figure is seen for a second and is closed:

![img_113](./images/img_113.png)

The saved image can be seen in Windows Explorer:

![img_114](./images/img_114.png)

![img_115](./images/img_115.png)

To recap on functional programming, the following functions were examined and each function was called in turn from the ```pyplot``` module:

|pyplot function|description|
|---|---|
|figure|Create a new Figure, or activate an existing Figure.|
|axes|Add Axes to the current Figure and make it the current Axes.|
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
|show|Show the currently selected Figure (required for some IDEs).|
|close|Close the currently selected Figure.|
|savefig|Save the currently selected Figure to an image file.|

## Object Orientated Programming (OOP) Overview

The ```pyplot``` module also has an Object Orientated Programming (OOP) Application Interface (API). The ```pyplot``` function ```figure``` creates an instance of the ```Figure``` class. The following data can be created:

```
x = np.linspace(start=-5, stop=5, num=100)
y1 = x
y2 = x ** 2
y3 = x ** 3
```

![img_124](./images/img_124.png)

### Figure Class

```
fig = plt.figure(num=21, figsize=None, dpi=None)
```

![img_120](./images/img_120.png)

The list of identifiers can be accessed by inputting the ```Figure``` instances name ```fig``` followed by a dot ```.``` and a tab ```↹```:

![img_121](./images/img_121.png)

### Axes Class

The most commonly used identifiers relate to axes, for example the method ```add_axes``` can be used to draw an ```Axes``` instance using a rectangle on the figure canvas. The rectangle is specified by the keyword argument ```rect``` on the figure:

![img_122](./images/img_122.png)

The ```rect``` tuple has four values which correspond to the normalised co-ordinates of the figure canvas. ```left``` and ```bottom``` correspond to the same values seen previously. Instead of specifying the ```right``` and ```top```, the ```width``` and ```height``` are specified. These are also provided in the form of normalised floats relating to the co-ordinate system of the figure canvas.

![img_123](./images/img_123.png)

If ```left``` and ```bottom``` are set to ```0``` and ```width``` and ```height``` are set to ```1```. The square box of the axes will be at the four corners of the figure canvas.

![img_124](./images/img_124.png)

The list of identifiers from the ```Axes``` instance ```ax1``` can be viewed by inputting ```ax1.``` followed by a tab ```↹```. There are number of get methods which return a value. For example everything that has been viewed on the xaxis and yaxis:

![img_125](./images/img_125.png)

![img_126](./images/img_126.png)

There are also a number of associated set methods which mutate the ```AxesSubplot``` instance ```ax1``` in place. For example everything that has been manipulated with the xaxis and yaxis:

![img_127](./images/img_127.png)

The ```grid``` and ```minorticks_on``` methods are also available to manipulate gridlines:

![img_129](./images/img_129.png)

![img_128](./images/img_128.png)

### Line2D Class

The ```plot``` method is also available and can be used to add a lineplot to ```ax1```:

![img_130](./images/img_130.png)

Recall that ```plot``` has the multiline form:

```
fig = plt.figure(num=23, figsize=None, dpi=None)
ax1 = fig.add_axes(rect=(0, 0, 1, 1))
lines1 = ax1.plot(x, y1, 'lightcoral',
                  x, y2, 'khaki', 
                  x, y3, 'slateblue')
```

![img_131](./images/img_131.png)

![img_132](./images/img_132.png)

A consequence is the return value is always a list of ```Line2D``` instances (even if only 1 line is specified):

```
lines1
```

![img_133](./images/img_133.png)

Multiple ```Axes``` instances can be added, to a single ```Figure``` canvas. For example:

```
fig = plt.figure(num=24, figsize=None, dpi=None)
ax1 = fig.add_axes(rect=(0, 0, 1, 1))
lines1 = ax1.plot(x, y1, 'lightcoral',
                  x, y2, 'khaki', 
                  x, y3, 'slateblue')
ax2 = fig.add_axes(rect=(0.2, 0.2, 0.75, 0.75))
lines2 = ax2.plot(x, y1, 'lightcoral')
ax3 = fig.add_axes(rect=(0.3, 0.4, 0.5, 0.4))
lines3 = ax3.plot(x, y2, 'khaki')
```

![img_134](./images/img_134.png)

![img_135](./images/img_135.png)

The ```Axes``` instances can all be individually selected using:

```
ax1
ax2
ax3
```

![img_136](./images/img_136.png)

The ```Figure``` identifier ```axes``` is a list of ```Axes``` instances which belong to the ```Figure``` canvas. Each ```Axes``` instance is listed in the order created and can be accessed via indexing:

```
fig.axes
fig.axes[0]
fig.axes[0] == ax1
```

![img_137](./images/img_137.png)

Each set of lines can be individually accessed:

```
lines1
lines2
lines3
```

![img_138](./images/img_138.png)

The ```Axes``` identifier ```lines``` is a list of ```Line2D``` instances which belong to the ```Axes```. Each ```Line2D``` instance is listed in the order created and can be accessed via indexing:

```
ax1.lines
ax2.lines
ax3.lines
ax3.lines[0]
```

![img_139](./images/img_139.png)

### Getting and Setting Current Figure or Axes

The ```pyplot``` module has the functions get current figure ```gcf``` and get current axes ```gca``` which can be used to assign a figure and an axes to an object name if not done during instantiation. There is also the associated ```pyplot``` function set current axes ```sca```.  ```gca``` and ```sca``` are also available as ```Figure``` methods. 

Examples of selection are given throughout below:

```
plt.figure(num=25, figsize=None, dpi=None)
figa = plt.gcf()

plt.subplot(2, 2, 1)
ax1a = plt.gca()
ax1b = fig.gca()

plt.subplot(2, 2, 2)
ax2a = plt.gca()
ax2b = fig.gca()

plt.figure(num=26, figsize=None, dpi=None)

figb = plt.figure(num=25)

ax2c = plt.gca()
ax2d = fig.gca()
ax2e = fig.axes[1]

ax1c = fig.axes[0]

plt.figure(num=25)
plt.sca(ax1a)
figa.sca(figa.axes[0])

plt.plot(x, y1)
```

![img_140](./images/img_140.png)

Note that ```figa```, ```figb``` are selections of the same ```Figure```. ```ax1a```, ```ax1b```, ```ax1c``` are selections of the same ```Axes```. ```ax2a```, ```ax2b```, ```ax2c```, ```ax2d```, ```ax2e``` are selections of the same ```Axes```. 

Notice that figure 25 and figure 26 were both recreated but figure 25 was reselected and the current axes was changed to the first subplot. Therefore when the ```pyplot``` function ```plot``` was used, this axes was updated:

![img_141](./images/img_141.png)

![img_142](./images/img_142.png)

Learning to navigate around a created figure that hasn't been assigned to an object name can be quite useful, if a property is to be checked. The ```pyplot``` functions ```getp``` and ```setp``` can be used to get and set properties of a matplotlib object. Let's create a simpler figure:

```
fig = plt.figure(num=27, figsize=None, dpi=None)
ax = fig.add_axes(rect=(0.2, 0.2, 0.75, 0.75))
lines = ax.plot(x, y1, 'lightcoral',
                x, y2, 'khaki', 
                x, y3, 'slateblue')
```

![img_143](./images/img_143.png)

![img_144](./images/img_144.png)

### Get and Set Properties

The properties of the axes can be examined:

```
plt.getp(ax)
```

![img_145](./images/img_145.png)

Everything in the output list is a keyword input argument, available to use when the ```setp``` function is used on the same object:

```
plt.setp(ax, 
         xlabel=r'$x$', 
         ylabel=r'$y$', 
         title=r'$x$ vs $y$',
         xticks=[-3, -1, 1, 3],
         xticklabels=['-3a', '-1b', '1c', '3d'])
```

![img_146](./images/img_146.png)

![img_147](./images/img_147.png)

The properties of the lines can also be examined:

```
plt.getp(lines)
```

![img_148](./images/img_148.png)

Once again everything in the output list is a keyword input argument, available to use when the ```setp``` function is used on the same object. In this case, changing the properties here will update all lines:

```
plt.setp(lines, lw=3.0, ls=':')
```

![img_149](./images/img_149.png)

![img_150](./images/img_150.png)

The properties of an individual line can also be examined:

```
plt.getp(lines[0])
```

![img_151](./images/img_151.png)

Setting a property here will just update that single line:

```
plt.setp(ax.lines[0], c='crimson', lw=5.0, ls='-')
```

![img_152](./images/img_152.png)

![img_153](./images/img_153.png)

### Subplots

Creating an ```Axes``` instance by using the ```Figure``` method ```add_axes``` and specifying a rectangle isn't always the most convenient way. 

There is also the ```Figure``` method ```add_subplot```, which behaves consistently to the ```pyplot``` function ```subplot```. It is normally used with three positional input arguments ```nrows```, ```ncols``` and ```index```:

![img_154](./images/img_154.png)

```
fig = plt.figure(num=28, figsize=None, dpi=None)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
```

![img_155](./images/img_155.png)

![img_156](./images/img_156.png)

It can also be used with a single input argument which is a three digit integer corresponding to ```nrows```, ```ncols``` and the ```index``` respectively:

```
fig = plt.figure(num=29, figsize=None, dpi=None)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
```

![img_157](./images/img_157.png)

![img_158](./images/img_158.png)

If no input arguments are supplied to the ```Figure``` method ```add_subplot```, a single ```Axes``` is created that spans the figure canvas i.e. the default is ```nrows=1```, ```ncols=1```, ```index=1``` or ```111```. This behaves consistently to the ```Axes``` created when the ```pyplot``` function ```axes``` is used:

```
fig = plt.figure(num=30, figsize=None, dpi=None)
ax = fig.add_subplot()
```

![img_159](./images/img_159.png)

![img_160](./images/img_160.png)

Instead of having each ```Axes``` assigned to a seperate ```object``` name, it can be more convenient to have all of the ```Axes``` within a collection such as a ```ndarray```. The ```Figure``` method ```subplots``` does this:

![img_161](./images/img_161.png)

Because the output is a collection of all of the ```Axes```, only ```nrows``` and ```ncols``` are required as input argument. There is no ```index``` input argument as the desired ```Axes``` is selected via indexing.

```
fig = plt.figure(num=31, figsize=None, dpi=None)
axarray = fig.subplots(2, 1)
```

![img_162](./images/img_162.png)

![img_163](./images/img_163.png)

Since ```ncols=1```, a 1d ```ndarray``` is output. This can be indexed using regular zero-order indexing of a 1d ```ndarray```:

```
axarray
axarray[0]
```

![img_164](./images/img_164.png)

If ```nrows=2``` and ```ncols=2```:

```
fig = plt.figure(num=32, figsize=None, dpi=None)
axarray = fig.subplots(2, 2)
```

![img_165](./images/img_165.png)

![img_166](./images/img_166.png)

Then the output is a 2d ```ndarray```:

![img_166](./images/img_166.png)

This can be indexed using regular zero-order indexing of a 2d ```ndarray```:

```
axarray
axarray[0, 1]
```

![img_167](./images/img_167.png)

Since each item in the ```ndarray``` instance           ```axarray``` is an ```Axes```, they can be indexed into and all the identifiers for that ```Axes``` instance can be used:

```
fig = plt.figure(num=33, figsize=None, dpi=None)
axarray = fig.subplots(2, 2)
axarray[0, 0].plot(x, y1, c='deepskyblue')
axarray[0, 1].plot(x, y2, c='peru')
axarray[1, 0].plot(x, y3, c='plum')
```

![img_168](./images/img_168.png)

![img_169](./images/img_169.png)

The first two lines are often combined using the ```pyplot``` function ```subplots```. The ```pyplot``` function ```subplots``` outputs a ```tuple```, the first index of the ```tuple``` is the ```Figure``` and the second index of the ```tuple``` is the ```ndarray``` of ```Axes```:

```
fig, axarray = plt.subplots(2, 2, 
                           num=34, figsize=None, dpi=None)
axarray[0, 0].plot(x, y1, c='deepskyblue')
axarray[0, 1].plot(x, y2, c='peru')
axarray[1, 0].plot(x, y3, c='plum')
```

![img_170](./images/img_170.png)

![img_171](./images/img_171.png)

The ```Figure``` method ```subplot_mosaic``` can be used to create a ```dict``` of ```Axes``` using a ```mosaic```. A ```mosaic``` is a list of strings or a list of nested list of strings. The strings in a ```mosaic``` should be valid identifiers, as each string will become a key in the ```dict```:

![img_172](./images/img_172.png)

```
fig = plt.figure(num=35, figsize=None, dpi=None)
axdict = fig.subplot_mosaic(mosaic=[['linear', 'quadratic'],
                                    ['cubic', 'cubic']])
axdict
```

![img_173](./images/img_173.png)

![img_174](./images/img_174.png)

This key is used to index into the dictionary ```axdict``` to get the corresponding ```Axes```:

```
fig = plt.figure(num=36, figsize=None, dpi=None)
axdict = fig.subplot_mosaic(mosaic=[['linear', 'quadratic'],
                                ['cubic', 'cubic']])
axdict['linear'].plot(x, y1, c='deepskyblue')
axdict['quadratic'].plot(x, y2, c='peru')
axdict['cubic'].plot(x, y3, c='plum')
```

![img_175](./images/img_175.png)

![img_176](./images/img_176.png)

The first two lines are also combined using the ```pyplot``` function ```subplot_mosaic```. The ```pyplot``` function ```subplot_mosaic``` outputs a ```tuple```, the first index of the ```tuple``` is the ```Figure``` and the second index is the ```dict``` of ```Axes```:

```
fig, axdict = plt.subplot_mosaic(mosaic=[['linear', 'quadratic'],
                                         ['cubic', 'cubic']],
                                 num=37, figsize=None, dpi=None)
axdict['linear'].plot(x, y1, c='deepskyblue')
axdict['quadratic'].plot(x, y2, c='peru')
axdict['cubic'].plot(x, y3, c='plum')
```

![img_177](./images/img_177.png)

![img_178](./images/img_178.png)

The ```subplot_mosaic``` ```pyplot``` function or ```Figure``` method can take a keyword input argument ```per_subplot_kw```. The ```per_subplot_kw``` is also a ```dict``` where the keys correspond to the keys used within the axes ```dict``` and the values are a nested ```dict``` of properties. The nested ```dict``` has keys that are keyword arguments recognised by an ```Axes``` and the values are their corresponding values. These properties get supplied to each corresponding ```Axes```:

```
axdictprop = {'linear': {'xlabel': 'x', 'ylabel': 'y1'},
              'quadratic': {'xlabel': 'x', 'ylabel': 'y2'},
              'cubic': {'xlabel': 'x', 'ylabel': 'y3'}}

fig, axdict = plt.subplot_mosaic(mosaic=[['linear', 'quadratic'],
                                         ['cubic', 'cubic']],
                                 per_subplot_kw=axdictprop,
                                 num=38, figsize=None, dpi=None)
axdict['linear'].plot(x, y1, c='deepskyblue')
axdict['quadratic'].plot(x, y2, c='peru')
axdict['cubic'].plot(x, y3, c='plum')
fig.tight_layout()
```

![img_179](./images/img_179.png)

![img_180](./images/img_180.png)

Recall valid input arguments that can be supplied as ```Axes``` properties in the nested ```dict``` in ```per_subplot_kw``` can be seen by using the ```pyplot``` function ```getp``` on an ```Axes```:

```
plt.getp(axdict['linear'])
```

![img_181](./images/img_181.png)

The above plot uses the ```Figure``` method ```tight_layout```, the other options seen in the borders and spacing GUI are accessible from the ```Figure``` method ```subplots_adjust```. There is also a ```pyplot``` function ```subplots_adjust``` which operates similarly on the currently selected figure.

![img_183](./images/img_183.png)

These use keyword arguments ```left```, ```bottom```, ```right```, ```top```, ```wspace``` and ```hspace``` which match the labels of the spinboxes in the borders and spacing GUI:

![img_182](./images/img_182.png)

```
axdictprop = {'linear': {'xlabel': 'x', 'ylabel': 'y1'},
              'quadratic': {'xlabel': 'x', 'ylabel': 'y2'},
              'cubic': {'xlabel': 'x', 'ylabel': 'y3'}}

fig, axdict = plt.subplot_mosaic(mosaic=[['linear', 'quadratic'],
                                         ['cubic', 'cubic']],
                                 per_subplot_kw=axdictprop,
                                 num=39, figsize=None, dpi=None)
axdict['linear'].plot(x, y1, c='deepskyblue')
axdict['quadratic'].plot(x, y2, c='peru')
axdict['cubic'].plot(x, y3, c='plum')
plt.subplots_adjust(left=0.12, bottom=0.12, 
                    right=0.98, top=1.0,
                    wspace=0.4, hspace=0.3)
```

![img_184](./images/img_184.png)

![img_185](./images/img_185.png)

### Projection

The ```Figure``` method ```add_subplots``` has a keyword argument ```projection``` which has a default value ```rectilinear```. It can be changed to another option such as ```'polar'``` to get a polar plot. 

A complex number can be represented as:

$$z=x+jy$$

Where $x$ is the real axis and $y$ is the imaginary axis denoted by $j$. 

If this number is compared to the origin $x=0$ (angle 0 radians) and $y=0$ (radius 0). A straight line can be drawn from the point to this origin which is known as the radius $r$. An angle $\varphi$ (in radians) can be calculated by measuring the value of this angle from the real axis. The complex number can therefore be expressed as:

$$z=r\exp(j\varphi)$$

And plotted on a polar plot at the angle $\varphi$ with the radius $r$. $\varphi$ is measured in radians and 8 angles corresponding to eighths of $\tau$ can be plotted as markers at a fixed $r$ of 1:

```
fig = plt.figure(num=40, figsize=None, dpi=None)
axpolar = fig.add_subplot(111, projection='polar')
axpolar.plot(0*math.tau/8, 1, color='royalblue', 
             ls=None, marker='o', markersize=10)
axpolar.plot(1*math.tau/8, 1, color='gold', 
             ls=None, marker='s', markersize=10)
axpolar.plot(2*math.tau/8, 1, color='forestgreen', 
             ls=None, marker='p', markersize=10)
axpolar.plot(3*math.tau/8, 1, color='salmon', 
             ls=None, marker='h', markersize=10)
axpolar.plot(4*math.tau/8, 1, color='violet', 
             ls=None, marker='8', markersize=10)
axpolar.plot(5*math.tau/8, 1, color='peru', 
             ls=None, marker='X', markersize=10)
axpolar.plot(6*math.tau/8, 1, color='deeppink', 
             ls=None, marker='*', markersize=10)
axpolar.plot(7*math.tau/8, 1, color='slategray', 
             ls=None, marker='P', markersize=10)
```

![img_186](./images/img_186.png)

![img_187](./images/img_187.png)

Although the unit of measurement of an angle is in radians. It is shown in degrees. If the properties of the ```axpolar``` are examined using the ```pyplot``` function ```getp```:

```
plt.getp(axpolar)
```

![img_188](./images/img_188.png)

The xticks themselves are shown to be in radians, however the xticklabels are shown to be in degrees. The xtick labels can be changed to a numeric scale involving $\tau$ using the ```pyplot``` function ```setp```:

```
[f'{num/math.tau}'+r'$\tau$' for num in axpolar.get_xticks()]
```

![img_189](./images/img_189.png)

```
plt.setp(axpolar, xticklabels=[f'{num/math.tau}'+r'$\tau$' 
                              for 
                              num 
                              in 
                              axpolar.get_xticks()])
```

![img_190](./images/img_190.png)

There is a ```UserWarning: FixedFormatter should only be used together with FixedLocator``` however this warning can be ignored as the change takes place as expected:

![img_191](./images/img_191.png)

Instead of decimals, fractions can be used:

```
[r'$\frac{'+f'{num}'+r'}{8\tau}$' for num in range(8)]
```

![img_192](./images/img_192.png)

Note the difference in the use of ```{}``` in the formatted string and relative string:

```
plt.setp(axpolar, xticklabels=[r'$\frac{'+f'{num}'+r'}{8\tau}$' 
                              for 
                              num 
                              in 
                              range(8)])
```

![img_193](./images/img_193.png)

There is once again a ```UserWarning: FixedFormatter should only be used together with FixedLocator``` however this warning can be ignored as the change takes place as expected:

![img_194](./images/img_194.png)

This ```UserWarning``` can be removed by updating ```xticks``` to the original values:

```
plt.setp(axpolar, xticks=axpolar.get_xticks(),
         xticklabels=[r'$\frac{'+f'{num}'+r'}{8}\tau$' 
                     for 
                     num 
                     in 
                     range(8)])
```

![img_195](./images/img_195.png)

Another projection is ```'3d'``` which will give a ```Axes3D``` instance:

```
fig = plt.figure(num=41, figsize=None, dpi=None)
ax3d = fig.add_subplot(111, projection='3d')
```

![img_196](./images/img_196.png)

![img_197](./images/img_197.png)

The 3D Axes has a Z-Axis shown in the Figure Options:

![img_198](./images/img_198.png)

If the ```pyplot``` function ```getp``` is used on the 3d ```Axes3D```, the properties for the ```Z-Axis``` will display:

```
plt.getp(ax3d)
```

![img_199](./images/img_199.png)

The identifiers of the ```Axes3D``` instance can be viewed by inputting ```ax.``` followed by a tab ```↹```. The azimuthal angle ```azim``` and elevation ```elev``` angle are related to the view of the ```Axes3D``` from the users fixed reference plane:

![img_200](./images/img_200.png)

![img_201](./images/img_201.png)

And supplementary 3D plots are available such as ```plot3D```:

![img_202](./images/img_202.png)

 The azimuthal angle is a horizontal angle measured clockwise from the users fixed reference plane. The altitude angle is the angle above the horizon. The default azimuthal angle ```azim``` and elevation ```elev``` angle are ```-60``` and ```30``` respectively:

```
ax3d.azim
ax3d.elev
```

![img_203](./images/img_203.png)

![img_204](./images/img_204.png)

To explore the above views in more detail, some data can be created:

```
xrow = np.linspace(-2, 2, 100)[np.newaxis, :]
ycol = np.linspace(-2, 2, 100)[:, np.newaxis]
xmat, ymat = np.meshgrid(xrow, ycol)
zdata_fun = lambda x, y: x * np.exp(-x**2 - y**2)
zmat = zdata_fun(x=xrow, y=ycol)
xarray = xmat.flatten()
yarray = ymat.flatten()
zarray = zmat.flatten()
```

![img_218](./images/img_218.png)

The equally sized flattened 1d ```ndarrays``` can be supplied to ```Axes3D``` method ```plot3D``` and the ```Axes3D``` methods ```set_xlabel```, ```set_ylabel``` and ```set_zlabel``` can be used for clarity:

```
fig = plt.figure(num=42, figsize=None, dpi=None)
ax3d = fig.add_subplot(111, projection='3d')
ax3d.plot3D(xarray, yarray, zarray)
ax3d.set_xlabel(r'$x$')
ax3d.set_ylabel(r'$y$')
ax3d.set_zlabel(r'$z$')
```

![img_219](./images/img_219.png)

![img_220](./images/img_220.png)

The view angles are:

```
ax3d.azim
ax3d.elev
```

![img_221](./images/img_221.png)

The ```Axes3D``` can be rotated by left clicking the ```Axes3D``` with the mouse, holding down the left click and moving the mouse:

![img_222](./images/img_222.png)

After moving the view angles are:

```
ax3d.azim
ax3d.elev
```

![img_223](./images/img_223.png)

![img_224](./images/img_224.png)

After moving the view angles are:

```
ax3d.azim
ax3d.elev
```

![img_225](./images/img_225.png)

### Aspect

The aspect ratio of a set of an ```Axes``` or ```Axes3D``` instance can be configured, this is particularly useful if wanting to plot a square or cube. The ```Axes``` or ```Axes3D``` class has a number of set methods, these can be accessed by inputting an instance, for example ```ax3d``` followed by a dot ```.``` and a tab ```↹```:

![img_226](./images/img_226.png)

The docstring for the ```Axes3D``` method ```set_aspect``` can be examined by typing in ```ax3d.set_aspect()```, followed by a shift ```⇧``` and tab ```↹```:

![img_227](./images/img_227.png)

For an ```Axes3D``` instance, there is the default ```'auto'``` which independently scales each axis. This can be changed to ```'equal'``` which will maintain an equal aspect ratio or one of the other strings ```'equalxy'```, ```'equalxy'``` and ```'equalxz'``` that leave one axes independent and maintain the aspect ratio of the other two.

For simplicity an ```Axes``` instance will be examined:

![img_228](./images/img_228.png)

The docstring for the ```Axes``` method ```set_aspect``` can be examined by typing in ```ax.set_aspect()```, followed by a shift ```⇧``` and tab ```↹```:

![img_229](./images/img_229.png)

For an ```Axes``` instance, there is the default ```'auto'``` which independently scales each axis. This can be changed to ```'equal'``` which will maintain an equal aspect ratio. Finally a floating point value can be used to select the length of the $y$ axis to the length of the $x$. 

```
fig, axarray = plt.subplots(3, 1, num=43, figsize=None, dpi=None)
axarray[0].set_aspect('auto')
axarray[0].plot(1, 1, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[0].plot(1, 2, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[0].plot(2, 1, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[0].plot(2, 2, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[0].plot(4, 4, ls=None, marker='o', mfc='fuchsia', mec='lawngreen')
axarray[1].set_aspect('equal')
axarray[1].plot(1, 1, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[1].plot(1, 2, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[1].plot(2, 1, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[1].plot(2, 2, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[1].plot(4, 4, ls=None, marker='o', mfc='fuchsia', mec='lawngreen')
axarray[2].set_aspect(4)
axarray[2].plot(1, 1, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[2].plot(1, 2, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[2].plot(2, 1, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[2].plot(2, 2, ls=None, marker='o', mfc='royalblue', mec='tomato')
axarray[2].plot(4, 4, ls=None, marker='o', mfc='fuchsia', mec='lawngreen')
```

![img_230](./images/img_230.png)

![img_231](./images/img_231.png)

### Shared Axes

Sometimes it is desirable to share an axis between two axes. Sharing the xaxis between two axes means if the xlimits, xticks or xticklabels in one is altered, the other is also altered. The trigonometric functions can once again be examined:

```
import math
x = np.linspace(start=-math.tau, stop=math.tau, num=100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
```

![img_232](./images/img_232.png)

And a plot can be configured as shown:

```
fig = plt.figure(num=44, figsize=None, dpi=None)
ax1 = fig.add_subplot(211)
ax1.plot(x, y1, label=r'$y$=sin($x$)')
ax1.plot(x, y2, label=r'$y$=cos($x$)')
ax2 = fig.add_subplot(212, sharex=ax1)
ax2.plot(x, y3, label=r'$y$=tan($x$)')
```

![img_233](./images/img_233.png)

![img_234](./images/img_234.png)

Since ```ax2``` and ```ax1``` share the xaxis, using the ```pyplot``` function ```getp``` to update the properties of ```ax2``` also updates ```ax1```. In this case the xticks, xticklabels and xlim for both ```ax2``` and ```ax1``` are updated however the ```xlabel``` is independent and only updated in ```ax2```:

```
plt.setp(ax2, 
         xticks=np.linspace(start=-math.tau, 
                            stop=math.tau, 
                            num=5),
         xticklabels=[r'$\frac{'+f'{num}'+r'}{2}\tau$' 
                      for 
                      num 
                      in 
                      range(-2, 3, 1)],
         xlim=(-9, 9),
         xlabel=r'$x$')
```

![img_235](./images/img_235.png)

![img_236](./images/img_236.png)

### Twin Axes

Sometimes it is desirable to twin an axis between two axes allowing a plot overlay of two related datasets. For example the trigonmetric data above which has the same $x$ data can have a twinned xaxis and use the left $y$ axis for the sin and cos function and the right yaxis for the tan function:

```
fig = plt.figure(num=45, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y1, label=r'$y$=sin($x$)', c='royalblue')
ax1.plot(x, y2, label=r'$y$=cos($x$)', c='olivedrab')
ax2 = ax1.twinx()
ax2.plot(x, y3, label=r'$y$=tan($x$)', c='tomato')
fig.legend(loc='upper right')
```

![img_237](./images/img_237.png)

![img_238](./images/img_238.png)

Notice the use of the ```Figure``` method ```legend``` instead of the ```Axes``` method ```legend```. This creates a combined ```legend``` containing the traces for all ```Axes``` in the ```Figure```.

For a twinx axis, it is important to clearly label the axes and sometimes it may be desirable to have the legends for each ```Axes``` seperately shown beside the respective ```Axes```. For example:

```
fig = plt.figure(num=46, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y1, label=r'$y$=sin($x$)', c='royalblue')
ax1.plot(x, y2, label=r'$y$=cos($x$)', c='olivedrab')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y1$ or $y2$')
ax1.legend(loc='upper left')
ax2 = ax1.twinx()
ax2.plot(x, y3, label=r'$y$=tan($x$)', c='tomato')
ax2.set_ylabel(r'$y3$')
ax2.legend(loc='upper right')
fig.tight_layout()
```

![img_239](./images/img_239.png)

![img_240](./images/img_240.png)

If the ```pyplot``` function ```getp``` is used on each ```Axes``` ```yaxis``` attribute, details about the ```yaxis```:

```
plt.getp(ax1.yaxis)
plt.getp(ax2.yaxis)
```

![img_241](./images/img_241.png)

![img_242](./images/img_242.png)

The ```label_location```, ```tick_params``` and ```ticks_position``` all show right for ```ax2```. These can be accessed and modified using their corresponding get and set methods:```⇧```

![img_243](./images/img_243.png)

```
ax2.yaxis.get_label_position()
ax2.yaxis.get_tick_params()
ax2.yaxis.get_ticks_position()
```

![img_244](./images/img_244.png)

### Tick Parameters and Grid

```ax2.yaxis.get_tick_params()``` means ```yaxis``` is an attribute of the ```Axes``` instance ```ax2``` and ```get_tick_params``` is in turn a method of ```yaxis```. If the docstring of the corresponding set method is examined by inputting ```ax2.yaxis.get_tick_params()``` and pressing shift ```⇧``` and tab ```↹```:

![img_245](./images/img_245.png)

The docstring refers to the more general ```tick_params``` method of the ```Axes``` instance ```ax2```. Its docstring may examined by inputting ```ax2.tick_params()``` and pressing shift ```⇧``` and tab ```↹```:

![img_246](./images/img_246.png)

This function has the three keyword parameters ```axis```, ```which``` and ```reset``` which are used to select the component the changes are applied to. 

The ```axis``` can be used to select the axis ```'x'```, ```'y'``` or ```'both'```. When the ```yaxis``` attribute is selected, the ```axis``` parameter is redundant  following two are therefore equivalent:

```
ax2.yaxis.set_tick_params()
ax2.tick_params(which='y')
```

The ```which``` parameter has the options ```'major'```, ```'minor'``` or ```'both'```.

The ```reset``` parameter will reset the ticks to default before making any changes.

The parameters that can be changed are then listed. These relate to the ticks, the ticklabel and the grid:

![img_247](./images/img_247.png)

![img_248](./images/img_248.png)

The grid parameters are often modified using the seperate function ```grid```. Its docstring may examined by inputting ```ax2.grid()``` and pressing shift ```⇧``` and tab ```↹```:

![img_249](./images/img_249.png)

This has a ```visible``` parameter which is a boolean value and has the ```which``` and ```axis``` parameters which behave consistently to their counterparts in the ```tick_params``` method. Like the ```tick_params``` method, the two expressions are equivalent:

```
ax2.yaxis.grid()
ax2.grid(which='y')
```

The additional keyword arguments ```color``` or ```c```, ```linewidth``` or ```lw``` and ```linestyle``` or ```ls``` for example behave consistently to their counterparts in the method ```plot```. Other keyword arguments relating to markers are also available.

When the grid is made visible it looks like the following:

```
fig = plt.figure(num=47, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y1, label=r'$y$=sin($x$)')
ax1.plot(x, y2, label=r'$y$=cos($x$)')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.grid(visible=True)
```

![img_250](./images/img_250.png)

![img_251](./images/img_251.png)

The major gridlines can be customised and the minorticks can be enabled:

```
fig = plt.figure(num=48, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y1, label=r'$y$=sin($x$)')
ax1.plot(x, y2, label=r'$y$=cos($x$)')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.grid(visible=True, axis='both', which='major',
         c='lightgrey', ls='-', lw=1.5)
ax1.minorticks_on()
```

![img_252](./images/img_252.png)

![img_253](./images/img_253.png)

Now minor gridlines can be added:

```
fig = plt.figure(num=49, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y1, label=r'$y$=sin($x$)')
ax1.plot(x, y2, label=r'$y$=cos($x$)')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.grid(visible=True, axis='both', which='major',
         c='lightgrey', ls='-', lw=1.5)
ax1.minorticks_on()
ax1.grid(visible=True, axis='both', which='minor',
         c='lightgrey', ls=':', lw=1.0)
```

![img_254](./images/img_254.png)

![img_255](./images/img_255.png)

Both the gridlines and the tick parameters cn be customised:

```
fig = plt.figure(num=50, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y1, label=r'$y$=sin($x$)')
ax1.plot(x, y2, label=r'$y$=cos($x$)')
ax1.set_xlabel(r'$x$', c='blueviolet')
ax1.set_ylabel(r'$y$', c='blueviolet')
ax1.grid(visible=True, axis='both', which='major', 
         c='lightgrey', ls='-', lw=1.5)
ax1.tick_params(axis='both', which='major',
                direction='in', length=5,
                width=3,
                color='tomato', labelcolor='dodgerblue')
ax1.minorticks_on()
ax1.grid(visible=True, axis='both', which='major',
         c='lightgrey', ls=':', lw=1.0)
ax1.tick_params(axis='both', which='minor',
                direction='in', length=3,
                width=1.5,
                color='darkorange', labelcolor='aqua')
```

![img_256](./images/img_256.png)

![img_257](./images/img_257.png)

### Spines

The ```Axes``` attribute ```spines``` can be accessed by from an ```Axes``` instance ```ax1```:

![img_258](./images/img_258.png)

Attributes can be accessed from this by typing in a further dot ```.``` and a tab ```↹```:

![img_259](./images/img_259.png)

This is a dictionary like collection and its keys can be viewed by use of the ```keys``` method and casting to a ```tuple```:

```
ax1.spines.keys()
tuple(ax1.spines.keys())
```

![img_260](./images/img_260.png)

A key can be used to index into the dictionary to get a spine value. Unfortunately then using a dot ```.``` and tab ```↹``` does not display the attributes:

![img_261](./images/img_261.png)

These can be viewed by assigning the value to a new object name and indexing from that:

```
rightspine = ax1.spines['right']
```

![img_262](./images/img_262.png)

The spine has a number of get and set methods. The method ```set_visible``` can be used to hide the spine:

```
rightspine.set_visible(False)
```

This is equivalent to the expression (code completion won't show any of the docstrings for the methods):

```
ax1.spines['right'].set_visible(False)
```

![img_263](./images/img_263.png)

![img_264](./images/img_264.png)

The top spine can also be examined. It may be convenient to use the ```pyplot``` fucntion ```getp``` to view the properties:

```
topspine = ax1.spines['top']
plt.getp(topspine)
```

![img_265](./images/img_265.png)

The following settings can be applied:

```
plt.setp(topspine, ls=':', lw=5, 
         ec='aquamarine', fc='mediumblue',
         visible=True)
```

![img_266](./images/img_266.png)

![img_267](./images/img_267.png)

Note as the spine is mainly a line. The ```facecolor``` or ```fc``` and ```hatch``` are negligible.

### Axes and Figure FaceColor

The ```Axes``` and ```Figure``` facecolor can be accessed using their respective methods ```get_facecolor```:

```
ax1.get_facecolor()
fig.get_facecolor()
```

![img_268](./images/img_268.png)

The color is given as a ```tuple``` of normalised floating point numbers. This has the form ```(r, g, b, a)``` corresponding to the red, green, blue and alpha channels respectively. Instead of having 255 integer levels displayed in hexadecimal, the float tuple is normalised. A value of ```1``` is equivalent to the integer ```255``` or hexadecimal ```FF```. In other words ```255/255``` is ```1```. The color given is therefore ```'white'``` or ```'#FFFFFF'``` or ```'#FFFFFFFF'```. The analogous ```set_facecolor``` method can be used to set the color:

```
ax1.set_facecolor('lightcyan')
fig.set_facecolor('paleturquoise')
```

![img_269](./images/img_269.png)

![img_270](./images/img_270.png)

### Figure and Axes Methods

Previously the ```pyplot``` function ```savefig``` was examined. The ```Figure``` class has an analogous method ```savefig``` which behaves similarly:

```
fig.savefig('trigonmetricplots2.png')
```

![img_271](./images/img_271.png)

![img_272](./images/img_272.png)

![img_273](./images/img_273.png)

The ```pyplot``` function ```show``` was also examined. The ```Figure``` class has an analogous method ```show``` which behaves similarly. For IDEs such as VSCode which require a figure to be shown, normally the ```show``` method is used seperately for each figure and then the ```pyplot``` function ```show``` is used to show all the plots:

```
fig.show()
plt.show()
```

![img_274](./images/img_274.png)

The ```pyplot``` function ```clf``` and ```cla``` can be used to clear a ```Figure``` or ```Axes``` respectively:

```
plt.cla()
```

![img_275](./images/img_275.png)

![img_276](./images/img_276.png)

```
plt.clf()
```

![img_277](./images/img_277.png)

![img_278](./images/img_278.png)

The ```Figure``` and the ```Axes``` classes also have their own ```clear``` methods which behave analogously:

```
fig.clear()
ax.clear()
```

![img_279](./images/img_279.png)

The ```pyplot``` function ```close``` can be used to close an open Figure by specification of the ```fig``` using its integer value:

```
plt.close(fig=50)
```

![img_280](./images/img_280.png)

Assigning the string ```'all'``` will close all open figures:

```
plt.close(fig='all')
```

![img_281](./images/img_281.png)

### Annotate

Let's examine the simple $x$, $y$ dataset:

```
x = np.arange(start=0, stop=10, step=1)
y = 2 * x
```

![img_282](./images/img_282.png)

This straight line will be plotted out 6 times with markers using subplots:

```
fig = plt.figure(num=51, figsize=None, dpi=None)
ax1 = fig.add_subplot(321)
ax1.plot(x, y, label=r'$y$=2$x$', marker='o')
ax2 = fig.add_subplot(323)
ax2.plot(x, y, label=r'$y$=2$x$', marker='o')
ax3 = fig.add_subplot(325)
ax3.plot(x, y, label=r'$y$=2$x$', marker='o')
ax4 = fig.add_subplot(322)
ax4.plot(x, y, label=r'$y$=2$x$', marker='o')
ax5 = fig.add_subplot(324)
ax5.plot(x, y, label=r'$y$=2$x$', marker='o')
ax6 = fig.add_subplot(326)
ax6.plot(x, y, label=r'$y$=2$x$', marker='o')
```

![img_283](./images/img_283.png)

![img_284](./images/img_284.png)

The ```Axes``` method ```annotate``` can be used to annotate a data point. The ```text``` is the string that is to be be displayed on the figure. ```xy``` is a ```tuple``` which corresponds to the x and y co-ordinate to be annotated. ```xytext``` is another ```tuple``` which states the co-ordinate where the lower left corner of the text is to be placed. The ```xycoords``` is a string relating to the co-ordinate system and is usually set to the string ```'data'```. ```arrowprops``` is a dictionary which contains the key ```'arrowstyle'``` and other optional keys:

![img_285](./images/img_285.png)

```
text1 = ax1.annotate(text=f'(2, 4)', xy=(2, 4), 
                     xytext=(2, 10), xycoords='data',
                     arrowprops={'arrowstyle': 'simple'})
text2 = ax2.annotate(text=f'(2, 4)', xy=(2, 4), 
                     xytext=(2, 10), xycoords='data',
                     arrowprops={'arrowstyle': 'fancy'})
text3 = ax3.annotate(text=f'(2, 4)', xy=(2, 4), 
                     xytext=(2, 10), xycoords='data',
                     arrowprops={'arrowstyle': 'wedge'})
text4 = ax4.annotate(text=f'(2, 4)', xy=(2, 4), 
                     xytext=(2, 10), xycoords='data',
                     arrowprops={'arrowstyle': '->'})
text5 = ax5.annotate(text=f'(2, 4)', xy=(2, 4), 
                     xytext=(2, 10), xycoords='data',
                     arrowprops={'arrowstyle': '<-'})
text6 = ax6.annotate(text=f'(2, 4)', xy=(2, 4), 
                     xytext=(2, 10), xycoords='data',
                     arrowprops={'arrowstyle': '<->'})
```

![img_286](./images/img_286.png)

![img_287](./images/img_287.png)

Other keyword arguments can be added to the ```arrowprops``` dictionary for additional customisation. More details are given in matplotlibs documentation:

[Annotations](https://matplotlib.org/stable/tutorials/text/annotations.html)

## Line Plots

The ```pyplot``` functions or ```Axes``` method ```plot``` was seen to produce a line plot. There are additional ```pyplot``` functions or ```Axes``` methods which also create line plots, these functions have some of the default values for the line such as the drawstyle of the options for the Axes such as the xlimit, ylimit, xscale and yscale precofigured.

The ```pyplot``` function or ```Axes``` method ```step``` creates a line plot with the drawstyle preconfigured to ````'steps-pre'```. This can be seen by comparing:

```
fig = plt.figure(num=52, figsize=None, dpi=None)
ax1 = fig.add_subplot(211)
ax1.plot(x, y, ds='steps-pre')
ax2 = fig.add_subplot(212)
ax2.step(x, y)
```

![img_288](./images/img_288.png)

![img_289](./images/img_289.png)

The ```pyplot``` function or ```Axes``` method ```semilogx``` creates a line plot with the xscale preconfigured to ```'log'```. This can be seen by comparing:

```
fig = plt.figure(num=53, figsize=None, dpi=None)
ax1 = fig.add_subplot(211)
ax1.plot(x, y)
ax1.set_xscale('log')
ax2 = fig.add_subplot(212)
ax2.semilogx(x, y)
```

![img_290](./images/img_290.png)

![img_291](./images/img_291.png)

The ```pyplot``` function or ```Axes``` method ```semilogy``` creates a line plot with the yscale preconfigured to ````'log'```. This can be seen by comparing:

```
fig = plt.figure(num=54, figsize=None, dpi=None)
ax1 = fig.add_subplot(211)
ax1.plot(x, y)
ax1.set_yscale('log')
ax2 = fig.add_subplot(212)
ax2.semilogy(x, y)
```

![img_292](./images/img_292.png)

![img_293](./images/img_293.png)

The ```pyplot``` function or ```Axes``` method ```loglog``` creates a line plot with the xscale and yscale preconfigured to ````'log'```. This can be seen by comparing:

```
fig = plt.figure(num=55, figsize=None, dpi=None)
ax1 = fig.add_subplot(211)
ax1.plot(x, y)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax2 = fig.add_subplot(212)
ax2.loglog(x, y)
```

![img_294](./images/img_294.png)

![img_295](./images/img_295.png)

The ```pyplot``` function and ```Axes``` method ```axhline``` can be used to draw a horizontal line:

![img_296](./images/img_296.png)

It has the input argument ```y``` and the optional input arguments ```xmin``` and ```xmin```. Note that ```y``` is in data co-ordinates whereas ```xmin``` and ```xmax``` use normalised co-ordinates corresponding to the normalised dimensions of the xaxis.

```
fig = plt.figure(num=56, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y, c='royalblue', marker='o')
ax1.axhline(y=2, xmin=0, xmax=1, c='tomato')
ax1.axhline(y=4, xmin=0.25, xmax=0.75, c='darkorange')
```

![img_297](./images/img_297.png)

![img_298](./images/img_298.png)

The ```pyplot``` function and ```Axes``` method ```axvline``` can be used to draw a vertical line. It has the input argument ```x``` and the optional input arguments ```ymin``` and ```ymin```. Note that ```x``` is in data co-ordinates whereas ```ymin``` and ```ymax``` use normalised co-ordinates corresponding to the normalised dimensions of the xaxis.

```
fig = plt.figure(num=57, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y, c='royalblue', marker='o')
ax1.axvline(x=2, ymin=0, ymax=1, c='tomato')
ax1.axvline(x=4, ymin=0.25, ymax=0.75, c='darkorange')
```

![img_299](./images/img_299.png)

![img_300](./images/img_300.png)

The ```pyplot``` function and ```Axes``` method ```axline``` can be used to draw an infinite line to the edges of the ```Axes```. This has the input arguments ```xy1``` which is a ```tuple``` of ```(x, y)``` data co-ordinates. A floating point ```slope``` can be calculated so an infinite line of that slope that intersects that point is drawn. Alternatively a second co-ordinate ```xy2``` can be used and an infinite line that intersects both points will be drawn.

![img_301](./images/img_301.png)

```
fig = plt.figure(num=58, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y, c='royalblue', marker='o')

ax1.plot(0.5, 2.0, ls=None, c='aqua', marker='o')
ax1.axline(xy1=(0.5, 2.0), slope=2, c='tomato')

ax1.plot(1.5, 2.0, ls=None, c='lime', marker='o')
ax1.plot(4.5, 6.0, ls=None, c='lime', marker='o')
ax1.axline(xy1=(1.5, 2.0), xy2=(4.5, 6.0), c='hotpink')
```

![img_302](./images/img_302.png)

![img_303](./images/img_303.png)

The ```pyplot``` function and ```Axes``` method ```hlines``` or ```vlines``` can be used to draw multiple horizontal or vertical lines respectively:

![img_304](./images/img_304.png)

```hlines``` has the input argument ```y``` and the optional input arguments ```xmin``` and ```xmin```. Note that ```y``` is a ```tuple``` of y values in data co-ordinates. ```xmin``` and ```xmax``` also use data co-ordinates. ```vlines``` instead has ```x```, ```ymin``` and ```ymax```. Because there are multiple lines the keyword input arguments are slightly different, ```c``` cannot be used as an abbreviation for ```color``` as there is a singular version that specifies the color for all lines using a string and a plural version that individually specifies a color for each collection using a list of strings equal in length to the number of lines:

```
fig = plt.figure(num=59, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.plot(x, y, c='royalblue', marker='o')
ax1.hlines(y=(2, 4, 6), xmin=2, xmax=8, 
           colors=('orange', 'cyan', 'lime'))
ax1.vlines(x=(2, 4, 6), ymin=3, ymax=11, 
           color='magenta')
```

![img_305](./images/img_305.png)

![img_306](./images/img_306.png)

If the following are assigned to variables:

```
fig = plt.figure(num=60, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
lines = ax1.plot(x, y, c='royalblue', marker='o')
axvline = ax1.axvline(x=4, ymin=0.25, ymax=0.75, 
                      c='darkorange')
hlines = ax1.hlines(y=(2, 4, 6), xmin=2, xmax=8, 
                    colors=('orange', 'cyan', 'lime'))
```

![img_307](./images/img_307.png)

![img_308](./images/img_308.png)

Notice the difference:

```
lines
axvline
hlines
```

![img_309](./images/img_309.png)

```lines``` is a list of individual ```Line2D```, each ```Line2D``` is designed to be easily accessible from the list and can be altered independently. ```axvline``` is a ```Line2D``` and can be altered independently. ```hlines``` is a ```LineCollection``` and cannot be indexed independently. Instead the entire ```LineCollection``` has plural and sometimes singular style input arguments that can be altered. This can be seen by use of the ```pyplot``` function ```getp```:

```
plt.getp(hlines)
```

![img_310](./images/img_310.png)

## Scatter Plots

The ```plot``` function is by default configured for a lineplot. It can be used for a scatter plot by overriding the default ```ls``` from ```'-'``` to ```None``` and the ```marker``` default ```None``` to one of the markers previously discussed. 

There is also the function ```scatter``` which in contrast will create a scatter plot by default without a line. ```s``` is the size of the marker, it has a default value of ```30``` (although ```None``` is shown). The ```marker``` is the marker type and it has a default value of ```'c'``` corresponding to a circle (although ```None``` is shown). ```c``` corresponds to the colors of the markers and should be assigned to a ```tuple``` of color strings, equal in length to the number of data points. When a single color is used, the keyword ```color``` should instead be used which should be assigned to a single color string. Both ```s``` and ```c``` can be arrays that are of equal length to the data points:

![img_311](./images/img_311.png)

```
fig = plt.figure(num=61, figsize=None, dpi=None)
ax1 = fig.add_subplot(311)
points1 = ax1.scatter(x, y)
ax2 = fig.add_subplot(312)
points2 = ax2.scatter(x, y, 
                      s=30, color='tab:blue', 
                      marker='o')
ax3 = fig.add_subplot(313)
points3 = ax3.scatter(x, y, 
                      s=10*y, 
                      c=('tab:blue', 'tab:orange', 
                         'tab:green', 'tab:red', 
                         'tab:purple', 'tab:brown', 
                         'tab:pink', 'tab:gray',
                         'tab:olive','tab:cyan'),
                      marker='o')
```

![img_312](./images/img_312.png)

![img_313](./images/img_313.png)

The keyword ```linewidths``` can be assigned to a float scalar or an array of floats equal in length to the number of datapoints and changes the size of the line around each marker. There is an associated keyword ```ec``` which behaves similarly to ```c``` and is used for the edgecolor. The alpha keyword can be assigned to a normalised float or an array of normalised floats equal in length to the number of datapoints and changes the size of the line around each marker. 

```
fig = plt.figure(num=62, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
points1 = ax1.scatter(x, y, 
                      s=100, 
                      c='mediumpurple',
                      linewidths=(0.2, 0.4, 0.6, 0.8, 1.0, 
                                  1.2, 1.4, 1.6, 1.8, 2.0), 
                      ec='deepskyblue',
                      alpha=(0.1, 0.2, 0.3, 0.4, 0.5, 
                             0.6, 0.7, 0.8, 0.9, 1.0))
```

![img_314](./images/img_314.png)

![img_315](./images/img_315.png)

## Bar and Pie Plots

The ```pyplot``` function or ```Axes``` method ```bar``` can be used to create a bar graph. The bar plot requires the input arguments ```x``` which is typically a ```tuple``` of strings corresponding to the names of each bar. The input argument ```heights``` is also a ```tuple``` of equal length, containing the heights for each bar. There is also the input argument ```width``` which is set to a normalised floating point number. It is set to a default width of ```0.8``` which leaves some spacing between the bars, raising this to ```1.0``` will make all the bars touch:

![img_316](./images/img_316.png)

In this example ```x``` is a ```tuple``` of strings corresponding to the names fo four countries and ```height``` is a ```tuple``` of numeric values corresponding to the population of each country:

```
fig = plt.figure(num=63, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.bar(x=('Poland', 'Czechia', 'Hungary', 'Slovakia'), 
        height=(41.0, 10.51, 10.20, 5.80))
ax1.set_xlabel('Country')
ax1.set_ylabel('Population (millions)')
ax1.set_title('Countries')
ax1.grid(visible=True, which='major')
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
```

![img_317](./images/img_317.png)

![img_318](./images/img_318.png)

More countries will be added, so that there are 10 bars. Each bar can be customised with a ```color``` and a ```hatch```. Note only the singular keyword ```color``` is accepted, even though it is used in a plural context in this case. The most common use case for a bar graph is to use a singular value for all the bars. The plural ```colors``` or single letter ```c``` are not accepted. There are 10 main hatch styles. The hatch style is an escape string ```'\\'```, the first ```\``` indicates insertion of an escape character and the second ```\``` is the escape character to be inserted:

```
fig = plt.figure(num=64, figsize=(10, 5), dpi=None)
ax1 = fig.add_subplot(111)
ax1.bar(x=('Poland', 'Ukraine', 'Czechia', 'Hungary', 
           'Austria', 'Slovakia', 'Lithuania', 'Slovenia',
           'Latvia', 'Estonia'), 
            height=(36.7, 41.0, 10.51, 10.20, 
                    8.95, 5.80, 2.72, 2.12, 
                    1.83, 1.32),
            hatch=('*', '+', 'x', 'o', 
                   '.', 'O', '-', '|', 
                   '/', '\\'),
            color=('tomato', 'limegreen', 'darkorange', 'darkviolet',
                   'dodgerblue', 'violet', 'purple', 'aqua',
                   'olive', 'lightcoral'),
                   lw=2, ec='black')
ax1.set_xlabel('Country')
ax1.set_ylabel('Population (millions)')
ax1.set_title('Countries')
ax1.grid(visible=True, which='major')
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
ax1.xaxis.set_tick_params(rotation=45)
fig.tight_layout()
```

![img_319](./images/img_319.png)

![img_320](./images/img_320.png)

A stacked bar graph can be created by use of the ```bottom``` keyword and assigning it to the height of all the original bars. In this case, the projected population increase (positive) or decrease (negative) f0r 2050 can be plotted. For clairty the original bars won't be shown and the bottom ylimit will be set to ```0```:

```
fig = plt.figure(num=65, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
#ax1.bar(x=('Poland', 'Czechia', 'Hungary', 'Slovakia'), 
#        height=(41.0, 10.51, 10.20, 5.80))
ax1.bar(x=('Poland', 'Czechia', 'Hungary', 'Slovakia'), 
        height=(-2.85, 0.03, -1.40, -0.6),
        bottom=(41.0, 10.51, 10.20, 5.80),
        color='tomato')
ax1.set_xlabel('Country')
ax1.set_ylim(bottom=0)
ax1.set_ylabel('Population (millions)')
ax1.set_title('Countries')
ax1.grid(visible=True, which='major')
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
```

![img_321](./images/img_321.png)

![img_322](./images/img_322.png)

The previous bars can be shown:

```
fig = plt.figure(num=66, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.bar(x=('Poland', 'Czechia', 'Hungary', 'Slovakia'), 
        height=(41.0, 10.51, 10.20, 5.80))
ax1.bar(x=('Poland', 'Czechia', 'Hungary', 'Slovakia'), 
        height=(-2.85, 0.03, -1.40, -0.6),
        bottom=(41.0, 10.51, 10.20, 5.80),
        color='tomato')
ax1.set_xlabel('Country')
ax1.set_ylim(bottom=0)
ax1.set_ylabel('Population (millions)')
ax1.set_title('Countries')
ax1.grid(visible=True, which='major')
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
ax1.legend(labels=('2023', '2050'))
```

![img_323](./images/img_323.png)

![img_324](./images/img_324.png)

Because some of the data is negative, this representation can be misinterpretted i.e. the visualisation makes the 2023 population look lower and appears to represent population growth from 2023-2050 which is incorrect. In such a case, side by side bars will be more appropriate. When ```x``` is assigned to a string of labels, the xticks are automatically assumed to be integer values. This can be seen by examining the properties of the xaxis:

```
plt.getp(ax1.xaxis)
```

![img_325](./images/img_325.png)

Setting ```x``` explicitly to a ```tuple``` of integers, and ```width``` explictly to ```0.8``` gives the following plot:

```
fig = plt.figure(num=67, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.bar(x=(0, 1, 2, 3), 
        height=(41.0, 10.51, 10.20, 5.80),
        width=0.8, color='royalblue')
```

![img_326](./images/img_326.png)

![img_327](./images/img_327.png)

Note the first bar is centred at ```0``` and has a width of ```0.8``` and therefore spans from ```-0.4``` to ```0.4```, this can be changed to a narrower bar:

```
fig = plt.figure(num=68, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.bar(x=(0, 1, 2, 3), 
        height=(41.0, 10.51, 10.20, 5.80),
        width=0.4, color='royalblue')
ax1.bar(x=(0.4, 1.4, 2.4, 3.4), 
        height=(38.15, 10.54, 8.8, 5.1),
        width=0.4, color='tomato')
```

![img_328](./images/img_328.png)

![img_329](./images/img_329.png)

The xticks can be modified using:

```
ax1.xaxis.set_ticks((0.2, 1.2, 2.2, 3.2))
```

![img_330](./images/img_330.png)

![img_331](./images/img_331.png)

Then the labels can be added using:

```
ax1.xaxis.set_ticklabels(('Poland', 'Czechia', 'Hungary', 'Slovakia'))
```

![img_332](./images/img_332.png)

![img_333](./images/img_333.png)

The ```barh``` produces a horizontal bar chart. It uses similar input arguments however because it is horizontal, it uses ```y``` for the labels and there is a variation in ```width``` and constant ```height```:

```
fig = plt.figure(num=69, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.barh(y=('Poland', 'Czechia', 'Hungary', 'Slovakia'), 
        width=(41.0, 10.51, 10.20, 5.80),
        height=0.8, 
        color=('tomato', 'darkorange', 'darkviolet', 'dodgerblue'),
        hatch=('*', 'x', 'o', '.'),
        ec='black', lw=2)
ax1.set_xlabel('Population (millions)')
ax1.set_ylabel('Country')
ax1.set_title('Country')
ax1.grid(visible=True)
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
fig.tight_layout()
```

![img_334](./images/img_334.png)

![img_335](./images/img_335.png)

The bar plot wasn't assigned to a variable however they can be accessed from the ```Axes``` using its attribute ```containers``` which gives a list with 1 item in it:

```
ax1.containers
```

![img_336](./images/img_336.png)

The first index is the ```BarContainer```:

```
ax1.containers[0]
```

![img_337](./images/img_337.png)

The ```Axes``` methof ``bar_label``` can be used to label a bar graph or horizontal bar graph:

```
ax1.bar_label(container=ax1.containers[0])
```

![img_338](./images/img_338.png)

![img_339](./images/img_339.png)

Other data types can be accessed via the ```Axes``` plural attributes ```lines```, ```collections```, ```patches```, ```images```, ```tables```, ```texts``` and ```legend_```.

The data above can also be shown in a pie graph. The ```pyplot``` function or ```Axes``` method ```pie``` can be used to create a pie chart:

![img_340](./images/img_340.png)

It takes the input argument ```x``` which is the data used to create pie segments otherwise known as wedges, it is equivalent to the heights of the bars in a vertical bar graph although these are normalised in the pie chart. ```explode``` takes a ```tuple``` of normalised floating point numbers equal in length to the number of segments. An explode value of zero has each wedge placed in the middle and increasing the explode value drags the wedge out until it is off the edge of the ```Axes```. ```labels``` is a ```tuple``` of strings corresponding to the label for each wedge. Like the ```bar``` graph there is the input argument ```hatch``` which behaves analogously. There is also the input argument ```colors``` (notice that it is plural for a pie chart). The ```wedgeprops``` input argument is a dictionary that is typically used to set a conwtant value across all wedges:

```
fig = plt.figure(num=70, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.pie(x=(41.0, 10.51, 10.20, 5.80),
        explode=(0, 0.1, 0, 0.2),
        labels=('Poland', 'Czechia', 'Hungary', 'Slovakia'), 
        hatch=('*', 'x', 'o', '.'),
        colors=('tomato', 'darkorange', 'darkviolet', 'dodgerblue'),
        wedgeprops={'lw': 2, 'ec': 'black'})
```

![img_341](./images/img_341.png)

![img_342](./images/img_342.png)

## Histogram Plots

The ```pyplot``` function or ```Axes``` method ```hist``` can be used to create a histogram plot. Under the hood, the histogram plot is essentially a call to a bar graph so shares many of the keyword input arguments used to customise a bar graph. The input argument ```x``` is the data to be histogrammed. ```bins``` is an integer number of bins to be created. ```range``` is a ```tuple``` of start and stop values. The ```range``` keyword input argument should not be confused with the ```range``` class; however both behave similarly inclusive of the start bound and exclusive of the stop bound. The ```range``` class uses a step whereas the ```range``` input argument uses ```bins``` alongside the ```start``` and ```stop``` values provided to effectively calculate the step. 

![img_343](./images/img_343.png)

Supposing a dataset has the following numbers:

```
nums = (1.0, 1.2, 1.3, 2.3, 2.3, 2.4, 3.5, 3.4, 4.1, 4.2, 
        4.7, 5.1, 5.1, 5.5, 5.7, 5.7, 5.8, 5.9, 5.9, 5.9,
        6.1, 6.1, 6.1, 6.1, 6.2, 7.3, 7.4, 7.4, 7.4, 7.4,
        8.8, 8.8, 8.8, 8.8, 8.8, 9.2, 9.2, 9.2, 9.2, 9.9)
```

![img_344](./images/img_344.png)

The histogram plot can be created using ```10``` bins with a range between ```0``` and ```10```, in other words ```10``` bins starting from ```0``` and going up to but excluding ```10``` in steps of ```2```:

```
fig = plt.figure(num=71, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.hist(x=nums, bins=10, range=(0, 10),
         color='mediumseagreen',
         hatch='O',
         lw=2, ls='-', ec='k')
ax1.grid(visible=True)
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
ax1.set_xlabel('bins')
ax1.set_ylabel('frequency')
```

![img_345](./images/img_345.png)

![img_346](./images/img_346.png)

Since it is a small dataset, the number of datapoints lying in each bin can be physically counted by examining ```nums```.

The number of bins can be decreased to 5, which effectively combines every 2 bars:

```
fig = plt.figure(num=72, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.hist(x=nums, bins=5, range=(0, 10),
         color='mediumseagreen',
         hatch='O',
         lw=2, ls='-', ec='k')
ax1.grid(visible=True)
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
ax1.set_xlabel('bins')
ax1.set_ylabel('frequency')
```

![img_347](./images/img_347.png)

![img_348](./images/img_348.png)

## Box and Violin Plots

A distribution for example the ```tuple``` of floats ```nums``` can be categorised using quantiles, that is seperation of data into 4 parts. The central divider is the median value. The lower quantile and the upper quantile form a box around the median value and this box contains 50 % of datapoints. There is a whisker from the box to the lower and upper bounds, exclusive of outliers. The statistics module can be imported and the quantiles of ```nums``` examined:

```
import statistics as st
st.median(nums)
st.quantiles(data=nums, n=4, method='inclusive')
```

![img_349](./images/img_349.png)

The ```pyplot``` function or ```Axes``` method ```boxplot``` can be used to create a quantile plot which is otherwise known as a box plot:

![img_350](./images/img_350.png)

A box plot of ```nums``` can be created using:

```
fig = plt.figure(num=73, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.boxplot(x=nums)
ax1.grid(visible=True)
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
ax1.set_xlabel('bins')
ax1.set_ylabel('frequency')
```

![img_351](./images/img_351.png)

![img_352](./images/img_352.png)

A violin plot is similar but instead of a box, gives a kernel density estimation which gives more details about the shape of the distribution:

```
fig = plt.figure(num=74, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.violinplot(dataset=nums)
ax1.grid(visible=True)
ax1.minorticks_on()
ax1.grid(visible=True, which='minor', ls=':')
ax1.set_xlabel('bins')
ax1.set_ylabel('frequency')
```

![img_353](./images/img_353.png)

![img_354](./images/img_354.png)

## MatShow and PColor

A matrix can be created using:

```
xrow = np.linspace(-2, 2, 10)[np.newaxis, :]
ycol = np.linspace(-2, 2, 10)[:, np.newaxis]
xmat, ymat = np.meshgrid(xrow, ycol)
zdata_fun = lambda x, y: x * np.exp(-x**2 - y**2)
zmat = zdata_fun(x=xrow, y=ycol)
xarray = xmat.flatten()
yarray = ymat.flatten()
zarray = zmat.flatten()
```

```
fig = plt.figure(num=75, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.matshow(zmat)
ax1.set_xlabel('column')
ax1.xaxis.set_label_position('top') 
ax1.set_ylabel('row')
```








```
fig = plt.figure(num=76, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.pcolor(zmat)
ax1.set_xlabel('column')
ax1.set_ylabel('row')
```

```
fig = plt.figure(num=77, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
ax1.pcolor(xrow, ycol, zmat)
ax1.set_xlabel('column')
ax1.set_ylabel('row')
```

```
pcolor.cmap
```

```
colorbar = fig.colorbar(mappable=pcolor, ax=ax1, 
                        location='top')
```



```
fig = plt.figure(num=78, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
pcolor = ax1.pcolor(xrow, ycol, zmat,
                    cmap='viridis',
                    vmin=0, vmax=0.4)
ax1.set_xlabel('column')
ax1.set_ylabel('row')
colorbar = fig.colorbar(mappable=pcolor, ax=ax1)
```



```
fig = plt.figure(num=79, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
pcolor = ax1.pcolor(xrow, ycol, zmat,
                    cmap='viridis',
                    vmin=0, vmax=1.0)
ax1.set_xlabel('column')
ax1.set_ylabel('row')
colorbar = fig.colorbar(mappable=pcolor, ax=ax1)
```


```
fig = plt.figure(num=80, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
pcolor = ax1.pcolor(xrow, ycol, zmat,
                    cmap='viridis',
                    vmin=-0.4, vmax=0.4)
ax1.set_xlabel('column')
ax1.set_ylabel('row')
colorbar = fig.colorbar(mappable=pcolor, ax=ax1, 
                        orientation='horizontal')
```


```
plt.getp(pcolor)
```


```
plt.viridis
```

```
plt.cm.viridis
```

```
plt.setp(pcolor, cmap=plt.cm.jet)
```


```
plt.setp(pcolor, cmap=plt.cm.cividis)
```


```
plt.setp(pcolor, cmap=plt.cm.hot)
```


```
plt.setp(pcolor, cmap=plt.cm.magma)
```


```
plt.setp(pcolor, cmap=plt.cm.inferno)
```

A matrix can be created using:

```
xrow = np.linspace(-2, 2, 1000)[np.newaxis, :]
ycol = np.linspace(-2, 2, 1000)[:, np.newaxis]
xmat, ymat = np.meshgrid(xrow, ycol)
zdata_fun = lambda x, y: x * np.exp(-x**2 - y**2)
zmat = zdata_fun(x=xrow, y=ycol)
xarray = xmat.flatten()
yarray = ymat.flatten()
zarray = zmat.flatten()
```


```
fig = plt.figure(num=81, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
pcolor = ax1.pcolormesh(xrow, ycol, zmat,
                        cmap='jet',
                        vmin=-0.4, vmax=0.4)
ax1.set_xlabel('column')
ax1.set_ylabel('row')
colorbar = fig.colorbar(mappable=pcolor, ax=ax1, 
                        orientation='horizontal')
```


## Contour and Contourf

```
fig = plt.figure(num=82, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
contour = ax1.contour(xmat, ymat, zmat,
                      levels=(-0.4, -0.3, -0.2, -0.1, 0.0, 
                              0.1, 0.2, 0.3, 0.4),
                      cmap='jet')
ax1.set_xlabel('column')
ax1.set_ylabel('row')
colorbar = fig.colorbar(mappable=pcolor, ax=ax1, 
                        orientation='horizontal')
```


```
fig = plt.figure(num=83, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
contour = ax1.contourf(xmat, ymat, zmat,
                       levels=(-0.4, -0.3, -0.2, -0.1, 0.0, 
                              0.1, 0.2, 0.3, 0.4),
                       cmap='jet')
ax1.set_xlabel('column')
ax1.set_ylabel('row')
colorbar = fig.colorbar(mappable=pcolor, ax=ax1, 
                        orientation='horizontal')
```


```
fig = plt.figure(num=84, figsize=None, dpi=None)
ax1 = fig.add_subplot(111)
contour = ax1.contour(xmat, ymat, zmat,
                      levels=np.linspace(start=-0.4,
                                        stop=0.4,
                                        num=25),
                      cmap='jet')
ax1.set_xlabel('column')
ax1.set_ylabel('row')
colorbar = fig.colorbar(mappable=pcolor, ax=ax1, 
                        orientation='horizontal')
```

## Plot3D

```
fig = plt.figure(num=85, figsize=None, dpi=None)
ax1 = fig.add_subplot(111, projection='3d')
plot3d = ax1.plot3D(xarray, yarray, zarray)
```

## Wireframe and Surface

```
fig = plt.figure(num=86, figsize=None, dpi=None)
ax1 = fig.add_subplot(111, projection='3d')
plot3d = ax1.plot_surface(xrow, ycol, zmat)
```


```
fig = plt.figure(num=87, figsize=None, dpi=None)
ax1 = fig.add_subplot(111, projection='3d')
plot3d = ax1.plot_wireframe(xrow, ycol, zmat)
```

```
fig = plt.figure(num=88, figsize=None, dpi=None)
ax1 = fig.add_subplot(111, projection='3d')
plot3d = ax1.plot_wireframe(xrow, ycol, zmat,
                            color='tomato')
```


```
fig = plt.figure(num=88, figsize=None, dpi=None)
ax1 = fig.add_subplot(111, projection='3d')
plot3d = ax1.plot_surface(xrow, ycol, zmat, color='tomato')
```


```
fig = plt.figure(num=88, figsize=None, dpi=None)
ax1 = fig.add_subplot(111, projection='3d')
plot3d = ax1.plot_surface(xrow, ycol, zmat, cmap='jet')
```

## Contour and Countourf

```
fig = plt.figure(num=90, figsize=None, dpi=None)
ax1 = fig.add_subplot(111, projection='3d')
plot3d = ax1.contour3D(xmat, ymat, zmat,
                       levels=np.linspace(start=-0.4,
                                          stop=0.4,
                                          num=25),
                       cmap='jet')
```

```
fig = plt.figure(num=91, figsize=None, dpi=None)
ax1 = fig.add_subplot(111, projection='3d')
plot3d = ax1.contourf3D(xmat, ymat, zmat,
                        levels=np.linspace(start=-0.4,
                                           stop=0.4,
                                           num=25),
                        cmap='jet')
```



## ImShow










fig.colorbar(im, cax=ax.inset_axes([0, 1.05, 1, 0.05]),
             location='top')


