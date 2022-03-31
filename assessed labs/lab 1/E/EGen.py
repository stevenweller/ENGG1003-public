import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,100)

y = 4.5*np.cos(3*t-np.pi)

plt.plot(t,y)
plt.title("Oscillation One Vs. Time")
plt.savefig("plot.png")

with open("sequence.txt", "w") as f:
    x = np.zeros(10)
    x[0] = -1.2
    x[1] = 1.0
    f.write(f'\\\\{x[0]:.5f}\\\\\n')
    f.write(f'{x[1]:.5f}\\\\\n')
    sum1 = x[0] + x[1]
    sum2 = 0
    for n in range(2,10):
        x[n] = 3*x[n-1] - 1.3*x[n-2]
        sum1 = sum1 + x[n]
        if x[n] > 10 and x[n] < 100:
            sum2 = sum2 + x[n]
        f.write(f'{x[n]:.5f}\\\\\n')

with open("sum1.txt", "w") as f:
    f.write(f'{sum1:.5f}')

with open("sum2.txt", "w") as f:
    f.write(f'{sum2:5f}')