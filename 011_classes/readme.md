# Inbuilt Classes

A number of Python objects have previously been explored which belong to either the ```str```, ```int```, ```bool```, ```float```, ```list```, ```tuple``` and ```dict``` classes. Notice that when one of these class names is input followed by a dot ```.``` and tab ```↹```, that a list containing functions and properties displays:

![img_000](./images/img_000.png)

![img_001](./images/img_001.png)

![img_002a](./images/img_002a.png)

![img_002](./images/img_002.png)

![img_003](./images/img_003.png)

![img_004](./images/img_004.png)

![img_005](./images/img_005.png)

Under the hood, each of these functions and properties is defined in the class. A class can be conceptualised as a blueprint which is a set of instructions to make an object and is not a physical object itself. Any instance of the class (physical object built using the blueprint) will have these associated functions and properties. For example:

```
num = 5
```

![img_006](./images/img_006.png)

```
word = "Hello"
```

![img_007](./images/img_007.png)

Notice that there is a subtle difference between ```int.attribute``` and ```int_instance.attribute```. In the former case ```attribute of "int" objects``` displays and the class is displaying information, like a blueprint does. In the latter case a number displays. Attributes can be conceptualised as an embedded object and an analogy to an attribute of an instance of a class is a variable in a module. Notice that identical syntax is used in both cases compare ```module.variable``` with ```int_instance.attribute```, in both cases the object being accessed is to the right hand side of the dot ```.``` and the object used as a container is to the left hand side of the ```.```:

```
int.real
int.imag

num.real
num.imag
```

![img_027](./images/img_027.png)

A function can be referenced in an identical manner to an attribute:

```
int.conjugate
num.conjugate
```

Notice that there is a subtle difference between ```int.function``` and ```int_instance.function```. In the former case the function is called a ```method```. A ```method``` has an additional positional input argument called ```self``` which must be assigned to an instance of the object for the function to act on. In the latter case, because the function is referenced from an instance, this instance is automatically implied to be ```self```:

![img_028](./images/img_028.png)

Functions are called using parenthesis to enclose any input arguments:

* For the method ```conjugate``` an instance ```self``` must be proved for the function to operate on. 
* For the function ```conjugate``` there are no input arguments with ```self``` being implied from the instance ```num```. 

```
int.conjugate(num)
num.conjugate()
```

![img_029](./images/img_029.png)

There are a number of hidden functions not shown in the lists above which typically map to operators. For example the hidden function ```__add__``` which is mapped to the ```+``` operator:

```
num1 = 5
num2 = 6
num1 + num2
num1.__add__(num2)
```

![img_008](./images/img_008.png)

```
word1 = "Hello"
word2 = "World"
word1 + word2
word1.__add__(word2)
```

![img_009](./images/img_009.png)

Notice the different behaviour in the code above; numeric addition for the integer class versus concatenation for the string class. The difference in behaviour is due to the two functions ```int.__add__``` and ```str.__add__``` being unique. 

Conceptually each class can be thought of as a seperate module which contains a function with the same name but this function has different code in the code block and therefore carries out different behaviour:

![img_010](./images/img_010.png)

![img_011](./images/img_011.png)

Notice that in either case, the return value for each function is itself an instance of the same class. i.e. numeric addition of two integers results in an integer and concatenation of two strings results in a string.

The functions do not always return an instance of the same class. For example the list function ```__len__``` returns an instance of the integer class:

![img_012](./images/img_012.png)

```
collection = [1, 2, 3, 4, 5]
collection.__len__()
```

![img_013](./images/img_013.png)

The string function count also returns an instance of the integer class:

```
word1.count("l")
```

![img_014](./images/img_014.png)

The string functions ```__repr__``` and ```__str__``` are two functions which define the string representations of an object. ```__repr__``` is formal and ```__str__``` is informal. Often the string is the same for both functions and as a result they are often confused. However there is a subtle difference. 

