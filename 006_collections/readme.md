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

Inputting ```tuple()``` followed by shift ```⇧``` and tab ```↹``` will display the docstring of the init signature. It has a single input argument which is an iterable:

![img_001](images/img_001.png)

More conventionally the ```tuple``` uses parenthesis ```( )``` to enclose the collection and a comma ```,``` as a delimiter to seperate each individual items. A number of Python objects can be assigned:

```
record0 = 1
record1 = True
record2 = 3.14
record3 = 'hello'
record4 = 'hello'
record5 = 'goodbye'
```

![img_002](images/img_002.png)

A ```tuple``` of records can be created:

```
archive = (record0, record1, record2, record3, record4, record5)
archive
```

![img_003](images/img_003.png)

Each record can also be placed on a seperate line which can make it eaiser to visualise longer entries:

```
archive = (record0, 
           record1, 
           record2, 
           record3, 
           record4, 
           record5)
archive
```

![img_004](images/img_004.png)

Python objects do not require previous assignment to an individual object name. In the example below, the only record or reference to these objects is within the ```tuple``` ```archive```:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
archive
```

![img_005](images/img_005.png)

In the previous tutorials the parenthesis ```()``` were seen to be used in Python to call a function and enclose any input arguments and for order of precedence in numeric operations (PEDMAS). 

Therefore to create an archive with a single item, a ```,``` delimiter must be placed after the single item:

```
pedmas = (1 + 2)
pedmas
single_archive = (1 + 2,)
single_archive
```

![img_006](images/img_006.png)

To create an empty archive, the ```tuple``` class is used:

```
empty_archive = tuple()
empty_archive
```

![img_007](images/img_006.png)

Returning to:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
```

The JupyterLab Variable Inspector can be opened from the right click context menu:

![img_008](images/img_008.png)

Sadly this Variable Inspector is limited:

![img_009](images/img_009.png)

The Variable Explorer in the Spyder IDE is interactive and gives lots more information. Note the name, size and type on the Variable Explorer:

![img_010](images/img_010.png)

Double clicking the value on the Variable Explorer, opens it in its own window:

![img_011](images/img_011.png)

Note the numeric index starting at zero. For each index, there is a record which points to a value, this value also has a type and size. All the fields are highlighted in grey, because they cannot be editted in the immutable tuple.

### Identifiers

Returning to:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
```

![img_012](images/img_012.png)

If the instance name ```archive``` is input followed by a dot ```.``` and then tab ```↹``` a list of identifiers displays:

For the ```tuple``` collection only ```index``` and ```count``` display. These have been seen on the ```str```, ```byte``` and ```bytearray``` class and behave similarly.

![img_013](images/img_013.png)

If ```archive.index()``` followed by shift ```⇧``` and tab ```↹``` is input, the docstring of the method will display:

![img_014](images/img_014.png)

For example, the index of the value ```3.14``` can be determined:

```
archive.index(3.14)
```

![img_015](images/img_015.png)

![img_016](images/img_016.png)

The index of the first occurance of the value ```1``` can be determined:

```
archive.index(1)
```

![img_017](images/img_017.png)

![img_018](images/img_018.png)

The index of the second occurance of the value ```1``` can be determined by restricting the search for the value between index 1 (inclusive) to index 6 (exclusive):

![img_019](images/img_019.png)

```
archive.index(1, 1, 6)
```

![img_020](images/img_020.png)

![img_021](images/img_021.png)

If the starting limit is restricted further, so that the reference to the value is not in the specified index range an ```IndexError``` displays:

![img_022](images/img_022.png)

```
archive.index(1, 2, 6)
```

![img_023](images/img_023.png)

If ```archive.count()``` followed by shift ```⇧``` and tab ```↹``` is input, the docstring of the method will display:

![img_024](images/img_024.png)

The count of ```3.14``` can be determined using:

```
archive.count(3.14)
```

![img_025](images/img_025.png)

![img_026](images/img_026.png)

The count of ```1``` can be determined using:

```
archive.count(1)
```

![img_027](images/img_027.png)

![img_028](images/img_028.png)

### Data Model Identifiers

Returning to:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
```

![img_029](images/img_029.png)

The directory function ```dir``` can be used to look at the data model identifiers available. The ```pprint``` function from the ```pprint``` module can be imported and used to display the as compact:

```
from pprint import pprint
pprint(dir(archive), compact=True)
```

![img_030](images/img_030.png)

The ```__init__``` data model method is called when instantiating a ```tuple```:

![img_031](images/img_031.png)

When the new Python object is created, the ```__new__``` data model method is called. This creates the new instance which is given the label or object name ```archive``` and then the initialization signature ```__init__``` is called to initialize the instance a record at each index of the tuple.

The ```type``` class uses the data model identifier ```__class__``` to determine the class an instance belongs to:

```
type(archive)
```

![img_032](images/img_032.png)

![img_033](images/img_033.png)

The ```__getitem__```, ```__class_getitem__```, ```__len__```, ```__contains__``` and ```__iter__``` are data model identifiers are associated with immutable ordered collections.

Indexing using square brackets uses the data model method ```__getitem__``` and there is an associated class method ```__class_getitem__```. Indexing with the numeric index ```0``` will look up the associated record at this index, recalling a record is a reference to a Python object and return the Python object:

```
archive[0]
```

![img_034](images/img_034.png)

![img_035](images/img_035.png)

Slicing can also be carried out using square brackets. Recall, zero-order indexing is used, which is inclusive of the lower bound and exclusive of the upper bound (goes up to but excludes the upper bound):

```
archive[1:4]
```

![img_036](images/img_036.png)

![img_037](images/img_037.png)


The ```len``` function uses the data model identifier ```__len__``` to determine how many records are stored within the ```archive```.

```
len(archive)
```

![img_038](images/img_038.png)

![img_039](images/img_039.png)

![img_040](images/img_040.png)

The ```in``` keyword uses the data model identifier ```__contains__``` to see if a record is in the archive:

```
record2 in archive
```

![img_041](images/img_041.png)

![img_042](images/img_042.png)

The ```iter``` function and ```reversed``` function use the ```__iter__``` data model method to instantiate a forward or reverse iterator from the iterable ```tuple```:

```
forward_archive = iter(archive)
forward_archive
```

![img_043](images/img_043.png)

Recall that an iterator only displays a single element at a time. The ```next``` function moves onto the next element and any previous element is considered consumed:

```
next(forward_archive)
next(forward_archive)
next(forward_archive)
```

![img_044](images/img_044.png)

The first next gives the iterator, the value at index 0:

![img_045](images/img_045.png)

The second next gives the iterator, the value at index 1 and the previous value is discarded:

![img_046](images/img_046.png)

The second next gives the iterator, the value at index 2 and the previous value is discarded:

![img_047](images/img_047.png)

Use of ```tuple``` on the ```forward_archive``` consumes the remaining records:

```
tuple(forward_archive)
```

![img_048](images/img_048.png)

![img_049](images/img_049.png)

Alternatively:

```
backwards_archive = reversed(archive)
next(backwards_archive)
next(backwards_archive)
tuple(backwards_archive)
```

![img_050](images/img_050.png)

![img_051](images/img_051.png)

![img_052](images/img_052.png)

![img_053](images/img_053.png)

The ```hash``` function uses the data model identifier ```__hash__```:

```
hash(archive)
```

