# histogram_demo
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
d = np.random.normal(0.0, 1.0, size=100000)

x = np.linspace(-5,5,num=1000)
f = 1/(np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)

#plt.hist(d, 100)
plt.hist(d, 100, density=True)
plt.plot(x, f, color='r', linewidth=3)


#plt.plot(d, 'o')
plt.show()