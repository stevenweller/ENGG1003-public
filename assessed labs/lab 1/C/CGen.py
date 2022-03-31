import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,4*np.pi,300)

y = -3.4*np.sin(0.5*t+3*np.pi/2)

plt.plot(t,y)
plt.title("Oscillation One Vs. Time")
plt.savefig("plot.png")

with open("sequence.txt", "w") as f:
    x = np.zeros(10)
    x[0] = 0
    f.write(f'\\\\{x[0]:.5f}\\\\\n')
    sum1 = x[0]
    sum2 = 0
    n = 0
    while n < 9:
        n = n + 1
        x[n] = 0.2*x[n-1] - 5
        sum1 = sum1 + x[n]
        if x[n] < -6.1:
            sum2 = sum2 + x[n]
            print(sum2)
        f.write(f'{x[n]:.5f}\\\\\n')

with open("sum1.txt", "w") as f:
    f.write(f'{sum1:.5f}')

with open("sum2.txt", "w") as f:
    f.write(f'{sum2:5f}')