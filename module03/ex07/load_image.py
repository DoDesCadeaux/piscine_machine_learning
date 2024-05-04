import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    image_arr = np.asarray(Image.open(path))
    print(f"The shape of image is: {image_arr.shape}")
    return image_arr
