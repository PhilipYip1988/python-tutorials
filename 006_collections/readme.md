# Collections

## Recap: Fundamental Data Types

The following fundamental datatypes have been explored:

* text datatypes
    * str ("a", "hello world")
* numeric datatypes
    * int (0, 1, 2, 3, ...)
    * bool (False, True)
    * float (0.0, 0., 0.1, 3.14)

## The string class

A string with multiple characters, a string with an individual character and a string with no characters all belong to the ```str``` class. 

```
greeting = "hello"
letter_h = "h"
empty = ""
```

![img_001](./images/img_001.png)

Therefore, the string class is both regarded as a fundamental datatype and a collection of characters.

![img_002](./images/img_002.png)

The ```dir``` function can be used to inspect the directory of a string instance. The two datamodel methods ```__len__``` and ```__iter__``` show. The datamodel method ```__len__``` is not typically used directly. Instead the inbuilt function ```len``` is used and returns the length of a collection.

![img_003](./images/img_003.png)

Any object that has the datamodel method ```__iter__``` is iterable. Recall the string ```greeting``` can be conceptualised as being five individual characters, with a length of 5 and each character having an integer index of 0 (inclusive) to 5 (exclusive):

![img_004](./images/img_004.png)

The datamodel method ```__getitem__``` can be used to return an item using the numeric index of th item.

![img_005](./images/img_005.png)


This datamodel method is typically not used directly and maps to the use of square brackets ```[ ]``` for indexing. Where the square brackets enclose the integer index. An ```IndexError``` occurs when out of range. In this case the length of the string is out of range because Python uses zero-order indexing. Zero-order indexing is inclusive of the lower bound, in this case 0 and exclusive of the upper bound, in this case the length of the string.

```
greeting = "hello"
greeting.__getitem__(0)
greeting[0]
greeting[3]
greeting[4]
greeting[5]
```

![img_006](./images/img_006.png)

The ```__add__``` and ```__mul__``` datamodel methods map to the ```+``` operator and the ```*``` operator. In the case of an inbuilt collection ```+``` performs concatenation of two instances of that collection and ```*``` can be used with an instance of the collection and an integer to replicate the collection.

```
"hello" + "world"
"hello" * 3
```

![img_007](./images/img_007.png)

```__add__``` and ```__mul__``` are defined completely differently for numeric datatypes and perform arithmatic in such cases.

The string ```"hello"``` can be conceptualised as a line:

```
hello
```

It can then be conceptualised as being rolled up:

```

     h
o         e
          
   l   l
   
```

Going clockwise from the starting point 0, the positive integer index values can be seen:

```

     [0]
[4]       [1]
          
  [3]   [2]
   
```

Anti-clockwise motion can also be explored using negative indexes. The integer number before ```0``` is ```-1```:

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

The last value and the first value can be accessed using the negative integer index values:

```
"hello"[-1]
```

```
"hello"[-len("hello")]
```

![img_008](./images/img_008.png)

Indexing can also be carried out using a slice. The ```slice``` function can be used to create a slice object which can be used to obtain the character at multiple indexes.

![img_009](./images/img_009.png)

There is the option of 1, 2 or 3 positional input arguments. If only 1 is specified, slicing will occur from an index of 0 to the specified upper index bound using an index step size of 1. 

```
"hello"[slice(3)]
```

If 2 are specifed, slicing will occur from the specified lower index bound to the specified upper index bound using an index step size of 1.

```
"hello"[slice(1, 3)]
```

If 3 are specifed, slicing will occur from the specified lower index bound to the specified upper index bound using the specified index step size.

```
"hello"[slice(1, 5, 2)]
```

![img_010](./images/img_010.png)

Instead of indexing using the slice function. It is more common to slice using colons. This has the form:

```
string[start:stop:step]
```

For example:

![img_002](./images/img_002.png)

```
"hello"[0:3:1]
```

![img_011](./images/img_011.png)

Recall that Python uses zero-order indexing. In this case, the slice is from a start bound of 0 (inclusive) to a stop bound of 3 (exclusive) in steps of 1. This gives ```"hel"``` (index 0, 1 and 2 going up to 3 but not including 3).

By default the index step is 1, so the following abbreviation is also equivalent:

```
"hello"[0:3:]
"hello"[0:3]
```

![img_012](./images/img_012.png)

By default the start index is 0, because Python uses zero-order indexing. So the following abbreviation is also equivalent:

```
"hello"[:3]
```

![img_013](./images/img_013.png)

The default stop index is the length of the string. To get a copy of the string, the following expressions can be used:

```
"hello"[:len("hello")]
"hello"[:]
```

![img_014](./images/img_014.png)

The step size can be changed to 2, to get every even index using a start index of 0 and every odd index using a start index of 1 respectively:

