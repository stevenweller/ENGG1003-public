import numpy as np
import matplotlib.pyplot as plt

x = np.zeros([9, 9])

for row in range(0, 9, 2):
    x[row, :] = 1

print(x)

plt.imshow(x, cmap='Greys')
plt.show()
