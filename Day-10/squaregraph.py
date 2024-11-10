import numpy as np
import matplotlib.pyplot as plt

xcoordinate = np.array([0,0,8,8,0])
ycoordinate = np.array([0,8,8,0,0])

xcoordinate2 = np.array([1,1,9,9,1])
ycoordinate2 = np.array([1,9,9,1,1])

xarr = np.array([0,1])
yarr = np.array([0,1])

xarr2 = np.array([0,1])
yarr2 = np.array([8,9])

xarr3 = np.array([8,9])
yarr3 = np.array([8,9])

xarr4 = np.array([8,9])
yarr4 = np.array([0,1])

plt.plot(xcoordinate, ycoordinate)
plt.plot(xcoordinate2, ycoordinate2)
plt.plot(xarr, yarr, xarr2, yarr2, xarr3, yarr3, xarr4, yarr4)


plt.grid()
plt.show()
