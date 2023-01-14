# The Statistics Module

The statistics module provides a number of basic statistical functions including averages, variance and standard deviation.

The statistics module is normally imported using a 2 letter alias:

```
import statistics as st
```

The docstring of the statistics module is pretty detailed can be examined by inputting:

```
? statistics
```

As seen from the docmenation, the module contains a collection of functions for calculating averages, calculating the varibility or spread and for the relation between two inputs.

|function|description|
|---|---|
|mean|Arithmetic mean (average) of data.|
|fmean|Fast, floating point arithmetic mean.|
|geometric_mean|Geometric mean of data.|
|harmonic_mean|Harmonic mean of data.|
|median|Median (middle value) of data.|
|median_low|Low median of data.|
|median_high|High median of data.|
|median_grouped|Median, or 50th percentile, of grouped data.|
|mode|Mode (most common value) of data.|
|multimode|List of modes (most common values of data).|
|quantiles|Divide data into intervals with equal probability.|

|function|description|
|---|---|
|pvariance|Population variance of data.|
|variance|Sample variance of data.|
|pstdev|Population standard deviation of data.|
|stdev|Sample standard deviation of data.|

|function|description|
|---|---|
|covariance|Sample covariance for two variables.|
|correlation|Pearson's correlation coefficient for two variables.|
|linear_regression|Intercept and slope for simple linear regression.|



These statistical averages can be examined from a very simple dataset:

$$\text{data}=[\begin{matrix}7&5&3&1&2&4&6&4\end{matrix}]$$

$$\text{data}=[\begin{matrix}7&5&3&1&2&4&6&4\\\end{matrix}]$$

$$\text{data}=\left[ \begin{matrix}7&5&3&1&2&4&6&4\\\end{matrix} \right]$$

```
data = [7, 5, 3, 1, 2, 4, 6, 4]
```

This dataset can be sorted:

$$\text{data}=\left[\begin{matrix}1&2&3&4&4&5&6&7\\\end{matrix}\right]$$

```
data.sort()
data
```


The index of each element in the dataset can be shown. The length has a value of 1 higher than the last index. The last index is 7 so the length is 8:

$$\text{data}=\left[\begin{matrix}{\underset{0}{1}}&{\underset{1}{2}}&{\underset{2}{3}}&{\underset{3}{4}}&{\underset{4}{4}}&{\underset{5}{5}}&{\underset{6}{6}}&{\underset{7}{7}}\\\end{matrix}\right]$$

```
lendata = len(data)
lendata
```



The sum of the data can be calculated using:

$$\text{sum}=1+2+3+4+4+5+6+7=32$$

```
sumdata = sum(data)
```

The integer mean can be calculated:

$$\text{intmean}=32//8=4$$


```
sum(data) // len(data)
sum(data) % len(data)
```

The floating point mean can be calculated:

```
sum(data) / len(data)
```

The statistical function mean returns the integer mean for no modulus and the float mean, when a modulus is present:

```
st.mean(data)
```

The floating point mean, always returns the floating point mean:

```
st.fmean(data)
```

```
st.median(data)
```

