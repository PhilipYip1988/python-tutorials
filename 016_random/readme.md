# The Random Module

The random module is used to make a random choice from a selection such as a list or a distribution.

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

The ```choice```, ```choices``` and ```sample``` can be used to make a choice, choices (with replacement) or a sample (choices without replacement) from a list. The docstrings of these functions can be examined:

![img_004](./images/img_004.png)

![img_006](./images/img_006.png)

![img_005](./images/img_005.png)

The function ```choice``` has an optional input argument ```weights``` or cumulative weights ```cum_weights``` for weighting each value in the population. 

The function sample has the optional input argument ```counts``` which can be used to specify the occurance of each item in the population.

One thing to note about the ```random``` module is the random selection is randomly computer generated and is not really random. This is known as pseudo-random. The pseudo random result can be reproduced by setting a random ```seed```:

![img_007](./images/img_007.png)

Under the hood the random seed sets up a sequence of integers which correspond to random states and more details about these can be found using ```getstate```:

![img_008](./images/img_008.png)

To return to a state, ```setstate``` can be used:

![img_009](./images/img_009.png)

The simple list ```nums``` can be created. The random module imported, the seed set to 0 and three individual choices made using choice three times:

```
import random
nums = [1, 3, 5, 7, 9]
random.seed(0)
random.choice(nums)
random.choice(nums)
random.choice(nums)
```

![img_010](./images/img_010.png)

If the seed is reset to 0 and another three choices are made, these will be the same three choices as before:

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

