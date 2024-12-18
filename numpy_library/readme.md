# numpy

## builtins classes

Previously classes that followed a numeric design pattern such as `int`, `float` and `bool` were examined alongside classes that followed a `Collection` design pattern such as `tuple`, `list` and `str`. Both design patterns were based upon an `object` as the `object` is the base class for everything in Python. 

The `+` operator performs numeric addition for a number and concatenation for a `Collection`:

```python
In [1]: num1 = 1
      : num2 = 2
      : num1 + num2
Out[1]: 3

In [2]: fruits1 = ['apples', 'bananas', 'cabbage']
      : fruits2 = ['dates', 'elderberry', 'fig']
      : fruits1 + fruits2
Out[2]: ['apples', 'bananas', 'cabbage', 'dates', 'elderberry', 'fig']
```

Sometimes it is desirable to perform addition of numbers in two equally sized `Collection` instances. Using `+` will perform concatenation:

```python
In [3]: nums1 = [1, 2, 3] 
      : nums2 = [4, 5, 6]
      : nums1 + nums2
Out[3]: [1, 2, 3, 4, 5, 6]
```

Numeric addition can be carried out using a for loop:

```python
In [4]: result = []
      : for index in range(nums1):
      :     result.append(nums1[index] + nums2[index])
      : result
Out[4]: [5, 7, 9]      
```

This can be simplified slightly using a `list` comprehension and `zip`:

```python
In [5]: [num1 + num2 for num1, num2 in zip(nums1, nums2)]
Out[5]: [5, 7, 9]
```

This can also be done with a scalar:

```python
In [6]: [num1 + 1 for num1 in nums1]
Out[6]: [2, 3, 4]
```

However looping becomes more complicated and less readible for higher dimensional numeric data.

## Library Overview and Imports

`numpy`, an abbreviation for the numeric Python library is typically imported as the abbreviated alias `np`:

```python
In [7]: import numpy as np
```

`numpy` is a third-party library and the data model attribute `__version__` gives the version of the numpy library. This has the form `major.minor.patch` and the major version should be version `2`:

```python
In [8]: np.__version__
Out[8]: '2.1.3'
```

Version `2` made substantial changes to the `np` namespace and `np.ndarray` namespace removing a large number of identifiers that had duplicate names or outdated functionality, making it much more user-friendly to navigate through.

The identifiers of the `np` library can be examined:

```python
In [9]: np.
# NumPy Identifiers

# 🔢 Class:
#     - ndarray                    : n-dimensional array, the core structure of NumPy.

# 🏷️ Data Types:
#     - int8                       : 8-bit signed integer (-128 to 127).
#     - int16                      : 16-bit signed integer (-32768 to 32767).
#     - int32                      : 32-bit signed integer (-2147483648 to 2147483647).
#     - int64                      : 64-bit signed integer (-9223372036854775808 to 9223372036854775807).
#     - uint8                      : 8-bit unsigned integer (0 to 255).
#     - uint16                     : 16-bit unsigned integer (0 to 65535).
#     - uint32                     : 32-bit unsigned integer (0 to 4294967295).
#     - uint64                     : 64-bit unsigned integer (0 to 18446744073709551615).
#     - float16                    : Half precision float (16-bit).
#     - float32                    : Single precision float (32-bit).
#     - float64                    : Double precision float (64-bit).
#     - complex64                  : Complex number represented by two 32-bit floats (real and imaginary).
#     - complex128                 : Complex number represented by two 64-bit floats.
#     - bool_                      : Boolean type (True or False).
#     - str_                       : Unicode string type (variable length).
#     - bytes_                     : Byte string type (variable length).
#     - datetime64                 : Type representing dates and times.
#     - timedelta64                : Represents differences in datetime64 objects.

# ➕ Array Creation:
#     - array                     : Creates an array from a list or another array-like object.
#     - frombuffer                : Creates an array from a buffer (bytes or bytearray).
#     - asarray                   : Converts an input to an array, without copying if possible.
#     - empty                     : Creates an uninitialized array of given shape.
#     - empty_like                : Returns a new array with the same shape and type as a given array, but 
#                                   without any data.
#     - zeros                     : Creates an array filled with zeros.
#     - zeros_like                : Returns a new array filled with zeros, with the same shape as a given 
#                                   array.
#     - ones                      : Creates an array filled with ones.
#     - ones_like                 : Returns a new array filled with ones, with the same shape as a given array.
#     - full                      : Creates an array filled with a specified value.
#     - full_like                 : Returns a new array filled with a specified value, with the same shape as 
#                                   a given array.
#     - arange                    : Creates an array of evenly spaced values within a given interval.
#     - linspace                  : Generates evenly spaced numbers over a specified interval.
#     - logspace                  : Returns numbers spaced evenly on a log scale.
#     - ogrid                     : Provides an open multi-dimensional grid.
#     - mgrid                     : Provides a dense multi-dimensional "meshgrid."
#     - meshgrid                  : Generates coordinate matrices from coordinate vectors.
#     - indices                   : Returns an array with the indices of a grid.
#     - eye                       : Creates a 2D array with ones on the diagonal (identity matrix).
#     - identity                  : Returns the identity array.
#     - diag                      : Returns a square matrix with the specified diagonal and zeros elsewhere.

# 📈 Array Manipulation:
#     - diagonal                  : Returns the diagonal of the ndarray.
#     - reshape                   : Reshapes an array without changing its data.
#     - transpose                 : Permutes the axes of an array.
#     - flatten                   : Returns a flattened copy of an array.
#     - ravel                     : Flattens an array into 1D.
#     - shares_memory             : Checks if two arrays share the same memory block.
#     - concatenate               : Joins arrays along an axis.
#     - repeat                    : Repeats elements of the ndarray.
#     - tile                      : Constructs an array by repeating the input array a specified number 
#                                   of times along each axis.
#     - stack                     : Joins a sequence of arrays along a new axis.
#     - hstack                    : Stacks arrays in sequence horizontally (column-wise).
#     - vstack                    : Stacks arrays in sequence vertically (row-wise).
#     - dstack                    : Stacks arrays in sequence depth-wise (along the third axis).
#     - split                     : Splits an array into multiple sub-arrays.
#     - hsplit                    : Splits an array into multiple sub-arrays horizontally (column-wise).
#     - vsplit                    : Splits an array into multiple sub-arrays vertically (row-wise).
#     - dsplit                    : Splits an array into multiple sub-arrays along the third axis (depth-wise).
#     - pad                       : Pads an array with values.
#     - swapaxes                  : Interchanges two axes of an array.
#     - moveaxis                  : Moves axes to new positions.
#     - squeeze                   : Removes single-dimensional entries from the shape of an array.
#     - expand_dims               : Expands the shape of an array.
#     - take                      : Selects elements from the ndarray based on indices.
#     - take_along_axis           : Selects elements from an array along an axis using an array of indices.
#     - compress                  : Selects elements using a condition mask.
#     - insert                    : Inserts values into an array at specified indices along an axis.

# 🔢 Sorting Functions:
#     - argmin                     : Returns the indices of the minimum values along an axis.
#     - argmax                     : Returns the indices of the maximum values along an axis.
#     - nonzero                    : Returns the indices of the non-zero elements.
#     - sort                       : Returns a sorted copy of an array.
#     - argsort                    : Returns the indices that would sort an array.
#     - searchsorted               : Finds indices where elements should be inserted to maintain order.
#     - count_nonzero              : Counts the number of non-zero elements in an array.

# 🔗 Broadcasting and Vectorization
#     - broadcast                   : Produces an object that mimics broadcasting.
#     - broadcast_to                : Broadcasts an array to a new shape.
#     - vectorize                   : Vectorizes a function to apply element-wise on arrays.

# 📊 Mathematical Functions:
#     - add                       : Element-wise addition.
#     - subtract                  : Element-wise subtraction.
#     - multiply                  : Element-wise multiplication.
#     - divide                    : Element-wise division.
#     - power                     : Element-wise power.
#     - sqrt                      : Element-wise square root.
#     - mod                       : Element-wise modulus.
#     - exp                       : Element-wise exponential (e^x).
#     - log                       : Natural logarithm (base e).
#     - log10                     : Base-10 logarithm.
#     - sin                       : Trigonometric sine function.
#     - cos                       : Trigonometric cosine function.
#     - tan                       : Trigonometric tangent function.
#     - arcsin                    : Inverse sine function.
#     - arccos                    : Inverse cosine function.
#     - arctan                    : Inverse tangent function.
#     - deg2rad                   : Converts degrees to radians.
#     - rad2deg                   : Converts radians to degrees.
#     - cumprod                   : Cumulative product of array elements.
#     - cumsum                    : Cumulative sum of array elements.

# 📊 Statistical Functions:
#     - mean                      : Computes the arithmetic mean along the specified axis.
#     - median                    : Computes the median along the specified axis.
#     - average                   : Computes the weighted average.
#     - std                       : Computes the standard deviation along the specified axis.
#     - var                       : Computes the variance along the specified axis.
#     - min                       : Returns the minimum value along a given axis.
#     - max                       : Returns the maximum value along a given axis.
#     - ptp                       : Peak-to-peak (max - min) value along an axis.
#     - quantile                  : Computes the q-th quantile of the data along the specified axis.
#     - histogram                 : Computes the histogram of a set of data.
#     - bincount                  : Counts the number of occurrences of each value in a 1D array.
#     - corrcoef                  : Computes the Pearson correlation coefficients.
#     - cov                       : Computes the covariance matrix.

# 📦 Set Operations:
#     - unique                    : Finds the unique elements of an array.
#     - intersect1d               : Computes the intersection of two arrays.
#     - union1d                   : Computes the union of two arrays.
#     - setdiff1d                 : Computes the set difference of two arrays.
#     - setxor1d                  : Computes the exclusive or of two arrays.
#     - in1d                      : Tests whether each element of a 1D array is also in a second array.

# 🎲 Random Number Generation
#     - random.rand                 : Generates random numbers in a uniform distribution over [0,1].
#     - random.randn                : Generates random numbers in a standard normal distribution.
#     - random.randint              : Generates random integers within a specified range.
#     - random.random_sample        : Returns random floats in the half-open interval [0.0, 1.0).
#     - random.choice               : Generates a random sample from a given array.
#     - random.shuffle              : Randomly shuffles an array.
#     - random.seed                 : Sets the seed for the random number generator.

# 🧮 Linear Algebra
#     - dot                         : Dot product of two arrays.
#     - matmul                      : Matrix product of two arrays.
#     - linalg.inv                  : Computes the inverse of a matrix.
#     - linalg.eig                  : Computes the eigenvalues and eigenvectors of a matrix.
#     - linalg.svd                  : Singular Value Decomposition.
#     - linalg.qr                   : QR decomposition.
#     - linalg.det                  : Determinant of a matrix.
#     - linalg.norm                 : Matrix or vector norm.

# 📁 Data I/O
#     - load                        : Loads arrays from files.
#     - save                        : Saves an array to a file.
#     - savetxt                     : Saves an array to a text file.
#     - loadtxt                     : Loads data from a text file.
#     - genfromtxt                  : Loads data from a text file, with missing values handled.
```

The `numpy` library revolves around the `ndarray` class:

```python
In [9]: np.ndarray
# 🔗 Object Identifiers
#     - __doc__                    : Documentation string of the ndarray object.
#     - __class__                  : The class/type of the ndarray object.
#     - __dir__                    : Returns the list of valid attributes for the ndarray object.
#     - __sizeof__                 : Returns the size of the ndarray object in memory (in bytes).
#     - __format__                 : Defines how the ndarray object should be formatted when using the format() function.
#     - __new__                    : Used to create a new instance of the ndarray object.
#     - __init__                   : Initializes the newly created ndarray object.
#     - __repr__                   : Defines how the ndarray object is represented (for developers).
#     - __str__                    : Defines how the ndarray object is converted to a string (for users).
#     - __eq__                     : Equality comparison (==).
#     - __ne__                     : Inequality comparison (!=).
#     - __ge__                     : Greater than or equal to comparison (>=).
#     - __le__                     : Less than or equal to comparison (<=).
#     - __gt__                     : Greater than comparison (>).
#     - __lt__                     : Less than comparison (<).
#     - __hash__                   : Returns the hash value of the ndarray object, used for sets and dictionaries.
#     - __getattribute__           : Called to retrieve an attribute of the ndarray object.
#     - __setattr__                : Called to set an attribute of the ndarray object.
#     - __delattr__                : Called to delete an attribute of the ndarray object.
#     - __getstate__               : Gets the current state of the ndarray for pickling.
#     - __reduce__                 : Provides data for serialization with pickle.
#     - __reduce_ex__              : Similar to __reduce__, but with protocol-specific details for pickling.
#     - __getnewargs__             : Provides additional arguments needed when unpickling the ndarray object.
#     - __init_subclass__          : Called when a subclass of ndarray is created.
#     - __subclasshook__           : Defines custom behavior for determining class inheritance.

# 🔗 Numeric Identifiers
#     - __abs__                    : Returns the absolute value of the ndarray object.
#     - __pos__                    : Unary plus (+) for the ndarray object.
#     - __neg__                    : Unary minus (-) for the ndarray object.
#     - __add__                    : Addition operation (+).
#     - __sub__                    : Subtraction operation (-).
#     - __mul__                    : Multiplication operation (*).
#     - __pow__                    : Power operation (**).
#     - __floordiv__               : Floor division (//).
#     - __mod__                    : Modulus operation (%).
#     - __divmod__                 : Division and modulus together (divmod()).
#     - __truediv__                : True division (/).
#     - __radd__                   : Reverse addition (right-hand side).
#     - __rsub__                   : Reverse subtraction.
#     - __rmul__                   : Reverse multiplication.
#     - __rpow__                   : Reverse power operation.
#     - __rfloordiv__              : Reverse floor division.
#     - __rmod__                   : Reverse modulus.
#     - __rdivmod__                : Reverse division and modulus together.
#     - __rtruediv__               : Reverse true division.
#     - real                       : The real part of a complex ndarray.
#     - imag                       : The imaginary part of a complex ndarray.
#     - conjugate                  : The complex conjugate of the ndarray.

# 🔗 Bitwise Identifiers
#     - __and__                    : Bitwise and.
#     - __or__                     : Bitwise or.
#     - __xor__                    : Bitwise xor.
#     - __invert__                 : Bitwise not.
#     - __lshift__                 : Bitwise left shift.
#     - __rshift__                 : Bitwise right shift.

# 🔗 Casting Identifiers
#     - tolist                     : Converts the ndarray to a nested list.
#     - tobytes                    : Converts the ndarray to a bytes string.

# 🔗 Collection Identifiers
#     - __getitem__                : Allows indexing (obj[index]).
#     - __setitem__                : Allows setting an item (obj[index] = value).
#     - __iter__                   : Returns an iterator for the ndarray.
#     - __len__                    : Returns the length of the ndarray.
#     - __contains__               : Checks if an item is in the ndarray (in operator).
#     - copy                       : Returns a shallow copy of the ndarray.

# 🔗 Supplementary Collection Identifiers
#     - ndim                       : The number of dimensions of the ndarray.
#     - shape                      : The shape of the ndarray.
#     - size                       : The number of elements in the ndarray.
#     - itemsize                   : The size of one array element in bytes.
#     - nbytes                     : The total number of bytes consumed by the ndarray.
#     - T                          : The transpose of a 2D ndarray.
#     - flat                       : The flattened iterator of the ndarray.
#     - diagonal                   : Returns the diagonal of the ndarray.
#     - reshape                    : Changes the shape of the ndarray without altering data.
#     - flatten                    : Flattens the ndarray into a 1D array.
#     - ravel                      : Returns a flattened view of the ndarray.
#     - transpose                  : Permutes the axes of the ndarray.
#     - swapaxes                   : Interchanges two axes of the ndarray.
#     - item                       : Copies a single element from the ndarray.
#     - repeat                     : Repeats elements of the ndarray.
#     - squeeze                    : Removes single-dimensional entries from the shape.
#     - take                       : Selects elements from the ndarray based on indices.
#     - fill                       : Fills the ndarray with a scalar value.
#     - compress                   : Selects elements using a condition mask.

# 🔗 Sorting, Searching, and Counting
#     - argmin                     : Returns the indices of the minimum values along an axis.
#     - argmax                     : Returns the indices of the maximum values along an axis.
#     - nonzero                    : Returns the indices of the non-zero elements.
#     - sort                       : Sorts the ndarray along the specified axis.
#     - argsort                    : Returns the indices that would sort the ndarray.
#     - searchsorted               : Finds indices where elements should be inserted to maintain order.

# 🔗 Supplementary Numerical Identifiers
#     - round                      : Rounds the ndarray elements to the given number of decimals.
#     - astype                     : Converts the ndarray to a different data type.
#     - dot                        : Computes the dot product of two ndarrays.
#     - conjugate                  : Returns the complex conjugate of the ndarray.
#     - min                        : Returns the minimum value along the specified axis.
#     - max                        : Returns the maximum value along the specified axis.
#     - clip                       : Limits the values in the ndarray to a given range.
#     - mean                       : Returns the mean value along the specified axis.
#     - all                        : Checks if all elements are True along the specified axis.
#     - any                        : Checks if any elements are True along the specified axis.
#     - sum                        : Returns the sum of ndarray elements along the specified axis.
#     - var                        : Returns the variance along the specified axis.
#     - std                        : Returns the standard deviation along the specified axis.
#     - prod                       : Returns the product of ndarray elements along the specified axis.
#     - cumprod                    : Returns the cumulative product of ndarray elements.
#     - cumsum                     : Returns the cumulative sum of ndarray elements.
#     - choose                     : Constructs an ndarray by selecting elements from a sequence of ndarrays.

# 🔗 Miscellaneous Operations
#     - byteswap                   : Swaps the byte order of the ndarray data.
```

