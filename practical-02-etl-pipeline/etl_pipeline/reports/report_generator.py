import csv

def write_schema_report(schemas, path="output/schema_report.txt"):
    with open(path, "w") as f:
        for schema in schemas:
            f.write(f"=== {schema['dataset'].upper()} ===\n")
            f.write(f"Columns: {schema['columns']}\n")
            f.write(f"Dtypes: {schema['dtypes']}\n\n")

def write_quality_report(profiles, valid_invalid_counts, path="output/quality_report.txt"):
    with open(path, "w") as f:
        for profile in profiles:
            name = profile["dataset"]
            f.write(f"=== {name.upper()} ===\n")
            f.write(f"Rows: {profile['rows']}\n")
            f.write(f"Nulls: {profile['null_counts']}\n")
            f.write(f"Duplicate rows: {profile['duplicate_rows']}\n")
            valid, invalid = valid_invalid_counts.get(name, (0, 0))
            f.write(f"Valid: {valid}, Invalid: {invalid}\n\n")

def write_rejected_records(invalid_rows, path="output/rejected_records.csv"):
    if not invalid_rows:
        with open(path, "w") as f:
            f.write("no rejected records\n")
        return

    keys = set()
    for row in invalid_rows:
        keys.update(row.keys())
    keys = list(keys)

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(invalid_rows)