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

![001_concatenation](./images/001_concatenation.png)

### Indexing

We have also discussed how we can index from a string using square brackets enclosing an integer value:

```
"hello"[1]
```

In the above example, the letter ```"e"``` is returned which is at index 1.


![002_str_indexing](./images/002_str_indexing.png)


If you expected ```"h"```, recall that Python indexing uses zero order which is inclusive of ```0```:

![003_str_indexing](./images/003_str_indexing.png)

```
"hello"[0]
```

![004_str_indexing](./images/004_str_indexing.png)

Python zero order indexing is exclusive of the upper bound, which is the length of the string. We go up to but don't include the upper bound:

```
"hello"[len("hello")]
```

```
"hello"[len("hello") - 1]
```

![005_str_indexing](./images/005_str_indexing.png)

To recap, in Pythons zero order indexing, the first value is at index 0 and the last value is at the length of the string minus one:

```
"hello"[0]
```

```
"hello"[len("hello") - 1]
```

![006_str_indexing](./images/006_str_indexing.png)

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

![007_str_indexing](./images/007_str_indexing.png)

We can index using a slice. In full a slice uses the following notation:

```
"hello"[start:stop:step]
```

Because zero-order indexing is used, we are inclusive of the start bound and inclusive of the stop bound:

```
"hello"[1:3:1]
```

![008_str_indexing](./images/008_str_indexing.png)

so this means we start at the letter at index 1 which is ```"e"``` and we go up in steps of one, taking us to index 2 which has the letter ```"l"```. We go up to the stop index 3 but we do not include it. Therefore this slice is ```"el"``` and not ```"ell"```.

Indexing has default values:

```
"hello"[start:stop:step]
```

The ```start``` has a default value that is ```0```, the ```stop``` has a default value that is the length of the string and the ```step``` has a default value of ```1```. Explicitly specifying these will return the complete string:

```
"hello"[0:len("hello"):1]
```

![009_str_indexing](./images/009_str_indexing.png)

If we don't specify the step, a default value of 1 is selected, returning the whole string:

```
"hello"[0:len("hello"):]
```

![010_str_indexing](./images/010_str_indexing.png)

This also works if we don't supply the second colon:

```
"hello"[0:len("hello")]
```

![011_str_indexing](./images/011_str_indexing.png)

Examples using the default value of ```stop```:

```
"hello"[0:]
```

```
"hello"[1:]
```

![012_str_indexing](./images/012_str_indexing.png)

Examples using the default value of ```start```:

```
"hello"[:len("hello")]
```

```
"hello"[:3]
```

![013_str_indexing](./images/013_str_indexing.png)

Examples using the default value of ```start```, ```stop``` and ```step```:

```
"hello"[:]
```

```
"hello"[::]
```

![014_str_indexing](./images/014_str_indexing.png)

We can take every second value of the string using a ```step``` of ```2```:

```
"hello"[::2]
```

![015_str_indexing](./images/015_str_indexing.png)

Since we ```start``` at ```0```, this selects all the even indexs. If we instead want all the odd indexes, we can start at ```1```:

```
"hello"[1::2]
```

![016_str_indexing](./images/016_str_indexing.png)

We can get the string in reverse by specifying a step size of ```-1```:

```
"hello"[::-1]
```

![017_str_indexing](./images/017_str_indexing.png)

When using a step of ```-1```, the ```start``` takes on a default value of ```-1``` and the ```stop``` takes on a default values of - the length of the string minus 1:

```
"hello"[-1:-len("hello")-1:-1]
```

![018_str_indexing](./images/018_str_indexing.png)

Care needs to be taken when using the negative index as we are still inclusive of the ```start``` bound and exclusive of the ```stop``` bound.

## The list collection

A list can be used to store a collection of fundamental datatypes. The list has the following features:

* It is enclosed in square brackets ```[ ]```.
* It uses the comma ```,``` as a delimiter between each element (fundamental datatype) in the list.

The list can be visualised as a shopping list of singular items:

```
shopping_list = ["apples", "bananas", "cheese"]
```
![019_lists](./images/019_lists.png)

![020_lists](./images/020_lists.png)

Note however that when integer numbers are used to muliply individual strings, that string replication occurs:

```
shopping_list = ["apples", 2*"bananas", "cheese"]
```

![021_lists](./images/021_lists.png)

