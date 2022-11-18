import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a = math.comb(3, 2)
b = math.perm(3, 2)


fig, ax = plt.subplots(3, 1)
c1 = plt.Circle((0.3, 0.5), 0.15, color="#00B050")
c2 = plt.Circle((0.7, 0.5), 0.15, color="#7030A0")
ax[0].set_aspect(1)
ax[0].add_artist(c1)
ax[0].add_artist(c2)
ax[0].axis('off')

c1 = plt.Circle((0.3, 0.5), 0.15, color="#00B050")
c2 = plt.Circle((0.7, 0.5), 0.15, color="#FF0000")
ax[1].set_aspect(1)
ax[1].add_artist(c1)
ax[1].add_artist(c2)
ax[1].axis('off')

c1 = plt.Circle((0.3, 0.5), 0.15, color="#7030A0")
c2 = plt.Circle((0.7, 0.5), 0.15, color="#FF0000")
ax[2].set_aspect(1)
ax[2].add_artist(c1)
ax[2].add_artist(c2)
ax[2].axis('off')

plt.show()