![img_054](images/img_054.png)

Note ```hash``` only works when every record in the tuple is itself immutable. If a mutable ```bytearray``` instance is added to the ```tuple```, a ```TypeError```: unhashable type displays:

```
hash(('red', 'green', 'blue', bytearray('black', encoding='ASCII')))
```

![img_055](images/img_055.png)

Because a ```tuple``` containing only immutable items is itself hashable, it can be used as a key in a mapping such as the dictionary. For example:

```
colors = {(1, 0, 0): 'red', 
          (0, 1, 0): 'green',
          (0, 0, 1): 'blue'}

colors[(1, 0, 0)]
```

![img_056](images/img_056.png)

``` 
colors = {('red', 'green', 'blue'): ((1, 0, 0), (0, 1, 0), (0, 0, 1))}

colors[('red', 'green', 'blue')]
```

![img_057](images/img_057.png)

The ```?``` uses the data model identifiers ```__class__``` to identify the class and ```__doc__``` to generate information about the ```tuple``` instance:

```
? archive
```

![img_058](images/img_058.png)

The formal and informal string representation of a ```tuple``` are given by the ```repr``` function and ```str``` class which use the ```__repr__``` and ```__str__``` data model identifiers respectively:

```
repr(archive)
str(archive)
```

![img_059](images/img_059.png)

For a ```tuple``` these are the same even if the tuple contains string records that have escape characters. For example:

```
file = (r'C:\Users\Philip\Documents', 
        'script0.py')
str(file)
repr(file)
```

![img_060](images/img_060.png)

This can be contrasted to the equivalent string data model methods which show a clear difference:

```
str(file[0])
repr(file[0])
```

![img_061](images/img_061.png)

The ```__format__``` data model method is used by formatted strings when formatting a ```tuple```. There are no ```tuple``` specific format specifications:

```
f'The tuple is {archive}'
```

![img_062](images/img_062.png)

The memory size of a ```tuple``` in bytes can be measured using the function ```sys.getsizeof``` which uses the data model identifier ```__sizeof__```:

```
import sys
sys.getsizeof(archive)
```

![img_063](images/img_063.png)

The ```__getattribute__```, ```__setattr__``` and ```__delattr__``` identifiers are used to get, set and delete attributes. A ```tuple``` has no attributes so these are not used by the end user.

The ```+``` operator is setup to perform concatenation using the data model identifier ```__add__```:

```
archive1 = ('hello', 1, True)
archive2 = ('bye', 2, False, 3.14)
archive1 + archive2
```

![img_064](images/img_064.png)

The ```*``` operator is setup to perform record replication with an integer. The ```*``` operator uses the data model identifier ```__mul__``` or the reverse data model idenfier ```__rmul__``` depending on whether the tuple is to the left hand side or right hand side of the ```*``` operator:

```
archive
archive * 3
3 * archive
```

![img_065](images/img_065.png)

![img_066](images/img_066.png)

The six comparison operators ```==```, ```!=```, ```<```, ```<=```, ```>```, ```>=``` can be used with a ```tuple```. These use the data model identifiers ```__eq__```, ```__ne__```, ```__lt__``` and ```__le__```, ```__gt__``` and ```__ge__``` respectively. These operators operate along the index of each ```tuple``` archive comparing the records:

```
('red', 'green', 'blue') == ('red', 'green', 'yellow')
```

![img_067](images/img_067.png)

Conceptualise the above as:

```
('red' == 'red') #equal→check next records
('green' == 'green') #equal→check next records
('blue' == 'yellow') #different→not equal
```

![img_068](images/img_068.png)

The records at each correspond index are compared one by one. The following comparison is made at index 0 and index 1. There is a difference at index 1 and the right hand tuple is determined to be greater:

```
('red', 'green', 'blue') > ('red', 'yellow')
```

![img_069](images/img_069.png)

The following comparison is made at index 0 and index 1. The records for both archives at these indexes are the same. The left archive has an additional record and is determined to be greater:

```
('red', 'green', 'blue') > ('red', 'green')
```

![img_070](images/img_070.png)

Comparisons can be made with numeric tuples:

```
(1, 5, 9) > (1, 7)
```

![img_071](images/img_071.png)

However care needs to be made when a tuple archive contains records of mixed datatypes:

```
(1, 'hello', 2) > (1, 'hello', 3)
```

![img_072](images/img_072.png)

Comparisons are normally made between tuples that have a similar form.

```
student1 = ('James', 'Smith', 31, 'M')
student2 = ('Lucie', 'Brown', 32, 'F')
student1 > student2
```

![img_073](images/img_073.png)

The ```namedtuple``` in the ```collections``` module reinforces this use case. In the ```namedtuple```, each numeric index has a corresponding field name. The field names for the above examples could be ```forename```, ```sirname```, ```age``` and ```sex```.

If records that are being compared are of different data types, there will be a ```TypeError```, similar to the same comparison made outwith a ```tuple```:

```
(1, 'hello', 2) > (1, 'hello', 'three')
```

![img_074](images/img_074.png)

The data model identifiers ```__getstate__```, ```__reduce__```, ```__reduce_ex__``` and ```__getnewargs__``` are used by the pickle module to serialize the ```tuple```. The ```__init_subclass__``` is used for subclassing.

### tuple Unpacking

Supposing the two immutable numeric variables are created:

```
x = 1
y = 2
```

To swap the values of these variables, a temporary variable can be introduced:

```
xold = x
```

Then ```x``` can be assigned the value of ```y```:

```
x = y
```

And ```y``` can be assigned the value of ```xold```:

```
y = xold
```

Finally ```xold``` can be deleted:

```
del xold
```

And the changes are made:

```
x
y
```

![img_075](images/img_075.png)

Switching variables can also be carried out using ```tuple``` unpacking. The original values can be checked:

```
x
y
```

And ```tuple``` unpacking can be explicitly used:

```
(x, y) = (y, x)
```

Then the changes can be checked:

```
x
y
```

![img_076](images/img_076.png)

```tuple``` unpacking is normally implicitly carried out. Notice that the tuples on the left hand side and right hand side are not enclosed in parenthesis:

```
x
y
x, y = y, x
x
y
```

![img_077](images/img_077.png)

The Python interpretter recognises ```x, y``` as the ```tuple``` ```(x, y)```:

```
x
y
x, y
```

![img_078](images/img_078.png)

```tuple``` unpacking is normally carried out in conjunction with functions. A simple function with no input arguments that explicitly returns a tuple of two values can be defined:

```
def fun():
   return ('a', 'b')
```

Then called using:

```
fun()
```

To assign the returned values to variables, ```tuple``` unpacking can be explictly used:

```
(x, y) = fun()
```

These values can be checked:

```
x
y
```

![img_079](images/img_079.png)

It can also be implicitly used:

```
y, x = fun()
```

These values can be checked:

```
x
y
```

![img_080](images/img_080.png)

```tuple``` unpacking is normally implicitly used in the ```return``` statement of the function. The function can be redefined:

```
def fun():
   return 'a', 'b'
```

And called:

```
x, y = fun()
```

The values of ```x``` and ```y``` can be checked:

```
x
y
```

![img_081](images/img_081.png)

## The list Class

To recap a ```tuple``` is an **immutable** collection of references to Python objects. It was conceptualised as an archive of records. Each record has an index and in the case of a ```namedtuple``` also has an associated field name.

