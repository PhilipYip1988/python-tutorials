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

Some more details may be deciphered from the variable name:

```
date = (4, 3, 2023)
```

However it is still unclear whether the 4 is the day (UK format) or the month (US format). In such a case, a dictionary may be more appropriate. The ```dict``` class can be used to instantiate the dictionary:

```
date = dict(day=4, month=3, year=2023)
date
```

When dealing with a large number of archives, the keys need to be specified every time:

```
today = dict(day=14, month=3, year=2023)
tommorrow = dict(day=15, month=3, year=2023)
yesterday = dict(day=13, month=3, year=2023)
nextmonth = dict(day=14, month=4, year=2023)
nextyear = dict(day=14, month=3, year=2024)
```

And there is no check to make sure the keys are input consistently:

```
tommorrow = dict(d=15, m=3, y=2023)
```

It is more convenient to group all of the data above into a subclass that has a datastructure similar to a ```tuple``` but is fixed length and associates each record with an appropriate field name. 

The ```namedtuple``` is a factory function that creates a ```NamedTuple``` subclass; essentially a ```tuple```-like data structure or template that in this case has only three fields the  ```'day'```, ```'month'``` and ```'year'``` respectively. Once this subclass is created, it can be instantiated for each date above. 

Do not confuse the factory function ```namedtuple``` which is lower case and the abstract class ```NamedTuple``` which is CamelCase. Note that the abstract class ```NamedTuple``` isn't used directly, instead subclasses with a predefined number of fields and field names are created.

The ```namedtuple``` factory function can be imported from the ```collections``` module using:

```
from collections import namedtuple
```

![img_002](./images/img_002.png)

To view the docstring of the ```namedtuple``` factory function input the function name with open parenthesis followed by shift ```⇧``` + tab ```↹```:

![img_003](./images/img_003.png)

For example the subclass ```DateTuple``` can be created using:

```
DateTuple = namedtuple('DateTuple', ('day', 'month', 'year'))
```

The name of the ```NamedTuple``` subclass ```'DateTuple'``` is supplied as a string for the first input argument which is used to generate a docstring. This normally matches the name ```DateTuple``` the subclass is assigned to and should be in CamelCase. Note the difference between the object name specified without quotations to the left hand side of the assignment operator and the string provided as the first input argument to the ```namedtuple``` factory function which is enclosed in quotations:

![img_004](./images/img_004.png)

The names of the fields are supplied as a ```tuple``` of strings:

```
DateTuple = namedtuple('DateTuple', 
                       ('day', 'month', 'year'))
```

These can optionally be given default values:

```
DateTuple = namedtuple('DateTuple', 
                       ('day', 'month', 'year')
                       defaults=(14, 3, 2023))
```


The ```DateTuple``` subclass docstring can be viewed by typing in ```DateTuple``` with open parenthesis followed by shift ```⇧``` + tab ```↹```:

![img_006](./images/img_006.png)

When the ```NamedTuple``` subclass was assigned a different name, the docstring uses the string supplied as the first input argument and is inconsistent to the init signature of the created subclass which uses the class name assigned:

```
DateTuple2 = namedtuple('DateTuple', ('day', 'month', 'year'))
```

![img_007](./images/img_007.png)

Date instances, that is archives with the fields ```day```, ```month``` and ```year``` can be instantiated. Consistency in their format (UK date format) is maintained by following the docstring:

![img_006](./images/img_006.png)

```
today = DateTuple(day=14, month=3, year=2023)
tomorrow = DateTuple(day=15, month=3, year=2023)
yesterday = DateTuple(day=14, month=3, year=2023)
```

![img_008](./images/img_008.png)

the field names were implicitly specified in the above. The values can be proved positionally:

```
today = DateTuple(14, 3, 2023)
tomorrow = DateTuple(15, 3, 2023)
yesterday = DateTuple(14, 3, 2023)
```

![img_009](./images/img_009.png)

The ```namedtuple``` factory function can take in a keyword input argument ```defaults``` which is assigned to a ```tuple``` of default values.

```
DateTuple = namedtuple('DateTuple', 
                       ('day', 'month', 'year'),
                       defaults=(14, 3, 2023))
```



Generally


```
today._fields
today._field_defaults

today._asdict()

today._replace(year=2024)

today._make((1, 2, 3))
DateTuple(*(1, 2, 3))
DateTuple(**{'day': 1, 'month': 2, 'year': 3})
```


Looking at the identifiers of ```today``` by inputting ```today.``` followed by a tab ```↹```:

![img_010](./images/img_010.png)

The field names ```day```, ```month``` and ```year``` display as attributes:

```
today.day
today.month
today.year
```

![img_011](./images/img_011.png)

The other two identifiers ```count``` and ```index``` are identifiers which are inherited from the ```tuple``` and therefore behave in an identical manner.

As a ```NamedTuple``` subclass is based upon a ```tuple``` it is immutable and the instance inherits all the data model identifiers from the ```tuple```, which can be seen if the directory of this instance is examined:

```
dir(today)
```

![img_012](./images/img_012.png)

These data model identifiers behave in an identical manner to a ```tuple``` as they are inherited from the ```tuple```.

The Spyder Variable Explorer, doesn't show the Field names and the ```NamedTuple``` subclass ```DateTuple``` instance ```today``` just displays as an ordinary ```tuple```:

![img_013](./images/img_013.png)

![img_014](./images/img_014.png)

Hopefully a Field column will be added, that displays the field names.

## 


















