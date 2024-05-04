import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


class ColorFilter:
    def invert(self, array):
        inverted = np.copy(array)
        inverted = 255 - inverted
        imgplot = plt.imshow(inverted)
        plt.show()
        print(inverted.shape)

    def to_blue(self, array):
        blue = np.copy(array)
        blue[::, ::, 0:2] = 0
        plt.imshow(blue)
        plt.show()

    def to_green(self, array):
        green = np.copy(array)
        green[::, ::, [0, 2]] = 0
        plt.imshow(green)
        plt.show()

    def to_red(self, array):
        red = np.copy(array)
        red[::, ::, 1:] = 0
        plt.imshow(red)
        plt.show()

arr1 = np.asarray(Image.open("42AI.png"))
filter = ColorFilter()

# filter.invert(arr1)
# filter.to_blue(arr1)
filter.to_green(arr1)
filter.to_red(arr1)
