kata = "The right format is right I guess"


def main():
    if type(kata) is not str or (len(kata) > 42):
        print("InsertionError bad kata format")
        exit(2)
    print(f"{kata:->41}")


if __name__ == "__main__":
    main()
