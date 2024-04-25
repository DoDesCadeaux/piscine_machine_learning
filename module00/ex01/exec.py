from sys import argv


def main():
    merged_input = ' '.join(argv[1::])

    new_input = ""
    for c in merged_input[::-1]:
        if c.islower():
            new_input += c.upper()
        else:
            new_input += c.lower()

    if len(argv) > 1:
        print(new_input)


if __name__ == "__main__":
    main()
