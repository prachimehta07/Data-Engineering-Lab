import pandas as pd
import os

df = pd.read_csv("data/metrics.csv")

partition_count = 0

for (year, month, region), group in df.groupby(["year", "month", "region"]):
    folder = f"partitions/year={year}/month={month}/region={region}"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, "metrics.csv")
    group.to_csv(file_path, index=False)

    partition_count += 1

print("Partitioning completed.")
print("Partitions created:", partition_count)