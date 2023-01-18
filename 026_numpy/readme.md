# The Numeric Python Library - numpy

The Numeric Python library - ```numpy``` is the most commonly used data science library. Moreover other popular data science libraries such as the Python and Data Analysis Library - ```pandas```, the Matrix Plotting Library - ```matplotlib``` and the Data Visualization Library - ```seaborn``` are based upon ```numpy```.

## Scalability in Python

The following data structures have been explored in inbuilt Python and Python standard modules:

* list - collection of mixed datatypes
* array - 1d uniform data structure
* nested lists

These data structures are collections and their datamodel methods are setup as collections.

The following mathematical concepts have also been explored:

* numeric datamodel methods for int, float and bool classes
* range objects
* math and complex module
* statistics module
* datetime module
* random module

Most of these mathematical concepts have been constrained to a scalar variable (that is a variable with a single element). To scale the operations to multiple dimensions list comprehensions and loops have been used.

## N-Dimensional Array

The numeric Python Library is based upon the n-dimensional array ```ndarray``` data structure. The ```ndarray``` bridges the features mentioned above over multiple dimensions using simple succinct syntax. 

The numpy library is therefore a very large Python library. Despite it being large, previous tutorials have established a vigourous understanding of how each of these features operates over a single dimension using builtin Python or a standard Python module. Once the mechanics of using a ndarray are setup, such as indexing and working across multiple dimensions, this previous knowledge can easily be applied. It becomes a case of using the equivalent function from the numpy library to act on the ndarray(s) or the equivalent ndarray method.

## Importing numpy

The ```numpy``` library is typically imported using a 2 letter abbreviation ```np```. The numpy library includes a large number of functions and it is more convenient to access these using this two letter abbreviation:

```
import numpy as np
```

![img_001](./images/img_001.png)

```numpy``` is a third-party Python library. If it has not been installed, a ```ModuleNotFoundError``` will display.

![img_002](./images/img_002.png)

