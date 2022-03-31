import matplotlib.pyplot as plt
import matplotlib.image as mpimg

m = mpimg.imread('stinkbugs.jpg')  # m is a numpy array

# array dimensions: rows=618, columns=926, RGB=3
print(m.shape)
print(type(m))

plt.imshow(m)
plt.show()