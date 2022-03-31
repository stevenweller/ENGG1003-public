import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# a1 = [1 2 3]
a1 = m[0, :]        # row 0, all columns

# a2 = [2 5 8]
a2 = m[:, 1]        # all rows, column 1