import math
from math import pi, tau, e
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def error_function(z):
    value = 0
    for n in range(100):
        value += (2 / math.sqrt(pi)) * (-1) ** n * z ** (2 * n + 1)/((math.factorial(n)*(2 * n + 1)))
    return value


def cerror_function(z):
    return 1 - error_function(z)


a = error_function(2)
a2 = math.erf(2)
b = cerror_function(2)
b2 = math.erfc(2)

"""
the error function erf(x) is the probability that a number drawn at random from the standard normal distribution (mean =0, standard deviation = 1) will be no greater than x.
"""

"""
https://mathworld.wolfram.com/Erf.html
"""

def standard_normal(x):
    return (math.exp(-(x**2)/2))/math.sqrt(tau)

x = [num/10 for num in range(-40, 41, 1)]
y = [standard_normal(num/10) for num in range(-40, 41, 1)]
z = [math.erf(num/10) for num in range(-40, 41, 1)]
z2 = [math.erfc(num/10) for num in range(-40, 41, 1)]

fig, ax = plt.subplots(3, 1)
ax[0].plot(x, y)
ax[1].plot(x, z)
ax[2].plot(x, z2)

from statistics import NormalDist
nd = NormalDist(mu=0, sigma=1)



