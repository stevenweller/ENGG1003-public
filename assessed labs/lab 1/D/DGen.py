import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2*np.pi,2*np.pi/3,150)

y = -2.5*np.sin(5*t+6*np.pi/5)

plt.plot(t,y)
plt.title("Oscillation One Vs. Time")
plt.savefig("plot.png")

with open("sequence.txt", "w") as f:
    x = np.zeros(10)
    x[0] = 3.5
    f.write(f'\\\\{x[0]:.5f}\\\\\n')
    sum1 = x[0]
    sum2 = 0
    n = 0
    while n < 9:
        n = n + 1
        x[n] = 1.3*x[n-1] + 2.1
        sum1 = sum1 + x[n]
        if x[n] > 16 and x[n] < 50:
            sum2 = sum2 + x[n]
        f.write(f'{x[n]:.5f}\\\\\n')

with open("sum1.txt", "w") as f:
    f.write(f'{sum1:.5f}')

with open("sum2.txt", "w") as f:
    f.write(f'{sum2:5f}')