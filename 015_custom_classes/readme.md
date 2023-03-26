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

Let's create a ```list``` based subclass with one additional mutable method. Note that the mutable method has no return value as it mutates the list in place:

```
class CustomList(UserList):
    def append_hello(self):
        self.append('hello')


```

![img_036](./images/img_036.png)

A new instance can be created using:

```
active = CustomList()
```

![img_037](./images/img_037.png)

The list of identifiers can be viewed by inputting ```active.``` followed by a tab ```↹```:

![img_038](./images/img_038.png)

Inputting ```active.append_hello()``` followed by a shift ```⇧``` and tab ```↹``` shows the docstring:

![img_039](./images/img_039.png)

This method has no input arguments and can be called using:

```
active.append_hello()
```

![img_040](./images/img_040.png)

Notice that calling this mutable method displays no output in the cell as it has no return statement. If the instance:

```
active
```

is examined, the value ```'hello'``` is appended:

![img_041](./images/img_041.png)

Another method ```appendleft``` which behaves equivalently to its coutnerpart in the ```deque``` collection can be made using the ```list``` method ```insert```. If the docstring is viewed by typing in ````active.insert()``` followed by a shift ```⇧``` and tab ```↹```, this method has two input arguments ```index``` and ```value```:

![img_042](./images/img_042.png)

For the ```appendleft``` method, the ```index``` is going to be locked to ```0``` however a single input argument ```value``` will need to be provided:

```
class CustomList(UserList):
    def appendleft(self, value):
        """Add an element to the left side of the CustomList"""
        self.insert(0, value)


```

![img_043](./images/img_043.png)

Now an instance can be created:

```
active = CustomList(('a', 'b', 'c'))
```

![img_044](./images/img_044.png)

The list of identifiers can be viewed by inputting ```active.``` followed by a tab ```↹```:

![img_045](./images/img_045.png)

The docstring for the identifier ```appendleft``` can be viewed by inputting ```active.appendleft()``` followed by a shift ```⇧``` and tab ```↹``` and requests the input argument ```value```:

![img_046](./images/img_046.png)

The ```active``` instance of ```CustomList``` can be examined:

```
active
```

Then the method ```appendleft``` can be used:

```
active.appendleft('hello')
```

This method is mutable so has no return value. The ```active``` instance of ```CustomList``` can be examined again using:

```
active
```

The value ```'hello'``` is appended as expected:

![img_047](./images/img_047.png)

Other methods found in the ```deque``` could be made such as ```extendleft``` and ```popleft```:

```
class CustomList(UserList):
    def appendleft(self, value):
        """Add an element to the left side of the CustomList"""
        self.insert(0, value)
        
    def popleft(self):
        """Remove and return the leftmost element."""
        return self.pop(0) # pop has a return value
        
    def extendleft(self, seq):
        """Extend the left side of the CustomList with elements from the iterable"""
        for item in seq:
            self.appendleft(item)


```

![img_048](./images/img_048.png)

These can be tested using:

```
active = CustomList([1, 2, 3])
active
active.popleft()
active
active.extendleft(('a', 'b', 'c'))
active
```

![img_049](./images/img_049.png)

Notice the cell output:

```
active
```

This differs from:

```
repr(active)
str(active)
```

![img_050](./images/img_050.png)

Normally the formal string representation shows how to instantiate a new instance. To change this the data model method ```__repr__``` needs to be defined:

```
class CustomList(UserList):
    def __repr__(self):
        string = super().__repr__()
        updatedstring = f'CustomList({string})'
        return updatedstring

    def appendleft(self, value):
        """Add an element to the left side of the CustomList"""
        self.insert(0, value)
        
    def popleft(self):
        """Remove and return the leftmost element."""
        return self.pop(0) # pop has a return value
        
    def extendleft(self, seq):
        """Extend the left side of the CustomList with elements from the iterable"""
        for item in seq:
            self.appendleft(item)


