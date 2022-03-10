import numpy as np
import matplotlib.pyplot as plt

v0 = 4.5                     # Initial velocity
g = 9.81                     # Acceleration of gravity
t = np.linspace(0, 1, 1000)  # 1000 points in time interval
y = v0*t - 0.5*g*t**2        # Generate all heights

# find smallest i for which y[i] < 0
i = 0
while y[i] >= 0:
    i = i + 1

# Since y[i] is the height at time t[i], we know the
# time as well when we have the index i...
print('Time of flight (in seconds): {:.2f}'.format(t[i]))

plt.plot(t, y)
plt.plot(t, 0*t, 'g--')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()