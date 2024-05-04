import pandas as pd

def load(path: str):
    if not isinstance(path, str):
        print("Path should be a string")
        return None
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
    except :
        print("CSV Dataset file not found or bad format")
        return None
    return dataset



def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
