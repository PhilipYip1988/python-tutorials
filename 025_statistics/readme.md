# The Statistics Module

The statistics module provides a number of basic statistical functions including averages, variance and standard deviation.

The statistics module is normally imported using a 2 letter alias:

```
import statistics as st
```

![img_001](./images/img_001.png)

The docstring of the statistics module is pretty detailed can be examined by inputting:

```
? statistics
```

![img_002](./images/img_002.png)

As seen from the docmenation, the module contains a collection of functions for calculating averages:

|function|description|
|---|---|
|mean|Arithmetic mean (average) of data.|
|fmean|Fast, floating point arithmetic mean.|
|median|Median (middle value) of data.|
|median_low|Low median of data.|
|median_high|High median of data.|
|mode|Mode (most common value) of data.|

And for calculating the associated varibility or spread:

|function|description|
|---|---|
|pvariance|Population variance of data.|
|variance|Sample variance of data.|
|stdev|Sample standard deviation of data.|
|pstdev|Population standard deviation of data.|

These statistical averages can be examined from a very simple dataset:

$$\text{data}=[\begin{matrix}7&5&3&1&2&4&6&4\end{matrix}]$$

```
data = [7, 5, 3, 1, 2, 4, 6, 4]
```

![img_003](./images/img_003.png)

This dataset can be sorted:

$$\text{data}=\left[\begin{matrix}1&2&3&4&4&5&6&7\end{matrix}\right]$$

```
data.sort()
data
```

![img_004](./images/img_004.png)

The index of each element in the dataset can be shown. The length has a value of 1 higher than the last index. The last index is 7 so the length is 8:

$$\text{data}=\left[\begin{matrix}{\underset{0}{1}}&{\underset{1}{2}}&{\underset{2}{3}}&{\underset{3}{4}}&{\underset{4}{4}}&{\underset{5}{5}}&{\underset{6}{6}}&{\underset{7}{7}}\end{matrix}\right]$$

```
lendata = len(data)
lendata
```

![img_005](./images/img_005.png)

The sum of the data can be calculated using:

$$\text{sum}=1+2+3+4+4+5+6+7=32$$

```
sumdata = sum(data)
sumdata
```

![img_006](./images/img_006.png)

The integer mean can be calculated:

$$\text{intmean}=32//8=4$$

$$\text{intmod}=32﹪8=0$$

```
sum(data) // len(data)
sum(data) % len(data)
```

![img_007](./images/img_007.png)

The floating point mean can be calculated:

$$\text{floatmean}=32/8=4.0$$

```
sum(data) / len(data)
```

![img_008](./images/img_008.png)

The function ```mean``` returns the integer mean for no modulus and the float mean, when a modulus is present. The docstring can be seen by inputting ```st.mean()``` followed by pressing shift ```⇧ ``` and tab ```↹```:

![img_009](./images/img_009.png)

The mean of the dataset can be calculated using:

```
st.mean(data)
```

![img_010](./images/img_010.png)

The function floating point mean, ```fmean``` on the other hand always returns the floating point mean. The docstring can be seen by inputting ```st.fmean()``` followed by pressing shift ```⇧ ``` and tab ```↹```:

![img_011](./images/img_011.png)

The floating point mean of the dataset can be calculated using:

```
st.fmean(data)
```

![img_012](./images/img_012.png)

The median is the middle point of the data which can be selected directly when the data is odd. When the data has an even number of values it is the mean of these two middle values:

$$\text{data}=\left[\begin{matrix}1&2&3&\textbf{4}&\textbf{4}&5&6&7\end{matrix}\right]$$

$$\text{median}=\frac{4+4}{2}=4$$

The docstring of the function ```median``` can be seen by inputting ```st.median()``` followed by pressing shift ```⇧ ``` and tab ```↹```:

![img_013](./images/img_013.png)

The median of the dataset can be calculated using:

```
st.median(data)
```

![img_014](./images/img_014.png)

Alternatively the value on the left is the median low value and can be read off directly:

$$\text{data}=\left[\begin{matrix}1&2&3&\textbf{4}&4&5&6&7\end{matrix}\right]$$

The docstring of the function ```median_low``` can be seen by inputting ```st.median_low()``` followed by pressing shift ```⇧ ``` and tab ```↹```:

![img_015](./images/img_015.png)

The median low of the dataset can be calculated using:

```
st.median_low(data)
```

