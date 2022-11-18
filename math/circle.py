import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

alpha = np.linspace(0, math.tau, 100)

x = np.sin(alpha)
y = np.cos(alpha)

fig, ax = plt.subplots() 
 
ax.plot(x, y) 
ax.set_aspect(1) 

ax.plot([-1, 1], [0, 0])

ax.set_xlabel(r"$x=sin(\alpha)$")
ax.set_ylabel(r"$y=cos(\alpha)$")