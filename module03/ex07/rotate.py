import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np


def rotate(image):
    image_T = np.empty((image.shape[1], image.shape[0]))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image_T[j][i] = image[i][j]

    return image_T


def zoom(image, start_y, end_y, start_x, end_x):
    if end_y > image.shape[0] or end_x > image.shape[1]:
        raise ValueError("Values out of bound")
    elif start_y < 0 or start_x < 0:
        raise ValueError("Values out of bound")
    return image[start_y:end_y, start_x:end_x, 0]


def display_img(img):
    plt.imshow(img, cmap="gray")
    print(f"New shape {img.shape}")
    plt.show()


def main():
    loaded_img = ft_load("animal.jpeg")
    try:
        zoomed = zoom(loaded_img, 0, 480, 400, 900)
        print(zoomed)
        display_img(zoomed)
        rotated = rotate(zoomed)
        print(rotated)
        display_img(rotated)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