A ```list``` is an ordered finite **mutable** collection of references to Python objects. This means that unlike the ```tuple```, the list can be **modified** once it is created. A list can be conceptualised as an active list of records.

### The Initialization Signature

Inputting ```list()``` followed by shift ```⇧``` and tab ```↹``` will display the docstring of the init signature:

![img_082](images/img_082.png)

A list can be created from an iterable such as a ```tuple``` using the ```list``` class:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
active = list(archive)
active
```

![img_083](images/img_083.png)

Notice the list is enclosed in square brackets opposed to parenthesis. It can be instantiated directly using:

```
active = [1, True, 3.14, 'hello', 'hello', 'bye']
```

![img_084](images/img_084.png)

Notice that both ```archive``` and ```active``` display in the Variable Explorer:

![img_085](images/img_085.png)

Recall that ```archive``` is greyed out because it is immutable (cannot be modified):

![img_086](images/img_086.png)

In contrast ```active``` is coloured as all the fields can be mutated (can be modified):

![img_087](images/img_087.png)

For example the value at index 0 can be clicked into and the integer number ```1``` can be replaced with the number ```123```:

![img_088](images/img_088.png)

The Spyder Variable Explorer, has an Insert Row above and Insert Row below button:

![img_089](images/img_089.png)

![img_090](images/img_090.png)

### Identifiers

Returning to:

```
active = [1, True, 3.14, 'hello', 'hello', 'bye']
```

![img_091](images/img_091.png)

If the instance name ```active``` is input followed by a dot ```.``` and then tab ```↹``` a list of identifiers displays:

![img_092](images/img_092.png)

For the ```list``` collection the ```index``` and ```count``` identifiers display, these behave identically to their equivalent identifiers in the immutable ```tuple``` and the identifier ```copy``` performs a shallow copy. The rest of the identifiers ```sort```, ```reverse```, ```append```, ```extend```, ```insert```, ```pop```, ```remove``` and ```clear``` are mutable methods which modify the list in place. ```pop``` is the only method to mutate the ```list``` and return a value (the popped value). The other mutable methods do not have a return statement.

If ```active.sort()``` followed by shift ```⇧``` and tab ```↹``` is input, the docstring of the method will display:

![img_093](images/img_093.png)

By default ```sort``` will use the comparison operators to sort records in a ```list``` of all numeric values or all string values. In this case, sorting will fail showing a ```TypeError``` as this ```list``` has mixed data types:

```
active.sort()
```

![img_094](images/img_094.png)

There is a keyword input argument ```key``` which can be assigned to a function. If assigned to the ```str```, class the initialization signature of the ```str``` class will be used on every record in a tuple as a key and these keys will be sorted alphabetically. Before running the next command, ```active``` will be opened in the Variable Explorer:

![img_095](images/img_095.png)

```
active.sort(key=str)
```

Notice that there is no return statement.

![img_096](images/img_096.png)

This is because the ```list``` ```active``` has been directly mutated (modified) as seen in the Variable Explorer:

![img_097](images/img_097.png)

Recall that each character in a string is ordinal:

```
ord('1')
ord('3')
ord('T')
ord('h')
```

![img_098](images/img_098.png)

The method ```reverse``` has no input arguments and will reverse the order of the items in the ```list```:

![img_099](images/img_099.png)

```
active.reverse()
```

![img_100](images/img_100.png)

Once again there is no return value for the method and the changes can be vieweed in the Variable Explorer:

![img_101](images/img_101.png)

Because ```sort``` was called before ```reverse```, ```active``` is now reverse sorted.

The ```append``` method is used to ```append``` a single item at the end of a ```list```. 

![img_102](images/img_102.png)

For example:

```
active.append('world')
```

![img_103](images/img_103.png)

![img_104](images/img_104.png)

Each record in a ```tuple``` or ```list``` is a Python object. This Python object can be another ```tuple``` or ```list``` for example: 

```
active2 = ['a', 'b', 'c']
```

![img_105](images/img_105.png)

![img_106](images/img_106.png)

![img_107](images/img_107.png)

This can be appended:

```
active.append(active2)
```

![img_108](images/img_108.png)

Notice the change in the Variable Explorer:

![img_109](images/img_109.png)

The last index has a nested list:

![img_110](images/img_110.png)

This can be selected to view the nested list in more detail:

![img_111](images/img_111.png)

![img_112](images/img_112.png)

Notice that ```active2``` is a single record appended to ```active```. Index 7 of ```active``` can be compared to ```active2```. Index 7 of ```active``` and ```active2``` are equal as expected:

```
active[7] == active2
```

However they are also the same object:

```
active[7] is active2
```

![img_113](images/img_113.png)

A consequence of ```active2``` being considered a single record can be seen when the ```in``` keyword is used. A record in the ```active2``` is not considered being in ```active``` as ```in``` only looks for a complete record:

```
'a' in active
```

![img_114](images/img_114.png)

![img_115](images/img_115.png)

```active2``` as a complete record is in ```active```:

```
active2 in active
['a', 'b', 'c'] in active
```

![img_116](images/img_116.png)

In addition if the length of the ```active``` is examined:

```
len(active)
```

![img_117](images/img_117.png)

Notice that the ```active2``` is considered to only be one record. It can be accessed via ```active``` using indexing:

```
active[7]
```

![img_118](images/img_118.png)

![img_119](images/img_119.png)

Since ```active2``` is also a list. It can be indexed into:

```
active2[1]
```

![img_120](images/img_120.png)

![img_121](images/img_121.png)

Or from ```active``` using indexing twice:

```
active[7][1]
```

![img_122](images/img_122.png)

![img_123](images/img_123.png)

![img_124](images/img_124.png)

The method ```extend``` can be used to extend a list using the contents of an iterable such as a ```tuple``` or ```list```:

![img_125](images/img_125.png)

For example:

```
active.extend(active2)
```

![img_126](images/img_126.png)

![img_127](images/img_127.png)

![img_128](images/img_128.png)

Each record in ```active2``` is now a seperate record in ```active```.

```
'a' in active
len(active)
```

![img_129](images/img_129.png)

The ```insert``` method behaves similarly to ```append``` except takes in an numeric index input argument to insert a record. The record that was at that index and all subsequent records are increased by an index of one:

![img_130](images/img_130.png)

For example at index 1:

![img_131](images/img_131.png)

```active2``` can be inserted:

```
active.insert(1, active2)
```

![img_132](images/img_132.png)

![img_133](images/img_133.png)

The ```pop``` method by default pops off the record at the last index:

![img_137](images/img_137.png)

For example, the last item in ```active```:

![img_134](images/img_134.png)

Can be popped using:

```
active.pop()
```

Notice the popped value is returned:

![img_135](images/img_135.png)

**And** the list is mutated:

![img_136](images/img_136.png)

This is the only ```list``` method that mutates the ```list``` and returns a value. 

```pop``` by default pops off the last item, acting like an inverse of the ```append``` method. It can however be supplied a numeric index. Once this record is popped all subsequent records are decreased by an index of one. FOr example the value at index 2:

![img_138](images/img_138.png)

Can be popped:

```
active.pop(2)
```

![img_139](images/img_139.png)

![img_140](images/img_140.png)

The ```remove``` method, removes the first instance of a specified record. All records subsequent to that record are decreased by an index of one:

![img_141](images/img_141.png)

For example, the first occurance of ```active2```:

![img_142](images/img_142.png)

Can be removed using:

```
active.remove(active2)
```

![img_143](images/img_143.png)

![img_144](images/img_144.png)

The method ```clear``` will clear all records, resulting in an empty list:

![img_146](images/img_146.png)

For example:

```
active.clear()
```

![img_145](images/img_145.png)

![img_147](images/img_147.png)

### Data Model Identifiers

Returning to:

```
active = [1, True, 3.14, 'hello', 'hello', 'bye']
```

![img_148](images/img_148.png)

The directory function ```dir``` can be used to look at the data model identifiers available. The ```pprint``` function from the ```pprint``` module can be imported and used to display the as compact:

```
from pprint import pprint
pprint(dir(active), compact=True)
```

![img_149](images/img_149.png)

Most of the data model identifiers listed are the same as the identifiers listed for the immutable ```tuple``` and the ```list``` identifiers behave consistently with their ```tuple``` counterparts. 

The ```hash``` function which uses the ```__hash__``` identifier will always give a ```TypeError``` for a ```list``` because it is immutable:

```
hash(active)
```

![img_150](images/img_150.png)

The **immutable** ```tuple``` only has ```__getitem__```.
The **mutable** ```list``` has ```__getitem__```, ```__setitem__``` and ```__delitem__```. This means for both a ```tuple``` and a ```list```, the value at an index can be read using:

```
active[3]
```

![img_151](images/img_151.png)

![img_152](images/img_152.png)

For a ```list``` it can also be assigned a new value:

```
active[3] = 'hi'
```

![img_153](images/img_153.png)

![img_154](images/img_154.png)

For a ```list``` it can also be deleted. When a record is deleted, all subsequent records have their numeric index value lowered by 1:

```
del active[3]
```

![img_155](images/img_155.png)

![img_156](images/img_156.png)

### Mutability

Many begineer tutorials over-emphasis the use of lists and under-emphasise the use of tuples. Overuse of lists can result in unexpected behaviour due to mutability. If the four object names are assigned:

```
from copy import deepcopy
active1 = [1, 2, 3, 4]
active2 = ['a', 'b', 'c', active1]
active3 = active2
active4 = active2.copy()
active5 = deepcopy(active2)
```

![img_157](images/img_157.png)

![img_158](images/img_158.png)

Notice that:

* ```active1``` is a record in ```active2```
* ```active3``` is an alias of ```active2```
* ```active1``` is therefore a record in ```active3```
* ```active4``` is a shallow copy of ```active2```
* ```active1``` is therefore still a record in ```active4``````active5``` is a deep copy of ```active2```
* a copy of ```active1``` is a record in ```active5```

If ```active4``` is indexed into, to get to the nested list ```active1``` and this is in turn indexed and assigned a new value. The change will modify ```active1``` and ```active4```. Moreover because ```active1``` is included in ```active2``` and ```active3```, these in turn will be modified (think of all of these as four labels to the same object). The copy of ```active1``` in ```active5``` will not be changed:

```
active4[3][1] = 'f'
```

![img_159](images/img_159.png)

![img_160](images/img_160.png)

If another index in ```active4``` is modified, ```active2``` and ```active3``` will not be modified because it is a shallow copy:

```
active4[1] = 'g'
```

![img_161](images/img_161.png)

![img_162](images/img_162.png)

If another index in ```active3``` is modified, ```active2``` will be modified as they are an alias to the same object (think of it as the same object with two labels):

```
active3[2] = 'h'
```

![img_163](images/img_163.png)

![img_164](images/img_164.png)

Returning to:

```
active1 = [1, 2, 3, 4]
active2 = ['a', 'b', 'c', active1]
active3 = active2
active4 = active2.copy()
active5 = deepcopy(active2)
```

![img_165](images/img_165.png)

It is worthwhile understanding the subtle difference between *is* and *is equal to*. When a label *is* another label it means they point to the same object, in other word act as alias. When a label *is equal to* another label, it means the objects, they point to have equal values, they can be different objects with the same values or the same object:

```
active1 is active2[3]
active1 is active3[3]
active1 is active4[3]
active1 is active5[3]
active1 == active5[3]
```

![img_166](images/img_166.png)

```
active2 is active3
active2 is active4
active2 == active4
active2 is active5
active2 == active5
```

![img_167](images/img_167.png)

Create the 5 object names above in the Spyder IDE, take your time indexing into them and making mutations and view the changes on the Variable Explorer. This will give you a better understanding of the subtle concept of mutability, which when used incorrectly can become a minefield when used in larger more complicated nested lists.

**Reassignment often gets confused with mutability.** If the following ```tuple``` is assigned to the object name or label ```archive1```:

```
archive1 = (1, 2, 3, 4, 5)
archive1
```

And then later the following ```tuple``` is reassigned to the object name of label ```archive1```:

```
archive1 = ('a', 'b', 'c', 'd', 'e')
archive1
```

![img_168](images/img_168.png)

The original ```tuple``` ```(1, 2, 3, 4, 5)``` is **not modified**. Instead the label ```archive1``` now points to a completely independent object ```('a', 'b', 'c', 'd', 'e')```. If an object has no object names (which can be conceptualised as labels or references to the object), then it is cleaned up by Pythons garbage collection. This was discussed further in the [Text Data Types: Object Orientated Programming Conception](https://github.com/PhilipYip1988/python-tutorials/tree/main/004_text_datatypes#object-orientated-programming-conception). It is worthwhile re-reading this section to ensure a solid understanding of object orientated prgoramming and mutability.

Functions have their own local scope. If the immutable integer variables ```x``` and ```y``` are assigned in the main scope and then reassigned in the functions local scope they will remain unchanged once the function has been called and the functions local scope has been exited:

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

![img_169](images/img_169.png)

Care should be taken when using an immutable data type within a function. If a mutable method is used on a mutable object in the functions local scope, it will mutate the immutable data type in the global scope:

```
active = ['a', 'b', 'c']