![022_lists](./images/022_lists.png)

Duplicates can however manually be added to a list:

```
shopping_list = ["apples", "bananas", "bananas", "cheese"]
```

![023_lists](./images/023_lists.png)

![024_lists](./images/024_lists.png)

The list can include numbers:

```
numbers = [1, 2, 3]
```

![025_lists](./images/025_lists.png)

![026_lists](./images/026_lists.png)

The list can also contain a mixture of fundamental datatypes:

```
items = [1, "apples", 3.14]
```

![027_lists](./images/027_lists.png)

![028_lists](./images/028_lists.png)

A list can also include other lists:

```
outer_list = [1, numbers, items]
```

![029_lists](./images/029_lists.png)

![030_lists](./images/030_lists.png)

In the example above numbers and items are nested lists. This can be input directly using:

```
outer_list = [1, [1, 2, 3], [1, "apples", 3.14]]
```

![031_lists](./images/031_lists.png)

Care should be taken to ensure that the square brackets inner and outer brackets match up appropriately. When a bracket is selected the JupyterLab IDE will automatically highlight what it determines to be the corresponding bracket in green, if the bracket isn't matched it will be highlighted in red to indicate a syntax error:

![032_lists](./images/032_lists.png)

### list functions and mutability

If we type in the variable or object name of one of the lists followed by a dot ```.``` and press tab ```↹```, we will see a number of functions that we can call from the object:

![033_lists](./images/033_lists.png)

Most of these functions modify the original list, this in place modification is also known as mutation. Notice that cell 31 and cell 33 do not show an output. In cell 32 and cell 34, when we look at the original list, we see the list has been updated:

```
items.append([5, "bananas"])
items
items.extend([5, "bananas"])
items
```

![034_lists](./images/034_lists.png)

We can see the subtle difference between the list functions ```append``` which appends a collection to a new upper index of the list and ```extend``` which extends the list by the items in the collection. For a single fundamental datatype such as an integer, float, boolean or string we should use ```append``` opposed to ```extend```:

```
items.append(1)
items
```

![035_lists](./images/035_lists.png)

If we type in the function name with open parenthesis and press shift ```⇧``` and tab ```↹``` we can see the functions docstring and details about the input arguments. We see in the case of append, we are looking for an object whereas in the case of extend, we are looking for an iterable object i.e. a collection:

![036_lists](./images/036_lists.png)

Recall that a string is a collection, if we use the string method extend with a string, we will iterate over the string and extend the list by placing each individual letter in the string as its own additional index:

```
items.extend("hello")
items
```

![037_lists](./images/037_lists.png)

Care should be taken to understand how these functions operate regarding list mutability. These functions modify the list object in place and if we assign the output of the function to a new variable name, the new variable name will be the type ```NoneType``` object:

```
old_list = [1, 2, 3, 4]
new_list = old_list.append(5)
```

![038_lists](./images/038_lists.png)

Reassignment will modify the list in place and then reassign the list to the output to ```NoneType``` object:

```
old_list = [1, 2, 3, 4]
old_list = old_list.append(5)
```

![039_lists](./images/039_lists.png)

A list is a collection, like a string and the operator ```+``` can be used to concatenate two lists together. The operator ```*``` can also be used to with a list and int to replicate the list:

```
items1 = [1, "apples", 3.14]
items2 = [2, "bananas"]
items1 + items2
2 * items1
```

Note in cells 42 and 43 an output is shown. This is because the operators ```+``` and ```*``` defined by the functions ```__add__``` and ```__mul__``` each have a return value:

![040_lists](./images/040_lists.png)

To understand how mutability works, we can create a custom append function, that uses a global list and mutates it:

```
items1 = [1, "apples", 3.14]

def append1(other_list):
    global items1
    items1 = items1 + other_list
```

If we call this function, supplying the positional input argument ```other_list```:

```
append1(["hello", "goodbye"])
```

We see that there is no return value shown because this function has no return statement but ```items1``` is mutated:

![041_lists](./images/041_lists.png)

Now if we instead create a function without a global variable and instead use a return value:

```
items1 = [1, "apples", 3.14]

def append2(orig_list, other_list):
    return orig_list + other_list
```

If we call this function supplying the two input inputs ```orig_list``` and ```other_list```:

```
append2(items1, ["hello", "goodbye"])
```