![img_002](./images/img_002.png)

```
"hello"[::2]
"hello"[1::2]
```

![img_015](./images/img_015.png)

Negative indexes can also be used. To reverse the string, an index step of -1 can be used:

```
"hello"[-1:-len("hello")-1:-1]
"hello"[::-1]
```

![img_016](./images/img_016.png)

Care should be taken when using negative values as zero-order indexing is still used which is inclusive of the start index bound and exclusive of the stop index bound.

## The list class

The string method split can be used to split a string, on any whitespace character by default.

![img_017](./images/img_017.png)

For example:

```
greeting = "h e l l o"
split_greeting = greeting.split()
```

![img_018](./images/img_018.png)

Notice that a new datatype is shown on the variable inspector called a list. In the contents or value cell, the list is seen to use square brackets ```[ ]``` to enclose all elements and each element in the list is seperated out using a comma ```,``` as a delimiter, similar to the use of a comma to seperate out input arguments in a function.

The list instance ```split_greeting``` can be input followed by a ```dot``` and tab ```↹``` to view the available inbuilt identifiers:

![img_019](./images/img_019.png)

The ```dir``` function can be used to have a look at the hidden datamodel identifiers.

![img_020](./images/img_020.png)

Notice the similarity between the list datamodel methods and a list datamodel methods. These methods are setup to operate in a similar manner.

The following lists can be created, analogous to shopping lists:

```
shop1 = ["apples", "bananas", "cheese"]
shop2 = ["melons", "oranges"]
```

![img_021](./images/img_021.png)

Indexing is analogous to indexing in a string

```
shop1[0]
shop1[0:2]
```

![img_022](./images/img_022.png)

Addition of two list instances and replication of a list instance using an integer is also analogous to the same operations for the string class:

```
shop1 + shop2
shop1 * 2
```

![img_023](./images/img_023.png)

Despite these operations appearing to be analogous, they are setup to be used between two instances of the same class:

![img_024](./images/img_024.png)

The ```list``` class can be used to convert a string into a list of string characters:

```
list("lemons")
```

![img_025](./images/img_025.png)

The ```str``` class can be used to convert a list into a string:

```
shop1 = ["apples", "bananas", "cheese"]
shop1_str = str(shop1)
shop1_str
```

![img_026](./images/img_026.png)

Notice on the variable inspector that the content of the variables ```shop1``` and ```shop1_str``` looks identical. These are however different classes.

To convert from ```shop1_str``` back to a list. The string method ```strip``` has to be used to remove ```[```, ```]```, the escape character ```\'``` and the escape character ```\"```. strip only removes characters on the outside of the string.

The delimiter or seperator therefore becomes ```', '```. The string method ```split``` can be used with this seperator to return the original list:

```
shop1_str.strip("[ ] \' \"")
shop1_str.strip("[ ] \' \"").split(sep="', '")
shop1_list = shop1_str.strip("[ ] \' \"").split(sep="', '")
```

![img_027](./images/img_027.png)

```shop1``` can be viewed in more detail g the Spyder Variable Explorer:

```
shop1 = ["apples", "bananas", "cheese"]
```

![img_028](./images/img_028.png)

A list instance the datamodel methods ```__iter__``` and ```__reversed__``` which are mapped to Pythons inbuilt classes ```iter``` and ```reversed```. These classes create an instance of an iterator class which is not shown on the variable inspector:

```
forward.__iter__(shop1)
forward = iter(shop1)
forward
reversed.__iter__(shop1)
backward = reversed(shop1)
backward
```

![img_029](./images/img_029.png)

The ```dir``` function can be used to lookup the directory of the iterator instance so the datamodel identifiers can be examined:

```
dir(forward)
```

![img_030](./images/img_030.png)

The ```__next__``` datamodel method maps to the ```next``` function and is used to step up an index in the iterator returning the value at the associated index. It is only possible to increment one way.

![img_031](./images/img_031.png)

```
shop1 = ["apples", "bananas", "cheese"]
forward = iter(shop1)
next(forward)
next(forward)
next(forward)
next(forward)
```

A ```StopIteration``` error displays if the ```next``` function is used on a consumed iterator.

The ```list``` class can be used to convert an iterator object into a list. It will convert only the remaining items within the iterator into the new list:

![img_032](./images/img_032.png)

Similar beahaviour is observed for the reversed iterator:

```
shop1 = ["apples", "bananas", "cheese"]
backward = reversed(shop1)
next(backward)
next(backward)
```

![img_033](./images/img_033.png)

Most of the list methods available, modify the list inplace. The docstring of the ```reverse``` method can be examined:

![img_034](./images/img_034.png)

When this method is used:

```
shop1 = ["apples", "bananas", "cheese"]
shop1.reverse()
```

Notice there is no cell output. Instead the content of the variable ```shop1``` is reversed in place. This can be seen by examining the variable inspector.

![img_035](./images/img_035.png)

Care should be taken when assigning the output to a variable name. The list method is a function that returns the value of ```None```. Notice how the variable ```output``` has the value ```None``` on the variable inspector:

```
shop1 = ["apples", "bananas", "cheese"]
output = shop1.reverse()
```

![img_036](./images/img_036.png)

This is similar to the output of the inbuilt function ```print``` which also has a return statement of ```None```.

```
output = print("hello world!")
```

Notice when ```print``` is used, the output is always printed even when the function is assigned to a variable. The variable ```output``` has a value of ```None``` once again because this function returns ```None```:

![img_037](./images/img_037.png)

Care should be taken when attempting to use reassignment with a list method that occurs in place:

```
shop1 = ["apples", "bananas", "cheese"]
shop1 = shop1.reverse()
```

The method on the right hand side will carry out the inplace function however have a return value of ```None```. The value on the right will then be assigned to the variable name on the left and therefore the variable will be updated to have a value of ```None```:

![img_038](./images/img_038.png)

The list method ```append``` is used to append a single item to the end of a list and occurs in place. This item can be a string.

![img_039](./images/img_039.png)

```
shop1 = ["apples", "bananas", "cheese"]
shop1.append("lemons")
```

![img_040](./images/img_040.png)

The list method ```extend``` can be used to append a list onto another list. This occurs inplace updating the list, the method was called from.

```
shop1 = ["apples", "bananas", "cheese"]
shop2 = ["melons", "oranges"]
shop1.extend(shop2)
```

![img_041](./images/img_041.png)

The list method ```append``` can be used with another list. Notice that ```shop2``` is nested to the last index of ```shop1```. The ```len``` function will only return the length of the outer list. A nested list still only occupies an index of 1 in the outer list. This can be seen by indexing into the outer list to get this last element returning the nested list. Since this is also a list, this can be indexed into again to get a string.

```
shop1 = ["apples", "bananas", "cheese"]
shop2 = ["melons", "oranges"]
shop1.append(shop2)
len(shop1)
shop1[-1]
shop1[-1][1]
```

![img_042](./images/img_042.png)

So far only the string fundamental datatypes have been used to make a list however, lists can take numeric datatypes and other collections such as nested lists.

```
items = [1, "apples", 3.14]
```

![img_043](./images/img_043.png)

A list of numbers should be conceptualised as **a list of** numbers. The ```+``` operator will perform concatenation and not numeric addition:

```
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers1 + numbers2
numbers1.extend(numbers2)
```

![img_044](./images/img_044.png)

```
items = [1, "apples", 3.14]
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
nested = [numbers2, 2, "hello", items]
```

![img_045](./images/img_045.png)

For a long list:

```
shop1 = ["bananas", "melons", "oranges", "apples", "cheese"]
```

It is often more convenient to write the list over multiple lines:

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
```

![img_046](./images/img_046.png)

The output in the variable inspector is unchanged when the list is written over multiple lines.

The list method ```clear```, will clear all the items in an existing list. This method operates in place, making the original list an empty list:

```
shop1.clear()
```

![img_047](./images/img_047.png)

The empty list can be seen in the variable inspector:

![img_048](./images/img_048.png)

It is also possible to create an empty list by using the empty square brackets ```[ ]``` or the ```list``` class without any input arguments supplied:

```
empty1 = []
empty2 = list()
```

![img_049](./images/img_049.png)

The list method ```reverse```, will reverse all the items in an existing list. This method operates in place:

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop1.reverse()
```

![img_050](./images/img_050.png)

The list is now reversed as seen in the variable inspector.

![img_051](./images/img_051.png)

The list method ```sort``` can be used to sort a list in place. By default the ```sort``` uses the comparison operator which is configured for text or numeric data. The comparison perator is not configured for a string and a numeric datatype and  ```TypeError``` will display if this method is used on a list of mixed datatypes:

![img_052](./images/img_052.png)

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop1.sort()
nums = [1.1, 5, 3.2]
nums.sort()
mixed = [1, "apples", nums]
mixed.sort()
```

![img_053](./images/img_053.png)

The list method ```sort``` has a keyword input argument ```reverse``` which by default has a value of ```False```. This can be changed to ```True``` for a reverse sort.

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop1.sort(reverse=True)
nums = [1.1, 5, 3.2]
nums.sort(reverse=True)
```

![img_054](./images/img_054.png)

The keyword input argument ```key``` is typically used for advanced sorting and is assigned to a custom function or lambda expression (these will be covered in later tutorials).