```

![img_051](./images/img_051.png)

This can be tested with:

```
active = CustomList((1, 2, 3))
active
repr(active)
active2 = CustomList(('a', 'b', 'c'))
active2
repr(active2)
str(active2)
```

![img_052](./images/img_052.png)

Notice the informal string has the same format as the formal string, this is the default case when ```__repr__``` is defined and ```__str__``` is not defined. For clarity ```__str__``` can be defined to something different:

```
class CustomList(UserList):
    def __repr__(self):
        string = super().__repr__()
        updatedstring = f'CustomList({string})'
        return updatedstring

    def __str__(self):
        string = super().__repr__()
        return string    
    
    def appendleft(self, value):
        """Add an element to the left side of the CustomList"""
        self.insert(0, value)
        
    def popleft(self):
        """Remove and return the leftmost element."""
        return self.pop(0) # pop has a return value
        
    def extendleft(self, seq):
        """Extend the left side of the CustomList with elements from the iterable"""
        for item in seq:
            self.appendleft(item)


```

![img_053](./images/img_053.png)

This can be tested with:

```
active2 = CustomList(('a', 'b', 'c'))
active2
repr(active2)
str(active2)
```

![img_054](./images/img_054.png)

If the method resolution order of the ```builtins``` objects are compared to their counterparts in the ```collections``` module:

```
str.mro()
UserString.mro()
```

![img_055](./images/img_055.png)

Notice that the ```UserString``` has a much larger number of abstract base classes. Inclusion of the abstract base classes is a design pattern, that makes it easier for another Python programmer to identify what data model methods to expect in a third-party class. Looking at only the abstract base classes from bottom to top, the following relationship can be outlined:

|Abstract<br />Class|Abstract<br />Parent<br />Class|Abstract<br />Data<br />Model<br />Methods|Inherited<br />Data<br />Model<br />Methods|Abstract<br />Methods|Inherited<br />Abstract<br />Methods|
|---|---|---|---|---|---|
|Container||\_\_contains\_\_||||
|Iterable||\_\_iter\_\_||||
|Sized||\_\_len\_\_||||
|Collection|Container <br /> Iterable <br /> Sized||\_\_contains\_\_ <br /> \_\_iter\_\_ <br /> \_\_len\_\_|||
|Reversible|Iterable|\_\_reversed\_\_|\_\_iter\_\_|||
|Sequence|Reversible <br /> Collection|\_\_getitem\_\_|\_\_contains\_\_ <br /> \_\_iter\_\_ <br /> \_\_len\_\_ <br /> \_\_reversed\_\_|count <br /> index||

A ```Collection``` for example inherits everything from ```Container```, ```Iterable``` and ```Sized```.

A ```str``` is a ```Sequence``` and has all the immutable ```Sequence``` methods shown in the table above. 

A ```tuple``` is also a ```Sequence``` and has all the immutable ```Sequence``` methods shown in the table above which behave equivalently. i.e. the ```str``` and ```tuple``` classes behave consistently when it comes to indexing, slicing and looping over for example:

```
list.mro()
UserList.mro()
```

![img_056](./images/img_056.png)

Notice that the ```UserList``` once again has a much larger number of abstract base classes. Most of these are the same however there is the inclusion of ```MutableSequence```:

|Abstract<br />Class|Abstract<br />Parent<br />Class|Abstract<br />Data<br />Model<br />Methods|Inherited<br />Data<br />Model<br />Methods|Abstract<br />Methods|Inherited<br />Abstract<br />Methods|
|---|---|---|---|---|---|
|Container||\_\_contains\_\_||||
|Iterable||\_\_iter\_\_||||
|Sized||\_\_len\_\_||||
|Collection|Container <br /> Iterable <br /> Sized||\_\_contains\_\_ <br /> \_\_iter\_\_ <br /> \_\_len\_\_|||
|Reversible|Iterable|\_\_reversed\_\_|\_\_iter\_\_|||
|Sequence|Reversible <br /> Collection|\_\_getitem\_\_|\_\_contains\_\_ <br /> \_\_iter\_\_ <br /> \_\_len\_\_ <br /> \_\_reversed\_\_|count <br /> index||
|MutableSequence|Sequence|\_\_iadd\_\_ <br /> \_\_setitem\_\_ <br /> \_\_delitem\_\_|\_\_contains\_\_ <br /> \_\_getitem\_\_ <br /> \_\_iter\_\_ <br /> \_\_len\_\_ <br /> \_\_reversed\_\_|append <br /> extend <br /> insert <br /> pop <br /> remove <br /> reverse|count <br /> index|

A ```list``` is a ```MutableSequence``` and inherits all the immutable methods from the ```Sequence```, therefore as seen previously equivalent methods between a ```tuple``` and a ```list``` behave identically. The ```list``` also has all the mutable ```MutableSequence``` methods shown in the table above.

```
dict.mro()
UserDict.mro()
```

![img_057](./images/img_057.png)

Notice that the ```UserDict``` once again has a much larger number of abstract base classes:

|Abstract<br />Class|Abstract<br />Parent<br />Class|Abstract<br />Data<br />Model<br />Methods|Inherited<br />Data<br />Model<br />Methods|Abstract<br />Methods|Inherited<br />Abstract<br />Methods|
|---|---|---|---|---|---|
|Container||\_\_contains\_\_||||
|Iterable||\_\_iter\_\_||||
|Sized||\_\_len\_\_||||
|Collection|Container <br /> Iterable <br /> Sized||\_\_contains\_\_ <br /> \_\_iter\_\_ <br /> \_\_len\_\_|||
|Mapping|Collection|\_\_getitem\_\_|\_\_contains\_\_ <br /> \_\_eq\_\_ <br /> \_\_iter\_\_ <br /> \_\_len\_\_ <br /> \_\_ne\_\_ <br />|get<br />  items<br />  keys<br />  values||
|MutableMapping|Mapping|\_\_delitem\_\_ <br />  \_\_setitem\_\_|\_\_contains\_\_ <br /> \_\_eq\_\_ <br /> \_\_getitem\_\_  <br />\_\_iter\_\_ <br /> \_\_len\_\_ <br /> \_\_ne\_\_ <br />|clear <br /> pop <br />  popitem <br /> setdefault <br />  update|get<br />  items<br />  keys<br />  values|

The ```dict``` is not a ```Mapping```. Notice that both the ```Sequence``` and ```Mapping``` inherit from the ```Collection``` which is why there is some consistent behaviour between a ```dict``` and a ```tuple``` for example. A ```Sequence``` has a numeric index, whereas a ```Mapping``` has keys, both of these use the ```__getitem__``` data model method but it is defined differently.

Sticking to the design patterns above makes it easier for another Python programmer to use the third-party class.

## Property

So far subclassing using the UserClasses of the ```collections``` module has been examined. This has typically involved the addition or modification of methods which act on instance data. Let's create an ```XVariable``` class which directly subclasses from ```object```, recall everything in Python is ultimately an ```object```. 

Three methods will be created for a variable ```x```, an associated ```get_x```, ```set_x``` and ```del_x``` method:

```
class XVariable(object):

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def del_x(self):
        self.x = None


