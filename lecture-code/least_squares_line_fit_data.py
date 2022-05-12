import numpy as np
import matplotlib.pyplot as plt

x = np.array([20.5, 32.7, 51.0, 73.2, 95.7])    # temp (degC)
y = np.array([765, 826, 873, 942, 1032])  # resistance (ohms)

plt.plot(x, y, 'r.', markersize=15)
plt.xlabel('x')
plt.ylabel('y')
plt.show()