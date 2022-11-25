# Pickle, JSON and CSV

## Text Data

In the Previous tutorial, a list was created and written to a text file using inbuilt Python:

```
new_file_contents = ["Hello\n",
                     "\tWorld\n"]
              
with open(file="text_file.txt", mode="w") as file_object:
    file_object.writelines(new_file_contents)
    file_object.close()


```

Recall when a file is opened using ```with```, it is automatically closed when the code block ends so the following code is equivalent:

```
new_file_contents = ["Hello\n",
                     "\tWorld\n"]
              
with open(file="text_file.txt", mode="w") as file_object:
    file_object.writelines(new_file_contents)


```

![img_001](./images/img_001.png)

The file can be seen in the JupyterLab file explorer:

![img_002](./images/img_002.png)

And within the Windows files explorer:

![img_003](./images/img_003.png)

If it is opened in Notepad++, then the hidden punctuation symbols can be viewed by selecting View → Show Symbol → Show All Characters:

![img_004](./images/img_004.png)

The hidden printer punctuation symbols New Line (Carriage Return, Line Feed) and the Horizontal Tab display:

![img_005](./images/img_005.png)

Text data can be conceptualised as a single column of horizontal rows, where each row can contain text data:

![img_006](./images/img_006.png)

## Comma Seperated Value Files

A Comma Seperated Values (CSV) uses the comma as a delimiter. 

![img_007](./images/img_007.png)

This delimiter gives a specific instruction, to move to the next column. Notice that every row in the file has one comma, meaning each row is seperated into two columns:

![img_008](./images/img_008.png)

Some programs such as Microsoft Excel or Only Office Desktop Editors WorkSheet translate the New Line (CRLF) and commas , into a grid:

![img_009](./images/img_009.png)

In Python, the ```csv``` module is used to open and save csv files. It can be imported using:

```
import csv
```

And the module docstring can be accessed using:

```
? csv
```

![img_010](./images/img_010.png)

Essentially the module has a reading api and a writing api which will use default parsing options. These default parsing options will work with files made using English (UK and USA). Other languages for example German use the ```,``` as a decimal point and the ```;``` as a delimiter and therefore require customised parsing options or dialects.

The list of identifiers from the ```csv``` module can be accessed by inputting ```csv.``` followed by a tab ```↹```:

![img_011](./images/img_011.png)

The ```reader``` functions docstring can be viewed by typing in the function name with open parenthesis followed by Shift ```⇧``` and Tab ```↹```. 

![img_012](./images/img_012.png)

The function takes in an iterable as an input argument which is usually an opened file. Recall a file can be opened and closed using:

```
import csv
file = open("commaseperatedvalues.csv", "r")
file.close()
```

![img_013](./images/img_013.png)

The csv reader function should be used on the file after it is opened and before it is closed:

```
import csv
file = open("commaseperatedvalues.csv", "r")
csvreader = csv.reader(file)
file.close()
```

![img_014](./images/img_014.png)

The csvreader instance has two attributes ```line_num``` and ```dialect```:

![img_015](./images/img_015.png)

```
csvreader.line_num
csvreader.dialect
```

In this case the line number is 0, as no data has been read from the csvreader and the dialect is the default ```Dialect``` class:

![img_016](./images/img_016.png)

If the directory function ```dir``` is used on the ```csvreader```, the datamodel identifiers are displayed:

```
dir(csvreader)
``` 

The ```__next__``` datamodel method displays meaning ```csvreader``` is an iterator.

![img_017](./images/img_017.png)

Therefore the ```next``` function can be used on the iterator. Each time a line is consumed using the ```next``` function, the line number increments

```
csvreader.line_num
next(csvreader)
csvreader.line_num
next(csvreader)
csvreader.line_num
```

![img_018](./images/img_018.png)

Each line is a single tab delimited string and that string is enclosed in an otherwise empty list.

Recall that the class ```list``` can be used on an iterator to see all the available items left:

![img_019](./images/img_019.png)

This gives a list of lists.

Notice in the above ```\t``` a tab delimiter displays inplace of the ```,``` comma  delimiter. This is to prevent confusion between the delimiter in a Python list and a delimiter in the csv file.

As ```csvreader``` is an iterator, it can also be used with a for loop:

```
import csv
file = open("commaseperatedvalues.csv", "r")
csvreader = csv.reader(file)
for row in csvreader:
    print(row)

file.close()
```

![img_020](./images/img_020.png)


Recall that it is more common to open a file within a ```with``` code block. This code block will automatically close the file, although the close command is shwon below for clarity:

```
with open("commaseperatedvalues.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
    file.close()


```    

![img_021](./images/img_021.png)

Instead of printing, the file contents can be saved to a list.


```
file_contents = []

with open("commaseperatedvalues.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        file_contents.append(row)
    file.close()


```

![img_022](./images/img_022.png)

```
file_contents = []

with open("commaseperatedvalues.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        file_contents.append(row[0])
    file.close()


```

![img_023](./images/img_023.png)