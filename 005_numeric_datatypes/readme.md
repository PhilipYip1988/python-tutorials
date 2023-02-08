# Numeric Data Types

There are six fundamental numeric datatypes used in Python. The ```int``` class (whole number), ```bool``` class (```True``` or ```False```), the ```float``` class (number with a decimal point) and the ```complex``` class (number with imaginary component $j=\sqrt{-1}$) are all in ```builtins```. The ```float``` class is displayed as decimal but under the hood is encoded in binary. This results in recurring rounding problems making floating point arithmetric slightly different from traditional arithmetric. The ```Decimal``` class is contained in the ```decimal``` standard module is higher precision and behaves like traditional numbers which use the decimal system. The ```Fraction``` class is contained in the ```fraction``` standard module.

## int class

An integer is a whole number. 

### Initialization Signature

The init signature of the ```int``` class can be viewed by inputting the class name with open parenthesis and pressing shift ```⇧``` and tab ```↹```:

![img_001](./images/img_001.png)

The init signature is normally used when cast an integer from a string such as:

```
int('65')
```

The default base is ```10```. For a binary or hexadecimal string this needs to be specified:

```
int('0b1000001', base=2)
int('0x41', base=16)
```

![img_002](./images/img_002.png)

Without quotation marks, these are all recognised as an integer:

```
65
0b1000001
0x41
```

![img_003](./images/img_003.png)

The default way to instantiate an integer is to use a decimal as it uses a base 10 by default. The number can be assigned to an object name:

```
num1 = 65
```

![img_004](./images/img_004.png)

Recall assigning to an object name can be conceptualised as adding a label to the integer object. This label can be used to reference the integer object. The Variable Inspector may be opened by right clicking blank space and selecting Open Variable Inspector:

![img_005](./images/img_005.png)

The datatype is ```int``` as expected:

![img_006](./images/img_006.png)

### Identifiers

Inputting ```num1.``` and pressing tab ```↹``` will display a list of identifiers:

![img_007](./images/img_007.png)

The integer ```65``` is designed for interoperability with the ```Fraction``` class and can be conceptualised as the fraction instance:

$$\left(\frac{65}{1}\right)$$

The ```numerator``` will match the value of the integer in this case ```65``` and the ```denominator``` will be ```0```. The associated method ```as_integer_ratio``` returns these two attributes and returns the fraction as a ```tuple```:

```
num1.numerator
num1.denominator
num1.as_integer_ratio()
```

![img_008](./images/img_008.png)

The integer ```65``` is designed for interoperability with the ```complex``` class and can be conceptualised as the complex number:

$$65+0j$$

where $j = \sqrt{-1}$.

The ```real``` attribute reads the real value will match the value of the integer in this case ```65``` and the ```imag``` will be ```0```. The associated method ```conjugate``` takes these two attributes and inverts the sign of the ```imag``` attribute, because this is ```0``` the complex conjugate matches the original integer:

```
num1.real
num1.imag
num1.complex()
```

![img_009](./images/img_009.png)

The remaining identifiers are for interoperability with the ```bytes``` class. Details about ```bytes``` and encoding were given in the previous tutorial. The binary representation of the integer which can be viewed using:

```
bin(num1)
```

The method ```bit_count``` returns the number of ones which in this case is ```2``` and the method ```bit_length``` returns the bit length (the number of digits past the ```0b``` prefix):

```
num1.bit_count()
num1.bit_length()
```

The ```to_bytes``` method can cast the integer to a ```bytes``` instance. By default a length of ```1``` byte is used with a byteorder that is ```big``` (big endian) and signed is ```False``` meaning the bytes are unsigned:

![img_010](./images/img_010.png)

This behaviour will therefore only work for a positive integer between ```0:256``` as these are the limits for a 8 bit signed integer. The defaults will behave similarly to the ```chr``` function which returns a Unicode value:

```
num1.to_bytes()
chr(num1)
```

![img_011](./images/img_011.png)

If a byte length of ```3``` bytes is selected:

```
num1.to_bytes(length=3)
```

![img_012](./images/img_012.png)

The escape sequence for ```\x00``` will display as this is a non-printable character. The letter ```'A'``` has an escape sequence of ```\x41``` but displays as ```'A'``` as it is readible. This can be seen by using the ```bytes``` method ```hex```:

```
num1.to_bytes(length=3).hex()
```

![img_013](./images/img_013.png)

A Unicode character can be examined that occupies two bytes:

```
num2 = 949
chr(num2)
letter2 = num2.to_bytes(length=2, byteorder='big')
letter2.decode(encoding='UTF-16-BE')
```

![img_015](./images/img_015.png)

The ```from_bytes``` class method is an alternative constructor which can be used to instantiate an integer from a ```bytes``` object. For example:

```
int.from_bytes(letter2)
```

![img_016](./images/img_016.png)


### Data Model Identifiers

If the directory function ```dir``` is used on an integer instance ```num1```, the last of identifiers displays alongside data model identifiers. 

![img_017](./images/img_017.png)

To view this list horizontally, pretty print will be used:

```
import pprint
pprint.pprint(dir(num1), compact=True)
```

![img_018](./images/img_018.png)

In the previous tutorial, the data model identifiers were discussed in detail for the ```str``` class. Some analogy can be seen between these two classes.

The inbuilt function ```dir``` uses the datamodel method ```__dir__``` and the list of identifiers as just seen. 

The ```__repr__``` and ```__str__``` data model identifiers give the formal representation of an ```int``` and the informal representation. These map to the ```repr``` and function ```str``` class respectively:

```
repr(num1)
str(num1)
```

![img_019](./images/img_019.png)

For the ```int``` class, the formal and informal representations are identical. Recall conventionally that ```print``` uses the informal ```str``` representation:

```
print(num1)
```

![img_020](./images/img_020.png)

And the cell output prints the formal representation:

```
print(repr(num1))
num1
```

![img_021](./images/img_021.png)

The ```__format___``` identifier is typically used when an integer variable is placed in a formatted string. This was examined in detail when the string class was examined however to recap:

```
f'The number is {num1 :d}'
f'The number is {num1 :03d}'
f'The number is {num1 :+04d}'
```

![img_022](./images/img_022.png)

The data model identifier ```__class__``` maps to the inbuilt class ```type``` which displays the class type of the object. 

```
type(num1)
```

![img_023](./images/img_023.png)

This displays ```int``` as expected.

The data model identifier ```__doc__``` is the document string for a string instance. It is more commonly used with the ```?``` which includes some other information from the data model identifiers ```__type__```, ```__str__```, and ```__doc__```:

```
? num1
```

![img_024](./images/img_024.png)

The ```__index__``` method means that an ```int``` can be used for indexing:

```
'hello'[0]
b'hello'[0]
```

![img_025](./images/img_025.png)

The ```__hash__``` method means that an ```int``` is hashable. A hashable value is permissible as a key in a dictionary or mapping. 

```
num_dict = {1: 'one', 2: 'two', 3: 'three'}
num_dict[1]
```

![img_026](./images/img_026.png)

Keys in the dictionary are normally strings but can be integers aswell. Note this dictionary has the numeric keys and these differ from the numeric index in other collections like a list. The numeric keys above for example lack the key ```0```.


```__getitem__``` is an collection data model identifier. It is used when:

```
num1[0]
```

![img_027](./images/img_027.png)

This is setup to raise a ```TypeError``` as an ```int``` is not subscriptable.

The data model ```__sizeof__``` displays the memory an object occupies in bytes:

```
import sys
sys.getsizeof(num1)
```

![img_028](./images/img_028.png)

The ```__getattribute__```, ```__setattr__``` and ```__delattr__``` methods are used to get, set and delete attributes. ```__getattribute__``` is used when:

```
num1.real
```

![img_029](./images/img_029.png)

```__setattr__``` is used when:

```
num1.real = 66
```