Notice that the `ndarray`, like everything in Python follows an `object` design pattern. Notice also that the `ndarray` follows a numeric design pattern and a `Collection`-like design pattern. Most of the methods in the `ndarray` are immutable however a handful of the methods are mutable, behaving consistently to their design pattern.

The methods `__setitem__ ` and `sort` follow the design pattern of a `MutableSequence` and are mutable, like in a `list`. 

`resize` is the mutable counterpart to `reshape` and resizes an `ndarray` in place.

`fill` is also mutable and fills in an `ndarray` in place with a fill value.

```python
In [9]: exit
```

## Buffer and Datatypes

The `ndarray` can be instantiated from a buffer, typically a `bytes` instance:

```python
In [1]: import numpy as np
      : hexvals = ['00000000', '01000000', '02000000', '03000000',
      :            '04000000', '05000000', '06000000', '07000000',
      :            '08000000', '09000000', '0a000000', '0b000000',
      :            '0c000000', '0d000000', '0e000000', '0f000000',
      :            'ffffffff', 'feffffff', 'fdffffff', 'fcffffff',
      :            'fbffffff', 'faffffff', 'f9ffffff', 'f8ffffff',
      :            'f7ffffff', 'f6ffffff', 'f5ffffff', 'f4ffffff',
      :            'f3ffffff', 'f2ffffff', 'f1ffffff', 'f0ffffff']
      :
      : hexvals = ''.join(hexvals)
      : b = bytes.fromhex(hexvals)
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif; background-color: #1e1e1e; color: #d4d4d4;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Name ▲</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Type</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Size</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Value</th>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e;">hexvals</td>
    <td style="padding: 8px; background-color: #1e1e1e;">str</td>
    <td style="padding: 8px; background-color: #1e1e1e;">256</td>
    <td style="padding: 8px; background-color: #506E16; color: #ffffff;">000000000100000002000000030000000400000005000000060000000700000008000000090000000a0000000b0000000c0000000d0000000e0000000f000000fffffffffefffffffdfffffffcfffffffbfffffffafffffff9fffffff8fffffff7fffffff6fffffff5fffffff4fffffff3fffffff2fffffff1fffffff0ffffff</td> <!-- Updated background color for strings -->
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #252526;">b</td>
    <td style="padding: 8px; background-color: #252526;">bytes</td>
    <td style="padding: 8px; background-color: #252526;">128</td>
    <td style="padding: 8px; background-color: #148F77; color: #ffffff;">b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x0e\x00\x00\x00\x0f\x00\x00\x00\xff\xff\xff\xff\xfe\xff\xff\xff\xfd\xff\xff\xff\xfc\xff\xff\xff\xfb\xff\xff\xff\xfa\xff\xff\xff\xf9\xff\xff\xff\xf8\xff\xff\xff\xf7\xff\xff\xff\xf6\xff\xff\xff\xf5\xff\xff\xff\xf4\xff\xff\xff\xf3\xff\xff\xff\xf2\xff\xff\xff\xf1\xff\xff\xff\xf0\xff\xff\xff'</td> <!-- Different background color for bytes -->
  </tr>
</table>

Note that this `bytes` instance is little endian. An `ndarray` can be instantiated by specifying the `shape` as a `tuple`, `dtype` (datatype) and `buffer`. In this case, the shape is `(8, 4)` which means 8 rows by 4 columns. The datatype is `np.int32`, which means 32 bit signed integers. As there are 8 bits in a byte, this means 4 bytes are used to represent each integer in memory. The first half of the numbers in the 4 byte sequence represent positive numbers and the second half of the numbers are used to represent negative numbers:

```python
In [2]: np.ndarray(shape=(8, 4), dtype=np.int32, buffer=b)
Out[2]:
array([[  0,   1,   2,   3],
       [  4,   5,   6,   7],
       [  8,   9,  10,  11],
       [ 12,  13,  14,  15],
       [ -1,  -2,  -3,  -4],
       [ -5,  -6,  -7,  -8],
       [ -9, -10, -11, -12],
       [-13, -14, -15, -16]], dtype=int32)
```

The datatype `np.uint32`, means 32 bit unsigned integers and each number is positive. The first half of the bytes in the 4 byte sequence are consistent between `np.uint32` and `np.int32` and give the same integers. The bytes in the second half of the bytes sequence differ, giving large positive values for `uint32`:

```python
In [3]: np.ndarray(shape=(8, 4), dtype=np.uint32, buffer=b)
Out[3]: 
array([[         0,          1,          2,          3],
       [         4,          5,          6,          7],
       [         8,          9,         10,         11],
       [        12,         13,         14,         15],
       [4294967295, 4294967294, 4294967293, 4294967292],
       [4294967291, 4294967290, 4294967289, 4294967288],
       [4294967287, 4294967286, 4294967285, 4294967284],
       [4294967283, 4294967282, 4294967281, 4294967280]], dtype=uint32)
```

A second `bytes` instance `b2` can be instantiated:

```python
In [4]: hexvals2 = ['0000000000000000', '0100000000000000', '0200000000000000', '0300000000000000',
      :             '0400000000000000', '0500000000000000', '0600000000000000', '0700000000000000',
      :             '0800000000000000', '0900000000000000', '0a00000000000000', '0b00000000000000',
      :             '0c00000000000000', '0d00000000000000', '0e00000000000000', '0f00000000000000',
      :             'ffffffffffffffff', 'feffffffffffffff', 'fdffffffffffffff', 'fcffffffffffffff',
      :             'fbffffffffffffff', 'faffffffffffffff', 'f9ffffffffffffff', 'f8ffffffffffffff',
      :             'f7ffffffffffffff', 'f6ffffffffffffff', 'f5ffffffffffffff', 'f4ffffffffffffff',
      :             'f3ffffffffffffff', 'f2ffffffffffffff', 'f1ffffffffffffff', 'f0ffffffffffffff']
      : hexvals2 = ''.join(hexvals2)
      : b2 = bytes.fromhex(hexvals2)
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif; background-color: #1e1e1e; color: #d4d4d4;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Name ▲</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Type</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Size</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Value</th>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e;">hexvals2</td>
    <td style="padding: 8px; background-color: #1e1e1e;">str</td>
    <td style="padding: 8px; background-color: #1e1e1e;">512</td>
    <td style="padding: 8px; background-color: #506E16; color: #ffffff;">00000000000000000100000000000000020000000000000003000000000000000400000000000000050000000000000006000000000000000700000000000000080000000000000009000000000000000a000000000000000b000000000000000c000000000000000d000000000000000e000000000000000f00000000000000fffffffffffffffffefffffffffffffffdfffffffffffffffcfffffffffffffffbfffffffffffffffafffffffffffffff9fffffffffffffff8fffffffffffffff7fffffffffffffff6fffffffffffffff5fffffffffffffff4fffffffffffffff3fffffffffffffff2fffffffffffffff1fffffffffffffff0ffffffffffffff</td> <!-- Updated background color for strings -->
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #252526;">b2</td>
    <td style="padding: 8px; background-color: #252526;">bytes</td>
    <td style="padding: 8px; background-color: #252526;">256</td>
    <td style="padding: 8px; background-color: #148F77; color: #ffffff;">b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xfd\xff\xff\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff\xff\xff\xff\xff\xfa\xff\xff\xff\xff\xff\xff\xff\xf9\xff\xff\xff\xff\xff\xff\xff\xf8\xff\xff\xff\xff\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xf6\xff\xff\xff\xff\xff\xff\xff\xf5\xff\xff\xff\xff\xff\xff\xff\xf4\xff\xff\xff\xff\xff\xff\xff\xf3\xff\xff\xff\xff\xff\xff\xff\xf2\xff\xff\xff\xff\xff\xff\xff\xf1\xff\xff\xff\xff\xff\xff\xff\xf0\xff\xff\xff\xff\xff\xff\xff'</td> <!-- Different background color for bytes -->
  </tr>
</table>

This `bytes` instance can be used to instantiate an `ndarray` using `np.int64` and `np.unint64`:

```python
In [5]: np.ndarray(shape=(8, 4), dtype=np.int64, buffer=b2)
Out[5]:
array([[  0,   1,   2,   3],
       [  4,   5,   6,   7],
       [  8,   9,  10,  11],
       [ 12,  13,  14,  15],
       [ -1,  -2,  -3,  -4],
       [ -5,  -6,  -7,  -8],
       [ -9, -10, -11, -12],
       [-13, -14, -15, -16]])

In [6]: np.ndarray(shape=(8, 4), dtype=np.uint64, buffer=b2)
Out[6]:
array([[                   0,                    1,                    2,                    3],
       [                   4,                    5,                    6,                    7],
       [                   8,                    9,                   10,                   11],
       [                  12,                   13,                   14,                   15],
       [18446744073709551615, 18446744073709551614, 18446744073709551613, 18446744073709551612],
       [18446744073709551611, 18446744073709551610, 18446744073709551609, 18446744073709551608],
       [18446744073709551607, 18446744073709551606, 18446744073709551605, 18446744073709551604],
       [18446744073709551603, 18446744073709551602, 18446744073709551601, 18446744073709551600]], 
      dtype=uint64)     
```

`np.int64` is the Operating System default. `np.int_` and `int` are alias for `np.int64`.

```python
In [7]: np.ndarray(shape=(8, 4), dtype=int, buffer=b2)
Out[7]: 
array([[  0,   1,   2,   3],
       [  4,   5,   6,   7],
       [  8,   9,  10,  11],
       [ 12,  13,  14,  15],
       [ -1,  -2,  -3,  -4],
       [ -5,  -6,  -7,  -8],
       [ -9, -10, -11, -12],
       [-13, -14, -15, -16]])

In [8]: np.ndarray(shape=(8, 4), dtype=np.int_, buffer=b2)
Out[8]: 
array([[  0,   1,   2,   3],
       [  4,   5,   6,   7],
       [  8,   9,  10,  11],
       [ 12,  13,  14,  15],
       [ -1,  -2,  -3,  -4],
       [ -5,  -6,  -7,  -8],
       [ -9, -10, -11, -12],
       [-13, -14, -15, -16]])
```

## ndarray attributes

If the following ndarrays are instantiated:

```python
In [9]: mat1 = np.ndarray(shape=(8, 4), dtype=np.int32, buffer=b)
      : mat2 = np.ndarray(shape=(8, 4), dtype=np.int64, buffer=b2)
```

The `ndarray` attributes can be examined.

`ndim` is the number of dimensions of the `ndarray`:

```python
In [10]: mat1.ndim 
Out[10]: 2
```

`shape` is the shape `tuple` of the `ndarray`:

```python
In [11]: mat1.shape
Out[11]: (8, 4)
```

The `builtins` function `len` returns the length of the first axis:

```python
In [12]: len(mat1)
Out[12]: 8
```

This can be better understood when the `ndarray` is cast into a `list` of nested `list` instances:

```python
In [13]: mat1.tolist()
Out[13]: 
[[0, 1, 2, 3],
 [4, 5, 6, 7],
 [8, 9, 10, 11],
 [12, 13, 14, 15],
 [-1, -2, -3, -4],
 [-5, -6, -7, -8],
 [-9, -10, -11, -12],
 [-13, -14, -15, -16]]
```

The length of this outer `list` is `8`.

`size` is the `size` (number of numeric elements) in the `ndarray`:

```python
In [14]: mat1.size
Out[14]: 32
```

`itemsize` is the memory size (in bytes) of one element in the `ndarray`:

```python
In [15]: mat1.itemsize
Out[15]: 4

In [16]: mat2.itemsize
Out[16]: 8
```

`nbytes` is the total memory size of all the elements in the `ndarray`:

```python
In [16]: mat1.nbytes
Out[16]: 128

In [17]: mat2.nbytes
Out[17]: 256
```

`dtype` is the datatype of the `ndarray`:

```python
In [18]: mat1.dtype
Out[18]: dtype('int32')

In [19]: mat2.dtype
Out[19]: dtype('int64')
```

The `ndarray` can be cast into a `bytes` buffer using the method `tobytes`:

```python
In [20]: mat1.tobytes()
Out[20]:
b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x0e\x00\x00\x00\x0f\x00\x00\x00\xff\xff\xff\xff\xfe\xff\xff\xff\xfd\xff\xff\xff\xfc\xff\xff\xff\xfb\xff\xff\xff\xfa\xff\xff\xff\xf9\xff\xff\xff\xf8\xff\xff\xff\xf7\xff\xff\xff\xf6\xff\xff\xff\xf5\xff\xff\xff\xf4\xff\xff\xff\xf3\xff\xff\xff\xf2\xff\xff\xff\xf1\xff\xff\xff\xf0\xff\xff\xff'
```

Notice this is the same as `b` which was used to instantiate the `ndarray`.

The `ndarray` has the informal `str` representation:

```python
In [21]: str(mat1)
Out[21]: '[[  0   1   2   3]\n [  4   5   6   7]\n [  8   9  10  11]\n [ 12  13  14  15]\n [ -1  -2  -3  -4]\n [ -5  -6  -7  -8]\n [ -9 -10 -11 -12]\n [-13 -14 -15 -16]]'
```
When printed, this displays a `list` of `list` instances:

```python
In [22]: print(str(mat1))
[[  0   1   2   3]
 [  4   5   6   7]
 [  8   9  10  11]
 [ 12  13  14  15]
 [ -1  -2  -3  -4]
 [ -5  -6  -7  -8]
 [ -9 -10 -11 -12]
 [-13 -14 -15 -16]]
```

The `ndarray` also has a formal `str` representation:

```python
In [23]: repr(mat1)
Out[23]: 'array([[  0,   1,   2,   3],\n       [  4,   5,   6,   7],\n       [  8,   9,  10,  11],\n       [ 12,  13,  14,  15],\n       [ -1,  -2,  -3,  -4],\n       [ -5,  -6,  -7,  -8],\n       [ -9, -10, -11, -12],\n       [-13, -14, -15, -16]], dtype=int32)'
```

When printed, this displays the preferred way to instantiate an `ndarray`:

```python
In [24]: print(repr(mat1))
array([[  0,   1,   2,   3],
       [  4,   5,   6,   7],
       [  8,   9,  10,  11],
       [ 12,  13,  14,  15],
       [ -1,  -2,  -3,  -4],
       [ -5,  -6,  -7,  -8],
       [ -9, -10, -11, -12],
       [-13, -14, -15, -16]], dtype=int32)
```

## ndarray creation functions

Notice the formal representation displays the `array` function, instead of the `ndarray` class. This is because the `array` function is more commonly used to instantiate an `ndarray` from an `object` such as a `list` of `list` instances opposed to the direct instantiation of an `ndarray` using a buffer. The docstring of the `ndarray` states that `ndarray` instances should be constructed using the `array` function of related functions:

```python
In [25]: np.ndarray:
Init signature: np.ndarray(self, /, *args, **kwargs)
Docstring:     
ndarray(shape, dtype=float, buffer=None, offset=0,
        strides=None, order=None)

An array object represents a multidimensional, homogeneous array
of fixed-size items.  An associated data-type object describes the
format of each element in the array (its byte-order, how many bytes it
occupies in memory, whether it is an integer, a floating point number,
or something else, etc.)

Arrays should be constructed using `array`, `zeros` or `empty` (refer
to the See Also section below).  The parameters given here refer to
a low-level method (`ndarray(...)`) for instantiating an array.
```

If the docstring of the `ndarray` function is examined:

```python
In [26]: np.array?
Docstring:
array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
      like=None)

Create an array.

Parameters
----------
object : array_like
    An array, any object exposing the array interface, an object whose
    ``__array__`` method returns an array, or any (nested) sequence.
    If object is a scalar, a 0-dimensional array containing object is
    returned.
dtype : data-type, optional
    The desired data-type for the array. If not given, NumPy will try to use
    a default ``dtype`` that can represent the values (by applying promotion
    rules when necessary.)

See Also
--------
empty_like : Return an empty array with shape and type of input.
ones_like : Return an array of ones with shape and type of input.
zeros_like : Return an array of zeros with shape and type of input.
full_like : Return a new array with shape of input filled with value.
empty : Return a new uninitialized array.
ones : Return a new array setting values to one.
zeros : Return a new array setting values to zero.
full : Return a new array of given shape filled with value.
copy: Return an array copy of the given object.
```

An `ndarray` can be constructed using:

```python
In [27]: mat1 = np.array([[0, 1, 2, 3],
       :                  [4, 5, 6, 7],
       :                  [8, 9, 10, 11]])

In [28]: mat2 = np.array([[0., 1, 2, 3],
       :                  [4, 5, 6, 7],
       :                  [8, 9, 10, 11]])
```

Notice in the Variable Explorer that the datatypes of each `ndarray` is inferred from the supplied `object`:

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>  
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 0  1  2  3]<br>&nbsp;[ 4  5  6  7]<br>&nbsp;[ 8  9 10 11]]</td>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat2</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of float64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 0.  1.  2.  3.]<br>&nbsp;[ 4.  5.  6.  7.]<br>&nbsp;[ 8.  9. 10. 11.]]</td>
  </tr>                  
</table>

```python
In [27]: mat3 = np.zeros(shape=(5, 2))
In [28]: mat4 = np.ones(shape=(2, 2))
In [29]: mat5 = np.full(shape=(3, 5), fill_value=2)
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>  
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat3</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of float64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(5, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 0.  0.]<br>&nbsp;[ 0.  0.]<br>&nbsp;[ 0.  0.]<br>&nbsp;[ 0.  0.]<br>&nbsp;[ 0.  0.]]</td>
  </tr> 
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat4</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of float64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1.  1.]<br>&nbsp;[ 1.  1.]]</td>
  </tr>    
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat5</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 5)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 2  2  2  2  2]<br>&nbsp;[ 2  2  2  2  2]<br>&nbsp;[ 2  2  2  2  2]]</td>
  </tr>                  
</table>

Notice that `mat3` and `mat4` have the datatype `np.float64`, whereas `mat5` has the datatype `np.int64`:

```python
In [30]: mat3.dtype
Out[30]: dtype('float64')

In [31]: mat4.dtype
Out[31]: dtype('float64')

In [32]: mat5.dtype
Out[32]: dtype('int64')
```

The datatype for the `zeros` and `ones` function is `np.float64` by default however can be set to `np.int64` using the optional parameter `dtype`. The `full` function infers the datatype from the provided `fill_value`.

```python
In [33]: mat6 = np.zeros(shape=(2, 2), dtype=np.int64)
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat6</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 0  0]<br>&nbsp;[ 0  0]]</td>
  </tr>                  
</table>

So far only a 2 dimensional `ndarray` has been considered, which is known as a matrix. A 1 dimensional `ndarray`, known as a vector can be examined:

```python
In [34]: active = [0, 0, 0, 0, 0]
       : vec = np.zeros(shape=(5, ), dtype=np.int64)
```

Notice the shape only has 1 element in it. The vector is similar to a `list` and both of these display in the Variable Explorer:

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">active</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">list</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">5</td>
    <td style="padding: 8px; background-color: #2C748E; color: #ffffff;">[0, 0, 0, 0, 0]</td>
  </tr>   
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">vec</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(5, )</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[ 0  0  0  0  0]</td>
  </tr>                  
</table>

Each of these can be expanded. Notice because, the `list` can have a different datatype at each index, the `Type` and `Size` are explictly shown for each element:

<table style="width: 80%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">active - list (5 elements)</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Index ▲</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Type</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Size</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Value</th>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">int</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #8C5616; color: #ffffff;">0</td>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">int</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #8C5616; color: #ffffff;">0</td>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">int</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #8C5616; color: #ffffff;">0</td>
  </tr> 
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">3</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">int</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #8C5616; color: #ffffff;">0</td>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">int</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #8C5616; color: #ffffff;">0</td>
  </tr>  
</table>

Because the `ndarray` has a uniform `np.int64` datatype and each element is a scalar of size `1`, these additional properties aren't shown and more of a focus can be made on the numeric data. Some IDEs such as Spyder will apply a colormap so trends in the numeric data can be visualised:

<table style="width: 20%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="2" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">vec - numpy int64 array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;"> </td>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr> 
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>     
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>  
</table>

Notice that the `list` and the vector are neither rows or columns. When convienient, they are displayed either as a row (Variable Explorer collapsed view) or as a column (Variable Explorer expanded view).

A vector is a 1d `ndarray` and should not be confused with a 2d `ndarray` that is explictly a column (last dimension is `1`) or row (second last dimension is `1`):

```python
In [35]: col = np.zeros(shape=(5, 1), dtype=np.int64)
In [36]: row = np.zeros(shape=(1, 5), dtype=np.int64)
```

Notice these both explictly show as a column and row in the collapsed and expanded view of the Variable Explorer:

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>       
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">col</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(5, 1)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[0]<br>&nbsp;[0]<br>&nbsp;[0]<br>&nbsp;[0]<br>&nbsp;[0]]</td>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">row</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(1, 5)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 0  0  0  0  0]]</td>
  </tr> 
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">vec</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(5, )</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[ 0  0  0  0  0]</td>
  </tr>                                
</table>

<table style="width: 20%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="2" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">col - numpy int64 array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr> 
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>     
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>  
</table>

<table style="width: 40%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="6" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">row - numpy int64 array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th> 
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">3</th>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</th>                        
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0</td> 
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0</td> 
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0</td>              
  </tr>
</table>

<table style="width: 20%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="2" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">vec - numpy int64 array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;"> </td>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr> 
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>     
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>  
</table>

In the expanded view `col` and `vec` look very similar, however `vec` is a 1d `ndarray` and therefore doesn't have the second dimension for the index:

<table style="width: 20%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="2" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">col - numpy int64 array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #ff0000; color: #ffffff;">0</th>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr> 
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>     
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">0<td>
  </tr>  
</table>

This can be seen when indexing into the `ndarray`. Indexing for the column can be carried out using square brackets and supplying `[nrow, ncol]` where `ncol` is the last index and `nrow` is the second last index. This is analogous to the behaviour of the `shape` `tuple`:

```python
In [37]: col[1]
Out[37]: array([0])

In [38]: col[1, 0]
Out[38]: np.int64(0)
```

For the vector there is only 1 dimension, so only `[ncol]` can be specified (this makes sense if the 1d `ndarray` is conceptualised as a row, using the collapsed form of the Variable Explorer):

```python
In [39]: vec[1]
Out[39]: np.int64(0)

In [40]: vec[1, 0]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[40], line 1
----> 1 vec[1, 0]

IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
```

The function `frombuffer` will create a vector from a `bytes` buffer:

```python
In [41]: np.frombuffer(dtype=np.int32, buffer=b)
Out[41]: 
array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        13,  14,  15,  -1,  -2,  -3,  -4,  -5,  -6,  -7,  -8,  -9, -10,
       -11, -12, -13, -14, -15, -16], dtype=int32)
```

A `range` instance has the parameters `start`, `stop` and `step`. When the `range` instance is cast into a `list`, all the element can be seen. Python uses zero-order indexing, and is inclusive of the `start` boundary and elements are incremented using the specified `step` up to but exclusive to the `stop` boundary: 

```python
In [42]: list(range(0, 5, 1))
Out[42]: [0, 1, 2, 3, 4]
```

The `arange` (array range) function behaves similarly but returns a 1d `ndarray`:

```python
In [43]: np.arange(0, 5, 1)
Out[43]: array([0, 1, 2, 3, 4])
```

The default `step` is `1`:

```python
In [44]: list(range(0, 5))
Out[44]: [0, 1, 2, 3, 4]

In [45]: np.arange(0, 5)
Out[45]: array([0, 1, 2, 3, 4])
```

The default `start` is `0`:

```python
In [46]: list(range(5))
Out[46]: [0, 1, 2, 3, 4]

In [47]: np.arange(5)
Out[47]: array([0, 1, 2, 3, 4])
```

A negative `step` can be used, notice that the `range` instance is inclusive of the `start` and `exclusive` of the `stop`: 

```python
In [48]: list(range(5, 1, -1))
Out[48]: [5, 4, 3, 2]

In [49]: np.range(5, 1, -1)
Out[49]: array([5, 4, 3, 2])
```

The `range` function requires `start`, `stop` and `step` to be integers:

```python
In [50]: list(range(1, 2, 0.1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[50], line 1
----> 1 list(range(1, 2, 0.1))

TypeError: 'float' object cannot be interpreted as an integer
```

The array range function is more powerful and can use non-integer `start`, `stop` and `step` values:

```python
In [51]: np.arange(1, 2, 0.1)
Out[51]: array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
```

Notice `2.0` is not present because, the output 1d `ndarray` is inclusive of the `start` and `exclusive` of the `stop` bound: 

```python
In [52]: np.arange(1, 2+0.1, 0.1)
Out[52]: array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0])
```

A related function is the linear space function `linspace` which creates linearly spaced values between the `start` and `stop` boundaries inclusive of both boundaries. Instead of a `step`, the `num` of points is selected:

```python
In [53]: np.linspace(1, 2, 10)
Out[53]: 
array([1.        , 1.11111111, 1.22222222, 1.33333333, 1.44444444,
       1.55555556, 1.66666667, 1.77777778, 1.88888889, 2.        ])

In [54]: np.linspace(1, 2, 11)
Out[54]: array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. ])       
```

There is also the related function logspace, where `start` and `stop` are expressed in powers of `10` and `num` is to the power of `1`. Notice below that the `start` and `stop` boundaries are the same and included in both 1d `ndarray` instances returned. The `8` values are linearly and logarithmically spaced:

```python
In [54]: np.linspace(10**1, 10**8, 8)
Out[54]: 
array([1.00000000e+01, 1.42857229e+07, 2.85714357e+07, 4.28571486e+07,
       5.71428614e+07, 7.14285743e+07, 8.57142871e+07, 1.00000000e+08])

In [55]: np.logspace(1, 8, 8)
Out[55]: array([1.e+01, 1.e+02, 1.e+03, 1.e+04, 1.e+05, 1.e+06, 1.e+07, 1.e+08])
```

The `arange`, `linspace` and `logspace` functions return a 1d `ndarray`. This can be reshaped into other dimensions using the function or immutable method `reshape`:

```python
In [56]: np.arange(12).reshape((3, 4))
Out[56]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```

To reshape into a row, the `shape` `tuple` should have `1` row and be the length of the original `ndarray`

```python
In [57]: np.arange(3).reshape((1, len(np.arange(3))))
Out[57]: array([[0, 1, 2]])

In [58]: np.arange(3).reshape((1, np.arange(3).size))
Out[58]: array([[0, 1, 2]])
```

Alternatively `-1` can be specified which means all elements:

```python
In [59]: np.arange(3).reshape((1, -1))
Out[59]: array([[0, 1, 2]])
```

However it is normally preferable to index into the `ndarray` specifying a `np.newaxis` for the row and all elements, indicated by a `:` for the column:

```python
In [60]: np.arange(3)[np.newaxis, :]
Out[60]: array([[0, 1, 2]])
```

For a column, all elements `:` should be specified for the `row` and `np.newaxis` should be specified for the column:

```python
In [61]: np.arange(3)[:, np.newaxis]
Out[61]: 
array([[0],
       [1],
       [2]])
```

The `array` function has an optional parameter `ndmin` which can be used to specify, the minimum number of dimensions an array has. If this is set to `2`, the vector becoems a row:

```python
In [62]: np.array(np.arange(3))
Out[62]: array([0, 1, 2])

In [63]: np.array(np.arange(3), ndmin=2)
Out[63]: array([[0, 1, 2]])
```

The attribute `T` is the transpose. The transpose for a row is a column and vice-versa:

```python
In [64]: np.array(np.arange(3), ndmin=2).T
Out[64]: 
array([[0],
       [1],
       [2]])

In [65]: np.array(np.arange(3), ndmin=2).T.T
Out[65]: array([[0, 1, 2]])
```

Supposing the following matrices are created in a datastructure that is a `list` of `list` instances and an `ndarray` respectively:

```python
In [66]: mat1 = [[1, 2],
       :         [3, 4]]
       : mat2 = np.arange(mat1)
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>   
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">list</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #2C748E; color: #ffffff;">[[1, 2],[3, 4]]</td>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat2</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2]<br>&nbsp;[ 3  4]]</td>
  </tr>       
</table>

If `mat1` is explored:

<table style="width: 80%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - list (2 elements)</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Index ▲</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Type</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Size</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Value</th>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">list</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #2C748E; color: #ffffff;">[1, 2]</td>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">list</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #2C748E; color: #ffffff;">[3, 4]</td>
  </tr>      
</table>

If the `list` at index `1` is explored:

<table style="width: 80%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1[0] - list (2 elements)</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Index ▲</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Type</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Size</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">Value</th>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">int</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #8c5616; color: #ffffff;">3</td>
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">int</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #8c5616; color: #ffffff;">4</td>
  </tr>      
</table>

The data model method `__getitem__`  is defined which allows indexing into a `list`. When indexing square brackets are used to contain the index:

```python
In [67]: mat1[1]
Out[67]: [3, 4]
```

Because these are two data structures, an outer `list` and an inner `list`, two sets of square brackets are used:

```python
In [68]: mat1[1][0]
Out[68]: 3
```

If a `tuple` of elements is used, a `TypeError` is flagged up:

```python
In [69]: mat1[(1, 0)]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[69], line 1
----> 1 mat1[(1, 0)]

TypeError: list indices must be integers or slices, not tuple
```

The 2d `ndarray` on the other hand is a singular data structure:

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat2</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2]<br>&nbsp;[ 3  4]]</td>
  </tr>                  
</table>

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat2 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c8d; color: #ffffff;">2</td>  
          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #7a3cab; color: #ffffff;">3</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">4</td>        
  </tr>
  </table>

The data model method `__getitem__`  is defined which allows indexing into a `ndarray`. When indexing square brackets are used to contain the index:

```python
In [70]: mat2[1]
Out[70]: array([3, 4])

In [71]: mat2[1][0]
Out[71]: np.int64(3)
```

Because the 2d `ndarray` is a singular data structure, a `tuple` of elements can be provided:

```python
In [72]: mat2[(1, 0)]
Out[72]: np.int64(3)
```

Note that the `tuple` has the same form as the `shape` `tuple` previously examined:

```python
In [73]: np.zeros((3, 2))
Out[73]: 
array([[0., 0.],
       [0., 0.],
       [0., 0.]])
```

For indexing, the `tuple` is often unpacked:

```python
In [74]: 1, 0
Out[74]: (1, 0)

