from sys import argv as av
import re


def args_protection():
    if len(av) != 3:
        print("ERROR")
        exit(1)
    if type(av[1]) is not str:
        print("ERROR")
        exit(1)
    elif av[2]:
        try:
            int(av[2])
        except ValueError:
            print("ERROR")
            exit(1)


def arg_to_list(av):
    no_ponctuation = re.sub(r'[^\w\s]', '', av[1])

    formatted_list = no_ponctuation.split()
    return formatted_list


def bigger_than_n(arg_list):
    final = [w for w in arg_list if len(w) > int(av[2])]

    return final


def main():
    args_protection()
    arg_list = arg_to_list(av)
    final = bigger_than_n(arg_list)
    print(final)


if __name__ == "__main__":
    main()
