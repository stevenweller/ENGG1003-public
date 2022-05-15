import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def RGB_to_gray(m):

    R = m[:, :, 0]
    G = m[:, :, 1]
    B = m[:, :, 2]

    return 0.2989*R + 0.5870*G + 0.1140*B


m = mpimg.imread('stinkbugs.jpg')
I = RGB_to_gray(m)
#plt.imshow(I, cmap='Greys')
plt.imshow(I, cmap='gray')

plt.show()