To setup a Python Environment with the Scientific Libraries, it is recommended to use Mambaforge and the ```mamba``` package manager. See [Python Installation Windows, Linux and Mac](https://github.com/PhilipYip1988/python-tutorials/blob/main/001_install/readme.md)

Once imported, the module datamodel attributes ```__name__```, ```__version__``` and ```__path__``` can be examined:

```
np.__name__
np.__version__
np.__path__
```

The version should be ```>=``` ```1.24.1```

![img_003](./images/img_003.png)

Once imported a large number of identifiers will be listed by inputting ```np.``` followed by a tab ```↹```:

![img_004](./images/img_004.png)

## ndarray Factory Functions

The n-dimensional array ```ndarray``` class is the data structure the ```numpy``` library is based around. The init signature is long and can be output into a cell using:

```
? nd.ndarray
```

![img_005](./images/img_005.png)

The docstring states: Arrays should be constructed using the ```array``` factory function.

The docstring also gives some import parameters for array creation:

|parameter|description|
|---|---|
|shape|tuple of ints representing the shape of the created array.|
|dtype|data-type, optional object that can be interpreted as a numpy data type.|
|order|{'C', 'F'}, optional Row-major (C-style) or column-major (Fortran-style) order.|

And important attributes of an ```ndarray```:

|attribute|description|
|---|---|
|size|int number of elements in the array|
|ndim|int number of dimensions of the array|
|shape|tuple of ints representing the shape of the array.|
|T|transpose of the array.|
|flat|flattened version of the array as an iterator.|
|real|real part of the array.|
|imag|imaginary part of the array.|
|data|the elements array in memory.|
|itemsize|the memory use of each array element in bytes.|
|nbytes|the total number of bytes required to store the array data, data * itemsize|

The ```array``` factory function is used to create a new ```ndarray``` from an existing object. Its docstring can be viewed as a pop up balloon by inputting ```np.array()``` followed by shift ```⇧``` and tab ```↹```:

![img_006](./images/img_006.png)

This is once again quite a long docstring so it is worthwhile examining it in a cell output using:

```
? np.array
```

![img_007](./images/img_007.png)

Normally only the ```object``` is supplied to the ```np.array``` factory function. 

|parameter|description|
|---|---|
|object|any (nested) sequence, usually a list.|
|dtype|data-type, optional object that can be interpreted as a numpy data type.|
|copy|if true (default), then the object is copied.|
|ndmin|specifies the minimum number of dimensions that the resulting array should have. Ones will be prepended to the shape to satisfy this requirement|

Sometimes a custom ```dtype``` is supplied but most of the time this is not supplied and the factory automatically determines the best datatype from the input data. 

The ```copy``` bool is normally set to ```True```, this prevents unwanted mutability of the output ```ndarray``` if the supplied ```object``` is mutated. 

The ```ndmin``` can be useful when creating higher dimensional arrays.

The docstring also includes details about other factory functions to create an ```ndarray```:

|factory function|description|
|---|---|
|empty_like|Return an empty array with shape and type of input.|
|ones_like|Return an array of ones with shape and type of input.|
|zeros_like|Return an array of zeros with shape and type of input.|
|full_like|Return a new array with shape of input filled with value.|
|empty| Return a new uninitialized array.|
|ones|Return a new array setting values to one.|
|zeros|Return a new array setting values to zero.|
|full|Return a new array of given shape filled with value.|

A ```ndarray``` can specifically be created from a ```list``` using:

```
list1 = [1, 2, 3, 4]
list1

array1 = np.array(object=list1)
array1
```

![img_008](./images/img_008.png)

This is normally done directly and using a positional input argument:

```
array1 = np.array([1, 2, 3, 4])
array1
```

![img_009](./images/img_009.png)

Dimensionality details about this ```ndarray``` can be found using the attributes ```size```, ```ndim``` and ```shape``` respectively:

```
array1.size
array1.ndim
array1.shape
```

![img_010](./images/img_010.png)

The ```size``` is ```4``` as there are 4 elements in the array. The number of dimensions ```ndim``` is ```1``` and the ```shape``` is a ```tuple``` with value ```(4,)```. 

A 1d array is known as a *vector*. Note the shape tuple states that this *vector* only has ```4``` *columns*. 

Care should be taken regarding the dimensionality in a ```ndarray```. It does not behave like a ```list``` which can be represented as either a row or column for convenience:

```
list1 = [1, 2, 3, 4]
list1

list1 = [1, 
         2, 
         3, 
         4]
list1
```

![img_011](./images/img_011.png)

A 1d array or *vector* should be distiguished from a 2d array known as a *2d row vector*, a *2d row vector* by definition has 1 row by multiple columns.

Sometimes it is required to specifically create a *2d row vector* as dimensionality can be important in array operations. This can be done by providing the ```ndmin``` keyword input argument and assigning it to ```2``:

```
arrayr = np.array([1, 2, 3, 4], ndmin=2)
arrayr
arrayr.size
arrayr.ndim
arrayr.shape
```

The ```size``` is still ```4``` as there are 4 elements in the array. The number of dimensions ```ndim``` is now ```2``` and the ```shape``` is a ```tuple``` with value ```(4, 1)```. This shape tuple represents 4 columns and 1 row:

![img_012](./images/img_012.png)

Compare:

```
array1.ndim
array1.shape

array1.ndim
arrayr.shape
```

![img_013](./images/img_013.png)

|ndim|shape|
|---|---|
|1|(4,)|
|2|(1, 4)|

The 1d array or *1d vector* has a single dimension that spans over 4 columns.

The 2d array or *2d row vector*, has 1 row and 4 columns.

|ndim|shape|
|---|---|
|1|(4 columns,)|
|2|(1 row, 4 columns)|

Notice that in the ```shape``` ```tuple``` the new dimension is left appended, this makes sense as the origin of the new dimension is the outer list:

```
column = [1, 2, 3, 4]
row = [column]
row
```

![img_014](./images/img_014.png)

The ```shape``` ```tuple``` can be indexed to retrieve the number of columns for the 1d vector and the 2d row vector and the number of rows for the 2d row vector:

```
array1_cols = array1.shape[0]
array1_cols

arrayr_rows = arrayr.shape[0]
arrayr_rows

arrayr_cols = arrayr.shape[1]
arrayr_cols
```

![img_015](./images/img_015.png)

Since the new dimension is left appended, the positive index used in the ```shape``` ```tuple``` to retrieve the column increases as the number of dimensions increases. 

On the other hand, if the negative index is used, i.e. indexing from the right. An index of ```-1``` always corresponds to the columns and ```-2``` always corresponds to the rows:

```
array1_cols = array1.shape[-1]
array1_cols

arrayr_rows = arrayr.shape[-1]
arrayr_rows

arrayr_cols = arrayr.shape[-2]
arrayr_cols
```

![img_016](./images/img_016.png)

Sometimes it is required to specifically create a *2d column vector* as dimensionality. The easiest way to do this is by creating the equivalent row vector and using the transpose attribute ```T``` to transpose it. Transposing a 2D array switches the row and column indices:

```
arrayc = np.array([1, 2, 3, 4], ndmin=2).T
arrayc
arrayc.size
arrayc.ndim
arrayc.shape
```

![img_017](./images/img_017.png)

When every value in the input list, is a list of integers, the datatype will automatically be assumed to be an integer:

```
array1 = np.array([1, 2, 3, 4])
array1
array1.dtype
```

![img_018](./images/img_018.png)

If one of these datatypes is updated to a floating point number, the datatype of the array will be assumed to be floating point:

```
array1 = np.array([1., 2, 3, 4])
array1
array1.dtype
```

![img_019](./images/img_019.png)

If one of these datatypes is updated to a complex number, the datatype of the array will be assumed to be complex:

```
array1 = np.array([1=2j, 2, 3, 4])
array1
array1.dtype
```

![img_020](./images/img_020.png)

If all of the datatypes are boolean, the datatype of the array will be assumed to be boolean:

```
array1 = np.array([True, False, False, False])
array1
array1.dtype
```

![img_021](./images/img_021.png)

In some cases it is more convenient to specify the datatype using the keyword input argument ```dtype``` and assigning it to ```builtins``` classes ```bool```, ```int```, ```float```, or ```complex```:

```
array1 = np.array([1, 2, 3, 4], dtype=float)
array1
array1.dtype
```

![img_022](./images/img_022.png)

There are also corresponding ```int```, ```float```, or ```complex``` classes available in the ```numpy``` library. The numbers 8, 16, 32, 64, 128 correspond to the number of bytes used to store each individual number in the array, these are typically only used for application with very large arrays to optimise memory management:

![img_023](./images/img_023.png)

![img_024](./images/img_024.png)

![img_025](./images/img_025.png)

```int_```, ```float_```, or ```complex_``` act as alias for ```int32```, ```float64``` and ```complex128```. These are the defaults used when the ```int```, ```float```, or ```complex``` classes are selected from builtins:

![img_026](./images/img_026.png)

A 2d array is known as a matrix and can be formed when the ```object``` is a list of equally sized lists:

```
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])
matrix1
matrix1.size
matrix1.ndim
matrix1.shape
```

![img_027](./images/img_027.png)

Notice that the ```size``` is ```6```, the number of dimensions ```ndim``` is ```2``` and the ```shape``` ```tuple``` is ```(2, 3)``` i.e. 2 rows by 3 columns as expected.

The other factory functions ```empty_like```, ```ones_like```, ```zeros_like``` and ```fulls_like``` can be used on this matrix:

```
matrix2 = np.empty_like(prototype=matrix1)
matrix2

