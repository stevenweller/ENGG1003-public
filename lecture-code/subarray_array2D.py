import numpy as np

m = np.array([[1,2,3],[4,5,6],[7,8,9]])

a = m[0, [0, 2]]        # row 0, cols 0 & 2
m2 = m[:, [0, 2]]       # all rows, cols 0 & 2