def fun():
    active.append('d')
    return None


fun()

active

fun()

active
```

![img_170](images/img_170.png)

If however reasignment of the mutable object is used within the functions local scope and then the object is mutated. Only the object within the functions local scope will be modified. The mutable object within the global scope will be unaltered:

```
active = ['a', 'b', 'c']

def fun():
    active = ['a', 'b', 'c']
    active.append('d')
    return None  


fun()

active
```

![img_171](images/img_171.png)

Unintended mutability of an original object can occur when the object is supplied as an input argument to a function:

```
active = ['a', 'b', 'c']

def fun(mutable):
    mutable.append('d')
    return None  


fun(active)

active
```

![img_172](images/img_172.png)

When this is not desired, the ```copy``` method can be used to create a local copy of the variable within the functions local scope:

```
active = ['a', 'b', 'c']

def fun(mutable):
    mutable = mutable.copy()
    mutable.append('d')
    return None  


fun(active)

active
```

![img_173](images/img_173.png)

## The set Class

A ```set``` is an unordered finite **mutable** collection of unique Python objects

### The Initialization Signature

Inputting ```set()``` followed by shift ```⇧``` and tab ```↹``` will display the docstring of the init signature:

![img_174](images/img_174.png)

A ```set``` can be created from an iterable such as a ```tuple``` or ```list``` using the ```set``` class:

```
archive = (1, True, 3.14, 'hello', 'hello', 'bye')
unique = set(archive)
unique
```

![img_175](images/img_175.png)

Notice the ```set``` is enclosed in braces and all duplicates have been removed. This can be seen in the Variable Explorer, the ```set``` ```unique``` has a size smaller than the ```tuple``` ```archive```:

![img_176](images/img_176.png)

By removing duplicates the numeric index has been lost, a ```set``` is unordered and has no index. The values are shown in the Variable Explorer in a random order.

![img_177](images/img_177.png)

Although the fields are greyed out in the Spyder Variable Explorer, a ```set``` is **mutable**. In this case being greyed out indicates that support for mutating a ```set``` via the Variable Explorer is not available. The reason for this is a ```set``` is unordered and therefore it is not possible to index into a ```set``` to select a value or mutate a value. In the case of the ```list```, the Spyder Variable Explorer under the hood used the ```list``` data model method ```__setitem__``` to reassign a value. For a ```set``` it is not possible to modify a value directly in the same manner. It is however possible to discard a value and to add a new value using mutable identifiers.

A ```set``` can be instantiated directly using:

```
unique = {1, 3.14, 'hello', 'bye'}
```

![img_178](images/img_178.png)

A ```set``` with a single value can be created using:

```
unique = {1}
```

![img_204](images/img_204.png)

For an empty ```set```, the ```{}``` cannot be used as they are used to enclose another collection, the ```dict```. Therefore the ```set``` initialization signature must be used directly to create an empty ```set```:

```
dictionary = {}
unique = set()
```

![img_205](images/img_205.png)

![img_206](images/img_206.png)

### Identifiers

Supposing the simple instance is created:

```
unique = {1, 2, 0}
```

![img_179](images/img_179.png)

![img_180](images/img_180.png)

![img_181](images/img_181.png)

If the instance name ```unique``` is input followed by a dot ```.``` and then tab ```↹``` a list of identifiers displays:

![img_182](images/img_182.png)

The ```set``` identifier ```add``` is similar to the list method ```append```. The difference in the name indicates that there is no order in the set. 

![img_187](images/img_187.png)

Note this identifier should not be confused with the data model identifier ```__add__``` which isn't defined for a ```set```.

The element ```3``` can be added using:

```
unique.add(3)
```

This identifier is a method that has no return value:

![img_183](images/img_183.png)

This is a mutatable method and modifies the instance inplace:

![img_184](images/img_184.png)

If the value to be added to the set is already included in the set, it won't be added again as sets can't have duplicates:

```
unique.add(2)
```

![img_185](images/img_185.png)

![img_186](images/img_186.png)

The ```set``` identifier```remove``` operates analogously to the ```list``` counterpart identifier ```remove```. It is also supplemented by ```discard```:

![img_188](images/img_188.png)

![img_189](images/img_189.png)

For example:

```
unique.remove(3)
```

![img_190](images/img_190.png)

![img_191](images/img_191.png)

```
unique.discard(2)
```

![img_192](images/img_192.png)

![img_193](images/img_193.png)

Both identifiers are mutable methods that have no return value and mutate the ``set``` inplace.

