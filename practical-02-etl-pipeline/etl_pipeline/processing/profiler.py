def discover_schema(df, name):
    schema = {
        "dataset": name,
        "columns": list(df.columns),
        "dtypes": {col: str(df[col].dtype) for col in df.columns},
        "num_columns": len(df.columns)
    }
    return schema

def profile_data(df, name):
    profile = {
        "dataset": name,
        "rows": len(df),
        "columns": len(df.columns),
        "null_counts": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_usage_bytes": int(df.memory_usage(deep=True).sum())
    }
    return profile

def print_report(schema, profile):
    print(f"\n=== {schema['dataset'].upper()} ===")
    print(f"Rows: {profile['rows']}")
    print(f"Columns: {profile['columns']}")
    print(f"Column names: {schema['columns']}")
    print(f"Data types: {schema['dtypes']}")
    print(f"Null values: {profile['null_counts']}")
    print(f"Duplicate rows: {profile['duplicate_rows']}")
    print(f"Memory usage: {profile['memory_usage_bytes']} bytes")

if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ingestion"))
    from file_reader import read_customers
    from db_reader import read_products
    from api_reader import read_transactions
    from config_reader import read_config

    config = read_config()

    customers = read_customers()
    products = read_products()
    transactions = read_transactions(config["API_URL"], int(config["TIMEOUT"]))

    for df, name in [(customers, "customers"), (products, "products"), (transactions, "transactions")]:
        schema = discover_schema(df, name)
        profile = profile_data(df, name)
        print_report(schema, profile)