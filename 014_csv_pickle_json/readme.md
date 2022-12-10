# Text, CSV, Pickle and JSON Data

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

The function takes in an iterable as an input argument which is usually an opened file. Recall a file can be opened and closed using the inbuilt function ```open``` where the 2nd input argument in ```open``` is ```"r"``` indicating read only access. To encode a file properly, the following keyword arguments must be assigned to the following values ```encoding="UTF-8-Sig"``` and ```newline=""```. "UTF-8-Sig" includes a signature otherwise known as a Byte Order Marker BOM. If "UTF-8" is used opposed to "UTF-8-Sig" the BOM will be read in as additional data:

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

The ```pickle``` module can be used to create portable "pickled" serialised representations of Python objects. Each "pickled" serialised representation is a byte string. These byte strings can be used to transfer Python objects for example over to simple hardware using a serial port or to a file which can be reopened in another Python session.

It can be imported using:

```
import pickle
```

And the module docstring can be accessed using:

```
? pickle
```

![img_036](./images/img_036.png)

There are four main functions: 

```dumps``` dump string which creates a pickled string from an object.

```loads``` load string which unpickles a pickled string returning the object.

And:

```dump``` dump file which creates a pickled string from an object that is stored as a new row in a file.

```load``` load file which unpickles a pickled string from the current row in a file returning the object.

The docstring for the dump string ```dumps``` function can be examined and takes in a Python object as a positional input argument. The ```protocol``` keyword input argument and other keyword input arguments can be left at their default values: 

![img_037](./images/img_037.png)

A simple variable ```x``` can be created and dump string can be used to dump it to a pickled string:

```
import pickle
x = 11.5
pickled.dumps(x)
```

![img_038](./images/img_038.png)

This pickled string can be assigned to a new object name:

```
import pickle
x = 11.5
x_pickled = pickled.dumps(x)
```

![img_039](./images/img_039.png)

The object ```x_pickled``` is a ```byte``` otherwise known as a byte string. If ```x_pickled.``` is input followed by a tab ```↹``` a list of identifiers displays:

![img_040](./images/img_040.png)

The ```hex``` function can be used to display the byte string in hexadecimal which is slightly easier to read:

```
x_pickled.hex()
```

![img_041](./images/img_041.png)

The ```type``` and ```len``` functions can be used on ```x_pickled```:

```
type(x_pickled)
len(x_pickled)
```

![img_042](./images/img_042.png)

The type is ```bytes```  otherwise known as a byte string. 

The ```int``` alternative constructor ```from_bytes``` can be used to convert this ```byte``` into an integer. Recall that an alterative constructor is a class method, called from the class. The docstring can be viewed by using Shift ```⇧``` and Tab ```↹```:

![img_043](./images/img_043.png)

The alternative constructor needs two positional input arguments, the ```bytes``` object and the ```byteorder``` which is ```big``` endian for a pickled string. As an integer, this number can be cast into a hexadecimal and binary number using the ```hex``` and the ```bin``` functions respectively:

```
int.from_bytes(x_pickled, "big")
hex(int.from_bytes(x_pickled, "big"))
bin(int.from_bytes(x_pickled, "big"))
```

![img_044](./images/img_044.png)

Notice that the ```hex``` method of the byte array and casting to ```int``` and then ```hex``` lead to the same results:

![img_045](./images/img_045.png)

The ```byte``` cast to an ```int``` and then ```binary``` number can be cast to a ```str```. To make it more readible, the binary prefix can be deleted and a space can be placed in after every 8 bits (1 byte) using a for loop:

```
bin_num = bin(int.from_bytes(x_pickled, "big"))
bin_num_str = str(bin_num)
bin_num_str
bin_num_str = bin_num_str[2:]
bin_num_str

bin_num_str2 = ""
for idx, letter in enumerate(bin_num_str):
    if (idx > 0) and (idx % 8 == 0):
        bin_num_str2 += " "
    bin_num_str2 += letter

bin_num_str = bin_num_str2
del(bin_num_str2)
bin_num_str
```

![img_046](./images/img_046.png)

This gives the number:

**10000000** 00000100 10010101 00001010 00000000 00000000 00000000 00000000 00000000 00000000 00000000 01000111 01000000 00100111 00000000 00000000 00000000 00000000 00000000 00000000 **00101110**

A serial port with a 9600 baud rate is setup to process 9600 bits per second. The serial port takes in a digital signal like the number above where ```1``` is a voltage of about 12 V (known as High) and ```0``` is a voltage around 0 V (known as Low). These 168 bits would therefore take 0.0175 s to transfer.

The first and the last byte are Byte Order Markers (BOMs):

0b**10000000**
0x**80**

0b**00101110**
0x**2e**

If ```x``` is changed to a different variable such as the string ```"hello"``` and the code rerun:

![img_047](./images/img_047.png)

The byte array is now:

