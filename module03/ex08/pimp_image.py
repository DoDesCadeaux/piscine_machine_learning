import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def ft_invert(img) -> np.ndarray:
    inverted_img = 255 - img
    plt.imshow(inverted_img)
    plt.show()
    return inverted_img

def ft_red(array) -> np.ndarray:
    red = np.copy(array)
    red[::, ::, 1::] = 0
    plt.imshow(red)
    plt.show()
    return red

def ft_green(array) -> np.ndarray:
    green = np.copy(array)
    green[::, ::, [0, 2]] = 0
    plt.imshow(green)
    plt.show()
    return green

def ft_blue(array) -> np.ndarray:
    blue = np.copy(array)
    blue[::, ::, [0, 1]] = 0
    plt.imshow(blue)
    plt.show()
    return blue

def ft_grey(array) -> np.ndarray:
    mean = np.mean(array, axis=2)
    mean_expanded = np.expand_dims(mean, axis=2)
    grey = np.repeat(mean_expanded, 3, axis=2).astype(np.uint8)

    plt.imshow(grey)
    plt.show()
    return grey

def main():
    loaded_img = ft_load("landscape.jpg")
    try:
        print(loaded_img)
        ft_invert(loaded_img)
        ft_green(loaded_img)
        ft_blue(loaded_img)
        ft_red(loaded_img)
        ft_grey(loaded_img)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
