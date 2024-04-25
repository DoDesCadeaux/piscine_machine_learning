kata = (0, 4, 132.42222, 10000, 12345.67)


def main():
    if type(kata[0]) is not int or type(kata[1]) is not int or type(kata[3]) is not int:
        print("Expected int values are not integers")
        exit(1)
    elif kata[0] < 0 or kata[0] > 100 or kata[1] < 0 or kata[1] >= 100:
        print("First 2 values should be 2 non-negative integer containing up to 2 digits")
        exit(1)
    elif type(kata[2]) is not float or type(kata[4]) is not float:
        print("Expected float values are not decimals")
        exit(1)
    elif len(kata) != 5:
        print("Should be only 5 elements")
    print(f"module_{kata[0]:0>2d}, ex_{kata[1]:0>2d} : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}")


if __name__ == "__main__":
    main()
