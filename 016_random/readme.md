# The Random Module

The random module is used to select a pseudo random from a collection such as a list or an underlying distribution.

It can be imported using:

```
import random
```

And details about the available distributions can be seen by looking at the docstring:

```
? random
```

![img_001](./images/img_001.png)

The random module has a number of identifiers which can be accessed by inputting ```random.``` followed by a tab ```↹```:

![img_002](./images/img_002.png)

Before looking at any distributions, let's construct a list of values:

```
nums = [1, 3, 5, 7, 9]
```

![img_003](./images/img_003.png)

The ```choice``` function can be used to make a pseudo random choice from a list.

## seed and state

One thing to note about the ```random``` module is the random selection is randomly computer generated and is not really random. This is known as pseudo-random. The pseudo random result can be reproduced by setting a random ```seed```:

![img_007](./images/img_007.png)

Under the hood the random seed sets up a sequence of integers which correspond to random states and more details about these can be found using ```getstate```:

![img_008](./images/img_008.png)

To return to a state, ```setstate``` can be used:

![img_009](./images/img_009.png)

The simple list ```nums``` can be created. The random module imported, the seed set to 0 and three individual choices made using choice four times:

```
import random
nums = [1, 3, 5, 7, 9]
random.seed(0)
random.choice(nums)
random.choice(nums)
random.choice(nums)
```

![img_010](./images/img_010.png)

If the seed is reset to ```0``` and another three choices are made, these will be the same three choices as before:

```
random.seed(0)
random.choice(nums)
random.choice(nums)
random.choice(nums)
```

![img_011](./images/img_011.png)

The current state can be retrieved and assigned to a variable. Notice if another three random choices are made after getting the state, that these are different to before:

```
state = random.getstate()
random.choice(nums)
random.choice(nums)
random.choice(nums)
```

![img_012](./images/img_012.png)

This state can be restored from the variable and if the three random choices are made, they will be the the same as before:

```
random.setstate(state)
random.choice(nums)
random.choice(nums)
random.choice(nums)
```

![img_013](./images/img_013.png)

The ```state``` can be viewed in the variable explorer of the Spyder IDE. It is shown as a tuple. The 1st element at index 0 has an integer value of 3 and corresponds to the version of the random number algorithm. The 2nd element at index 1 is a list of large integer number values, these sequence of numbers are used internally by the associated functions in the random module to generate "random" states:

![img_014](./images/img_014.png)

If the seed is changed, a different set of random states are obtained:

```
random.seed(1)
random.choice(nums)
random.choice(nums)
```

![img_015](./images/img_015.png)

This can be seen by looking at only the first 5 numbers:

```
random.seed(0)
random.getstate()[1][:5]
random.seed(1)
random.getstate()[1][:5]
random.seed(2)
random.getstate()[1][:5]
```

![img_016](./images/img_016.png)

To recap the seed is the value used to initialise the generator and the state is the current state of the generator after each call to generate a random number. 

## choice

```choice``` can be used to make a pseudo random choice from a sequence, such as a list:

![img_004](./images/img_004.png)

```
import random
nums = [1, 3, 5, 7, 9]
random.seed(0)
random.choice(nums)
random.choice(nums)
random.choice(nums)
random.choice(nums)
```

![img_017](./images/img_017.png)

## choices

```choices``` can be used to make multiple choices from a population, the number of choices is determined by specifying the keyword argument ```k``` which has a default value of 1 and therefore behaves similar to  ```choice``` by default. 

![img_006](./images/img_006.png)

```
import random
nums = [1, 3, 5, 7, 9]
random.seed(0)
random.choices(nums)
random.choices(nums)
random.choices(nums)
random.choices(nums)
```

Notice the output is a list with a single element. This is because ```choices``` is usually used to select multiple choices from a population. 

![img_018](./images/img_018.png)

Let's assign ```k=3``` to make 3 choices:

```
import random
nums = [1, 3, 5, 7, 9]
random.seed(0)
random.choices(nums, k=3)
```

![img_019](./images/img_019.png)

