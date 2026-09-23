# Practical 06 - Storage Lifecycle Management

## Objective

To design and test an automated storage lifecycle policy that classifies operational data into Hot, Warm and Cold storage tiers based on data age and access frequency.

The objective is to reduce storage cost while keeping frequently accessed data readily available.

---

## Problem Definition

Historical operational logs and server audit records can consume large amounts of storage over time.

Keeping all historical data in the same high-performance storage tier can increase operational storage cost.

This practical implements a lifecycle management process that:

- Monitors object age
- Tracks access frequency
- Classifies objects into Hot, Warm and Cold tiers
- Simulates movement of objects between tiers
- Calculates the potential storage cost reduction
- Runs the lifecycle process periodically using a background Python script

---

## Project Structure

```text
practical-06-storage-lifecycle/
│
├── data/
│   ├── access_manifest.csv
│   ├── audit/
│   │   ├── audit_Q1_2026.txt
│   │   ├── audit_Q2_2026.txt
│   │   ├── audit_Q3_2026.txt
│   │   └── audit_Q4_2025.txt
│   │
│   └── logs/
│       ├── server_log_Q1_2026.txt
│       ├── server_log_Q2_2026.txt
│       ├── server_log_Q3_2026.txt
│       └── server_log_Q4_2025.txt
│
├── policies/
│   └── lifecycle.json
│
├── results/
│   ├── lifecycle_results.csv
│   └── tiers/
│       ├── HOT/
│       ├── WARM/
│       └── COLD/
│
└── scripts/
    ├── lifecycle_automation.py
    ├── cost_analysis.py
    └── background_automation.py