In [75]: mat2[1, 0]
Out[75]: np.int64(3)
```

Note that this is not possible in all functions where the `shape` `tuple` is used. Unpacking in the `zeros` function for example implies each element in the `shape` `tuple` is a different positional parameter and flags up a `TypeError`:

```python
In [76]: np.zeros(3, 2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[76], line 1
----> 1 np.zeros(3, 2)

TypeError: Cannot interpret '2' as a data type
```

If a larger 2d `ndarray` is examined:

```python
In [77]: mat1 = np.arange(20).reshape(5, 4)
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(5, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 0  1  2  3]<br>&nbsp;[ 4  5  6  7]<br>&nbsp;[ 8  9 10 11]<br>&nbsp;[12 13 14 15]<br>&nbsp;[16 17 18 19]]</td>
  </tr>                  
</table>

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5d; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #a33c89; color: #ffffff;">6</td>
    <td style="padding: 8px; background-color: #a33c94; color: #ffffff;">7</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #983cab; color: #ffffff;">10</td>
    <td style="padding: 8px; background-color: #8d3cab; color: #ffffff;">11</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #6b3cab; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #3f3cab; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>

Indexing of a single element can be carried out: by indexing using the row index and then the column index:

```python
In [78]: mat1[3, 2]
Out[78]: np.int64(14)
```

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5d; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #a33c89; color: #ffffff;">6</td>
    <td style="padding: 8px; background-color: #a33c94; color: #ffffff;">7</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #983cab; color: #ffffff;">10</td>
    <td style="padding: 8px; background-color: #8d3cab; color: #ffffff;">11</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #3f3cab; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>

A `tuple` of `rows` can be selected:

```python
In [79]: mat1[(1, 3), 2]
Out[79]: array([ 6, 14])
```

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5d; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">6</td>
    <td style="padding: 8px; background-color: #a33c94; color: #ffffff;">7</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #983cab; color: #ffffff;">10</td>
    <td style="padding: 8px; background-color: #8d3cab; color: #ffffff;">11</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #3f3cab; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>


A colon `:` can be used to select all rows:

```python
In [80]: mat1[:, 2]
Out[80]: array([ 2,  6, 10, 14, 18])
```

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">6</td>
    <td style="padding: 8px; background-color: #a33c94; color: #ffffff;">7</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">10</td>
    <td style="padding: 8px; background-color: #8d3cab; color: #ffffff;">11</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>


Note indexing all rows and a single column, creates a vector i.e. a 1d `ndarray`. The dimensions can be kept using:

```python
In [81]: mat1[:, 2][:, np.newaxis]
Out[81]: 
array([[ 2],
       [ 6],
       [10],
       [14],
       [18]])
```

If an equally lengthed `tuple` is supplied for row and column selection, the corresponding elements on each `tuple` will be used to specify the indexes for a value in a `ndarray`. The output will be a 1d `ndarray` of the selected values

```python
In [82]: mat1[(1, 2), (2, 3)]
Out[82]: array([ 6, 11])

In [83]: np.array([mat1[1, 2], mat1[2, 3]])
Out[83]: array([ 6, 11])
```

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5d; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">6</td>
    <td style="padding: 8px; background-color: #a33c94; color: #ffffff;">7</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #983cab; color: #ffffff;">10</td>
    <td style="padding: 8px; background-color: #8d3cab; color: #ffffff;">11</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #6b3cab; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #3f3cab; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">3</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5d; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #a33c89; color: #ffffff;">6</td>
    <td style="padding: 8px; background-color: #a33c94; color: #ffffff;">7</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #983cab; color: #ffffff;">10</td>
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">11</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #6b3cab; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #3f3cab; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>

The colon `:` is an abbreviation for `start:stop:step` where the default `start=0`, `stop=len(dimension)` and `step=1` and is inclusive of the `start` and exclusive of the `stop`. These can be used to select a sub 2d `ndarray`:

```python
In [84]: mat1[1:3, 2:4]
Out[84]: 
array([[ 6,  7],
       [10, 11]])
```

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">3</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5d; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">6</td>
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">7</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">10</td>
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">11</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #6b3cab; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #3f3cab; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>


The index before index `0` is index `-1` which is the last value along the axis. The negative index can be calculated from the positive index by subtracting the index by the number of elements along that axis:

```python
In [85]: mat1[3, 2]
Out[85]: np.int64(14)

In [86]: nrows, ncols = mat1.shape

In [87]: mat1[3-nrows, 2-ncols]
Out[87]: np.int64(14)

In [88]: mat1[-2, -2]
Out[88]: np.int64(14)
```

For clarity the negative indexes are shown below:

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0 (-4)</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1 (-3)</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2 (-2)</th> 
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3 (-1)</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0 (-5)</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5d; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1 (-4)</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #a33c89; color: #ffffff;">6</td>
    <td style="padding: 8px; background-color: #a33c94; color: #ffffff;">7</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2 (-3)</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #983cab; color: #ffffff;">10</td>
    <td style="padding: 8px; background-color: #8d3cab; color: #ffffff;">11</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">3 (-2)</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4 (-1)</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #3f3cab; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>

The data model `__setitem__` is defined and therefore a selection of the `ndarray` can be assigned to a new value of equal dimensions:

```python
In [89]: mat1[1:3, 2:4] = np.full((2, 2), fill_value=9)
```

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th> 
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">3</th>               
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">0</td>  
    <td style="padding: 8px; background-color: #a33c51; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5d; color: #ffffff;">2</td>
    <td style="padding: 8px; background-color: #a33c68; color: #ffffff;">3</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c73; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #a33c7e; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">9</td>
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">9</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33ca0; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">9</td>
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">9</td>         
  </tr>  
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">3</th>
    <td style="padding: 8px; background-color: #823cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #773cab; color: #ffffff;">13</td>  
    <td style="padding: 8px; background-color: #6b3cab; color: #ffffff;">14</td>
    <td style="padding: 8px; background-color: #603cab; color: #ffffff;">15</td>         
  </tr>    
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">4</th>
    <td style="padding: 8px; background-color: #553cab; color: #ffffff;">16</td>  
    <td style="padding: 8px; background-color: #4a3cab; color: #ffffff;">17</td>  
    <td style="padding: 8px; background-color: #3f3cab; color: #ffffff;">18</td>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">19</td>         
  </tr>      
  </table>

If the following `ndarray` is instantiated:

```python
In [90]: vec = np.arange(int(1e6))
```

It can be indexed into using a slice with a positive `start` and `stop`:

```python
In [91]: vec[0:3]
Out[91]: array([0, 1, 2])
```

The orthogonal grid `ogrid` can be indexed into using a slice with a positive `start` and `stop`. With these positive values it can be conceptualised as being similar to the `ndarray` above:

```python
In [92]: np.ogrid[0:3]
Out[92]: array([0, 1, 2])
```

The orthogonal grid behaves slightly differently with a negative `start` or `stop`, instead of using a negative index to retrieve values, negative values are taken from the orthgonal grid:

```python
In [93]: array([], dtype=int64)
Out[93]: array([])

In [94]: np.ogrid[-2:3]
Out[94]: array([-2, -1,  0,  1,  2])
```

The mesh grid is used to create 2d `ndarray` of `x` and `y` data:

```python
In [95]: x, y = np.mgrid[-2:2:1, -5:5:1]
In [96]: x
Out[96]:
array([[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1]])
In [97]: y
Out[97]: 
array([[-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
       [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
       [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
       [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4]])
```

This can later be used to calculate `z` which has a relationship dependent on `x` and `y`:

```python
In [98]: z = x + y
       : z
Out[98]: 
array([[-7, -6, -5, -4, -3, -2, -1,  0,  1,  2],
       [-6, -5, -4, -3, -2, -1,  0,  1,  2,  3],
       [-5, -4, -3, -2, -1,  0,  1,  2,  3,  4],
       [-4, -3, -2, -1,  0,  1,  2,  3,  4,  5]])
```

The function `meshgrid` has a similar return value but requires two starting vectors. Notice that `x` is a row vector and `y` is a column vector:

```python
In [99]: x_row = np.array([0, 1, 2])[np.newaxis, :]
       : x_row
Out[99]: array([[0, 1, 2]])

In [100]: y_col = np.array([0, 10, 20, 30])[:, np.newaxis]
       : y_col
Out[100]: 
array([[ 0],
       [10],
       [20],
       [30]])

In [101]: x, y = np.meshgrid(x_row, y_col)

In [102]: x
Out[102]: 
array([[0, 1, 2],
       [0, 1, 2],
       [0, 1, 2],
       [0, 1, 2]])

In [103]: y
Out[103]: 
array([[ 0,  0,  0],
       [10, 10, 10],
       [20, 20, 20],
       [30, 30, 30]])
```

If the following 2d `ndarray` is instantiated:

```python
In [104]: mat1 = np.arange(1, 7).reshape((3, 2))
Out[104]: 
array([[1, 2],
       [3, 4],
       [5, 6]])
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2]<br>&nbsp;[ 3  4]<br>&nbsp;[ 5  6]]</td>
  </tr>                  
</table>

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c71; color: #ffffff;">2</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c9b; color: #ffffff;">3</td>  
    <td style="padding: 8px; background-color: #883cab; color: #ffffff;">4</td>          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #5e3cab; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">6</td>      
  </tr>     
  </table>

The function `indices` can be used to retrieve the rows and columns required for each element in `mat1`:

```python
In [105]: rows, cols = np.indices(mat1.shape)

In [106]: rows
Out[106]: 
array([[0, 0],
       [1, 1],
       [2, 2]])

In [107]: cols
Out[107]: 
array([[0, 1],
       [0, 1],
       [0, 1]])
```

If the `mat1` is indexed into using all of its indices, all of the elements in `mat1` are selected:

```python
In [108]: mat1[rows, cols]
Out[108]: 
array([[1, 2],
       [3, 4],
       [5, 6]])
```

The functions `zeros`, `ones` and `full` have already been examined and require a `shape` and optional `dtype`. The `shape` and `dtype` can be specified using the `shape` and `dtype` attributes from an existing `ndarray`. The complementary functions `zeros_like`, `ones_like` and `full_like` give short-hand ways of doing this:

```python
In [109]: np.zeros(mat1.shape, dtype=mat1.dtype)
Out[109]: 
array([[0, 0],
       [0, 0],
       [0, 0]])

In [110] np.zeros_like(mat1)
Out[110]: 
array([[0, 0],
       [0, 0],
       [0, 0]])
```

The functions `empty` and `empty_like` should not be confused with `zeros` and `zeros_like`. An empty `ndarray` is assigned a memory location and the memory location is not cleared before use. The uninitialised values are simply what was left at these `bytes` when they were previously used before being designated garbage:

```python
In [111]: np.empty((3, 2))
Out[111]: 
array([[0.00000000e+000, 1.35392324e-311],
       [8.48798316e-314, 5.56276953e-309],
       [1.90135812e-246, 1.05699581e-307]])
```

Instantiation of an empty `ndarray` is faster than creating an empty `ndarray` and initialising all the values to `0` and can give a performance boost in some applications.

The function `identity` gives a square identity matrix, which has `1` at the diagonal and `0` elsewhere. This is important for linear algebra:

```python
In [112]: np.identity(5)
Out[112]: 
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
```

The related function `eye` also gives a square identity matrix but there is an option to specify a second dimension which will essentially create the square matrix and then index a rectangular section from it:

```python
In [113]: np.eye(5)
Out[113]: 
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])

In [114]: np.eye(5, 4)
Out[114]: 
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.],
       [0., 0., 0., 0.]])
```

These functions have the optional parameter `dtype`, consistent with the other `ndarray` creation functions.

The `diag` function will create a square matrix using the specified diagonal and have zeros elsewhere:

```python
In [115]: np.diag([1, 2, 3, 4])
Out[115]: 
array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]])
```

## ndarray manipulation (Collection-like)

If the kernel is restarted and `numpy` is imported:

```python
In [116]: exit
In [1]: import numpy as np
```

The `Collection`-like `ndarray` manipulation methods of the `ndarray` can be examined:

```python
In [2]: np.ndarray.
# 🔗 Collection Identifiers
#     - __getitem__               : Allows indexing (obj[index]).
#     - __setitem__               : Allows setting an item (obj[index] = value).
#     - __iter__                  : Returns an iterator for the ndarray.
#     - __len__                   : Returns the length of the ndarray.
#     - __contains__              : Checks if an item is in the ndarray (in operator).
#     - copy                      : Returns a shallow copy of the ndarray.

# 🔗 Supplementary Collection Identifiers
#     - ndim                      : The number of dimensions of the ndarray.
#     - shape                     : The shape of the ndarray.
#     - size                      : The number of elements in the ndarray.
#     - itemsize                  : The size of one array element in bytes.
#     - nbytes                    : The total number of bytes consumed by the ndarray.
#     - T                         : The transpose of a 2D ndarray.
#     - flat                      : The flattened iterator of the ndarray.
#     - diagonal                  : Returns the diagonal of the ndarray.
#     - reshape                   : Changes the shape of the ndarray without altering data.
#     - flatten                   : Flattens the ndarray into a 1D array.
#     - ravel                     : Returns a flattened view of the ndarray.
#     - transpose                 : Permutes the axes of the ndarray.
#     - repeat                    : Repeats elements of the ndarray.
#     - swapaxes                  : Interchanges two axes of the ndarray.
#     - item                      : Copies a single element from the ndarray.
#     - squeeze                   : Removes single-dimensional entries from the shape.
#     - take                      : Selects elements from the ndarray based on indices.
#     - compress                  : Selects elements using a condition mask.
#     - fill                      : Fills the ndarray with a scalar value.
```

The `Collection`-like attributes `ndim`, `shape`, `size`, `itemsize`, `nbytes` as well as the datamodel method `__len__` have already been explored. The remaining identifiers are immutable methods which are also complemented by functions:

```python
In [2]: np.
 📈 Array Manipulation:
#     - diagonal                  : Returns the diagonal of the ndarray.
#     - reshape                   : Reshapes an array without changing its data.
#     - transpose                 : Permutes the axes of an array.
#     - flatten                   : Returns a flattened copy of an array.
#     - ravel                     : Flattens an array into 1D.
#     - shares_memory             : Checks if two arrays share the same memory block.
#     - concatenate               : Joins arrays along an axis.
#     - repeat                    : Repeats elements of the ndarray.
#     - tile                      : Constructs an array by repeating the input array a specified number 
#                                   of times along each axis.
#     - stack                     : Joins a sequence of arrays along a new axis.
#     - hstack                    : Stacks arrays in sequence horizontally (column-wise).
#     - vstack                    : Stacks arrays in sequence vertically (row-wise).
#     - dstack                    : Stacks arrays in sequence depth-wise (along the third axis).
#     - split                     : Splits an array into multiple sub-arrays.
#     - hsplit                    : Splits an array into multiple sub-arrays horizontally (column-wise).
#     - vsplit                    : Splits an array into multiple sub-arrays vertically (row-wise).
#     - dsplit                    : Splits an array into multiple sub-arrays along the third axis (depth-wise).
#     - pad                       : Pads an array with values.
#     - swapaxes                  : Interchanges two axes of an array.
#     - moveaxis                  : Moves axes to new positions.
#     - squeeze                   : Removes single-dimensional entries from the shape of an array.
#     - expand_dims               : Expands the shape of an array.
#     - take                      : Selects elements from the ndarray based on indices.
#     - take_along_axis           : Selects elements from an array along an axis using an array of indices.
#     - compress                  : Selects elements using a condition mask.
```

All of these methods are immutable. The immutable method and the function carry out similar behaviour. Generally the method is preferenced, as the code is more succinct:

```python
In [2]: mat1 = np.arange(20)

In [3]: mat1.reshape((5, 4))
Out[3]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])

In [4]: np.reshape(mat1, (5, 4))
Out[4]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
```

Functions like `concatenate`, `stack`, `split`, and `pad` are designed to operate across multiple `ndarray` instances. These functions are not tied to a single instance and therefore not available as a method. Supposing the following `3` 2d `ndarray` instances are instantiated:

```python
In [5]: mat1 = np.array([[1, 2], 
      :                  [3, 4]])
      
In [6]: mat2 = np.array([[5, 6], 
      :                  [7, 8]])      

In [7]: mat3 = np.array([[ 9, 10], 
      :                  [11, 12]])   
```

They can be concatenated along `axis` `0` or `1`: 

```python
In [8]: np.concatenate((mat1, mat2, mat3), axis=0)
Out[8]: 
array([[ 1,  2],
       [ 3,  4],
       [ 5,  6],
       [ 7,  8],
       [ 9, 10],
       [11, 12]])

