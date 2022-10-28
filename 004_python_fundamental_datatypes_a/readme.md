# fundamental datatypes

In python consider the following fundamental types of data:

* text data
* numeric data
  * whole numbers
  * numbers with a decimal point

## The string class

### quotations

For the text datatype there is the ```str``` class. ```str``` is an abbreviation for a string of characters.

Note that text contained as part of a string must be enclosed in quotations. 

![img_001](./images/img_001.png)

These quotations can either be a set of double quotations ```" "``` or a set of single quotations ```' '```. For example:

```
"hello"
'hello'
```

When text is not enclosed in quotations Python looks for an inbuilt object name, or an object that ha been assigned by the user.

```
hello
```

Python displays a ```NameError``` because it is looking for an object name which does not exist. Objects that the user has created can be found in the variable inspector or variable explorer of the IDE:

![img_002](./images/img_002.png)

In this example, no user defined variables have been assigned so the Variable Inspector is empty:

![img_003](./images/img_003.png)

The Variable Inspector can be repositioned:

![img_004](./images/img_004.png)

A variable can be assigned using:

```
hello = "hi"
```

![img_005](./images/img_005.png)

It is conversely better to conceptualise assignment as a process that occurs from the right to left. The value that is being assigned (or expression that is being calculated and then assigned) is on the right. In this case this is the string ```"hi"```:

![img_006](./images/img_006.png)

In the middle is the assignment operator ```=``` and this should be thought of as *assignment* and not *equals* like used in mathematics:

![img_007](./images/img_007.png)

The variable name otherwise known as the object name the string is being assigned to is on the left hand side. Notice that there are no quotations around an object name:

![img_008](./images/img_008.png)

When this cell is run, no output displays. This is because the output isstored in the variable name ```hello``` and this ca now be seen displayed on the Variable inspector with the name ```hello``` and content or value ```"hi"```:

![img_009](./images/img_009.png)

Now tha this object name is assigned, the top cell can be rerun.

![img_010](./images/img_010.png)

Because this object ```hello``` is now assigned, Python looks up this object and displays its value or content. Because this cell has no assignment to a new value. The content or value is displayed in the cell:

![img_011](./images/img_011.png)

Notice tat h top cellnow dislays ```[5]``` opposed to ```[1]``` which indicates the order each cell was run in the Python Kernel. This cell as ran twice at ```[1]``` and ```[5]``` but only the last run is displayed.

It is really bad practice to place cells in an inteactive notebook out of order. Normally when a notebook is reopened, the user will for to Kernel → Restart Kernel and Run All Cells...

![img_012](./images/img_012.png)

In this configuration, executing the top cell will once again result in a ```NameError``` and halt the kernel from running any further cells:

![img_013](./images/img_013.png)

The cell which assigned the variable ```hello``` can be repositioned to the top:

![img_014](./images/img_014.png)

![img_015](./images/img_015.png)

Now Restarting the Kernel and running all cells works without any errors as expected:

![img_016](./images/img_016.png)

![img_017](./images/img_017.png)

The *assignment operator* ```=``` should not be confused with the *is equal* to operator ```==``` which checks to see if the value on the right is equal to the value on the left. 

```
"hi" == "hi"
"hi" == "bye"
``` 

![img_018](./images/img_018.png)

The following will yield ```True``` and ```False``` respectively. Notice that ```True``` and ```False``` do not include quottions as they are not strings but are another ata type known as a ```bool```. Notice that they and are also capitalised. 

Python is case sensitive, so the following strings are not equal:

```
"hello" == "Hello"
``` 

![img_019](./images/img_019.png)

In addition if the variable ```hello``` is assgned but ```Hello``` is requested, a ```NameError``` will display:

```
hello = "hi"
Hello
``` 

![img_020](./images/img_020.png)

Sometimes *is equal* ```==``` is used in conjunction to *assignment* ```=```. In this case it is once again useful to conceptualise this as a process that occurs from the right to left.

```
var = "hi" == "bye"
```

To the right the equality operator is used to compare the two strings. Because they are not the same, this returns the value ```False```.

![img_021](./images/img_021.png)

The assignment operator ```=``` then assigns this value ```False```

![img_022](./images/img_022.png)

To the variable name or object name ```var``` on the left:

![img_023](./images/img_023.png)

When this cell is ran, there is no output displayed because the value ```False``` has been assigned to the variable anme or object name ```var```. This displays in the variable inspector:

![img_024](./images/img_024.png)

Python has naming conventions for variables:

* variable names should have only lower case characters
* numbers can be included in variable names but variable names cannot start with numbers
* no special characters or spaces should be used in a variable name. The only special character that can be used in a variable name is the underscore ```_``` which is used in place of a space
* variable names should be concise but descriptive

Examples include:

```
greeting = "hi"
greeting1 = "hello"
greeting_1 = "howdy"
```

A variable can be assigned: 

```
greeting = "hi"
```

![img_025](./images/img_025.png)

It can also be assigned again also know as reassignment:

```
greeting = "howdy"
```

![img_026](./images/img_026.png)

It can be reassigned again:

```
greeting = "hello"
```

![img_027](./images/img_027.png)

Notice that only the last value of the variable is stored and all previous values are disregarded.

A variable that is assigned to a value that is never intended to change is known as a constant. Constant names should be in all capitals:

```
GREETING = "hi"
```

![img_028](./images/img_028.png)

Python won't stop reassignment of a constant like other programming languages however it should be clear to another programmer that a variable name in all capitals is designed to be a constant.

If a string variable name is input followed by a dot ```.``` and tab ```↹```, a list of identifiers that can be called from a string display:

![img_029](./images/img_029.png)

These identifiers originate from the class string:

![img_030](./images/img_030.png)

The assignment operator ```=``` is used to assign instances of the string class to variable or object or instance names. This process is known as instantiation.

Another string can be instantiated using:

```
farewell = "bye"
```

In this case , the string is ```"bye"``` and is assigned to the instance name ```farewell```.

Notice on the variable inspector that both ```farewell``` and ```greeting``` are instances of the string class.

If ```farewell``` is input followed by a dot ```.``` and tab ```↹```, the same list of identifiers display:

![img_031](./images/img_031.png)

A method is essentially a function that is defined within the class. In this case the string class. If the following is input, the function is referenced:

```
farewell.capitalize
```

![img_032](./images/img_032.png)

Functions can also be called. To call a function use parenthesis after the function name. The parenthesis should enclose any input arguments expected by the string.

```
farewell.capitalize()
```

Once parenthesis are supplied pressing shift ```⇧``` and tab ```↹``` can be used to view the functions docstring as a popup balloon:

![img_033](./images/img_033.png)

The docstring gives details about the input arguments, in the case of the string methods, many of the functions don't require input arguments because the data the functions act upon is provided in the instance. In this case the data is the text ```"bye"``` and the string method ```capitalize"``` will act upon it to return the output string ```"Bye"```:

![img_034](./images/img_034.png)

The string methods ```upper```, ```lower```, ```title``` all work in a similar manner to ```captilize``` returning an uppercase, lowercase, titlecase and capitalized version of the string. This can be demonstrated by using the string:

```
greeting = "hello world!"
greeting.upper()
greeting.lower()
greeting.title()
greeting.capitalize()
```

![img_035](./images/img_035.png)

Other functions require input arguments. Input arguments can be positional where they are supplied in order or keyword where they are assigned to a temporary variable name within the function.

The string method ```format``` has ```*args``` and ```**kwargs``` as input arguments, meaning it can take in a variable number of either positional or input arguments:

![img_036](./images/img_036.png)

This method essentially allows one to create a formatted string. Variables can be inserted into the string using numeric placeholders, braces are used within the string to denote a placeholder ```{ }```. The string has to have a corresponding number of positional input arguments for each placeholder present in the string:

```
"Zero {0} One {1}".format("zero", "one")
```

![img_037](./images/img_037.png)

Alternatively named placeholder can be created. The name of the placeholders are provided as keyword input arguments that are assigned to a value when calling the ```format``` method:

![img_038](./images/img_038.png)

It is possible to create a formatted string suing the f-string syntax. The quotations in the string are prepended with f and the variable names are provided as variable names within the placeholder.

Two variables can be created:

```
greeting = "hello"
customer = "world"
```

These variables can be supplied as positional input arguments with numeric placeholders using the ```format``` method:

```
"{0} {1}!".format(greeting, customer)
```

These variables (on the right hand side) can be assigned to the keyword input arguments (left hand side) within the parenthesis of the ```format``` method. These keyword input arguments are then accessible within the string as placeholders and get replaced by the values of the keyword input arguments which becomes the value of the variables.

```
"{greeting} {customer}!".format(greeting=greeting, 
                                customer=customer)
```

The fstring prepends the string with ```f``` and placeholders can be used directly to contain existing variable names:

```
f"{greeting} {customer}!"
```

