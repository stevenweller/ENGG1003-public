import numpy as np

m = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# 4 rows, 3 cols
print(m)

# number of rows = 4
print(len(m))
print(np.size(m, 0))
print(m.shape[0])

# number of cols = 3
print(len(m[0]))
print(np.size(m, 1))
print(m.shape[1])