![img_030](./images/img_030.png)

Notice that this is not supported and the method is setup to invoke an ```AttributeError```.

```__delattr__``` is used when:

```
del num1.real
```

![img_031](./images/img_031.png)

This is not supported and the method is setup to invoke an ```AttributeError```.

The ```__init__``` data model method is called when instantiating an integer. 

![img_032](./images/img_032.png)

When the new Python object is created, the ```__new__``` data model method is called. This creates the new instance which is given the label or object name and then the initialization signature ```__init__``` is called to initialize the instance with the unique numeric data.

The data model identifiers ```__getstate__```, ```__reduce__```, ```__reduce_ex__``` and ```__getnewargs__``` are used by the pickle module to serialise the ```str```.

The last data model identifier is ```init_subclass``` and ```__subclasshook__``` which is used for Abstract Base Classes.

### Unitary Data Model Identifiers

The unitary data model identifiers allow use of a mathematical operator on a unitary instance:

```__pos__``` maps to the ```+``` operator:

```
num1
+ num1
```

![img_033](./images/img_033.png)

This doesn't change the sign of the integer.

```__neg__``` maps to the ```-``` operator:

```
num1
- num1
```

![img_034](./images/img_034.png)

This changes the sign of the integer.

```__abs__``` maps to the function ```abs```:

```
abs(num1)
abs(- num1)
```

![img_035](./images/img_035.png)

Notice that both of these are positive, the signs have been stripped.

```__ceil__```, ```__floor__``` and ```__trunc__``` map to ```math.ceil```, ```math.floor``` and ```math.trunc```. These methods are designed to cast a non-integer number into an integer. When the number is already an integer, the result is unchanged:

```
num1
import math
math.ceil(num1)
math.floor(num1)
math.trunc(num1)
```

![img_036](./images/img_036.png)

```__round__``` maps to ```round``` which by default rounds to an integer. When the number is already an integer, the result is unchanged:

```
round(num1)
```

![img_037](./images/img_037.png)

```__int__``` maps to the ```int``` init signature to cast the number to an ```int```. When the number is already an integer, the result is unchanged:

```
num1
int(num1)
```

![img_038](./images/img_038.png)

```__bool__``` maps to the ```bool``` init signature to cast the number to an ```bool```. Any ```int``` that is non-zero will map to a boolean value of ```True```, zero will map to ```False```:

```
num1
bool(num1)
num2 = 0
bool(num2)
num3 = -1
bool(num3)
```

![img_039](./images/img_039.png)

```__float__``` maps to the ```float``` init signature to cast the number to a ```float```. Notice the subtle difference in the output, a decimal point is now included:

```
num1
float(num1)
```

![img_040](./images/img_040.png)

### Binary Data Model Identifiers

Binary data model methods require two numeric instances.

```
num1 = 65
num2 = 4
```

![img_041](./images/img_041.png)

If the docstring of the ```__add__``` binary data model method is examined, the numeric instance the data model method is being called from is referred to as self and the other instance is referred to as value:

![img_042](./images/img_042.png)

```__add__``` maps to the addition operation ```+``` performing numeric addition:

```
num1 = 65
num2 = 4
num1 + num2
```

![img_043](./images/img_043.png)

```__radd__``` the reverse add data model method when called from ```num1``` carries out the operation:

```
num2 + num1
```

![img_044](./images/img_044.png)

The operation above is commutative and both instances are of the same int class so the result is the same. When the operator is used between different class types, there can be subtle differences. 

The ```__add__``` method also controls the behaviour of the inplace addition ```+=``` operator:

```
num1 = 65
num2 = 4
num1 += num2
```

![img_045](./images/img_045.png)

This is shorthand for:

```
num1 = 65
num2 = 4
num1 = num1 + num2
```

![img_046](./images/img_046.png)

Recall the calculation on the right is carried out first using the original value of ```num1```. The object name or ```num1``` is then assigned to this new result.

```__mul__``` maps to the ```*``` operator:

```
num1 = 65
num2 = 4
num1 * num2
```

![img_047](./images/img_047.png)

The ```*``` operator in the ```int``` class performs numeric multiplication as seen above. In the ```str``` class the ```*``` operator is defined to allow string replication with an ```int```.

```
str1 = 'hello'
```

![img_048](./images/img_048.png)

If the following is used, the ```__mul__``` method from the ```str``` class is used ```'hello'``` is the string instance self and ```num1``` is the int instance value. String replication occurs:

```
num1 = 3
str1 = 'hello'
str1 * num1
```

![img_049](./images/img_049.png)

When the following is carried out, the ```__mul__``` method from the ```int``` class is used ```num1``` is the int instance self and ```'hello'``` is the string instance value. As ```__mul__``` is setup in an integer for multiplication, the first operation fails:

![img_050](./images/img_050.png)

```
num1 = 3
str1 = 'hello'
num1 * str1
```

![img_051](./images/img_051.png)

Behind the scenes the reverse multiplication ```__rmul__``` is attempted. The ```__rmul__``` sees that ```'hello'``` is a string and then calls the ```__mul__``` method of the string class, effectivelty computing:

```
'hello' * num1
```

```__mul__``` also maps to the assignment multiplication operator ```*=```.

```__sub__``` maps to the subtraction operator ```-``` which carries out numeric subtraction:

```
num1 = 65
num2 = 4
num1 - num2
```

![img_052](./images/img_052.png)

```__sub__``` also maps to the assignment multiplication operator ```-=```. There is also the associated reverse subtraction ```__rsub__```.

```__pow__``` maps to the power operator ```**``` which raises self to the power of the value:

```
num1 = 65
num2 = 4
num1 ** num2
```

![img_053](./images/img_053.png)

Recall this is equivalent to:

```
65 * 65 * 65 * 65
```

![img_054](./images/img_054.png)

```__pow__``` also maps to the assignment power operator ```**=```. There is also the associated reverse subtraction ```__rpow__```.

```__floordiv__``` maps the floor division ```//``` operator which performs floor division also known as integer division. The associated ```__modulo__``` maps the modulo operator ```%``` which calculates the modulo. ```__divmod__``` maps to the function ```divmod``` which returns the floor division and modulo as components of a tuple. These are usually used with positive itneger values:

```
num1 = 65
num2 = 4
num1 // num2
num1 % num2
divmod(num1, num2)
```

![img_055](./images/img_055.png)

```__floordiv__``` and ```__mod__``` also maps to the assignment floor division operator ```//=``` and the assignment mudulo operator ```%=``` respectively. There is also the associated reverse versions ```__rfloordiv__```, ```__rmodulo__``` and ```__rdivmod__```.

```__truediv__``` maps to float division ```/``` operator which performs float division. The result will always be a float. Notice the inclusion of the decimal point:

```
num1 = 65
num2 = 4
num1 / num2
num1 / 1
```

![img_056](./images/img_056.png)

```__truediv__``` also maps to the assignment floor division operator ```/=```. There is also the associated reverse float divide ```__rtruediv__```.

The six comparison data model identifiers equals ```__eq```, not equals ```__ne__```, less than or equal to ```__le__```, less than ```__lt__```, greater than or equal to ```__ge__``` and greater than ```__gt__``` control the behaviour behind the 6 comparison operators ```==```, ```!=```, ```<=```, ```<```, ```>=``` and ```>``` respectively.

```
num1 = 65
num2 = 4
num1 > num2
num1 > num1
num1 == num1
num1 >= num1
num1 != num1
```

![img_057](./images/img_057.png)

```__and__```, ```__or__``` and ```__xor__``` map to the and operator ```&```, or operator ```|```, xor operator ```^```. These are normally associated with ```boolean``` values recall any integer value that is non-zero is ```True``` and an integer equal to zero is ```False```.

```&``` is ```True``` only if both conditions are ```True```:

```
True & True
True & False
False & False
```

![img_058](./images/img_058.png)