matrix3 = np.zeros_like(a=matrix1)
matrix3

matrix4 = np.ones_like(a=matrix1)
matrix4

matrix5 = np.full_like(a=matrix1, fill_value=2)
matrix5
```

![img_028](./images/img_028.png)

All four of these factory functions have the positional input argument ```a``` which is the original array that the shape is extracted from, ```empty_like``` is inconsistent and calls this positional input argument ```prototype```. The ```empty_like``` factory function retrieves garbage values, it is normally better to use ```zeros_like``` factory function instead. The ```full_like``` factory function requires a ```fill_value``` as a second positional input argument. All four of these factory functions will take the datatype from the original array but have an input argument ```dtype``` which can be overridden to a custom datatype. All four of these factory functions will take the shape from the original array but have an input argument ```shape``` which can be overridden to a custom tuple of integers. This is not commonly done as the related factory functions ```empty```, ```zeros```, ```ones``` and ```full``` are more convenient for this use case. 

```
matrix2 = np.empty(shape=(4, 3))
matrix2

matrix3 = np.zeros(shape=(4, 3))
matrix3

matrix4 = np.ones(shape=(4, 3))
matrix4

matrix5 = np.full(shape=(4, 3), fill_value=4)
matrix5
```

![img_029](./images/img_029.png)

The datatype for ```empty```, ```zero```, ```ones``` is ```float``` by default but can be overridden with the ```dtype``` keyword input argument. The datattype for the ```full``` function is inferred by the ```fill_value``` but can be overridden using the keyword input argument ```dtype```.

It is possible to construct higher dimension arrays, however it becomes difficult to visualise arrays that have a higher dimension than the computer screen. For this reason it is worthwhile conceptualising some physical objects:

|ndim|description|shape|
|---|---|---|
|1|line vector|(c, )|
|2|page consisting of rows of equal length line vectors|(r, c)|
|3|book of equally sized pages|(b, r, c)|
|4|shelf of equally sized books|(s, b, r, c)|
|5|wardrobe of equally sized shelves|(w, s, b, r, c)|
|6|library of equally sized wardrobes|(l, w, s, b, r, c)|
|7|group of equally sized libraries|(g, l, w, s, b, r, c)|

A book can therefore be constructed from a list, of lists, of equally sized lists:

```
book1 = np.array([[[1, 2,], 
                   [3, 4]],
                  
                  [[5, 6], 
                   [7, 8]],
                  
                  [[9, 10], 
                   [11, 12]]])
