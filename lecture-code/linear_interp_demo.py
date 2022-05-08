import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# seed random number generator to reproduce lecture results
np.random.seed(3)

N = 11
t = np.linspace(0, 100, num=N)       # 0,10,20,...,100
n = np.random.uniform(-25, 25, N)     # noise on linear function

m = 3               # gradient
b = 50              # intercept
y = m*t + b + n     # dataset is straight line + noise

# INTERPOLATION
f = interp1d(t, y)

# apply f() at a single number
t1 = 17
print(t1, f(t1))

# apply f() to a numpy array
t2 = np.linspace(0, 100, num=1001)
y2 = f(t2)

# PLOT RESULTS
plt.plot(t, y, 'ro')
plt.plot(t2, y2, 'b')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title("Linear interpolation")
plt.show()