import numpy as np
import matplotlib.pyplot as plt

N = 1000000

x1 = np.random.normal(0, 1, size=N)
x2 = np.random.normal(5, 1, size=N)
x3 = np.random.normal(15, 1, size=N)

# bell curve for large N
plt.hist(x1, bins=100)
plt.hist(x2, bins=100)
plt.hist(x3, bins=100)

plt.xlabel('Value of random number')
plt.ylabel('Number of samples in bin')
plt.show()