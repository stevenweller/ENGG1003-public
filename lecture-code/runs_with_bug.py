import numpy as np

# sum elements of array
total = 0
x = np.array([1, 2, 3, 4])
for i in range(1, 4):
    total += x[i]

print("Total is: {}".format(total))