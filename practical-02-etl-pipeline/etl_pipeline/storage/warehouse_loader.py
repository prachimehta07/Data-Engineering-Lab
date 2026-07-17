import sqlite3
import pandas as pd

def load_to_warehouse(valid_rows, table_name, db_path="warehouse/warehouse.db"):
    if not valid_rows:
        print(f"No valid rows to load for {table_name}")
        return

    df = pd.DataFrame(valid_rows)
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded {len(valid_rows)} rows into {table_name}")