```|``` is ```True``` if one or both conditions are ```True```:

```
True | True
True | False
False | False
```

![img_059](./images/img_059.png)

```^``` is ```True``` if both conditions are different:

```
True ^ True
True ^ False
False ^ False
```

![img_060](./images/img_060.png)

```__and__```, ```__or__``` and ```__xor__``` also maps to the assignment and operator ```=&```, assignment or operator ```=|``` and assignment xor operator ```^=```. There is also the associated reverse versions ```__rand__```, ```__ror__```, ```__rxor__```.

```__lshift__``` maps to the binary left shift operator ```<<``` and ```__rshift__``` maps to the binary right shift operator ```>>```. These operate at the byte level. The ```bin``` function can be used to examine the change. 

Notice that trailing zeros of the specified number have been added to the end shifting the existing byte sequence to the left:

```
num1 = 65
bin(num1)
bin(num1 << 1)
num1 << 1
bin(num1)
bin(num1 << 2)
```

![img_061](./images/img_061.png)

Notice the specified number of digits on the right have been stripped:

```
num1 = 65
bin(num1)
bin(num1 >> 1)
num1 >> 1
bin(num1)
bin(num1 >> 2)
```

![img_062](./images/img_062.png)

```__lshift__``` and ```__rshift__``` also map to the assignment binary left shift operator ```<<=``` and assignment binary right shift operator ```>>=```. There is the associated reverse versions ```__rlshift__``` and ```__rrshift__```.

### PEDMAS

PEDMAS is an abbreviation for order of operator precedence:

|Letter|Meaning|Operator|
|---|---|---|
|P|Parenthesis|( )|
|E|Exponentiation|\*\*|
|D|Division (Floor, Float or Modulus)|\\ or \\\\ or %|
|M|Multiplication|\*|
|A|Addition or Positive|+|
|S|Subtraction or Negative|-|

D and M are of equal precedence.

A and S are of equal precedence.

Compare the expression:

```
-3 ** 2
```

With:

```
(-3) ** 2
```

![img_163](./images/img_163.png)

The first expression has E and S. E occurs before S so the 3 is brought to the power of 2 and then the negative operator is applied.

The second expression has P, E and S. P occurs first and within the parenthesis, the operation S is carried out. Once the operation in parenthesis is carried out, the final operation E is carried out.

## bool class

A boolean is a ```True``` or ```False``` value.

When the method resolution order for the ```int``` class is examined:

```
int.mro()
```

![img_063](./images/img_063.png)

The output list displays ```int``` and then ```object```. This means the ```int``` (like everything else in Python is an object). The method resolution order means Python will first look for a method defined in the ```int``` class (blueprint) and then if it can't find the method there, take a second look in the ```object``` class (blueprint).

When the method resolution order for the ```bool``` class is examined:

```
bool.mro()
```

![img_064](./images/img_064.png)

The output list displays ```bool```, ```int``` and then ```object```. The method resolution order means Python will first look for a method defined in the ```bool``` class (blueprint), then secondly look for a method in the ```int``` class (blueprint) and finally if it can't find the method there, take a third look in the ```object``` class (blueprint). The only major modification to the ```bool``` class is a restriction to only two possible values ```False``` and ```True```. Otherwise it behaves identically to the ```int``` class as most its methods are taken directly from the ```int``` class unmodified (i.e. accessed directly from the ```int``` blueprint).

### Initialization Signature

The init signature of the ```bool``` class can be viewed by inputting the class name with open parenthesis and pressing shift ```⇧``` and tab ```↹```:

![img_065](./images/img_065.png)

The init signature states that the builtins ```False``` and ```True``` are the only two instances of the class ```bool``` and clarifies that the class ```bool``` is a subclass of the class ```int```, and cannot be subclassed.

Recall casting an integer to a bool gives ```True``` for any non-zero integer and ```False``` for zero:

```
bool(0)
bool(1)
bool(-4)
```

![img_066](./images/img_066.png)

Typically the inbuilts ```False``` and ```True``` are sued directly but they can be assigned to object names:

```
False
True
```

![img_067](./images/img_067.png)

### Identifiers

A list of identifiers can be found by inputting one of these object names followed by a dot ```.``` and tab ```↹```:

![img_068](./images/img_068.png)

These methods are the same as their counterparts in the ```int``` class because this is a subclass and the methods are taken directly from the ```int``` classes blueprint.

### Data Model Identifiers

All the identifiers, including the data model identifiers can be viewed using:

```
pprint.pprint(dir(False), compact=True)
```

![img_069](./images/img_069.png)

Most of these behave identically to the ```int``` class as they are taken directly from this blueprint. The two string related data model identifiers ```__repr__``` and ```__str__``` have been updated to display strigns of the two builtin identifiers ```'False'``` and ```'True'``` opposed to ```'0'``` and ```'1'```.

```
repr(False)
str(False)
```

![img_070](./images/img_070.png)

Notice the difference in syntax highlighting from the builtin bool instance ```False``` and the string ```'False'```. The inbuilt instance is case sensitive and if ```false``` is referenced, Python will look for an object ```false``` which won't have been created resulting in a ```NameError```.

If the comparison operator is equal ```==``` is used:

```
False == 0
True == 1
True == 2
```

![img_071](./images/img_071.png)

Numerically it can be seen that ```False``` is the same as ```0``` and ```True``` is the same as ```1```. 

When boolean values are used with most of the mathematical operators, they take on these numeric values. This can be seen by use of the basic positive and negative unitary operators. Recall for a unitary ```+``` and unitary ```-```, the ```__pos__``` and ```__neg__``` data model identifiers are invoked and a change can be seen in the result when ```+``` is used:

```
+ True
- True
```

![img_072](./images/img_072.png)

For most mathematical operations, it is more common to use the integers directly. However it is common to use boolean values with the and operator ```&```, or operator ```|```, xor operators ```^``` as these operators return a boolean value. This use case was explored when these methods were examined earlier.

## float class

A float is number that has an incomplete unit. This incomplete unit is normally expressed using a decimal point.

When the method resolution order for the ```float``` class is examined:

```
float.mro()
```

![img_073](./images/img_073.png)

This class inherits directly from ```object``` and is not a subclass of the ```int``` class.

### Initization Signature

The init signature of the ```float``` class can be viewed by inputting the class name with open parenthesis and pressing shift ```⇧``` and tab ```↹```:

![img_074](./images/img_074.png)

The initialization signature is only typically used when casting an existing number or a string of a number to a floating point number. For example:

```
float(10)
float('10')
```

![img_075](./images/img_075.png)

Notice the difference in the syntax highlighting for the input arguments which distinguish the numerical input argument from the text input argument. Notice the output in all cases includes the postfix ```.0```. The ```.``` in this case indicates a decimal point. This should not be confused with the other use of the ```.``` which is used to access identifiers from an object.

Every day items are not measured in quantised units and the decimal point means it is possible to include an incomplete quantity. For example a human may have a height of 1.5 metres:

```
1.5
```

![img_076](./images/img_076.png)

Floating point numbers are particularly common when the item size is extremely small or extremely large with respect to the unit of measurement. For example, the radius of a hydrogen atom is 0.000000000053 metres:

```
0.000000000053
```

![img_077](./images/img_077.png)

Because this number is so small, it becomes difficult to transcribe and the output uses scientific notation. 

The 0th position is the unit value which is to the left hand side of the decimal point:

```
5e0
```

![img_078](./images/img_078.png)

The 1st position is the tens, which is one to the left hand side of the unit value:

```
5e1
```

![img_079](./images/img_079.png)

The negative 1st position is the 10ths which is one to the right hand side of the unit. The decimal point itself is not counted as a numeric digit when using scientific notation:

```
5e-1
```

![img_080](./images/img_080.png)

In the example above the first non-zero digit for the radius of the hydrogen atom was 5 which was at the 11th digit to the right hand side to the decimal point. This is why the power was -11.

