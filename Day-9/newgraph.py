import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,3,4,5])
ypoints = np.array([7,5,9,5,1])

plt.plot(xpoints, ypoints, marker='o', ms=8, linewidth=3.5)
plt.plot(xpoints, ypoints, marker='*:r', ms=7, linewidth=4)

plt.show()