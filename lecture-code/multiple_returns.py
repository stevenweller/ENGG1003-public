import numpy as np

def circle(r):
    """calculate circumference and area given radius"""
    return 2*np.pi*r, np.pi*r**2

circ, area = circle(5)
print("Circumference: {:.3f}".format(circ))
print("Area         : {:.3f}".format(area))