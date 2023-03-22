# Custom Classes

## Subclasses

The ```collections``` module has the classes ```UserString```, ```UserList``` and ```UserDict``` which are designed for subclassing. They can be imported using:

```
from collections import UserString, UserList, UserDict
```

![img_001](./images/img_001.png)

The ```UserString``` class can be used directly. Its initialization signature can be accessed by inputting the class name ```UserString()``` and inputting shift ```⇧``` and tab ```↹```:

![img_002](./images/img_002.png)

If ```UserString.``` is input followed by a tab ```↹```, a list of identifiers are available, that are identical to the ```str``` class:

![img_003](./images/img_003.png)

The method resolution order identifier ```mro``` gives the method resolution order:

![img_004](./images/img_004.png)

```
UserString.mro()
```

![img_005](./images/img_005.png)

This is a ```list``` of class names. The top entry is the class itself and the bottom entry is the class ```object``` as every class in Python is ultimately an ```object```. The ```abc``` stands for abstract base classes. An abstract base class is not used directly but are used as parent classes. The name of these abstract base classes gives some of the properties of a ```UserString``` which recall is equivalent to the ```str``` class, i.e. that it has a container, is iterable, has a size, is a collection, is reversible and is a sequence.

```
UserList.mro()
```

![img_006](./images/img_006.png)

If the ```mro``` of the ```UserList``` class is examined which recall is equivalent to the ```list``` class, the same abstract base classes show, in addition to ```MutableSequence``` which makes sense as a ```list``` has all of these properties in common with a ```str``` but is mutable.

```
UserDict.mro()
```

![img_007](./images/img_007.png)

If the ```mro``` of the ```UserDict``` class is examined which recall is equivalent to the ```dict``` class, many of the same abstract base classes show, the ```dict``` is not a sequence i.e. has no numeric index, instead it has a mapping and is a mutable mapping.

An instance of ```UserString``` can be created using:

```
greeting = UserString('hello')
```

And any of the methods available for a string can be used:

```
greeting.upper()
```

Notice that all the mutable methods have a return value, in this case returning a new ```UserString``` instance:

```
greeting = UserString('hello')
greeting.upper()
type(greeting.upper())
```

![img_008](./images/img_008.png)

Let's create a subclass with one additional method:

```
class CustomString(UserString):
    def plural(self):
        return self + 's'
```

The ```class``` keyword is used:

![img_009](./images/img_009.png)

Followed by the class name which is in ```CamelCase```. ```CamelCase``` is used for all third-party classes:

![img_010](./images/img_010.png)

The parenthesis contains the parent classes which are also known as the superclasses:

![img_011](./images/img_011.png)

The colon ```:``` indicates the beginning fo a code block. all additional methods are nested within this code block:

![img_012](./images/img_012.png)

A method is very similar to a function. It always has ```self``` as the first input argument:

![img_013](./images/img_013.png)

```self``` is the conventional term and essentially means *this instance*.

The method is immutable and therefore has a return value, in this case using the ```+``` operator. The ```__add__``` data model method is defined in the parent class ```UserString``` so concatenation can be used:

![img_014](./images/img_014.png)

The method resolution order of ```CustomString``` can now be examined:

```
CustomString.mro()
```

The list has ```CustomString``` at the top followed by all the entries which came from the parent class ```UserString```:

![img_015](./images/img_015.png)

An instance can be created:

```
greeting = CustomString('hello')
```

![img_016](./images/img_016.png)

If ```CustomClass.``` is input followed by a tab ```↹```, the list of identifiers displays, note the inclusion of the identifier ```plural```:

![img_017](./images/img_017.png)

If its docstring is examined by inputting ```CustomClass.plural()``` followed by shift ```⇧``` and tab ```↹```, it requires the input argument ```self```. Recall that ```self``` can be thought of as meaning *this instance*. In this particular instance, the instance name is ```greeting```: 

![img_018](./images/img_018.png)

```
CustomString.plural(greeting)
```

![img_019](./images/img_019.png)

Supplying ```self``` means the method has access to the instance data which is the text ```'hello'```. The output returns the new ```UserString``` ```'hellos'```.