This can be demonstated using the string ```file_path```. Due to the ```\``` being used to insert escape characters and the ```\``` being an escape character inserted in the file path:

```
file_path = "C:\\Users\\Philip"
```

Notice the subtle difference between the cell output. The informal representation shows how the string would be input using escape characters:

```
file_path
```

Versus a print statement, which shows what the formal representation of what the string looks like taking into account the effect of the escape characters:

```
print(file_path)
```

![img_015](./images/img_015.png)

The behaviour of these are controlled with ```__repr__``` and ```__str__``` respectively. If these functions are called within a print statement, the same cell output in response to the string ```file_path``` and due to a print statement of the string ```file_path``` are observed:

```
file_path.__repr__()
print(file_path.__repr__())
```

```
file_path.__str__()
print(file_path.__str__())
```

![img_016](./images/img_016.png)

Instead of mapping to inbuilt operators, the hidden functions ```__len__```, ```__repr__``` and ```__str__``` define how the  inbuilt functions ```len```, ```repr``` and casting an object to a string using ```str``` behave.

```
len([1, 2, 3, 4, 5])
repr(file_path)
str(file_path)
```

![img_017](./images/img_017.png)

Notice, the function ```__len__``` when called from an instance of a list requires no input arguments. However if ```__len__``` is called from the class list there is a ```TypeError``` and a warning that an input argument missing:

```
collection = [1, 2, 3, 4, 5]

collection.__len__()

list.__len__()

