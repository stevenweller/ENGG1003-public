import numpy as np

# array of heights (m)
h = np.array([1.6, 1.85, 1.75, 1.8, 0.5])
total = 0
for i in range(0, 5):
    total += h[i]
avg = total/len(h)
print("Average height is: {}m".format(avg))