![img_016](./images/img_016.png)

And the value on the right is the median high value and can be read off directly:

$$\text{data}=\left[\begin{matrix}1&2&3&4&\textbf{4}&5&6&7\end{matrix}\right]$$

The docstring of the function ```median_high``` can be seen by inputting ```st.median_high()``` followed by pressing shift ```⇧ ``` and tab ```↹```:

![img_017](./images/img_017.png)

The median high of the dataset can be calculated using:

```
st.median_high(data)
```

![img_018](./images/img_018.png)

The mode is the most commonly occuring value:

$$\text{data}=\left[\begin{matrix}1&2&3&\textbf{4}&\textbf{4}&5&6&7\end{matrix}\right]$$

The docstring of the function ```mode``` can be seen by inputting ```st.mode()``` followed by pressing shift ```⇧ ``` and tab ```↹```:

![img_019](./images/img_019.png)

The mode of the dataset can be calculated using:

```
st.mode(data)
```

![img_020](./images/img_020.png)

The concept of variance is to compute the average distance a datapoint differs from the mean.

Notice when when the sum of (each datapoint minus the mean) is calculated, the positive values and negative values cancel each other out and the result is 0:

$$\sum_{i=0}^{n}\left(x-\mu\right)=\left(1-4\right)+\left(2-4\right)+\left(3-4\right)+\left(4-4\right)+\left(4-4\right)+\left(5-4\right)+\left(6-4\right)+\left(7-4\right)$$

$$\left(-3\right)+\left(-2\right)+\left(-1\right)+\left(0\right)+\left(0\right)+\left(1\right)+\left(2\right)+(3)$$

$$-3-2-1+0+0+1+2+3$$

$$0$$

Instead the sum of (each datapoint minus the mean) squared is calculated. A negative value multiplied by itself is positive and this therefore always gives a positive value:

$$\sum_{i=0}^{n}\left(x-\mu\right)^2=\left(1-4\right)^2+\left(2-4\right)^2+\left(3-4\right)^2+\left(4-4\right)^2+\left(4-4\right)^2+\left(5-4\right)^2+\left(6-4\right)^2+\left(7-4\right)^2$$

$$\left(-3\right)^2+\left(-2\right)^2+\left(-1\right)^2+\left(0\right)^2+\left(0\right)^2+\left(1\right)^2+\left(2\right)^2+\left(3\right)^2$$

$$9+4+1+0+0+1+4+9$$

$$28$$

The mean is a normalised sum, and the population variance is the normalised sum of (each datapoint minus the mean) squared. The normalisation factor is the number of datapoints.

$$\frac{28}{8}=3.5$$

The variance takes into account a difference in the number of degrees of freedom and uses the number of datapoints minus one as a normalisation factor:

$$\frac{28}{(8-1)}=\frac{28}{7}=4.0$$

```
st.pvariance(data)
st.variance(data)
```

Due to the squaring used when calculating the population variance or variance, these measurements have units of the mean squared. The standard deviation is the square root of the variance, which is measured in the same units as the mean:

$$\sqrt{3.5}=$$

$$\sqrt{3.5}=1.8708$$



```
st.pstdev(data)
st.stdev(data)
```

A distribution is normally quoted using the mean and stdev in the form:

$$4.0\pm2.0$$

The median value is less susceptible to large outliers and in such a scenario can be more accurate when describing a small dataset. For example if an outlier is purposely introduced, there is not much change in the median but the mean is highly distorted:

```
data.append(999)
data
st.mean(data)
st.median(data)
st.stdev(data)
```

The mode can be an important metric in a trial run. For example if a fashion designer wants to issue a prototype design of clothe, they may simplify manufacturing by starting only with the mode cloth size, as it has the largest customer base. If the cloth is successful, they may complicate the manufacturer process to accomodate other sizes.


The outlier can be removed from the data:

```
data.pop()
data
```

Let's now examine the geometric mean.











|function|description|
|---|---|
|geometric_mean|Geometric mean of data.|
|harmonic_mean|Harmonic mean of data.|
|multimode|List of modes (most common values of data).|
|quantiles|Divide data into intervals with equal probability.|
|median_grouped|Median, or 50th percentile, of grouped data.|


|function|description|
|---|---|
|covariance|Sample covariance for two variables.|
|correlation|Pearson's correlation coefficient for two variables.|
|linear_regression|Intercept and slope for simple linear regression.|
