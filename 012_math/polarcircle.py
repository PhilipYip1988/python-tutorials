import numpy as np
import matplotlib.pyplot as plt

# circle



fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_xticks([0, np.pi/4, 2*np.pi/4, 3*np.pi/4, 4*np.pi/4, 5*np.pi/4, 6*np.pi/4, 7*np.pi/4])
ax.set_xticklabels([0, r"1$\pi$/4", r"2$\pi$/4", r"3$\pi$/4", r"$4\pi$/4", r"5$\pi$/4", r"6$\pi$/4", r"7$\pi$/4"])
# circle
t = np.linspace(0, 2*np.pi, 50)
r = 1 + 0 * np.zeros(np.shape(t))
ax.plot(t, r)

# radius
r = [0, 1]
t = [0, (np.pi/4)]
ax.plot(t, r, color="r")

# diameter
r = [0, 1]
t = [0, (-3*np.pi/4)]
ax.plot(t, r, color="r")


ax.set_rmax(1.25)
ax.set_rticks([0, 0.5, 1.0])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

plt.show()