import requests
import pandas as pd

def read_transactions(api_url, timeout=30):
    response = requests.get(api_url, timeout=timeout)
    response.raise_for_status()
    data = response.json()
    df = pd.json_normalize(data)
    return df

if __name__ == "__main__":
    from config_reader import read_config
    config = read_config()
    df = read_transactions(config["API_URL"], int(config["TIMEOUT"]))
    print(df.head())
    print(df.shape)