book1

book1.size
book1.ndim
book1.shape
```

![img_030](./images/img_030.png)

## ravel and reshape

An array has the attributes ```size```, ```ndim``` and ```shape```. The dimensionality of an array can be lost when the ```flat``` attribute is used. The ```flat``` attribute``` creates an iterator which has no dimensionality:

```
it = book1.flat
it

next(it)
next(it)
next(it)
next(it)
next(it)
list(it)
```

![img_031](./images/img_031.png)

Notice that the array is deconstructed in row order, meaning each consecutive row is essentially concentenated. This can be seen by consuming the iterator by casting it to a ```list```. Then using this ```list``` as the ```object``` with the ```np.array``` factory function:

```
it = book1.flat
it

array1 = np.array(list(it))
array1
```

![img_032](./images/img_032.png)

The associated method, ```flatten``` carries out the above in a single step:

```
array1 = np.flatten(book1)
```

![img_033](./images/img_033.png)

It is also possible to ravel an array, which is the same process as flattening but doesn't involve use of the ```ndarray``` iterator attribute ```flat```. For this there is a ```ravel``` function in the ```numpy``` library alongside a complementary method ```ravel``` which can called from an ```ndarray```. In ```numpy``` most ```numpy``` functions which operate on a ```ndarray``` have a complementary ```ndarray``` method.

```
array1 = book1.ravel()
array1

array1 = np.ravel(book1)
array1
```

![img_034](./images/img_034.png)

The ```ravel``` function can also be used on other sequences such as a list of lists:

```
booklist1 = [[[1, 2,], 
              [3, 4]],
                  
              [[5, 6], 
               [7, 8]],
                  
              [[9, 10], 
               [11, 12]]]

booklist1

array1 = np.ravel(booklist1)
array1
```

![img_035](./images/img_035.png)

The inbuilt ```list``` class can be used to cast the ravelled ```ndarray``` back to a list. There is also an associated ```ndarray``` method ```tolist```:

```
list(array1)
array1.tolist()
```

![img_036](./images/img_036.png)

The ```numpy``` function and ```ndarray``` method ```ravel``` have the keyword input argument ```order```. The ```order``` is assigned to a string that is ```'C'``` (default) or ```'F'``` which stand for the C (row-major) and Fortran (column-major) programming languages respectively. **Do not confuse C with column.**

```
booklist1 = [[[1, 2,], 
              [3, 4]],
                  
              [[5, 6], 
               [7, 8]],
                  
              [[9, 10], 
               [11, 12]]]

booklist1

np.ravel(booklist1, order='F')
```

![img_037](./images/img_037.png)

Comparison of the 2 unravelled arrays shows that it is far more logical to use the default ```'C'`` (row-order).

An ```ndarray``` can also be reshaped to new dimensions, providing that the ```size``` of the new dimensions matches the ```size``` of the original dimensions. The original ```ndarray``` is essentially ravelled and each element is then used to populate the new dimensions. Once again there is the ```numpy``` function ```reshape``` and the ```ndarray``` method ```reshape```:

```
matrix1 = np.reshape(a=book1, newshape=(4, 3))
matrix1

matrix1 = book1.reshape((4,3))
matrix1
```

![img_038](./images/img_038.png)

## Indexing and Slicing

The following matrix:

$$\text{matrixlist1}=\left[\begin{matrix}1&2&3\\4&5&6\\7&8&9\\10&11&12\end{matrix}\right]$$

Can be represented as a list of lists:

```
matrixlist1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [10, 11, 12]]
```

And more explicitly as:

```
row0 = [1, 2, 3]
row1 = [4, 5, 6]
row2 = [7, 8, 9]
row3 = [10, 11, 12]

matrixlist1 = [row0,
               row1,
               row2,
               row3]
