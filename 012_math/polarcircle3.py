import numpy as np
import matplotlib.pyplot as plt

# circle



fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_xticks([0, np.pi/12, 2*np.pi/12, 3*np.pi/12])
ax.set_xticklabels([0, r"1$\pi$/12", r"2$\pi$/12", r"3$\pi$/12"])
# circle
t = np.linspace(0, 2*np.pi, 50)
r = 1 + 0 * np.zeros(np.shape(t))
ax.plot(t, r)

# radius 0
r = [0, 1]
t = [0, 0]
ax.plot(t, r, c="grey", ls=":")
ax.scatter([0], [1], 50, c="grey")

# # radius pi/12
# r = [0, 1]
# t = [0, np.pi/12]
# ax.plot(t, r, "r:")
# ax.scatter([np.pi/12], [1], 50, "r")


# # radius 6*pi/12
# r = [0, 1]
# t = [0, 6*np.pi/12]
# ax.plot(t, r, c="grey", ls=":")
# ax.scatter([6*np.pi/12], [1], 50, c="grey")

# radius 3*pi/12
r = [0, 1]
t = [0, 3*np.pi/12]
ax.plot(t, r, "r")
ax.scatter([3*np.pi/12], [1], 50, c="r")

r = [np.sin(3*np.pi/12), 1]
t = [0, 3*np.pi/12]
ax.plot(t, r, "c:")





ax.set_rmax(1.25)
ax.set_rticks([0, 0.5, 1.0])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

plt.show()