# 🛠️ Tools Referenced in Practical 1

Scoped to what actually appears in the Practical 1 architecture — not a forward-looking course list. Add a new section here only when a later practical introduces a genuinely new tool.

## Design & Docs

| Tool | What it's for |
|------|----------------|
| **Draw.io / diagrams.net** | Free tool to draw architecture diagrams as editable shapes, not flat images |
| **Git / GitHub** | Version control and hosting for this repository |
| **Markdown** | Plain-text formatting used for every `.md` file here |

## Ingestion

| Tool | What it's for |
|------|----------------|
| **Apache Kafka** | Real-time message queue — lets many systems publish/subscribe to events (e.g. "an order happened") without talking to each other directly |
| **Apache Flink** | Processes Kafka streams continuously as they arrive (windowing, checkpointing) |
| **Apache Spark** | Processes large batches (or streams) of data in parallel — used for heavier ETL and CDC |

## Storage

| Tool | What it's for |
|------|----------------|
| **Delta Lake / Apache Iceberg** | Table formats that add transactional reliability to files sitting in cheap storage |
| **Parquet** | Compressed, column-based file format — faster to query than CSV |
| **Snowflake / BigQuery / Redshift** | Managed cloud data warehouses for business-ready, queryable data |

## Transformation

| Tool | What it's for |
|------|----------------|
| **dbt** | SQL-based transformations with version control and testing built in |
| **Python / SQL** | Languages used for cleaning, joining, and business-logic code |

## Serving

| Tool | What it's for |
|------|----------------|
| **Power BI / Tableau** | Turns processed data into dashboards |
| **FastAPI** | Exposes processed data as a REST API |
| **PostgreSQL** | Relational database — where the transactional data (orders, customers) is born |
| **MongoDB** | Document database — used for less-structured data like logs or clickstream events |
