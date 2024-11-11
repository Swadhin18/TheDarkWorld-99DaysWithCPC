import numpy as np
import matplotlib.pyplot as plt

xnames = np.array(["Mehedi", "Maruf", "Average", "Swadhin"])
ylength = np.array([87, 90, 70, 20])

plt.barh(xnames, ylength)
plt.title("Scores of Individuals")

for index, value in enumerate(ylength):
    plt.text(value + 1, index, str(value + 1, index, str(value))

plt.show()