In [9]: np.concatenate((mat1, mat2, mat3), axis=1)
Out[9]: 
array([[ 1,  2,  5,  6,  9, 10],
       [ 3,  4,  7,  8, 11, 12]])
```

Recall the `shape` `tuple` has the form `(nrows, ncols)`. Index `0` of the `shape` `tuple` operates along `axis` `0` and specifies the number of rows:

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c8d; color: #ffffff;">2</td>  
          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #7a3cab; color: #ffffff;">3</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">4</td>        
  </tr>
  </table>

Index `1` of the `shape` `tuple` operates along axis `1` and specifies the number of columns:

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">1</th>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c8d; color: #ffffff;">2</td>  
          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #7a3cab; color: #ffffff;">3</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">4</td>        
  </tr>
  </table>

For the 2d `ndarrays` above, the functions vertical stack `vstack` and horizontal stack `hstack` are more readible:

```python
In [10]: np.vstack((mat1, mat2, mat3))
Out[10]: 
array([[ 1,  2],
       [ 3,  4],
       [ 5,  6],
       [ 7,  8],
       [ 9, 10],
       [11, 12]])

In [11]: np.hstack((mat1, mat2, mat3))
Out[11]: 
array([[ 1,  2,  5,  6,  9, 10],
       [ 3,  4,  7,  8, 11, 12]])
```

There is also the function `stack` which stacks each of these arrays over a new dimension:

```python
In [12]: np.stack((mat1, mat2, mat3))
Out[12]: 
array([[[ 1,  2],
        [ 3,  4]],

       [[ 5,  6],
        [ 7,  8]],

       [[ 9, 10],
        [11, 12]]])
```

Notice there are now three outer square brackets `[[[`, indicating a 3d `ndarray`. This can be conceptualised as a `book` with `sheet0=mat1`, `sheet1=mat2`, and `sheet2=mat3`:

```python:
In [13]: book = np.stack((mat1, mat2, mat3))
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">book</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 2, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[[ 1  2]<br>&nbsp;&nbsp;[ 3  4]]<br>&nbsp;[[ 5  6]<br>&nbsp;&nbsp;[ 7  8]]<br>&nbsp;[[ 9 10]<br>&nbsp;&nbsp;[11 12]]]</td>
  </tr>                  
</table>

`book` is a 3d `ndarray` with the `shape` `tuple`:

```python
In [14]: nsheets, nrows, ncols = book.shape
```

When visualised axis `0` is selected by default and `sheet0` `book[0, :, :]` displays:

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">book - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c8d; color: #ffffff;">2</td>     
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #7a3cab; color: #ffffff;">3</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">4</td>        
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Axis:<br>0</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Shape:<br>(3, 2, 2)</td>    
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Index: 0<br>Slicing [0, :, :]</td>        
  </tr>
  </table>

`sheet1`, `book[1, :, :]` can be examined: 

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">book - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #a33c8d; color: #ffffff;">6</td>     
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #7a3cab; color: #ffffff;">7</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">8</td>        
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Axis:<br>0</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Shape:<br>(3, 2, 2)</td>    
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Index: 1<br>Slicing [1, :, :]</td>        
  </tr>
  </table>

`sheet2`, `book[2, :, :]` can be examined: 

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">book - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>       
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #a33c8d; color: #ffffff;">10</td>     
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #7a3cab; color: #ffffff;">11</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">12</td>        
  </tr>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Axis:<br>0</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Shape:<br>(3, 2, 2)</td>    
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Index: 2<br>Slicing [2, :, :]</td>        
  </tr>
  </table>

`axis1` can be selected:

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">book - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>             
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c5e; color: #ffffff;">2</td>          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33ca5; color: #ffffff;">5</td>    
    <td style="padding: 8px; background-color: #923cab; color: #ffffff;">6</td>    
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #4b3cab; color: #ffffff;">9</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">10</td>    
  </tr>  
  <tr>
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Axis:<br>1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Shape:<br>(3, 2, 2)</td>    
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Index: 0<br>Slicing [:, 0, :]</td>        
  </tr>
  </table>

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">book - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>             
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">3</td>  
    <td style="padding: 8px; background-color: #a33c5e; color: #ffffff;">4</td>          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33ca5; color: #ffffff;">7</td>    
    <td style="padding: 8px; background-color: #923cab; color: #ffffff;">8</td>    
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #4b3cab; color: #ffffff;">11</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">12</td>    
  </tr>  
  <tr>
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Axis:<br>1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Shape:<br>(3, 2, 2)</td>    
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Index: 1<br>Slicing [:, 1, :]</td>        
  </tr>
  </table>

`axis2` can be selected:

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">book - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>             
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #a33c71; color: #ffffff;">3</td>          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c9b; color: #ffffff;">5</td>    
    <td style="padding: 8px; background-color: #883cab; color: #ffffff;">7</td>    
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #5e3cab; color: #ffffff;">9</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">11</td>    
  </tr>  
  <tr>
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Axis:<br>2</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Shape:<br>(3, 2, 2)</td>    
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Index: 0<br>Slicing [:, :, 0]</td>        
  </tr>
  </table>

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">book - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>             
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">2</td>  
    <td style="padding: 8px; background-color: #a33c71; color: #ffffff;">4</td>          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c9b; color: #ffffff;">6</td>    
    <td style="padding: 8px; background-color: #883cab; color: #ffffff;">8</td>    
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #5e3cab; color: #ffffff;">10</td>    
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">12</td>    
  </tr>  
  <tr>
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Axis:<br>2</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Shape:<br>(3, 2, 2)</td>    
    <td style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">Index: 1<br>Slicing [:, :, 1]</td>        
  </tr>
  </table>

The method `swapaxes` can be used to return the view of axis `1`: 

```python
In [15]: book.swapaxes(0, 1)
Out[15]: 
array([[[ 1,  2],
        [ 5,  6],
        [ 9, 10]],

       [[ 3,  4],
        [ 7,  8],
        [11, 12]]])
```

To get the view from axis `2`:

```python
In [16]: book.swapaxes(0, 1).swapaxes(0, 2)
Out[16]: 
array([[[ 1,  3],
        [ 5,  7],
        [ 9, 11]],

       [[ 2,  4],
        [ 6,  8],
        [10, 12]]])
```

The function `moveaxis` can also be used to do this:

```python
In [17]: np.moveaxis(book1, 2, 0)
Out[17]: 
array([[[ 1,  3],
        [ 5,  7],
        [ 9, 11]],

       [[ 2,  4],
        [ 6,  8],
        [10, 12]]])
```

These three arrays can also be stacked using the depth stack function `dstack` which is also a 3d stack. Its docstring can be examined:

```python
In [18]: np.dstack?
Call signature:  np.dstack(*args, **kwargs)

Docstring:      
Stack arrays in sequence depth wise (along third axis).

This is equivalent to concatenation along the third axis after 2-D arrays
of shape `(M,N)` have been reshaped to `(M,N,1)` and 1-D arrays of shape
`(N,)` have been reshaped to `(1,N,1)`. Rebuilds arrays divided by
`dsplit`.
```

```python
In [19]: mat1.reshape(mat1.shape + (1, ))
Out[19]: 
array([[[1],
        [2]],

       [[3],
        [4]]])

In [20]: mat2.reshape(mat2.shape + (1, ))
Out[20]: 
array([[[5],
        [6]],

       [[7],
        [8]]])

In [21]: mat3.reshape(mat3.shape + (1, ))
Out[21]: 
array([[[ 9],
        [10]],

       [[11],
        [12]]])

In [22]: np.dstack((mat1, mat2, mat3))
Out[22]: 
array([[[ 1,  5,  9],
        [ 2,  6, 10]],

       [[ 3,  7, 11],
        [ 4,  8, 12]]])
```

Each of the `stack` functions has a corresponding `split` function which reverses the behaviour:

```python
In [23]: sheet0, sheet1, sheet2 = np.split(book1, 3)

In [24]: sheet0
Out[24]: 
array([[[1, 2],
        [3, 4]]])

In [25]: sheet1
Out[25]: 
array([[[5, 6],
        [7, 8]]])

In [26]: sheet2
Out[26]: 
array([[[ 9, 10],
        [11, 12]]])
```

Note each of the sheets above is a 3d `ndarray`, i.e. a book with a single sheet in it, this extra dimension can be squeezed:

```python
In [27]: sheet1.squeeze()
Out[27]: 
array([[5, 6],
       [7, 8]])
```

If `mat1` is examined, its dimensions can be expanded into 3d using the function expand dimensions `expand_dims`:

```python
In [28]: mat1
Out[28]: 
array([[1, 2],
       [3, 4]])

In [29]: np.expand_dims(mat1, 0)
Out[29]: 
array([[[1, 2],
        [3, 4]]])
```

The method `repeat` can be used to repeat values along an `axis`:

```python
In [30]: mat1
Out[30]: 
array([[1, 2],
       [3, 4]])

In [31]: mat1.repeat(3, axis=0)
Out[31]: 
array([[1, 2],
       [1, 2],
       [1, 2],
       [3, 4],
       [3, 4],
       [3, 4]])
```

The function `tile` can be used to tile the `ndarray` using a `shape` `tuple`:

```python
In [32]: np.tile(mat1, (3, 1))
Out[32]: 
array([[1, 2],
       [3, 4],
       [1, 2],
       [3, 4],
       [1, 2],
       [3, 4]])

In [33]: np.tile(mat1, (3, 2))
Out[33]: 
array([[1, 2, 1, 2],
       [3, 4, 3, 4],
       [1, 2, 1, 2],
       [3, 4, 3, 4],
       [1, 2, 1, 2],
       [3, 4, 3, 4]])
```

In a `ndarray` the `+` and `*` operators are reserved for numeric operations and the function `concatenate` and method `repeat` replace the `Collection`-like functionality.

The method `transpose` can be used to transpose a column into a row or a row into a column however it is more common to use the attribute `T`.

The method `diagonal` and function `diag` should not be confused with one another. The method `diagonal` retrieves the diagonal from a 2d `ndarray` and returns it as a 1d `ndarray`:

```python
In [34]: mat1
Out[34]: 
array([[1, 2],
       [3, 4]])

In [35]: mat1.diagonal()
Out[35]: array([1, 4])
```

Recall in contrast the function `diag` is used to create a square matrix (2d `ndarray`) from a 1d `ndarray`:

```python
In [36]: np.diag([1, 2, 3, 4])
Out[36]: 
array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]])
```

The function `pad` can be used to pad an `ndarray`:

```python
In [37]: mat1
Out[37]: 
array([[1, 2],
       [3, 4]])

In [38]: np.pad(mat1, ((1, 2), (3, 4)))
Out[38]: 
array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 2, 0, 0, 0, 0],
       [0, 0, 0, 3, 4, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]])
```

For `pad` the `shape` `tuple` has the form `(rows, cols)` however `rows` is itself a 2-element `tuple` as rows can be padded before the original data and after the original data. `cols` likewise is a 2-element `tuple` and columns can be padded before and after the original data.

`rows` can be set to `(0, 0)` allowing only the columns to be padded. `mode` is an optional parameter and has a default value of `'constant'`. The constant itself is set with another optional parameter `constant_values` which has a default value of `0`:

```python
In [39]: np.pad(mat1, ((0, 0), (1, 1)))
Out[39]: 
array([[0, 1, 2, 0],
       [0, 3, 4, 0]])

In [40]: np.pad(mat1, ((0, 0), (1, 1)), mode='constant', constant_values=9)
Out[40]: 
array([[9, 1, 2, 9],
       [9, 3, 4, 9]])
```

The `mode` can also be set to `'edge'` or `'wrap'` or a statistical term like `'minimum'`, `'maximum'`, `'median'`, `mean'`:

```python
In [41]: np.pad(mat1, ((0, 0), (1, 1)), mode='edge')
Out[41]: 
array([[1, 1, 2, 2],
       [3, 3, 4, 4]])

In [42]: np.pad(mat1, ((0, 0), (1, 1)), mode='wrap')
Out[42]: 
array([[2, 1, 2, 1],
       [4, 3, 4, 3]])

In [43]: np.pad(mat1, ((0, 0), (1, 1)), mode='minimum')
Out[43]: 
array([[1, 1, 2, 1],
       [3, 3, 4, 3]])

In [44]: np.pad(mat1, ((0, 0), (1, 1)), mode='maximum')
Out[44]: 
array([[2, 1, 2, 2],
       [4, 3, 4, 4]])

In [45]: np.pad(mat1, ((0, 0), (1, 1)), mode='median')
Out[45]: 
array([[2, 1, 2, 2],
       [4, 3, 4, 4]])

In [46]: np.pad(mat1, ((0, 0), (1, 1)), mode='mean')
Out[46]: 
array([[2, 1, 2, 2],
       [4, 3, 4, 4]])

In [47]: np.pad(mat1, ((0, 0), (1, 1)), mode='linear_ramp')
Out[47]: 
array([[0, 1, 2, 0],
       [0, 3, 4, 0]])
```

Some of the statistical terms generally require more data i.e. a larger `ndarray`.

The method `flatten`, flattens an `ndarray` to a 1d vector:

```python
In [48]: mat1
Out[48]: 
array([[1, 2],
       [3, 4]])

In [49]: mat1.flatten()
Out[49]: array([1, 2, 3, 4])
```

Notice the first row is shown in the flattened 1d `ndarray` and then the second row is appended to it. This is a known as a row-major order. 

The parameter `order` has the default value `'C'`, in this case C comes from the C programming language which uses row-major order. Another option is `'F'`, in this case F comes from the Fortran programming language which uses column-major order. Notice the flattened array takes the elements of the first column, then appends the elements of the second column:

```python
In [50]: mat1.flatten(order='C')
Out[50]: array([1, 2, 3, 4])

In [51]: mat1.flatten(order='F')
Out[51]: array([1, 3, 2, 4])
```

Another option is `'K'` which stands for keep and relies on the `order` being specified when the `ndarray` is instantiated:

```python
In [52]: matc = np.array([[1, 2], [3, 4]]) # order='C' is the default
       : matf = np.array([[1, 2], [3, 4]], order='F')

In [53]: matc.flatten(order='K')
Out[53]: array([1, 2, 3, 4])

In [54]: matf.flatten(order='K')
Out[54]: array([1, 3, 2, 4])
```

The `order` parameter is normally onlu used for compatibility with other programming such as Fortran and Matlab. For most use cases, the optional `order` parameter is unspecified and therefore uses its default value `C`.

The `ravel` method, at first glance appears to be similar to the `flatten` method:

```python
In [55]: mat1.flatten()
Out[55]: array([1, 2, 3, 4])

In [56]: mat1.ravel()
Out[56]: array([1, 2, 3, 4])
```

However there is a subtle difference in the return value. The `flatten` method returns a flattened copy of the original `ndarray` which uses unique memory:

```python
In [57]: np.shares_memory(mat1, mat1.flatten())
Out[57]: False
```

The `ravel` method returns a memory view of the original `ndarray` which uses the same memory:

```python
In [58]: np.shares_memory(mat1, mat1.ravel())
Out[58]: True
```

A memory view is often preferable when a large 2d `ndarray` is required in the format of a 1d `ndarray`. This is commonly required, for example in a plotting function.

The attribute `flat` is the flattened iterator of the `ndarray`:

```python
In [59]: mat1
Out[59]:
array([[1, 2],
       [3, 4]])

In [60]: forward = mat1.flat

In [61]: next(forward)
Out[61]: np.int64(1)

In [62]: next(forward)
Out[62]: np.int64(2)

In [63]: next(forward)
Out[63]: np.int64(3)

In [64]: next(forward)
Out[64]: np.int64(4)

In [65]: next(forward)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In[65], line 1
----> 1 next(forward)

StopIteration: 
```

If the flattened iterator is assigned to a `list` or `ndarray` of equal length, all the elements will be replaced:

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2]<br>&nbsp;[ 3  4]]</td>
  </tr>                  
</table>

```python
In [66]: id(mat1)
Out[66]: 1685025693712

In [67]: mat1.flat = [1, 6, 5, 4]
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  6]<br>&nbsp;[ 5  4]]</td>
  </tr>                  
</table>

Notice that the identification of `mat1` is changed and therefore `mat1` has been mutated in place:

```python
In [68]: id(mat1)
Out[68]: 1685025693712
```

If the following 2d `ndarray` is instantiated:

```python
In [69]: mat1 = np.arange(1, 7).reshape((3, 2))
Out[69]: 
array([[1, 2],
       [3, 4],
       [5, 6]])
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2]<br>&nbsp;[ 3  4]<br>&nbsp;[ 5  6]]</td>
  </tr>                  
