from sys import argv


def operations(lhs: int, rhs: int):
    print(f"Sum: {lhs + rhs}")
    print(f"Difference: {lhs - rhs}")
    print(f"Product: {lhs * rhs}")
    if rhs == 0:
        print("Quotient: ERROR (division by zero)")
        print("Modulo: ERROR (modulo by zero)")
    else:
        print(f"Quotient: {lhs / rhs}")
        print(f"Modulo: {lhs % rhs}")


def main():
    if len(argv) == 1 or len(argv) == 2:
        print("Usage: python3 operations.py <number1> <number2>")
        print("Example:")
        print("    python3 operations.py 10 2")
    elif len(argv) > 3:
        print("AssertionError: too many arguments")
    elif not argv[1].isdecimal() or not argv[2].isdecimal():
        print("AssertionError: only integers")
    else:
        operations(int(argv[1]), int(argv[2]))


if __name__ == "__main__":
    main()
