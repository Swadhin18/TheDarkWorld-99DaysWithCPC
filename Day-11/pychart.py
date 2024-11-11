import numpy as np
import matplotlib.pyplot as plt

arr = np.array([12,36,30,10])
mylabels = ["Bipasa","Sharmin","Shreyoshi","Borsha"]
myexplode = [0,0.2,0,0]
plt.pie(arr, labels = mylabels, startangle =90, explode= myexplode)
plt.legend(title = "Their names :    ")

plt.show()