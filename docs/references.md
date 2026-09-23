# References

Resources used while researching and building this lab.

## Official Docs

- Apache Kafka — Official Documentation
- Apache Flink — Official Documentation
- Apache Spark — Official Documentation
- Delta Lake — Official Documentation
- Apache Iceberg — Official Documentation
- dbt — Official Documentation
- Draw.io / diagrams.net — Official Documentation
- MinIO — Official Documentation
- MinIO Client (`mc`) — Official Documentation
- Python — Official Documentation

## Concepts

- *Fundamentals of Data Engineering* — Joe Reis & Matt Housley (O'Reilly)
- *Designing Data-Intensive Applications* — Martin Kleppmann

## Cloud Platforms

- AWS — Big Data, Data Lakes and Analytics
- GCP — Data Lake Solutions
- Azure — Data Lake Solutions

---

## Practical 2 — ETL Pipeline

- Faker Documentation
- Pandas Documentation
- FastAPI Documentation
- Requests Documentation
- SQLite Documentation

---

## Practical 3 — Kafka Streaming

- Apache Kafka Documentation
- Apache Kafka Quickstart
- kafka-python-ng Documentation and Repository
- Pandas Documentation

---

## Practical 6 — Storage Lifecycle Management

- MinIO Documentation — Object storage concepts and S3-compatible storage
- MinIO Client Documentation — Command-line object storage management
- Python Documentation — File handling, CSV, JSON and automation
- JSON Documentation / Python `json` module — Lifecycle policy configuration
- Python `csv` module — Access manifest and lifecycle result processing
- Python `pathlib` module — Cross-platform file and directory handling
- Python `shutil` module — Simulated movement/copying of objects between storage tiers
- Python `time` module — Periodic background lifecycle checks

### Practical 6 Concepts

- Storage lifecycle management
- Hot, Warm and Cold storage tiers
- Object age and retention
- Access frequency
- Storage cost optimization
- Automated data tiering
- Background lifecycle processing
- Object-storage lifecycle policies

> Note: Practical 6 uses a Python-based lifecycle simulation for the actual tier classification and movement. The local MinIO AIStor environment was used as the intended object-storage context, but native S3 operations were not used because the local installation required a valid license.