```

![img_058](./images/img_058.png)

Notice that ```get_x``` returns a value and does not modify the instance, whereas ```set_x``` and ```del_x``` directly mutate the instance and have no return statement.

The default Initialization Signature inherited from the parent class ```object``` can be examined by inputting ```XVariable()``` and pressing shift ```⇧``` and tab ```↹```:

![img_059](./images/img_059.png)

An instance can be created using:

```
x1 = XVariable()
```

![img_060](./images/img_060.png)

The identifiers can be viewed by inputting ```x1.``` and pressing tab ```↹```:

![img_061](./images/img_061.png)

Notice the three identifiers ```get_x```, ```set_x``` and ```del_x``` show but there is no variable ```x``` itself. If the ```get_x``` is attempted to be called an ```AttributeError``` displays:

```
x1.get_x()
```

![img_062](./images/img_062.png)

If ```x``` is set:

```
x1.set_x(3)
```

![img_063](./images/img_063.png)

The identifiers can be viewed once again by inputting ```x1.``` and pressing tab ```↹```:

![img_064](./images/img_064.png)

Now the attribute ```x``` displays. Its value can be viewed by the ```get_x``` method, it can also be deleted using the ```del_x``` method. Since deleting is designed to return ```None``` instead of removing the attribute, the method ```get_x``` can be used after deletion:

```
x1.get_x()
x1.del_x()
x1.get_x()
```

![img_065](./images/img_065.png)

More conventionally an attribute can be set using:

```
x1.x = 4
```

It can be get using:

```
x1.x
```

And it can be del using:

```
del x1.x
```

![img_066](./images/img_066.png)

Once deleted it cannot be accessed, giving an ```AttributeError``` if attempting to do so:

```
x1.x
```

![img_067](./images/img_067.png)

Supposing, the attribute is supposed to only be interacted with using the three methods ```get_x```, ```set_x``` and ```del_x```, it can be prefixed with an underscore. 

Prefixing a variable with a single underscore, indicates the attribute is designed to only be accessed internally (within the class itself).

```
class XVariable(object):

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def del_x(self):
        self._x = None


