import matplotlib.pyplot as plt
import numpy as np

m = np.zeros([10, 10])  # array of float zeros
m[4:6, :] = 1       # set rows 4 and 5
m[:, 4:6] = 1       # set columns 4 and 5

m[2, 2] = 0.5       # gray pixel

plt.imshow(m, cmap='Greys')
plt.xticks([])      # suppress x-axis ticks
plt.yticks([])      # suppress y-axis ticks

# save the figure
plt.savefig('gray_image_2.jpg')

plt.show()