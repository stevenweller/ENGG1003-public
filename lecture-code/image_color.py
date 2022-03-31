import matplotlib.pyplot as plt
import numpy as np

# 3D numpy array for 20x20 image, each pixel [R,G,B]
m = np.zeros([20, 20, 3], int)

# purple cross on a red background
m[:, :] = [255, 0, 0]       # all pixels red by default
m[8:12, :] = [65, 0, 125]   # rows 8-11 are purple
m[:, 8:12] = [65, 0, 125]   # columns 8-11 are purple

plt.imshow(m)
plt.axis('off')             # no ticks, no axes
plt.savefig('purple_cross.jpg')
plt.show()