In scientific notation the mantissa is always expressed with the unit value occupied and the power uses is always an integer. 

Scientific notation is typically used for very small and very large numbers to prevent transcription errors from leading or trailing zeros respectively. The radius of the sun is expressed as 696340 km where k means to the power of 3. This means the radius of the sun in metre is:

```
696340e3
```

Or with a proper mantissa as:

```
6.96340e8
```

![img_081](./images/img_081.png)

Python will display scientific notation for numbers with an exponent less than ```-5``` and greater than ```16```. This behaviour can be seen using:

```
for i in range(-12, 25, 2):
    print(float(5**i))
```    

![img_082](./images/img_082.png)

### Identifiers

The ```.``` is used as a decimal point for numeric data and therefore it is not possible to access identifiers from a number unless the number has an object name and the ```.``` is placed after the object name.

For example if the instance is assigned to an object name ```num1```:

```
num1 = 0.5
```

Then pressing ```num1``` followed by a dot ```.``` and tab ```↹``` displays the identifiers:

![img_083](./images/img_083.png)

Although the ```float``` class is not a subclass of the ```int``` class, its identifiers are setup to be consistent with the ```int``` class.

The ```real```, ```imag``` and ```conjugate``` methods are present in the ```int``` class and the ```float``` class as both classes are setup to be compatible with complex numbers. The ```real``` component is once again going to be the same as the original value and the ```imag``` component is going to be zero. The ```conjugate``` which returns the ```real``` component and switches the sign of the zero ```imag``` component is going to be identical to the existing instance:

![img_084](./images/img_084.png)

The ```float``` class is also setup to be compatible with the ```Fractions``` class, it does not have the attributes ```numerator``` or ```denominator``` as the values of these have to be calculated, opposed to being merely read off like in the case of the integer class. It does however have the method ```as_integer_ratio``` which calculates these and displays them in a tuple:

```
num1 = 0.5
num1.as_integer_ratio()
```

![img_085](./images/img_085.png)

Sometimes the results may be unexpected...

```
num2 = 0.1
num2.as_integer_ratio()
```

![img_086](./images/img_086.png)

A ```float``` is displayed using the 10 decimal characters but under the hood is stored using a finite number of binary bits. The binary system only uses 2 characters and recurring rounding errors are quite prevalent.

Recurring rounding errors occur in decimal also. In decimal a recurring rounding error occurs with the concept of one third which is easy to represent as a fraction:

$$\left(\frac{1}{3}\right)$$

But cannot be represented cleanly as a decimal, essentially the same recurring operation occurs on and on and on ... forever.

$$0.3333333333\cdots$$

In real life the number will be written down using a finite number of characters:

$$0.3333333333$$

The concept of one third plus one third plus one third equalling unity is simple as a fraction:

$$\left(\frac{1}{3}\right) + \left(\frac{1}{3}\right) + \left(\frac{1}{3}\right)$$

However in decimal there will be a recurring rounding error for each third:

$$0.3333333333 + 0.3333333333 + 0.3333333333$$

As a result a very small proportion will be lost and the result will be just shy of unity:

$$0.9999999999$$

The ```hex``` method will convert a ```float``` instance to a hexadecimal string, more details can be seen by examining the docstring by inputting the method name with open parenthesis and pressing shift ```⇧``` and tab ```↹```:

![img_087](./images/img_087.png)

The format is best seen by an example:

```
num1 = 0.5
num1.hex()
```

![img_088](./images/img_088.png)

This gives ```'0x1.0000000000000p-1'```

The general form is:

```
'[sign] [0x] integer [. fraction] [p exponent]'
```

```[sign]``` the sign is not shown so it is implied to be positive.

```[0x]``` is a constant prefix denoting a hexadecimal number.

```integer [. fraction]``` are in hexadecimal. To convert to decimal powers of 16 need to be used.

The unit 1 and $1*16^{0}=1$

The first value past the decimal point is 0 and $0*16^{-1}=0$

The second value past the decimal point is 0 and $0*16^{-2}=0$

The third value past the decimal point is 0 and $0*16^{-3}=0$

The fourth value past the decimal point is 0 and $0*16^{-4}=0$

$\vdots$

Combining these together gives $1.00000$ in decimal.

```[p exponent]``` indicates ```2``` to the power of a decimal exponent. In this example ```p-1``` means:

$2^{-1}=0.5$

Combining the above:

$+1*0.5$

which is the original value:

$0.5$

Let's look at a more complicated example:

```
num2 = 0.12
num2.hex()
```

![img_089](./images/img_089.png)

This gives ```'0x1.eb851eb851eb8p-4'```

The general form is:

```
'[sign] [0x] integer [. fraction] [p exponent]'
```

```[sign]``` the sign is not shown so it is implied to be positive.

```[0x]``` is a constant prefix denoting a hexadecimal number.

```integer [. fraction]``` are in hexadecimal. To convert to decimal powers of 16 need to be used.

The unit 1 and $1*16^{0}=1$

The first value past the decimal point is e which is $14*16^{-1}=0.875$

The second value past the decimal point is b and $11*16^{-2}=0.04296875$

The third value past the decimal point is 8 and $8*16^{-3}=0.001953125$

The fourth value past the decimal point is 5 and $5*16^{-4}=0.0000762939453125$

$\vdots$

Combining the 5 values above gives $1.9199981689453125$ in decimal.

```[p exponent]``` indicates ```2``` to the power of a decimal exponent. In this example ```p-4``` means:

$2^{-4}=0.0625$

Combining the above:

$+1.9199981689453125*0.0625$

this is close to the original value:

$0.11999988555908203$

```
((1 * 16 ** 0) 
 + (14 * 16 ** -1) 
 + (11 * 16 ** -2) 
 + (8 * 16 ** -3) 
 + (5 * 16 ** -4)) * (2 ** -4)
```

![img_090](./images/img_090.png)

In the calculation above only the 4 most significant components of the fraction were used. A closer approximation will be made if all 14 are used. If the result ```'0x1.eb851eb851eb8p-4'``` is examined, notice that ```eb851``` is recurring which means there will be at least some rounding error when using a finite number of digits.

The alternative constructor ```fromhex``` is a class method that is used to create a new float instance from a hexadecimal string. It can be used with the strings above:

```
float.fromhex('0x1.0000000000000p-1')
float.fromhex('0x1.eb851eb851eb8p-4')
```

![img_091](./images/img_091.png)

### Data Model Identifiers

To view the data model identifiers, the directory function ```dir``` can be used:

```
num1 = 0.5
pprint.pprint(dir(num1), compact=True)
```

![img_092](./images/img_092.png)

Most of the numeric identifiers are available and the ```float``` class and the ```int``` class are setup to be consistent with one another. 

The string identfiers ```__repr__``` and ```__str__``` are setup for the formal and informal string repreentations, which in the case of the ```float``` class match. The decimal point is always included in the representation. Scientific notation will display for numbers with an exponent less than ```-5``` and greater than ```16```.

```
num1 = 1.5
num2 = 0.000000000053
num3 = 6.96340e8
repr(num1)
str(num1)
repr(num2)
str(num2)
repr(num3)
str(num3)
```

![img_093](./images/img_093.png)

The ```float``` class has the  ```__hash__``` data model identifier but lacks the ```__index__``` data model identifier. 

This means the dictionary can be used as a key in a mapping:

```
num1
hash(num1)
num_dict = {1.5: 'one and a half', 2.5: 'two and a half'}
num_dict[1.5]
```

![img_094](./images/img_094.png)

But it does not make sense to try and index an ordered collection using a floating point number, there is an ambiguity whena floating point number of 1.5 is used for example and a ```TypeError``` displays:

![img_095](./images/img_095.png)

### Unitary Data Model Identifiers

