# Code Blocks

This tutorial will look at the use of code blocks in the Python programming language. Code blocks can be used to direct code in response to a condition, repeat an operation multiple times, or handle errors.

## Code Block Spacing

The code block has the following syntax.

```
statement:
    line of code
    line of code
    line of code


```

![img_001](./images/img_001.png)

The statement ends in a colon ```:``` which is used to indicate the beginning of a code block. 

![img_002](./images/img_002.png)

Each line of code belonging to the code block is indented by 4 spaces. Spaces are shown in the image below for clarity:

![img_003](./images/img_003.png)

Usually there are two blank lines left at the end of the code block to make it clear the code block has ended.

![img_004](./images/img_004.png)

```
statement:
    belong in block
    belong in block
    belong in block


outside block
outside block
```

Code blocks can included statements with nested code blocks. Anything belonging to a nested statement is indented twice using 8 spaces (4 spaces for the outer statement and another 4 spaces for the inner statement).

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

![img_005](./images/img_005.png)

## if, elif and else Code Blocks

### if Code Block

The ```if``` code block is carried out in response to a condition. Notice that the print statement is executed for a ```True``` condition:

```
condition = True

if condition:
    print('The condition was True')


```    

![img_006](./images/img_006.png)

When the condition is instead ```False```, the print statement is not executed and the contents of the code block are skipped:

```
condition = False

if condition:
    print('The condition was True')


``` 

![img_007](./images/img_007.png)

A print statement outside the code block can be added. This is carried out after the code block when the condition is ```True```:

```
condition = True

if condition:
    print('The condition was True')


print('Outside the Code Block')
```

![img_008](./images/img_008.png)

When the condition is ```False``` and the code block is skipped, only the print statement outside the code block is carried out:

```
condition = False

if condition:
    print('The condition was True')


print('Outside the Code Block')
```

![img_009](./images/img_009.png)

### Comparison Operators

The six comparison operators are:

|comparison operator|description|
|---|---|
|==|is equal to|
|!=|not equal|
|>|greater than|
|>=|greater than or equal to|
|<|less than|
|<=|less than or equal to|

The previous tutorials examined use of these comparison operators for text data types, numeric data types and collections.

A comparison operator is typically used to specify a condition:

```
condition = 5 > 3
condition

if condition:
    print('The condition was True')
    
    
```

![img_010](./images/img_010.png)

This can be shortened using:

```
if 5 > 3:
    print('The condition was True')
    
    
```    

![img_011](./images/img_011.png)

An ```if``` statement can be configured to examine multiple conditions through the use of the and ```&``` and or ```|``` operators. 

The ```&``` and ```|``` operators take precedence over the comparison operators ```==```, ```!=```, ```>```, ```>=```, ```<``` and ```<=```, so conditions are normally placed in parenthesis:

```
if (5 > 3) & ('a' < 'b'):
    print('The condition was True')
    
    
```

![img_012](./images/img_012.png)

If the parenthesis are removed, the operation ```3 & 'a'``` is attempted which gives a ```TypeError```:

![img_013](./images/img_013.png)

Other conditions can be added, using parenthesis appropriately:

```
if (((5 > 3) & ('a' > 'b')) | (4 == 3)):
    print('The condition was True')
    
    
```

![img_014](./images/img_014.png)

### else Code Block

It is common to setup a code block in response to a ```True``` condition and another code block in response to a ```False``` condition:

```
condition = False

if condition:
    print('The condition was True')
if not condition:
    print('The condition was False')


```

![img_015](./images/img_015.png)

This is typically done shorthand using an associated ```else``` code block:

```
condition = False

if condition:
    print('The condition was True')
else:
    print('The condition was False')

    
```

![img_016](./images/img_016.png)

### elif Code Block

If multiple ```if``` code blocks are used, they are each individually assessed and the ```else``` code block is only associated with the last ```if``` code block. When both conditions are ```True```, the print statements in both ```if``` code blocks are carried out:

```
if 10 > 3:
    print('10 is greater')
if 9 > 3:
    print('9 is greater')
else:
    print('These are not greater')
    
    
```

![img_017](./images/img_017.png)

When the first condition in the first ```if``` code block is ```True```, the print statement in the first code block is carried out. When the condition in the second ```if``` code block is ```False```, the print stement in the associated ```else``` code block is also carried out:

```
if 10 > 9:
    print('10 is greater')
if 9 > 9:
    print('9 is greater')
else:
    print('These are not greater')
    
    
```    

![img_018](./images/img_018.png)

