# Functions

The previous tutorials have looked at using inbuilt functions with inbuilt datatypes such as strings, integers, floats, bools, lists, tuples, sets and dictionaries. When using a function, some concepts have already been explored such a positional and keyword input arguments and referencing a function versus calling a function. In this guide, custom functions will be defined and called.

## Variables Recap

Variables can be created by assigning a value to an object name using the assignment operator ```=```.

```
var1 = 1
var2 = 2.1
var3 = "hello"
var4 = ["apples", "bananas", "grapes"]
```

Once created, these variables display on the variable explorer.

![img_069](./images/img_069.png)

## Function Definition

Instead of using the assignment operator ```=```, a function is defined to an object name using the ```def``` keyword, an abbreviation for definition. Function definition is typically more complicated than variable assignment, as functions require an input arguments and also include a function code block. The cocept of code blocks has previously been explored.

The form of a function is as follows.

```
def fun_name():
    print("Hello")
    return None


```

![img_002](./images/img_002.png)

The function is defined using the ```def``` keyword. 

![img_003](./images/img_003.png)

The ```def``` keyword is followed by the functions name. The functions name follows the standard naming convention of variable or object names.

![img_004](./images/img_004.png)

After the function name, is a set of parenthesis ```( )``` which are used to enclose any input arguments. These will be discussed in more detail later.

![img_005](./images/img_005.png)

After the parenthesis is a colon ```:``` which is used to indicate the beginning of a code block.

![img_006](./images/img_006.png)

Code belonging to the code block is indented by four spaces, as previously discussed.

![img_007](./images/img_007.png)

The final line in the code block is the ```return``` statement, which can be used to optionally return a value. 

![img_008](./images/img_008.png)

When the function is defined, it does not display on the variable inspector. 

![img_070](./images/img_070.png)

Using the function ```dir``` without any input arguments will look up the directory of the current interctive notebook file and the function ```fun_name``` displays:

![img_071](./images/img_071.png)

Inputting a prefix of the functions name in a cell followed by a tab ```↹``` will show object names in the interactive notebooks name space that begin with the prefix. In this case the prefix is ```f``` and the function ```fun_name``` displays:

![img_072](./images/img_072.png)

## Calling a Function

If the function name is typed into a cell. The output of the cell states that the object is a function, giving some details about the location where the function is defined. ```__main__``` is a datamodel identifier and in this case corresponds to the interactive notebook file itself which is directly running in Python. The reference essentially states ```fun_name``` is a function, defined in the current interactive notebook and has the name ```fun_name```.

```
fun_name
```

![img_010](./images/img_010.png)

To call a function, the function name must be followed by a set of parenthesis ```( )```. These parenthesis should include the values of any input arguments, for each input argument from the function definition. In this example, no input arguments were included in the definition of ```fun_name```, so the parenthesis should be left empty.

```
fun_name()
```

![img_011](./images/img_011.png)

Notice that the print statement in the functions code block is now executed. The output of a function call, can be assigned to a variable. For example.

```
fun_out = fun_name()
```

![img_073](./images/img_073.png)

Notice that the variable displays on the variable inspector with a value of ```NoneType```. This is because the last line in the functions code block is ```return None```. 

Note when the ```return``` statement is not included at the end of the function block ```return None``` is taken as the default. This is explicitly implied in this example for clarity. 

## return Statement

Two subtly different functions will now be defined, ```print_hello``` which has a print statement printing the value ```"Hello"``` to the console and a ```return None``` return value. And the function ```return_hello``` which has no print statement but returns the value ```"Hello"```.

```
def print_hello():
    print("Hello")
    return None


```

```
def return_hello():
    return "Hello"


```

When these functions are called, the behaviour appears to be similar.

```
print_hello()
return_hello()
```

![img_014](./images/img_014.png)

In the first case, a value is printed to the cell output and because it is printed, the output is formatted, so ```Hello``` displays without any quotation marks. i.e. the print function is displaying text in the cell output using the ```__str__``` method of the string.

In the second case, the value returned and not assigned to a variable name so the representation of the string is displayed in the cell output. i.e. the cell is displaying text which used the ```__repr__``` method of the string.

The difference can be seen more clearly, when the two functions are called and assigned to variables.

```
print_out = print_hello()
return_out = return_hello()
```

![img_074](./images/img_074.png)

Notice that there is still a cell output when the ```print_hello``` function is used, because this function uses a print statement which always as the name suggests prints. The variable ```print_out``` has the value ```None``` because this function has a ```return None``` return statement.

In constrast there is no cell output when the ```return_hello``` function is used, because this function has returned the value to the variable ```return_out```. ```return_out``` can be seen to have the value ```"Hello"``` on the variable explorer.

The behaviour of the ```"print_hello"``` function does not change if the ```return None``` return statement is removed.

```
def print_hello():
    print("Hello")


```

```
print_out = print_hello()
```

![img_075](./images/img_075.png)

This is because ```None``` is the default return value.

## Input Arguments

A simple function can be defined which has a single input argument ```value```. This function will merely return this input argument ```value``` unaltered.

```
def return_value(value):
    return value


```

If this function is called without providing the input argument ```value``` then an error message is displayed.

```
var = return_value()
```

![img_019](./images/img_019.png)

If the function name is typed with open parenthesis followed by the shortcut key shift ```⇧``` and tab ```↹```, details about the expected input argument are displayed.

![img_020](./images/img_020.png)

If the function is called with an input argument, it will run as expected. The new variables ```var1``` and ```var2``` will display on the variable inspector.

```
var1 = return_value("Hello")
var2 = return_value(value="Hello")
```

![img_076](./images/img_076.png)

In the above case, when assigning the output of the function to ```var1```, the function was called by providing a singular positional input argument. When using positional input arguments, they need to be provided in the correct order, matching the order of the function definition.

When assigning the output of the function to ```var2```, the function was called by explicitly defining a variable name and assigning it to a value. In such a scenario, the order of the positional input arguments can be changed provided that all the positional input arguments are supplied. In general however it is recommended to maintain the order of the positional input arguments.


## docstring

When using shift ```⇧``` and tab ```↹```, details about the input arguments are supplied, alongside the functions docstring. A docstring can be provided by creating a multi-line comment at the top of the functions code block. 

```
def return_value(value):
    """
    """
    return value


```

Notice that the template for the docstring displays as soon as the multiline comment is added.

```
def return_value(value):
    """
    

    Parameters
    ----------
    value : TYPE
        DESCRIPTION.

    Returns
    -------
    value : TYPE
        DESCRIPTION.

    """
    return value


```

This template should be filled out, so that the docstring should provide a quick description of what the function does. For each input argument and the return value, the expected datatype should be supplied. For example.

```
def return_value(value):
    """
    This function takes in an input value and returns it unaltered.

    Parameters
    ----------
    value : str
        This the value input.

    Returns
    -------
    value : str
        This is the unaltered value returned.

    """
    return value


```

When inputting the functions name with open parenthesis followed by shift ```⇧``` and tab ```↹```, the updated docstring displays. 

![img_023](./images/img_023.png)

Another function ```make_plural``` can be defined which once again takes in a singular input value. This time the input is manipulated to a plural value by concatention with an ```"s"``` within the functions body and the function returns the plural value. 

```
def make_plural(word):
    """
    This function takes in a singular word and returns the plural word.

    Parameters
    ----------
    word : str
        The singular word.

    Returns
    -------
    plural_word : str
        The plural word.

    """
    plural_word = word + "s"
    return plural_word


```

![img_024](./images/img_024.png)

This function can be tested using the input strings ```"cat"``` and ```"dog"``` respectively.

```
word1 = "cat"
word2 = "dog"

word1s = make_plural(word1)
word2s = make_plural(word2)
```

![img_077](./images/img_077.png)


Another function can be defined which counts the number of vowels within a word. In this example the code block of the function body contains a nested for loop. The input argument ```word``` is a string and the return value ```vowel_count``` is an integer.

```
def count_vowels(word):
    """
    This function takes in a word and counts the number of vowels.

    Parameters
    ----------
    word : str
        Input word.

    Returns
    -------
    vowel_count: int
        The number of vowels.

    """
    vowel_count = 0
    for let in word:
        if let in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
    

    return vowel_count


```

This function can be tested using the input string ```"anaconda"```.

![img_027](./images/img_027.png)


Since the function has a return statement, the value being returned can be assigned to a variable during the function call:

```
word1 = "anaconda"
vowel_n = count_vowels(word1)
```

![img_078](./images/img_078.png)

Each function can only have one return statement. However this return value can be a collection such as a list or a tuple. The function above can be modified to return a list containing two values, the vowel count and the consonant count. Once again the docstring should outline clearly what each input argument is and what each value in the return list is.

```
def count_vowels_cons(word):
    """
    This function takes in a word and returns the number of vowels 
    and consonants.

    Parameters
    ----------
    word : str
        Input word.

    Returns
    -------
    [vowel_count, cons_count]: [int, int]
        The number of vowels and the number of consonants.

    """
    vowel_count = 0
    cons_count = 0
    for let in word:
        if let in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
        else:
            cons_count += 1
    

    return [vowel_count, cons_count]


```

This function can be once again be tested using the input string ```"anaconda"```. 

![img_030](./images/img_030.png)

Since the function has a return statement, which returns a collection, each value in the collection can be assigned to a variable during the function call:

```
word1 = "anaconda"
[vowel_n, cons_n] = count_vowels_cons(word1)
```

![img_079](./images/img_079.png)


The list collection can also be unpacked using.

```
vowel_n, cons_n = count_vowels_cons(word1)
```

![img_080](./images/img_080.png)

## Positional and Keyword Input Arguments

So far a function has been created with no positional input arguments and one positional input argument. It is possible to create a function with other combinations of positional and keyword input arguments. 

A keyword input argument is assigned a default value during the functions definition and this means the function can be called without specifying the keyword input argument. For example a custom ```print_word``` function can be created.

```
def print_word(word="Hello"):
    """
    

    Parameters
    ----------
    word : string, optional
        DESCRIPTION. The default is "Hello".

    Returns
    -------
    None.

    """
    print(word)
    return None


```

If no input argument is supplied when calling the function, the default value is printed.

```
print_word()
```

This default value can however be assigned a new value while calling the function to instead print the new value.

```
print_word(word="Goodbye")
```

![img_034](./images/img_034.png)

Since this function only has a single keyword input argument, this function can be called using the position of this input argument:

```
print_word("Farewell")
```

![img_035](./images/img_035.png)

A more complicated function can be created with 4 input arguments; 2 positional and 2 keyword input arguments.

```
def print_words(word1, word2, word3="Hello", word4="Goodbye"):
    """
    

    Parameters
    ----------
    word1 : string
        DESCRIPTION.
    word2 : string
        DESCRIPTION.
    word3 : string, optional
        DESCRIPTION. The default is "Hello".
    word4 : string, optional
        DESCRIPTION. The default is "Goodbye".

    Returns
    -------
    None.

    """
    output = [word1, word2, word3, word4]
    print(output)
    return None


```

![img_036](./images/img_036.png)

When calling this function, the 2 positional input arguments must be supplied in order. 

```
print_words("Python", "Anaconda")
```

Normally the name of positional input arguments aren't provided but they can optional be supplied:

```
print_words(word1="Python", word2="Anaconda")
```

Once all positional input arguments are assigned a value, any keyword input arguments can also be supplied a custom value:

```
print_words("Python", "Anaconda", word3="pip")

print_words("Python", "Anaconda", word4="mamba")

print_words("Python", "Anaconda", word3="pip", word4="mamba")
```

It is possible to call the function by assigning the name of all the input arguments and assigning them each to a value:

```
print_words(word1="Python", word2="Anaconda", word3="pip", word4="mamba")
```

Alternatively it is possible to list the value of all input arguments without use of any of the input argument names:

```
print_words("Python", "Anaconda", "pip", "mamba")
```

![img_037](./images/img_037.png)

When all the names of the input arguments are supplied, they can be listed in any order. 

```
print_words(word4="mamba", word1="Python", word2="Anaconda", word3="pip")
```

![img_038](./images/img_038.png)

**However this is generally bad practice** and it is better practice to maintain the order of the positional input arguments to prevent any confusion. 

The more conventional syntax used to call the function above is of the form:

```
print_words("Python", "Anaconda", word3="pip", word4="mamba")
print_words("Python", "Anaconda", word3="pip")
print_words("Python", "Anaconda", word4="mamba")
print_words("Python", "Anaconda")
```

![img_039](./images/img_039.png)

### Asserting Input Arguments

The following function can be created which expects 4 strings as input arguments; 2 positional strings and 2 keyword strings:

```

def print_words(word1, word2, word3="Hello", word4="Goodbye"):
    """
    prints the concatenation of all input words

    Parameters
    ----------
    word1 : str
        DESCRIPTION.
    word2 : str
        DESCRIPTION.
    word3 : str, optional
        DESCRIPTION. The default is "Hello".
    word4 : str, optional
        DESCRIPTION. The default is "Goodbye".

    Returns
    -------
    None.

    """
    output = word1 + word2 + word3 + word4
    print(output)
    return None


```

![img_040](./images/img_040.png)

The function can be called using 2 positional strings and works as expected, concatenating all the strings together and printing the concatenated string.

```
print_words("Python", "Anaconda")
```

![img_041](./images/img_041.png)

When one of these is set to an incorrect datatype, an error is displayed:

```
print_words(1, "Anaconda")
```
![img_042](./images/img_042.png)

However, more dangerously, when all of these input arguments are the wrong datatype, the code appears to "work":

```
print_words(1, 2, word3=3, word4=4)
```

![img_043](./images/img_043.png)

The inbuilt ```isinstance``` function can be used to check if a variable belongs to a class. It has the form:

```
isinstance(variable, class)
```

Or:

```
isinstance(variable, (class1, class2, class2))
```
For example, the following can be checked:

```
isinstance("Python", str)
```

![img_044](./images/img_044.png)

```
isinstance(1, str)
```

![img_045](./images/img_045.png)

```
isinstance(3.14, str)
```

![img_046](./images/img_046.png)

```3.14``` can be checked to see if it is an integer using:

```
isinstance(3.14, int)
```

![img_047](./images/img_047.png)

```3.14``` can be checked to see if it is numeric using:

```
isinstance(3.14, (int, float, bool))
```

![img_048](./images/img_048.png)

The ```assert``` keyword can be used, to assert a condition. If the condition is True, the code will continue as normal:

```
condition = True
assert condition
```

![img_049](./images/img_049.png)

If the condition is False, an ```AssertionError``` will display:

```
condition = False
assert condition
```

![img_050](./images/img_050.png)

An optional message can be displayed alongside the error. This does not display when the condition is True:

```
condition = True
assert condition, "optional message"
```

![img_051](./images/img_051.png)

But displays when the condition is False:

```
condition = False
assert condition, "optional message"
```

![img_052](./images/img_052.png)

The function above can be modified, to assert that each input is a string:

```
def print_words(word1, word2, word3="Hello", word4="Goodbye"):
    """
    prints the concatenation of all input words

    Parameters
    ----------
    word1 : str
        DESCRIPTION.
    word2 : str
        DESCRIPTION.
    word3 : str, optional
        DESCRIPTION. The default is "Hello".
    word4 : str, optional
        DESCRIPTION. The default is "Goodbye".

    Returns
    -------
    None.

    """
    assert isinstance(word1, str), "word1 must be a str"
    assert isinstance(word2, str), "word2 must be a str"
    assert isinstance(word3, str), "word3 must be a str"
    assert isinstance(word4, str), "word4 must be a str"
    
    output = word1 + word2 + word3 + word4
    print(output)
    return None
    
    
```

![img_053](./images/img_053.png)

The function works in the same manner as before, when the input arguments supplied are of the correct datatype:

```
print_words("Python", "Anaconda")
```

![img_054](./images/img_054.png)

The ```AssertionError``` will display when these are the wrong datatypes:

```
print_words(1, 2, word3=3, word4=4)
```

![img_055](./images/img_055.png)

```try``` and ```except``` code blocks can be setup to handle the ```AssertionError``` for the keyword input arguments. When these arguments are the wrong datatypes, the value can be assigned to a default value:

```
def print_words(word1, word2, word3="Hello", word4="Goodbye"):
    """
    prints the concatenation of all input words

    Parameters
    ----------
    word1 : str
        DESCRIPTION.
    word2 : str
        DESCRIPTION.
    word3 : str, optional
        DESCRIPTION. The default is "Hello".
    word4 : str, optional
        DESCRIPTION. The default is "Goodbye".

    Returns
    -------
    None.

    """
    assert isinstance(word1, str), "word1 must be a str"
    assert isinstance(word2, str), "word2 must be a str"
    try:
        assert isinstance(word3, str), "word3 must be a str, set to default \"Hello\""
    except AssertionError:
        word3 = "Hello"
    try:
        assert isinstance(word4, str), "word4 must be a str, set to default \"Goodbye\""
    except AssertionError:
        word4 = "Goodbye"
    
    output = word1 + word2 + word3 + word4
    print(output)
    return None


```

![img_056](./images/img_056.png)

The default value for ```word3``` is now automatically applied when ```word3``` is assigned to a value of the wrong datatype:

```
print_words("Python", "Anaconda", word3=2)
```

![img_057](./images/img_057.png)

Because the ```AssertionError``` has been handled, the error message does not display. A warning can be printed using the ```except``` code block to inform the user, that the default value has been used:

```
def print_words(word1, word2, word3="Hello", word4="Goodbye"):
    """
    prints the concatenation of all input words

    Parameters
    ----------
    word1 : str
        DESCRIPTION.
    word2 : str
        DESCRIPTION.
    word3 : str, optional
        DESCRIPTION. The default is "Hello".
    word4 : str, optional
        DESCRIPTION. The default is "Goodbye".

    Returns
    -------
    None.

    """
    assert isinstance(word1, str), "word1 must be a str"
    assert isinstance(word2, str), "word2 must be a str"
    try:
        assert isinstance(word3, str), "word3 must be a str, set to default \"Hello\""
    except AssertionError:
        print("word3 must be a str, set to default \"Hello\"")
        word3 = "Hello"
    try:
        assert isinstance(word4, str), "word4 must be a str, set to default \"Goodbye\""
    except AssertionError:
        print("word4 must be a str, set to default \"Goodbye\"")
        word4 = "Goodbye"
    
    output = word1 + word2 + word3 + word4
    print(output)
    return None


```

![img_058](./images/img_058.png)

The default value for ```word3``` is now automatically applied when ```word3``` is assigned to a value of the wrong datatype and the user is informed of this change:

```
print_words("Python", "Anaconda", word3=2)
```

![img_059](./images/img_059.png)

## Function Local Scope

Three variables will be created ```x```, ```y``` and ```z```, alongside a function ```add_numbers``` that takes two positional input arguments ```x``` and ```y```. **These should not be confused with one another and are not the same variable.**

```
x = 1
y = 2
z = 3

def add_numbers(x, y):
    """
    Returns the sum of the two input integers

    Parameters
    ----------
    x : int
        DESCRIPTION.
    y : int
        DESCRIPTION.

    Returns
    -------
    value : int
        DESCRIPTION.

    """
    value = x + y + z
    return value


result = add_numbers(x=3, y=4)


```
Functions have their local namespace. To explore this concept the debugger will be used. To use the debugger, all of the code, defining the function and calling the function will be input into the same cell. 

Under View, Show Line Numbers should be enabled:

![img_081](./images/img_081.png)

To the top select debug and then select the lower and upper line numbers to debug:

![img_082](./images/img_082.png)

Expand the debug tab and run the cell:

![img_083](./images/img_083.png)

To the right a callstack displays. It has the following buttons Continue, Stop, Next, Step In and Step Out:

![img_084](./images/img_084.png)

Selecting Next three tmes will assign the variables ```x```, ```y``` and ```z``` which belong to the global namespace of the Interactive Python Notebook file.

![img_085](./images/img_085.png)

Selecting Next again assigns the function to the object name ```add_numbers```. This is displayed as a function variable in the global namespace. The three variables ```x```, ```y``` and ```z``` and the function variable ```add_numbers``` are objects within the global namespace.

![img_086](./images/img_086.png)

Now the function call is highlighted. The function has two input arguments ```x``` and ```y``` and data must be supplied to each of these during the function call. The data 3 and 4 is provided to the functions positional input arguments ```x``` and ```y```. 

Selecting Step In will step in to the local names space of the function ```add_numbers``` where the input arguments display as local variables ```x``` and ```y```:

![img_087](./images/img_087.png)

The function has its own local namespace but can also access variables in the global namespace such as ```x```, ```y``` and ```z```.

![img_098](./images/img_098.png)

There is an ```x``` and ```y``` in the functions local namespace and a ```x``` and ```y``` in the global name space. Within the functions namespace, the variables ```x``` and ```y``` are effectively reassigned to the new values. However in the global namespace there is no change of ```x``` and ```y``` 

Selecting Next runs the line of code and ```value``` is created as another local variable within the functions namespace and has the value of 10:

![img_088](./images/img_088.png)

Selecting either Next or Step Out will Step Out of this function. ```value``` which is a local variabl within th functions namespace which had a value of 10 is returned to the global namespace. If the function call was not assigned to a variable, its representation 10 would display. In this case however the function call is assigned to the variable ```result``` so ```result``` stores this value of 10.

![img_089](./images/img_089.png)

Selecting Continue steps out of the function and into the global namespace. The global variables ```x```, ```y``` and ```result``` all display in the variable inspector. Notice that ```x``` and ```y``` are unchanged:

![img_090](./images/img_090.png)

Data from the global namespace is accessible within the functions namespace. 

Data from the functions local namespace is not accessible to the global namespace unless provided in a return statement during the function call.

If there are now only two global variables ```x``` and ```y```. The function can have two input arguments ```x``` and ```y``` which are assigned to new values during the function call. This reassigns the variables ```x``` and ```y``` within the local namespace of the function. These local variables are then later reassigned within the code block of the function and another local variable ```z``` is created. The final values of ```x```, ```y``` and ```z``` are in the functions local namespace and not accessible to the global namespace outside the function unless used within the ```return``` statement. In this case the ```return``` statement sums these local variables and this returned value is assigned to the global variable ```result```. Once again the global variables ```x``` and ```y``` are unaltered:

```
x = 1
y = 2

def add_numbers(x, y):
    """
    Returns the sum and more of the two input integers

    Parameters
    ----------
    x : int
        DESCRIPTION.
    y : int
        DESCRIPTION.

    Returns
    -------
    value : int
        DESCRIPTION.

    """
    x = x + 1
    y = y + 1
    z = 5
    value = x + y + z
    return value


result = add_numbers(x=3, y=4)


```

![img_063](./images/img_063.png)

Variables from outside a function can be modified in a function by making them global variables within the function using the statement ```global```. Notice that the values of these variables will be altered within the function.

```
x = 1
y = 2

def add_numbers():
    """
    Returns the sum and more of the two global variables
    
    Parameters
    ----------
    x : int
        DESCRIPTION.
    y : int
        DESCRIPTION.
    Returns
    -------
    value : int
        DESCRIPTION.
    """
    
    global x
    global y
    x = x + 1
    y = y + 1
    value = x + y
    return value


result = add_numbers()


```

![img_064](./images/img_064.png)

## *args and **kwargs

Up until this point, a specified number of positional and keyword input arguments have been used. 

Sometimes, it is desirable to have more flexibility and instead to have a function that accepts a variable number of input arguments. For example conceptualise a simple function that sums numbers:

```
sum_all(1)
sum_all(1, 2)
sum_all(1, 2, 3)
```

The desired output would be ```1```, ```3``` and ```6``` respectively.

This can be achieved by using ```*args``` as the input arguments. This becomes accessible as the list ```args``` within the code block of the function in the form of a list. This list can be used in a for loop which can iterate over each provided input argument to generate, in this basic sample, the sum of the arguments.

```
def sum_all(*args):
    """
    

    Parameters
    ----------
    *args : list
        List of integers.

    Returns
    -------
    summed_args : int
        summation of int values in args.

    """
    summed_args = 0
    for arg in args:
        summed_args += arg
        
    
    return summed_args


```

![img_065](./images/img_065.png)

This function works as expected:

```
sum_all()
sum_all(1)
sum_all(1, 2)
sum_all(1, 2, 3)
```

![img_066](./images/img_066.png)

A variable number of keyword input arguments can be supplied if ```**kwargs``` is supplied as the input arguments. ```kwargs``` is accessible in the code block in the form of a dictionary. This dictionary can be iterated over in a for loop. In this example a new dict ```a_dict``` is created which only has the key value pairs of keys that begin with the letter ```"a"```:

```
def a_keys(**kwargs):
    """
    

    Parameters
    ----------
    **kwargs : dict
        key, value pairs.

    Returns
    -------
    a_dict : dict
        key, value pairs with only key values
        that begin with a

    """
    print(kwargs)
    a_dict = {}
    for (key, val) in kwargs.items():
        if key[0] == "a":
            a_dict[key] = val
    
    
    return a_dict


```

![img_067](./images/img_067.png)

This can be tested using:

```
a_keys(apple=1, banana=2, apricot=3)
```

![img_068](./images/img_068.png)


## First-Class Function

The following simple function ```greeting``` can be defined.

```
def greeting(name):
    """
    prints a greeting
    Parameters
    ----------
    name : str

    Returns
    -------
    None
    """
    print(f"Hello {name}")
    return None


```

![img_091](./images/img_091.png)

This function can be treated as a variable and assigned to any other variable name. For example:

```
f = greeting
```

To the right hand side of the assignment operator, the function is being referenced and not called. Therefore, there is no parenthesis following the function name. ```f``` is essentially a copy of the original function ```greeting```. If ```f``` is input followed by open parenthesis and shift ```⇧``` and the tab ```↹``` are input, details about the input argument displays alongside the docstring provided in ```greeting```:

![img_092](./images/img_092.png)

```f``` can therefore be called using:

```
f("philip")
f("Lucie")
```

![img_093](./images/img_093.png)

Note ```f``` is not an alias to ```greeting``` but a copy. If ```greeting``` is deleted or reassigned, tis will not change the functionality of ```f```:

```
del greeting
f("Sarah")
```

![img_094](./images/img_094.png)

## Second-Order Function

The function ```greeting_function``` can be defined and configured to take in an input argument ```name``` and to return a formatted string, greeting a user using the provided ```name```:

```
def greeting_function(name):
    """
    returns a greeting
    Parameters
    ----------
    name : str
   
    Returns
    -------
    str
    """
    return f"Hello {name}"


```

A second order function ```format_greeting_function``` can be designed which takes in the first-order function ```greeting_function``` as the input argument ```welcome```. The input argument of the second order function ```welcome``` (which is a copy of the first order function ```greeting_function```) is called using the provided input argument ```user``` which is a local variable provided within the second order function. The function ```greeting_function``` has a return statement and when the copy of ```greeting_function``` is called as ```welcome```, the output is assigned to a variable ```text```. ```text``` is a local variable within the second order function ```format_greeting_function``` and is modified further before being returned by ```format_greeting_function```.

```
def format_greeting_function(welcome):
    """
    Takes in a greeting function and formats it to 
    welcome Philip

    Parameters
    ----------
    welcome : function

    Returns
    -------
    text : str
    """
    user = "Philip"
    text = welcome(user)
    text = text.upper()
    text = text.center(20, "*")
    return text


```

The ```format_greeting_function``` can be called taking in the ```greeting_function``` as an input argument:

```
format_greeting_function(greeting_function)
```

![img_095](./images/img_095.png)


## Closures

In the above section it was seen that a function can be used as an input argument for another function. It is also possible to define a function wthin a function, to make a nested function or *second-order* function.

An ```inner``` function can be defined within an ```outer``` function:

```
def outer():
    def inner():
        pass
    pass


```

![img_096](./images/img_096.png)

The return statement of a function can be used to return a function. In this example, the ```outer``` function can be used to return the ```inner``` function:

```
def outer():
    def inner():
        pass
    return inner


```

![img_097](./images/img_097.png)

Because the ```inner``` function is define within the local scope of the ```outer``` function it can access variables within the ```outer``` functions scope:

```
def outer():
    name = "Philip"
    def inner():
        return f"hello {name}"
    return inner


```

![img_099](./images/img_099.png)

Notice the subtle difference between referencing ```outer```:

```
outer
```

Calling ```outer```:

```
outer()
```

Calling ```outer``` to get ```inner``` and then calling ```inner```:

```
outer()()
```

![img_100](./images/img_100.png)

More generally, ```outer``` would be called and assigned to a variable name:

```
f_in = outer()
```

Then this variable name which is assigned to a function would be called:

```
f_in()
```

![img_101](./images/img_101.png)

Let's modify the above code so an input argument ```name``` is requested by the ```outer``` function. This input argument is accessible by the ```inner``` function:

```
def outer(name):
    def inner():
        return f"hello {name}"
    return inner


```

![img_102](./images/img_102.png)

The ```outer``` function can be called and assigned to a variable name:

```
f_in = outer("Lucie")
```

The variable ```"Lucie"``` was provided by the ```outer``` function which has finished executing but is now **enclosed** within the ```inner``` function.

```
f_in()
f_in()
```

![img_103](./images/img_103.png)

For this reason, the configuration above is known as a **closure** as variables provided from the outer function can be enclosed within the inner function.

In HTML the following tags ```<p>``` and ```<\p>``` are used to enclose a paragraph and ```<h1>``` and ```<\h1>``` are used to enclose a heading of level 1.

A closure can be defined using:

```
def html_tag(tag):
    def html_text(text):
        return f"<{tag}>{text}</{tag}>"
    return html_text


```

The outer ```html_tag``` function can be called using a provided tag.

```
para = html_tag("p")
h1 = html_tag("h1")
```

This creates the inner function with an enclosed tag, which can be called providing text to format it using the enclosed tag:

```
h1("My First Program")
para("prints")
para("Hello World")
para("Goodbye World")
```

![img_104](./images/img_104.png)

## Decorators

A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it. 

The ```decorator_function``` therefore is configured to take in an ```original_function``` as its input argument. To extend the behaviour of the ```original_function```, the ```decorator_function``` must include a nested ```wrapper_function``` which returns the ```original_function```. The ```wrapper_function``` will only include a simple print statement in this case for simplicity:

```
def decorator_function(original_function):
    def wrapper_function():
        print(f"calling the {original_function}")
        return original_function
    return wrapper_function


```

Let's use the above with a simple ```greeting_function```:

```
def greeting_function():
    """
    returns a greeting
   
    Returns
    -------
    str
    """
    return f"Hello"


```

The decorator function can be called and assigned to a variable name:

```
greeting_function_decorated = decorator_function(greeting_function)
```

The ```greeting_function_decorated``` can be referenced using:

```
greeting_function_decorated
```

It can be called using:

```
greeting_function_decorated()
```

```
greeting_function_decorated()()
```

![img_105](./images/img_105.png)

Now if instead of referencing the ```original_function``` within the return statement of the ```wrapper_function```, it is called:

```
def decorator_function(original_function):
    def wrapper_function():
        print(f"calling the {original_function}")
        return original_function()
    return wrapper_function


```

The function being decorated, ```greeting_function``` is unchanged:

```
def greeting_function():
    """
    returns a greeting
   
    Returns
    -------
    str
    """
    return f"Hello"


```

The decorator function can be called and assigned to a variable name:

```
greeting_function_decorated = decorator_function(greeting_function)
```

It can be referenced:

```
greeting_function_decorated
```

And called:

```
greeting_function_decorated()
```

![img_106](./images/img_106.png)

In the above case, the ```greeting_function``` being decorated had no input arguments. In this example, an input argument ```name``` will be added:

```
def greeting_function(name):
    """
    returns a greeting
    Parameters
    ----------
    name : str
   
    Returns
    -------
    str
    """
    return f"Hello {name}"
```

Now the return statement of the ```wrapper_function``` must call the function and provide the input argument ```name```.

```
def decorator_function(original_function):
    def wrapper_function():
        print(f"calling the {original_function}")
        return original_function(name)
    return wrapper_function


```

In order to do so, the wrapper function must supply the input argument ```name```:

```
def decorator_function(original_function):
    def wrapper_function(name):
        print(f"calling the {original_function}")
        return original_function(name)
    return wrapper_function


```

More generally ```*args``` and ```**kwargs``` will be used for the input arguments of the ```wrapper_function``` so that they can be supplied when calling the ```original_function``` within the return statement of the ```wrapper_function```

```
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"calling the {original_function}")
        return original_function(*args, **kwargs)
    return wrapper_function


```

The decorator function can be called and assigned to a variable name as before:

```
greeting_function_decorated = decorator_function(greeting_function)
```

It can be referenced:

```
greeting_function_decorated
```

And called using the input argument ```name```:

```
greeting_function_decorated("Philip")
```

![img_107](./images/img_107.png)

Normally the decorator function ```decorator_function``` is previously defined:

```
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"calling the {original_function}")
        return original_function(*args, **kwargs)
    return wrapper_function


```
It can be used to decorate a function using the ```@decorator_function``` above the original function definition for example:

```
@decorator_function
def greeting_function(name):
    """
    returns a greeting
    Parameters
    ----------
    name : str
   
    Returns
    -------
    str
    """
    return f"Hello {name}"


```

The ```@``` syntax is shorthand for assignment of the original function decorated:

```
greeting_function_decorated = decorator_function(greeting_function)
```

When the ```@``` syntax is used reassignment of the original function is carried out to the original function decorated:

```
greeting_function = decorator_function(greeting_function)
```

Therefore in this case using:

```
greeting_function("Philip")
```

will implement the decorated version of ```greeting_function```:

![img_108](./images/img_108.png)

[Home Python Tutorials](https://github.com/PhilipYip1988/python-tutorials/blob/main/readme.md)