It is more common to call the method from the instance. If ```greeting.``` is input followed by a tab ```↹```, the list of identifiers displays, note the inclusion of the identifier ```plural```:

![img_020](./images/img_020.png)

If its docstring is examined by inputting ```greeting.plural()``` followed by shift ```⇧``` and tab ```↹```. Notice omission of the input argument ```self```. Since the method is being called from *this instance* ```greeting```, ````self``` is already implied:

![img_021](./images/img_021.png)

```
self.plural()
```

![img_022](./images/img_022.png)

Implicitly supplying ```self``` by accessing the method from the instance, means the method has access to the instance data which is the text ```'hello'```. The output once again returns the new ```UserString``` ```'hellos'```.

The ```type``` of the instance and the return value from this method call can be checked using:

```
type(greeting)
type(greeting.plural())
```

![img_023](./images/img_023.png)

In both cases they are ```CustomString``` instances as expected.

The following class can be defined with two additional methods:

```
class CustomString(UserString):
    def plural(self):
        return self + 's'
    
    def custom_upper(self):
        print('From class:')
        return self.upper()
    
    def custom_super_upper(self):
        print('From superclass:')
        return super().upper()


```

The method ```custom_upper``` calls the existing method ```upper``` from *this instance* ```self``` i.e. calling the method from the same class ```CustomString```:

![img_024](./images/img_024.png)

The method ```custom_super_upper``` calls the existing method ```upper``` from *this instance of the superclass* i.e. calling the method as defined in the parent class ```UserString```:

![img_025](./images/img_025.png)

Sometimes the above is more explicitly written as:

```
class CustomString(UserString):
    def plural(self):
        return self + 's'
    
    def custom_upper(self):
        print('From class:')
        return self.upper()
    
    def custom_super_upper(self):
        print('From superclass:')
        print(f'{super(CustomString, self)}')
        return super(CustomString, self).upper()


```

![img_026](./images/img_026.png)

```super(CustomString, self)``` looks at the superclass of ```CustomString``` which is ```UserString``` and provides the parent class the parameter ```self```. Recall ```self``` was previously conceptualised as *this instance*. In the context of a superclass *self* can mean this *instance* or any *equivalent parent class instance*.

```super(CustomString, self)``` means *equivalent parent instance* and a method called from ```super(CustomString, self)``` is being called from an equivalent instance of the parent class. 

Usually the parent class and ```self``` are implicitly implied. Taken from the first positional argument supplied during the class definition and the first positional input argument from the method respectively:

![img_027](./images/img_027.png)

```greeting``` can once again be instantiated:

```
greeting = CustomString('hello')
```

![img_028](./images/img_028.png)

These methods can be compared:

```
greeting.upper()
```

![img_029](./images/img_029.png)

```self``` means *this instance* and in this case the instance name is ```greeting``` which is assigned to the value ```'hello'``` which is printed:

```
greeting.custom_upper()
```

![img_030](./images/img_030.png)

The superclass is being provided the name of the child class alongside an object or instance of the child class:

```
greeting.custom_super_upper()
```

![img_031](./images/img_031.png)

In all the cases above a new instance of ```CustomString``` is returned:

```
type(greeting.upper())
type(greeting.custom_upper())
type(greeting.custom_super_upper())
```

![img_032](./images/img_032.png)

Calling a method from an equivalent instance of the parent class allows slight modification of the equivalent method name in the child class. For example a simple print statement can be added. The class can be created with the ```upper``` method defined:

```
class CustomString(UserString):
    def plural(self):
        return self + 's'
    
    def upper(self):
        print('Shouting:')
        return super().upper()
    
```

![img_033](./images/img_033.png)

```greeting``` can once again be instantiated:

```
greeting = CustomString('hello')
```

And the modified method called:

```
greeting.upper()
```

![img_034](./images/img_034.png)

The method resolution order can be examined:

```
CustomString.mro()
```

![img_035](./images/img_035.png)

The method ```upper``` is now defined in two places and this class ```CustomString``` will preference the definition closer towards the top of the method resolution order list i.e. the definition in ```CustomString```. In this case, the definition in ```CustomString``` uses the definition in ```UserString``` and builds upon it.

... mutable method ...


```
import collections.abc
import numbers
```





