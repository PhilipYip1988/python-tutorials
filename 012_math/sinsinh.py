import numpy as np
import matplotlib.pyplot as plt
from sympy import var, plot_implicit
var('x y')

ax = plot_implicit(x**2 + y**2 - 1, xlim=[-0.5, 0.5], ylim=[-0.5, 0.5], aspect_ratio=(1, 1), autoscale=False, xlabel="x", ylabel="y")
ax2 = plot_implicit(x**2 - y**2 - 1, aspect_ratio=(1, 1), xlabel="x", ylabel="y")
