# Code Blocks

## range and enumerate

The previous tutorial looked at ```list``` and ```tuple``` collections. A ```str``` was also considered to be a collection of characters. Each of these collections have an index with the first number in the index being ```0``` as Python uses zero-order indexing.

In addition to the above a ```range``` object can be created using the syntax:

```
range(start, stop, step)
```

For example:
```
range(0, 10, 1)
```

Because Python uses zero-order indexing, the ```range``` object is inclusive of the ```start``` bound and exclusive of the ```stop``` bound. The ```start``` value of 0 is included and the range object increases using a ```step``` of 1 until the ```stop``` of 10 is reached, however the final value 10 itself is excluded. This can be seen more clearly by assigning the range object to a variable:

```
ro = range(0, 10, 1)
```

And then casting it to a ```list```:

```
rol = list(ro)
```

Or directly:

```
list(range(0, 10, 1))
```

The range object can be indexed in a similar manner to a ```list```:

```
ro[0]
ro[1]
ro[2]
ro[3]
ro[4]
```

And if the final index of the ```range``` object is exceeded, an out of range error is displayed:

```
ro[5]
```

In the above as the ```start``` was 0 and the ```step``` was 1, the index and the value for each item in the ```range``` object matched. These are the default values.

The ```range``` object can be created explicitly specifying 3 positional input arguments. When the ```step``` is 1, it does not have to be explicitly specified:

```
range(start, stop, step)
range(start, stop, 1)
range(start, stop)
```

When the ```step``` is 1, and the ```start``` is 0, only the ```stop``` value needs to be specified:

```
range(start, stop, step)
range(0, stop, 1)
range(0, stop)
range(stop)
```

For clarity, a range object with a ```step``` of 2 will be created, which means the index and the value at the index now differ:

```
ro = range(0, 10, 2)
rol = list(ro)
```

Sometimes it is useful to ```enumerate``` such a ```range``` object:

```
roe = enumerate(ro)
```

Enumeration creates a collection of ```tuple``` (index, value) pairs. This can be more clearly seen by casting the ```enumerate``` object to a ```list```:

```
roel = list(roe)
```

A ```list``` object has an index for each value and like demonstrated above can also be enumerated:

```
lo = ["apples", "bananas", "grapes"]
loel = list(enumerate(lo))
```

A ```str``` can also be regarded as a collection of characters, with each character having its own index and can also be enumerated:

```
s = "apples"
sl = list(s)
soel = list(enumerate(s))
```

## Code Block Spacing

The code block has the following syntax.

```
statement:
    line of code
    line of code
    line of code


```

The statement ends in a colon ```:``` which is used to indicate the beginning of a code block. Each line of code belonging to the code block is indented by 4 spaces. Usually there are two blank lines left at the end of the code block to make it clear the code block has ended.

```
statement:
    belong in block
    belong in block
    belong in block


outside block
outside block
```

Some code blocks can be more complicated and have nested statements. Anything belonging to a nested statement is indented twice using 8 spaces (4 spaces for the outer statement and another 4 spaces for the inner statement).

```
statement1:
    belong in block1
    belong in block1
    belong in block1
    statement2:
        belong in block2 within block1
        belong in block2 within block1
        belong in block2 within block1


outside block
outside block
```

## for loop

The ```for``` loop executes a code block for every item in a collection. The ```for``` loop uses the keywords ```for``` and ```in```. As an example, the collection can be a ```list``` of ```str```:

```
collection = ["apples", "bananas", "grapes"]
```

A ```loop_var``` can be assigned. Thus ```loop_var``` will take on a new value for each iteration of the ```for``` loop. This can be demonstrated by including a ```print``` statement in the code block.

```
collection = ["apples", "bananas", "grapes"]

for loop_var in collection:
    print(loop_var)
    
    
```

Notice that the loop variable ```loop_var``` displays in the Spyder variable explorer and has its final value.

The ```loop_var``` follows the standard Python convention for object names. The above can be rewritten using.

```
collection = ["apples", "bananas", "grapes"]

for word in collection:
    print(word)
    
    
```

Or alternatively.

```
fruits = ["apples", "bananas", "grapes"]

for fruit in fruits:
    print(fruit)
    
    
```

Notice that the collection is plural and the loop variable is singular. 

This can be examined in more detail using the Spyder debugger.

...


Instead of printing the loop variable, a constant ```hello``` can be printed. This is printed for index 0, 1 and 2.

image of collection

```
collection = ["apples", "bananas", "grapes"]

for loop_var in collection:
    print("hello")
    
    
```

Notice in this case, ```loop_var``` was defined but never used. It is common convention to use ```_``` in such a scenario:

```
collection = ["apples", "bananas", "grapes"]

for _ in collection:
    print("hello")
    
    
```

A ```range``` object could also be used to reproduce this.

```
for _ in range(0, 3, 1):
    print("hello")
    
    
```

And simplified to

```
for _ in range(3):
    print("hello")
    
    
```

A ```range``` object can be enumerated as seen before.

```
ro = range(0, 10, 2)
rol = list(ro)
roe = enumerate(ro)
roel = list(roe)
```

In this case, the loop variable ```loop_var``` is now a ```tuple``` with index 0 of the ```tuple``` being the index of the ```range``` object and index 1 of the ```tuple``` being the value of the ```range``` object. We can view this by printing a formatted string.

```
ro = range(0, 10, 2)
roe = enumerate(ro)

for loop_var in roe:
    print(f"idx {loop_var[0]}, val{loop_var[1]}")
    

```

The loop variable can also be explicitly specified as a tuple:

```
ro = range(0, 10, 2)
roe = enumerate(ro)

for (idx, val) in roe:
    print(f"idx {idx}, val{val]}")
    

```

Or implicitly, the parenthesis around the ```tuple``` can be dropped, using ```tuple``` unpacking.

```
ro = range(0, 10, 2)
roe = enumerate(ro)

for idx, val in roe:
    print(f"idx {idx}, val{val]}")
    

```

## if, elif, else

Code in the ```if``` code block is only implemented if the condition is ```True```

```
condition = True

if condition:
    print("Hello")
    
    
```

```
condition = False

if condition:
    print("Hello")
    
    
```

Code not belonging to the code block is implemented regardless of this condition.


```
condition = True

if condition:
    print("Inside Code Block")
    

print("Outside Code Block")
```

```
condition = False

if condition:
    print("Inside Code Block")
    

print("Outside Code Block")
```

A condition involving the conditional operators ```>```, ```>=```, ```==```, ```!=```, ```<``` and ```<=``` is normally expressed within the ```if``` statement, for example.

```
if (5>3):
    print("Inside Code Block")
    

print("Outside Code Block")
```

An ```if``` statement can be matched with an ```else``` statement which is carried out when the ```if``` statement is ```False```.

```
if (5>3):
    print("Hello")
else:
    print("Goodbye")


print("Outside")
```

```
if (5<3):
    print("Hello")
else:
    print("Goodbye")


print("Outside")
```