![img_039](./images/img_039.png)

So far all the strings created have been alphanumerical only. It is possible to create a string which has symbols. However some of the symbols are recognised by Python as code. Quotations ```" "``` or ```' '``` are recognised as special characters which denote the beginning and end of a string. Notice the syntax highlighting above uses the first set of quotations to make a string. Python is then seen as an object name and then there is an empty string.

![img_040](./images/img_040.png)

It is possible to use these to use an outer set of quotations to create a string which contains one of the other quotations.

![img_041](./images/img_041.png)

![img_042](./images/img_042.png)

To include both sets of quotations within a string, an escape character is required. 

![img_043](./images/img_043.png)

The symbol ```\``` is used to insert an escape character. ```\"``` denotes the ```"``` is to be inserted as an escape character in the string.

![img_044](./images/img_044.png)

When a string is outputted to a cell, its representation is displayed which is essentially the syntax required to recreate the string. The ```print``` function can be used to print the string which will display what the string looks like once formatting is applied. ```print``` is an inbuilt function and is designed to work with multiple object types such as strings or numeric datatypes. It is used directly and the object to be printed is supplied as a positional input argument.

This differs from the string method ```capitalize``` which is designed to only work with string datatypes and is therefore called from a string.

![img_045](./images/img_045.png)

Inputting the ```print``` function followed by parenthesis and pressing shift ```⇧``` and tab ```↹``` will once again view the functions docstring as a popup balloon:

![img_046](./images/img_046.png)

The ```value``` and ```...``` indicate that a variable number of input arguments can be supplied. 

The keyword input argument ```sep``` an abbreviation for seperator is assigned to ```" "``` a single space and ```end``` is assigned to ```"\n"``` which means an escape charater is inserted and in this case ```n``` is an escape character for a new line.

The keyword input arguments have default values ```sep=" "``` and ```end="\n"```. When they are not supplied the print function will print with default behaviour.

```
print("hello", "world")
print("hello", "world")
print("hello", "world")
```

The values however can be overidden which will change the behaviour of the print function or that single call. For example to end with a new line and then tab and to print with no spaces between input arguments:

```
print("hello", "world", end="\n\t")
print("hello", "world")
print("hello", "world", sep="")
```

![img_047](./images/img_047.png)

The character ```\``` is used to insert an escape character but is also used in a file path for example ```C:\Windows```. To insert ```\``` as an escape character use ```\\```, recall the first ```\``` means insert an escape character and the second ```\``` indicates the escape character to be inserted. Once again observe the difference between the cell output which shows the representation of the string with instructions to reproduce the string with the print statement which displays the formatted version of the string:

```
"C:\\Windows"
print("C:\\Windows")
```

![img_048](./images/img_048.png)

Because file paths are copied and pasted frequently, it becomes cumbersome to replace every instance of ```\``` with ```\\```. 

```
"C:\\Windows\\System32"
```

A relative string or rstring prepends the string with ```r``` and every ```\``` supplied is taken to be a ```\\```.

```
"C:\\Windows\\System32"
r"C:\Windows\System32"
print(r"C:\Windows\System32")
```

![img_049](./images/img_049.png)

The del function

The dir function

Datamodel methods

Once ints are discussed.

The input function






















### special string functions 

The string function has a special method ```__add__```. This special function does not display when we type in the variable name and press ```.``` and tab ```↹```. However if we type in the function name with open parenthesis and press shift ```⇧``` and tab ```↹``` we can see details about its docstring. In this case we see we have a single positional input argument ```value```:

![31_string_methods](./images/31_string_methods.PNG)

We can use this method to add the string value to the string we are calling the function from. For example:

```
greeting.__add__(farewell)
```

![32_string_methods](./images/32_string_methods.PNG)

Notice that the text of the 1st string is immediately followed by the text of the 2nd string and there is no spacing. This is known as concatenation.

Because concatenation of strings is so commonly carried out it uses the special function ```__add__```which is mapped to the ```+``` operator. This means the following two lines of code are equivalent:

```
greeting.__add__(farewell)
greeting + farewell
```

![33_string_methods](./images/33_string_methods.PNG)

And therefore if we wanted a space between the two words, we could easily use:

```
greeting + " " + farewell
```

![34_string_methods](./images/34_string_methods.PNG)

## numeric variables

### integers and floating point numbers

There are two types of numeric datatypes, an int which is an abbreviation for an integer and is a discrete full number and there is a float which is an abbreviation for floating point number.

We can assign four variables to numeric values using:
```
num1 = 1
num2 = 3.14
num3 = 3.0
num4 = 3.
```

We can see in the Variable Inspector that any number which includes a ```.``` in its value is assigned to a float.

![35_numeric_datatypes](./images/35_numeric_datatypes.PNG)

### numeric functions

Like strings, numbers have a number of functions which can be accessed by typing in the numbers variable name followed by a dot ```.``` and tab ```↹```:

![36_numeric_datatypes](./images/36_numeric_datatypes.PNG)

### special numeric functions

Most of the functions commonly used with a number are however setup as special numeric methods mapped to an operator. In the case of a number the special numeric method ```__add__``` is mapped to ```+``` performs addition of two numbers. Likewise:

|special function|operator|function|
|---|---|---|
|```__add__```|```+```|adds two numbers|
|```__sub__```|```-```|subtracts two numbers|
|```__mul__```|```*```|multiplies two numbers|
|```__pow__```|```*```|raises the first number to the power of the second number|
|```__floordiv__```|```//```|integer floor division of the first number by the second number|
|```__mod__```|```%```|integer floor remainder of the first number by the second number|
|```__div__```|```/```|float division of the first number by the second number|