It is common to instead setup a linked else if code block using ```elif```. When conditions are linked, only the **first** code block that has a ```True``` condition is executed. All subsequent code blocks are skipped, regardless if the condition is ```True``` or not, as in the case with the example below:

```
if 10 > 3:
    print('10 is greater')
elif 9 > 3:
    print('9 is greater')
else:
    print('These are not greater')
    
    
```   

![img_019](./images/img_019.png)

The ```else``` code block is linked to all the subsequent code blocks and is only carried out if all conditions specified are ```False```:

```
if 10 > 30:
    print('10 is greater')
elif 9 > 30:
    print('9 is greater')
else:
    print('These are not greater')
    
    
```   

![img_020](./images/img_020.png)

There can be multiple ```elif``` code blocks:

```
num = 2

if num == 0:
    print('zero')
elif num == 1:
    print('one')
elif num == 2:
    print('two')
else:
    print('num not zero, one or two')
    
    
```

![img_021](./images/img_021.png)

## match and case

When a series of code blocks are used to match a variable to ordinal values, like in the case above, it is better to use a ```match``` code block. Each condition in the ```match``` code block is a ```case``` and each ```case``` has its own nested code block. Notice the double indentation of code, indicating it belongs to the corresponding ```case``` code block which in turn belongs to the ```match``` code block. ```case _``` is used to represent any other value of the variable ```num```:

```
num = 2

match num:
    case 0:
        print('zero')
    case 1:
        print('one')
    case 2:
        print('two')
    case _:
        print('num not zero, one or two')
    
    
```

![img_022](./images/img_022.png)

Recall that characters are ordinal and therefore can also be used with ```match```. For example:

```
letter = 'c'

match letter:
    case 'a':
        print(ord('a'))
    case 'b':
        print(ord('b'))
    case 'c':
        print(ord('c'))
    case _:
        print("letter not 'a', 'b' or 'c'")
    

```    

![img_023](./images/img_023.png)

## Nested Code Blocks

The ```match``` code block is a demonstration of a nested code block. It is possible to nest other code blocks:

```
letter = 'a'
num = 1

if letter == 'a':
    if num == 0:
        print("letter == 'a', num == 0")
    elif num == 1:
        print("letter == 'a', num == 1")
    else:
        print("letter == 'a', num != 0")
else:
    print("letter != 'a'")

    
```    

![img_024](./images/img_024.png)

With too much nesting, the code often becomes hard to read. It is generally better to try and branch out the conditions using a single level with the and ```&``` and or ```|``` operators where possible:

```
letter = 'a'
num = 1

if (letter == 'a') & (num == 0):
    print("letter == 'a', num == 0")
elif (letter == 'a') & (num == 1):
    print("letter == 'a', num == 0")
else:
    print("letter != 'a'")    


```

![img_025](./images/img_025.png)

## with Code Block

If the following text file is created:

```
Baa, baa, black sheep,
Have you any wool?
Yes, sir, yes, sir,
Three bags full;
One for my master,
One for my dame,
And one for the little boy
Who lives down the lane.
```

And stored in the same folder as the interactive Python notebook file (or Python script file):

![img_026](./images/img_026.png)

Its contents including whitespace can be viewed in Notepad++:

![img_027](./images/img_027.png)

The file can be opened using the ```open``` function:

![img_028](./images/img_028.png)

The ```open``` function requires a file which can be specified directly when it is in the same folder as the interactive Python notebook file (or Python script file).

The ```mode``` keyword input argument can be specified using a single letter:

|mode|definition|
|---|---|
|'r'|open an existing file and read existing content|
|'w'|open an existing file and write over existing content|
|'a'|open an existing file and append new content|
|'x'|create a new file and write new content|

A second letter can also be used for the encoding. The encoding can be ```'t'``` text (default) which is also known as ```UTF-8``` or ```'b'``` binary which is known as ```'ASCII'```. 

```mode=rt``` for example is the default which reads a text file encoded as text ('ASCII'). 

For other encoding schemes, the ```encoding``` keyword argument is seperately used. For a CSV file created in Microsoft Excel, the ```'UTF-8-Sig'``` encoding needs to be used to properly handle the BOM. The other encoding schemes available were previously discussed in the text data types tutorial. 

|encoding|bit|bytes|byte order|BOM|
|---|---|---|---|---|
|'ASCII'|1|8| |---|
|'Latin1'|1|8| | |
|'UTF-16-LE'|2|16|little endian| |
|'UTF-16-BE'|2|16|big endian| |
|'UTF-16'|2|16| |BOM|
|'UTF-32-LE'|4|32|little endian| |
|'UTF-32-BE'|4|32|big endian| |
|'UTF-32'|4|32| |BOM|
|'UTF-8'|1-4|adaptive|1-4 adaptive| |
|'UTF-8-Sig'|1-4|adaptive|1-4 adaptive|BOM|