```

Supposing the following ```2``` is a scalar value of interest:

$$\text{matrixlist1}=\left[\begin{matrix}1&\textbf{2}&3\\4&5&6\\7&8&9\\10&11&12\end{matrix}\right]$$


To retrieve this scalar value, ```matrixlist1``` must be indexed, and a square set of brackets is used to select the row, which is ```row0``` at index ```0```:

```
matrixlist1[0]
```

Now that this row is selected, it must also be indexed. A second set of square brackets is used to select the column, which is the column at index ```1```:

```
matrixlist1[0][1]
```

![img_039](./images/img_039.png)

For an equivalent numpy array:

```
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])
```

Indexing can be carried out in a similar manner:

```
matrix1[0][1]
```

However as the ```ndarray``` is setup to be a n dimensional structure, there is simpler syntax, which involves a single set of square brackets and use of a ```,``` as a delimiter. This simpler syntax does not work with a list of lists as the list data structure is not setup to be n dimensional:

```
matrix1[0, 1]
```

![img_040](./images/img_040.png)

Notice that the form of the square bracket, has a similar form to the ```shape``` ```tuple```. Indexing a scalar value from a higher dimension array follows the same trend as the ```shape``` ```tuple```:

|ndim|description|indexing|
|---|---|---|
|1|line vector|array1d[c, ]|
|2|page consisting of rows of equal length line vectors|array2d[r, c]|
|3|book of equally sized pages|array3d[b, r, c]|
|4|shelf of equally sized books|array4d[s, b, r, c]|
|5|wardrobe of equally sized shelves|array5d[w, s, b, r, c]|
|6|library of equally sized wardrobes|array6d[l, w, s, b, r, c]|
|7|group of equally sized libraries|array7d[g, l, w, s, b, r, c]|

Multiple values can be selected from the array by indexing using a list. This outputs an ```ndarray```:

$$\text{matrix1}=\left[\begin{matrix}1&\textbf{2}&3\\\textbf{4}&5&6\\7&8&9\\10&11&12\end{matrix}\right]$$

The scalar ```2``` is on row ```0``` and column ```1```.

The scalar ```4``` is on row ```1``` and column ```0```.

```
matrix1[[0, 1], [1, 0]]
```

![img_041](./images/img_041.png)

Supposing all of the items are along an axis, for example row 0, all columns:

$$\text{matrix1}=\left[\begin{matrix}\textbf{1}&\textbf{2}&\textbf{3}\\4&5&6\\7&8&9\\10&11&12\end{matrix}\right]$$

This can be indexed explicitly using two lists:

```
matrix1[[0, 0, 0], [0, 1, 2]]
```

For short hand, a scalar value can be used the row:

```
matrix1[0, [0, 1, 2]]
```

![img_042](./images/img_042.png)

To select all columns slicing can be used. Recall that the ```colon``` is used for slicing. Specifically with the form ```start:stop:step```, the ```start``` ```stop``` and ```step``` values can explictly be specified:

```
matrix1[0, 0:matrix1.shape[1]:1]
```

If they are not, the default values will be taken, that is ```start=0```, ```stop=array.shape[n]``` where ```array``` is the array name and ```n``` is the dimension and ```step=1```:

```
matrix1[0, ::]
```

If the second colon is not specified, it is assumed ```step=1```:

```
matrix1[0, :]
```

![img_043](./images/img_043.png)

Indexing is also possible using a negative step:

```
matrix1[0, -1:-matrix1.shape[1]-1:-1]
```

Use of a negative step will change the default ```start=-1``` and ```stop=-array.shape[n]-1``` where once again ```array``` is the array name and ```n``` is the dimension and ```step=1```.

![img_044](./images/img_044.png)

Since it is easier to conceptualise a matrix on a computer screen. Higher order arrays are often constructed using the zeros function and then populated by slicing and assigning the slice to a matrix. For example the following 3darray ```book``` can be created using:

```
book = np.zeros(shape=(3, 4, 3))
book

book.size
book.ndim
book.shape
```

![img_052](./images/img_052.png)

The data for a single page can be constructed as a matrix:

```
page0 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])
page0

page0.size
page0.ndim
page0.shape
```

![img_053](./images/img_053.png)

Notice that ```book0.shape[-1]``` and ```page0.shape[-1]``` match meaning the number of columns is the same. Also ```book0.shape[-2]``` and ```page0.shape[-2]``` match meaning the number of rows is the same.

The other two pages can be created using:

```
page1 = np.array([[13, 14, 15],
                  [16, 17, 18],
                  [19, 20, 21],
                  [22, 23, 24]])
page1
page2 = np.array([[25, 26, 27],
                  [28, 29, 30],
                  [31, 32, 33],
                  [34, 35, 36]])
