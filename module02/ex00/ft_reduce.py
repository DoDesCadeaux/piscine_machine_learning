def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
    iterable:
        an iterable object (list, tuple, iterator).

    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """

    try:
        result = iterable[0]
        i = 1
        while i < len(iterable):
            result = function_to_apply(result, iterable[i])
            i += 1
        return result

    except TypeError as e:
        print(e)
        return None


def add(x, y):
    return x + y


def main():
    x = [1, 2, 3, 4, 5, 6]
    z = ft_reduce(add, x)
    print(z)

if __name__ == "__main__":
    main()
