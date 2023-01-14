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