The ```newline``` keyword input argument can be used to specify the character that is used to represent a new line. in the example above a carriage return and line feed were shown in Notepad++. In Python the escape characters ```\r\n``` are used to represent this which is the default.

The file can be opened using:

```
file_object = open('text.txt', mode='rt')
file_object
```

![img_029](./images/img_029.png)

A number of identifiers are available from the ```file_object``` and can be viewed by inputting ```file_object.``` followed by a tab ```↹```:

![img_030](./images/img_030.png)

In the example above the mode is set for reading, so ```readline``` can be used to read an individual line and return it as a ```str``` or ```readlines``` can be used to read all lines and return a ```list``` of lines. i.e. each item in the list is a ```str``` corresponding to the line:

```
file_object.readline()
file_object.readlines()
```

![img_031](./images/img_031.png)

Once a file has been worked with, it should be closed:

```
file_object.close()
```

![img_032](./images/img_032.png)

This will release the physical file from Python, allowing it to be used by other programs in Windows. The ```file_object``` will still present in Python but no longer associated to the physical file. If the directory function ```dir``` is used a number of data model identifiers can also be viewed:

```
dir(file_object)
```

![img_033](./images/img_033.png)

There are two data model identifiers of particular interest ```__enter__``` and ```__exit__``` which means the ```file_object``` can be entered and exited using a context manager. 

The context manager is essentially a code block, ```with``` is used to create the code block and has an associated colon ```:```. Instead of assignment to a variable using the assignment operator ```=```, the ```as``` keyword is used. The operations above with a context manager are:

```
with open('text.txt', mode='rt') as file_object:
    first_line = file_object.readline()
    remaining_lines = file_object.readlines()


first_line
remaining_lines    
```

![img_034](./images/img_034.png)

The use of the ```with``` context manager opens, the physical file within the code block using the data model method ```__enter__``` and when the code block ends uses the data model method ```__exit__``` to release the physical file. This prevents a file from being opened in Python and not properly closed and the code is a bit cleaner to read grouping all the operations with that file together.

## The for Loop

The ```for``` loop can be used to carry out operations within a code block *for* a specified number of times.

### Iterator

The for loop requires an iterator which comes from a collection. The following ```str``` can be used to examine the mechanics behind a ```for``` loop:

```
word = 'hello'
'h' in 'hello'
```

![img_035](./images/img_035.png)

The data model identifiers can be viewed using:

```
dir(word)
```

![img_036](./images/img_036.png)

Recall that use of ```in``` in the context above, uses the data model identifier ```__contains__```. There is also the ```__iter__``` data model method which can be used to create an iterator and the ```__len__``` data model method which specifies the number of Unicode characters in the Unicode string.

An iterator can be created using:

```
letter = iter(word)
letter
```

![img_037](./images/img_037.png)

The ```next``` keyword can be used until the iterator is exhausted:

```
next(letter)
next(letter)
next(letter)
next(letter)
next(letter)
```

![img_038](./images/img_038.png)

If the iterator is exhausted, a ```StopIteration``` error displays:

```
next(letter)
```

![img_039](./images/img_039.png)

Recall to exhaust the iterator, ```next``` is called 5 times, which matches the length of the ```word```:

```
len(word)
```

![img_040](./images/img_040.png)

The ```word``` can also be cast into a ```tuple``` and viewed on the Variable Explorer:

```
word_t = tuple(word)
```

![img_041](./images/img_041.png)

![img_042](./images/img_042.png)

![img_043](./images/img_043.png)

If the directory function ```dir``` is used on ```word_t```:

```
dir(word_t)
```

![img_044](./images/img_044.png)

Notice there are also the data model methods ```__contains__```, ```__iter__``` and ```__len__```. This means an iterator can be created. This iterator is a ```tuple``` iterator, where each item can be a Python object. Since this ```tuple``` was cast from a ```str``` each Python object is a one character Unicode ```str```:

```
letter_t = iter(word_t)
letter_t
```

![img_045](./images/img_045.png)

Therefore the following behaves similarly:

```
next(letter_t)
next(letter_t)
next(letter_t)
next(letter_t)
next(letter_t)
```

![img_046](./images/img_046.png)

A ```list``` which is essentially a mutable ```tuple``` behaves similarly. 

The ```word``` can also be cast into a ```set``` and viewed on the Variable Explorer:

```
word_s = set(word)
```

![img_047](./images/img_047.png)

![img_048](./images/img_048.png)

![img_049](./images/img_049.png)

A ```set``` only contains unique values and is not ordered. If the directory function ```dir``` is used on ```word_s```:

```
dir(word_s)
```

![img_050](./images/img_050.png)

The data model methods ```__contains__```, ```__iter__``` and ```__len__``` are still available. An iterator can be created:

```
letter_s = iter(word_s)
letter_s
```

![img_051](./images/img_051.png)

```
next(letter_s)
next(letter_s)
next(letter_s)
next(letter_s)
```

![img_052](./images/img_052.png)

### Iterating using a for Loop

A ```for``` loop can be used to loop over each letter in each of the collections above. Returning to the Unicode string for example:

```
word = 'hello'

for letter in word:
    print(letter)
    
    
```

![img_053](./images/img_053.png)

Under the hood, the ```for``` loop uses the ```__contains__```, ```__iter__``` and ```__len__``` data model methods to loop over each Unicode character in the string ```word```. 

```letter``` is a loop variable which can be accessed in the loop and can be renamed using any variable name. When the variable is not referenced in the ```for``` loop, it is called ```_```. For example:

```
for _ in word:
    print(word)
    
    
```

![img_054](./images/img_054.png)

Notice that ```hello``` is printed out 5 times, because it has a length of 5.

Another example can be given using qa ```tuple``` which recall can be conceptualised as an archive of records:

```
archive = (0, True, 3.14, 'hello')

for record in archive:
    print(record)
    
    
```

![img_055](./images/img_055.png)

It is somewhat common to use a plural term for the collection being looped over and a singular term for the loop variable:

```
records = (0, True, 3.14, 'hello')

for record in records:
    print(record)
    
    
```

![img_056](./images/img_056.png)

### Mutability Issues

Mutable methods such as the ```list``` method ```append``` are commonly used within ```for``` loops. 

Care should be taken not to use a ```for``` loop to iterate over the mutable sequence itself, while mutating the same sequence, as an infinite loop can occur. For example:

```
active = [0, True, 3.14, 'hello']

for record in active:
    active.append('bye')
    
    
```

![img_057](./images/img_057.png)

To exit an infinite loop, use the keyboard shortcut ```Ctrl``` + ```c```.

Instead a copy of the mutable sequence can be made to loop over, for example: 

```
active = [0, True, 3.14, 'hello']

for record in active.copy():
    active.append('bye')
    

active    
```   

![img_058](./images/img_058.png)

### The range class

A ```range``` object is commonly used within a loop. For example:

```
active = [0, True, 3.14, 'hello']

for num in range(len(active)):
    active.append('bye')
    
    
active
```

![img_059](./images/img_059.png)

This essentially gives access to the numeric index of the Unicode string being looped over:

```
active = [0, True, 3.14, 'hello']

for num in range(len(active)):
    active.append('bye')
    print(num, active)
    
    
```

![img_060](./images/img_060.png)

This can be used for the purposes of indexing:

```
word = 'hello'

for num in range(len(word)):
    print(word[num])


```

![img_061](./images/img_061.png)

Note that the above is not as readible as:

```
word = 'hello'

for letter in word:
    print(letter)


```

![img_062](./images/img_062.png)

Howeveer having access to the index is sometimes useful for other purposes. For example string replication can be carried out using multiplication of the index:

```
word = 'hello'

for num in range(len(word)):
    print(num * word[num])


```

![img_063](./images/img_063.png)

Or alternatively the index can be printed alongside the character:

```
word = 'hello'

for num in range(len(word)):
    print(num, word[num])


```

![img_064](./images/img_064.png)

A ```range``` object has been created from the length of a collection. The docstring of the init signature of the ```range``` class can be examined by inputting ```range()``` and pressing shift ```⇧``` and tab ```↹```:

![img_065](./images/img_065.png)

A ```range``` object uses zero-order indexing and increments in integer steps of ```1``` up to but excluding the integer ```stop``` value. It has consistency to the ```slice``` object which was examined when indexing collections. If only an integer ```stop``` value is specified:

```
ro = range(5)
ro
```

![img_066](./images/img_066.png)

The integer ```start``` will assumed to be ```0```. The range object ```ro``` can be cast into a ```tuple``` and examined in the Variable Explorer:

```
ro_t = tuple(ro)
```

![img_067](./images/img_067.png)

![img_068](./images/img_068.png)

Notice in this scenario, the index and value of the ```tuple``` match:

![img_069](./images/img_069.png)

