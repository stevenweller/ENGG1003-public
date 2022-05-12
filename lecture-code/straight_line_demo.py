import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco


def line(t, m, b):
    return m * t + b


# seed random number generator to reproduce lecture results
np.random.seed(3)

N = 11
t = np.linspace(0, 100, num=N)       # 0,10,20,...,100
n = np.random.uniform(-25, 25, N)     # noise on linear function

mm = 3              # gradient
bb = 50             # intercept
y = mm*t + bb + n   # dataset is straight line + noise

# STRAIGHT-LINE FIT
popt, _ = sco.curve_fit(line, t, y)
m = popt[0]
b = popt[1]

# apply f() to a numpy array
ybest = m * t + b

# PLOT RESULTS
plt.plot(t, y, 'ro')
plt.plot(t, ybest, 'b')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title("Straight-line fit")
plt.show()