# The Collections Module

Python has a ```collections``` module which has a number of supplementary collections to those explored in Pythons ```builtins```. It can be imported using:

```
import collections
```

And the modules docstring can be viewed:

```
? collections
```

![img_001](./images/img_001.png)

The most important classes are listed. The three in lower case were orginally designed to become.

## namedtuple

A ```tuple``` can be conceptualised as an immutable archive of records. Each record only has a numeric index associated with the value and doesn't have a field name to describe what the value is. For example in the following tuple it is hard to distinguish what field is what:

```
(4, 3, 2023)
```

![img_002](./images/img_002.png)

Some more details may be deduced from the variable name:

```
date = (4, 3, 2023)
```

![img_003](./images/img_003.png)

However it is still unclear whether the 4 is the day (UK format) or the month (US format). In such a case, a dictionary may be more appropriate. The ```dict``` class can be used to instantiate the dictionary:

```
date = dict(day=4, month=3, year=2023)
date
```

![img_004](./images/img_004.png)

When dealing with a large number of archives, the keys need to be specified every time:

```
today = dict(day=14, month=3, year=2023)
tommorrow = dict(day=15, month=3, year=2023)
yesterday = dict(day=13, month=3, year=2023)
nextmonth = dict(day=14, month=4, year=2023)
nextyear = dict(day=14, month=3, year=2024)
```

![img_005](./images/img_005.png)

And there is no check to make sure the keys are input consistently:

```
tommorrow = dict(d=15, m=3, y=2023)
tommorrow
```

![img_006](./images/img_006.png)

It is more convenient to group all of the data above into a subclass that has a datastructure similar to a ```tuple``` but is fixed length and associates each record with an appropriate field name. 

The ```namedtuple``` is a factory function that creates a ```NamedTuple``` subclass; essentially a ```tuple```-like data structure or template that in this case has only three fields the  ```'day'```, ```'month'``` and ```'year'``` respectively. Once this subclass is created, it can be instantiated for each date above. 

Do not confuse the factory function ```namedtuple``` which is lower case and the abstract class ```NamedTuple``` which is CamelCase. Note that the abstract class ```NamedTuple``` isn't used directly, instead subclasses with a predefined number of fields and field names are created.

The ```namedtuple``` factory function can be imported from the ```collections``` module using:

```
from collections import namedtuple
```

![img_007](./images/img_007.png)

To view the docstring of the ```namedtuple``` factory function input the function name with open parenthesis followed by shift ```⇧``` + tab ```↹```:

![img_008](./images/img_008.png)

For example the subclass ```DateTuple``` can be created using:

```
DateTuple = namedtuple('DateTuple', 
                       ('day', 'month', 'year'))
```

![img_009](./images/img_009.png)

The name of the ```NamedTuple``` subclass ```'DateTuple'``` is supplied as a string for the first input argument which is used to generate a docstring. This normally matches the name ```DateTuple``` the subclass is assigned to and as it is a subclass should be in CamelCase. Note the difference between the object name specified without quotations to the left hand side of the assignment operator and the string provided as the first input argument to the ```namedtuple``` factory function which is enclosed in quotations:

![img_010](./images/img_010.png)

The names of the fields are supplied as a ```tuple``` of strings:

![img_011](./images/img_011.png)

The field names follow the same rules as Python object names and become input arguments for the ```DateTuple``` subclass as well as identifiers of any ```DateTuple``` instances. 

The input arguments can be seen if the init signature of the ```DateTuple``` subclass by typing in the subclass name followed by open parenthesis and shift ```⇧``` + tab ```↹```:

![img_012](./images/img_012.png)

The identifiers can be seen by inputting the subclass name followed by a ```.``` and pressing tab ```↹```:

![img_013](./images/img_013.png)

The ```count``` and ```index``` methods are inherited from the ```tuple``` superclass and the method resolution order ```mro``` is inherited from the ```object``` superclass. The ```mro``` can be examined using:

```
DateTuple.mro()
```

![img_014](./images/img_014.png)

From the method resolution order, the abstract superclass ```NamedTuple```, the superclass ```tuple``` and the ```superclass``` object are seen. These methods are not redefined and therefore behave identically to those from their parent class.

If the subclass is assigned to an inconsistent name to the first input argument provided as an input argument in the factory function ```namedtuple```, the init signature and the docstring become inconsistent:

```
InconsistentName = namedtuple('DateTuple', 
                              ('day', 'month', 'year'))
```

![img_015](./images/img_015.png)