**10000000** 00000100 10010101 00001001 00000000 00000000 00000000 00000000 00000000 00000000 00000000 10001100 00000101 01101000 01100101 01101100 01101100 01101111 10010100 **00101110**

The code above can be placed into a function:

```
import pickle

def pickled(obj):
    obj = pickle.dumps(obj)
    obj = bin(int.from_bytes(obj, "big"))
    obj = str(obj)
    obj = obj[2:]
    obj2 = ""
    for idx, letter in enumerate(obj):
        if (idx > 0) and (idx % 8 == 0):
            obj2 += " "
        obj2 += letter
    return(obj2)

pickled_print("hello")
```

![img_048](./images/img_048.png)

This function may be used to inspect the byte of the pickled objects using binary representation. The binary array of simple integers displays a byte within the array that counts in a similar manner to an integer:

```
for num in range(10):
    print(pickled(num))
```

![img_049](./images/img_049.png)

The binary array of single letters displays a byte within the array that counts in a similar manner to an integer. Notice that there is an offset:

```
for letter in "abcdefgh":
    print(pickled(letter))
```

![img_050](./images/img_050.png)

There is because the alphabetical character ```"a"``` is the 97th character mapped to the underlying integer sequence. Therefore in this case, counting begins at 97.

```
ord(a)
bin(ord(a))
```

![img_052](./images/img_052.png)

The binary array of floating points displays four bytes in memory which corresponds to the IEEE 754 standard for binary 32: 

```
for num in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]:
    print(pickled(num))
```

![img_051](./images/img_051.png)

Returning to the case where:

```
import pickle
x = 11.5
x_pickle = pickled.dumps(x)
```

The docstring for the dump string ```loads``` function can be examined and takes in a pickled data object as a positional input argument. The keyword input arguments can be left at their default values: 

![img_053](./images/img_053.png)

The pickled data ```x_pickle``` can be unpickled using:

```
x2 = pickled.loads(x_pickle)
x2
```

![img_054](./images/img_054.png)

Notice that ```x2``` has the same value as the original variable ```x```.

The dump file ```dump``` method is similar to the dump string ```dumps``` method, except the pickled object is dumped to a file. This file must be provided as an input argument:

```
pickle.dump()
```

![img_055](./images/img_055.png)

The file must be opened with write permissions ```"w"``` and be configured for binary ```"b"```:

```
import pickle
file = open("newfile.pkl", "wb")
pickle.dump(11.5, file)
pickle.dump("hello", file)
pickle.dump([1, 2, 3, 4, 5], file)
file.close()
```

![img_056](./images/img_056.png)

The file created can be viewed in Windows File Explorer:

![img_057](./images/img_057.png)

If the file is opened in Notepad or Notepad++, it will be viewed using UTF-8 or ASCII encoding and won't make much sense:

![img_058](./images/img_058.png)

The text in Notepad++ can be highlighted and then converted to Hex using Plugins → Converter → ASCII -> Hex:

![img_059](./images/img_059.png)

The pickled content can then be viewed in Hex:

![img_060](./images/img_060.png)

A file is usually opened using a with code block which automatically closes the file when the code block terminates. For clarity the file is explicitly closed:

```
import pickle

with open("newfile.pkl", "wb") as file:
    pickle.dump(11.5, file)
    pickle.dump("hello", file)
    pickle.dump([1, 2, 3, 4, 5], file)
    file.close()
```    

![img_061](./images/img_061.png)

The load file ```load``` method is similar to the load string ```loads``` method, except the pickled object is loaded from a file opposed to a string. This file must be provided as an input argument:

```
pickle.load()
```

![img_062](./images/img_062.png)

The file must be opened with read permissions ```"r"``` and be configured for a byte string ```"b"```. Each item can be unpickled and loaded using:

```
with open("newfile.pkl", "rb") as file:
    print(pickle.load(file))
    print(pickle.load(file))
    print(pickle.load(file))
    file.close()
```

![img_063](./images/img_063.png)

Notice that the object name or variable name itself is not saved to the pickled file. It is quite common to save a single pickled object to a file and save the file as the intended variable name for the object. For example:

```
with open("xdata.pkl", "wb") as file:
    pickle.dump([1, 2, 3, 4, 5], file)
    file.close()
```  

```
with open("xdata.pkl", "rb") as file:
    xdata = pickle.load(file)
    file.close()
```  

```
xdata
```

![img_064](./images/img_064.png)

## JSON Data

pickle is Python specific and has support for pretty much all Python datatypes however has the disadvantage that it is Python specific and is not very user readible. 

Another common datatype is the JavaScript Object Notation (JSON) that is more user readible than pickled data. The JSON syntax originated from JavaScript but has become a commonly used standard data stream and most data on a website is stored in JSON for example.

Because it is in JavaScript, there are slight conversions between a JavaScript object and an equivalent Python object due to subtle differences in programming language syntax. Not all Python objects are supported as they do not have a JavaScript equivalent. The JSON module essentially carries out all the supported conversions. It can be imported using:

