import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# seed random number generator to reproduce lecture results
np.random.seed(27101967)

N = 11
t = np.linspace(0,100,11)           # 0,10,20,...,100
tnew = np.linspace(0,100,100*N)     # 0,0.1,0.2,...,100
n = np.random.uniform(-25,25,N)     # noise on linear function

m = 3                               # gradient
b = 50                              # intercept
y = m*t + b + n                     # dataset is straight line + noise

# INTERPOLATION
f3 = interp1d(t, y, 'cubic')

# PLOT RESULTS
plt.plot(t, y, 'ro')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.plot(tnew, f3(tnew), 'b')
plt.title('Cubic spline interpolation')
plt.show()