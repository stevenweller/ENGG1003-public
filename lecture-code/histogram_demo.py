import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
d = np.random.normal(0.0, 1.0, size=100000)

x = np.linspace(-5, 5, num=1001)
f = 1/(np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

plt.hist(d, bins=100, density=True) #area under histogram equal to 1
plt.plot(x, f, color='r', linewidth=3)
plt.show()