import numpy as np

x = np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0])

x[2] = x[1] + x[0]
x[3] = x[2] + x[1]
x[4] = x[3] + x[2]
x[5] = x[4] + x[3]
x[6] = x[5] + x[4]
x[7] = x[6] + x[5]
x[8] = x[7] + x[6]
x[9] = x[8] + x[7]

print(x)