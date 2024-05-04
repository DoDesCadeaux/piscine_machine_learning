import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("lists must be the same length")
    if not all(isinstance(x, (int, float)) for x in height):
        raise TypeError("Height elements should be int or float")
    elif not all(isinstance(x, (int, float)) for x in weight):
        raise TypeError("Weight elements should be int or float")

    bmi = np.empty(0)
    for h, w in zip(height, weight):
        result = w / (h**2)
        bmi = np.append(bmi, result)
    return list(bmi)

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise ValueError("BMI elements should be float or int")
    if not isinstance(limit, int):
        raise ValueError("limit should be a int")

    limits = list()
    for element in bmi:
        if element > limit:
            limits.append(True)
        elif element < limit:
            limits.append(False)
        else:
            limits.append(True)
    return limits


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi)
    print(apply_limit(bmi, 30))

if __name__ == "__main__":
    main()
