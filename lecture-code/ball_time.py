import numpy as np
import matplotlib.pyplot as plt

v0 = 4.5
g = 9.81
t = np.linspace(0, 1, num=1000)
y = v0*t - 0.5*g*t**2

i = 0
while y[i] >= 0:
    i += 1

print(i)
print(y[i-1])
print(y[i])
print("Flight time: {:.2f} s".format(t[i]))

plt.plot(t, y, '.')
plt.grid('on')
plt.show()