</table>

<table style="width: 30%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="3" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat1 - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">2</td>              
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #a33c9b; color: #ffffff;">3</td>  
    <td style="padding: 8px; background-color: #883cab; color: #ffffff;">4</td>          
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #ffcc3e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">5</td>  
    <td style="padding: 8px; background-color: #e94e10; color: #ffffff;">6</td>      
  </tr>     
  </table>

The following selection can be made using indexing:

```python
In [70]: mat1[(0, 2), :]
Out[70]: 
array([[1, 2],
       [5, 6]])
```

The method `take` is similar and operates along a specified `axis`:

```python
In [71]: mat1.take((0, 2), axis=0)
Out[71]: 
array([[1, 2],
       [5, 6]])
```

The function `take_along_axis` uses an array of indices to take values along an `axis` using the provided indices:

```python
In [72]: mat1
Out[72]: 
array([[1, 2],
       [3, 4],
       [5, 6]])

In [73]: indices = np.array([[2, 1], 
                             [1, 2],
                             [0, 0]])

In [74]: np.take_along_axis(mat1, indices, axis=0)
Out[74]: 
array([[5, 4],
       [3, 6],
       [1, 2]])
```

Index selection along an `axis` can also be carried out using a boolean vector of equal length to the `axis`:

```python
In [75]: mat1
Out[75]: 
array([[1, 2],
       [3, 4],
       [5, 6]])

In [76]: selection = (True, False, True)

In [77]: mat1[selection, :]
Out[77]: 
array([[1, 2],
       [5, 6]])
```

The `compress` method is similar to `take` but uses a `bool` vector to specify index selection:

```python 
In [78]: mat1.compress(selection, axis=0)
Out[78]: 
array([[1, 2],
       [5, 6]])
```

The `fill` method is mutable and will fill an existing `ndarray` with a specified fill instance:

```python 
In [79]: mat1
Out[79]: 
array([[1, 2],
       [3, 4],
       [5, 6]])

In [80]: mat1.fill(9)
```

Notice there is no return value and instead `mat1` is updated in place.

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat1</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 2)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 9  9]<br>&nbsp;[ 9  9]<br>&nbsp;[ 9  9]]</td>
  </tr>                  
</table>

```python
In [81]: exit
```

## axis, shape and negative index

So far 1d, 2d and 3d `ndarray` instances have been explored:

```python
In [1]: import numpy as np
In [2]: vec = np.array([1, 2, 3, 4])
In [3]: row = np.array([[1, 2, 3, 4]])
In [4]: col = np.array([[1],
      :                 [2],
      :                 [3],
      :                 [4]])
In [5]: mat = np.array([[1, 2, 3, 4],
      :                 [5, 6, 7, 8]])
In [6]: book = np.array([[[1.0, 2.0, 3.0, 4.0],
      :                   [5.0, 6.0, 7.0, 8.0]],
      :                  
      :                  [[1.1, 2.1, 3.1, 4.1],
      :                   [5.1, 6.1, 7.1, 8.1]],
      :
      :                  [[1.2, 2.2, 3.2, 4.2],
      :                   [5.2, 6.2, 7.2, 8.2]]])
```

The shape of all of these can be seen on the Variable Explorer:

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">vec</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(4, )</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[ 1  2  3  4]</td>
  </tr>    
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">row</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(1, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2  3  4]]</td>
  </tr>        
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">col</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(4, 1)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[1]<br>&nbsp;[2]<br>&nbsp;[3]<br>&nbsp;[4]]</td>
  </tr> 
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2  3  4]<br>&nbsp;[ 5  6  7  8]]</td>
  </tr>      
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">book</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of float64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 2, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[[ 1.0  2.0  3.0  4.0]<br>&nbsp;&nbsp;[ 5.0  6.0  7.0  8.0]]<br><br>&nbsp;&nbsp;[[ 1.1  2.1  3.1  4.1]<br>&nbsp;&nbsp;&nbsp;[ 5.1  6.1  7.1  8.1]]<br><br>&nbsp;&nbsp;[[ 1.2  2.2  3.2  4.2]<br>&nbsp;&nbsp;&nbsp;[ 5.2  6.2  7.2  8.2]]]</td>
  </tr>                          
</table>

If `vec`, `row` and `col` are compared and conceptualised in the collapsed view as being `list`-like structures. Notice in `vec` that the outer `list` has `4` elements and therefore a shape `(4,)`. `row` has `1` element in its outer `list`, a nested `list` and this nested `list` has `4` elements and therefore the shape is `(1, 4)`. `col` has `4` elements in its outer `list`, each is a `list` with `1` element each and therefore the shape is `(4, 1)`:

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">vec</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(4, )</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[ 1  2  3  4]</td>
  </tr>    
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">row</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(1, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2  3  4]]</td>
  </tr>        
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">col</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(4, 1)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[1]<br>&nbsp;[2]<br>&nbsp;[3]<br>&nbsp;[4]]</td>
  </tr> 
</table>

If `vec`, `mat` and `book` are compared, notice the `shape` `tuples` have `1` element, `2` elements and `3` elements indicating that `vec` is a 1d `ndarray`, `mat` is a 2d `ndarray` and `book` is a 3d `ndarray`.

`vec` has an outer `list` with `4` elements. This gives a `shape` `tuple` of `(4,)` which of the form `(ncols,)`.

`mat` has an outer `list` with `2` elements that are each a nested `list`. Each nested `list` has `4` elements. This gives a `shape` `tuple` of `(2, 4)` which of the form `(nrows, ncols)`.

`book` has an outer `list` with `3` elements that are each a nested `list` (`axis` `0`). Each nested `list` has `2` elements that are each a nested `list` (`axis` `1`). Each of these nested `list` elements are in turn a nested `list` of `2` elements (`axis` `2`). This gives a `shape` `tuple` of `(3, 2, 4)` which of the form `(sheets, nrows, ncols)`.

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">vec</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(4, )</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[ 1  2  3  4]</td>
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[ 1  2  3  4]<br>&nbsp;[ 5  6  7  8]]</td>
  </tr>      
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">book</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of float64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(3, 2, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[[ 1.0  2.0  3.0  4.0]<br>&nbsp;&nbsp;[ 5.0  6.0  7.0  8.0]]<br><br>&nbsp;&nbsp;[[ 1.1  2.1  3.1  4.1]<br>&nbsp;&nbsp;&nbsp;[ 5.1  6.1  7.1  8.1]]<br><br>&nbsp;&nbsp;[[ 1.2  2.2  3.2  4.2]<br>&nbsp;&nbsp;&nbsp;[ 5.2  6.2  7.2  8.2]]]</td>
  </tr>                          
</table>

If the general form of each of the `shape` `tuple` for each dimension is examined:

|dimensions|shape tuple|
|---|---|
|1|(ncols,)|
|2|(nrows, ncols)|
|3|(nsheets, nrows, ncols)|

Notice that the outer dimension is always `axis` `0` and is different for each dimension of `ndarray`. This can be conceptualised as `{'1d': 'ncols', '2d': 'nrows', '3d: 'ncols'}`.

Indexing the `shape` `tuple` left to right, gives `axis=0`, `axis=1`, `axis=2`, ... and `axis=0` has a different meaning for each dimension of `ndarray`.

Indexing the `shape` `tuple` right to left, gives `axis=-1`, `axis=-2`, `axis=-3`. Notice `axis=-1` will always correspond to `ncols`, `axis=-2` will always correspond to `ncols` and `axis=-3` will always correspond to `nsheets`.

Humans visualise data only in 3 dimensions. Higher dimensions are harder to conceptualise, however the following folder structure can be visualised:

|dimensions|outer axis|description|shape tuple|
|---|---|---|---|
|1|-1|vector of columns|(ncols,)|
|2|-2|row of vectors|(nrows, ncols)|
|3|-3|sheet of rows|(nsheet, nrows, ncols)|
|4|-4|book of sheets|(nbook, nsheets, nrows, ncols)|
|5|-5|subfolder of books|(nbooks, nsheets, nsheets, nrows, ncols)|
|6|-6|folder of subfolders|(nsubfolders, nworkbooks, nsheets, nsheets, nrows, ncols)|

`axis=-2` row of vectors:

<img src='./images/img_001.png' alt='img_001' width='400'/>

`axis=-3` sheet of rows:

<img src='./images/img_002.png' alt='img_002' width='400'/>

`axis=-4` book of sheets:

<img src='./images/img_003.png' alt='img_003' width='400'/>

`axis=-5` subfolder of books:

<img src='./images/img_004.png' alt='img_004' width='400'/>

<img src='./images/img_005.png' alt='img_005' width='400'/>

`axis=-6` folder of subfolders:

<img src='./images/img_006.png' alt='img_006' width='400'/>

`axis` is a common optional parameter in many functions and methods. `axis=None` generally flattens the `ndarray` treating it as a vector (1d `ndarray`), `axis=-1` means an operation is being carried out along the `axis` that represents the number of columns, `axis=-2` means an operation is being carried out along the `axis` that represents the number of rows, `axis=-3` means an operation is being carried out along the `axis` that represents the number of sheets... This can be seen with the `concatenate` function:

```python

In [7]: book
Out[7]:
array([[[1. , 2. , 3. , 4. ],
        [5. , 6. , 7. , 8. ]],

       [[1.1, 2.1, 3.1, 4.1],
        [5.1, 6.1, 7.1, 8.1]],

       [[1.2, 2.2, 3.2, 4.2],
        [5.2, 6.2, 7.2, 8.2]]])

In [8]: book.shape
Out[8]: (3, 2, 4)

In [9]: np.concatenate((book, book), axis=None) # flatten
Out[9]: array([1. , 2. , 3. , 4. , 5. , 6. , 7. , 8. , 1.1, 2.1, 3.1, 4.1, 5.1,
       6.1, 7.1, 8.1, 1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 1. , 2. ,
       3. , 4. , 5. , 6. , 7. , 8. , 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1,
       8.1, 1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2])

In [11]: np.concatenate((book, book), axis=-1) # along column axis
Out[11]:
array([[[1. , 2. , 3. , 4. , 1. , 2. , 3. , 4. ],
        [5. , 6. , 7. , 8. , 5. , 6. , 7. , 8. ]],

       [[1.1, 2.1, 3.1, 4.1, 1.1, 2.1, 3.1, 4.1],
        [5.1, 6.1, 7.1, 8.1, 5.1, 6.1, 7.1, 8.1]],

       [[1.2, 2.2, 3.2, 4.2, 1.2, 2.2, 3.2, 4.2],
        [5.2, 6.2, 7.2, 8.2, 5.2, 6.2, 7.2, 8.2]]])

In [12]: np.concatenate((book, book), axis=-2) # along row axis 
Out[12]:
array([[[1. , 2. , 3. , 4. ],
        [5. , 6. , 7. , 8. ],
        [1. , 2. , 3. , 4. ],
        [5. , 6. , 7. , 8. ]],

       [[1.1, 2.1, 3.1, 4.1],
        [5.1, 6.1, 7.1, 8.1],
        [1.1, 2.1, 3.1, 4.1],
        [5.1, 6.1, 7.1, 8.1]],

       [[1.2, 2.2, 3.2, 4.2],
        [5.2, 6.2, 7.2, 8.2],
        [1.2, 2.2, 3.2, 4.2],
        [5.2, 6.2, 7.2, 8.2]]])

In [12]: np.concatenate((book, book), axis=-3) # along sheet axis
Out[12]:
array([[[1. , 2. , 3. , 4. ],
        [5. , 6. , 7. , 8. ]],

       [[1.1, 2.1, 3.1, 4.1],
        [5.1, 6.1, 7.1, 8.1]],

       [[1.2, 2.2, 3.2, 4.2],
        [5.2, 6.2, 7.2, 8.2]],

       [[1. , 2. , 3. , 4. ],
        [5. , 6. , 7. , 8. ]],

       [[1.1, 2.1, 3.1, 4.1],
        [5.1, 6.1, 7.1, 8.1]],

       [[1.2, 2.2, 3.2, 4.2],
        [5.2, 6.2, 7.2, 8.2]]])
```

The `insert` function when operated along `axis=-2` (the row axis) can be used to insert a row of an equal number of columns:

```python
In [13]: np.insert(book, 1, np.full((1, 4), 99), axis=-2)
Out[13]:
array([[[ 1. ,  2. ,  3. ,  4. ],
        [99. , 99. , 99. , 99. ],
        [ 5. ,  6. ,  7. ,  8. ]],

       [[ 1.1,  2.1,  3.1,  4.1],
        [99. , 99. , 99. , 99. ],
        [ 5.1,  6.1,  7.1,  8.1]],

       [[ 1.2,  2.2,  3.2,  4.2],
        [99. , 99. , 99. , 99. ],
        [ 5.2,  6.2,  7.2,  8.2]]])
```

Note `insert` is not defined as a mutable method for the `ndarray` and the function returns a new value.

```python
In [14]: exit
```

## sorting

Supposing the following 2d `ndarray` is instantiated:

```python
In [1]: import numpy as np
In [2]: mat = np.array([[12, 7, 3, 10],
      :                 [15, 9, 8, 6],
      :                 [1, 14, 4, 11]])
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[12  7  3 10]<br>&nbsp;[15  9  8  6]<br>&nbsp;[ 1 14  4 11]]</td>
  </tr>                              
</table>

<table style="width: 60%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>          
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">2</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>                 
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #613cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #a33ca1; color: #ffffff;">7</td>  
    <td style="padding: 8px; background-color: #a33c65; color: #ffffff;">3</td>  
    <td style="padding: 8px; background-color: #7f3cab; color: #ffffff;">10</td>                  
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">15</td>  
    <td style="padding: 8px; background-color: #8e3cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #9e3cab; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33c92; color: #ffffff;">6</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #433cab; color: #ffffff;">14</td>  
    <td style="padding: 8px; background-color: #a33c74; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #703cab; color: #ffffff;">11</td>
  </tr>     
  </table>


The data in this `ndarray` can be sorted. The `ndarray` has a number of sorting methods:

```python
In [3]: np.array.
# 🔗 Sorting, Searching, and Counting
#     - argmin                     : Returns the indices of the minimum values along an axis.
#     - argmax                     : Returns the indices of the maximum values along an axis.
#     - nonzero                    : Returns the indices of the non-zero elements.
#     - sort                       : Sorts the ndarray in place along the specified axis.
#     - argsort                    : Returns the indices that would sort the ndarray.
#     - searchsorted               : Finds indices where elements should be inserted to maintain order.
```

Which are complemented by sorting functions:

```python
In [3]: np.
# 🔢 Sorting Functions:
#     - argmin                     : Returns the indices of the minimum values along an axis.
#     - argmax                     : Returns the indices of the maximum values along an axis.
#     - nonzero                    : Returns the indices of the non-zero elements.
#     - sort                       : Returns a sorted copy of an array.
#     - argsort                    : Returns the indices that would sort an array.
#     - searchsorted               : Finds indices where elements should be inserted to maintain order.
#     - count_nonzero              : Counts the number of non-zero elements in an array.
```

The `sort` function returns a new `ndarray`:

```python
In [3]: np.sort(mat, axis=None)
Out[3]: array([ 1,  3,  4,  6,  7,  8,  9, 10, 11, 12, 14, 15])

In [4]: np.sort(mat, axis=-1) # along column axis
Out[4]:
array([[ 3,  7, 10, 12],
       [ 6,  8,  9, 15],
       [ 1,  4, 11, 14]])

In [5]: np.sort(mat, axis=-2) # along row axis
Out[5]:
array([[ 1,  7,  3,  6],
       [12,  9,  4, 10],
       [15, 14,  8, 11]])     
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[12  7  3 10]<br>&nbsp;[15  9  8  6]<br>&nbsp;[ 1 14  4 11]]</td>
  </tr>                              
</table>

Whereas, the method is mutable, following the design pattern of a `MutableSequence` and modifies the `ndarray` in place:

```python
In [6]: mat.sort(axis=-1) # along column axis
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[3  7  10 12]<br>&nbsp;[6  8  9  15]<br>&nbsp;[ 1 14  11 14]]</td>
  </tr>                              
</table>

Reassigning `mat` to the original values:

```python
In [3]: mat = np.array([[12, 7, 3, 10],
      :                 [15, 9, 8, 6],
      :                 [1, 14, 4, 11]])
```

<table style="width: 65%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="4" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">Variable Explorer</th>
  </tr>     
  <tr>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">mat</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">Array of int64</td>
    <td style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">(2, 4)</td>
    <td style="padding: 8px; background-color: #705693; color: #ffffff;">[[12  7  3 10]<br>&nbsp;[15  9  8  6]<br>&nbsp;[ 1 14  4 11]]</td>
  </tr>                              
</table>

<table style="width: 60%; border-collapse: collapse; font-family: sans-serif;">
  <tr>
    <th colspan="5" style="text-align:center; padding: 8px; background-color: #2d2d30; color: #ffffff;">mat - numpy object array</th>
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;"></th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">0</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">1</th>          
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">2</th>
    <th style="padding: 8px; background-color: #252526; color: #ffffff;">3</th>                 
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">0</th>
    <td style="padding: 8px; background-color: #613cab; color: #ffffff;">12</td>  
    <td style="padding: 8px; background-color: #a33ca1; color: #ffffff;">7</td>  
    <td style="padding: 8px; background-color: #a33c65; color: #ffffff;">3</td>  
    <td style="padding: 8px; background-color: #7f3cab; color: #ffffff;">10</td>                  
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">1</th>
    <td style="padding: 8px; background-color: #3840ab; color: #ffffff;">15</td>  
    <td style="padding: 8px; background-color: #8e3cab; color: #ffffff;">9</td>  
    <td style="padding: 8px; background-color: #9e3cab; color: #ffffff;">8</td>  
    <td style="padding: 8px; background-color: #a33c92; color: #ffffff;">6</td>         
  </tr>
  <tr>
    <th style="padding: 8px; background-color: #1e1e1e; color: #ffffff;">2</th>
    <td style="padding: 8px; background-color: #a33c46; color: #ffffff;">1</td>  
    <td style="padding: 8px; background-color: #433cab; color: #ffffff;">14</td>  
    <td style="padding: 8px; background-color: #a33c74; color: #ffffff;">4</td>  
    <td style="padding: 8px; background-color: #703cab; color: #ffffff;">11</td>
  </tr>     
  </table>


The argument minimum method `argmin` gives the index of the minimum element:

```python
In [4]: mat.argmin(axis=-1) # along column axis
Out[4]: array([2, 3, 0])
```

For row `0`, the minimum value is `3` at index `2`. For row `1`, the minimum value is `6` at index `3`. For row `2`, the minimum value is `1` at index `0`. 

Notice that:

```python
In [5]: mat[(0, 1, 2), mat.argmin(axis=-1)]
Out[5]: array([3, 6, 1])

In [6]: mat.min(axis=-1)
Out[6]: array([3, 6, 1])
```

The argument minimum method `argmin` gives the index of the minimum element:

```python
In [7]: mat.argmax(axis=-1)
Out[7]: array([0, 0, 1])
```

For row `0`, the maximum value is `12` at index `0`. For row `1`, the maximum value is `15` at index `0`. For row `2`, the maximum value is `14` at index `1`. 

Notice also that the following are consistent:

```python
In [8]: mat[(0, 1, 2), mat.argmax(axis=-1)]
Out[8]: array([12, 15, 14])

In [9]: mat.max(axis=-1)
Out[9]: array([12, 15, 14])
```

`argmin` and `argmax` have the optional parameter `keepdims` which make it easier to visualise. Operating along `axis=-1` (the column axis) returns a column of indexes:

```python
In [10]: mat.argmin(axis=-1, keepdims=True)
Out[10]: 
array([[2],
       [3],
       [0]])

In [11]: mat.argmax(axis=-1, keepdims=True)
Out[11]: 
array([[0],
       [0],
       [1]])    
```

The argument sort method `argsort` will return an array of indexes:

```python
In [10]: mat.argsort(axis=-1) # along column axis
Out[10]: 
array([[2, 1, 3, 0],
       [3, 2, 1, 0],
       [0, 2, 3, 1]])
```

Notice that column `0` is `mat.argmin(axis=-1, keepdims=True)` as expected and column `-1` is `mat.argmax(axis=-1, keepdims=True)`/.

A corresponding `ndarray` of row co-ordinates can be constructed:

```python
In [11]: np.tile(np.ogrid[0: 3][:, np.newaxis], (1, 4))
Out[11]: 
array([[0, 0, 0, 0],
       [1, 1, 1, 1],
       [2, 2, 2, 2]])
```
Notice that the following are consistent:

```python
In [12]: mat[np.tile(np.ogrid[0: 3][:, np.newaxis], (1, 4)), 
       :     mat.argsort(axis=-1)]
Out[12]: 
array([[ 3,  7, 10, 12],
       [ 6,  8,  9, 15],
       [ 1,  4, 11, 14]])

In [13]: np.sort(mat, axis=-1)
Out[13]: 
array([[ 3,  7, 10, 12],
       [ 6,  8,  9, 15],
       [ 1,  4, 11, 14]])
```






```
update the section above to have these before sort
```

```
np.fliplr
np.flipud
np.filip
```





```
vec = np.array([3, 4, 4, 7, 9]) # sorted array

elements = [1, 2, 6, 6, 8, 10, 11, 13] # elements to be inserted into sorted array

indices = np.searchsorted(sorted_array, elements, side='right')

vec_extended = np.insert(vec, indices, elements)

vec_extended

vec
vec1 = np.insert(vec, 0, 1)
vec2 = np.insert(vec1, 0, 2)
vec3 = np.insert(vec2, 3, 3)

```





```



## other collection based behaviour

active1 = ['apples', 'cherries', 'bananas']
active2 = ['grapes', 'avocados', 'pears']

# vector expansion

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

row = np.array([10, 20, 30])[np.newaxis, :]

col = np.array([10, 40])[:, np.newaxis]

row_x2_num = row * 2 # scalar broadcast

row_x2_collection = np.tile(row, 2)
row_x2_collection = np.tile(row, 4)
row_x_2_4_collection = np.tile(row, (4, 2))

# view
# mat
# view row

mat + row # row broadcast
mat + np.tile(row, (2, 1))
mat + np.array([10, 20, 30]) # also works
# but generally better to be explicit



# under the hood the broadcasting use np.broadcast
b = np.broadcast(row, mat)
out = np.zeros(shape=b.shape)
out.flat = [u + v for (u, v) in b]
#             ↑ operator being broadcast

row_broadcast_to_mat = np.broadcast_to(row, shape=mat.shape)

scalar_3_broadcast_to_mat = np.broadcast_to(3, shape=mat.shape)
scalar_3_broadcast_to_mat2 = np.full_like(mat, fill_value=3) # better to use full_like

mat + col # col broadcast
mat + np.tile(col, (1, 3))

mat + np.array([10, 40]) # doesn't work

page0 = np.array([[1, 2],
                  [3, 4]])

page1 = np.array([[5, 6],
                  [7, 8]])

page2 = np.array([[9, 10],
                  [11, 12]])



vec = np.array([3, 4, 4, 7, 9]) # sorted array

elements = [1, 2, 6, 6, 8, 10, 11, 13] # elements to be inserted into sorted array

indices = np.searchsorted(sorted_array, elements, side='right')

vec_extended = np.insert(vec, indices, elements)

vec_extended

vec
vec1 = np.insert(vec, 0, 1)
vec2 = np.insert(vec1, 0, 2)
vec3 = np.insert(vec2, 3, 3)

mat

mat_lr = mat[:, ::-1]

mat_lr2 = np.fliplr(mat)

mat_ud = mat[::-1, :]

mat_ud2 = np.flipud(mat)

mat_lr3 = np.flip(mat, axis=-1) # operating along columns axis

mat

mat_padded = np.pad(mat, pad_width=((1, 2), (3, 4)), mode='constant',
                    constant_values=0)

mat_padded2 = np.pad(mat, pad_width=(0, 2), (0, 0))

# broadcast numeric operators

exit

mat1 = np.arange(16).reshape(4, 4)
mat2 = np.arange(-15, 15+2, 2).reshape(4, 4)

 '__abs__', # Returns the absolute value of the object.
 '__pos__', # Unary plus (+) for the object.
 '__neg__', # Unary minus (-) for the object.

 '__add__', # Addition operation (+).
 '__sub__', # Subtraction operation (-).
 '__mul__', # Multiplication operation (*).
 '__pow__', # Power operation (**).
 '__floordiv__', # Floor division (//).
 '__mod__', # Modulus operation (%).
 '__divmod__', # Division and modulus together (divmod()).
 '__truediv__', # True division (/).

 'real', # Returns the real part of a complex number.
 'imag', # Returns the imaginary part of a complex number.
 'conjugate', # Returns the complex conjugate of a number.

# unitary operators
u__abs__mat2 = abs(mat2)
u__pos__mat2 = +mat2
u__neg__mat2 = -mat2

# binary operators

mat1__add__mat2 = mat1 + mat2
mat1__sub__mat2 = mat1 - mat2
mat1__mul__mat2 = mat1 * mat2
mat2__pow__mat1 = mat2 ** mat1

mat2__pow__2 = mat2 ** 2

mat1__floordiv__mat2 = mat1 // 2
mat1__div__2 = mat1 % 2
mat1__divmod__2 = divmod(mat1, 2)

mat1__truediv__2 = mat1 / 2

mat3 = mat2 ** 0.5 # error

mat4 = mat2.astype(np.complex128) ** 0.5

mat4_real = mat4.real
mat4_imag = mat4.imag
mat4_conjugate = mat3.conjugate()

# rounding

mat = np.array([[1.12, -2.12, 3.12, -4.12],
                [-5.12, 6.12, -7.12, 8.12],
                [9.12, -10.12, 11.12, -12.12]])

mat_round_to_int = mat.round() # datatype is float64
mat_round_to_1dp = mat.round(decimals=1)

# datatypes

nums = np.array([[1, 2], [3, 4]], dtype=np.uint8)
2 ** 8

nums + 200

nums + 255

nums - 20

nums = np.array([[1, 2], [3, 4]], dtype=np.int8)
-(2 ** 8 / 2)
(2 ** 8 / 2) - 1 # because 0

nums + 100

nums - 100

nums + 200

# boolean section

x = np.array([0, 0, 0, 1, 0, 0, 2, 0, 0, 1])

n_nonzero_elements_x = np.count_nonzero(x)

indexes_nonzero_elements_x = np.nonzero(x)

x[indexes_nonzero_elements_x]

x == 0

x != 0

# array([False, False, False,  True, False, False,  True, False, False,
#        True])

x[x != 0]
# array([1, 2, 1])

x[x > 1]

y = np.array([1, 2, 3, 4])
boolean_mask = np.array([True, True, False, False])


boolean_mask.shape == y.shape

y_where_booleans_mask_true = y[boolean_mask]

text_vec = np.where(y==0, 'zero', 'non-zero')
# condition, what to do if True, what to do if False

z = np.array([(0+1j), 2, (2+2j), (1-3j), 5, 6])

result = np.isreal(z)

result = np.iscomplex(z)

mat1 = np.arange(0, 20, 1).reshape(5, 4)
mat2 = -mat1

selection_mask = np.zeros(shape=(5, 4))
selection_mask[1:3, :]
selection_mask[1:3, :] = np.ones(shape=(2, 4))
selection_mask = selection_mask.astype(np.int64)

mat3_choice = np.choose(selection_mask, [mat1, mat2])

# set operations

active = [1, 1, 1, 2, 2, 3, 4, 4, 5, 8]
unique = set(active)

x = np.array([1, 1, 1, 2, 2, 3, 4, 4, 5, 8])
unique = np.unique(x)

np.in1d(np.array([1, 2, 3, 6]), np.array([1, 2, 4, 5, 9]))

{1, 2, 3, 6} | {1, 2, 4, 5, 9}
np.union1d(np.array([1, 2, 3, 6]), np.array([1, 2, 4, 5, 9]))

{1, 2, 3, 6} & {1, 2, 4, 5, 9}
np.intersect1d(np.array([1, 2, 3, 6]), np.array([1, 2, 4, 5, 9]))

{1, 2, 3, 6} - {1, 2, 4, 5, 9}
np.setdiff1d(np.array([1, 2, 3, 6]), np.array([1, 2, 4, 5, 9]))

{1, 2, 3, 6} ^ {1, 2, 4, 5, 9}
np.setxor1d(np.array([1, 2, 3, 6]), np.array([1, 2, 4, 5, 9]))

# statistics

w = np.array([0.4, 1.2, 1.3, 2.3, 2.3, 2.4, 3.5, 3.4, 4.1, 4.2,
              4.7, 5.1, 5.1, 5.5, 5.7, 5.7, 5.8, 5.9, 5.9, 5.9,
              6.1, 6.1, 6.1, 6.7, 6.2, 7.3, 7.4, 7.4, 7.4, 7.4,
              8.8, 8.8, 8.8, 8.8, 8.8, 9.2, 9.2, 9.2, 9.2, 9.9])

w_min_val = w.min()
w_min_idx = w.argmin()
w[min_idx]

w_max_val = w.max()
w_max_idx = w.argmax()
w[max_idx]

w_cumulative_sum = w.cumsum()
w_sum = w.sum()

w_mean = w.mean()
w.sum() / w.size

w_variance = w.var(ddof=1) # n-1

w_standard_deviation = w.std(ddof=1) # n-1
w.var(ddof-1) ** 0.5

w_peaktopeak = w.ptp()

w_cumulative_product = w.cumprod()
w_product = w.prod()

w_clipped_between_3_and_9 = w.clip(3, 8)

# statistics
active = [1, 2, 3, 4]
max(active) # builtins
min(active) # builtins
sum(active) # builtins

range(5) # builtins

x = np.array([0, 0, 0, 1, 0, 0, 2, 0, 0, 1])
x_any = x.any()
x_all = x.all()

exit

w = np.array([0.4, 1.2, 1.3, 2.3, 2.3, 2.4, 3.5, 3.4, 4.1, 4.2,
              4.7, 5.1, 5.1, 5.5, 5.7, 5.7, 5.8, 5.9, 5.9, 5.9,
              6.1, 6.1, 6.1, 6.7, 6.2, 7.3, 7.4, 7.4, 7.4, 7.4,
              8.8, 8.8, 8.8, 8.8, 8.8, 9.2, 9.2, 9.2, 9.2, 9.9])

# historically
# from numpy import *
# builtins max, min, range, sum, any, all builtins would be reassigned to np functions
# a prefix (meaning array) amax, amin and arange were used instead
# import * discouraged
# max and min added for consistency with array methods

min_val_w = np.min(w)
min_idx_w = np.argmin(w)
max_val_w = np.max(w)
max_idx_w = np.argmax(w)
cumsum_w = np.cumsum(w)
sum_w = np.sum(w)
mean_w = np.mean(w)
var_w = np.var(w, ddof=1) # n-1
std_w = np.std(w, ddof=1) # n-1
ptp_w = np.ptp(w)
cumprod_w = np.cumprod(w)
prod_w = np.prod(w)
clip_w = np.clip(w, 3, 8)

x = np.array([1, 2, 3, 4])
boolean_mask = np.array([True, True, False, False])

any_x = np.any(x)
all_x = np.all(x)

# all of these statistical functions take in an axis

mat = np.array([[9, 3, 5, 6],
                [12, 4, 2, 3],
                [1, 6, 9, 8]])

max_mat = mat.max(axis=None)
argmax_mat = mat.argmax(axis=None)

mat.ravel()
mat.ravel()[10]

max_col = mat.max(axis=-1, keepdims=True) # operate along column axis
argmax_col = mat.argmax(axis=-1, keepdims=True)

max_col_indexes = mat.argmax(axis=-1)
mat[np.arange(0, 3), max_col_indexes]

max_row = mat.max(axis=-2, keepdims=True) # operate along row axis
argmax_row = mat.argmax(axis=-2, keepdims=True)

