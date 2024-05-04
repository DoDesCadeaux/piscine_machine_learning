import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def aff_life(path: str):
    if not isinstance(path, str):
        raise TypeError("Path should be a str")


    df = load(path)
    belgium_data = df[df["country"] == "Belgium"].iloc[0, 1:]
    print(belgium_data)
    belgium_data.plot()
    plt.ylabel("Life Expectancy")
    plt.xlabel("Year")
    plt.show()


def main():
    aff_life("life_expectancy_years.csv")

if __name__ == "__main__":
    main()
