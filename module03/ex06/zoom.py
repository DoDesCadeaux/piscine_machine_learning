import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(image, start_y, end_y, start_x, end_x):
    if end_y > image.shape[0] or end_x > image.shape[1]:
        raise ValueError("Values out of bound")
    elif start_y < 0 or start_x < 0:
        raise ValueError("Values out of bound")

    print(f"New shape {image[start_y:end_y, start_x:end_x].shape}")
    return image[start_y:end_y, start_x:end_x]


def display_img(img):
    plt.imshow(img)
    plt.show()


def main():
    loaded_img = ft_load("animal.jpeg")
    try:
        zoomed = zoom(loaded_img, 500, 610, 603, 800)
        display_img(zoomed)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