# additional statistics available as functions only

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

covar = np.sum((x - x.mean()) * (y - y.mean())) / (len(x) - 1)

x_var = x.var(ddof=1)
y_var = y.var(ddof=1)

np.cov(x, y)

differences_col = np.diff(mat, axis=-1)
difference_col_of_differences = np.diff(differences_col, axis=-1)
difference_col_of_differences2 = np.diff(mat, axis=-1, n=2)

y = np.array([1, 2, 2, 3, 1, 0, 1])
unique_y = np.unique(z)
bincount_y = np.bincount(z)

from collections import Counter
counts = Counter(y)

z = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4])

median_z = np.median(w)

mean_z = np.mean(z)
average_z = np.average(z)

weights_z = np.array([1, 1, 1, 1000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
average_weighted_z = np.average(w, weights=w_weights)

boundaries_20_percent = np.quantile(x, [0, 0.2, 0.4, 0.6, 0.8, 1]) # 0-1
boundaries_25_percent = np.quantile(x, [0, 0.25, 0.5, 0.75, 1]) # 0-1
boundaries_20_percent2 = np.percentile(x, [0, 20, 40, 60, 80, 100]) # 0-100

x = np.array([0.4, 1.2, 1.3, 2.3, 2.3, 2.4, 3.5, 3.4, 4.1, 4.2,
              4.7, 5.1, 5.1, 5.5, 5.7, 5.7, 5.8, 5.9, 5.9, 5.9,
              6.1, 6.1, 6.1, 6.7, 6.2, 7.3, 7.4, 7.4, 7.4, 7.4,
              8.8, 8.8, 8.8, 8.8, 8.8, 9.2, 9.2, 9.2, 9.2, 9.9])

counts, bins = np.histogram(x) # histogram

# look at histogram of x in variable explorer, roughly equivalent, bins differ

x = np.array([0.4, 1.2, 1.3, 2.3, 2.3, 2.4, 3.5, 3.4, 4.1, 4.2,
              4.7, 5.1, 5.1, 5.5, 5.7, 5.7, 5.8, 5.9, 5.9, 5.9,
              6.1, 6.1, 6.1, 6.7, 6.2, 7.3, 7.4, 7.4, 7.4, 7.4,
              8.8, 8.8, 8.8, 8.8, 8.8, 9.2, 9.2, 9.2, 9.2, 9.9])


x2 = 2 * x - 1
correlation = np.correlate(x, x2, mode='full')

x2[10] = 20.1
corrcoef_x_x2 = np.corrcoef(x, x2)

x2[10] = 2000
corrcoef_x_x2 = np.corrcoef(x, x2)

x2 = -2 * x - 1
corrcoef_x_x2 = np.corrcoef(x, x2)

## correlate
x = np.array([1, 2, 3])
y = np.array([0, 1, 0.5])

y = np.array([0, 1, 0.5])
# lag -2
y_m2 = np.array([0, 0, 0])
np.dot(x, y_m2)
# lag -1
y_m1 = np.array([0, 0, 1])
np.dot(x, y_m1)
# lag 0
y = np.array([0, 1, 0.5])
np.dot(x, y)
# lag +1
y_p1 = np.array([1, 0.5, 0])
np.dot(x, y_p1)
# lag +2
y_p2 = np.array([0.5, 0, 0])
np.dot(x, y_p2)

correlation = np.correlate(x, y, mode='full')

## math

# circle constant / 2
np.pi

# infinite
np.inf

# not a number
np.nan

# eulers number

def factorial(n):
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    result = 1
    for idx in range(2, n + 1):
        result *= idx
    return result

def series_expansion(terms=1000):
    return sum(1 / factorial(n) for n in range(terms))

series_expansion(1)  
series_expansion(10)
series_expansion(100)      
series_expansion(1000)

np.e

# euler gamma number

def series_expansion2(n=1000):
    return np.sum(1.0 / np.arange(1, n + 1)) - np.log(n)


series_expansion2(1)  
series_expansion2(10)
series_expansion2(100)      
series_expansion2(1000)  

np.euler_gamma
   

inf_mat = np.full(shape=(4, 2), fill_value=np.inf)

# a Python function
def croot(num):
    return num ** (1 / 3)

# Can be mapped to a list:
map(croot, [1, 3, 27])

# The result can be cast into a list to sreturn all the values:
list(map(croot, [1, 3, 27]))

# vectorize is similar but vectorizes to an ndarray

np_croot = np.vectorize(croot)
np_croot(np.array([1, 3, 27]))

# Most math expressions are already vectorised...

import math

math.sqrt(4)
np.sqrt(4)

vec = np.array([1, 4, 9, 16, 25])
np.sqrt(vec)

mat = np.array([[1, 4, 9],
                [15, 25, 36]])

# natural
np.exp(1)
np.e

x = np.linspace(0, 10, 100)

y1 = np.exp(x) # natural base
# use variable explorer to plot both and view

y2 = np.log(np.exp(x)) # natural base # cancel out

# base 10
x = np.array([10**0, 10**1, 10**2, 10**3, 10**4, 10**5])

y = np.log10(x) # retrieves the powers
y

np.pi
2 * np.pi

x1 = np.linspace(0, 360, 100)
x2 = np.deg2rad(x1)
# x1 * (2 * np.pi) / 360
x3 = np.rad2deg(x2)
# x3 * 360 / (2 * np.pi)

y1 = np.sin(x2)
# plot y1 from variable explorer

y2 = np.cos(x2)
# plot y2 from variable explorer

y3 = np.tan(x2)
# plot y3 from variable explorer

x4 = np.linspace(0, np.pi/4, 100)

y4 = np.arcsin(x4)

y5 = np.arccos(x4)

y6 = np.arctan(x4)

# random number generation

import numpy as np

[## Random Number Generators & Utility Functions:
 ## These functions deal with generating or setting seeds for random number generation.
 'seed', # Sets the seed for the random number generator to ensure reproducibility.
 'get_state', # Returns the current state of the random number generator.
 'set_state', # Sets the state of the random number generator.
 'random_state', # Returns a new random state generator.
 'PCG64', # Instantiates a PCG64 pseudo-random number generator.

 ## Random Sampling and Permutation Functions:
 ## These functions generate random selections or reorder elements of arrays.
 'permutation', # Returns a randomly permuted sequence or array.
 'shuffle', # Shuffles the sequence x in place.
 'choice', # Randomly selects elements from an array with or without replacement.

 ## Continuous Distributions:
 ## These functions generate random floating-point numbers based on various continuous
 ## distributions.
 'randint', # Generates random integers between low (inclusive) and high (exclusive).
 'uniform', # Samples from a uniform distribution in the range [low, high).
 'random_sample', # Generates random floats in the range [0, 1).
 'triangular', # Samples from a triangular distribution.
 'standard_normal', # Samples from a standard normal distribution (mean = 0, variance = 1).
 'normal', # Samples from a normal (Gaussian) distribution.
 'exponential', #  Samples from an exponential distribution.
 'standard_exponential', # Samples from a standard exponential distribution.
 'rayleigh', # Samples from a Rayleigh distribution.
 'gamma', # Samples from a gamma distribution.
 'standard_gamma', # Samples from a standard gamma distribution.
 'lognormal', # Samples from a log-normal distribution.
 'beta', # Samples from a beta distribution.
 'laplace', # Samples from a Laplace distribution (double-exponential distribution).
 'weibull', # Samples from a Weibull distribution.
 'chisquare', # Samples from a chi-square distribution.
 'f', # Samples from an F-distribution.
 'pareto', # Samples from a Pareto distribution.
 'logistic', # Samples from a logistic distribution.
 'gumbel', # Samples from a Gumbel distribution, typically used for modeling extreme values.
 'power', # Samples from a power-law distribution.
 'wald', # Samples from a Wald (inverse Gaussian) distribution.
 'vonmises', # Samples from a von Mises distribution, a circular distribution.
 'standard_cauchy', # Samples from a standard Cauchy distribution.

 ## Discrete Distributions:
 ## These distributions generate random integers based on various discrete probability
 ## distributions.
 'binomial', # Samples from a binomial distribution with n trials and success probability p.
 'geometric', # Samples from a geometric distribution, representing the number of trials
  # before the first success.
 'hypergeometric', # Samples from a hypergeometric distribution, modeling draws without
 # replacement.
 'negative_binomial', # Samples from a negative binomial distribution.
 'poisson', # Samples from a Poisson distribution.
 'multinomial', #  Samples from a multinomial distribution (generalization of the
 # binomial distribution).
 'zipf', # Samples from a Zipf distribution.

 ## Multivariate Distributions:
 ## These distributions generate random vectors based on multivariate probability
 ## distributions.
 'multivariate_normal', # Samples from a multivariate normal distribution.
 'dirichlet', # Samples from a Dirichlet distribution, often used in Bayesian statistics.
]

np.random.seed(66) # set random number generator to a state (for reproducability)
vec = np.arange(16)
permutation(vec)

np.random.shuffle(vec) # no return value
vec # mutatedin place

np.random.choice(vec)
np.random.choice(vec, size=(12,))
np.random.choice(vec, size=(12,), replace=False)

np.random.choice(vec, size=(4, 5))

# int
x1 = np.random.randint(low=0, high=11, size=(int(1e7),))

# dtype float...
x2 = np.random.uniform(low=0.0, high=11.0, size=(int(1e7),))

x3 = np.random.random_sample(size=(int(1e7),))
# x3 = np.random.uniform(low=0.0, high=1.0, size=(int(1e7),))

x4 = np.random.triangular(left=3, mode=4, right=5, size=(int(1e7),))

x5 = np.random.triangular(left=3, mode=3, right=5, size=(int(1e7),))

x6 = np.random.normal(loc=100, scale=30, size=(int(1e7),))

x7 = np.random.standard_normal(size=(int(1e7),))
# x7 = np.random.standard_normal(loc=0, scale=1, size=(int(1e7),))

x8 = np.random.exponential(scale=0.1, size=(int(1e7),))

x9 = np.random.exponential(scale=10, size=(int(1e7),))

x10 = np.random.standard_exponential(size=(int(1e7),))
# x10 = np.random.exponential(scale=1.0, size=(int(1e7),))

x11 = np.random.rayleigh(scale=1, size=(int(1e7),))

x12 = np.random.binomial(n=100, p=0.1, size=(int(1e7),))

x13 = np.random.binomial(n=100, p=0.2, size=(int(1e7),))

x14 = np.random.binomial(n=100, p=1, size=(int(1e7),))

x15 = np.random.poisson(lam=1, size=(int(1e7),))
# view histogram and plot, skewed to low values with low lam

x16 = np.random.poisson(lam=4, size=(int(1e7),))
# view histogram and plot, becomes more symmetric as lam increases

x17 = np.random.poisson(lam=10, size=(int(1e7),))
# view histogram and plot, large lam, approximates a normal distribution

x18 = np.random.gamma(shape=1, scale=5, size=(int(1e7),))
# view histogram and plot, similar to negative exponential with a scale of 1

x19 = np.random.gamma(shape=2, scale=5, size=(int(1e7),))
# view histogram and plot, moves towards a bellshape

x20 = np.random.gamma(shape=3, scale=5, size=(int(1e7),))
# view histogram and plot, tend continues to moves towards a bellshape

x21 = np.random.gamma(shape=100000, scale=5, size=(int(1e7),))
# view histogram and plot, the plot tends towards a bellshape with a mean of 500000
# which is the product of shape and scale

## np.datetime64, accurate to a ns

np.datetime64('2024-09-16T17:30:25.123456789')

# np.timedelta64, accuracy to

np.datetime64('2024-09-01') - np.datetime64('2024-08-01')

np.datetime64('2024-09-01') - np.datetime64('2024-08-01T01')

np.datetime64('2024-09-01') - np.datetime64('2024-08-01T01:15')

np.datetime64('2024-09-01') - np.datetime64('2024-08-01T01:15:30')

np.datetime64('2024-09-01') - np.datetime64('2024-08-01T01:15:30.001')

np.datetime64('2024-09-01') - np.datetime64('2024-08-01T01:15:30.001002')

np.datetime64('2024-09-01') - np.datetime64('2024-08-01T01:15:30.001002003')

# np.timedelta64

np.timedelta64(1,'D') + np.timedelta64(1,'h') + np.timedelta64(1,'m') + \
    np.timedelta64(1, 's') + np.timedelta64(1, 'ms') + \
        np.timedelta64(1, 'us') + np.timedelta64(1, 'ns')

# doesn't support dates as it focuuses on float division
np.linspace(np.datetime64('2024-09-01'),
            np.datetime64('2024-09-03'),
            3)

dates = np.arange(np.datetime64('2024-09-01'),
                  np.datetime64('2024-09-03') + np.timedelta64(1, 'D'),
                  np.timedelta64(1, 'D'))

# doesn't display in variable explroer
# look in ipython console

times = np.arange(np.timedelta64(1, 's'),
                  np.timedelta64(10, 's') + np.timedelta64(1, 's'),
                  np.timedelta64(1, 's'))

# doesn't display in variable explorer
# look in ipython console

# array operations and linear algebra

# exit

# normalised matrix

vec = np.array([3, 4])
np.linalg.norm(vec)

# ((3 ** 2) + (4 ** 2)) ** 0.5

mat = np.array([[1, 2],
                [3, 4]])
np.linalg.norm(mat)
# ((1 ** 2) + (2 ** 2) + (3 ** 2) + (4 ** 2)) ** 0.5

# exit
row = np.array([3, 4])[np.newaxis, :]
col = np.array([1, 2])[:, np.newaxis]
# open in the variable explorer

row.shape[-1] == col.shape[0]

mat = row @ col

(row.shape[0], col.shape[-1]) == mat.shape

np.inner(np.array([3, 4]),
         np.array([1, 2]))

col.shape[-1] == row.shape[0]

mat = col @ row

(col.shape[0], row.shape[1]) == mat.shape

np.outer(np.array([3, 4]),
         np.array([1, 2]))

# equations used to create this matrix are not unique
# (3x + 4y)
# (6x + 8y) = 2 * (3x + 4y)

# The determinnant of the matrix is the difference of the products of the diagonals
np.linalg.det(mat)

# Therefore this matrix has no inverse and
np.linalg.inv(mat)
# gives an error singularmatrix

matrix = np.array([[5, 6],
                   [3, 3]])


results = np.array([83, 42])[:, np.newaxis]


# matrix @ coeefficients = results
# (2, 2) @ (2, 1) = (2, 1)

inv_matrix = np.linalg.inv(matrix)

inv_matrix @ matrix
# creates the identity matrix

np.identity(2)
# the identity matrix can be made shorthand using

col = np.array([1, 2])[:, np.newaxis]
# take an example column

np.identity(2) @ col
# look at this operation by opening the variables in the variable explorer
# look at the effect of multiplying by 1

# matrix @ coeefficients = results
# (2, 2) * (2, 1) = (2, 1)

# inv_matrix @ matrix @ coefficients = inv_matrix @ results
# (2, 2) @ (2, 2) @ (2, 1) = (2, 2) @ (2, 1)

# identity @ coefficients = inv_matrix @ results
# (2, 2) @ (2, 1) = (2, 2) @ (2, 1)

# coefficients = inv_matrix @ results
# (2, 1) = (2, 2) @ (2, 1)

coefficients = inv_matrix @ results

coefficients = np.linalg.solve(matrix, results)

## eigenvalues and eigenvectors

mat = np.array([[4, -2],
                [1, 1]])

eigenvalues, eigenvectors = np.linalg.eig(mat)

v = eigenvectors[:, 0]
lamb = eigenvalues[0]

mat @ v

lamb * v

v = eigenvectors[:, 1]
lamb = eigenvalues[1]

mat @ v

lamb * v

## single vector decomposition

mat = np.array([[1, 2],
                [3, 4],
                [5, 6]])

u, s, v = np.linalg.svd(mat)


sigma = np.zeros((mat.shape))
sigma[:len(s), :len(s)] = np.diag(s)


mat_reconstructed = u @ sigma @ v

##  qr decomposition

mat = np.array([[1, 2],
                [3, 4],
                [5, 6]])

q, r = np.linalg.qr(mat)

mat_reconstructed = q @ r

# other statistical functions

## more specialised scientific functions scipy...
```