If a non-zero ```start``` value is also supplied. For example:

```
ro = range(1, 5)
ro
ro_t = tuple(ro)
```

![img_070](./images/img_070.png)

![img_071](./images/img_071.png)

Notice in this scenario, the index and value of the ```tuple``` do not match:

![img_072](./images/img_072.png)

Finally an integer ```step``` can be specified. When an integer ```step``` is specified, the integer ```start``` needs to also be specified even if it is ```0```:

```
ro = range(0, 6, 2)
ro
ro_t = tuple(ro)
```

![img_073](./images/img_073.png)

![img_074](./images/img_074.png)

Notice that once again zero-order indexing is used, going up to but not including the ```stop``` value of ```6```:

![img_075](./images/img_075.png)

Zero-order indexing needs to be addressed when using negative values. For example beginning at a negative value and counting up until ````0``` requires a ```stop``` value ```1``` past ```0``` which is ```1```:

```
ro = range(-5, 1, 1)
ro
ro_t = tuple(ro)
```

![img_076](./images/img_076.png)

![img_077](./images/img_077.png)

![img_078](./images/img_078.png)


Or using a negative step of ```-1``` to count down from a positive integer value to ```0```, requires a ```stop``` value ```-1``` past ```0``` which is ```-1```:

```
ro = range(5, -1, -1)
ro
ro_t = tuple(ro)
```

![img_079](./images/img_079.png)

![img_080](./images/img_080.png)

![img_081](./images/img_081.png)

To check your understanding, create the following ```range``` objects:

![img_082](./images/img_082.png)

![img_083](./images/img_083.png)

### Dictionary Keys

Recall that a dictionary has the form:

```
mapping = {'red': '#FF0000', 
           'green': '#00B050', 
           'blue': '#0070C0'}
```

![img_084](./images/img_084.png)

This can be viewed in the Variable Explorer. Recall that a dictionary has keys mapped to values:

![img_085](./images/img_085.png)

![img_086](./images/img_086.png)

The data model identifiers can be viewed using:

```
dir(mapping)
```

![img_087](./images/img_087.png)

Notice the data model identifiers ```__contains__```, ```__iter__``` and ```__len__```. If an iterator is created from a dictionary, it examines the keys:

```
keys = iter(mapping)
keys
next(keys)
next(keys)
next(keys)
```

![img_088](./images/img_088.png)

This means that using a ```for``` loop on a dictionary iterates over the keys:

```
for key in mapping:
    print(key)
    
    
```

![img_089](./images/img_089.png)

Recall that the value can be retrieved via indexing with the key.

```
for key in mapping:
    print(mapping[key])
    
    
```

![img_090](./images/img_090.png)

Recall that the dictionary has the three identifiers ```keys```, ```values``` and ```items```:

```
mapping.keys()
mapping.values()
mapping.items()
```

![img_091](./images/img_091.png)

These are all iterable. ```keys``` are not normally explicitly used as it is the same as iterating using a dicitonary directly:

```
for key in mapping.keys():
    print(key)
    
    
```

![img_092](./images/img_092.png)

```values``` are also not normally explicitly used as it is relatively easy to index into the dictionary using a key as seen before:

```
for value in mapping.values():
    print(value)
    
    
```

![img_093](./images/img_093.png)

Each item in ```items``` is a ```tuple``` of the form ```(key, value)```. This ```tuple``` can be accessed:

```
for (key, value) in mapping.items():
    print(key, value)
    
    
```

![img_094](./images/img_094.png)

This is normally simplified using ```tuple``` unpacking:

```
for key, value in mapping.items():
    print(key, value)
    
    
```

![img_095](./images/img_095.png)

### The enumerate class

Using the dictionary identifier ```items``` gives an iterable that cotnains a ```tuple``` of the form ```(key, value)```:

![img_096](./images/img_096.png)

For another collection such as the string ```word``` which was ```'hello'``` a numeric index is used opposed to a key and the value is the corresponding Unicode character. This was seen in more detail when this was cast to the tuple ```word_t```:

![img_097](./images/img_097.png)

Using ```range``` on the length of the collection, gave a ```range``` object that was associated with the numeric index. This was examined earlier and it was seen, that the value could be retrieved by indexing into the collection.

To get both the index and value however, an ```enumerate``` object can be created:

```
word_t = tuple('hello')
enumerate(word_t)
```

![img_098](./images/img_098.png)

If this ```enumerate``` object is cast into a ```list```, notice that it has a similar form to the dictionary ```items```.

```
list(enumerate(word_t))
mapping.items()
```

![img_099](./images/img_099.png)

Casting into a ```list``` opposed to a ```tuple``` clearly distinguishes the inner and outer brackets.

The ```enumerate``` object can be looped over to get the index and the value at the index, analogously to the key and the value at the key for a dictionary:

```
word = 'hello'

