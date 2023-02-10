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


### Data Model Identifiers

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

```
len(archive)
```



The ```in``` keyword uses the data model identifier ```__contains__``` to see if a record is in the archive:

```
record2 in archive
3.14 in archive
```



The ```iter``` function and ```reversed``` function use the ```__iter__``` data model method to instantiate a forward or reverse iterator from the iterable ```tuple```:

```
forward_archive = iter(archive)
```

Recall that an iterator only displays a single element at a time. The ```next``` function moves onto the next element and any previous element is considered consumed:

```
next(forward_archive)
next(forward_archive)
next(forward_archive)
```

Use of ```tuple``` on the ```forward_archive``` consumes the remaining records:

```
tuple(forward_archive)
```



Alternatively:

```
backwards_archive = reversed(archive)
next(backwards_archive)
next(backwards_archive)
tuple(backwards_archive)
```



The ```hash``` function uses the data model identifier ```__hash__```:

```
hash(archive)
```



Note ```hash``` only works when every record in the tuple is itself immutable. If a mutable ```bytearray``` instance is added to the ```tuple```, a ```TypeError```: unhashable type displays:

```
hash(('red', 'green', 'blue', bytearray('black', encoding='ASCII')))
```



Because a ```tuple``` containing only immutable items is itself hashable, it can be used as a key in a mapping such as the dictionary. For example:

```
colors = {(1, 0, 0): 'red', 
          (0, 1, 0): 'green',
          (0, 0, 1): 'blue'}
```



``` 
colors = {('red', 'green', 'blue'): ((1, 0, 0), (0, 1, 0), (0, 0, 1))}
```



The ```?``` uses the data model identifiers ```__class__``` to identify the class and ```__doc__``` to generate information about the ```tuple``` instance:

```
? archive
```



The formal and informal string representation of a ```tuple``` are given by the ```repr``` function and ```str``` class which use the ```__repr__``` and ```__str__``` data model identifiers respectively:

```
repr(archive)
str(archive)
```


For a ```tuple``` these are the same even if the tuple contains string records that have escape characters. For example:

```
file = (r'C:\Users\Philip\Documents', 
        'script0.py')
str(file)
repr(file)
```



This can be contrasted to the equivalent string data model methods which show a clear difference:

```
str(file[0])
repr(file[0])
```



The ```__format__``` data model method is used by formatted strings when formatting a ```tuple```. There are no ```tuple``` specific format specifications:

```
f'The tuple is {archive}'
```



The memory size of a ```tuple``` in bytes can be measured using the function ```sys.getsize``` which uses the data model identifier ```__sizeof__```:

```
import sys
sys.sizeof(archive)
```



The ```__getattribute__```, ```__setattr__``` and ```__delattr__``` identifiers are used to get, set and delete attributes. A ```tuple``` has no attributes so these are not used by the end user.

The ```+``` operator is setup to perform concatenation using the data model identifier ```__add__```:

```
archive1 = ('hello', 1, True)
archive2 = ('bye,' 2, False, 3.14)
archive1 + archive2
```



The ```*``` operator is setup to perform record replication with an integer. The ```*``` operator uses the data model identifier ```__mul__``` or the reverse data model idenfier ```__rmul__``` depending on whether the tuple is to the left hand side or right hand side of the ```*``` operator:

```
archive
archive * 3
3 * archive
```



The six equality operators ```==```, ```!=```, ```<```, ```<=```, ```>```, ```>=``` can be used with a ```tuple```. These use the data model identifiers ```__eq__```, ```__ne__```, ```__lt__``` and ```__le__```, ```__gt__``` and ```__ge__``` respectively. These operators operate along the index of each ```tuple``` archive comparing the records:

```
('red', 'green', 'blue') == ('red', 'green', 'yellow')
```



Conceptualise the above as:

```
('red' == 'red') #equal check next records
('green' == 'green') #equal check next records
('blue' == 'yellow') #different
```



The records at each correspond index are compared one by one. The following comparison is made at index 0 and index 1. There is a difference at index 1 and the right hand tuple is determined to be greater:

```
('red', 'green', 'blue') > ('red', 'yellow')
```



The following comparison is made at index 0 and index 1. The records for both archives at these indexes are the same. The left archive has an additional record and is determined to be greater:

```
('red', 'green', 'blue') > ('red', 'green')
```



Comparisons can be made with numeric tuples:

```
(1, 5, 9) > (1, 7)
```



However care needs to be made when a tuple archive contains records of mixed datatypes:

```
(1, 'hello', 2) > (1, 'hello', 3)
```



If records that are being comapred are of different data types, there will be a ```TypeError```, similar to the same comparison made outwith a ```tuple```:

```
(1, 'hello', 2) > (1, 'hello', 'three')
```



The data model identifiers ```__getstate__```, ```__reduce__```, ```__reduce_ex__``` and ```__getnewargs__``` are used by the pickle module to serialize the ```tuple```. The ```__init_subclass__``` is used for subclassing.

## The list class

A list is an ordered finite **mutable** collection of references to Python objects. Think of the ```list``` as an ordered numeric *live register* and each reference to a Python object in the live register as a *live report*. In other words a list is a mutable tuple, that can be modified once created. 



Active archive...



act



### The Initialization Signature

Inputting ```list()``` followed by shift ```⇧``` and tab ```↹``` will display the docstring of the init signature:



A list can be created from an iterable such as a ```tuple``` using the ```list``` class

```
register = list(archive)
register
```



Notice the list is enclosed in square brackets opposed to parenthesis. It can be instantiated directly using:

```
register = [1, True, 3.14, 'hello', 'hello', 'bye']
```


### Identifiers