```choices``` makes choices from the population with replacement. With replacement means that once a choice is made, it is still present in the population. In the case where the population is an unweighted simple sequence such as a list, there is no mutation of the list to remove the value choosen after making a choice. Therefore it is possible to make 6 choices from a list with only 5 unique values.

```
nums = [1, 3, 5, 7, 9]
random.seed(0)
random.choices(nums, k=6)
```

Notice the same value ```5``` is chosen multiple times.

![img_020](./images/img_020.png)

The population can be weighted, using the keyword argument ```weights``` and assigning it to a list of respective weights for each value in the population. For example the following:

```
import random
nums = [1, 3, 5, 7, 9]
weights = [100, 10, 5, 1, 1]
random.seed(0)
random.choices(nums, weights=weights, k=3)
```

The weight is used to calculate the weighted probability. The above essentially multiplies the probability of getting a ```1``` by ```100``` and getting a ```9``` by ```1```. 

![img_021](./images/img_021.png)

For this reason, most the values chosen are ```1``` due to the respective weight. This effect is seen more clearly when the number of choices is made larger. A ```Counter``` will be created to make viewing the results easier:

```
import random
from collections import Counter
nums = [1, 3, 5, 7, 9]
weights = [100, 10, 5, 1, 1]
random.seed(0)
chosen = random.choices(nums, weights=weights, k=100)
Counter(chosen)
```

Most of the choices are ```1``` with a smaller proportions of ```3``` and the very occasional ```5``` as expected from the above weights.

![img_022](./images/img_022.png)

Cumulative weights can also be used. The cumulative weight is the cumulative weight of the previous elements plus the new weight. For example to make cumulative weights equivalent to the aboves:

```
import random
from collections import Counter
nums = [1, 3, 5, 7, 9]
cum_weights = [100, 110, 115, 116, 117]
random.seed(0)
chosen = random.choices(nums, cum_weights=cum_weights, k=100)
Counter(chosen)
```

![img_023](./images/img_023.png)

The weights and cumultative weights are not expressed in percentages. However they can be:

```
from random import random
from collections import Counter
nums = [1, 3, 5, 7, 9]
weights = [5, 10, 15, 20, 50]
random.seed(0)
chosen = random.choices(nums, weights=weights, k=100)
```

![img_024](./images/img_024.png)

```
from random import random
from collections import Counter
nums = [1, 3, 5, 7, 9]
cum_weights = [5, 15, 30, 50, 100]
random.seed(0)
chosen = random.choices(nums, cum_weights=cum_weights, k=100)
```

![img_025](./images/img_025.png)

For a small value of ```k``` such as ```100```, the percentages obtained will differ from the percentages supplied. As ```k``` increases, say to ```10000``` the percentages will more closely resemble what was supplied.

```
from random import random
from collections import Counter
nums = [1, 3, 5, 7, 9]
weights = [5, 10, 15, 20, 50]
random.seed(0)
chosen = random.choices(nums, weights=weights, k=100)
random.seed(0)
chosen = random.choices(nums, weights=weights, k=10000)
```

![img_026](./images/img_026.png)

## sample

```sample``` can be used to take a ```sample``` of ```k``` values from a population. Unlike ```choices``` the values taken for the sample are taken without replacement.

![img_005](./images/img_005.png)

The function sample has the optional input argument ```counts``` which can be used to specify the count of each item in the population. This behaves similar to ```weight``` which was seen in ```choice``` but also acts as a physical ```count``` as items are taken in a ```sample``` without replacement.

For a population of 5 items where each item has a single count. A sample of 3 values can be taken. Or a sample of 5 items can be taken. In the latter case, a sample of all the items is taken and the list is essentially shuffled:

```
import random
nums = [1, 3, 5, 7, 9]
random.seed(0)
random.sample(nums, k=3)
random.sample(nums, k=5)
```

![img_027](./images/img_027.png)

If 6 items are taken in a sample of only 5 items, there is a ```ValueError```:

```
random.sample(nums, k=6)
```

