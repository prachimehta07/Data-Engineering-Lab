import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "ingestion"))
sys.path.append(os.path.join(os.path.dirname(__file__), "processing"))
sys.path.append(os.path.join(os.path.dirname(__file__), "storage"))
sys.path.append(os.path.join(os.path.dirname(__file__), "reports"))

from config_reader import read_config
from file_reader import read_customers
from db_reader import read_products
from api_reader import read_transactions

from profiler import discover_schema, profile_data, print_report
from validator import validate_customer, validate_product, validate_transaction, separate_valid_invalid

from warehouse_loader import load_to_warehouse
from report_generator import write_schema_report, write_quality_report, write_rejected_records

def run_pipeline():
    print("Reading config...")
    config = read_config()

    print("Extracting data from all sources...")
    customers = read_customers()
    products = read_products()
    transactions = read_transactions(config["API_URL"], int(config["TIMEOUT"]))

    schemas = []
    profiles = []
    valid_invalid_counts = {}
    all_invalid_rows = []

    datasets = [
        (customers, "customers", validate_customer, "customer_id"),
        (products, "products", validate_product, "product_id"),
        (transactions, "transactions", validate_transaction, None)
    ]

    for df, name, validate_func, id_col in datasets:
        schema = discover_schema(df, name)
        profile = profile_data(df, name)
        print_report(schema, profile)

        schemas.append(schema)
        profiles.append(profile)

        valid_rows, invalid_rows = separate_valid_invalid(df, validate_func, id_col)
        valid_invalid_counts[name] = (len(valid_rows), len(invalid_rows))
        all_invalid_rows.extend(invalid_rows)

        load_to_warehouse(valid_rows, name, config["WAREHOUSE_DB"])

    print("Writing reports...")
    write_schema_report(schemas)
    write_quality_report(profiles, valid_invalid_counts)
    write_rejected_records(all_invalid_rows)

    print("Pipeline complete. Check the output/ folder.")

if __name__ == "__main__":
    run_pipeline()