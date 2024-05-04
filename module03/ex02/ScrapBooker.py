import numpy as np

class ScrapBooker:

    def crop(self, array, dim, position=(0, 0)):
        start_y, start_x = position
        height, width = dim

        end_y = start_y + height
        end_x = start_x + width

        if end_y > array.shape[0] or end_x > array.shape[1]:
            return None

        return array[start_y:end_y, start_x:end_x]


    def thin(self, array, n, axis):
        if (
            not isinstance(array, np.ndarray)
            or not isinstance(n, int)
            or not isinstance(axis, int)
        ):
            return None
        if n < 0:
            return None
        if axis == 0 and n > array.shape[0]:
            return None
        elif axis == 1 and n > array.shape[1]:
            return None

        if axis == 0:
            indexes_to_delete = np.arange(
                0, array.shape[0], n
            )  # Array des indices: De 0 a array.shape[0] (6), avec un step de n
            new_arr = np.delete(array, indexes_to_delete, axis)
            return new_arr

        if axis == 1:
            indexes_to_delete = np.arange(0, array.shape[1], n)
            new_arr = np.delete(array, indexes_to_delete, axis)
            return new_arr


    def juxtapose(self, array, n, axis):
        if (
            not isinstance(n, int)
            or not isinstance(axis, int)
            or not isinstance(array, np.ndarray)
        ):
            return None
        if axis == 0:
            juxt = np.tile(array, (n, 1))
        elif axis == 1:
            juxt = np.tile(array, (1, n))
        else:
            return None
        return juxt


    def mosaic(self, array, dim):
        if not isinstance(dim, tuple) or not isinstance(array, np.ndarray):
            return None
        mosaic = np.tile(array, dim)
        return mosaic


sb = ScrapBooker()
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print(arr2.shape)
print()
result = sb.thin(arr2, 3, 1)
print(arr2)

arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

juxt = sb.juxtapose(arr3, 4, 0)
print(juxt)

mosa = sb.mosaic(arr3, (3, 2))
print(mosa)
