from collections.abc import Iterable


def ft_map(function_to_apply, iterable):
    """ Map the function to all elements of the iterable. Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
        Return: An iterable. None if the iterable can not be used by the function.
    """
    try:
        for i in iterable:
            yield function_to_apply(i)
    except TypeError:
        return None


def addition(x) -> int :
    return x + 1


def main():
    y = [1, 2, 3, 4, 5]
    z = ft_map(addition, y)
    print(list(z))

if __name__ == "__main__":
    main()
