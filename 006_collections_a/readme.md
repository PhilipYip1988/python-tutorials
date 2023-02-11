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

## The tuple Class

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

## The list Class

A list is an ordered finite **mutable** collection of references to Python objects. Think of the ```list``` as an ordered numeric active archive and each reference to a Python object in this active archive as a record. Because the active archive is mutable, the position of each record in the archive can be altered and items can be added or removed to the archive. In other words a list is a mutable tuple, that can be modified once created. 



### The Initialization Signature

Inputting ```list()``` followed by shift ```⇧``` and tab ```↹``` will display the docstring of the init signature:



A list can be created from an iterable such as a ```tuple``` using the ```list``` class

```
active_archive = list(archive)
active_archive
```



Notice the list is enclosed in square brackets opposed to parenthesis. It can be instantiated directly using:

```
active_archive = [1, True, 3.14, 'hello', 'hello', 'bye']
```


### Identifiers

Returning to:

```
active_archive = [1, True, 3.14, 'hello', 'hello', 'bye']
```

If the instance name ```active_archive``` is input followed by a dot ```.``` and then tab ```↹``` a list of identifiers displays:



For the ```list``` collection the ```index``` and ```count``` identifiers display, these behave identically to their equivalent identifiers in the immutable ```tuple``` and the identifier ```copy``` performs a shallow copy. The rest of the identifiers ```sort```, ```reverse```, ```append```, ```extend```, ```insert```, ```pop```, ```remove``` and ```clear``` are mutable methods which modify the list in place. ```pop``` is the only method to mutate the ```list``` and return a value (the popped value). The other mutable methods do not have a return statement.

If ```active_archive.sort()``` followed by shift ```⇧``` and tab ```↹``` is input, the docstring of the method will display:



By default ```sort``` will use the comparison operators to sort records in a ```list``` of all numeric values or all string values. In this case, sorting will fail showing a ```TypeError``` as this ```list``` has mixed data types:

```
active_archive.sort()
```



There is a keyword input argument ```key``` which can be assigned to a function. If assigned to the ```str```, class the initialization signature of the ```str``` class will be used on every record in a tuple as a key and these keys will be sorted alphabetically:

```
active_archive.sort(key=str)
```

Notice that there is no return statement. Instead ```active_archive``` has been directly mutated (modified). This can be viewed on the Variable Inspector:



Recall that each character in a string is ordinal:

```
ord('1')
ord('3')
ord('T')
ord('h')
```



The method ```reverse``` has no input arguments and will reverse the order of the items in the ```list```:

```
active_archive.reverse()
```



Once again there is no return value for the method and the changes can be vieweed in the Variable Inspector. Because ```sort``` was called before ```reverse```, ```active_archive``` is now reverse sorted.

The ```append``` method is used to ```append``` a single item at the end of a ```list```. For example:

```
active_archive.append('world')
```



Each record in a ```tuple``` or ```list``` is a Python object. This Python object can be another ```tuple``` or ```list``` for example: 

```
nested_archive = ['a', 'b', 'c']
```



This can be appended:

```
active_archive.append(nested_archive)
```



Notice that the ```nested_archive``` is a single record appended to ```active_archive```. A consequence of ```nested_archive``` being considered a single record can be seen when the ```in``` keyword is used. A record in the ```nested_archive``` is not considered being in the ```active_archive```. However ```nested_archive``` as a complete record is in ```active_archive```. This makes sense recalling that each record is a reference and a nested ```list``` or ```tuple``` is a reference to an object of references.

```
'a' in active_archive
['a', 'b', 'c'] in active_archive
```



In addition if the length of the ```active_archive``` is examined:

```
len(active_archive)
```



Notice that the ```nested_archive``` is considered to only be one record. If this record is indexed into, ```nested_list``` is returned. This can also be indexed into:

```
active_archive[7]
active_archive[7][1]
nested_archive[1]
```



If ```active_archive``` is examined, the nested archive can be clearly seen by the additional ```[]```:

```
active_archive
```



The method ```extend``` can be used to extend a list using the contents of an iterable such as a ```tuple``` or ```list```:

```
active_archive.extend(nested_archive)
```



Each record in the ```nested_list``` is now a seperate record in ```active_archive```.

```
'a' in active_archive
len(active_archive)
```



The ```insert``` method behaves similarly to ```append``` except takes in an numeric index input argument to insert a record. The record that was at that index and all subsequent records are increased by an index of one:

```
active_archive.insert(1, nested_archive)
```


The ```pop``` method by default pops off the record at the last index:

```
active_archive.pop()
active_archive
```



Notice that this method has a return statement and returns the value that was popped but also mutates the list. This is the only ```list``` method that mutates the ```list``` and returns a value. ```pop``` by default pops off the last item, acting like an inverse of the ```append``` method. It can however be supplied a numeric index. Once this record is popped all subsequent records are decreased by an index of one:

```
active_archive.pop(2)
active_archive
```


The ```remove``` method, removes the first instance of a specified record. All records subsequent to that record are decreased by an index of one:

```
active_archive.remove(nested_archive)
```



```
active_archive.remove(nested_archive)
```



The method ```clear``` will clear all records:

```
active_archive.clear()
```


### Data Model Identifiers

Returning to:

```
active_archive = [1, True, 3.14, 'hello', 'hello', 'bye']
```

The directory function ```dir``` can be used to look at the data model identifiers available. The ```pprint``` function from the ```pprint``` module can be imported and used to display the as compact:

```
from pprint import pprint
pprint(dir(active_archive), compact=True)
```


```__hash__```

```
hash(active_archive)
```




```__getitem__```, ```__setitem__```, ```__delitem__```

```
active_archive[3]
```

```
active_archive[3] = 'hi'
```


```
del active_archive[3]
```



### Mutability

```
archive1 = [1, 2, 3, 4]
archive2 = ['a', 'b', 'c', archive1]
archive3 = archive2
archive4 = archive2.copy()
```



```
archive4[1] = 'f'
```



```
archive3[1] = 'g'
```



```
archive2[3][1] = 6
```



```
from copy import deepcopy
archive5 = deepcopy(archive2)
```


```
archive5[3][1] = 8
```



```
x = 1
y = 2

def fun():
    x = 4
    y = 5
    return None    

fun()

x
y
```


```
archive = ['a', 'b', 'c']

def fun():
    archive.append('d')
    return None    

fun()

archive
```













