# Classes

## Datamodel Identifiers

In the previous tutorials, methods and attributes were examined for the string, integer, floating point, boolean, list, tuple, set and dictionary classes. If the ```dir``` function is used on a class or any instance of a class, additional datamodel identifiers displayed. These datamodel identifiers are not typically used directly and were observed to map to inbuilt Python functions or operators.


|datamodel identifier|purpose, function or operator|
|---|---|
|\_\_new\_\_(cls)|constructor creates a new instance|
|\_\_init\_\_(self, a, b)|initializer creates instance variables self.a and self.b|
|\_\_getattribute(self)\_\_|self.attr|
|\_\_setattr(self, value)\_\_|self.attr = value|
|\_\_delattr(self)\_\_|del self.attr|
|\_\_class\_\_(self)|type(self)|
|\_\_dir\_\_(self)|dir(self)|
|\_\_doc\_\_|? cls or ? self|
|\_\_repr\_\_(self)|repr(self)|
|\_\_str\_\_(self)|str(self)|
|\_\_int\_\_(self)|int(self)|
|\_\_float\_\_(self)|float(self)|
|\_\_sizeof(self)\_\_|sys.getsize(self)|
|\_\_hash(self)\_\_|hash(self)|


```__new__``` is a class method and returns a new instance of a class. The ```__new__``` method normally calls the ```__init__``` method which is used to initialize instance variables. ```__doc__``` is a class attribute which can be accessed from the class and any instance of the class.

For a collection, the typical datamodel methods were observed.

|datamodel method|function or operator|
|---|---|
|\_\_len\_\_(self)|len(self)|
|\_\_getitem\_\_(self, key)|self[key]|
|\_\_setitem\_\_(self, key, value)|self[key]=value|
|\_\_add\_\_(self, other)|self + other|
|\_\_mul\_\_(self, other)|self * other|
|\_\_iter\_\_(self)|iter(self)|
|\_\_reversed\_\_(self)|reversed(self)|

A collection can store multiple values and has a length.

A string, list and tuple are ordered collections with numeric keys known as indexes. In a dictionary which is an unordered collection the key is typically a string. A set is an unordered collection without a key.

In a collection the ```+``` operator is setup for concatenation and the ```*``` operator is setup to perform collection replication using an integer.

The ```__iter__``` method converts the iterable object into an iterator which is used when looping over a collection. When using the classes ```list```, ```tuple``` and ```dict``` to cast from one collection to another, the iterator can be thought of as an intermediate. For example:

```
d1 = {"a": 1, "b": 2, "c": 3}
l1 = list(d1)
```

```
d1 = {"a": 1, "b": 2, "c": 3}
i1 = iter(d1)
l1 = list(i1)
```

For a number, the typical datamodel methods were observed.