page2
```

![img_054](./images/img_054.png)

Now ```page0``` can be added to ```book``` by slicing the ```book``` and assigning the value to the matrix ```page0```:

```
book[0, :, :] = page0
book
```

![img_055](./images/img_055.png)

This can be done for the other pages:

```
book[1, :, :] = page1
book[2, :, :] = page2
book
```

![img_056](./images/img_056.png)

## axis, flip, fliplr, flipud

A matrix can be left right flipped by indexing with rows=```:``` and columns=```::-1```

$$\text{matrix1}=\left[\begin{matrix}1&2&3\\4&5&6\\7&8&9\\10&11&12\end{matrix}\right]$$

$$\text{matrix1\_lr}=\left[\begin{matrix}3&2&1\\6&5&4\\9&8&7\\12&11&10\end{matrix}\right]$$

```
matrix1_lr = matrix1[:, ::-1]
matrix1_lr
```

![img_045](./images/img_045.png)

There is an associated ```fliplr``` ```numpy``` function:

```
matrix1_lr = np.fliplr(m=matrix1)
matrix1_lr
```

![img_046](./images/img_046.png)

And there is an associated ```flip``` ```numpy``` function. This function has the keyword input argument ```axis``` which is a common parameter for ```numpy``` functions.

When flipping left right using indexing, the following operation ```matrix1[:, ::-1]``` was carried out. All rows were selected and the flipping operation was carried out on the columns, therefore the column axis should be selected. Since a matrix is a 2darray the rows are ```axis=0``` and the columns are ```axis=1```.

```
matrix1_lr = np.flip(m=matrix1, axis=-1)
matrix1_lr
```

![img_047](./images/img_047.png)

Recall when the number of dimensions in the ```shape``` ```tuple``` were discussed, that the new dimension is left appended. This means the ```axis``` positive value of the columns will increase by 1 for each dimension. On the other hand the negative value will always be ```-1``` and it is therefore recommended to use the negative value for the sake of consistency.

|ndim|description|indexing|
|---|---|---|
|1|line vector|array1d[c, ]|
|2|page consisting of rows of equal length line vectors|array2d[r, c]|
|3|book of equally sized pages|array3d[b, r, c]|
|4|shelf of equally sized books|array4d[s, b, r, c]|
|5|wardrobe of equally sized shelves|array5d[w, s, b, r, c]|
|6|library of equally sized wardrobes|array6d[l, w, s, b, r, c]|
|7|group of equally sized libraries|array7d[g, l, w, s, b, r, c]|

![img_048](./images/img_048.png)

A matrix can be up down flipped by indexing with rows=```::-1``` and columns=```:```. The flipping operation this time is carried out on the ```axis``` of the rows, therefore the ```numpy``` function ```flip``` can be used with ```axis=0``` in the case of a 2d array or more generally ```axis=-2``` for any dimension of array that has rows, to achieve the same operation. There is also the associated ```numpy``` function ```flipud```:

$$\text{matrix1}=\left[\begin{matrix}1&2&3\\4&5&6\\7&8&9\\10&11&12\end{matrix}\right]$$

$$\text{matrix1\_ud}=\left[\begin{matrix}10&11&12\\7&8&9\\4&5&6\\1&2&3\end{matrix}\right]$$

```
matrix1_ud = matrix1[::-1, :]
matrix1_ud

matrix1_ud = np.flipud(m=matrix1)
matrix1_ud

matrix1_ud = np.flip(m=matrix1, axis=-2)
matrix1_ud
```

![img_049](./images/img_049.png)

## Transposing

The ```T``` attribute and complementary ```numpy``` function ```transpose``` an be used to transpose an array. 

This is typically used most for 2d arrays for example 2d row vectors can be transposed into 2d column vectors or vice versa: 

$$\text{arrayr}=\left[\begin{matrix}1&2&3&4\end{matrix}\right]$$

$$\text{arrayc}=\left[\begin{matrix}1\\2\\3\\4\end{matrix}\right]$$

A row vector can be transposed into a column, which can be transposed back into a row. Transposing the 2d array 2 times, returns the original array:

```
arrayr = np.array([1, 2, 3, 4], ndmin=2)
arrayr

arrayc = arrayr.T
arrayc