We see a return value corresponding to the return value supplied when the function ```append2``` was defined and in this case the original list ```items1``` is unaltered:

![042_lists](./images/042_lists.png)

We will look at functions and code blocks in a later guide. However the main point to highlight here is the list functions that mutate the original list have no return function and therefore return NoneType when assigned or reassigned to a variable or object name. 

We have already seen the ```append``` and ```extend``` list function which mutate the list:

![033_lists](./images/033_lists.png)

The list function ```index```, will return the index of a value, if the value exists in the list. In this case the value ```"apples"``` is at index ```1```:

```
items1 = [1, "apples", 3.14]
items1.index("apples")
```

![043_lists](./images/043_lists.png)

![044_lists](./images/044_lists.png)

For duplicates only the  first occurance will be returned:

```
items1 = [1, "apples", 3.14, "apples"]
items1.index("apples")
```

An optional secondary input argument can be supplied to selecting a starting index value to begin the search from. If for example index 2 is selected, we will return the next occurance of ```"apples"``` at index 3:

```
items1.index("apples", 2)
```

![045_lists](./images/045_lists.png)

![046_lists](./images/046_lists.png)

If we recreate the simple list:

```
items1 = [1, "apples", 3.14]
```

![047_lists](./images/047_lists.png)

![048_lists](./images/048_lists.png)

The ```insert``` function, can be used to select an index and insert a value at the index. Any values past the index of insertion will be shunted one up:

```
items1.insert(2, "bananas")
```

![049_lists](./images/049_lists.png)

![050_lists](./images/050_lists.png)

Note this function mutates the list and the function has no return statement.

Recreating the list:

```
items1 = [1, "apples", 3.14, "apples"]
```

![051_lists](./images/051_lists.png)

![052_lists](./images/052_lists.png)


The function ```remove``` will remove the first occurance of an item in a list:

```
items1.remove("apples")
```

This function mutates the original list and an item higher than the index of the item being removed is shunted down by one index:

![053_lists](./images/053_lists.png)

![054_lists](./images/054_lists.png)

The function ```reverse``` will reverse the contents in the list and once again mutate the original list:

```
items1.reverse()
```

![055_lists](./images/055_lists.png)

![056_lists](./images/056_lists.png)

Recreating the list:

```
items1 = [1, "apples", 3.14, "apples"]
```

![051_lists](./images/051_lists.png)

![052_lists](./images/052_lists.png)

The function ```count``` will return the count of the number of occurances of a value in the list. 

```
items1.count(3.14)
items1.count("apples")
```

![057_lists](./images/057_lists.png)

Note it will only count the occurances in the outer list and no occurances within nested collections. For example if we append a list:

```
items1.append(["apples", "apples"])
```

![058_lists](./images/058_lists.png)

![059_lists](./images/059_lists.png)

And then use:

```
items1.count("apples")
```

![060_lists](./images/060_lists.png)

We get a return value of ```2``` and not ```4```. The last index with respect to the outer list has the value ```["apples", "apples"]``` which differs from the precise search term ```"apples"```. Likewise if we append a single value ```"pineapples"```:

```
items1.append("pineapples")
```

![061_lists](./images/061_lists.png)

![062_lists](./images/062_lists.png)

This precise search term ```"apples"``` is only counted twice. The search term ```"apples"``` differs from ```"pineapples"```:

![063_lists](./images/063_lists.png)

The ```clear``` function clears the list. This removes all the contents in the list. Once again this function mutates the original list, leaving an empty list:

```
items1.clear()
```

![064_lists](./images/064_lists.png)

![065_lists](./images/065_lists.png)

An empty list can be created using:

```
empty_list = []
```

![066_lists](./images/066_lists.png)

The function ```pop``` can be used to ```pop``` the last value off the list. This is one of the only functions that both mutates the original list and has a return value. i.e. the original list is updated with the last value removed (cell 78) and the return value is the value popped from the list (cell 77):

```
items1.pop()
```

![067_lists](./images/067_lists.png)

Therefore when using this function, we can assign the output to a variable:

```
last_value = items1.pop()
```

![068_lists](./images/068_lists.png)

The function ```sort``` can be used to sort the values in a list, mutating the original list. This sorting only works if all the numbers in the list are numeric or alphabetical:

```
numbers = [1, 3, 2]
numbers.sort()
numbers
```

```
words = ["banana", "apples", "grapes"]
words.sort()
words
```

![069_lists](./images/069_lists.png)

If we assign the list to a new object name:

```
fruits = words
```

We see that both the new list ```fruits``` is equal ```==``` to the list ```words``` meaning all the values in the list match but also that ```fruits``` ```is``` ```words``` meaning the two names are alias for the same list object in memory:

```
fruits == words
fruits is words
```

This means when we mutate ```fruits```, then because ```words``` ```is``` ```fruits``` then ```fruits``` is seen to be mutated:

```
fruits.append("oranges")
```

![070_lists](./images/070_lists.png)

We have the list function ```copy``` which returns a copy of the original list:

```
words = ["banana", "apples", "grapes"]
fruits = words.copy()
```

We see that the new list ```fruits``` is equal ```==``` to the list ```words``` meaning all the values in the list match but now that ```fruits``` ```is not``` ```words``` meaning these are two different list objects in memory:

```
fruits == words
fruits is words
```

Mutating one list now leaves the other list unchanged:

```
fruits.append("oranges")
```

![071_lists](./images/071_lists.png)

## The tuple collection

If we replace the square brackets ```[ ]``` with ```( )``` we get another collection known as a ```tuple```: 

```
words_l = ["banana", "apples", "grapes"]
words_t = ("banana", "apples", "grapes")
```

Both collections look very similar however a ```tuple``` once created cannot be mutated and this is why all the items in the tuple have a grey background in the Variable Explorer:

![072_tuples](./images/072_tuples.png)

![073_tuples](./images/073_tuples.png)

The difference can be more clearly seen when inputting the objects name followed by a dot ```.``` and press tab ```↹``` to view the number of functions available to call from the object:

![074_tuples](./images/074_tuples.png)

We see in the case of the ```tuple``` that we only have the functions which return a value and cannot access equivalents to any of the list functions which mutate the list. 

A tuple can be indexed using ```[ ]``` brackets in the exact same manner as a list or a string:

```
words[0]
```

![075_tuples](./images/075_tuples.png)

In Python the ```( )``` are also used for parenthesis, this means care needs to be taken when creating a tuple with a single element or an empty tuple:

```
not_a_tuple = ("hello")
a_tuple = ("hello",)
empty_tuple = tuple()
```

![076_tuples](./images/076_tuples.png)

The classes ```tuple``` and ```list``` can be used to create an empty tuple or empty list. We can think of them as conversion functions which will return a tuple form a list or vice versa:

```
fruits = ("banana", "apples", "grapes")
fruits_2 = list(fruits)
```

![077_tuples](./images/077_tuples.png)

Once created a ```tuple``` cannot be modified, however the object name assigned to the tuple can be reassigned to a new value:

```
fruits = ("banana", "apples", "grapes")
fruits = list(fruits)
```

![078_tuples](./images/078_tuples.png)

tuples at first glance may seem to be lists with limited capabilities however mutability isn't always a desired trait, for example when using constants, mutability can allow accidental change of the constant which lead to issues in a longer program. tuples also use less memory than lists, and may be faster for large datasets that don't need mutated.

## The set collection

Another collection is a ```set```, which is a collection of unique items. Curly braces ```{ }``` are used to enclose a set:

```
items1 = {1, "apples", 3.14, "apples"}
```

![079_sets](./images/079_sets.png)

![080_sets](./images/080_sets.png)

When we created the set above, we supplied ```"apples"``` at 1 and also 3. Only one instance of ```"apples"``` displays. Notice also on the variable explorer, that there is no index in a ```set```, order is not maintained as only a single instance of a unique item is retained. A ```set``` is an unordered collection.

Input the set objects name followed by a dot ```.``` and press tab ```↹``` to view the number of functions that can be called from the set the object:

![081_sets](./images/081_sets.png)

Some of these closely resemble the analogous function available for a list and mutate the set. The others relate to mathematical set operations such as looking at the difference and union of sets.

The ```set``` class can be used to convert a ```tuple``` or ```list``` to a ```set```. It can also be used to create an empty ```set```:

```
empty_set = set()
not_a_set = {}
```

![082_sets](./images/082_sets.png)

![083_sets](./images/083_sets.png)