**Be careful to distinguish the difference between the string special function ```+``` which performs concatenation of two strings and the numeric special function ```+``` which performs addition of two numbers.**

For example:

```
1 + 2
1 - 2
2 * 3
5 ** 2
6 // 4
6 % 4
6 / 4
```

![37_numeric_functions](./images/37_numeric_functions.PNG)

### float precision

The reason numbers are separated out into integers and floating point numbers is due to a computer having a finite number of bytes to store data. floating point numbers are therefore approximated to conserve memory. There can sometimes be unexpected results in calculations due to rounding. For example:

```
0.1 + 0.2
```

![38_numeric_datatypes](./images/38_numeric_datatypes.PNG)

And if we use the is equal to operator ```==``` which checks equality of both sides of the equation we get which might perhaps be an unexpected ```False```

```
0.1 + 0.2 == 0.3
```

![39_numeric_datatypes](./images/39_numeric_datatypes.PNG)

This is because the left hand side of the equation is rounded to be very slightly larger than the right hand side of the equation:

![40_numeric_datatypes](./images/40_numeric_datatypes.PNG)

### comparison operators

We have just seen an example of 2 of the comparison operators used to compare two numbers. There are 6 comparison operators in total:

|special function|operator|function|
|---|---|---|
|```__lt__```|```<```|checks if the left hand side is less than the right hand side|
|```__le__```|```<=```|checks if the left hand side is less than or equal to the right hand side|
|```__eq__```|```==```|checks if the left hand side is equal to the right hand side|
|```__neq__```|```!=```|checks if the left hand side is **not** equal to the right hand side|
|```__gt__```|```>```|checks if the left hand side is greater than the right hand side|
|```__ge__```|```>=```|checks if the left hand side is greater than or equal to the right hand side|

### the round function

Python has an inbuilt ```round``` function. If we type in the function name with open parenthesis and press shift ```⇧``` and tab ```↹``` we can see details about its docstring. 

![41_round_function](./images/41_round_function.PNG)

The first positional argument is the number or calculation which yields a number to be rounded and the second is the number of decimal places to specify. Once rounded accordingly, the comparison operator works as one might expect:

```
round(0.1+0.2, 6)
round(0.1+0.2, 6) == 0.3
```

![42_round_function](./images/42_round_function.PNG)

### boolean numbers

The ```bool``` is an abbreviation for boolean and has two values ```False``` or ```True```. We have seen these boolean values when we used the comparison operators above. These two values map to two values of binary integers ```0``` and ```1``` and are therefore considered numeric. For example ```False + True``` can be conceptualised as ```0``` + ```1``` and ```False * True``` can be conceptualised as ```0``` * ```1```:

![61_boolean_values](./images/61_boolean_values.PNG)

Although boolean values can be used as ```0``` and ```1``` with numeric operators. It is more common to use them with the ```and``` or ```or``` operator which combines the conditions.

condition 1 ```and``` condition 2 will only be ```True``` if both condition 1 **and** condition 2 are ```True```:

```
(True) and (True)
(True) and (False)
(False) and (True)
(False) and (False)
```

condition 1 ```or``` condition 2 will be ```True``` if either condition 1 **or** condition 2 are ```True```:

```
(True) or (True)
(True) or (False)
(False) or (True)
(False) or (False)
```

