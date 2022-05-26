import numpy as np
import matplotlib.pyplot as plt

# Q1(a)
a = 1
b = -2
c = -3
x = 4
y = a*x**2 + b*x + c
print(y)

# Q1(b)
x = np.linspace(-5, 5, num=1001)
y = a*x**2 + b*x + c

plt.plot(x, y)
plt.grid('on')
plt.show()