```

And not outwith the class for example from an instance:

```
x1 = XVariable()
x1.set_x(4)
```

![img_068](./images/img_068.png)

The identifiers can be viewed once again by inputting ```x1.``` and pressing tab ```↹```:

![img_069](./images/img_069.png)

Notice the private attribute ```_x``` does not show and it is therefore more obvious to use the ```get_x``` method:

```
x1.get_x()
```

![img_070](./images/img_070.png)

```
from pprint import pprint
pprint(dir(x1), compact=True)
```

![img_071](./images/img_071.png)

It becomes rather cumbersome to have three methods for each attribute displaying in the list of identifiers. Instead a property is typically configured. The function names ```get_x```, ```set_x``` and ```del_x``` are all renamed ```x```. The getter has the decorator ```@property```, the setter has the decorator ```@x.setter``` and the deleter has the decorator ```@x.deleter```:

```
class XVariable(object):

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @x.deleter
    def x(self):
        self._x = None


```

![img_072](./images/img_072.png)

Now when the instance ```x1``` is instantiated. The attribute ```x``` can be get, set and deleted using Pythons standard syntax. Notice when it is accessed again after deletion, ```None``` is returned opposed to the ```AttributeError``` meaning the custom deleter method is invoked:

```
x1 = XVariable()
x1.x = 4
del x1.x
x1.x
```

If the directory of the instance ```x1``` is examined, there is the property attribute ```x``` and the private attribute ```_x```. The user should only interact with ```x``` as the getter, setter and deleter are configured as desired:

```
from pprint import pprint
pprint(dir(x1), compact=True)
```

![img_073](./images/img_073.png)

If a second instance is created, although ```x``` is recognised as an identifier, when it is attempted to be accessed without prior assignment an ```AttributeError``` displays:

```
x2 = XVariable()
x2.x
```

![img_074](./images/img_074.png)

The purpose of an Initialization Signature is to initialize instance attributes, during instantiation. This is done using the data model method ```__init__```. 

```
class XVariable(object):

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = None

    def __init__(self, value):
        self.x = value
    

```

![img_075](./images/img_075.png)

Notice that this assigns the ```value``` supplied as an input argument to the attribute ```x```. Assignment of a value to the attribute ```x``` invokes the setter method for ```x```. 

Note that the ```__init__``` signature only initializes instance attributes and has **no** return statement. When ```XVariable()``` is input followed by a shift ```⇧``` and tab ```↹```, the docstring of the initialization signature i.e. the ```__init__``` method displays. All the input arguments required for this method need to be supplied:

![img_076](./images/img_076.png)

Although the docstring of the initialization signature displayed above. Instantiation actually uses another data model method ```__new__```. The ```__new__``` data model method creates a new instance, then calls the ```__init__``` method to initialize instance attributes and then finally has a return value which returns the new instance:

```
XVariable(4)
```

![img_077](./images/img_077.png)

This effect of ```__new__``` can be seen by the return value shown in the cell output above, recall ```__init__``` has no return value and if ```__init__``` was instead invoked there would be no instance:

```
x1 = XVariable(4)
x1.x
```

![img_078](./images/img_078.png)

## Abstract Base Class

An Abstract Base Class (ABC) is a design pattern that is used to create an abstract template for a class. For example, the following outline can be made for a coordinate:

```
from abc import ABC, abstractmethod

