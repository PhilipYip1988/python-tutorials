# The Decimal Module

In the previous tutorials which covered the fundamental datatypes and underlying principles of numbering systems. The floating point number was seen to have been encoded in binary using the IEEE-754 standard and as a result has some unexpected rounding recursion errors.

```
0.1 + 0.2
```

The decimal module is a module built around the ```Decimal``` class which is instead encoded in decimal using the IEEE-854 standard and is designed to work more similar to human based mathematics which also uses the decimal system. It can be imported using:

```
import decimal
```

The docstring for the module isn't very detailed:

```
? decimal
```

```decimal.``` followed by a tab ```↹``` can be pressed to view a list of identifiers. The module is based around the ```Decimal``` class which is usually directly imported.

```
from Decimal import Decimal
```

The ```Decimal``` class can be used to construct new ```Decimal``` instances. 


Typically this is constructed from a string or a series of integers:

```
Decimal("0.3")
```

```
Decimal((0, (3,), -1))
```

```
Decimal((1, (3,), -1))
```

```
Decimal((1, (3, 2, 1), -1))
```


If assigned to an instance, a number of methods are available:

```
dec1 = Decimal("0.3")
```


All of the traditional mathematical operators are also assigned to their respective datamodel methods and can be viewed by looking at the directory using ```dir```:

```
dir(dec1)
```



The mathematics of ```Decimal``` instances behaves more similar to traditional mathematics:

```
Decimal("0.1") + Decimal("0.2")
```

A ```Decimal``` instance can be constructed from a ```float``` instance and will be stored in a higher precision but will inherit the rounding errors from the original ```float``` which was encoded using binary:

```
Decimal(0.1 + 0.2)
```

The concept of ```1/3``` is recurring in decimal:

```
dec1 = Decimal(1) / Decimal(3)
dec1
```

```
num1 = 1/3
num1
```

Notice the difference in the length of the float instance which is 16 and the length of the Decimal instance which is 28:

```
len("3333333333333333")
len("3333333333333333333333333333")
```

The size of the float instance is 24 bytes and the Decimal instance is 104 bytes:

```
from sys import getsizeof
getsizeof(num1)
getsizeof(dec1)
```


Therefore it will take more memory to work with the Decimal instance compared to the float instance. 

## Context

The context for arithmetic is an environment specifying precision, rounding rules, limits on exponents, format of exponents and flags indicating the results of operations, and trap enablers which determine whether signals are treated as exceptions. The context of the ```Decimal``` class can be accessed by using the ```getcontext``` function which is usually imported alonside the ```Decimal``` class using:

```
from decimal import Decimal, getcontext
```

To view the context use:

```
getcontext()
```

## Precision

Each of the items displayed in the output below is accessible as an attribute. For example:

```
getcontext().prec
```



These can also be varied. The ```decimal``` module has a number of constants which relate to the boundaries or discrete values of the context attributes. For ```prec```, there is ```MAX_PREC``` which can be imported using:

```
from decimal import MAX_PREC
MAX_PREC
```


The precision may be changed to 100. Notice the difference in output from before showing an increased number of characters and the object size in memory is also larger:

```
getcontext().prec = 100
dec1 = Decimal(1) / Decimal(3)
dec1
len("3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333")
getsizeof(dec1)
```


Although the upper precision is specified in ```MAX_PREC``` assignment to that value is generally unusable and displays a memory error:

```
getcontext().prec = MAX_PREC
dec1 = Decimal(1) / Decimal(3)
dec1
```


The precision will be set back to the default:

```
getcontext().prec = 28
```


## Rounding

The rounding protocol can be viewed by accessing the ```rounding``` attribute from the context:

```
getcontext().rounding
```

The default is ```ROUND_HALF_EVEN```, the other rounding constants can be imported using:

```
from decimal import ROUND_HALF_EVEN
from decimal import ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_DOWN
from decimal import ROUND_UP, ROUND_CEILING, ROUND_HALF_UP, ROUND_05UP
```

There are very subtle differences in these depending on the rounding boundaries be takenf from ```-inf```, ```0``` or ```+inf```.

```
getcontext().rounding = ROUND_UP
dec1 = Decimal(1) / Decimal(3)
dec1
dec2 = Decimal(2) * Decimal(1) / Decimal(3)
dec2
```



```
getcontext().rounding = ROUND_DOWN
dec1 = Decimal(1) / Decimal(3)
dec1
dec2 = Decimal(2) * Decimal(1) / Decimal(3)
dec2
```



```
getcontext().rounding = ROUND_HALF_EVEN
dec1 = Decimal(1) / Decimal(3)
dec1
dec2 = Decimal(2) * Decimal(1) / Decimal(3)
dec2
```


## Exponent Min, Exponent Max and Exponent Format

```
getcontext().Emin
getcontext().Emax
getcontext().capitals
```

```
from decimal import MIN_EMIN, MAX_EMAX
```

```
getcontext().Emin = -1000
getcontext().Emax = 1000
```

```
Decimal("1.234e-1000") * Decimal("1.234e-1000")
```

```
getcontext().Emin = -10000
getcontext().Emax = 10000
getcontext().capitals = 0
```

```
Decimal("1.234e-1000") * Decimal("1.234e-1000")
```


## Overflow and Underflow

```
getcontext().traps
```


```
from decimal import Underflow, Overflow
```

```
getcontext().traps[Underflow] = True
getcontext().traps[Overflow] = True
getcontext().prec = 6 
getcontext().Emin=-999
getcontext().Emax=999
getcontext().clamp = 1
```


```
Decimal("1.230000e999") * Decimal("10000")
Decimal("1.230000e-999") / Decimal("10000")
```

## Division by Zero and Invalid Operation

```
from decimal import DivisionByZero, InvalidOperation
```



```
Decimal("1") / Decimal("0")
```


```
getcontext().traps[DivisionByZero] = False
```



```
Decimal("1") / Decimal("0")
```



```
Decimal("0") / Decimal("0")
```



```
getcontext().traps[InvalidOperation] = False
```



```
Decimal("0") / Decimal("0")
```



