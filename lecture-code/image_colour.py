import matplotlib.pyplot as plt
import numpy as np

# create a 3D numpy array, 20x20 RGB image
m = np.zeros([20, 20, 3], int)

# purple cross on a red background
m[:, :] = [255, 0, 0]       # all pixels red by default
m[8:12, :] = [65, 0, 125]   # rows 8-11 are purple
m[:, 8:12] = [65, 0, 125]   # columns 8-11 are purple

plt.imshow(m)
plt.axis('off')
plt.savefig('purple_cross.jpeg')
plt.show()