By default, ```rename``` is ```False``` which means if an invalid object name is assigned a ```ValueError``` displays:

```
BadName = namedtuple('BadName', 
                     ('da y', 'month', 'year'),
                     rename=False)
```

![img_016](./images/img_016.png)

If ```rename``` is set to ```True``` invalid names will be renamed ```_0``` where the number is the index in the ```NamedTuple``` subclass:

```
BadName = namedtuple('BadName', 
                     ('da y', 'month', 'year'),
                     rename=True)
```
![img_017](./images/img_017.png)

The field names can optionally be given default values:

```
DateTuple = namedtuple('DateTuple', 
                       ('day', 'month', 'year'),
                       defaults=(14, 3, 2023))
```

![img_018](./images/img_018.png)

This means when ```DateTuple``` is instantiated without values provided, the defaults are given:

```
DateTuple()
```

![img_019](./images/img_019.png)

The keyword argument ```module``` is used to update the  ```__module__``` data model identifier. This is consistent to the name of the Python script file (```script```.py file) that the ```NamedTuple``` subclass ```DateTuple``` is assigned in:

```
DateTuple = namedtuple('DateTuple', 
                       ('day', 'month', 'year'),
                       module='script')

DateTuple.__module__
```

![img_020](./images/img_020.png)

Returning to:

```
DateTuple = namedtuple('DateTuple', 
                       ('day', 'month', 'year'),
                       defaults=(14, 3, 2023))
```

![img_021](./images/img_021.png)

The ```DateTuple``` docstring can be viewed by typing in ```DateTuple``` with open parenthesis followed by shift ```⇧``` + tab ```↹```:

![img_022](./images/img_022.png)

```DateTuple``` instances, that is archives with the fields ```day```, ```month``` and ```year``` can be instantiated. Consistency in their format (UK date format) is maintained by following the docstring. Instances can be created using default values, named parameters or positional parameters:

```
today = DateTuple()
tomorrow = DateTuple(day=15, month=3, year=2023)
yesterday = DateTuple(14, 3, 2023)
```

![img_023](./images/img_023.png)

Identifiers can be viewed by typing in an instance name followed by a dot ```.``` and tab ```↹```:

![img_024](./images/img_024.png)

The field names ```day```, ```month``` and ```year``` can be used to read off each value:

```
today.day
today.month
today.year
```

![img_025](./images/img_025.png)

There are a number of additional identifiers available from the parent class ```NamedTuple``` that begin with a leading underscore. The purpose of the leading underscore is to prevent accidental overriding of the identifier with a field name. These identifiers cannot be viewed by typing in the instance name followed by a dot ```.``` and tab ```↹``` and instead the directory of the instance has to be examined using the ```dir``` function:

```
dir(today)
```

![img_026](./images/img_026.png)

The data model identifiers that begin and end with a double underscore are inherited from the superclass ```tuple``` are unmodified and behave identically.

The additional identifiers are the attributes ```_fields``` which returns the ```tuple``` of field names and ```_field_defaults``` which returns a ```dictionary``` where the keys are the field names and the values are the default values:

```
yesterday._fields
yesterday._field_defaults
```

![img_027](./images/img_027.png)

```asdict``` is a method that returns a dictionary where the keys are the field names and the values are the default values:

```
yesterday._asdict
yesterday._asdict()
```

![img_028](./images/img_028.png)

Attempting to cast a ```NamedTuple``` subclass into a dictionary using the ```dict``` class attempts to convert only the ```tuple``` properties into the dictionary and gives a ```TypeError```:

```
dict(yesterday)
```

![img_029](./images/img_029.png)

```_replace``` will create a new instance using replaced field names. In this example only the field name year is replaced:

```
yesterday._replace(year=2024)
```

![img_030](./images/img_030.png)

```_make``` is a class method which will create a new instance from a ```tuple```:

```
t1 = (17, 3, 2024)
DateTuple._make(t1)
```

![img_031](./images/img_031.png)

```tuple``` and ```dict``` unpacking can also be used for this purpose:

```
t1 = (17, 3, 2024)
DateTuple(*t1)
```

![img_032](./images/img_032.png)

```
d1 = {'day': 17, 'month': 3, 'year': 2024}
DateTuple(**d1)
```

![img_033](./images/img_033.png)

The Spyder Variable Explorer, doesn't show the field names in a ```NamedTuple``` subclass and instead just displays an ordinary ```tuple```:

![img_034](./images/img_034.png)

![img_035](./images/img_035.png)

Hopefully a Field column will be added, that displays the field names in the future.

## 


















