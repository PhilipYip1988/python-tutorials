# Fundamental Datatypes

## Object Orientated Programming

Python is an Object Orientated Programming (OOP) language. To conceptualise some of the features of OOP, consider a hypothetical ```Banana``` class. The ```Banana``` class itself can be considered as a blueprint which under the hood contains instructions. These instructions tell Python how to construct a ```banana``` object. 

![img_001](./images/img_001.png)

The class or blueprint instructions outlines the properties of a ```banana``` object, which are in the form of data variables, known as attributes. The class or blueprint instructions also outline the behaviour that a ```banana``` object can exhibit by defining functions that are designed to operate on attributes. Functions contained in a class that operate on instance attributes are known as methods. 

A new banana object is known as an instance of the ```Banana``` class. The initialization signature is a method that has the following form:

```
Banana()
```

The parenthesis are used to call the method and to supply any input arguments. The purpose of the initialization signature is to initialize unique instance variables using the input arguments. For simplicity, the ```Banana``` classes initialization signature has no input arguments:

![img_002](./images/img_002.png)

The code above creates a ```banana``` object. This object has no reference because it was not assigned to an object name during instantiation. As it has no reference it cannot be accessed after it is created and is immediately removed by Pythons garbage collection.

During instantiation, the ```banana``` object created known as an instance is typically assigned to an object name. This is known as assignment and uses the assignment operator ```=``` for example:

```
banana_1 = Banana()
```

![img_003](./images/img_003.png)

Conceptualise the assignment operator as operating from the right to the left. To the right hand side of the assignment operator is the physical object being created. This physical object is assigned to an object name on the left hand side of the assignment operator. The object name can be conceptualised as a label.

The object name acts as a reference to the object. Conceptually the ```banana``` object instance now has an object name, that you and the Python interpretter both know. 

An attribute can be accessed from the ```banana``` object by referencing the objects name, in this case ```banana_1``` followed by a dot ```.``` and then the name of the attribute. For example an attribute of the banana class may be ```color``` and therefore:

```
banana_1.color
```

When the banana is new, the color returned will be ```'yellow'``` as it is fresh. 

![img_003](./images/img_003.png)

This attribute is an example of a class variable. The class variable is common to all ```Banana``` object instances during instantiation and therefore is not supplied in the classes initialization signature. The initial value ```'yellow'``` is instead hardcoded into the ```Banana``` class. Behind the scenes this ```color``` attribute is a data variable and looking up an attribute is just instructing the Python interpretter to look up this attribute without further interaction with the ```banana``` object.

In real life ```banana``` objects go off and if the ```banana``` object is past its sell by date its ```color``` will be ```'brown'```. In Python an action is typically carried out using a function. In this simple example, the action to update the ```color``` attribute can be carried out by a method called ```gone_off```. Notice once again that the method is called using ```( )```. Many methods do not require input arguments as they are acting internally upon the attributes of the object they are called from and therefore do not require additional data in the form of input arguments: 

```
banana.gone_off()
```

![img_004](./images/img_004.png)

In this simple example, the ```gone_off``` method updates the ```color``` attribute from ```'yellow'``` to ```'brown'```. After this method has been invoked, the attribute ```color``` read from the instance ```banana_1``` will be ```'brown'```:

```
banana_1.color
```

Another action carried out with a real banana is to peel the banana. ```banana_1``` can be peeled using the ```peel``` method:

```
banana_1.peel()
```

![img_005](./images/img_005.png)

This method updates any attributes used which are used to represent the shape of the banana. Multiple objects can be constructed from a common class, in the same way that multiple cars can be constructed from a common blueprint. In the case of the ```Banana``` class:

```
banana_2 = Banana()
banana_3 = Banana()
```

![img_006](./images/img_006.png)

![img_007](./images/img_007.png)

Although these objects are constructed from a common class and may have the same attributes:

```
banana_2.color
```

is ```yellow```.

```
banana_3.color
```

is ```yellow```.

They are independent objects. Calling a method on one of these objects will not influence the other. For example using the ```peel``` method on ```banana_3``` will not change anything on ```banana_2```:

```
banana_3.peel()
```

![img_008](./images/img_008.png)

In this case the three banana objects can visually be seen to be different:

![img_005](./images/img_005.png)

![img_006](./images/img_006.png)

![img_008](./images/img_008.png)

To recap, the assignment operator ```=``` is used to assign an object (right hand side of the assignment operator) to an object name (left hand side of the assignment operator). This object name becomes a reference to the object.

The delete keyword ```del``` is used to delete the object name. This should be conceptualised as deleting the label. For example:

![img_005](./images/img_005.png)

```
del banana_1
```

![img_009](./images/img_009.png)

Now because this object has no references, it can no longer be accessed and is removed by Pythons garbage collection.

If an object that exists is assigned to a new object name. For example:

![img_006](./images/img_006.png)

```
fruit_2 = banana_2
```

The right hand side of the assignment operator is first examined. The object name ```banana_2``` is referenced and this reference takes us to the physical banana object. Then the new object name to the left hand side of the assignment operator is assigned to the object. The object now has two object names which can be conceptualised as two labels:

![img_010](./images/img_010.png)

If one of these object names are now deleted. It is the equivalent of removing one of these labels:

```
del banana_2
```

The other object name or label still remains for the object and as the object still has a reference, it can be accessed.

![img_011](./images/img_011.png)

An object is not removed by Pythons garbage collector untill all references to it are deleted.

## The string class

For the text datatype there is the ```str``` class. ```str``` is an abbreviation for a string of characters. The ```str``` class can be conceptualised as an abstract blueprint (written in C). The initialization signature of the ```str``` has some similarities to the hypothetical ```Banana``` class examined earlier:

```
str_1 = str()
```

![img_012](./images/img_012.png)

```
banana_1 = Banana()
```

![img_003](./images/img_003.png)

By convention, inbuilt classes use ```snake_case``` and custom classes use ```PascalCase```. When the initialization signature of the ```str``` class is supplied no input argument, an empty string will be created, that is a string of characters with no characters. 

Another instance can be created with the input argument assigned to ```'hello'```:

```
str_2 = str('hello')
```

![img_013](./images/img_013.png)

Note that text provided in the input argument must be enclosed in quotations, in order for Python to recognise them as belonging to a string of characters. If these are excluded, Python will recognise the text as an object name i.e. as a label to another object and attempt to retrieve that object.

As the ```str``` class is a fundamental datatype in Python, it can also be instantiated shorthand using:

```
str_3 = 'hello'
```

![img_014](./images/img_014.png)

The quotations used to enclose a string can be a set of single quotations ```' '``` (used by default):

```
'hello'
```

Or a set of double quotations ```" "```:

```
"hello"
```

When text is not enclosed in quotations Python looks for an inbuilt object name, or an object that has been assigned by the user.

```
hello
```