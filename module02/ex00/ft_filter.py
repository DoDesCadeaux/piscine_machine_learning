def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable. Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:An iterable.
    None if the iterable can not be used by the function.
    """
    try:
        for i in iterable:
            if function_to_apply(i):
                yield i
                continue
    except TypeError:
        return None


def is_even(x):
    return x % 2 == 0


def main():
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = ft_filter(is_even, x)
    print(list(y))


if __name__ == "__main__":
    main()

