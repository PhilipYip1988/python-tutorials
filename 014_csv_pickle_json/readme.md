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

The function takes in an iterable as an input argument which is usually an opened file. Recall a file can be opened and closed using the inbuilt function ```open``` where the 2nd input argument in ```open``` is ```"r"``` indicating read only access. To encode a file properly, the follwoign keyword arguments must be assigned to the following values ```encoding="UTF-8-Sig"``` and ```newline=""```.

```
import csv
file = open("commaseparatedvalues.csv", "r", encoding="UTF-8-Sig", newline="")
file.close()
```

![img_013](./images/img_013.png)

The csv reader function should be used on the file after it is opened and before it is closed:

```
import csv
file = open("commaseparatedvalues.csv", "r", encoding="UTF-8-Sig", newline="")
csvreader = csv.reader(file, delimiter=",")
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

Notice that each line read is a list of strings.

Recall that the class ```list``` can be used on an iterator to see all the available items left:

![img_019](./images/img_019.png)

This gives a list of lists.

As ```csvreader``` is an iterator, it can also be consumed by a for loop:

```
import csv
file = open("commaseparatedvalues.csv", "r", encoding="UTF-8-Sig", newline="")
csvreader = csv.reader(file)
for row in csvreader:
    print(row)

file.close()
```

![img_020](./images/img_020.png)


Recall that it is more common to open a file within a ```with``` code block. This code block will automatically close the file, although the close command is shown below for clarity:

```
with open("commaseparatedvalues.csv", "r", encoding="UTF-8-Sig", newline="") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
    file.close()


```    

![img_021](./images/img_021.png)

Instead of printing, the file contents can be saved to a list.

```
file_contents = []

with open("commaseparatedvalues.csv", "r", encoding="UTF-8-Sig", newline="") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        file_contents.append(row)
    file.close()


```

![img_022](./images/img_022.png)

The workflow used for the csv writer function is quite similar to that of the csv reader function. 

![img_024](./images/img_024.png)

The function also takes in an iterable as an input argument which is usually an opened file. Once again a file can be opened and closed using the inbuilt function ```open``` where in this case the 2nd input argument in ```open``` is ```"w"``` indicating write access:

```
import csv
file = open("newfile.csv", "w", encoding="UTF-8-Sig", newline="")
csvwriter = csv.writer(file)
file.close()
```

![img_025](./images/img_025.png)

The csvwriter instance has two methods ```writerow``` and ```writerows```:

![img_026](./images/img_026.png)

```writerow``` can be used to write an individual row. For example a file can be created one row at a time:

```
import csv
file = open("newfile.csv", "w", encoding="UTF-8-Sig", newline="")
csvwriter = csv.writer(file)
csvwriter.writerow(["x", "y", "z"])
csvwriter.writerow([1, 2, 3])
csvwriter.writerow([2, 4, 6])
csvwriter.writerow([3, 6, 9])
file.close()
```

![img_029](./images/img_029.png)

This file is now viewable in Windows File Explorer:

![img_030](./images/img_030.png)

And can be opened in Notepad++:

![img_031](./images/img_031.png)

Once again that it is more common to open a file within a ```with``` code block. This code block will automatically close the file, although the close command is shown below for clarity: 

```
import csv

with open("newfile.csv", "w", encoding="UTF-8-Sig", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(["x2", "y2", "z2"])
    csvwriter.writerow([1, 2, 3])
    csvwriter.writerow([2, 4, 6])
    csvwriter.writerow([3, 6, 9])
    file.close()


```    

![img_032](./images/img_032.png)

Notice that the previous file that was created has now been overridden with the new data (there is a subtle difference in the headings ```x2, y2 and z2``` are used opposed to ```x, y and z``` in the original file):

![img_033](./images/img_033.png)

Use of ```writerows``` requires the data to be in the form of a list of lists. Once again, the same data is going to be written to a file, this time slightly different headings ```x3, y3, z3``` are going to be used and a new file name ```"newfile2.csv"``` will be used:

```
import csv

data = [["x3", "y3", "z3"],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

with open("newfile2.csv", "w", encoding="UTF-8-Sig", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(data)
    file.close()
    

```        

![img_034](./images/img_034.png)

This new file can be opened and looks as expected:

![img_035](./images/img_035.png)

## Pickled Data