class AbstractCoordinate(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @property    
    @abstractmethod
    def x(self):
        pass

    @property    
    @abstractmethod
    def y(self):
        pass


```

![img_079](./images/img_079.png)

The docstring can be viewed by inputting ```AbstractCoordinate()``` and pressing shift ```⇧``` and tab ```↹```:

![img_080](./images/img_080.png)

This template is not designed to be instantiated directly and a ```TypeError``` displays if this is attempted:

```
AbstractCoordinate()
```

![img_081](./images/img_081.png)

A class can be made that uses ```AbstractCoordinate``` as a base class. All of the methods that have the decorator ```@abstractmethod``` in ```AbstractCoordinate``` need to be defined. For example:

```
class Coordinate(AbstractCoordinate):
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @y.deleter
    def y(self):
        self._y = None
        
    def __init__(self, xvalue, yvalue):
        self.x = xvalue
        self.y = yvalue
        

```

![img_082](./images/img_082.png)

The docstring can be viewed by inputting ```Coordinate()``` and pressing shift ```⇧``` and tab ```↹```:

![img_083](./images/img_083.png)

An instance can be instantiated using:

```
c1 = Coordinate(3, 4)
```

![img_084](./images/img_084.png)

The identifiers can be viewed once again by inputting ```c1.``` and pressing tab ```↹```:

![img_085](./images/img_085.png)

The attributes ```x``` and ```y``` from the instance ```c1``` can be get, set and deleted:

```
c1.x
c1.y
c1.x = 5
c1.x
del c1.y
c1.y
```

![img_086](./images/img_086.png)

Recall that ```self``` can be conceptualised as meaning *this instance*. A regular method is bound to *this instance* which is why ```self``` is the first input argument when each method is defined within the class.

Instead of being bound to *this instance* ```self```, a class method is bound to the class ```cls```. The ```@classmethod``` decorator is used to distinguish a class method from a standard instance method. Normally the return value of a class method is a new instance of the class itself and is therefore used as an alternative constructor.  This can alternative constructor can be defined in the ```AbstractCoordinate``` template:

```
class AbstractCoordinate(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @property    
    @abstractmethod
    def x(self):
        pass

    @property    
    @abstractmethod
    def y(self):
        pass

    @classmethod
    @abstractmethod
    def alternativeconstructor(cls):
        pass

```

![img_087](./images/img_087.png)

For simplicity the ```alternativeconstructor``` will use ```yvalue``` and ```xvalue``` opposed to ```xvalue``` and ```yvalue```:

```
class Coordinate(AbstractCoordinate):
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @y.deleter
    def y(self):
        self._y = None
        
    def __init__(self, xvalue, yvalue):
        self.x = xvalue
        self.y = yvalue
        
    @classmethod
    def alternativeconstructor(cls, yvalue, xvalue):
        return(Coordinate(xvalue, yvalue))   

```












classvariable
classmethod
staticmethod































The identifiers can be viewed by inputting ```x1.``` and pressing tab ```↹```:




)
x1.get_x()
```

```point1.``` and pressing tab ```↹```



```
point1.set_y(4)
```


```
class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def del_x(self):
        self.x = None

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def del_y(self):
        self.y = None


```


```
Coordinate()
```


```
point1 = Coordinate(3, 4)
```

```point1.``` and pressing tab ```↹```



```
class Coordinate(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def del_x(self):
        self._x = None

    def get_y(self):
        return self_.y

    def set_y(self, y):
        self._y = y

    def del_y(self):
        self._y = None


```

```
Coordinate()
```


```
point1 = Coordinate(3, 4)
```

```point1.``` and pressing tab ```↹```


```
class Coordinate(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @x.deleter
    def x(self):
        self._x = None

    @property
    def y(self):
        return self_.y

    @y.setter
    def y(self, y):
        self._y = y

    @y.deleter
    def y(self):
        self._y = None


```


```
point1.x
point1.x = 5
point1.x
del point1.x
point1.x
```













## Abstract Base Classes

```
from abc import ABC, abstractmethod

class PersonDesignPattern(ABC):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def talk(self):
        pass
    
```


```
PersonDesignPattern()
```

```
class Person(PersonDesignPattern):
    def walk(self):
        print('Plod Plod Plod')
    
    def talk(self):
        print('Blah Blah Blah')

```

```
fred = Person()
fred.walk()
fred.talk()
```

```
class Horse(PersonDesignPattern):
    def walk(self):
        print('Trot Trot Trot')
    
```


```
george = Horse()
```