![62_boolean_values](./images/62_boolean_values.PNG)

The operator ```not``` will invert a condition:

```
not True
```

![66_not](./images/66_not.PNG)

### parenthesis

The following code becomes hard to read. It is not obvious what operation occurs first:
 
```
1 > 5 or 1 < 2
```

When comparing conditions, parenthesis are normally used to enclose each condition:

```
(1 > 5) or (1 < 2)
```

![63_boolean_values](./images/63_boolean_values.PNG)

Both expressions are on the left hand side and the right hand side of the or operator are enclosed in single parenthesis therefore it doesn't matter which expression we tackle first:

<pre>
<b>(</b>1 > 5<b>)</b> or (1 < 2)
</pre>

This therefore becomes and we can now tackle the parenthesis on the right hand side:

<pre>
False or <b>(</b>1 < 2<b>)</b>
</pre>

Then:

```
False or True
```

This finally becomes:

```
True
```

Likewise for a more complicated expression, we can use multiple parenthesis:

```
(1 > 2) and ((1 > 5) or (1 < 2))
```

The left hand side is enclosed in single parenthesis right hand side is enclosed in double parenthesis, therefore we tackle the right hand side first:

<pre>
(1 > 2) and <b>(</b>(1 > 5) or (1 < 2)<b>)</b>
</pre>

Then within this double bracket, both conditions around the ```or``` operator are enclosed in single parenthesis, so it doesn't matter which operation we carry out first, so we will start with the left hand side expression:

<pre>
(1 > 2) and (<b>(</b>1 > 5<b>)</b> or (1 < 2))
</pre>

<pre>
(1 > 2) and <b>(</b>False or (1 < 2)<b>)</b>
</pre>

Now this calculated, we can tackle the right hand side expression:

<pre>
(1 > 2) and (False or <b>(</b>1 < 2)<b>)</b>)
</pre>

<pre>
(1 > 2) and (False or True)
</pre>

Now the left and right hand side of the ```and``` operator are enclosed in single parenthesis and it doesn't matter which side we carry out first. We will continue with the right hand side:

<pre>
(1 > 2) and <b>(</b>False or True<b>)</b>
</pre>

<pre>
(1 > 2) and True
</pre>

Now that the right hand side is tackled, we tackle the left hand side which is single parenthesis:

<pre>
<b>(</b>1 > 2<b>)</b> and True
</pre>

<pre>
False and True
</pre>

This finally becomes:

```
False
```

![64_boolean_values](./images/64_boolean_values.PNG)

Parenthesis are used to set order of preference for other numeric operations. For example, if you have a look at:

```
1 + 5 * 3
```

If you assume the operators are carried out from left to right, you may calculate:

```
6 * 3
```

Which is:

```
18
```

However by default multiplication and division operations take precedence over addition and subtraction and the result is actually:

```
1 + 15
```

Which is:

```
16
```

The order or precedence can be changed using parenthesis which take the highest precedence:

```
(1 + 5) * 3
```

Is:

```
18
```

And:

```
1 + (5 * 3)
```

Is:

```
16
```

![65_parenthesis](./images/65_parenthesis.PNG)

The order of precedence is:
* parenthesis ```( )```
* exponent ```**```
* multiplication ```*```, float division ```/```, floor division ```//```, modulus ```%```
* addition ```+```, subtraction ```-```


## working between numeric and text variables

### indexing

A string can be regarded as a collection of characters. The string "hello" for example has 5 characters. The ```len``` function can be used to determine the number of characters in an inbuilt collection such as a string. For example:

```
len("hello")
```

![43_indexing](./images/43_indexing.PNG)

integers are used commonly through Python for tasks such as indexing, in the case of the string "hello" there are 5 characters and we index to select one of these characters using an integer. Notice however that when we use the integer ```1``` we are presented with the second letter in the string ```"e"```.

```
"hello"[1]
```

This is because in Python we count from a lower bound of 0 and go up to but not including the upper bound. If we attempt to index using an integer of ```5``` we are informed that the string index is out of range.

![44_indexing](./images/44_indexing.PNG)

It is possible to index using the negative integer, the value before 0 is ```-1``` giving the last letter of the string ```"o"``` and we can go back to the front of the string by using a value of ```5```, recalling that the length of the string is ```5```. 

```
"hello"[len("hello")-1]
"hello"[-len("hello")]
```

![45_indexing](./images/45_indexing.PNG)

### TypeError

Attempting to add a numeric value to a string will yield a TypeError:

```
5 + "hello"
```

![46_type_errors](./images/46_type_errors.PNG)

This is because the ```__add__``` method configured for a text datatype performs concatenation and the ```__add__``` method for a numeric datatype performs addition. The operation above is undefined and hence Python doesn't know what to do an returns a TypeError.

There are some operations that can be carried out between a string and an integer value however such as:

```
5 * "hello"
```

which perform string replication:

![47_string_replication](./images/47_string_replication.PNG)

One needs to be careful when working between the different datatypes. This is particularly the case when working with strings that look like numbers:

```
"5" + "5"
```

![48_string_concatenation](./images/48_string_concatenation.PNG)

### the input function

The input function always returns a string. If we type in the function ```input(``` with open parenthesis and press shift ```⇧``` and tab ```↹``` we can see details about its docstring.

![49_input_function](./images/49_input_function.PNG)

We have an input argument ```prompt``` which we can assign to a string:

```
input("Input your name: ")
```

When this cell is ran, it will wait for user to input some text into the prompt:

![50_input_function](./images/50_input_function.PNG)

I will input ```Philip```:

![51_input_function](./images/51_input_function.PNG)

Notice that I didn't supply quotations but the output of the cell is ```"Philip"```:

![52_input_function](./images/52_input_function.PNG)

I can assign this output to a variable which I can use within a formatted string within the print function:

```
name = input("Input your name: ")
print(f"Hello {name}")
```

![53_input_function](./images/53_input_function.PNG)

### casting

Updating to prompt for two numbers and attempting to add them will lead to unexpected results. This is because the two numbers are read in as strings and string concatenation is used with he ```+``` operator:

```
num1 = input("Input a number: ")
num2 = input("Input a number: ")
print(f"{num1}+{num2}={num1+num2}")
```

![54_input_function](./images/54_input_function.PNG)

To resolve this we can cast between the datatypes using ```int```, ```float``` and ```str```. Let's update the following code to cast both input strings to integers.

```
num1 = input("Input a number: ") #num1 is a str
num1 = int(num1) #num1 is an int
num2 = input("Input a number: ") #num2 is a str
num2 = int(num2) #num2 is an int
print(f"{num1}+{num2}={num1+num2}")
```

![55_input_function](./images/55_input_function.PNG)

This can be simplified by using:

```
num1 = int(input("Input a number: "))
num2 = int(input("Input a number: "))
print(f"{num1}+{num2}={num1+num2}")
```

![56_input_function](./images/56_input_function.PNG)

### formatted strings with numeric variables

We have seen earlier, how to use a formatted string to include a variable within a string to print. We can include text and numeric variables:

```
a = "hello"
b = 1
c = 1.1
print(f"a is {a}, b is {b} and c is {c}.")
```

![57_formatted_strings](./images/57_formatted_strings.PNG)

Sometimes we wish to further format the way each variable is printed, such as the number of spaces the variable occupies in the case of a string or int and the number of decimal places for a floating point number. We can see the following example has a large number of decimal places:

```
a = "hello"
b = 1
c = 0.1 + 0.2
print(f"a is {a}, b is {b} and c is {c}.")
```

![58_formatted_strings](./images/58_formatted_strings.PNG)

After the variable we can use ```:``` to specify the datatype:

* ```:s``` is a format specifier to format the variable as a ```str```. 
    * The number of spaces can be specified before the format specifier, for example ```:10s``` will indicate that you wish the string to occupy 10 spaces.
    * If prefixed with a 0 trailing zeros will be added after the string.
* ```:d``` is a format specifier for signed decimal integers. 
    * The number of spaces the number can once again be specified before the format specifier, for example ```:5d```. 
    * If prefixed with a 0, trailing zeros will be added.
* ```:f``` is a format specifier for a floating number format. 
    * The number of digits displayed after the decimal point by default is 6. 
    * This can be altered using a ```.``` prefix followed by specification of the number of digits, for example ```:.10f```.
    * The total number of digits can be specified before this ```.```, for example ```:15.10f```
    * If prefixed with a 0, trailing zeros will be added.
* ```:g``` is an adaptive format specifier for a floating number format that will automatically adapt. 
    * This will adapt according to the float displaying the number in standard notation if it is in the range <10000 or >0.0001 and uses scientific notation outwith this range e-4 or <e4 respectively.  
    * If a 0 is placed in front of this number, trailing zeros will be added.
    
![59_formatted_strings](./images/59_formatted_strings.PNG)

Return to:

[Home](../../../)