If a list ```shop1``` is created:

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
```

And assigned to a new variable name ```shop2```:

```
shop2 = shop1
```

The values of ```shop1``` and ```shop2``` are the same so the check for equality is ```True```:

```
shop1 == shop2
```

The ```is``` keyword is an operator which checks whether the object name on the right is the same object as the object name on the left. This is ```tru``` and means ```shop2``` is an alias of ```shop1```:

```
shop1 is shop2
```

![img_055](./images/img_055.png)

As a consequence any method on ```shop1``` which operates in place will change ```shop2``` as ```shop2``` is ```shop1```:

```
shop1.clear()
```

![img_056](./images/img_056.png)

The list ```copy``` method is used to create a copy of the list which can be assigned to a new variable name:

![img_057](./images/img_057.png)

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop2 = shop1.copy()
shop1 == shop2
shop1 is shop2
shop1.clear()
```

Now ```shop2``` and ```shop1``` are equal but are not the same object. If an inplace operation is carried out on ```shop1``` after the copy ```shop2``` has been made, ```shop2``` is not changed as it is a copy and not an alias:

![img_058](./images/img_058.png)

The list method ```insert``` can be used to insert an object into a list, modifying the list in place. 

![img_059](./images/img_059.png)

Any object with that index or higher is shifted by one.

![img_060](./images/img_060.png)

For example, the string ```"grapes"``` can be inserted at index 2:

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop1.insert(2, "grapes")
```

![img_061](./images/img_061.png)

The string ```"oranges"``` which was at index 2 is now shifted to index 3, the  string ```"apples"``` which was at index 3 is now shifted to index 4 and the string ```"cheese"``` which was at index 5 is now shifted to index 6.

![img_062](./images/img_062.png)

The list method ```insert``` can be used with a collection:

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop2 = ["pears", "grapes"]        
shop1.insert(2, shop2)
```

![img_060](./images/img_060.png)

![img_063](./images/img_063.png)

In this context the list method ```insert``` works similarly to the list method ```append``` and will nest a collection into the specified index:

![img_064](./images/img_064.png)

The list method ```remove``` will remove the first occurance of a value, modifying the list in place:

![img_065](./images/img_065.png)

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]        
shop1.remove("melons")
```

![img_066](./images/img_066.png)

The list method ```pop``` removes a value from a list, by default the last value modifying the list in place. This method also has a return value, returning the popped value.

![img_067](./images/img_067.png)

In this example, the popped value isn't assigned to a variable but is displayed in the cell output. The list ```"shop1"``` is seen to be modified in place in the variable inspector.

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop1.pop()
```         

![img_068](./images/img_068.png)

The keyword index can be used to specify an index and the popped value can be assigned to a variable.

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
popped_val = shop1.pop(2)
```

```"Oranges"``` at index 2 will be popped:

![img_060](./images/img_060.png)

```popped_value``` displays in the variable explorer and ```shop_1``` is modified in place:

![img_069](./images/img_069.png)

Any item that had an index past the popped values original index is now shifted down by 1:

![img_070](./images/img_070.png)

The list method ```index``` searches for the index of a value between a lower ```start``` bound of 0 and an upper ```stop``` bound, which is the maximum possible length of a list.  These keyword input arguments can be modified to constrict the range if desired. 

![img_071](./images/img_071.png)

The index of the first occurance of the string ```"apples"``` can be searched for:

![img_060](./images/img_060.png)

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop1.index("apples")
```

This method returns the integer value of 3 and does not modify the original list:

![img_072](./images/img_072.png)

The list method ```count``` will count the number of occurances of a value. 

