kata = (19, 42, 21)


def check_kata(kata):
    if type(kata) is not tuple:
        print("Kata should be a tuple")
        exit(1)
    to_check = list(kata)
    return to_check


def main():
    for n in check_kata(kata):
        n = str(n)
        if not n.isdecimal():
            print(f"Kata element: '{n}' is not integer")
            exit(1)
    print(f"The 3 numbers are: {kata[0]}, {kata[1]}, {kata[2]}")


if __name__ == "__main__":
    main()