Casting a float to an integer using the ```int``` init signature wuill truncate the non-integer component of the number:

```
num1 = 1.5
int(num1)
```

![img_096](./images/img_096.png)

Recall that the ```__ceil__```, ```__floor__``` and ```__trunc__``` map to ```math.ceil```, ```math.floor``` and ```math.trunc```. These methods are designed to cast a non-integer number into an integer. The subtle differences between these methods can be seen with  positive and a negative number:

```
import math
num1 = 1.5
```

![img_097](./images/img_097.png)


The closest two integers to ```1.5``` are ```1``` and ```2```. The lower number ```1``` is known as the floor and the higher number ```2``` is known as the ceiling. Truncating the number just removes the non-integer value andis identical to using the init signature of the ```int``` class.

```
math.floor(num1)
math.ceil(num1)
math.trunc(num1)
```

![img_098](./images/img_098.png)

```
num2 = -1.5
math.floor(num2)
math.ceil(num2)
math.trunc(num2)
```

![img_099](./images/img_099.png)

```__round__``` maps to ```round``` function. The docstring of the ```round``` function can be examined in more detail by inputting it with open parentheis and pressing shift ```⇧``` and tab ```↹```:

![img_100](./images/img_100.png)

The ```round``` function by default rounds to the nearest integer however the keyword argument ```ndigits``` can be used to specify the number of digits after the decimal point to round to. For example:

```
num1 = 1.234
round(num1)
round(num1, ndigits=2)
```

![img_101](./images/img_101.png)

### Binary Data Model Identifiers

Most of the binary data model identifiers are consistent and configured to work seamlessly between the integer and float classes. An integer is automatically cast to a floating point number when used in a calculation with a binary operator and a float. 

```
num1 = 1
num2 = 1.5
num1 + num2
```

Explicitly this is the same as:

```
float(num1) + num2
```

![img_102](./images/img_102.png)

Some unexpected behaviour occurs with floating point numbers primarally due to the fact that they are under the hood stored in binary and there are recursive rounding errors:

```
num1 = 0.1
num2 = 0.2
num1 + num2
```

![img_103](./images/img_103.png)

Particular care needs to be taken to ccount for rounding when using conditional operators:

```
round(num1 + num2, ndigits=6) == num3
```

![img_104](./images/img_104.png)

## complex class

A complex number has a real and imaginary component. The imaginary component is a result of the square root of a negative number being undefined with only real components. The symbol $j$ is used to denote this imaginary component.

$$j=\sqrt{-1}$$

The algebra of complex numbers is similar to the algebra of vectors which have seperate $x$ and $y$ components and therefore the real axis is often visualised as $x$ and the imaginary access is visualised as $y$. In a complex number however any square term involving $j$ becomes real, taking on the original definition from above:

$j^{2}=-1$

When the method resolution order for the ```float``` class is examined, it is seen to be independent of the ```int``` class and ```float``` classes. As seen earlier however, these classes are configured to be consistent with each other to ensure compatibility:

```
complex.mro()
```

![img_105](./images/img_105.png)

### Initialization Signature

The init signature of the ```complex``` class can be viewed by inputting the class name with open parenthesis and pressing shift ```⇧``` and tab ```↹```:

![img_106](./images/img_106.png)

The init signaturehas two keyword arguments ```real``` and ```imag``` which each have a default value of ```0```.

![img_107](./images/img_107.png)

It is more common to use the shorthand notation to initiate a complex class as seen in the output:

```
num1 = 2+1j
num1
```

![img_108](./images/img_108.png)

### Identifiers

For example if the instance is assigned to an object name ```num1```:

```
num1 = 2+1j
```

Then pressing ```num1``` followed by a dot ```.``` and tab ```↹``` displays the identifiers:

![img_109](./images/img_109.png)

The ```real``` attribute will read off the real component of the complex number and the ```imag``` component will read of the imaginary component, which is now non-zero:

```
num1 = 2+1j
num1.real
num1.imag
```

![img_110](./images/img_110.png)

The complex conjugate can be calculated by using the ```conjugate``` method:

```
num1 = 2+1j
num1.conjugate()
```

![img_111](./images/img_111.png)

Notice the real component remains unchanged but the sign of the imaginary component is flipped. The consequence of this will be explored in a bit more detail in a moment.

### Data Model Identifiers

To view the data model identifiers, the directory function ```dir``` can be used:

```
num1 = 2+1j
pprint.pprint(dir(num1), compact=True)
```

![img_112](./images/img_112.png)

Notice that there are substantially less of the mathematical data model identifiers defined meaning the operators for ones that are not defined cannot be used. Dor example there is no ```__floordiv__``` or  ```__mod__``` meaning ```//``` and ```%``` cannot be used with a complex number:

![img_113](./images/img_113.png)

There is no ```__round__``` so the ```round``` function cannot be used. 

![img_114](./images/img_114.png)

Likewise there is no ```__floor__```, ```__ceil__``` or ```__trunc__``` so the math functions ```math.floor```, ```math.ceil``` and ```math.trunc``` cannot be used.

For casting to other data types only ```__complex__``` and ```__bool__``` are defined. Using the ```complex``` initialization signature will instantiate the same complex number. Using the ```bool``` initialization signature will result in a ```True``` value for any non-zero real or imaginary component. 

```
num1 = 2+1j
bool(num1)
num2 = 0+1j
bool(num2)
num3 = 0+0j
bool(num3)
```

![img_115](./images/img_115.png)

A ```TypeError``` will display if attempting to cast to an ```int``` or a ```float```:

![img_116](./images/img_116.png)

### Unitary Data Model Identifiers

The supported unitary data model identifiers will operate on both the real and imaginary component of the complex number. For example:

```
num1 = 2-1j
+num1
-num1
abs(num1)
```

![img_117](./images/img_117.png)

## Binary Data Model Operators

The binary operators will carry out the mathematical operation for there real components and imaginary components, treating the real and imaginary components as seperate variables. This can be seen with addition and subtraction:

$$(2+1j)+(3-2j)=(2+3)+(1-2)j=5-1j$$

```
num1 = 2+1j
num2 = 3-2j
num1 + num2
```

![img_118](./images/img_118.png)

$$(2+1j)-(3-2j)=(2-3)+(1+2)j=-1+3j$$

```
num1 = 2+1j
num2 = 3-2j
num1 - num2
```

![img_119](./images/img_119.png)

In multiplication, the individual terms are algebraically calculated:

$$(2+1j)\ast(3-2j)=2\ast3+1j\ast3+2j\ast-2j+1j\ast-2j=6+3j-4j-2j^{2}=6-j-2j^{2}$$

However taking the original definition of $j^{2}=-1$, this can be simplified:

$$6-j-2j^{2}=6-j-2\ast-1=6-j+2=8-j$$

```
num1 = 2+1j
num2 = 3-2j
num1 * num2
```

![img_120](./images/img_120.png)

Now some properties of the complex conjugate can be explored. When a number is added to its complex conjugate, the real component doubles and the imaginary components cancel out. When a number is subtracted by its complex conjugate its real term cancels and its imaginary component doubles. 

$$(2+1j)+(2-1j)=(4)+(1-1)j=4$$

$$(2+1j)-(2-1j)=(2-2)+(1+1)j=2j$$

Multiplication of a number by its complex conjugate yields the square magnitude of a complex number. This is real as the imaginary components cancel and $j^{2}=-1$:

$$(2+1j)\ast(2-1j)=2\ast2+1j\ast2+2\ast-1j+1j\ast1j=4+2j-2j-1j^{2}=4-j^{2}=5$$

```
num1 = 2+1j
num2 = num1.conjugate()
num2
num1 + num2
num1 - num2
num1 * num2
```

![img_121](./images/img_121.png)

Float division of a complex number uses the complex conjugate of the denominator. This is multiplied to the top and bottom:

