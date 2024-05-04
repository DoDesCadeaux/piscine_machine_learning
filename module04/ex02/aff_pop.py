import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def convert_population(value):
    if 'k' in value:
        return float(value.replace('k', '')) * 1e3
    elif 'M' in value:
        return float(value.replace('M', '')) * 1e6
    elif 'B' in value:
        return float(value.replace('B', '')) * 1e9
    return float(value)

def aff_pop(path: str):
    df = load(path)
    df.iloc[:, 1:] = df.iloc[:, 1:].map(convert_population)
        
    belgium_data = df[df["country"] == "Belgium"].iloc[0, 1:]
    compare_data = df[df["country"] == "France"].iloc[0, 1:]
    print(compare_data)
    belgium_data.plot(label="Belgium")
    compare_data.plot(color="green", label="France")
    plt.title("Population Projections")
    plt.ylabel("Population")
    plt.yticks([20e6, 40e6, 60e6], ["20M", "40M", "60M"])
    plt.xlabel("Year")
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    aff_pop("population_total.csv")

