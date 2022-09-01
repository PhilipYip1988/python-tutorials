# Collections

## Fundamental Datatypes

So far we have explored the following fundamental datatypes:

* text datatypes
    * str ("a", "hello world")
* numeric datatypes
    * int (0, 1, 2, 3, ...)
    * bool (False, True)
    * float (0.0, 0., 0.1, 3.14)

## The string collection

We have discussed in Python how a string can be regarded as both a fundamental datatype and also a collection of individual characters. In other words an individual character in Python is classified as a string. Let's explore some of the collection characteristics a string has:

### Concatenation

In the string collection the ```+``` operator performs concatenation of the two string collections and this differs for fundamental numeric datatypes where the ```+``` operator performs numeric addition:

```
word1 = "hello"
word2 = "world"
word1 + word2
```

```
num1 = 1
num2 = 2
num1 + num2
```

### Indexing

We have also discussed how we can index from a string using square brackets enclosing an integer value:

```
"hello"[1]
```

In the above example, the letter ```"e"``` is returned which is at index 1.

If you expected ```"h"```, recall that Python indexing uses zero order which is inclusive of ```0```:

```
"hello"[0]
```

Python zero order indexing is exclusive of the upper bound, which is the length of the string. We go up to but don't include the upper bound:

```
"hello"[len("hello")]
```

```
"hello"[len("hello") - 1]
```

To recap, in Pythons zero order indexing, the first value is at index 0 and the last value is at the length of the string minus one:

```
"hello"[0]
```

```
"hello"[len("hello") - 1]
```

We can also index using negative index values. When using a negative index we can think of the string as being a rolled up object. 

For example instead of viewing the string ```"hello"``` as a line:

```
hello
```

We can view it as:

```

     h
o         e
          
   l   l
   
```

Which has the positive indexes:

```

     [0]
[4]       [1]
          
  [3]   [2]
   
```

In this rolled up view, we have only explored the clockwise motion from the initial value ```0```, we can also explore the anti-clockwise motion using negative indexes. The integer number before ```0``` is ```-1```:

```

      [0]
[-1]       [-4]
          
  [-2]   [-3]
   
```

The initial value ```0``` can also be expressed as a negative index, which is the negative value of the length of the string:

```

      [-5]
[-1]       [-4]
          
  [-2]   [-3]
   
```

So we can get the last value and the first value using the negative indexes:

```
"hello"[-1]
```

```
"hello"[-len("hello")]
```

We can index using a slice. In full a slice uses the following notation:

```
"hello"[start:stop:step]
```

Because zero-order indexing is used, we are inclusive of the start bound and inclusive of the stop bound:

```
"hello"[1:3:1]
```

so this means we start at the letter at index 1 which is ```"e"``` and we go up in steps of one, taking us to index 2 which has the letter ```"l"```. We go up to the stop index 3 but we do not include it. Therefore this slice is ```"el"``` and not ```"ell"```.

Indexing has default values:

```
"hello"[start:stop:step]
```

The ```start``` has a default value that is ```0```, the ```stop``` has a default value that is the length of the string and the ```step``` has a default value of ```1```. Explicitly specifying these will return the complete string:

```
"hello"[0:len("hello"):1]
```

If we don't specify the step, a default value of 1 is selected, returning the whole string:

```
"hello"[0:len("hello"):]
```

This also works if we don't supply the second colon:

```
"hello"[0:len("hello")]
```

Example using the default value of ```stop```:

```
"hello"[0:]
```

```
"hello"[1:]
```

Example using the default value of ```start```:

```
"hello"[:len("hello")]
```

```
"hello"[:3]
```

Example using the default value of ```start```, ```stop``` and ```step```:

```
"hello"[:]
```

```
"hello"[::]
```

We can take every second value of the string using a ```step``` of ```2```:

```
"hello"[::2]
```

Since we ```start``` at ```0```, this selects all the even indexs. If we instead want all the odd indexes, we can start at ```1```:

```
"hello"[1::2]
```

We can get the string in reverse by specifying a step size of ```-1```:

```
"hello"[::-1]
```

When using a step of ```-1```, the ```start``` takes on a default value of ```-1``` and the ```stop``` takes on a default values of - the length of the string minus 1:

```
"hello"[-1:-len("hello")-1:-1]
```

Care needs to be taken when using the negative index as we are still inclusive of the ```start``` bound and exclusive of the ```stop``` bound.

## The list collection

A list can be used to store a collection of fundamental datatypes. The list has the following features:

* It is enclosed in square brackets ```[ ]```.
* It uses the comma ```,``` as a delimiter between each element (fundamental datatype) in the list.

The list can be visualised as a shopping list of singular items:

```
shopping_list = ["apples", "bananas", "cheese"]
```

Note however that when inteer numbers are used to muliply inividual strings, that string replication occurs:

```
shopping_list = ["apples", 2*"bananas", "cheese"]
```

Duplicates can however manually be added to a list:

```
shopping_list = ["apples", "bananas", "bananas", "cheese"]
```

The list can include numbers:

```
numbers = [1, 2, 3]
```

The list can also contain a mixture of fundamental datatypes:

```
items = [1, "apples", 3.14]
```

A list can also include other lists:

```
outer_list = [1, numbers, items]
```

In the example above numbers and items are nested lists. This can be input directly using:

```
outer_list = [1, [1, 2, 3], [1, "apples", 3.14]]
```

Care should be taken to ensure that the square brackets inner and outer brackets match up appropriately. When a bracket is selected the JupyterLab IDE will automatically highlight what it determines to be the corresponding bracket.