Note that empty braces ```{ }``` cannot be used to ceate a ```set``` as they are used for another collection which is far more commonly used known as a dictionary abbreviated ```dict```.

## The dictionary collection

A dictionary can be conceptualised as an English dictionary:

|word|meaning|
|:-:|:-:|
|drop|to let something you are carrying fall to the ground|
|a few|some, or a small number of|
|record|information that is written on paper or stored on computer so that it can be used in the future|
|record|a flat, round, plastic disc that music is stored on, used especially in the past|

Instead of a word and a meaning, we use the terms key and value:

|key|value|
|:-:|:-:|
|drop|to let something you are carrying fall to the ground|
|a few|some, or a small number of|
|record|information that is written on paper or stored on computer so that it can be used in the future|
|record|a flat, round, plastic disc that music is stored on, used especially in the past|

The key is typically a string, although numeric keys are possible:

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

The value can be a fundamental datatype such as an integer, float, boolean value, complex number or string (collection of characters). It can also be another collection. Dictionaries are normally used when a key is easy to remember and a value is more difficult to remember. If we have a look at a Word Processor such as Microsoft Word, we see that each Standard Color has a name which we can take as a key for example "green":

![084_dict](./images/084_dict.png)

The value is either designated as a hex string of the format ```#rrggbb``` or as a list of three integers ```[r, g, b]```:

![085_dict](./images/085_dict.png)

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

For a dictionary the comma ```,``` is used as delimiter and the colon ```:``` is used to split a key:value pair. Braces ```{ }``` are used to enclose a dictionary:

```
colors = {"wine": "#C00000", "red": "#FF0000", "orange": "#FFC000", "yellow": "#FFFF00", "light green": "#92D050", "green": "#00B050", "light blue": "#00B0F0", "blue": "#0070C0", "dark blue": "#002060", "purple": "#7030A0"}

```

![086_dict](./images/086_dict.png)

For readibility it is common to write each ```key:value``` pair on its own line:

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

![087_dict](./images/087_dict.png)

Notice in the variable explorer that the ```key``` in the dictionary is there opposed to a numeric ```index``` like seen in a list. Typically the keys are displayed in alphabetical order for convenience:

![088_dict](./images/088_dict.png)

The value can be obtained by indexing with square brackets, using the key (usually in the form of a string):

```
colors["wine"]
```

![089_dict](./images/089_dict.png)

Inputting the dictionary object name followed by a dot ```.``` and pressing tab ```↹``` will display the functions available to call from the dictionary object:

![090_dict](./images/090_dict.png)

The functions keys, values and items return a list like collection of keys, values and in the case of items a tuple of ```(key, value)``` for each ```key: value``` pair. These three functons are useful when it comes to iterating along a dictionary. Iteration will be discussed in more detail in the next tutorial:

```
colors.keys()
colors.values()
colors.items()
```

![091_dict](./images/091_dict.png)

Most of the other functions are similar to their counterparts in a list, with slight differences due to the dictionary having a ```key: value``` pair opposed to just a ```value```.

The color dicitonary can be recreated using a r, g, b list or tuple for each number: 

```
colors = {"wine": [192, 0, 0], 
          "red": [255, 0, 0], 
          "orange": [255, 192, 0], 
          "yellow": [255, 255, 0], 
          "light green" : [146, 208, 80], 
          "green": [0, 176, 80], 
          "light blue": [0, 176, 240],
          "blue": [0, 112, 192], 
          "dark blue": [0, 32, 96], 
          "purple": [112, 48, 160]}
```

![092_dict](./images/092_dict.png)
![093_dict](./images/093_dict.png)

We can get the value of the key ```"purple"``` using:

```
colors["purple"]

```



And specifically the g value of purple by indexing into this list using index 1:

```
colors["purple"][1]
```

![094_dict](./images/094_dict.png)

It is possible to create a dictionary by zipping together two list like collections using the ```zip``` function:

```
color_keys = ["wine", "red", "orange", "yellow", "light green", 
              "green", "light blue", "blue", "dark blue", "purple"]

color_values = ["#C00000", "#FF0000", "#FFC000", "#FFFF00", "#92D050", 
                "#00B050", "#00B0F0", "#0070C0", "#002060", "#7030A0"]

colors = dict(zip(color_keys, color_values))
```

![095_dict](./images/095_dict.png)

Return to:
[Home](../../../)