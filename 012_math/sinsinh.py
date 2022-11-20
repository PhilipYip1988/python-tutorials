import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import var, plot_implicit
var('x y')

# plot_implicit(x**2 + y**2 - 1, xlim=[-0.5, 0.5], ylim=[-0.5, 0.5], aspect_ratio=(1, 1), autoscale=False, xlabelQ="x", ylabel="y", line_color="r", linewidth=2)
# fig = plt.gcf()
# ax = plt.gca()
# ax.set_xlim(left=-1.5, right=1.5)
# ax.set_ylim(bottom=-1.5, top=1.5)



plot_implicit(x**2 - y**2 - 1, aspect_ratio=(1, 1), xlabel="x", ylabel="y", line_color="r")
fig = plt.gcf()
ax = plt.gca()
ax.plot([-5, 5], [-5, 5], color="k", ls=":")
ax.plot([-5, 5], [5, -5], color="k", ls=":")
ax.set_xlim(left=-3, right=3)
ax.set_ylim(bottom=-3, top=3)

ax.scatter([math.cosh(1)], [math.sinh(1)], s=50)