The difference between two methods is in error handling; ```remove``` raises an error if a value is not present and ```discard``` is silent:

```
unique.remove(2)
unique.discard(2)
```

![img_194](images/img_194.png)

The ```pop``` identifier does not have the keyword input argument ```index``` because a ```set``` is unordered and will always pop off an arbitary value:

![img_195](images/img_195.png)

```
unique.pop()
```

This identifier is a mutatable method that returns the popped value:

![img_196](images/img_196.png)

And mutates the ```set``` inplace:

![img_197](images/img_197.png)

The set identifier ```copy``` operates analogously to the ```list``` counterpart identifier ```copy``` and performs a shallow copy. A deep copy can be performed using the ```deepcopy``` function from the ```copy``` module:

![img_200](images/img_200.png)

For example the shallow copy ```unique2``` can be made using:

```
unique2 = unique.copy()
```

![img_198](images/img_198.png)

![img_199](images/img_199.png)

The set identifier ```clear``` operates analogously to the ```list``` counterpart identifier  ```clear```. All of the items in the collection are cleared inplace and there is no return value:

![img_201](images/img_201.png)

The original instance ```unique``` can be cleared:

```
unique.clear()
```

![img_202](images/img_202.png)

![img_203](images/img_203.png)

Supposing the four ```set``` instances are created:

```
unique1 = {0, 1, 2, 3, 4, 5, 6, 7, 8}
unique2 = {0, 1, 2}
unique3 = {7, 8, 9}
unique4 = {'a', 'b', 'c'}
```

![img_208](images/img_208.png)

The ```issuperset``` identifier checks whether one ```set``` instance is a superset, that is a ```set``` that contains all the values of another ```set```: 

![img_209](images/img_209.png)

For example ```unique1``` contains all the elements in ```unique2``` and is a superset:

![img_210](images/img_210.png)

```
unique1.issuperset(unique2)
```

![img_211](images/img_211.png)

```unique1``` does not contain all the elements in ```unique3``` and is not a superset:

![img_212](images/img_212.png)

```
unique1.issuperset(unique3)
```

![img_213](images/img_213.png)

The ```issubset``` identifier checks whether one ```set``` instance is a subset, that is a ```set``` which all values are contained with the other ```set``` (superset): 

![img_214](images/img_214.png)

For example ```unique2``` is a subset of ```unique1```:

![img_215](images/img_215.png)

```
unique2.issubset(unique1)
```

![img_216](images/img_216.png)

```unique3``` is not a subset of ```unique1``` as there is a value in ```unique3``` that is not in ```unique1```:

![img_217](images/img_217.png)

```
unique3.issubset(unique1)
```

![img_218](images/img_218.png)

The ```disjoint``` identifiers checks whether one set is disjoint with another, that is two sets which share no values in common:

![img_219](images/img_219.png)

For example ```unique4``` is disjoint from ```unique1``` as they have no overlapping values:

![img_220](images/img_220.png)

```
unique4.isdisjoint(unique1)
```

![img_221](images/img_221.png)

For example ```unique3``` is not disjoint from ```unique1``` as they have overlapping values:

![img_222](images/img_222.png)

```
unique3.isdisjoint(unique1)
```

![img_223](images/img_222.png)

Supposing now:

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}
```

![img_224](images/img_224.png)

The ```union``` identifier makes a superset which contains all unique values of the set the method is called from *self* and the set or iterable the method is applied to *other*. This method has a return value producing a new set:

![img_225](images/img_225.png)

For example the ```union``` between ```unique1``` and ```unique2```:

![img_226](images/img_226.png)

```
unique1.union(unique2)
```

![img_227](images/img_227.png)

If the Variable Explorer is viewed:

![img_228](images/img_228.png)

The ```update``` method can be thought of as *union_update* and behaves similarly to the method ```union```. 

![img_229](images/img_229.png)

```
unique1.update(unique2)
```

The ```set``` method updates the instance *self* in place and there is no return value:

![img_230](images/img_230.png)

![img_231](images/img_231.png)

Returning back to:

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}
```

![img_232](images/img_232.png)

The ```intersection``` identifier returns all unique values which occur both in *self* and *other*. This method has a return value producing a new set:

![img_233](images/img_233.png)

For example the intersection between ```unique1``` and ```unique2```:

![img_234](images/img_234.png)

```
unique1.intersection(unique2)
```

![img_235](images/img_235.png)

The ```intersection_update``` is the mutable method equivalent of ```intersection```:

![img_248](images/img_248.png)

![img_236](images/img_236.png)

```
unique1.intersection_update(unique2)
```

![img_237](images/img_237.png)

![img_238](images/img_238.png)

Returning to:

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}
```

![img_239](images/img_239.png)

The ```difference``` identifier returns all unique values which occur both in *self* that do not occur *other*. This method has a return value producing a new set:

![img_240](images/img_240.png)

For example the difference between ```unique1``` and ```unique2```:

![img_241](images/img_241.png)

```
unique1.difference(unique2)
```

![img_242](images/img_242.png)

The ```difference_update``` is the mutable method equivalent of ```difference``:

![img_249](images/img_249.png)

![img_243](images/img_243.png)

```
unique1.difference_update(unique2)
```

![img_244](images/img_244.png)

![img_245](images/img_245.png)

Returning to:

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}
```

![img_246](images/img_246.png)

The ```symmetric_difference``` identifier returns all unique values which occur both in *self* that do not occur *other* and all the unique values that occur in *other* but do not occur in *self*. This method has a return value producing a new set:

![img_247](images/img_247.png)

For example the symmetric difference between ```unique1``` and ```unique2```:

![img_250](images/img_250.png)

```
unique1.symmetric_difference(unique2)
```

![img_251](images/img_251.png)

The ```symmetric_difference_update``` is the mutable method equivalent of ```symmetric_difference``:

![img_252](images/img_252.png)

![img_253](images/img_253.png)

```
unique1.symmetric_difference_update(unique2)
```

![img_254](images/img_254.png)

![img_255](images/img_255.png)

### Data Model Identifiers

Returning to:

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
```

![img_256](images/img_256.png)

The directory function ```dir``` can be used to look at the data model identifiers available. The ```pprint``` function from the ```pprint``` module can be imported and used to display the as compact:

```
pprint(dir(unique1), compact=True)
```

![img_257](images/img_257.png)

The ```__init__``` data model method is called when instantiating a ```set```:

![img_261](images/img_261.png)

When the new Python object is created, the ```__new__``` data model method is called. This creates the new instance which is given the label or object name and then the initialization signature ```__init__``` is called to initialize the instance data.

The ```type``` class uses the data model identifier ```__class__``` to determine the class an instance belongs to:

```
type(unique1)
```

![img_262](images/img_262.png)

The formal and informal string representation of a ```set``` are given by the ```repr``` function and ```str``` class which use the ```__repr__``` and ```__str__``` data model identifiers respectively:

```
repr(unique1)
str(unique1)
```

![img_258](images/img_258.png)

A set is mutatable, the ```hash``` function which uses the ```__hash__``` data model method:

```
hash(unique1)
```

![img_259](images/img_259.png)

Notice there is no ```__getitem__```, for this reason, the set is unordered and has no index:

![img_260](images/img_260.png)

The ```__len__``` data model is available which means the ```len``` function can be used to determine the number of items in the ```set```:

```
len(unique1)
```

![img_263](images/img_263.png)

The ```__doc__``` data model method is defined, so the help operator ```?``` can be used:

```
? unique1
```

![img_264](images/img_264.png)

The binary data model identifiers are setup to carry out similar operations to the ```set``` identifiers seen above. Most of these carry out a similar functionality to the set identifiers.

There is no ```__mul__``` identifier as it does not make sense to multiply a set to get duplicates because there is no duplicates in a set.

There is no ```__add__``` identifier so the ```+``` operator cannot be used. It does not make sense to have concatenation of two sets, as sets cannot have duplicates. Instead the ```union``` is used.

The ```|``` operator uses the ```__or__``` identifier which carries out similar functionality to the ```union``` identifier (values occur in ```unique1``` or ```unique2```):

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}
```

![img_270](images/img_270.png)

```
unique1 | unique2
```

![img_271](images/img_271.png)

The ```|=``` operator uses the ```__ior__``` identifier which is similar to the ```update``` (*union_update*) identifier. Notice that there is no return value, as the result has been reassigned to ```unique1```:

![img_272](images/img_272.png)

![img_273](images/img_273.png)

![img_274](images/img_274.png)

The ```union``` and ```update``` identifiers  are more powerful and can take a sequence as an input argument, which will be cast into a ```set```. In contrast ```|``` and ```|=``` require two ```set``` instances. 

Notice also the subtle difference when using the mutatable ```update``` method identifier and the ```|=``` operator within a function:

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}

def fun():
    unique1.update(unique2)

fun()

unique1
```

![img_275](images/img_275.png)

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}

def fun():
    unique1 |= unique2

fun()

unique1
```

![img_276](images/img_276.png)

The ```&``` operator uses the ```__and__``` identifier which carries out similar functionality to the ```intersection``` identifier (intersection values occur in ```unique1``` and ```unique2```):

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}
```

![img_277](images/img_277.png)

```
unique1 & unique2
```

![img_278](images/img_278.png)

The ```&=``` operator uses the ```__iand__``` identifier which is similar to the ```intersection_update```  identifier. Notice that there is no return value, as the result has been reassigned to ```unique1```:

![img_279](images/img_279.png)

```
unique1 &= unique2
```

![img_280](images/img_280.png)

![img_281](images/img_281.png)

The ```-``` operator uses the ```__sub__``` identifier which carries out similar functionality to the ```difference``` identifier:

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}
```

![img_265](images/img_265.png)

```
unique1 - unique2
```

![img_266](images/img_266.png)

The ```-=``` operator uses the ```__isub__``` identifier which is similar to the ```difference_update```  identifier. Notice that there is no return value, as the result has been reassigned to ```unique1```:

![img_267](images/img_267.png)

```
unique1 -= unique2
```

![img_268](images/img_268.png)

![img_269](images/img_269.png)

The ```^``` operator uses the ```__xor__``` identifier which carries out similar functionality to the ```symmetric_difference``` identifier (symmetric difference values occur in ```unique1``` exclusive or ```unique2```):

```
unique1 = {0, 1, 2, 3, 4, 5, 6}
unique2 = {4, 5, 6, 7, 8, 9}
```

![img_282](images/img_282.png)

```
unique1 ^ unique2
```

![img_283](images/img_283.png)

The ```^=``` operator uses the ```__ior__``` identifier which is similar to the ```symmetric_difference_update```  identifier. Notice that there is no return value, as the result has been reassigned to ```unique1```:

![img_284](images/img_284.png)

```
unique1 ^= unique2
```

![img_285](images/img_285.png)

![img_286](images/img_286.png)

The equality operators are setup using the logic of subsets and supersets. ```unique1``` is less than ```unique2``` if it is a subset of ```unique1```. ```unique1``` is greater than ```unique1``` if it is a superset of ```unique2```. ```unique1``` is equal to ```unique2``` if all values are the same, otherwise the sets are not equal. The six comparison operators ```==```, ```!=```, ```<```, ```<=```, ```>```, ```>=``` use the data model identifiers ```__eq__```, ```__ne__```, ```__lt__``` and ```__le__```, ```__gt__``` and ```__ge__``` respectively. 