arrayr = arrayc.T
arrayr
```

The ```numpy``` function ```transpose``` behaves in a similar manner:

```
arrayc = np.transpose(arrayr)
arrayc
```

![img_050](./images/img_050.png)

This also works for matrices:

$$\text{matrix1}=\left[\begin{matrix}1&2&3\\4&5&6\\7&8&9\\10&11&12\end{matrix}\right]$$

$$\text{matrix1\_t}=\left[\begin{matrix}1&4&7&9\\2&5&8&11\\3&6&9&12\end{matrix}\right]$$

```
matrix1
matrix1_t = matrix1.T
matrix1_t
```

![img_051](./images/img_051.png)

## arange and linspace

A numpy array can be created from a ```range``` object. Recall that the ```range``` object has a ```start```, ```stop``` and   ```step``` value and uses integer based zero-order indexing:

```
array1 = np.array(object=range(0, 10, 1))
array1
array1.ndim
array1.size
array1.dtype
```

![img_057](./images/img_057.png)

Recall that the ```range``` class can be instantiated with a varying number of positional input arguments:

|n|supplied|default|
|---|---|---|
|3|start, stop, step||
|2|start, stop|step=1|
|1|stop|start=0, step=1|

Zero-order indexing is exclusive of the stop value. To get an array that is inclusive of the stop value ```10```. The following would have to be used:

```
array1 = np.array(object=range(0, 10+1, 1))
array1
array1.ndim
array1.size
array1.dtype
```

![img_058](./images/img_058.png)

One limitation of the ```range``` class is confined to integers. 

![img_059](./images/img_059.png)

The ```numpy``` library includes the more powerful array range function ```arange```. This function behaves similar to the ```range``` class but can handle additional datatypes. Its docstring can be viewed as a pop up balloon by inputting ```np.arange()``` followed by shift ```⇧``` and tab ```↹```:

![img_060](./images/img_060.png)

The input arguments are similar to the ```range``` object hwoevder note inclusion of the optional keyword ```dtype```, indicating that this function can handle additional datatypes.The array created from the ```range``` object can be created with the array range function:

```
array1 = np.arange(start=0, stop=10, step=1)
array1
array1.ndim
array1.size
array1.dtype
```

![img_061](./images/img_061.png)

Once again, this uses zero-order indexing and is exclusive of the stop value. To get an array that is inclusive of the stop value ```10```, the following would have to be used:

```
array1 = np.arange(start=0, stop=10+1, step=1)
array1
array1.ndim
array1.size
array1.dtype
```

![img_062](./images/img_062.png)

The datatype is inferred by the input arguments. If the input arguments are floating point values, the datatype of the array will be ```float```. For example:

```
array1 = np.arange(start=0.0, stop=10.0+0.1, step=0.1)
array1
array1.ndim
array1.size
array1.dtype
```

![img_063](./images/img_063.png)

The array range function can also be used with ```datetimes``` and ```timedeltas```:

```
import datetime as dt

python3released = dt.datetime(year=2008, month=12, day=3, 
                              hour=12, minute=0, second=0, 
                              microsecond=0, tzinfo=london)
python3released

today = dt.datetime.now()
today

day = dt.timedelta(days=1)
day

python3birthdays = np.arange(start=python3released, stop=today+day, step=day)
python3birthdays
```

![img_064](./images/img_064.png)

Sadly at this moment, the array range function does not support timezone information, displaying a depreciation warning. This is because Python previously didn't handle timezones very well. Python 3.9 changed the way timezones were implemented using the ```zoneinfo``` standard module and depreciating the crude implementations in the ```datetime``` module. It is possible ```numpy``` will later be updated to use the features of this standard module to support timezone information:

![img_065](./images/img_065.png)

The ```numpy``` library converts instances of the ```datetime``` class to the ```np.datetime64``` class and instances of the ```timedelta``` class to the ```np.timedelta64``` class. The ```numpy``` implementations have higher precisions and can be constructed directly using the ```np.datetime64``` class and ```np.timedelta64``` class respectively: 

![img_066](./images/img_066.png)

![img_067](./images/img_067.png)

The array range function ```arange``` is complementated by the linearly spaced array function ```linspace```. Its docstring can be viewed as a pop up balloon by inputting ```np.linspace()``` followed by shift ```⇧``` and tab ```↹```:

![img_068](./images/img_068.png)

The linearly spaced array function also has a ```start``` and ```stop``` value but is inclusive to both boundaries by default. Instead of a ```step```, it uses ```num``` to specify the number of evenly spaced datapoints:

```
array1 = np.linspace(start=0, stop=10, num=11)
array1

