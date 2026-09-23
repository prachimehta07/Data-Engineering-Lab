# Practical 5: Partitioned Data Storage and Query Performance Evaluation

## Aim

To implement partitioned data storage using MinIO object storage and evaluate the performance difference between full-table scanning and partition-based querying.

## Objective

The practical demonstrates how partitioning analytical data by year, month, and region can reduce unnecessary data scanning and improve query performance.

## Dataset

A synthetic dataset containing 20,000 application metric records was generated.

### Dataset Columns

- `timestamp`
- `year`
- `month`
- `region`
- `application`
- `metric`
- `value`

### Dataset Details

- Records: 20,000
- Years: 2023–2025
- Regions: Gujarat, Maharashtra, Delhi, Rajasthan
- Applications: MobileApp, WebApp, API, Payment
- Metrics: response_time, cpu_usage, memory_usage, request_count

## Partitioning

The dataset was partitioned using the following structure:

```text
year → month → region