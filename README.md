# Data Engineering Laboratory

A working repository of Data Engineering lab practicals. Each practical lives in its own folder, self-contained: open one, understand one, no dependency on the others.

This repo doesn't pre-commit to a fixed number of practicals — folders are added as work is completed, not scaffolded in advance.

---

## Start here

The recurring idea across this lab is a five-step cycle that almost every data platform is built around:

```text
Generation → Ingestion → Storage → Transformation → Serving
   (born)      (moves)      (rests)      (reshaped)    (used)
```

Individual practicals zoom into one part of this cycle at a time. Whatever tools appear (Kafka, Spark, dbt, MinIO...) exist to make one of those five steps work at real scale — that's the lens to view every practical through.

---

## Structure

```text
Data-Engineering-Lab/
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── tools.md
│   └── references.md
│
├── practical-01-data-engineering-lifecycle/
│   ├── README.md
│   ├── architecture/
│   └── manifesto/
│
├── practical-02-etl-pipeline/
│   ├── README.md
│   ├── source_system/
│   ├── etl_pipeline/
│   ├── warehouse/
│   └── output/
│
├── practical-03-kafka-streaming/
│   ├── producer.py
│   ├── consumer.py
│   ├── sample-output/
│   ├── screenshots/
│   └── README.md
│
└── practical-06-storage-lifecycle/
    ├── README.md
    ├── data/
    ├── policies/
    ├── results/
    └── scripts/
```

Each practical folder documents itself in its own `README.md` — that's the single entry point per practical.

---

## Practicals

| # | Practical | Summary |
|---|-----------|---------|
| 1 | [Enterprise Data Engineering Lifecycle](./practical-01-data-engineering-lifecycle) | End-to-end architecture diagram + design rationale + manifesto for an e-commerce platform |
| 2 | [ETL Pipeline with Schema Discovery & Validation](./practical-02-etl-pipeline) | Simulated file/API/DB source systems, schema discovery, profiling, validation, and warehouse loading |
| 3 | [Kafka Real-Time Streaming Pipeline](./practical-03-kafka-streaming) | Apache Kafka Producer–Consumer implementation for real-time web activity log ingestion with latency and throughput measurement |
| 6 | [Storage Lifecycle Management](./practical-06-storage-lifecycle) | Automated Hot/Warm/Cold classification of operational logs and audit records using object age and access frequency, with cost analysis and background automation |

---

## Objectives

- Understand enterprise data engineering architecture end to end.
- Design scalable ETL and streaming data pipelines.
- Practice real-time data ingestion using Apache Kafka.
- Measure streaming performance using latency and throughput metrics.
- Apply storage lifecycle management concepts.
- Classify operational data using age and access frequency.
- Automate storage-tier decisions using Python.
- Analyze the potential cost reduction from data tiering.
- Practice professional technical documentation.
- Use Git and GitHub for version control and project management.

---

## Author

**Name: Prachi**