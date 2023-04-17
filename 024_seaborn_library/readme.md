# The Seaborn Library

Seaborn is a data visualisation library based upon ```matplotlib```. It has an appplication interface which simplifies the creation of complex but common visualisation plots from data contained within a ```pandas``` ```DataFrame``` instance. In theory all of the plots created by ```seaborn``` can be done directly in ```matplotlib``` but they would require much more lines of code.

## Importing Seaborn

The library name ```seaborn``` is derived from the two words Sea and Born. In this context the sea refers to a body of water i.e. a collection of data and born refers to the creation of the visualisation for that data. Like most of the other commonly used data science libraries it is common to import seaborn using a 3 letter abbreviation. The abbreviation ```sns``` is standard:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

![img_001](./images/img_001.png)

```sns``` comes from the fictional character Samual Norman Seaborn from the West Wing. His intiials were selected as the abbreviation by developers of the ```seaborn``` library as he has the sirname Seaborn.

Once imported the library version can be checked:

```
sns.__version__
```

![img_002](./images/img_002.png)

## Style

```seaborn``` is a wrapper library around ```matplotlib```. The ```matplotlib``` backend can be changed using:

```
%matplotlib qt5
```

![img_003](./images/img_003.png)

Some basic data can be created using ```numpy``` arrays:

```
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
```

![img_004](./images/img_004.png)

A simple line plot can be created using ```matplotlib```:

```
fig = plt.figure(num=1, figsize=None, dpi=None)
ax = fig.add_subplot(111)
ax.plot(x, y)
```

![img_005](./images/img_005.png)

The ```seaborn``` library has the function ```set_style``` which will change the default style for all ```matplotlib``` and by extension ```seaborn``` plots. Its docstring can be viewed by inputting ```sns.set_style()``` followed by a shift ```⇧``` and a tab ```↹```:

```
sns.set_style('whitegrid')
fig = plt.figure(num=2, figsize=None, dpi=None)
ax = fig.add_subplot(111)
ax.plot(x, y)
```

![img_007](./images/img_007.png)

![img_008](./images/img_008.png)

```
sns.set_style('darkgrid')
fig = plt.figure(num=3, figsize=None, dpi=None)
ax = fig.add_subplot(111)
ax.plot(x, y)
```

![img_009](./images/img_009.png)

![img_010](./images/img_010.png)

```
sns.set_style('white')
fig = plt.figure(num=4, figsize=None, dpi=None)
ax = fig.add_subplot(111)
ax.plot(x, y)
```

![img_011](./images/img_011.png)

![img_012](./images/img_012.png)

```
sns.set_style('dark')
fig = plt.figure(num=5, figsize=None, dpi=None)
ax = fig.add_subplot(111)
ax.plot(x, y)
```

![img_013](./images/img_013.png)

![img_014](./images/img_014.png)

## Palette

The ```seaborn``` function ```color_palette``` can be used to view the color palette:

```
sns.color_palette(palette='tab10')
```

![img_015](./images/img_015.png)

```
sns.color_palette(palette='pastel')
```

![img_016](./images/img_016.png)

```
sns.color_palette(palette='viridis')
```

![img_017](./images/img_017.png)

[Colormaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html)

The ```seaborn``` function ```set_palette``` can be used to set the default color palette used for subsequent plots:

```
sns.set_palette(palette='tab10')
```

![img_018](./images/img_018.png)

The following plot can be made with 15 lines:

```
fig = plt.figure(num=6, figsize=None, dpi=None)
ax = fig.add_subplot(111)
for num in range(15):
    ax.plot(x, y+num, lw=5)
```

![img_019](./images/img_019.png)

Since the color palette only has 10 colors and there are 15 lines, the additional 5 lines reuse the colors from the beginning of the palette:

![img_020](./images/img_020.png)

The ```seaborn``` function ```set_palette``` can be used to set the default color palette to ```'pastel'```:

```
sns.set_palette(palette='pastel')
```

![img_021](./images/img_021.png)

```
fig = plt.figure(num=7, figsize=None, dpi=None)
ax = fig.add_subplot(111)
for num in range(15):
    ax.plot(x, y+num, lw=5)
```

![img_022](./images/img_022.png)

![img_023](./images/img_023.png)

A custom palette can also be made using the seaborn function ```blend_palette``` and supplying the input argument ```colors``` which is usually a ```tuple``` of color strings, and ```n_colors``` which is an integer corresponding to the number of colors to be added to the palette:

```
bp = sns.blend_palette(colors=('tomato', 
                               'yellow', 
                               'darkseagreen', 
                               'royalblue'),
                       n_colors=10)
bp
```

![img_024](./images/img_024.png)

This custom palette can be set:

```
sns.set_palette(palette=bp)
```

![img_025](./images/img_025.png)

And will be used on a new plot:

```
fig = plt.figure(num=8, figsize=None, dpi=None)
ax = fig.add_subplot(111)
for num in range(15):
    ax.plot(x, y+num, lw=5)
```

![img_026](./images/img_026.png)

![img_027](./images/img_027.png)

The ```seaborn``` library has the dictionary ```xkcd_rgb``` which has color name keys and hexadecimal values for 954 of the most common rgb monitor colors:

```
sns.xkcd_rgb
```

![img_028](./images/img_028.png)

More details about these colors is available with the xkcd documentation:

[xkcd colors](https://xkcd.com/color/rgb/)

The ```seaborn``` method ```xkcd_palette``` can be used to create a color palette from these colors. This function requires every color in the palette to be specified as one of the corresponding key names in the ```xkcd_rgb``` dictionary:

```
xkcdp = sns.xkcd_palette(colors=('tomato red',
                                 'coral',
                                 'light plum',
                                 'cocoa',
                                 'yellowish', 
                                 'cool green',
                                 'faded green',
                                 'light teal',
                                 'faded blue',
                                 'cornflower blue'))
xkcdp
```

![img_029](./images/img_029.png)

The color palette can be set as the default:

```
sns.set_palette(palette=xkcdp)
```

![img_030](./images/img_030.png)

And will be used on a new plot:

```
fig = plt.figure(num=9, figsize=None, dpi=None)
ax = fig.add_subplot(111)
for num in range(15):
    ax.plot(x, y+num, lw=5)
```

![img_031](./images/img_031.png)

![img_032](./images/img_032.png)

There are a number of functions such as ```choose_diverging_palette```, ```choose_light_palette```, ```choose_dark_palette```, ```choose_colorbrewer_palette```, ```choose_cube_helix_palette```, and ```choose_cubehelix_palette``` which use interactive Python widgets for a customisable color palette: 

```
dp = sns.choose_diverging_palette()
```

![img_033](./images/img_033.png)

Changing the values on the sliders will recreate an inline plot. When the qt5 backend is enabled, it doesn't update the plot in the existing figure but instead creates a new figure and in my case produced 20 plots as I moved only one fo the sliders upwards:

![img_034](./images/img_034.png)

The diverging palette can be selected:

```
sns.set_palette(palette=dp)
```

![img_035](./images/img_035.png)

And will be used on a new plot:

```
fig = plt.figure(num=11, figsize=None, dpi=None)
ax = fig.add_subplot(111)
for num in range(15):
    ax.plot(x, y+num, lw=5)
```

![img_036](./images/img_036.png)

## Plot Configuration

The plot configuration options are normally specified at the top of the notebook after importing the scientific libraries:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib qt5
sns.set_style('whitegrid')
sns.set_palette(palette='tab10')
```

![img_037](./images/img_037.png)

## Pandas DataFrame

The ```seaborn``` plotting functions generally assume the data is contained within an instance of the ```pandas``` class ```DataFrame```. The ```DataFrame``` instance for the simple plot types should generally have a numeric ```Series``` instance corresponding to $x$ and a numeric ```Series``` instance corresponding to $y$. For example:

```
df = pd.DataFrame(data={'x': np.arange(0, 11, 1),
                        'y': np.arange(0, 22, 2)})
```

![img_038](./images/img_038.png)

The ```DataFrame``` method ```head``` can be called from the instance ```df```:

```
df.head()
```

![img_039](./images/img_039.png)

The data type can be tested using the ```DataFrame``` attribute ```dtype```:

```
df.dtype
```

![img_040](./images/img_040.png)

If the ```DataFrame``` instance ```df``` has a categorical ```Series``` it can be used to plot subsets of the data using the category. A ```bool``` ```Series``` instance can be made, which in this case checks if the $x$ value is even:

```
df['x'].head() % 2
```

```
df['x'].head() % 2 == 0
```

```
df['parity'] = df['x'] % 2 == 0
```

![img_041](./images/img_041.png)

This ```Seires``` instance can have its type changed to category and these categories can be renamed:

```
df['parity'] = df['parity'].astype('category')
```

```
df['parity'] = df['parity'].cat.rename_categories({True: 'even',
                                                   False: 'odd'})
```

![img_042](./images/img_042.png)

The ```DataFrame``` instance ```df``` head can be checked:

```
df.head()
```

![img_043](./images/img_043.png)

The ```DataFrame``` instance ```df``` datatypes can be checked:

```
df.dtypes
```

![img_044](./images/img_044.png)

The ```DataFrame``` instance ```df``` information can be checked:

```
df.info()
```

![img_045](./images/img_045.png)

The ```DataFrame``` instance ```df``` description can be checked which gives statistical details about only the numeric data:

```
df.describe()
```

![img_046](./images/img_046.png)

## Seaborn Example Datasets

For convenience a number of practice datasets in the form of ```DataFrames``` instances are inbuilt into ```seaborn```. The names of these datasets can be accessed by using the ```seaborn``` function ```get_dataset_names```:

```
sns.get_dataset_names()
```

![img_047](./images/img_047.png)

A dataset can be loaded using the ```seaborn``` function ```load_dataset``` and providing the ```name``` of the dataset as a string. The loaded dataset is a ```DataFrame``` instance.

### Flights Dataset

The flights dataset for example can be loaded using:

```
flights = sns.load_dataset(name='flights')
```

![img_048](./images/img_048.png)

The ```DataFrame``` instance ```flights``` head can be checked:

```
flights.head()
```

![img_049](./images/img_049.png)

```
flights.dtypes
```

```
flights.shape
```


```
flights.info()
```

```
flights.describe()
```


### Exercise Dataset

```
exercise = sns.load_dataset(name='exercise')
```

```
exercise.head()
```


```
exercise.dtypes
```


```
exercise.shape
```



```
exercise.info()
```

### Tips Dataset

```
tips = sns.load_dataset(name='tips')
```

```
tips.head()
```



```
tips.dtypes
```


```
tips.shape
```


```
tips.info()
```

### Taxis Dataset

```
taxis = sns.load_dataset(name='taxis')
```

```
taxis.head()
```



```
taxis.dtypes
```


```
taxis.shape
```


```
taxis.info()
```


### Iris Dataset


```
iris = sns.load_dataset(name='iris')
```

```
iris.head()
```



```
iris.dtypes
```


```
iris.shape
```


```
iris.info()
```

### Penguins Dataset


```
penguins = sns.load_dataset(name='penguins')
```

```
penguins.head()
```



```
penguins.dtypes
```


```
penguins.shape
```


```
penguins.info()
```




## Seaborn Syntax

The ```seaborn``` plot functions are setup to expect data from a dataframe. The first few input arguments relate to the data and the other keyword arguments are optional, meaning if they are unspecified, the plot is carried out using the default values.

The docstring of ```sns.lineplot()```


```
fig = plt.figure(num=11, figsize=None, dpi=None)
sns.lineplot(data=df, x='x', y='y')
```


```
fig = plt.figure(num=12, figsize=None, dpi=None)
sns.scatterplot(data=df, x='x', y='y')
```

```
fig = plt.figure(num=13, figsize=None, dpi=None)
sns.scatterplot(data=df, x='x', y='y', hue='parity')
```


```
fig = plt.figure(num=14, figsize=None, dpi=None)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
```


```
fig.sca(ax1)
sns.lineplot(data=df, x='x', y='y')
fig.sca(ax2)
sns.scatterplot(data=df, x='x', y='y', hue='parity')
fig.sca(ax3)
sns.swarmplot(data=df, x='x', y='y', hue='parity')
fig.sca(ax4)
sns.stripplot(data=df, x='x', y='y', hue='parity')
```


```
fig = plt.figure(num=15, figsize=None, dpi=None)
ax1 = fig.add_subplot(221)
sns.lineplot(data=df, x='x', y='y')
ax2 = fig.add_subplot(222)
sns.scatterplot(data=df, x='x', y='y', hue='parity')
ax3 = fig.add_subplot(223)
sns.swarmplot(data=df, x='x', y='y', hue='parity')
ax4 = fig.add_subplot(224)
sns.stripplot(data=df, x='x', y='y', hue='parity')
```