```
unique1 = {0, 1, 2, 3, 4, 5, 6, 7, 8}
unique2 = {0, 1, 2}
unique3 = {7, 8, 9}
unique4 = {'a', 'b', 'c'}

unique1 > unique2
unique2 < unique1
```

![img_287](images/img_287.png)

Notice that ```unique2``` is not greater than, not less than and not equal to ```unique3``` sinnce they are neither supersets or subsets of one another:

```
unique2 > unique3
unique2 < unique3
unique2 == unique3
unique2 != unique3
```

![img_288](images/img_288.png)

## The dict Class

The ```dict``` can be conceptualised as an English dictionary which has a keyword and corresponding definition. In Python a ```dict``` is a mapping of **key**: **value** pairs. 

Each **key** in **keys** has to be unique and **keys** is therefore set-like. For this reason, the ```dict``` shares the use of braces ```{ }``` to enclose the collection. 

The **value** in **values** does not have to be unique and **values** is tuple-like.

The colon ```:``` is used to split each ```key: value``` and the ```,``` is used to split each key, value pair in the mapping.

### The Initialization Signature

Inputting ```dict()``` followed by shift ```⇧``` and tab ```↹``` will display the docstring of the init signature:

![img_289](images/img_289.png)

A ```dict``` is normally  directly using:

```
mapping = {'red': '#FF0000', 
           'green': '#00B050', 
           'blue': '#0070C0'}
```

![img_290](images/img_290.png)

Notice that in the dictionary above, the value of the key is obscure however the key itself is easy to remember. 

The dictionary can be viewed in the Spyder Variable Explorer. Unlike sets which are unordered, dictionaries retain the order items (key: value pairs) were added to them. The mapping displays on the Variable Explorer with the order items were added to it:

![img_291](images/img_291.png)

When expanded however the items are listed by default using the alphabetical (ordinal) order of the keys:

![img_292](images/img_292.png)

An empty mapping can be made using:

```
mapping = {}
```

![img_294](images/img_294.png)

This can be viewed in the Variable Explorer:

![img_295](images/img_295.png)

### Identifiers

Returning to:

```
mapping = {'red': '#FF0000', 
           'green': '#00B050', 
           'blue': '#0070C0'}
```

![img_296](images/img_296.png)

If the instance name ```mapping``` is input followed by a dot ```.``` and then tab ```↹``` a list of identifiers displays:

![img_293](images/img_293.png)

The identifier ```keys``` retrieve the ```keys```:

```
mapping_keys = mapping.keys()
```

![img_299](images/img_299.png)

The ```mapping_keys``` is a set-like object that has the identifier ```isdisjoint``` that behaves identically to the analogous ```isdisjoint``` ```set``` method:

![img_297](images/img_297.png)

![img_298](images/img_298.png)

The ```mapping``` attribute retrieves the ```mapping_proxy``` which is essentially the dictionary:

![img_298](images/img_298.png)

The identifier ```values``` retrieve the ```values```:

```
mapping_values = mapping.values()
```

![img_301](images/img_301.png)

The ```mapping_values``` is a tuple-like object that has the identifier. It only has the identifier ```mapping``` which once again retireves the ```mapping_proxy```:

![img_302](images/img_302.png)

The identifier ```items``` is a set-like object of nested tuples. Each nested tuple has two indexes, the key and value respectively:

```
mapping_items = mapping.items()
```

![img_303](images/img_303.png)

![img_304](images/img_304.png)

These can be cast into lists so their contents can be viewed on the Variable Explorer:

```
mapping_keys = list(mapping_keys)
mapping_values = list(mapping_values)
mapping_items = list(mapping_items)
```

![img_305](images/img_305.png)

![img_306](images/img_306.png)

The method ```get``` can be used to retrieve a value using the key:

![img_307](images/img_307.png)

If the key exists:

![img_308](images/img_308.png)

The corresponding value will be shown:

![img_309](images/img_309.png)

If there is no corresponding value ```None``` will be returned:

![img_310](images/img_310.png)

The method ```setdefault``` behaves similarly to ```get``` when a key exists. Instead of returning ```None``` when the key does not exist, a default key can be set:

![img_311](images/img_311.png)

For example:

![img_312](images/img_312.png)

```
mapping.setdefault('red', '#000000')
mapping.setdefault('yellow', '#000000')
```

![img_313](images/img_313.png)

Notice the new new with the default value is included in the dictionary ```mapping``` which is mutated in place:

![img_314](images/img_314.png)

The ```update``` method can be used to update the value of existing keys or add new key: value pairs that don't already exist in ```mapping``` using another dictionary:

![img_315](images/img_315.png)

![img_316](images/img_316.png)

For example the key ```'yellow'``` exists and the key ```'purple'``` doesn't exist:

```
mapping.update({'yellow': '#FF0000',
               'purple': '#7030A0'})
```               

![img_317](images/img_317.png)

This is a mutable method. Notice that existing items in the dictionary ```mapping``` retain their order within the dictionary and new keys are appended to the end:

![img_318](images/img_318.png)

The dictionary ```pop``` identifier works similarly to the list ```pop``` identifier. As the dictionary does not have a numeric index, a key needs to be supplied instead:

![img_320](images/img_320.png)

```
mapping.pop('red')
```

The value of the popped key is returned:

![img_322](images/img_322.png)

And the dictionary ```mapping``` is mutated in place. Notice the order of all the other keys is maintained:

![img_323](images/img_323.png)

The method ```popitem``` identifier will pop an item from the dictionary, returning it as a tuple:

![img_324](images/img_324.png)

The item to be popped is the last item added:

```
mapping.popitem()
```

This was the key ```'purple'``` and the item ```tuple``` is returned:

![img_325](images/img_325.png)

The dictionary ```mapping``` is mutated in place:

![img_326](images/img_326.png)

The identifier ```copy``` can be used to perform a shallow copy of a dictionary:

![img_327](images/img_327.png)

This copy is returned and the return value can be assigned to a new value ```mapping2```

```
mapping2 = mapping.copy()
```

![img_328](images/img_328.png)

This shallow copy ```mapping2``` displays on the variable explorer:

![img_329](images/img_329.png)

The ```clear``` identifier can now be used on ```mapping``` and ```mapping2``` will be uninfluenced:

![img_330](images/img_330.png)

![img_331](images/img_331.png)

![img_332](images/img_332.png)

A deep copy may be required when the values in a dictionary are mutable. Recall that the keys in a dictionary must be immutable. For example:

```
x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

mapping = {'x': x,
           'y': y}

mapping2 = mapping.copy()
mapping3 = deepcopy(mapping)
```

![img_333](images/img_333.png)

![img_334](images/img_334.png)

The difference in the Variable Explorer can be seen when one of the values in the ```list``` ```x``` is updated:

```
x[1] = 99
```

![img_335](images/img_335.png)

![img_336](images/img_336.png)

```fromkeys``` is a dictionary class method that can be used to create a dictionary from a key of iterables and a constant value:

![img_337](images/img_337.png)

```
keys = ('a', 'b', 'c', 'd', 'e')
value = 0

dict.fromkeys(keys, value)
```

![img_338](images/img_338.png)

The ```zip``` function can be used to zip two equally sized iterables:

![img_339](images/img_339.png)

```
keys = ('a', 'b', 'c', 'd', 'e')
values = (0, 1, 2, 3, 4)
zip(keys, values)
```

![img_340](images/img_340.png)