for index, letter in enumerate(word):
    print(index, letter)
    
    
```

![img_100](./images/img_100.png)

## The while Loop

The ```while``` loop can be conceptualised as an ```if``` code block that is continually repeated *while* a condition is ```True```. Note when the condition is never updated in the code block, the ```while``` loop will never exit resulting in an infinite loop. 



















The mechanism of a for loop can be examined in more detail using the debugger in the JupyterLab IDE:

![103_img](./images/103_img.png)

To begin, select view and show line numbers:

![104_img](./images/104_img.png)

Select the debugger:

![105_img](./images/105_img.png)

Open the debug tab to the right:

![106_img](./images/106_img.png)

Click the lower and upper line numbers to debug between:

![107_img](./images/107_img.png)

Select run:

![108_img](./images/108_img.png)

To the right under callstack is the option to step through the code:

![109_img](./images/109_img.png)

Notice that the list ```fruits``` is instantiated. Stepping through goes to the for loop statement.

![110_img](./images/110_img.png)

In the for loop statement, ```fruits``` can be considered as an iterator and ```fruit``` can be considered as the current value returned from the iterator which is ```"apples"```. Conceptualise behind the scenes, ```next``` being applied to the iterator. Stepping through goes to the ```print``` statement within the code block:

![111_img](./images/111_img.png)

This value ```fruit``` which is ```"apples"``` is printed:

![112_img](./images/112_img.png)

As the iterator still has remaining values, the debugger revisits the for statement at the beginning of the code block. ```fruit``` is reassigned to the value ```"bananas"```. Once again behind the scenes conceptualise  ```next``` being called on the iterator. 

![113_img](./images/113_img.png)

Continuing to step through will take the debugger to the ```print``` statement and then back up to the for statement and then to the ```print``` statement before finally exiting the for loop as the iterator is exhausted and has no values left.

Instead of printing the loop variable, a constant ```hello``` can be printed. This constant ```"hello"``` is printed for each value of the iterator (irrespective of what the value itself is) at index 0, 1 and 2.

![033_for_loop](./images/033_for_loop.png)

```
collection = ["apples", "bananas", "grapes"]

for loop_var in collection:
    print("hello")
    
    
```

![048_for_loop](./images/048_for_loop.png)

Notice in this case, ```loop_var``` was defined but never used. Some IDEs will flag this up as a problem. It is a common convention to use ```_``` in such a scenario:

```
collection = ["apples", "bananas", "grapes"]

for _ in collection:
    print("hello")
    
    
```

![049_for_loop](./images/049_for_loop.png)

A range object would be better suited to reproduce printing the static string ```"hello"``` three times:

```
for _ in range(0, 3, 1):
    print("hello")
    
    
```

![050_for_loop](./images/050_for_loop.png)

And simplified to

```
for _ in range(3):
    print("hello")
    
    
```

![051_for_loop](./images/051_for_loop.png)

A range object with a step size of 2 can be enumerated:

```
ro = range(0, 10, 2)
rol = list(ro)
roe = enumerate(ro)
roel = list(roe)
```

![052_for_loop](./images/052_for_loop.png)

In this case, the loop variable ```loop_var``` is now a tuple with index 0 of the tuple being the index of the range object and index 1 of the tuple being the value of the range object. 

![053_for_loop](./images/053_for_loop.png)

Each components of this tuple can be included within a formatted string and the print statement for this formatted string can be placed within the body of the for loop.

```
ro = range(0, 10, 2)
roe = enumerate(ro)

for loop_var in roe:
    print(f"idx {loop_var[0]}, val {loop_var[1]}")
    

```

![054_for_loop](./images/054_for_loop.png)

The loop variable can also be explicitly specified as a tuple:

```
ro = range(0, 10, 2)
roe = enumerate(ro)

for (idx, val) in roe:
    print(f"idx {idx}, val {val}")
    

```

![055_for_loop](./images/055_for_loop.png)

Or implicitly, the parenthesis around the tuple can be dropped (known as tuple unpacking).

```
ro = range(0, 10, 2)
roe = enumerate(ro)

for idx, val in roe:
    print(f"idx {idx}, val {val}")
    

