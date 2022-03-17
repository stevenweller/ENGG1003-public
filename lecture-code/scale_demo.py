import numpy as np
import matplotlib.pyplot as plt

N = 100000

x1 = np.random.normal(0, 1, size=N)
x2 = np.random.normal(0, 2, size=N)
x3 = np.random.normal(0, 4, size=N)

# bell curve for large N
plt.hist(x1, bins=100, density=True, label="scale=1")
plt.hist(x2, bins=100, density=True, label="scale=2")
plt.hist(x3, bins=100, density=True, label="scale=4")

plt.xlabel('Value of random number')
plt.legend()
plt.show()