|datamodel method|function or operator|
|---|---|
|\_\_add\_\_(self, other)|self + other|
|\_\_pos\_\_(self|+self|
|\_\_sub\_\_(self, other)|self - other|
|\_\_neg\_\_(self)|-self|
|\_\_mul\_\_(self, other)|self * other|
|\_\_exp\_\_(self, other)|self ** other|
|\_\_floordiv\_\_(self, other)|self // other|
|\_\_mod\_\_(self, other)|self % other|
|\_\_truediv\_\_(self, other)|self / other|
|\_\_abs\_\_(self)|abs(self)|
|\_\_ceil\_\_(self)|ceil(self)|
|\_\_round\_\_(self)|round(self)|
|\_\_and\_\_(self, other)|self | other|
|\_\_or\_\_(self, other)|self & other|
|\_\_xor\_\_(self, other)|self ^ other|
|\_\_eq\_\_(self, other)|self == other|
|\_\_ne\_\_(self, other)|self != other|
|\_\_gt\_\_(self, other)|self > other|
|\_\_ge\_\_(self, other)|self >= other|
|\_\_lt\_\_(self, other)|self < other|
|\_\_le\_\_(self, other)|self <= other|
|\_\_lshift\_\_(self, other)|self << other|
|\_\_rshift\_\_(self, other)|self >> other|
|\_\_invert\_\_(self)|~self|

If the following integer instances are created:

```
num1 = 1
num2 = 2
```

The datamodel method ```__sub__``` will perform subtraction:

```
num1.__sub__(num2)
```

Where ```num1``` is the instance known as self (the instance the operation is being carried out from) and ```num2``` is known as other (the other instance involved in the interaction).

The above operation is more commonly done using the ```-``` operator which is the operator the ```__sub__``` method maps to:

```
num1 - num2
```

Some of the methods are prefixed with a ```r```` which stands for reverse. The reverse method carries out the operation from other opposed to self. The reverse operations are not too commonly used:

```
num1.__rsub__(num2)
```

```
num2 - num1
```

Some of the methods above are prefixed with an ```i```. The ```i``` stands for inplace and is shorthand notation for an operation involving a reassignment. For example:

```
num1 = num1 - num2
```

is shortened to:

```
num1 -= num2
```

## The object class

If ```object()``` is input followed by a shift ```⇧``` and tab ```↹``` the docstring for the intializer displays.



Notice that every inbuilt class is listed as a subclass. A subclass is a modified copy of a class and in Python everythng is a modified copy of an object, either directly or indirectly.

An instance of an object can be created using:

```
obj1 = object()
obj2 = object()
```

When ```obj.``` is input followed by a tab ```↹``` no identifier displays because no custom identifier has been defined in the ```object``` class:



However when the ```dir``` function is used, the following datamodel identifiers display:

```
dir(obj1)
```



In Python an ```object``` has inherent functionality and recognises the name of all the datamodel idenifiers that map to inbuilt functions and operators.

The ones listed in the directory above are defined. ```__dir__``` for example is defined, which is why the ```dir``` function worked on the instance of the ```object``` class. ```__repr__``` is also defined so the ```repr``` function will also work.

```
repr(obj1)
repr(obj2)
```



The ```__eq__``` datamodel method is also defined so the is equal to operator ```==``` can be used:

```
obj1 == obj2
```


These are two different objects so are not equal to one another.

```
obj1 == obj1
```


The ```+``` operatorand whennd looks for the corresponding ```__add__``` datamodel method within the ```object``` class which is not defined so a ```TypeError``` displays.

```
obj1 + obj2
```



## Class Names CamelCaseCapitalization

The ```class``` keyword is used to create a new class. This is followed by the class name. For the class name ```CamelCaseCapitalization``` is typically used and this differenciates custom classes from inbuilt classes. The class name is followed by parenthesis and the parenthesis enclose the parent class. By default a child class will inherit all the properties of the parent class, unless they are redefined. If no parent class is given, the parent class will automatically be assumed to be an object. After the parenthesis a colon ```:``` is present indicating the beginning of a code block. This code block normally contains several functions which each have their own perspective code blocks.

A custom class called ```ModObj``` can be created.  for class names.

```
class ModObj(object):
    pass



```

This class ```ModObj``` has been given no additional functionality to the parent ```object``` class. So creating the following instances and using ```repr``` and the is equal to ```==``` operator yields very similar results:

```
mobj1 = ModObj()
mobj2 = ModObj()
repr(mobj1)
repr(mobj2)
mobj1 == mobj2
```

Conceptually a class can be thought of as a collection of functions.

```
class ModObj(object):
    def fun1():
        return None
    def fun2():
        return None
    def fun3():
        return None
    def fun4():
        return None
```

Recall that functions used from an instance of a class are normally designed to interact with the instance it*self*. For example the string methods called from a string instance are designed to interact with the unique text in the string instance. Therefore, they need to be able to read and work on the instance data in some capacity. In order for them to act upon an instance, the first positional input argument must be ```self```.

```
class ModObj(object):
    def fun1(self):
        return None
    def fun2(self):
        return None
    def fun3(self):
        return None
    def fun4(self):
        return None
```

An instance can be created:

```
mobj1 = ModObj()
```

Notice that when ```mobj1.``` is input followed by a tab ```↹``` the four additional identifiers display:




The docstring of the first one of these can be viewed by inputting ```mobj1.fun1()``` followed by a dot ```.``` and tab ```↹```. Notice that in the empty docstring ```self``` is not mentioned because it is implicitly implied. As the method is being called from ```mobj1```, ```self``` is implied to be ```mobj1```. 



So this method can be called using:

```
mobj1.fun1()
```

This method does nothing but return ```None```.



If on the otherhand the class ```ModObj``` is input followed by a tab ```↹``` the four additional identifiers display. The docstring of the first one of these can be viewed by inputting ```ModObj.fun1()``` followed by a dot ```.``` and tab ```↹```. Notice that in the empty docstring ```self``` is mentioned because it is being called from the class itself and has no instance data. An instance needs to be explicitly implied.



So this method can be called and applied to the instance ```mobj1``` using:

```
ModOb.fun1(mobj1)
```



An attribute is a variable created within a class:

```
class ModObj(object):
    var1 = "value1"
    var2 = "value2"
```

Once again two instances can be created:

```
mobj1 = ModObj()
mobj2 = ModObj()
```

Notice that when ```mobj1.``` is input followed by a tab ```↹``` the two identifiers display:



The values of these attributes can be accessed from the instance using:

```
mobj1.var1
mobj1.var2
```

```
mobj2.var1
mobj2.var2
```

If the class ```ModObj``` is input followed by a tab ```↹``` the two identifiers display.



```
ModObj.var1
ModObj.var2
```



These variables are class variables and are the same for the class and every instance of the class. This is useful for something like a docstring which is written once and doesn't need to be rewritten for every variable.






defined for all of these datamodel identifiers.


























|\_\_format\_\_(self, specification)|format specification when used with formatted string specifier|
|\_\_index\_\_(self)|used to cast object as int for indexing|




 '__getnewargs__',
 '__init_subclass__',
'__reduce__',
 '__reduce_ex__',
'__subclasshook__'