```

![056_for_loop](./images/056_for_loop.png)

## if, elif, else

A number of code blocks can be made in response to a single condition.

|Code Block|Purpose|
|---|---|
|if|Code block is carried out if condition is True|
|else|Code block is carried out elsewise i.e. when the condition is False|

Or setup in response to multiple conditions.

|Code Block|Purpose|
|---|---|
|if|Code block is carried out if the first condition is True|
|elif|Code block is carried out if the first condition is False and the second condition is True|
|elif|Code block is carried out if the first and the second conditions are False and the third condition is True|
|elif...|Each additional elif code block is carried out if all previous conditions are False and the current condition is True|
|else|Code block is carried out elsewise i.e. all conditions above are False|


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

![057_if](./images/057_if.png)

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

![058_if](./images/058_if.png)

A condition involving the conditional operators ```>```, ```>=```, ```==```, ```!=```, ```<``` and ```<=``` is normally expressed within the ```if``` statement, enclosed in parenthesis, for example.

```
if (5>3):
    print("Inside Code Block")
    

print("Outside Code Block")
```

![059_if](./images/059_if.png)

An ```if``` statement can be matched with an ```else``` statement which is carried out when the ```if``` statement is ```False```.

```
condition = True
if condition:
    print("Do something")
else:
    print("Do something else")


print("Outside")
```

```
condition = False
if condition:
    print("Do something")
else:
    print("Do something else")


print("Outside")
```

![060_if](./images/060_if.png)

A series of linked conditions can be setup using the ```if```, ```elif``` (else if), ..., ```else```. In this case when ```num``` is 5, all the conditions are False so the else code block is executed:

```
num = 5

if (num>10):
    print("num is greater than 10")
elif (num>5):
    print("num is greater than 5")
else:
    print("num is lower than 5")

    
```

![061_if](./images/061_if.png)

In this case, when ```num``` is 8, the if condition is False and the elif condition is True so the elif code block is executed:

```
num = 8

if (num>10):
    print("num is greater than 10")
elif (num>5):
    print("num is greater than 5")
else:
    print("num is lower than 5")

    
```

![062_if](./images/062_if.png)

In the case where ```num``` is 100, the if condition is True and the if code block is executed. Because the if code block was executed, all subsequent code blocks below it are ignored. The elif code block is not executed despite this condition also being True. 

```
num = 100

if (num>10):
    print("num is greater than 10")
elif (num>5):
    print("num is greater than 5")
else:
    print("num is lower than 5")

    
```

![063_if](./images/063_if.png)

In order to execute the code blocks from both conditions, seperate unlinked if statements would need to instead be used.

```
num = 100

if (num>10):
    print("num is greater than 10")
    
    
if (num>5):
    print("num is greater than 5")
    
    
```

![064_if](./images/064_if.png)

Multiple ```elif``` code blocks can be used. In this example, the ```if``` condition is False and the associated code block is ignored. Next the first ```elif``` condition is True so the code block belonging it is executed. All other code blocks are ignored as a linked code block is already executed.

```
num = 9

if (num>10):
    print("num is greater than 10")
elif (num>8):
    print("num is greater than 8")
elif (num>7):
    print("num is greater than 7")
elif (num>5):
    print("num is greater than 5")
else:
    print("num is lower than 5")

    
```

![065_if](./images/065_if.png)

## match, case

An ```if```, multiple ```elif``` and an ```else``` code block can be setup to respond to a number of discrete values of a variable as shown. In this case as ```num``` is 1, the ```elif``` code block is executed.

```
num = 1

if (num==0):
    print("num is zero")
elif (num==1):
    print("num is one")
elif (num==2):
    print("num is two")
else:
   print("num is not zero, one or two")


```

![066_if](./images/066_if.png)

It is however more clean to use an outer code block to ```match``` the variable and provide associated code blocks for each discrete ```case``` of possible variables. Since ```num``` is 1, ```case``` 1 is True and so only this code block is executed.

```
num = 1

match num:
    case 0:
        print("num is zero")
    case 1:
        print("num is one")
    case 2:
        print("num is two")
    case _:
        print("num is not zero, one or two")


```

![067_if](./images/067_if.png)

In the following example ```num``` is 9, and none of the above cases outlined are True, so the code in the case ```_``` code block is executed.

```
num = 9

match num:
    case 0:
        print("num is zero")
    case 1:
        print("num is one")
    case 2:
        print("num is two")
    case _:
        print("num is not zero, one or two")


```

![068_if](./images/068_if.png)

## while loops

The code in an ```if``` code block only runs once if a condition is True. A ```while``` loop is similar to an ```if``` code block and the code in the code block will be executed when the condition is True. After the code block is executed however, the condition will be rechecked and the code block will run again if the condition is True. This will continue ```while``` the condition is True, until the condition is updated to be False. 

If the condition is never False, the loop will run forever and may hang the Python Kernel.

```
while True:
    print("spam my console")
    
    
