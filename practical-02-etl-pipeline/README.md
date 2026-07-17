# Data Engineering Practical 2 - ETL Pipeline

## What this does
Simulates three source systems (JSON file, REST API, SQLite database) and
config-driven ETL, discovering schema, profiling, validating, and loading
clean data into a warehouse.

## How to run
1. python source_system/generators/customer_generator.py
2. python source_system/generators/product_generator.py
3. python source_system/generators/transaction_generator.py
4. uvicorn source_system.api.main:app --reload  (keep running)
5. python etl_pipeline/main.py

## Output
- warehouse/warehouse.db - clean records
- output/schema_report.txt - discovered schema per dataset
- output/quality_report.txt - row counts, nulls, valid/invalid split
- output/rejected_records.csv - rejected rows with reasons