list.__len__(collection)
```

![img_018](./images/img_018.png)

Recall that a function determines the behaviour of an object.

For the method ```__len__``` an instance ```self``` must be proved for the function to operate on:

![img_019](./images/img_019.png)

For the function ```__len__``` there are no input arguments with ```self``` being implied from the instance ```num```. 

![img_020](./images/img_020.png)

**When a function is called from a class, it is known as a ```method``` and requires an instance ```self``` to be provided as the 1st positional input argument.**

Importing modules and librarys was examined in detail in the previous tutorial. Recall, that a library is a number of Python script files in a folder. One of these script files is an initialisation script file called ```__init__.py```:

![img_021](./images/img_021.png)

![img_022](./images/img_022.png)

Recall when the name of the folder is imported, this ```__init__.py``` is selected:

```
import library
```

![img_023](./images/img_023.png)

Each class also has an initialisation method ```__init__``` which typically takes in one or more input arguments and uses these alongside, a return statement to return a new instance of the class. This iniitialisation method can be thought of as a constructor function which builds a physical object from a blueprint:

![img_025](./images/img_025.png)

The ```__init__.py``` within a library is not imported using the name of the script file but instead using the name of the library. Analogously, the ```__init__``` method is not called using the name of the method but is called using the name of the class:

![img_026](./images/img_026.png)

An example of this is given when the integer number ```5``` is cast to a string using the ```str``` class:

```
str(5)
```

![img_024](./images/img_024.png)

# Datamodel Methods

Python uses a number of datamodel methods which control the behaviour of inbuilt Python functions or the behaviour of inbuilt operators. Under the hood, datamodel methods define how an instance ```self``` interacts or how an instance ```self``` interacts with another instance called ```other```. These datamodel methods are sometimes known as special methods or colloquially called double underscore methods abbreviated as dunder methods.

The following datamodel methods operate on only the instance ```self```:

|method|operator or function|int|float|bool|str|list|tuple|dict|
|---|:-:|---|---|---|---|---|---|---|
|\_\_init\_\_|class name|initialisation|initialisation|initialisation|initialisation|initialisation|initialisation|initialisation|
|\_\_len\_\_|len|Not Implemented|Not Implemented|Not Implemented|length|length|length|length|
|\_\_repr\_\_|repr|formal str|formal str|formal str|formal str|formal str|formal str|formal str|
|\_\_str\_\_|str|informal str|informal str|informal str|informal str|informal str|informal str|informal str|
|\_\_dir\_\_|dir|dir|dir|dir|dir|dir|dir|dir|

The following datamodel methods require two instances ```self``` and ```other```:

|method|operator or function|int|float|bool|str|list|tuple|dict|
|---|:-:|---|---|---|---|---|---|---|
|\_\_add\_\_|+|addition|addition|addition|concatenation|concatenation|concatenation|concatenation|
|\_\_sub\_\_|-|subtraction|subtraction|subtraction|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_mul\_\_|\*|multiplication|multiplication|multiplication|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_pow\_\_|\*\*|exponentiation|exponentiation|exponentiation|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_truediv\_\_| \\ |float division|float division|float division|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_floordiv\_\_| \\\\ |floor division|floor division|floor division|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_mod\_\_|%|modulo|modulo|modulo|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_divmod\_\_|divmod|(floor division, modulo)|(floor division, modulo)|(floor division, modulo)|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_matmul\_\_|@|Not Implemented|Not Implemented|Not Implemented|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_gt\_\_|>|greater than|greater than|greater than|greater than|greater than|greater than|greater than|
|\_\_ge\_\_|>=|greater than or equal to|greater than or equal to|greater than or equal to|greater than or equal to|greater than or equal to|greater than or equal to|greater than or equal to|
|\_\_lt\_\_|<|less than|less than|less than|less than|less than|less than|less than|
|\_\_le\_\_|>=|less than or equal to|less than or equal to|less than or equal to|less than or equal to|less than or equal to|less than or equal to|less than or equal to|
|\_\_eq\_\_|==|equal to|equal to|equal to|equal to|equal to|equal to|equal to|
|\_\_ne\_\_|!=|not equal to|not equal to|not equal to|not equal to|not equal to|not equal to|not equal to|

The following datamodel methods require two instances ```self``` and ```other``` and update ```self``` inplace:

|method|operator or function|int|float|bool|str|list|tuple|dict|
|---|:-:|---|---|---|---|---|---|---|
|\_\_iadd\_\_|+=|addition|addition|addition|concatenation|concatenation|concatenation|concatenation|
|\_\_isub\_\_|-=|subtraction|subtraction|subtraction|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_imul\_\_|\*=|multiplication|multiplication|multiplication|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_ipow\_\_|\*\*=|exponentiation|exponentiation|exponentiation|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_itruediv\_\_| \\= |float division|float division|float division|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_ifloordiv\_\_| \\\\= |floor division|floor division|floor division|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_imod\_\_|%=|modulo|modulo|modulo|Not Implemented|Not Implemented|Not Implemented|Not Implemented|
|\_\_imatmul\_\_|@=|Not Implemented|Not Implemented|Not Implemented|Not Implemented|Not Implemented|Not Implemented|Not Implemented|

# Class Instance and Blueprint House Analogy

In Python each object has a class, which initially can be conceptualised as an abstract blueprint which defines how to create a new object and outlines the properties and functionality behind an object. Before looking at creating a custom class, it is useful to explore the concept of a class by using every day intuition and framing it in Python syntax.

To conceptualise this idea take for example the concept of building a house. An Architect may create a blueprint for a house called ```House```, this blueprint is an abstract object, that an end user cannot interact with. CamelCaseCapitalisation is used for third-party class names and this convention is used to clearly distinguish them from inbuilt objects. The class ```House``` will outline the features or attributes of a house such as the height of the house ```househeight```, how many rooms it possesses ```nrooms``` and the size of the bedroom ```bedroomsize```. It will also outline the functionality of the house such as the doors in the house ```frontdooropen``` or ```frontdoorclose```, the windows in the house ```frontwindowopen``` or ```frontwindowclose```, the central heating system controls ```sethousetemperature``` and the sewage controls ```flushtoilet```.

A construction company can follow the instructions in this blueprint called ```House``` to create one or multiple houses. Each house will be constructed using the same blueprint but each object created will be unique. To indicate that each house is unique, the construction company will assign each new house object, a name during construction which is known as a post code. This process is known as initialisation or instantiation, creating a new physical object or instance from the blueprint or class ```House```. In Python, the post code is known as the ```object name``` or ```instance name```, for simplicity two houses ```house000``` and ```house001``` can be made.

The end user (homeowner or tenant) will be able to uniquely interact with their own house object using the functions outlined in the blueprint House. These functions are methods for interacting with a house object. For example the owner of ```house000``` will be able to leave their house by calling the method ```house000.frontdooropen()``` and ```house000.frontdoorclose()``` and set the temperature on their central heating system by calling the method ```house000.sethousetemperature(temp=24)```. Notice that these interactions with ```house000``` will not change the functionality of ```house001``` although the behaviour for both houses is defined in the same ```House``` class. Notice that these functions, are called with parenthesis and in the case of the last function an input argument is provided. The dot syntax ```.``` indicates that the function is being called from the object ```house000```.

The homeowner of ```house000``` may want to rent out a bedroom in their house and may have to list it with the following attributes ```house000.nrooms``` and ```house000.bedroomsize``` for example. The dot syntax ```.``` once again indicates that the attribute is being read from the object ```house000```. Usually if an attribute is altered, it'll be altered via a function and not reassigned directly. For example if the ```house000.nrooms``` attribute is altered, it'll typically be altered by using a function for example ```house000.buildextension()```.

# The object Class

In Python, everything is based around the concept of an object. To explore this in more detail, the generic ```object``` class can be examined. If ```object(``` is input followed by shift ```⇧``` and tab ```↹``` th docstring for the initialisation signature of the object class display:

![img_031](./images/img_031.png)

Recall that this uses the method ```__init__```:

![img_032](./images/img_032.png)

The docstring states:

```
"""
The base class of the class hierarchy.

When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.
"""
```

Therefore in this case, to create an object instance of the object class, no positional input arguments are required.

```
instance = object()
```

![img_033](./images/img_033.png)

If ```instance.``` is typed followed by a tab ```↹```, nothing displays because this object has no instance attributes.

![img_034](./images/img_034.png)

The ```dir``` function treats the object instance as a directory and lists all the objects within that directory. This includes the datamodel methods which are hidden from the ```.↹```listing: 

```
dir
```

A list displays which includes the data model methods:

![img_035](./images/img_035.png)

These include ```__init__```, ```__dir__```, ```__repr__``` and ```__str__```. ```__repr__``` and ```__str___```, the formal and informal representation of a string display that the object is present in a certain memory locaiton by default:

![img_036](./images/img_036.png)

```__eq__``` and ```__neq__``` comparison methods are defined.

![img_038](./images/img_038.png)

And they can be used to check whether or not two objects are the same:

```
instance1 = object()
instance2 = object()
instance1 == instance2
instance1 != instance2
```

![img_037](./images/img_037.png)

The four other comparison operators ```__gt__```, ```__ge__```, ```__lt__``` and ```__le__``` show in the directory listing. However these operations are not supported between instances of the class object as instance1 and instance2 are not ordinal:

![img_039](./images/img_039.png)

![img_040](./images/img_040.png)

The other data model methods are not listed and therefore have no code defining them and are unsupported:

![img_041](./images/img_041.png)

# Creating a Custom Class

The ```class``` keyword is used to construct a class. Third-party class names are typically named using CamelCaseCapitalisation. This syntax is used to clearly differenciate user defined third-party classes from inbuilt objects. Parenthesis are used to enclose the parent class. When no parent class is defined, the default parent class ```object``` is used. A colon ```:``` is then used to begin a code block. For now ```pass``` will be used:

```
class EmptyEmpty(object):
   pass
   
   
``` 

![img_042](./images/img_042.png)

The ```___init___``` datamodel method will be inherited from the parent class ```object```.

![img_043](./images/img_043.png)

Notice that no ```docstring``` displays for this method. Like the ```_init__``` method from the parent class ```object``` an instance is instantiated without providing an input argument

```
instance = EmptyEmpty()
instance
print(instance)
```

![img_044](./images/img_044.png)

The formal and informal string represation also display details about the instance, in a manner similar to the parent class ```object```. This is because the methods ```__repr__``` and ```__str__``` are inherited from the parent class. The ```dir``` function treats the ```EmptyEmpty``` ```instance``` called ```instance``` as a directory and lists all the objects within that directory.

```
dir(instance)
```

![img_045](./images/img_045.png)

Notice that these are identical to a instance of the ```object``` class. This is expected as the ```child``` class ```EmptyEmpty``` inherits these methods from the parent class ```object``` and no additional functionality has been added to the ```child``` class.

## Functions to Methods

Another class can be created called ```TestClass``` which has additional functionality. A class can be conceptualised as a grouping of functions.

```
class TestClass(object):
    def function1(*args, **kwargs):
        return None
       
       
    def function2(*args, **kwargs):    
        return None
       
       
    def function3(*args, **kwargs):    
        return None
       
       
    def function4(*args, **kwargs):    
        return None
       
   
``` 

Because each function in the class is a method, the first positional input argument must be ```self```:

```
class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       

``` 

## Variables to Attributes

An additional function can be created that takes in 4 additional input arguments and creates 4 variables:

```
class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
       
    def create_attributes(self, value1, value2, value3, value4):
        var1 = value1
        var2 = value2
        var3 = value3
        var4 = value4
   
   
``` 

For these variables to become attributes, they must be referenced with respect to the instance which is denoted ```self```:

```
class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
       
    def create_attributes(self, value1, value2, value3, value4):
        self.var1 = value1
        self.var2 = value2
        self.var3 = value3
        self.var4 = value4
        return None
   
   
``` 

Note a clear distinction was made to the left and right hand side of the assignment operator. The hand side attribute name and right hand side input argument have different names. It is more typical to use the same name in both cases:

```
class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
        
    def create_attributes(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
   
   
   
``` 

However it should be understood that ```value1``` on the right hand side of the assignment operator is provided by the input argument. The assignment operator assigns this to an attribute of the instance ```self``` with the name ```value1```.

Now that the ```TestClass``` class is ready:

![img_046](./images/img_046.png)

An instance can be created:

```
instance = TestClass()
```

![img_048](./images/img_048.png)


And if the instance name ```instance``` is input followed by a dot ```.``` and tab ```↹```, a list of available functions display:

![img_047](./images/img_047.png)

The following four functions can be called from the instance ```instance```. Note that no output is shown because the return value for each function is ```None```:

```
instance.function1()
instance.function2()
instance.function3()
instance.function4()
```



If the instance name ```instance``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions displays and is unaltered:



If ```instance.create_attributes(``` is input followed by shift ```⇧``` and ```↹```, details about the positional input arguments display ```value1```, ```value2```, ```value3``` and ```value4```. Because no docstring was provided, ```<no docstring>``` displays.

For simplicity these will be input as ```1```, ```2```, ```3``` and ```4```:

```
instance.create_attributes(1, 2, 3, 4)
```


If the instance name ```instance``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions displays and now includes a list of the four attributes:

```
instance.value1
instance.value2
instance.value3
instance.value4
```

## The ```__init__``` Datamodel Initialisation Method

The initialisation method ```__init__``` is invoked when instantiating a class. The ```__init__``` method is often refered to as a constructor as it is used to construct a new physical object or instance of the class. Going back to the analogy of a blueprint and a house, the constructor is used to build a house from the blueprint. 

If the method ```create_attributes``` is renamed ```__init__``` and the class is redefined.

```
class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
        
    def __init__(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
   
   
```

When ```TestClass(``` is input followed by shift ```⇧``` and ```↹```, details about the positional input arguments display. ```value1```, ```value2```, ```value3``` and ```value4``` are shown. These come from the definition of the ```__init__``` method and a value for each of these positional input arguments must now be provided during instantiation.



Two instantiations can be made to the names ```instance1``` and ```instance2```

``` 
instance1 = TestClass(1, 2, 3, 4)
instance2 = TestClass(2, 4, 6, 8)
```


If the instance name ```instance1``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions and attributes displays:



An identical list of available functions and attributes displays for ```instance2```:




Notice that although the attributes have the same name, they are assigned to have different values for each instance.

```
instance1.value1
instance1.value2
instance1.value3
instance1.value4
instance2.value1
instance2.value2
instance2.value3
instance2.value4
```

If ```instance1``` and ```instance2``` are conceptualised as houses, built from a common blueprint, each of the values can be considered as a property of the house. ```value1``` for example could be the number of rooms in the house during construction.

## Accessing a Method within another Method

The ```create_attributes``` method can be redefined:

```
    def create_attributes(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
        
        
```

The ```__init__``` method can be modified to call ```create_attributes``` function from the instance ```self```. 

```
    def __init__(self, value1, value2, value3, value4):

        return None
```

The ```create_attributes``` function can be called by the ```__init__``` method from the instance ```self```. 

```
    def __init__(self, value1, value2, value3, value4):
        self.create_attributes(value1, value2, value3, value4)
        return None
```

Notice ```self``` is provided as the first positional input argument for the ```__init__``` method. The other 4 positional arguments ```value1```, ```value2```, ```value3``` and ```value4``` must also be supplied, so they can be passed onto the method ```create_attributes```.

```
    def __init__(self, value1, value2, value3, value4):
        self.create_attributes(value1, value2, value3, value4)
        return None
```

Notice that when the function ```create_attributes``` is called, it is called from an instance ```self``` and therefore ```self``` should not be provided as an input argument.

The updated ```TestClass``` is as follows and should have identical behaviour to before:

```
class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
        
    def create_attributes(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
    
    
    def __init__(self, value1, value2, value3, value4):
        self.create_attributes(value1, value2, value3, value4)
        return None
   

```

Two instantiations can be made to the names ```instance1``` and ```instance2```

``` 
instance1 = TestClass(1, 2, 3, 4)
instance2 = TestClass(2, 4, 6, 8)
```

If the instance name ```instance1``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions and attributes displays:



An identical list of available functions and attributes displays for ```instance2```:



Both of these are identical to before.

```
instance1.value1
instance1.value2
instance1.value3
instance1.value4
instance2.value1
instance2.value2
instance2.value3
instance2.value4
```

## Public, Internal Use and Private

The method ```create_attributes``` is public and is therefore accessible from any instance created. It can be designated as a method designed for internal use by prefixing the method name with an underscore ```_```. In this case ```create_attributes``` becomes ```_create_attributes```. The ```__init__``` method also needs to be updated to call ```_create_attributes``` instead of ```create_attributes```:

```
    def _create_attributes(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
    
    
    def __init__(self, value1, value2, value3, value4):
        self._create_attributes(value1, value2, value3, value4)
        return None
```

The class therefore becomes:

```
class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
        
    def _create_attributes(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
    
    
    def __init__(self, value1, value2, value3, value4):
        self._create_attributes(value1, value2, value3, value4)
        return None
   
   
```   

Two instantiations can be made to the names ```instance1``` and ```instance2``` respectively:

``` 
instance1 = TestClass(1, 2, 3, 4)
instance2 = TestClass(2, 4, 6, 8)
```


If the instance name ```instance1``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions and attributes displays:



An identical list of available functions and attributes displays for ```instance2```:



Notice that both of these do not display ```_create_attributes``` which has been designated for only internal use.



This method will show if ```dir``` is used:

```
dir(TestClass)
```

The values of the attributes are identical to before:

```
instance1.value1
instance1.value2
instance1.value3
instance1.value4
instance2.value1
instance2.value2
instance2.value3
instance2.value4
```

Althought the method ```_create_attributes``` is designated for internal use. It can however be called from an instance using:

```
instance1._create_attributes(10, 20, 30, 40)
```


The attributes are updated as expected:

```
instance1.value1
instance1.value2
instance1.value3
instance1.value4
```


The method ```create_attributes``` can be designated as a private method using a double underscore ```__create_attributes``` instead of a single underscore ```_create_attributes```. Once again both the method and ```__init__``` which calls the method need to be updated:

```
    def __create_attributes(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
    
    
    def __init__(self, value1, value2, value3, value4):
        self.__create_attributes(value1, value2, value3, value4)
        return None
   
```

The updated class becomes:

```

class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
        
    def __create_attributes(self, value1, value2, value3, value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
    
    
    def __init__(self, value1, value2, value3, value4):
        self.__create_attributes(value1, value2, value3, value4)
        return None
   

```


Two instantiations can be made to the names ```instance1``` and ```instance2``` respectively:

``` 
instance1 = TestClass(1, 2, 3, 4)
instance2 = TestClass(2, 4, 6, 8)
```


If the instance name ```instance1``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions and attributes displays:



An identical list of available functions and attributes displays for ```instance2```:



Notice that both of these do not display ```__create_attributes``` which has been designated for only private use.



This method will show at the top if ```dir``` is used:

```
dir(TestClass)
```

Notice it shows as ```_TestClass__create_attributes``` opposed to ```__create_attributes```.

The values of the attributes are identical to before:

```
instance1.value1
instance1.value2
instance1.value3
instance1.value4
instance2.value1
instance2.value2
instance2.value3
instance2.value4
```



An ```AttributeError``` displays if the function```__create_attributes``` is attempted to be called from an instance:

```
instance1.__create_attributes(10, 20, 30, 40)
```



In Python, nothing is truely private and the function can be called using ```_TestClass__create_attributes``` with the clear syntax ```_TestClass``` (this method is designed for internal use only within ```TestClass``` and ```__``` this method is designed to be private):

```
instance1._TestClass__create_attributes(10, 20, 30, 40)
```



The attributes are updated as expected:

```
instance1.value1
instance1.value2
instance1.value3
instance1.value4
```



If the method ```create_attributes``` is updated to assert the datatype of each input argument as an ```int```:

```
    def create_attributes(self, value1, value2, value3, value4):
        assert type(value1) == int
        assert type(value2) == int
        assert type(value3) == int
        assert type(value4) == int
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
    
    
    def __init__(self, value1, value2, value3, value4):
        self.create_attributes(value1, value2, value3, value4)
        return None
   
```   

The updated class becomes:

```
class TestClass(object):
    def function1(self, *args, **kwargs):
        return None
       
       
    def function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
        
    def create_attributes(self, value1, value2, value3, value4):
        assert type(value1) == int
        assert type(value2) == int
        assert type(value3) == int
        assert type(value4) == int
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
    
    
    def __init__(self, value1, value2, value3, value4):
        self.create_attributes(value1, value2, value3, value4)
        return None
   

```

Two instantiations can be made to the names ```instance1``` and ```instance2```:

``` 
instance1 = TestClass(1, 2, 3, 4)
instance2 = TestClass(2, 4, 6, 8)
```


If the instance name ```instance1``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions and attributes displays:



An identical list of available functions and attributes displays for ```instance2```:



Since the attributes can be accessed directly, they can be assigned to any value or any datatype. For example:

```
instance1.value1 = "Hello"
```



This makes the assertion protection used in the method ```create_attributes``` redundant and the user could experience later problems with one of the attributes being the wrong datatype.

To prevent this, it is common to designate the attributes as designed for internal use or private once again by prefixing with a single underscore ```_``` or double underscore ```__```. Methods can be created to get and set the attribute, with the set method also asserting the correct datatype. In this example the method ```_function1``` and attribute ```_value``` are designated for internal use and the method ```__function2``` and attribute ```__value2``` are designated as private. Both these attributes have simple ```get``` and ```set``` methods.


```
class TestClass(object):
    def _function1(self, *args, **kwargs):
        return None
       
       
    def __function2(self, *args, **kwargs):    
        return None
       
       
    def function3(self, *args, **kwargs):    
        return None
       
       
    def function4(self, *args, **kwargs):    
        return None
       
        
    def create_attributes(self, value1, value2, value3, value4):
        assert type(value1) == int
        assert type(value2) == int
        assert type(value3) == int
        assert type(value4) == int
        self._value1 = value1
        self.__value2 = value2
        self.value3 = value3
        self.value4 = value4
        return None
    
    
    def __init__(self, value1, value2, value3, value4):
        self.create_attributes(value1, value2, value3, value4)
        return None
    
    
    def get_value1(self):
        return self._value1
   

    def set_value1(self, new_value1):
        assert type(new_value1) == int
        self._value1 = new_value1
        return None
    
    
    def get_value2(self):
        return self.__value2
   

    def set_value2(self, new_value2):
        assert type(new_value2) == int
        self.__value2 = new_value2
        return None
    
    
```    



Notice that the attributes designated for internal use and private use do not display when ```dir``` is used:

```
dir(TestClass)
```

An instantiation of the class can be made to the name ```instance1```:

```
instance1 = TestClass(1, 2, 3, 4)
```



If the instance name ```instance1``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions and attributes displays:



```
instance1.get_value1()
instance1.set_value1(10)
instance1.get_value1()
instance1.get_value2()
instance1.set_value2(20)
instance1.get_value2()
```


## Linking Get, Set and Del Methods

```
? property
```

```
class TestClass(object):
    def __init__(self, value1):
        self.value1 = value1
        return None
    
    
    def get_value1(self):
        print("get_value1 method used")
        return self._value1


    def set_value1(self, value1):
        assert type(value1) == int
        print("set_value1 method used")
        self._value1 = value1
        return None
    
    
    def del_value1(self):
        print("del_value1 method used")
        self._value1 = 0
        return None
    
    
    value1 = property(get_value1, set_value1, del_value1)
    
    
```

```
instance = TestClass(4)
instance.value1
instance.value1 = 10
instance.value1
del instance.value1
instance.value1
```

```
class TestClass(object):
    def __init__(self, value1):
        self.value1 = value1
        return None
    
    
    @property   
    def value1(self):
        print("get_value1 method used")
        return self._value1
    
    
    @value1.setter
    def value1(self, value1):
        assert type(value1) == int
        print("set_value1 method used")
        self._value1 = value1
        return None
    
    
    @value1.deleter
    def value1(self):
        print("del_value1 method used")
        self._value1 = 0
        return None
    
    
```

```
instance = TestClass(4)
instance.value1
instance.value1 = 10
instance.value1
del instance.value1
instance.value1
```


## Class Variable

```
class TestClass(object):
    def __init__(self, value1, value2, value3, value4):
        # internal attribute
        self._value1 = value1
        # private attribute
        self.__value2 = value2
        # public attributes
        self.value3 = value3
        self.value4 = value4        
        return None
        
        
```


```
class TestClass(object):
    def __init__(self, value1, value2, value3):
        # internal attribute
        self._value1 = value1
        # private attribute
        self.__value2 = value2
        # public attribute
        self.value3 = value3      
        return None
    
    # class variable
    value4 = 4  
    
    
```    



Three instantiations can be made to the names ```instance1```, ```instance2``` and ```instance3```:


```
instance1 = TestClass(1, 2, 3)
instance2 = TestClass(2, 4, 6)
instance3 = TestClass(3, 6, 9)
```


If the instance name ```instance1``` is input followed by a dot ```.``` and tab ```↹```, the list of available functions and attributes displays:



An identical list of available functions and attributes displays for ```instance2```:



An identical list of available functions and attributes displays for ```instance3```:




Notice only the public attribute and class variable display as attributes. Each instance of the class will have the same initial value for the attribute:

```
instance1.value4
instance2.value4
instance3.value4
```

If the variable is accessed as an attribute from an instance and changed, it will not influence other instances:

```
instance1.value4 += 1
instance1.value4
instance2.value4
instance3.value4
```

The class variable can be accessed from the class, without defining an instance. Reassigning it from the class will update the variable in all instances:

```
TestClass.value4 = 10
instance1.value4
instance2.value4
instance3.value4
```

Notice however that the class variable wasn't updated as an attribute for instance1 because the attribute on instance1 was previously redefined to an integer.

The class variable can be used to count the number of instances. ```n_instances``` is initially assigned to ```0``` however the initiation method ```__init__``` updates it by 1 for every instance created:

```
class TestClass(object):
    # class variable
    n_instances = 0
    
    def __init__(self, value1, value2, value3):
        # internal attribute
        self._value1 = value1
        # private attribute
        self.__value2 = value2
        # public attribute
        self.value3 = value3 
        TestClass.n_instances += 1
        return None
   
   
```

```
instance1 = TestClass(1, 2, 3)
instance1.n_instances
instance1 = TestClass(2, 4, 6)
instance1.n_instances
instance2.n_instances
instance3 = TestClass(3, 6, 9)
instance1.n_instances
```

## Class Methods and Static Methods







Instance methods need a class instance and can access the instance through self.

Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.

Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.

Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.

? property 
## Inheritance 

isinstance(4, int)

hasattr(int, "real")

getattr(int, "real")

getattr(num, "real")

delattr()

setattr(

issubclass(bool, int)

bool

int

? slice

[1, 2, 3, 4][slice(2)]