```

![069_while](./images/069_while.png)

Notice that the output of the cell continues indefinitely and the kernel gets hung on the cell output. The kernel typically needs to be restarted to exit out of the ```while``` loop.

|Code Block|Purpose|
|---|---|
|for|Code block is carried out for each item in a known sequence|
|while|Code block is carried out while a condition is True|

```while``` loops are typically invoked when interacting with hardware. For example a bathroom light might be instructed to turn on in respond to the reading from a Near-Infrared motion sensor. In this example there is no set sequence or specified period of time until someone walks until the bathroom, making it unviable to work with only a ```for``` loop.

```for``` loops are instead preferred when working over a known timeframe or sequence within a known collection. 

Although there is a preference to use a ```for``` loop or a ```while``` loop, the ```while``` loop can be used in place of the ```for``` loop for all circumstances however the ```for``` loop cannot replace the ```while``` loop with an unknown sequence or timeframe. To understand how to use a ```while``` loop it is useful to recreate some of the ```for``` loops used above with a ```while``` loop.

![033_for_loop](./images/033_for_loop.png)

Starting out with the simple ```for``` loop which prints out the value of each item in the collection.

```
collection = ["apples", "bananas", "grapes"]
for loop_var in collection:
    print(loop_var)
    
    
```

![070_while](./images/070_while.png)

The ```for``` loop will instead be updated to use a range object. In this case the stop value is ```len(collection)``` and the range object can be specified as ```range(0, len(collection), 1)``` or abbreviated as ```range(len(collection))```. The for loop has more cumbersome syntax but works as expected.

```
collection = ["apples", "bananas", "grapes"]
for loop_idx in range(len(collection)):
    print(collection[loop_idx])
    
    
```

![071_while](./images/071_while.png)

For a ```while``` loop, a condition must be established. This condition typically involves a variable that must be defined before using the ```while``` loop. In this case, the variable is called ```loop_idx``` and is assigned to an initial value of 0. The condition of the ```while``` loop setup is that this variable ```loop_idx``` is less than the length of the collection ```len(collection)```. 

If there is no change made in the ```while``` loop involving ```loop_idx``` or the ```len(collection)```, the ```while``` loop will run forever. So the last line in the code block will increment ```loop_idx```. The string in the collection at the current index can be printed by indexing using ```loop_idx```, for clarity both the index and value will be printed. This syntax is more cumbersome but yields similar results to the ```for``` loop.

```
collection = ["apples", "bananas", "grapes"]

loop_idx = 0

while (loop_idx < len(collection)):
    print(f"loop_idx {loop_idx}, {collection[loop_idx]}")
    loop_idx += 1
    
    
```

![072_while](./images/072_while.png)


Notice that the final value of ```loop_idx``` is 3, meaning the condition is the ```while``` loop is False and therefore the code block is not executed for a 4th time and the code block is exited.

![073_while](./images/073_while.png)

## try, except, else, finally

Earlier we seen the use of if, elif and else statements to carry out different code blocks in response to a condition or conditions. In Python we have a similar structure setup for handling errors.

|Code Block|Purpose|
|---|---|
|try|This code block will test the code for an expected error|
|except|This code block will be used to handle an error type|
|else|This code block will be used elsewise when there is no error|
|finally|This code block is carried out regardless if there is an error or not|

If the variable number is created and assigned to a string. Casting will work, if the string is recognised as numeric.

```
number = "5"
float(number)
```

![074_try](./images/074_try.png)

However a "ValueError" will be given when the string is not recognised as numeric.

```
number = "five"
float(number)
```

![075_try](./images/075_try.png)

The following code blocks can be setup in response to the ```number``` variable above. Normally these would be setup with a function and the variable ```number``` would be an input argument of the function. However for clarity these are shown outwith a function and functions will be discussed in the next tutorial.

```
try:
    float(number)
except ValueError:
    print("invalid number, number set to 0")
    number = 0
else:
    number = float(number)
finally:
    value = number + 1
```

When the ```try``` code block does not find an error, the code in the ```else``` code block and the ```finally``` code blocks are carried out.

![076_try](./images/076_try.png)

When the ```try``` code block does find a ```ValueError```, the code in the ```except ValueError``` code block and the ```finally``` code blocks are carried out.

![077_try](./images/077_try.png)

[Home Python Tutorials](https://github.com/PhilipYip1988/python-tutorials/blob/main/readme.md)
