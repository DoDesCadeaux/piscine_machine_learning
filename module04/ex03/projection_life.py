import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def clean_dataframe(value):
    if 'k' in str(value):
        return float(value.replace('k', '')) * 1000
    return float(value)

def main():
    income_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expect = load("life_expectancy_years.csv")
    
    x = income_df["1900"].map(clean_dataframe)
    y = life_expect["1900"]

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_ylabel("Life Expectancy")
    ax.set_xlabel("Gross domestic product")
    ax.set_xscale('log')
    plt.title("1900")
    plt.xticks([300, 1000, 10e3], ["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main() 
