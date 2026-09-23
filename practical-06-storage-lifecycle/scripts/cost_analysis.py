import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RESULT_FILE = BASE_DIR / "results" / "lifecycle_results.csv"

COST_PER_GB = {
    "HOT": 10,
    "WARM": 5,
    "COLD": 1
}


def calculate_cost():
    tier_storage = {
        "HOT": 0,
        "WARM": 0,
        "COLD": 0
    }

    with open(RESULT_FILE, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tier = row["assigned_tier"]
            size_mb = float(row["size_mb"])

            tier_storage[tier] += size_mb

    total_mb = sum(tier_storage.values())
    total_gb = total_mb / 1024

    baseline_cost = total_gb * COST_PER_GB["HOT"]

    lifecycle_cost = 0

    for tier in tier_storage:
        storage_gb = tier_storage[tier] / 1024
        lifecycle_cost += storage_gb * COST_PER_GB[tier]

    savings = baseline_cost - lifecycle_cost
    savings_percentage = (savings / baseline_cost) * 100

    print("Storage Lifecycle Cost Analysis")
    print("--------------------------------")
    print(f"Total storage: {total_mb:.2f} MB")
    print()

    for tier in tier_storage:
        print(f"{tier}: {tier_storage[tier]:.2f} MB")

    print()
    print(f"Cost without lifecycle: {baseline_cost:.2f} units")
    print(f"Cost with lifecycle:    {lifecycle_cost:.2f} units")
    print(f"Estimated savings:      {savings:.2f} units")
    print(f"Savings percentage:     {savings_percentage:.2f}%")


if __name__ == "__main__":
    calculate_cost()