![img_028](./images/img_028.png)

The ```counts``` can be assigned to values which amtched the original ```weights```, recall that these should be considered as aphysical counts. A sample of ```k=25``` can be taken and ```k=117``` (all values) can be taken. 

```
import random
from collections import Counter
nums = [1, 3, 5, 7, 9]
counts = [100, 10, 5, 1, 1]
random.seed(0)
sampled = random.sample(nums, counts=counts, k=25)
Counter(sampled)
sampled = random.sample(nums, counts=counts, k=117)
Counter(sampled)
```

![img_029](./images/img_029.png)

Notice that the sample of all the values matches precisely the counts supplied for each of the values. This is expected as each of these values was physically taken in order to get the sample.

## shuffle

The ```shuffle``` function takes in a list of values and mutates it its order in place. This is similar to taking a ```sample``` of all the items in the list for a list where every item has a count of 1 but ```sample``` outputs a new list while ```shuffle``` mutates the original in place: 

![img_030](./images/img_030.png)

```
import random
random.seed(0)
nums = [1, 3, 5, 7, 9]
random.shuffle(nums)
nums
```

![img_031](./images/img_031.png)

## randint

The ```randint``` is used to return a random integer between a lower bound and upper bound of integers, inclusive of both bounds:

![img_032](./images/img_032.png)

```
import random
random.seed(0)
random.randint(0, 10)
```

It is equivalent to taking a choice from a range object which has a step of 1:

```
random.choice(range(0, 11, 1))
```

The range object is exclusive of the upper bound, which is why the end is one higher.

![img_033](./images/img_033.png)

## getrandbits

The ```randbits``` will generate a random configuration of bits. Recall that each random configuration of bits can be visualised as a configuration of switches or LEDs and this configuration is mapped to an integer.  

![img_034](./images/img_034.png)

In the case of an arrangement of 8 bits (1 byte) this is essentially asking for a random integer between ```0-255``` and each grouping of 4 is mapped to a hexadecimal digit:

```
import random
random.seed(0)
num1 = random.getrandbits(8)
num1
hex(num1)
bin(num1)
```

This is equivalent to:

```
random.randint(0, 2**8-1)
random.choice(range(0, 2**8, 1))
```

![img_035](./images/img_035.png)

A random 16 bit (2 bytes) number can also be generated:

```
import random
random.seed(0)
num1 = random.getrandbits(16)
num1
hex(num1)
bin(num1)
```

![img_036](./images/img_036.png)

A random 32 bit (4 bytes) number can also be generated:

```
import random
random.seed(0)
num1 = random.getrandbits(32)
num1
hex(num1)
bin(num1)
```

![img_037](./images/img_037.png)

## randbytes

The function ```randbytes``` will generate a number of random bytes displaying each byte as a ```byte```. The relation to ```randbytes``` and ```randint``` function was explored with the ```getrandbits``` function:

![img_038](./images/img_038.png)

```
random.seed(0)
random.getrandbits(1)
random.getrandbits(2)
random.getrandbits(4)
```

![img_039](./images/img_039.png)

The ```byte``` consists of hexadecimal values in the form ```\x00```, if the hexadecimal value is in the range ```0x00``` to ```0x7f```, it is an ASCII character and the ASCII character is printable or non-printable but displayed in Python as an escape character such as the tab ```\t``` the escape character will display instead. The hex values of these can be seen by using the ```ord``` function on the character enclosed by the ```hex``` function:

```
hex(ord("L"))
hex(ord("\t"))
hex(ord("U"))
hex(ord("k"))
```

![img_040](./images/img_040.png)

## uniform

The ```uniform``` function is used to generate a random ```float``` in the range ```a``` to ```b```:

![img_041](./images/img_041.png)

```
import random
random.seed(0)
random.uniform(0, 10)
```

![img_042](./images/img_042.png)

At this stage it is useful to conceptualise what the distribution looks like in the form of a histogram of ```1000000``` values. A ```uniform``` distribution has an equal weighting for each value and looks like the following.

A triangular ...