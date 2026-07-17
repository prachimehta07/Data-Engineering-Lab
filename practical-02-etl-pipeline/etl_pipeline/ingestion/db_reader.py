import sqlite3
import pandas as pd

def read_products(path="source_system/database/products.db"):
    conn = sqlite3.connect(path)
    df = pd.read_sql("SELECT * FROM products", conn)
    conn.close()
    return df

if __name__ == "__main__":
    df = read_products()
    print(df.head())
    print(df.shape)