![img_073](./images/img_073.png)

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]
shop1.count("cheese")
```

This method returns an integer value of 1 and does not modifythe original list:

![img_074](./images/img_074.png)

## The tuple class

The list class has a number of methods whch modify the list in place. Modification in place is also known as mutation. There is another collection known as a ```tuple``` which is like a list but does not allow any modification of the tuple once it is created.

![img_075](./images/img_075.png)

A tuple is constructed in an almost identical manner to a list, except the enclosing brackets are circular opposed to square:

```
shop1 = ["bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]

shop2 = ("bananas", 
         "melons", 
         "oranges", 
         "apples", 
         "cheese")
```

![img_076](./images/img_076.png)

tuple are more memory efficient than lists as can be seen by comparing the memory size in bytes of the list and the tuple in the variable inspector. In the Spyder Variable Explorer, the tuples background shading is greyed out indiciating that the values in the tuple cannot be modified.

![img_077](./images/img_077.png)

If a tuple instance is input followed by a ```.``` and tab ```↹```, the list of identifiers displays:

![img_078](./images/img_078.png)

Notice that there are only 2 methods displaying ```index``` and ```count```. These methods behave in the same way as their counterparts in the list class, recalling that they did not modify the original list but instead returned a value.

If the ```dir``` function is used to lookup the directory of a tuple, the datamodel identifiers display. Most of these operate in a similar manner to a list. 

```
dir(shop2)
```

![img_079](./images/img_079.png)

```__add__``` is mapped to the ```+``` operator and performs concatenation. Concatenation returns a new instance and does not modify the original tuple.

```__mul__``` is mapped to the ```*``` operator and can be used to multiple a tuple by an integer. This operation does not alter the original tuple and instead returns a value that is the replicated version of the tuple. 

```__getitem__``` is used to index into a tuple using a numeric index enclosed in square brackets. The same notation, square brackets is used for indexing despite the tuple being constructed from different brackets.

```__iter__``` means the tuple is iteratable. This maps to the ```iter``` function and can be used to return an iterator object and does not modify the original tuple. There is no reversed iterator for a tuple.

```__len__``` is mapped to the ```len``` function and returns the legth of the tuple as an integer and does not modify the original tuple.

Because tuples are enclosed in circular brackets ```( )``` and parenthesis also use circular brackets ```( )``` to indicate order of oepration there is some confusion when it comes to creating an empty tuple or a tuple with a single element.

```
empty = ()
empty2 = tuple()
not_one = ("hello")
one = ("hello", )
```

![img_080](./images/img_080.png)

```not_one``` is not a tuple because the circular brackets ```( )``` are being used as parenthesis. Adding a comma ```,``` delimiter to the end of the singular element creates a tuple, as show for ```one```.

## The set class

lists and tuples have the method ```count``` which can be used to calculate the number of duplicate values for an entry in the outer collection. The ```set``` class is similar to a list except it cannot contain any duplicates. The set is constructed in a similar manner to a list or tuple however uses  braces ```{ }``` to enclose the collection.

```
shop1 = ["bananas", 
         "bananas",
         "melons", 
         "oranges", 
         "apples", 
         "cheese"]

shop2 = ("bananas", 
         "bananas",
         "melons", 
         "oranges", 
         "apples", 
         "cheese")

shop3 = {"bananas", 
         "bananas",
         "melons", 
         "oranges", 
         "apples", 
         "cheese"}
```

![img_081](./images/img_081.png)

Notice in the variable inspector that the set only displays ```"bananas"``` once despite two instances of this string being provided during instantiation (creating a new instance of a set).

Notice also the order is not in the order supplied; what index would an item have that was provided 100 times? A set is an unordered collection.

The comparison of these three collections can be seen in the variable explorer of the Spyder IDE. 

Notice that the ```list``` has an index associated with each value. The value has a coloured background indicating that it is possible to interact with the value and modify it. This can be done by indexing into the list and replacing the value:

![img_082](./images/img_082.png)

The ```tuple``` also has an index associated with each value. The value has a grey background indicating that it is not possible to interact with the value to modify it because tuples cannot be mutated:

![img_083](./images/img_083.png)

The ```set``` has no index because it is not an ordered collection. Because it has no index, it is not possible to replace a value using the index:

![img_084](./images/img_084.png)

The set instance name ```shop3``` can be input followed by a dot ```.``` and tab ```↹``` to view a list of set identifiers.

![img_085](./images/img_085.png)

The set methods ```clear```, ```copy``` and ```remove``` behave in an analogous way to the equivalent ```list``` methods.

The set method ```add``` is similar to the list method ```append```, the difference in the name indicates that there is no order in the set. Moreover if the value added is already included in the set, it won't be added again as sets can't have duplicates. 

![img_086](./images/img_086.png)

For example the string ```"grapes"``` can be added to the set using:

```
shop3 = {"bananas", 
         "bananas",
         "melons", 
         "oranges", 
         "apples", 
         "cheese"}
shop3.add("grapes")
```

![img_087](./images/img_087.png)

Notice that the set is updated inplace with ```"grapes"``` appearing in an unordered location.

Although this method is called ```add```, it should not be confused with the datamodel method ```__add__``` which is not available for a set. 

![img_089](./images/img_089.png)

The datamodel methods can be viewed by using ```dir``` to look up the directory of the set:

```
dir(shop3)
```

![img_088](./images/img_088.png)

The datamodel methods ```__str__```, ```__repr__```, ```__dir__``` and ```__doc__``` are mapped to the inbuilt class ```str```, the inbuilt functions ```repr```, ```dir``` and ```help```, ```?``` respectively behaving in the same behaviour as observed for the other inbuilt collections.

The datamodel method ```__len__``` maps to the inbuilt fucntion ```len``` and returns the number of unique items in the set.

The datamodel method ```__iter__``` maps to the inbuilt function ```iter``` and can be used to create an iterable object. This iterable object will have a numeric index and the values from the set will be randomly assigned to this index.

The datamodel methods ```__and__``` and ```__or__``` map to the operators ```&``` and ```|``` respectively and can be used to return a set that includes elements that occur in both sets in the case of ```&``` or the elements that occur in either set in the case of ```|``` respectively:

```
{1, 2, 3} | {2, 4, 6}
{1, 2, 3} & {2, 4, 6}
{1, 2, 3} & {4, 5}
```

![img_090](./images/img_090.png)

The set method ```pop``` differs from the ```list``` method ```pop``` because a set is unordered and therefore has no index input argument. An arbitrary value in the ```set``` will be popped:

![img_091](./images/img_091.png)

For example, in this case, the arbitrary popped value is ```"apples"```:

```
shop3 = {"bananas", 
         "bananas",
         "melons", 
         "oranges", 
         "apples", 
         "cheese"}
shop3.pop()
```

![img_092](./images/img_092.png)

The set method ```discard``` is similar to the set method ```remove```. These two methods behave differently when an item is not in the list, ignoring the item or flagging up an error respectively:

![img_093](./images/img_093.png)

![img_094](./images/img_094.png)

For example:

```
shop3 = {"bananas", 
         "bananas",
         "melons", 
         "oranges", 
         "apples", 
         "cheese"}
shop3.discard("oranges")
shop3.remove("cheese")
shop3.discard("lemons")
shop3.remove("grapes")
```

![img_095](./images/img_095.png)

The set method ```difference``` returns a set of the values in ```set1``` that are not present in ```set2```:

![img_096](./images/img_096.png)

Pictorally, this looks like:

![img_097](./images/img_097.png)

```
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set1.difference(set2)
```

![img_098](./images/img_098.png)

The set method ```intersection``` returns a set of the values in ```set1``` that are also present in ```set2```:

![img_099](./images/img_099.png)

Pictorally, this looks like:

![img_100](./images/img_100.png)

```
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set1.intersection(set2)
```

![img_101](./images/img_101.png)

The set method ```symmetric_difference``` returns a set of the values in ```set1``` that are not present in ```set2``` and the values in ```set2``` that are not in ```set1```:

![img_102](./images/img_102.png)

Pictorally, this looks like:

![img_103](./images/img_103.png)

```
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set1.intersection(set2)
```

![img_104](./images/img_104.png)

The set method ```union``` returns a set of all the unique values in ```set1``` and ```set2```:

![img_105](./images/img_105.png)

Pictorally, this looks like:

![img_106](./images/img_106.png)

```
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set1.union(set2)
```

![img_107](./images/img_107.png)

These four methods return a new set. There are four associated methods that perform an inplace update of ```set1```; ```difference_update```, ```intersection_update```, ```symmetric_difference_update``` and ```update``` (the latter can be thought of as ```union_update``` but is called ```update``` due to the fact that it is the most commonly used update method).

The method ```issuperset``` checks whether ```set1``` is a superset of ```set2```, i.e. all items in ```set2``` are in ```set1``` returning a boolean value:

![img_108](./images/img_108.png)

Pictorally this looks like:

![img_109](./images/img_109.png)

```
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {7, 8, 9}
set1.issuperset(set2)
```

![img_110](./images/img_110.png)

The method ```issubset``` checks whether ```set1``` is a subset of ```set2```, i.e. all items in ```set1``` are in ```set2``` returning a boolean value:

![img_111](./images/img_111.png)

Pictorally this looks like:

![img_112](./images/img_112.png)

```
set1 = {7, 8, 9}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set1.issubset(set2)
```

![img_113](./images/img_113.png)

The set method ```isdisjoint``` checks to see if there is no intersection between two sets returning a boolean value which is ```True``` for no insection and ```False``` if there is an intersection:

![img_114](./images/img_114.png)

```
set1 = {1, 2, 3}
set2 = {7, 8, 9}
set1.isdisjoint(set2)
```
![img_115](./images/img_115.png)

## The dictionary class

The dictionary class is a collection of key, value pairs; similar to an English dictionary which has a key or keyword and value or definition.

|keyword|definition|
|:-:|:-:|
|drop|to let something you are carrying fall to the ground|
|a few|some, or a small number of|
|record|information that is written on paper or stored on computer so that it can be used in the future|
|record|a flat, round, plastic disc that music is stored on, used especially in the past|

Instead of a keyword and a definition, the terms key and value are used:

|key|value|
|:-:|:-:|
|drop|to let something you are carrying fall to the ground|
|a few|some, or a small number of|
|record|information that is written on paper or stored on computer so that it can be used in the future|
|record|a flat, round, plastic disc that music is stored on, used especially in the past|

The key is typically a string, although numeric keys are also possible:

|key|value|
|:-:|:-:|
|"drop"|to let something you are carrying fall to the ground|
|"a few"|some, or a small number of|
|"record"|information that is written on paper or stored on computer so that it can be used in the future|
|"record"|a flat, round, plastic disc that music is stored on, used especially in the past|

Each key must be unique:

|key|value|
|:-:|:-:|
|"drop"|to let something you are carrying fall to the ground|
|"a few"|some, or a small number of|
|"record"|information that is written on paper or stored on computer so that it can be used in the future|

The value can be a fundamental datatype such as an integer, float, boolean value, string or another collection such as a tuple, list, set or even another dicitonary.

Dictionaries are often used when a key is easy to remember and a value is more difficult to remember. If a Word Processor is examined such as Microsoft Word, each Standard Color has a name which we can take as a key for example "green":

![img_116](./images/img_116.png)

The value is either designated as a hex string of the format ```#rrggbb``` or as a list of three integers ```[r, g, b]```:

![img_117](./images/img_117.png)

A dictionary of the standard colors using the values as hexadecimal values would look like:

|key|value|
|:-:|:-:|
|"wine"|"#C00000"|
|"red"|"#FF0000"|
|"orange"|"#FFC000"|
|"yellow"|"#FFFF00"|
|"light green"|"#92D050"|
|"green"|"#00B050"|
|"light blue"|"#00B0F0"|
|"blue"|"#0070C0"|
|"dark blue"|"#002060"|
|"purple"|"#7030A0"|

And using list of integer r, g, b values as:

|key|value|
|:-:|:-:|
|"wine"|[192, 0, 0]|
|"red"|[255, 0, 0]|
|"orange"|[255, 192, 0]|
|"yellow"|[255, 255, 0]|
|"light green|[146, 208, 80]|
|"green|[0, 176, 80]|
|"light blue"|[0, 176, 240]|
|"blue"|[0, 112, 192]|
|"dark blue"|[0, 32, 96]|
|"purple"|[112, 48, 160]|

For a dictionary the comma ```,``` is used as delimiter, the colon ```:``` is used to split a ```key: value``` pair and braces ```{ }``` are used to enclose the collection. The braces are shared with the ```set``` collection however there is usually no confusion between these collections as sets do not use colons.

The only time a set and dictionary get confused is with an empty dicitonary or empty set. In Python dicitonaries are far more commonly used, so an empty set of braces will make an empty dictionary and not an empty set.

```
empty_dict1 = {}
empty_dict2 = dict()
empty_set = set()
```

![img_118](./images/img_118.png)

```
colors = {"wine": "#C00000", "red": "#FF0000", "orange": "#FFC000", "yellow": "#FFFF00", "light green": "#92D050", "green": "#00B050", "light blue": "#00B0F0", "blue": "#0070C0", "dark blue": "#002060", "purple": "#7030A0"}
```

![img_119](./images/img_119.png)

For readibility it is common to write each ```key: value``` pair known as an ```item``` on its own line:

```
colors = {"wine": "#C00000", 
          "red": "#FF0000", 
          "orange": "#FFC000", 
          "yellow": "#FFFF00", 
          "light green" : "#92D050", 
          "green": "#00B050", 
          "light blue": "#00B0F0",
          "blue": "#0070C0", 
          "dark blue": "#002060", 
          "purple": "#7030A0"}
```

![img_120](./images/img_120.png)

The dictionary, like the set is an unordered collection and does not have a numeric index. In the case of the dictionary, keys are present in place of an index.

![img_121](./images/img_121.png)

In this example, all the keys are strings.

If a dictionary instance is input followed by a ```.``` and tab ```↹```, the list of identifiers displays:

![img_122](./images/img_122.png)

The dictionary methods ```clear``` and ```copy``` work in a similar manner to their counterparts in the ```list``` class.

The list of datamodel identifiers can be viewed by looking up the directory of a dictionary instance using the ```dir``` function:

![img_125](./images/img_125.png)

The datamodel identifiers ```__dir__```, ```__doc__```, ```__len__```, ```__repr__``` and ```__str__``` map to the inbuilt function ```dir```, ```?``` or ```help```, ```len```, ```rep``` and ```str``` and operate in a similar manner to their counterparts in the other collections as previously demonstrated with a string and list.

The datamodel method ```__getitem__``` is used to retrieve a value using its corresponding key. This method is not used directly and instead normally carried out using square brackets, to enclose the key. This is similar to indexing in a string, list or tuple but there is no numerical index for a dictionary and isntead a key is used (normally in the form of a string).

![img_126](./images/img_126.png)

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
colors.__getitem__("red")
colors["red"]
```

![img_127](./images/img_127.png)

If the key is not present in a dictionary, a ```KeyError``` displays. The dictionary also has a related method ```get``` that is also used to retrieve a value using the key however returns a value of ```None``` when the key is absent opposed to a ```KeyError```.

![img_123](./images/img_123.png)

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
colors["red"]
colors.get("red")
colors["white"]
colors.get("white")
```

![img_124](./images/img_124.png)

The datamodel method ```__setitem__``` is used to assign a new ```key: value``` pair to the dictionary.

![img_128](./images/img_128.png)

Typically this datamodel method is not used directly and instead a new value is assigned to the dictionary with a new key enclosed in square brackets:

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
colors.__setitem__("purple", "#7030A0")
colors["orange"] = "#FFC000"
```          

![img_129](./images/img_129.png)

The updated ```key: value``` pairs or items are seen in the dictionary. 

The dictionary datamodel methods, ```keys```, ```values``` and ```items``` return list like objects of keys, values and items. In ```items``` each element is a tuple of a ```(key, value)``` pair.

![img_130](./images/img_130.png)

![img_131](./images/img_131.png)

![img_132](./images/img_132.png)

The docstring for the ```keys``` and ```items``` methods states that the output collection is set like, this is because each key in a dictionary must be unique.

![img_133](./images/img_133.png)

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
colors.keys()
```

Assigning the output to the variable name ```keys```:

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
keys = colors.keys()
```

show the colelction has a limited number of methods. The method ```isdisjoint``` behaves in a similar manenr to ites counterpart in a set:

![img_134](./images/img_134.png)

The attribute ```mapping``` displays what value each key is mapped to:

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
keys = colors.keys()
keys.mapping
```

![img_135](./images/img_135.png)

```values``` only has the attribute ```mapping```:

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
values = colors.values()
values.mapping
```

![img_136](./images/img_136.png)

```items``` has the method ```disjoint``` and the attribute ```mapping```:

![img_137](./images/img_137.png)

These collections have datamodel identifiers which behave in a similar manner to seen in other collections:

![img_138](./images/img_138.png)

The datamodel method ```__getitem__``` is not defined for these classes which means indexing cannot be used for instances of these classes.

![img_139](./images/img_139.png)

It is quite common to use the ```list``` class to cast these collections into list instances for further manipulation.

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
keys = list(colors.keys())
values = list(colors.values())
items = list(colors.items())
items[0]
items[0][0]
```

![img_140](./images/img_140.png)

The ```zip``` function can be used to zip up multiple list-like collections. The zip collection instance created has the form of a list of tuples, similar to dictionary items.

![img_141](./images/img_141.png)

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
keys = list(colors.keys())
values = list(colors.values())
items = list(colors.items())
zipped = zip(keys, values)
```

the zipped colelction does not display on the variable explorer and no list of identifiers is displayed if an instance name is input followed by a dot ```.``` and tab ```↹```:

![img_142](./images/img_142.png)

Only the datamodel identifiers display if the directory is examined using ```dir```:

![img_143](./images/img_143.png)

Because the zipped object is however in the form of items. It can be cast into a dictionary using the ```dict``` class:

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
keys = list(colors.keys())
values = list(colors.values())
items = list(colors.items())
zipped = dict(zip(keys, values))
```

![img_144](./images/img_144.png)

Notice on the variable inspector the dictionary ```zipped``` has an identical form to the original dicitonary ```colors```.

The dictionary class has the datamodel methods ```__iter__``` and ```__reversed__``` which means the inbuilt functions ```iter``` and ```reversed``` can be used to create an iterator.

Notice that the iterable object only uses the keys. However the key returned in the iterator object can be used with the dictionary to return the corresponding value. For example:

```
colors = {"red": "#FF0000", 
          "green": "#00B050", 
          "blue": "#0070C0"}
forward = iter(colors)
backward = reversed(colors)
next(forward)
colors[next(forward)]
```

![img_145](./images/img_145.png)

## Using Collections Together

The fundamental datatypes are routinely jointly employed to store data ```int```, ```float```, ```string```, ```list```, ```set```, ```dict``` and ```tuple```.

Take for example a list of colors of objects where each color is stored as a string. As some objects can have the same color and the color of some other objects may later be added, the list is preferred.

```
colors = ["red", "red", "green", "green", "green", "blue"]
```

The unique colors can be found by casting this list to a set because a set can only have unique values:

```
unique_colors = set(colors)
```

The counts of each color can be computed using a dictionary where each key is a string and each value is an integer:

```
counts = {"red": 2,
         "green": 3,
         "blue": 1}
```

[Home Python Tutorials](https://github.com/PhilipYip1988/python-tutorials/blob/main/readme.md)