$$\frac{\left(2+1j\right)}{\left(2-2j\right)}=\frac{\left(2+1j\right)}{\left(2-2j\right)}\ast\frac{\left(2+2j\right)}{\left(2+2j\right)}=\frac{\left(2+1j\right)\ast\left(2+2j\right)}{\left(2-2j\right)\ast\left(2+2j\right)}$$

This means the denominator can be evaluated down to a real number:

$$\frac{\left(2+1j\right)\ast\left(2+2j\right)}{\left(4-4j+4j-4j^2\right)}=\frac{\left(2+1j\right)\ast\left(2+2j\right)}{8}$$

The numerator can then be evaluated to get the result:

$$\frac{4+2j+4j+2j^{2}}{8}=\frac{2+6j}{8}=\frac{1+3j}{4}=0.25+0.75j$$

```
num1 = 2+1j
num2 = 2-2j
num1 / num2
```

![img_122](./images/img_122.png)

The equal to operator and the not equal to operator are setup for the ```complex``` class. These check if both the real components are equal and if both the iamginary components are equal:

```
num1 = 2+1j
num2 = 3-3j
num1 == num2
num1 != num2
```

![img_123](./images/img_123.png)

The other four conditional operators will give a ```TypeError``` not supported. This is because there are two seperate sets of numbers to compare. The real component of ```num2``` is higher but the imaginary component of ```num1``` is higher, making their comparison ambiguous:

![img_124](./images/img_124.png)

## Decimal class

Floating point arithmetic differs from the decimal arithmetic one is acustomed to being brought up with the decimal system. The recursive rounding errors seen with floating point numbers are because they are under the hood stored as a binary number. Python has a ```Decimal``` class which is more precise than the floating point numbers and used in physics or finicial application when more accurcy is required. The down side of using the ```Decimal``` class is it must be imported.

### Importing Decimal

The ```Decimal``` class (PascalCase) is found within ```decimal``` module. The ```decimal``` module can be imported using:

```
import decimal
```

Inputting ```decimal.``` and pressing tab ```↹``` will display a list of identifiers:

![img_125](./images/img_125.png)

Most of the identifers are related to the context. To examine the context, the ```getcontext``` function can be used:

![img_126](./images/img_126.png)

The context has a precision ```prec``` which has a default value of 28. The identifier ```MAX_PREC``` specifies the maximum precision possible on a supercomputer, although using this value will likely exceed your computer memory.

The context has ```rounding``` which has a default value of ```ROUND_HALF_EVEN```. The other possible rounding modes are all other identifiers ```ROUND_05UP```, ```ROUND_CEILING```, ```ROUND_DOWN```, ```ROUND_FLOOR```, ```ROUND_HALF_DOWN```, ```ROUND_HALF_EVEN```, ```ROUND_HALF_UP```, ```ROUND_UP```.

The context has ```Emin``` and ```Emax``` which are the minimum and maximum values of the exponent. The identifiers ```MIN_EMIN``` and ```MAX_EMAX``` specifies the minimum and maximum values for the exponent possible on a supercomputer, once again using these values will likely exceed your computer memory. The context has ```capitals``` which is assigned to a boolean value. If capitals is enabled ```E``` will display in the exponent, otherwise ```e``` will display in the exponent.

The ```Etiny``` is a value equal to ```Emin - prec + 1```. There is a corresponding minimum possible value ```MIN_ETINY``` possible on a supercomputer, once again using this value will likely exceed your computer memory.

Otherwise there are ```flags``` and ```traps```. A flag will flag up a warning but proceed with an operation while a trap will raise an error, halting any subsequent Python code execution. The signals available for flags and traps are ```Clamped```, ```DecimalException```, ```DivisionByZero```, ```Inexact```, ```InvalidOperation```, ```Overflow```, ```Rounderd```, ```Subnormal```, ``` Underflow```, ```FloatOperation```. Some other signals are available for traps ```DivisionImpossible```, ```DivisionUndefined```,  ```InvalidContext```, ```ConversionSyntax```.

Identifiers can be accessed from the ```getcontext``` function by inputting ```decimal.getcontext().``` and pressing tab ```↹ ```:

![img_127](./images/img_127.png)

The statements can be accessed, essentially as attributes and assigned to new values.

It is also possible to instantiate one of the classes ```Context```, ```BasicContext```, ```DefaultContext``` and ```ExtendedContext``` to use with the function ```setcontext```. ```localcontext``` is an option to use a local context within a context manager, typically a ```with``` code block.

The main item of interest is the ```Decimal``` class, there is alsp the ```DecimalTuple``` which is a named tuple representation.

This guide will use the default context and therefore just import the ```Decimal``` class directly.

```
from decimal import Decimal
```

![img_128](./images/img_128.png)

### Initialization Signature

Once imported the docstring of the ```Decimal``` class can be viewed by inputting it with open parenthesis and pressing shift ```⇧``` and tab ```↹```:

![img_129](./images/img_129.png)

The initialization signature has a keyword input argument which is normally a string:

```
num1 = Decimal(value='1')
num1
```

![img_130](./images/img_130.png)

Value can also be an integer. Notice that the representation defaults to a string:

```
num1 = Decimal(value=1)
num1
```

![img_131](./images/img_131.png)

When the value is not an integer, it should be supplied as a string:

```
num1 = Decimal(value='0.1')
num1
```

![img_132](./images/img_132.png)

Notice that if the value is supplied as a floating point number, the limited precision and recursive rounding errors due to float binary encoding carry over to the conversion:

```
num1 = Decimal(value=0.1)
num1
```

![img_133](./images/img_133.png)

For this reason it is preferable to use a string to instantiate a decimal opposed to another number. There are some more details about this in the alternative constructor ```from_float``` which is a class method. Its docstring can be viewed by inputting the method with open parenthesis followed with a shift ```⇧``` and tab ```↹```:

![img_134](./images/img_134.png)

Using this alternative constructor, gives a similar result to providing a floating point number:

```
num1 = Decimal.from_float(0.1)
num1
```

![img_135](./images/img_135.png)

It is also possible to instantiate using a tuple of integers. This has the form: ```(sign, (digits), power)``` where the sign is ```0``` for positive values and ```1``` for negative values. The digits are each of the digits in the mantissa and the power is the power of the decimal exponent.

```
num1 = Decimal(value=(0, (1,), -1))
num1
```

![img_136](./images/img_136.png)

If using the tuple notation, it is often easier to use the named tuple class ```DecimalTuple```, which adds names to the fields in the tuple and therefore makes the code more readible:

```
from decimal import DecimalTuple
dectuple1 = DecimalTuple(sign=0, digits=(1,), exponent=(-1))
dectuple1
num1 = Decimal(value=dectuple1)
num1
```

![img_137](./images/img_137.png)

Or more directly:

```
num1 = Decimal(value=DecimalTuple(sign=0, digits=(1,), exponent=(-1)))
num1
```

![img_138](./images/img_138.png)

### Identifiers

For example if the instance is assigned to an object name ```num1```:

```
num1 = Decimal(value='0.1')
```

Then pressing ```num1``` followed by a dot ```.``` and tab ```↹``` displays the identifiers:

![img_139](./images/img_139.png)

There is a large number of identifiers available for the ```Decimal``` class. These identifiers include equivalents to mathematical functions that are compartmentalised into a seperate ```math``` module for the the other numeric datatypes. These will be covered in the ```math``` module tutorial once some other basics have been established.

The ```Decimal``` class is setup, like the other number types for compatibility with the ```complex``` class. 

```
num1 = Decimal(value='0.1')
num1.real
num1.imag
num1.conjugate()
```

![img_140](./images/img_140.png)

Although there is some compatibility, the ```complex``` class only operates with floating point numbers and any decimal instances are essentially cast to floating point approximations. This can be seen if the following is attempted:

```
num1 = Decimal(value='0.1')
num2 = Decimal(value='0.2')
num3 = complex(real=num1, imag=num2)
num4 = complex(real=num2, imag=num1)
num3 + num4
```

![img_141](./images/img_141.png)

There is also some compatibility with the ```Fraction``` class:

```
num1 = Decimal(value='0.1')
num1.as_integer_ratio()
```

![img_142](./images/img_142.png)

The ```as_tuple``` method and ```to_eng_string``` will display the decimal as ```DecimalTuple``` and engineering string respectively:

```
num1 = Decimal(value='1.2345e8')
num1.as_tuple()
```

The engineering generally uses three digits and then a power that is a multiple of three. 

```
num1.to_eng_string()
```

![img_143](./images/img_143.png)

In engineering and scientific applciations typically the power and the unit are combined into a unit with a prefix. The above number if it was a length for example would be taken as 123.45 megametres or 123.45 Mm.

|power|prefix name|prefix letter|
|---|---|---|
|$10^{24}$|yotta|Y|
|$10^{21}$|zetta|z|
|$10^{18}$|exa|E|
|$10^{15}$|peta|P|
|$10^{12}$|tera|T|
|$10^{9}$|giga|G|
|$10^{6}$|mega|M|
|$10^{3}$|kilo|k|
|$10^{-3}$|milli|m|
|$10^{-6}$|micro|µ|
|$10^{-9}$|nano|n|
|$10^{-12}$|pico|p|
|$10^{-15}$|femto|f|
|$10^{-18}$|atto|a|
|$10^{-21}$|zepto|z|
|$10^{-24}$|yocto|y|

### Data Model Identifiers

To view the data model identifiers, the directory function ```dir``` can be used:

```
num1 = Decimal(value='0.1')
pprint.pprint(dir(num1), compact=True)
```

![img_144](./images/img_144.png)

Differences between the formal string representation and informal string representation can be seen by comparing the output from the ```repr``` and ```str``` functions respectively:

```
num1 = Decimal(value='0.1')
repr(num1)
str(num1)
```

![img_145](./images/img_145.png)

The data model identifiers in the Decimal class behave similarly to their counterparts in the float class. The recursive rounding issues prevalent due to binary encoding are not prevalent:

```
num1 = Decimal(value='0.1')
num2 = Decimal(value='0.2')
num1 + num2
0.1 + 0.2
```

![img_146](./images/img_146.png)

```
num1 = Decimal(value='0.5')
num2 = Decimal(value='0.4')
num1 - num2
0.5 - 0.4
```

![img_147](./images/img_147.png)

```
num1 = Decimal(value='0.1')
num2 = Decimal(value='0.2')
num3 = Decimal(value='0.3')
num3 == num1 + num2
```

![img_148](./images/img_148.png)

The recursive rounding issues prevalent due to decimal encoding are however prevalent:

```
num1 = Decimal(value='1')
num2 = Decimal(value='3')
onethird = num1 / num2
```

![img_149](./images/img_149.png)

```
onethird + onethird + onethird
onethird * 3
```

![img_150](./images/img_150.png)

Care needs to be taken with comparison operators when decimal recursive rounding issues occur:

```
threethird = onethird + onethird + onethird
threethird
num1 == threethird
num1 > onethird + onethird + onethird
```

![img_151](./images/img_151.png)

### Traps

The traps are configured, by default to match those of the float class:

```
1.0 / 0.0
```

![img_152](./images/img_152.png)

```
num1 = Decimal(value='1.0')
num2 = Decimal(value='0.0')
num1 / num2
```

![img_153](./images/img_153.png)

This behaviour is defined in the context trap. To view the context, import the following:

```
from decimal import Decimal, getcontext, DivisionByZero
```

Then use the function ```getcontext```:

![img_154](./images/img_154.png)

If ```getcontext()``` is input followed by a dot ```.``` and tab ```↹``` a number of identifiers can be seen:

![img_155](./images/img_155.png)

The ```traps``` statement and ```clear_traps``` function can be used:

```
getcontext().traps
getcontext().clear_traps()
getcontext().traps
```

![img_156](./images/img_156.png)

Notice that the ```traps``` statement displays a dictionary. A dictionary has key value pairs. In this case the keys are the error classes and the values are boolean ```True``` or ```False```. When the traps are cleared these all have a value of ```False```. Now the following works:

```
num1 / num2
```

![img_157](./images/img_157.png)

Notice that the returned ```Decimal``` instance incorporates a string of ```'Infinity'```.

The traps dicitionary can be indexed into with one of the error class signals and assigned a boolean value of ```True```. This enables the trap and the error class will display when division by zero is attempted:

```
getcontext().traps[DivisionByZero] = True
num1 / num2
```

![img_158](./images/img_158.png)

Other traps can be enabled or disabled in the context in a similar manner.

## Fraction class

The ```Fraction``` class is used for fractions.

### Importing Fraction

The ```Fraction``` class (PascalCase and singular) is found within ```fractions``` module (snake_case and plural). The ```fractions``` module can be imported using:

```
import fractions
```

![img_159](./images/img_159.png)

A list of identifiers can be seen by inputting ```fractions``` followed by a dot ```.``` and tab ```↹```:

![img_160](./images/img_160.png)

Most of the identifiers are modules or dependencies. The main identifier of interest is the ```Fractions``` class which is typically imported directly:

```
from fractions import Fraction
```

![img_161](./images/img_161.png)

### Initialization Signature

The init signature of the ```Fraction``` class can be viewed by inputting the class name with open parenthesis and pressing shift ```⇧``` and tab ```↹```:

![img_162](./images/img_162.png)

A Fraction is normally created with two integers. These can be supplied using the ```numerator``` and ```denominator``` keyword arguments. The default value for the ```numerator``` is ```0``` and for the ```denominator``` is ```None``` whch in this case is a value of ```1``` effectively creating a fraction that is an integer.

The following fraction can be created:

$\text{num1}=\frac{3}{8}$

```
num1 = Fraction(numerator=3, denominator=8)
num1
```

![img_164](./images/img_164.png)

```
num1 = Fraction('3/8')
num1
```

![img_165](./images/img_165.png)