This creates a zipped object. This can be cast into a list:

```
list(zip(keys, values))
```

![img_341](images/img_341.png)

Notice this is the form of a dictionary items and therefore can alternatively be cast into a dictionary using:

```
dict(zip(keys, values))
```

![img_342](images/img_342.png)

### Data Model Identifiers

Returning to:

```
mapping = {'red': '#FF0000', 
           'green': '#00B050', 
           'blue': '#0070C0'}
```

![img_343](images/img_343.png)

The directory function ```dir``` can be used to look at the data model identifiers available. The ```pprint``` function from the ```pprint``` module can be imported and used to display the as compact:

```
pprint(dir(mapping), compact=True)
```

![img_344](images/img_344.png)

The ```__init__``` data model method is called when instantiating a ```dict```:

![img_345](images/img_345.png)

When the new Python object is created, the ```__new__``` data model method is called. This creates the new instance which then calls the initialization signature ```__init__``` to initialize the instance with instance items.

The ```type``` class uses the data model identifier ```__class__``` to determine the class an instance belongs to:

```
type(mapping)
```

![img_346](images/img_346.png)

The formal and informal string representation of a ```set``` are given by the ```repr``` function and ```str``` class which use the ```__repr__``` and ```__str__``` data model identifiers respectively:

```
repr(mapping)
str(mapping)
```

![img_347](images/img_347.png)

The ```__format__``` data model method is used by formatted strings when formatting a ```dict```. There are no ```dict``` specific format specifications.

The ```len``` function uses the data model identifier ```__len__``` to determine how many items are within the ```dict```:

```
len(mapping)
```

![img_348](images/img_348.png)

![img_349](images/img_349.png)

The ```hash``` function uses the data model identifier ```__hash__```:

```
hash(mapping)
```

Since the ```dict``` is mutable, a ```TypeError```: unhashable type displays:

![img_350](images/img_350.png)

The director function ```dir``` uses the data model identifier ```__dir__``` to display the directory of identifiers as seen earlier.

The ```?``` uses the data model identifiers ```__class__```, ```__str__```, ```__len__``` and ```__doc__``` to generate information about the ```dict``` instance:

```
? mapping
```

![img_351](images/img_351.png)

The ```iter``` function and ```reversed``` function use the ```__iter__``` and ```__reversed__``` data model identifiers to instantiate a forward or reverse iterator from the iterable ```dict```. Notice that the iterator is essentially equivalent to an iterator of the keys: 

```
forward = iter(mapping)
forward
next(forward)
next(forward)
next(forward)
```

![img_352](images/img_352.png)

```
reverse = reversed(mapping)
reverse
next(reverse)
next(reverse)
next(reverse)
```

![img_353](images/img_353.png)

For the reason, the ```in``` operator which uses the data model ```__contains__``` also only works with the keys and not the values of the keys:

![img_354](images/img_354.png)

```
'red' in mapping
'#FF0000' in mapping
```

![img_355](images/img_355.png)

The **mutable** ```dict``` has ```__getitem__```, ```__setitem__``` and ```__delitem__```. For a ```dict```, the keys are used instead of a numeric index:

![img_356](images/img_356.png)

If a key exists, the value will be retrieved:

```
mapping['red']
```

![img_357](images/img_357.png)

If a key does not exist, a ```KeyError``` will display. This behaviour differs from the ```get``` method which will silently return ```None```:

```
mapping['yellow']
```

![img_358](images/img_358.png)

A new item can be created by indexing into the dictionary with a new key and assigning it to a value:

![img_359](images/img_359.png)

```
mapping['yellow'] = '#FFFF00'
```

![img_360](images/img_360.png)

The new item is appended to the end of the dicitonary:

![img_361](images/img_361.png)

An item can be deleted by using the ```del``` keyword and indexing into the dictionary with the key of the item to be deleted:

```
del mapping['red']
```

![img_362](images/img_362.png)

![img_363](images/img_363.png)

The ```|``` operator uses the ```__or__``` data model identifier. There is also the associated reverse ```__ior__```` data model method:

```
mapping1 = {'a': 1, 'c': 3, 'e': 5}
mapping2 = {'b': 20, 'd': 40, 'e': 50}
mapping1 | mapping2
```

Notice that this gives a combined mapping from ```mapping1``` and ```mapping2```. Each item in ```mapping1``` displays in the output, however any key duplicated in ```mapping2``` is updated with the value in ```mapping2```. Then any item not in ```mapping1``` but in ```mapping2``` is appended:

![img_364](images/img_364.png)

The ```|=``` uses the ```__ior__``` data model identifier. This reassigns the value to the instance the inplace assignment or operator is called from:

![img_365](images/img_365.png)

```
mapping1 |= mapping2
```

![img_366](images/img_366.png)

![img_367](images/img_367.png)

The six comparison operators ```==```, ```!=```, ```<```, ```<=```, ```>```, ```>=``` use the data model identifiers ```__eq__```, ```__ne__```, ```__lt__``` and ```__le__```, ```__gt__``` and ```__ge__``` respectively. These behave similarly to sets. Only the is equal to ```==``` and not equal to ```!=``` can be used with dictionaries. A ```TypeError``` displays if another comparison operator is used:

```
mapping1 = {'a': 1, 'b': 2, 'c': 3}
mapping2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
mapping1 == mapping2
mapping1 != mapping2
mapping1 > mapping2
```

![img_368](images/img_368.png)

Notice that the dictionary keys, values and items also have data model identifiers:

```
pprint(dir(mapping), compact=True)
```

![img_369](images/img_369.png)

```
pprint(dir(mapping.keys()), compact=True)
```

![img_370](images/img_370.png)

```
pprint(dir(mapping.values()), compact=True)
```

![img_371](images/img_371.png)

```
pprint(dir(mapping.items()), compact=True)
```

![img_372](images/img_372.png)

All four of these collections have the data model identifiers ```__iter__``` and ```__reversed__``` which means they can be cast into an iterable or into another collection such as a ```tuple``` or ```list``` as seen before. This is important for programming constructs which will be examined in the next tutorial.

These three collections also have the formal ```__repr__``` and informal ```__str__``` data model identifers defined, meaning the ```repr``` and ```str``` functions can be used. Both formal and informal representations are identical:

```
repr(mapping.keys())
repr(mapping.values())
repr(mapping.items())
```

![img_376](images/img_376.png)

Recall that ```keys``` and ```items``` were set-like collections. The comparison operators behave analogously to those in sets:

```
mapping1
mapping2
mapping2.keys() > mapping1.keys()
mapping2.items() > mapping1.items()
```

![img_373](images/img_373.png)

Notice the subtle difference between keys and items when a value is replaced in the subset. The superset is still a superset in terms of keys but not in items as one of the values is different:

```
mapping1['c'] = 300
mapping1
mapping2
mapping2.keys() > mapping1.keys()
mapping2.items() > mapping1.items()
```

![img_374](images/img_374.png)

If an additional item is added to ```mapping1```, that is not in ```mapping2```, ```mapping2``` is no longer regarded as a superset:

```
mapping1['e'] = 500
mapping1
mapping2
mapping2.keys() > mapping1.keys()
mapping2.items() > mapping1.items()
```

![img_375](images/img_375.png)

[Home Python Tutorials](https://github.com/PhilipYip1988/python-tutorials/blob/main/readme.md)
