import numpy as np
import matplotlib.pyplot as plt

# seed random number generator to reproduce lecture results
np.random.seed(3)

N = 11
t = np.linspace(0, 100, num=N)       # 0,10,20,...,100
n = np.random.uniform(-25, 25, N)     # noise on linear function

m = 3                               # gradient
b = 50                              # intercept
y = m*t + b + n                     # dataset is straight line + noise

print(t)
print(y)

plt.plot(t, y, 'ro')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()