import pandas as pd

def read_customers(path="source_system/data/customers.json"):
    df = pd.read_json(path)
    return df

if __name__ == "__main__":
    df = read_customers()
    print(df.head())
    print(df.shape)