```
import json
```

Some details about the module can be seen by looking at the modules docstring:

```
? json
```

![img_065](./images/img_065.png)

There are four main functions, similar to pickle: 

```dumps``` dump string which creates a json string from an object.

```loads``` load string which unpickles a json string returning the object.

And:

```dump``` dump file which creates a json string from an object that is stored as a new row in a file.

```load``` load file which unpickles a json string from the current row in a file returning the object.

The ```dumps``` function can be used to examine the equivalent JavaScript notation for common Python objects:

![img_066](./images/img_066.png)

An integer gets converted into a string:

```
json.dumps(1)
```

![img_067](./images/img_067.png)

A float also gets converted into a string:

```
json.dumps(1.5)
```

![img_068](./images/img_068.png)

A boolean value gets converted into a string that is lower case:

```
json.dumps(True)
```

![img_069](./images/img_069.png)

A complex number is not supported, giving a ```TypeError``` because the Complex number is not JSON Serializable:

```
json.dumps(1 + 2j)
```

![img_070](./images/img_070.png)

A string gets enclosed in a second set of quotations:

```
json.dumps("apples")
json.dumps('apples')
```

![img_071](./images/img_071.png)

Unicode characters can be created in Python using the ```chr``` function, usually with a hexadecimal number. These get converted into a unicode string in JSON:

```
chr(0x394)
json.dumps(chr(0x394))
```

![img_072](./images/img_072.png)

```
chr(0x394)+"t"
json.dumps(chr(0x394)+"t")
```

![img_073](./images/img_073.png)

A Python list gets enclosed in quotations. Notice the strings contained within the list are not doubly quotated like they were when they were standalone strings. This is because the outer list collection containing them is cast into a string using single quotations and these single quotations denote the list which includes all the enclosed strings in double quotations are part of this list:

```
json.dumps(["Apples", "Bananas", "Grapes"])
```

![img_074](./images/img_074.png)

There is no tuple counterpart in JSON, so a Python tuple gets cast to a list and gets enclosed in quotations:

```
json.dumps(("Apples", "Bananas", "Grapes"))
```

![img_075](./images/img_075.png)

JSON is typically configured for Python dictionaries and a ```TypeError``` because the set is not JSON Serializable:

```
json.dumps({"Apples", "Bananas", "Grapes", "Grapes"})
```

![img_076](./images/img_076.png)

A set can be cast into a list and then converted:

```
json.dumps(list({"Apples", "Bananas", "Grapes", "Grapes"}))
```

![img_077](./images/img_077.png)

A Python dictionary gets enclosed in quotations:

```
json.dumps({"r": "red",
            "g": "green",
            "b": "blue"})
```

![img_078](./images/img_078.png)

Other Python specific objects for example range objects are not serializable and generally have to be cast into another datatype such as a list:

```
json.dumps(range(0, 10))
json.dumps(list(range(0, 10)))
```

![img_079](./images/img_079.png)

JSON data can be converted into a Python format using the function ```loads```:

![img_080](./images/img_080.png)

Normally when JSON data is extracted from websites it is highly nested. Example data can be taken from [MDN Working with JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) and made it to a multiline JSON string assigned to the variable ```data```:

```
data = """
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
"""
```

![img_081](./images/img_081.png)

This json ```data``` can be converted into Python readible data using the function ```loads```:

```
pydata = json.loads(data)
```

![img_082](./images/img_082.png)

An IDE like Spyder with a powerful variable explorer can be very helpful for navigating through the data:

![img_083](./images/img_083.png)

![img_084](./images/img_084.png)

![img_085](./images/img_085.png)

![img_086](./images/img_086.png)

![img_087](./images/img_087.png)

If the string ```"Turning tiny"``` is desired it can be accessed using:

```
pydata["members"][0]["powers"][1]
```

![img_088](./images/img_088.png)

This dataset can be used for practicing indexing within nested collections. For example try to obtain the string ```"Superhuman reflexes"```.

JSON is primarally used to extract data from websites and parse it through to Python or vice-versa. The method ```dump``` and ```load``` can however be ed to save JSON data to a file and to laod it from a file respectively. The ```dump``` method requires an object to dump and a file path:

![img_089](./images/img_089.png)

For example the following Python dictionary can be written to a Python file:

```
with open("json_data.txt", "w") as file:
    json.dumps({"r": "red",
                "g": "green",
                "b": "blue"})
    file.close()
```  

![img_090](./images/img_090.png)

The text file can be opened in Windows Explorer:

![img_091](./images/img_091.png)

![img_092](./images/img_092.png)

The data can be extracted from the file using the method ```load```:

![img_093](./images/img_093.png)

```
with open("json_data.txt", "r") as file:
    colors = json.load(file)
    file.close()
```  

![img_094](./images/img_094.png)

Normally, only a single JSON object is written to a file as complicated JSON objects are typically nested.

Return to:
[Home](../../../)

