import numpy as np


def sphere(r):
    return 4*np.pi*r**3/3


r = 2
V = sphere(r)
print("Volume: {:.4f}".format(V))
