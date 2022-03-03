import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = np.linspace(0, 1, num=1001)

y = v0*t - 0.5*g*t**2

plt.plot(t, y)

plt.title('This is a great title')
plt.grid('on')
plt.axis([0, 1.2, -0.2, 1.5])
plt.legend(['v0*t - 0.5*g*t**2'])

plt.show()