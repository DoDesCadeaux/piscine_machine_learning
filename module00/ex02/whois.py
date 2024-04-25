from sys import argv


def whois(number):
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    elif number % 2 != 0:
        print("I'm Odd.")


def main():
    if len(argv) == 1:
        print("No args provided")
    elif len(argv) > 2:
        print("AssertionError: more than one argument provided")
    elif not argv[1].isdecimal():
        print("AssertionError: argument is not an integer")
    else:
        whois(int(argv[1]))


if __name__ == "__main__":
    main()
