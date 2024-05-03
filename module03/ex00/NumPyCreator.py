from collections.abc import Iterable
from random import randint
import numpy as np

class NumPyCreator:
    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list):
            return None
        return np.array(lst, dtype=dtype)
    
    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple):
            return None
        return np.array(tpl, dtype=dtype)

    def from_iterable(self, itr, dtype=None):
        if not isinstance(itr, Iterable):
            return None
        return np.array(list(itr), dtype=dtype)

    def from_shape(self, shape, value=None, dtype=None):
        if not isinstance(shape, tuple):
            return None
        if not value:
            value = 0
        return np.full(shape, value, dtype=dtype)

    def random(self, shape, dtype=None):
        if not isinstance(shape, tuple):
            return None
        value = randint(0, 1000)
        return np.full(shape, value, dtype=dtype)

if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
    at = ("a", "b", "c")

    b = NumPyCreator()
    c = b.from_list(a)
    ct = b.from_tuple(at)

    f_shape = b.from_shape((2, 3))

    r_shape = b.random((3, 3), dtype=str)

    print(c)
    print(ct)
    print(f_shape)
    print(r_shape)

