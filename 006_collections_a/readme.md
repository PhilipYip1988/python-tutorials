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

A tuple is a finite immutate ordered collection of Python objects. 

There is similarities between a Unicode string ```str``` and a ```tuple```. Both are immutable collections, in the case of a ```str```, the individual unit is a Unicode character. In the case of a ```tuple```, each unit is a Python object.



### The Initialization Signature

Inputting ```tuple()``` followed by shift ```⇧``` and tab ```↹``` will display the docstring of the init signature:



It has a single input argument which is an iterable. 

More conventionally the ```tuple``` uses parenthesis ```( )``` to enclose the collection and a comma ```,``` as a delimiter to seperate each individual items. A number of Python objects can be assigned:

```
num1 = 1
num2 = True
num3 = 3.14
word1 = 'hello'
word2 = 'hello'
word3 = 'goodbye'
```



A ```tuple``` of these objects can be created:

```
objects = (num1, num2, num3, word1, word2, word3)
```



Each object can also be placed on a seperate line:

```
objects = (num1, 
           num2, 
           num3, 
           word1, 
           word2, 
           word3)
```



Python objects above can be directly placed into a tuple without privious assignment to individual object names:

```
objects = (1, True, 3.14, 'hello', 'hello', 'bye')
```



In the previous tutorials the parenthesis ```()``` were seen to be used in Python to call a function and enclose any input arguments and for order of precedence in numeric operations (PEDMAS). 

Therefore to create a ```tuple``` with a single item, a ```,``` delimiter must be placed after the single item:

```
pedmas = (1 + 2)
single_object = (1 + 2,)
```



To create an empty ```tuple```, the ```tuple``` class is used:

```
no_object = tuple()
```



### Identifiers

If the instance name ```objects``` is input followed by a dot ```.``` and then tab ```↹``` a list of identifiers displays:



For the ```tuple``` collection only ```index``` and ```count``` display. These have been seen on the ```str```, ```byte``` and ```bytearray``` class and behave similarly:



If ```objects.index()``` followed by shift ```⇧``` and tab ```↹``` is input, the docstring of the method will display:



```
objects.index(1)
```



If ```objects.count()``` followed by shift ```⇧``` and tab ```↹``` is input, the docstring of the method will display:













