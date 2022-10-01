# Objects

Python is an object orientated programming language. This tutorial will briefly recap over the concept of variables and focus on custom functions.

## Variables

Variables can be created by assigning a value to an object name using the assignment operator ```=```.

```
var1 = 1
var2 = 2.1
var3 = "hello"
var4 = ["apples", "bananas", "grapes"]
```

Once created, these variables display on the variable explorer.

![img_000](./images/img_000.png)

![img_001](./images/img_001.png)


## Functions

### Function Definition

Instead of using the assignment operator ```=```, a function is defined to an object name using the ```def``` keyword. Function definition is typically more complicated than variable assignment, as functions have input arguments and also include a function code block.

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

When the function is defined, it does not display on the variable explorer. However beginning to type the functions name in a cell, will display the function name as a an object. The object displays as a function. 

![img_001](./images/img_001.png)

![img_009](./images/img_009.png)


### Calling a Function

If the function name is typed into a cell. The output of the cell states that the object is a function, giving some details about the location where the function is defined.

```
fun_name
```

![img_010](./images/img_010.png)

To call a function, the function name must be followed by a set of parenthesis ```( )```. These parenthesis should include the values of any input arguments, for each input argument from the function definition. In this example, no input arguments were included in the definition of ```fun_name```, so the parenthesis should be left empty.

```
fun_name()
```

![img_011](./images/img_011.png)

Notice that the print statement in the functions code block is now executed.

The output of a function call, can be assigned to a variable. For example.

```
fun_out = fun_name()
```

![img_012](./images/img_012.png)

![img_013](./images/img_013.png)

Notice that the variable displays on the variable explorer as a ```NoneType``` object. This is because the last line in the functions code block is ```return None```.

### return Statement

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

In the first case, a value is printed to the cell output. In the second case, the value returned is displayed at the cell output.

The difference can be seen more clearly, when the functions are called and assigned to variables.

```
print_out = print_hello()
return_out = return_hello()
```

![img_015](./images/img_015.png)

![img_016](./images/img_016.png)

Notice that there is still a cell output when the ```print_hello``` function is used, because this function uses a print statement. The variable ```print_out``` has the value ```None``` because this function has a ```return None``` return statement.

In constrast there is no cell output when the ```return_hello``` function is used, because this function has returned the value to the variable ```return_out```. ```return_out``` can be seen to have the value ```"Hello"``` on the variable explorer.

The behaviour of the ```"print_hello"``` function does not change if the ```return None``` return statement is removed.

```
def print_hello():
    print("Hello")


```

```
print_out = print_hello()
```

![img_017](./images/img_017.png)

![img_018](./images/img_018.png)

This is because ```None``` is the default return value.

### Input Arguments

A simple function can be defined which has a single input argument ```value```. This function will return this input argument ```value``` unaltered.

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

If the function is called with an input argument, it will run as expected. The new variables ```var1``` and ```var2``` will display on the variable explorer.

```
var1 = return_value("Hello")
var2 = return_value(value="Hello")
```

![img_021](./images/img_021.png)

![img_022](./images/img_022.png)

In the above case, when assigning the output of the function to ```var1```, the function was called by providing a singular positional input argument. When using positional input arguments, they need to be provided in the correct order, matching the order of the function definition.

When assigning the output of the function to ```var2```, the function was called by explicitly defining a variable name and assigning it to a value. In such a scenario, the order of the positional input arguments can be changed provided that all the positional input arguments are supplied. In general however it is recommended to maintain the order of the positional input arguments.


### docstring

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

![img_025](./images/img_025.png)

![img_026](./images/img_026.png)

Another function can be defiend which coutns the number of vowels within a word. In this example the code block of the function body contains a nested for loop. The input argument ```word``` is a string and the return value ```vowel_count``` is an integer.

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

![img_027](./images/img_027.png)

This function can be tested using the input string ```"anaconda"```.

```
word1 = "anaconda"
vowel_n = count_vowels(word1)
```

![img_028](./images/img_028.png)

![img_029](./images/img_029.png)

Each function can only have one return statement. However this return value can be a collection such as a list or a tuple. The function above can be midified to return a list containing two values, the vowel count and the consonant count. Once again the docstring should outline clearly what each input argument is and what each value in the return list is.

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

![img_030](./images/img_030.png)

This function can be once again be tested using the input string ```"anaconda"```. 

```
word1 = "anaconda"
[vowel_n, cons_n] = count_vowels_cons(word1)
```
![img_031](./images/img_031.png)

![img_032](./images/img_032.png)

The list collection can also be unpacked using.

```
vowel_n, cons_n = count_vowels_cons(word1)
```

![img_033](./images/img_033.png)

### Positional and Keyword Input Arguments

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

**However this is generally bad practice*** and it is better practice to maintain the order of the positional input arguments to prevent any confusion. 

The more conventional syntax used to call the function above is of the form:

```
print_words("Python", "Anaconda", word3="pip", word4="mamba")
print_words("Python", "Anaconda", word3="pip")
print_words("Python", "Anaconda", word4="mamba")
print_words("Python", "Anaconda")
```

![img_039](./images/img_039.png)

### Function Local Scope

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

```
count_vowels("hello")
```




### Asserting Input Arguments


### *args and **kwargs


## lambda Expressions