It is also possible to instantiate a Fraction using a ````Decimal``` or ```float``` instances for the numerator. 

```
num1 = Fraction(numerator=Decimal('0.2'))
num1
```

![img_167](./images/img_167.png)

Note the recursive rounding issues for floating point numbers will be carried over into the fraction:

```
num1 = Fraction(numerator=0.2)
num1
```

![img_168](./images/img_168.png)

A string of a number which incorporates a decimal point, will be assumed to be a ```Decimal```:

```
num1 = Fraction(numerator='0.2')
num1
```

![img_169](./images/img_169.png)

The method resolution order for the ```Fraction``` class can be examined using:

```
fractions.Fraction.mro()
```

![img_166](./images/img_166.png)

Unlike the other data types examined so far which are written in C. The fractions module is available as a physical script file which can be examined:

![img_170](./images/img_170.png)

### Identifiers

For example if the instance is assigned to an object name ```num1```:

```
num1 = Fraction(numerator=3, denominator=8)
num1
```

Then pressing ```num1``` followed by a dot ```.``` and tab ```↹``` displays the identifiers:

![img_171](./images/img_171.png)

The ```Fraction``` class has limited interoperability with the ```complex``` class and can be conceptualised as the complex number:

$$\frac{3}{8}+0j$$

where $j = \sqrt{-1}$.

The ```real``` attribute reads the real value will match the value of the fraction in this case £\frac{3}{8}$ and the ```imag``` will be ```0```. The associated method ```conjugate``` takes these two attributes and inverts the sign of the ```imag``` attribute, because this is ```0``` the complex conjugate matches the original Fraction:

```
num1 = Fraction(numerator=3, denominator=8)
num1
num1.real
num1.imag
num1.conjugate()
```

![img_172](./images/img_172.png)

The ```complex``` class converts all components made with ```Fractions``` into a component of a floating point number:

```
num1 = Fraction(numerator=3, denominator=8)
num1
num2 = Fraction(numerator=5, denominator=8)
num2
complex(real=num1, imag=num2)
```

![img_173](./images/img_173.png)

The ```numerator``` and the ```denominator``` attributes are accessible. The associated method ```as_integer_ratio``` returns these two attributes as a ```tuple```:

```
num1 = Fraction(numerator=3, denominator=8)
num1
num1.numerator
num1.denominator
num1.as_integer_ratio()
```

![img_174](./images/img_174.png)

```from_decimal``` and ```from_float``` are class methods which can be used to construct a new instance from a ```Decimal``` or ```float```. These behave similarly to the initialization signature:

```
num1 = Fraction.from_decimal(Decimal('0.1'))
num1
num2 = Fraction.from_float(0.1)
num2
```

![img_175](./images/img_175.png)

Notice that ```num2``` has a huge numerator and huge denominator and this is due to the recirsvie rounding errors of the floating point number. The method ```limit_denominator``` can be used to limit the denominator and can be thought of a ```Fraction``` equivalent of rounding:

```
num2 = Fraction.from_float(0.1)
num2
num2.limit_denominator(max_denominator=1000)
```

![img_176](./images/img_176.png)

### Data Model Identifiers

To view the data model identifiers, the directory function ```dir``` can be used:

```
num1 = Fraction(numerator=3, denominator=8)
pprint.pprint(dir(num1), compact=True)
```

![img_177](./images/img_177.png)

The identifiers beginning with a single underscore are used internally by the equivalent data model identifiers with the same name. Recall that the ```__init__``` data model method is called when instantiating a ```Fraction```. When the new Python object is created, the ```__new__``` data model method is called. This creates the new instance which is given the label or object name and then the initialization signature ```__init__``` is called to initialize the instance with the unique numeric data. The ```__getattribute__``` data model identifier is used when an attribute is accessed.

The Python functions ```repr``` and ```str``` use the data model identifiers ```__repr__``` and ```__str__```. Differences between the formal string representation and informal string representation can be seen by comparing the output from the ```repr``` and ```str``` functions respectively:

```
num1 = Fraction(numerator=3, denominator=8)
repr(num1)
str(num1)
```

![img_178](./images/img_178.png)

Recall that the Python function ```dir``` uses the data model identifier ```__dir__``` to display the directory of the object as seen above. The Python ```type``` function uses the datamodel identifier ```__class__```:

```
type(num1)
```

![img_179](./images/img_179.png)

The data model identifier ```__doc__``` is the document string for a string instance. It is more commonly used with the ```?``` which includes some other information from the data model identifiers ```__type__```, ```__str__```, and ```__doc__```:

```
? num1
```

![img_180](./images/img_180.png)

The ```__format__``` data model identifier is typically used by a formatted string:

```
f'The fraction is {num1}.'
```

![img_181](./images/img_181.png)

The ```copy.copy``` and ```copy.deepcopy``` functions use the data model identifiers ```__copy__``` and ```__deepcopy__```:

```
from copy import copy, deepcopy
num2 = copy(num1)
num2
num3 = copy(num1)
num3
```

![img_182](./images/img_182.png)

### Unitary Data Model Identifiers

The unitary operators ```+```, ```-``` and the function ```abs``` use the data model identifiers ```__pos__```, ```__neg__``` and ```__abs__```respectively:

```
num1 = Fraction(numerator=3, denominator=8)
+num1
-num1
abs(-num1)
```

![img_183](./images/img_183.png)

Casting to ```int```, ```bool```, ```float``` or ```complex``` use the data model identifiers ```__int__```, ```bool```, ```__float__``` or ```__complex__```. When these are used the fraction is essentially handled intermediately as float instance and then cast into the other data types:

```
num1 = Fraction(numerator=11, denominator=8)
num1
float(num1)
int(num1)
bool(num1)
complex(num1)
```

![img_184](./images/img_184.png)

The ```math.trunc```, ```math.floor```, ```math.ceil``` and ```round``` use the data model identifiers ```__trunc__```, ```__floor__```, ```__math__``` and ```__round__``` respectively. When these are used the fraction is once again essentially handled intermediately as float instance and then handled like the ```float``` instance owuld be:

```
num1 = Fraction(numerator=11, denominator=8)
num1
float(num1)
math.trunc(num1)
math.floor(num1)
math.ceil(num1)
round(num1, ndigits=2)
```



### Binary Data Model Identifiers

The binary data model methods require two numeric instances, for example:

$$\text{num1} = \frac{3}{4}$$

$$\text{num2} = \frac{1}{8}$$

These can be instantiated using:

```
num1 = Fraction(numerator=3, denominator=4)
num2 = Fraction(numerator=1, denominator=8)
```

![img_186](./images/img_186.png)

It is easier to thnk of the ```*``` operator first which uses the ```__mul__``` data model identifier. Multiplication of the fractions is the product of the numerators divided by the product of the denominators:

$$\text{num1} \ast \text{num2} = \frac{3}{4} \ast \frac{1}{8} = \frac{3 \ast 1}{4 \ast 8} = \frac{3}{32}$$

This can be calculated using:

```
num1 * num2
```

![img_187](./images/img_187.png)

Float division can be thought of multiplication of the inverse:

$$\text{num1} / \text{num2} = \frac{3}{4} / \frac{1}{8} = \frac{3}{4} \ast \frac{8}{1} = \frac{3 \ast 4}{8 \ast 1} = \frac{6}{1} = 6$$

$$\text{num2} / \text{num1} = \frac{1}{8} / \frac{3}{4} = \frac{1}{8} \ast \frac{4}{3} = \frac{1 \ast 4}{8 \ast 3} = \frac{1}{6}$$

This can be calculated using the ```/``` operator which uses the ```__truediv__``` data model identifier:

```
num2 / num1
```

![img_188](./images/img_188.png)

The floor division ```//``` and the modulus ```%``` operators use the ```__floordiv__``` and ```__mod__``` data model identifiers. For ```Fractions``` they are calculated using the following:

$$\text{num2} // \text{num1} = \frac{1}{8} // \frac{3}{4} = \frac{1 \ast 4 // 3 \ast 2}{8 \ast 4} = \frac{4 // 6}{32} = \frac{0}{32} = 0$$

$$\text{num2} \text{﹪} \text{num1} = \frac{1}{8} \text{﹪} \frac{3}{4} = \frac{1 \ast 4 \text{﹪} 3 \ast 2}{8 \ast 4} = \frac{4 \text{﹪} 6}{36} = \frac{4}{36} = \frac{1}{8}$$

```
num2 // num1
num2 % num1
```

![img_189](./images/img_189.png)

The ```divmod``` fucntion returns these two values as a tuple and uses the ```divmod``` data model identifiers:

```
divmod(num2, num1)
```

![img_190](./images/img_190.png)

The ```**``` operator can be used to calculate the power of a ```Fraction``` instance to another ```Fraction``` instance. For simplicity the two numbers will be used:


$$\text{num1} = \frac{3}{4}$$

$$\text{num2} = \frac{1}{8}$$

```
num1 = Fraction(numerator=1, denominator=4)
num2 = Fraction(numerator=3, denominator=2)
```

![img_191](./images/img_191.png)

$$\text{num1} ** \text{num2} = \frac{1}{4} ** \frac{3}{2} = \frac{1 ** \frac{3}{2}}{4 ** \frac{3}{2}} = \frac{1 ** {3} ** \frac{1}{2}}{4 ** 3 ** \frac{1}{2}} = \frac{1 ** \frac{1}{2}}{64 ** \frac{1}{2}} = \frac{1}{8} = 0.125$$

```
num1 ** num2
```

![img_192](./images/img_192.png)



add, 

sub, 

eq, ne, ge, gt, lt, le