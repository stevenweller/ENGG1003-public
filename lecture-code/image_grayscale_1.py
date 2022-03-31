import matplotlib.pyplot as plt
import numpy as np

m = np.zeros([10, 10])
m[4:6, :] = 1
m[:, 4:6] = 1

plt.imshow(m, cmap='Greys')
plt.show()