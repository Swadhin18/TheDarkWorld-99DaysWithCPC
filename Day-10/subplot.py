import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6])
y = np.array([0,6,1,5,2,4,3])

r_x = np.zeros(len(x))
r_y = np.zeros(len(y))

for i in range(len(x)):
    r_x[i] = 6 - x[i]
    r_y[i] = 6 - y[i]

plt.subplot(2,2,1)
plt.plot(x,y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.subplot(2,2,2)
plt.plot(y,x)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.subplot(2,2,3)
plt.plot(r_x,r_y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.subplot(2,2,4)
plt.plot(r_y,r_x)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()