import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

class ImageProcessor:
    def load(self, path):
        array = np.asarray(Image.open(path))
        img_dimensions = array.shape 
        print(f"Loading image of dimsensions {img_dimensions[0]}x{img_dimensions[1]}")
        print(array)
        return array

    def display(self, array):
        plt.imshow(array)
        plt.show()


imp = ImageProcessor()
imp.display(imp.load("42AI.png"))