array1.ndim
array1.size
array1.dtype
```

![img_069](./images/img_069.png)

Notice that the datetype is ```float``` by default, as the linear spaced function uses float division to calculate each datapoint. The lineart spaced function has the keyword input argument ```dtype``` which can be used to set a custom datatype such as ```int```.

## Unitary Data model Methods

A 2d array or matrix can be quickly generated using the ```arange``` function and ```reshape``` method:

```
matrix1 = np.arange(start=1, stop=17, step=1).reshape((4, 4))
matrix1
```

![img_070](./images/img_070.png)

If the directory function ```dir``` is used on the ndarray:

```
dir(matrix1)
```

A large list of identifiers displays including a larger list of datamodel identifiers:

![img_071](./images/img_071.png)

The unitary datamodel methods require only a single instance:

|unitary datamodel method|use|description|
|---|---|---|
|array.\_\_dir\_\_|dir(array)|list directory for identifiers|
|array.\_\_str\_\_|str(array)|informal representation|
|array.\_\_repr\_\_|repr(array)|formal representation|
|array.\_\_doc\_\_|? array|lookup docstring|
|array.\_\_copy\_\_|copy.copy(array)|shallow copy of array|
|array.\_\_deepcopy\_\_|copy.deepcopy(array)|deep copy of array|

|array.\_\_len\_\_|len(array)|len of array, treated as ensted list of lists...|







## Unitary Mathematical Data model Methods

|unitary datamodel method|use|description|
|---|---|---|
|array.\_\_pos\_\_|+array|unitary positive operator|
|array.\_\_neg\_\_|-array|unitary negative operator|
|array.\_\_abs\_\_|abs(array)|absolute values of array|


## Binary Mathematical Data model Methods

|binary datamodel method|use|description|
|---|---|---|
|array1.\_\_add\_\_(array2)|array1 + array2|addition operator|
|array1.\_\_radd\_\_(array2)|array2 + array1|reverse addition operator|
|array1.\_\_iadd\_\_(array2)|array1 += array2|inplace addition operator|
|array1.\_\_sub\_\_(array2)|array1 - array2|subtraction operator|
|array1.\_\_rsub\_\_(array2)|array2 - array1|reverse subtraction operator|
|array1.\_\_isub\_\_(array2)|array1 -= array2|inplace subtraction operator|
|array1.\_\_mul\_\_(array2)|array1 * array2|multiplication operator|
|array1.\_\_mul\_\_(array2)|array2 * array1|reverse multiplication operator|
|array1.\_\_mul\_\_(array2)|array1 *= array2|inplace multiplication operator|
|array1.\_\_pow\_\_(array2)|array1 ** array2|power operator|
|array1.\_\_pow\_\_(array2)|array2 ** array1|reverse power operator|
|array1.\_\_pow\_\_(array2)|array1 **= array2|inplace power operator|
|array1.\_\_floordiv\_\_(array2)|array1 // array2|integer division operator|
|array1.\_\_floordiv\_\_(array2)|array2 // array1|integer division operator|
|array1.\_\_floordiv\_\_(array2)|array1 //= array2|integer division operator|
|array1.\_\_mod\_\_(array2)|array1 % array2|modulus operator|
|array1.\_\_floordiv\_\_(array2)|array2 % array1|modulus operator|
|array1.\_\_floordiv\_\_(array2)|array1 %= array2|modulus operator|
|array1.\_\_truediv\_\_(array2)|array1 / array2|float division operator|
|array1.\_\_truediv\_\_(array2)|array2 / array1|float division operator|
|array1.\_\_truediv\_\_(array2)|array1 /= array2|float division operator|
|array1.\_\_and\_\_(array2)|array1 & array2|and operator|
|array1.\_\_rand\_\_(array2)|array2 & array1|reverse and operator|
|array1.\_\_iand\_\_(array2)|array1 &= array2|inplace and operator|
|array1.\_\_or\_\_(array2)|array1 \| array2|or operator|
|array1.\_\_ror\_\_(array2)|array2 \| array1|reverse or operator|
|array1.\_\_ior\_\_(array2)|array1 \|= array2|inplace or operator|
|array1.\_\_xor\_\_(array2)|array1 ^ array2|xor operator|
|array1.\_\_rxor\_\_(array2)|array2 ^ array1|reverse xor operator|
|array1.\_\_ior\_\_(array2)|array1 ^= array2|inplace xor operator|
|array1.\_\_lshift\_\_(array2)|array1 << array2|leftshift operator|
|array1.\_\_rlshift\_\_(array2)|array2 << array1|reverse leftshift operator|
|array1.\_\_ilshift\_\_(array2)|array1 << array2|inplace leftshift operator|

conditional operators