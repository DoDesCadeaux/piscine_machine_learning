from typing import Any

from numpy import sqrt

def mean(args):
    return sum(args) / len(args)


def median(args):
    i = int(len(args) / 2)
    return args[i]


def quartile(args):
    quartile = []
    i = int(len(sorted(args)) / 4)
    j = int(len(sorted(args)) / 4) * 3
    quartile.append(args[i])
    quartile.append(args[j])
    return quartile


def standard_deviation(args):
    x_bar = mean(args)
    ecart = []
    for elem in args:
        ecart.append(round((elem - x_bar) ** 2, ndigits=2))
    ecart_bar = mean(ecart)
    return sqrt(ecart_bar)


def variance(args):
    squared = []
    for elem in args:
        squared.append(elem ** 2)
    return sum(squared) / len(args) - (mean(args) ** 2)


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError("All args must be int")
    sorted_args = sorted(args)
    authorized_operations = ["mean", "median", "quartile", "std", "var"]

    for elem in kwargs.values():
        if not isinstance(elem, str) or not elem in authorized_operations:
            raise TypeError("Key-word values must be valid operations")
        if elem == "mean":
            x_bar = mean(sorted_args)
            print(f"mean: {x_bar:.2f}")
        if elem == "median":
            med = median(sorted_args)
            print(f"median: {med}")
        if elem == "quartile":
            quart = quartile(sorted_args)
            print(f"quartile: [{quart[0]:.1f}, {quart[1]:.1f}]")
        if elem == "std":
            std = standard_deviation(args)
            print(f"std: {std}")
        if elem == "var":
            print(f"var: {variance(args)}")

            
            

def main():
    try:
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, prout="mean", shi="median", fu="quartile", lo="std", variance="var")
    except TypeError as te:
        print(te)

if __name__ == "__main__":
    main()
