# SDdemo
import numpy as np
import matplotlib.pyplot as plt

N = 100000
np.random.seed(1)
x0 = np.random.normal(0.0, 1.0, size=N)
x5 = np.random.normal(0.0, 2.0, size=N)
x15 = np.random.normal(0.0, 4.0, size=N)

plt.hist(x0, 100, density=True, color='r', label='SD=1')
plt.hist(x5, 100, density=True, color='b', label='SD=2')
plt.hist(x15, 100, density=True, color='k', label='SD=4')

plt.title('np.random.normal(0.0, SD, {})'.format(N))
plt.axis([-15, 15, 0, 0.45])
plt.legend()
plt.show()