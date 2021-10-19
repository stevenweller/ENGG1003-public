# meandemo
import numpy as np
import matplotlib.pyplot as plt

N = 100000
np.random.seed(1)
x0 = np.random.normal(0.0, 1.0, size=N)
x5 = np.random.normal(5.0, 1.0, size=N)
x15 = np.random.normal(15.0, 1.0, size=N)

plt.hist(x0, 100, density=True, color='r', label='mean=0')
plt.hist(x5, 100, density=True, color='b', label='mean=5')
plt.hist(x15, 100, density=True, color='k', label='mean=15')

plt.title('np.random.normal(mean, 1.0, {})'.format(N))
plt.axis([-5, 25, 0, 0.45])
plt.legend()
plt.show()