# Collections

## Fundamental Data Types Recap

In the previous two tutorials, three fundamental text data types were examined:

* The Immutable Unicode String (```str```)
* The Immutable Byte String (```bytes```)
* The Mutable Byte Array (```bytearray```)

And six fundamental numeric data types were examined:

* The Immutable Integer Whole Number (```int```)
* The Boolean ```True``` or ```False``` (```bool```)
* The Immutable Floating Point Number, Displayed in Decimal but Encoded in Binary (```float```)
* The Immutable Complex Number with a Real and Imaginary components (```complex```)
* The Immutable Decimal Number, Displayed in Decimal and Encoded in Decimal (```Decimal```)
* The Immutable Fraction (```Fraction```)

The text data types are collections, where the base unit of the ```str``` class is a character and the base unit of the ```byte``` and ```bytearray``` classes is a single byte. In these collections the ```+``` operator which uses the data model identifier ```__add__``` is configured for concantenation. 

In contrast, the numeric data types are individual numeric values and the ```+``` operator which uses the data model identifier ```__add__``` is configured for addition. The other numeric operators are setup for other numeric operations.

The ```str``` and ```byte``` classes were seen to be immutable. This means that once they were created, they cannot be modified. All identifiers returned a new value. With these immutable collections a value can be read from an index but a new value cannot be assigned to an index. 

The ```bytearray``` in contrast was seem to be mutable and had supplementary methods which had no return value but directly mutated the ```bytearray``` instance. In an immutable collection a value can be read from an index and a new value can be assigned to an index. 

The numeric data types were seen to be immutable.

These concepts will be explored with other inbuilt Python collections.

## The tuple Class (tuple)

A tuple is an ordered finite immutable collection of references to Python objects. Think of the ```tuple``` as an ordered numeric *archive* and each reference to a Python object in the archive as a *record*.

There are similarities between a Unicode string ```str``` and a ```tuple```. Both are immutable collections, in the case of a ```str```, the individual unit is a Unicode character. In the case of a ```tuple```, each unit is a reference to a Python object.



### The Initialization Signature

Inputting ```tuple()``` followed by shift ```⇧``` and tab ```↹``` will display the docstring of the init signature:



It has a single input argument which is an iterable. 

More conventionally the ```tuple``` uses parenthesis ```( )``` to enclose the collection and a comma ```,``` as a delimiter to seperate each individual items. A number of Python objects can be assigned:

```
record0 = 1
record1 = True
record2 = 3.14
record3 = 'hello'
record4 = 'hello'
record5 = 'goodbye'
```



A ```tuple``` of records can be created:

```
archive = (record0, record1, record2, record3, record4, record5)
archive
```



Each record can also be placed on a seperate line:

```
archive = (record0, 
           record1, 
           record2, 
           record3, 
           record4, 
           record5)
archive
```



Python objects do not require previous assignment to an individual object name. In the example below, the only record or reference to these objects is within the ```tuple``` ```archive```:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
archive
```



In the previous tutorials the parenthesis ```()``` were seen to be used in Python to call a function and enclose any input arguments and for order of precedence in numeric operations (PEDMAS). 

Therefore to create an archive with a single item, a ```,``` delimiter must be placed after the single item:

```
pedmas = (1 + 2)
pedmas
single_archive = (1 + 2,)
single_archive
```



To create an empty archive, the ```tuple``` class is used:

```
empty_archive = tuple()
empty_archive
```



### Identifiers

Returning to:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
```

If the instance name ```archive``` is input followed by a dot ```.``` and then tab ```↹``` a list of identifiers displays:



For the ```tuple``` collection only ```index``` and ```count``` display. These have been seen on the ```str```, ```byte``` and ```bytearray``` class and behave similarly:



If ```archive.index()``` followed by shift ```⇧``` and tab ```↹``` is input, the docstring of the method will display:



```
archive.index(3.14)
archive.index(1)
archive.index(1, 1, 6)
```


```
archive.index(1, 2, 6)
```



If ```archive.count()``` followed by shift ```⇧``` and tab ```↹``` is input, the docstring of the method will display:




```
archive.count(3.14)
archive.count(1)
```


## Data Model Identifiers

Returning to:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
```

The directory function ```dir``` can be used to look at the data model identifiers available. The ```pprint``` function from the ```pprint``` module can be imported and used to display the as compact:

```
from pprint import pprint
pprint(dir(archive), compact=True)
```



The ```__init__``` data model method is called when instantiating a ```tuple```:



When the new Python object is created, the ```__new__``` data model method is called. This creates the new instance which is given the label or object name ```archive``` and then the initialization signature ```__init__``` is called to initialize the instance a record at each index of the tuple.



The ```type``` class uses the data model identifier ```__class__``` to determine the class an instance belongs to:

```
type(archive)
```



The ```__getitem__```, ```__class_getitem__```, ```__len__```, ```__contains__``` and ```__iter__``` are data model identifiers are associated with immutable ordered collections.

Indexing using square brackets uses the data model method ```__getitem__``` and there is an associated class method ```__class_getitem__```. Indexing with the numeric index ```0``` will look up the associated record at this index, recalling a record is a reference to a Python object and return the Python object:

```
archive[0]
```



The ```len``` function uses the data model identifier ```__len__``` to determine how many records are stored within the ```archive```.



, , ```__iter__```, ```__len__```, ```__contains__```




iter(objects)

reversed(objects)

len(objects)

3.14 in objects

```__hash__```

hash(objects)

```
{(1, 0, 0): 'red', 
 (0, 1, 0): 'green',
 (0, 0, 1): 'blue'}
``` 



















The ```?``` uses the data model identifiers ```__class__``` to identify the class and ```__doc__``` to generate information about the ```tuple``` instance:


```
? objects
```



```
f'The tuple is {objects}'
sys.sizeof(objects)
```

```__class__```, ```__format__```, ```__sizeof__```











The formal and informal string representation of a ```tuple``` are given by the ```repr``` function and ```str``` class which use the ```__repr__``` and ```__str__``` data model identifiers respectively:

```
repr(objects)
str(objects)
```


For a ```tuple``` these are the same even if the tuple cotnains string records that have escape characters. For example:

```
file = (r'C:\Users\Philip\Documents', 
        'script0.py')
```        

```
str(file)
repr(file)
```

```
str(file[0])
repr(file[0])
```


















The ```__getattribute__```, ```__setattr__``` and ```__delattr__``` identifiers are used to get, set and delete attributes. A ```tuple``` has no attributes so these are not used by the end user.

















```__add__```, ```__mul__```, ```__rmul__```

```
colors = ('red', 'green', 'blue')
objects + colors

3 * objects
objects * 3
```



```__eq__```, ```__ne__```, ```__gt__```, ```__ge__```, ```__lt__``` and ```__le__```

```
('red', 'green', 'blue') > ('red', 'green', 'yellow')
```

```
('red', 'green', 'blue') > ('red', 'green', 2)
```



The data model identifiers ```__getstate__```, ```__reduce__```, ```__reduce_ex__``` and ```__getnewargs__``` are used by the pickle module to serialise the ```tuple```.


 
For subclassing:

```__init_subclass__```



