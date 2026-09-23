import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

regions = ["Gujarat", "Maharashtra", "Delhi", "Rajasthan"]
applications = ["MobileApp", "WebApp", "API", "Payment"]
metrics = ["response_time", "cpu_usage", "memory_usage", "request_count"]

records = []

start_date = datetime(2023, 1, 1)

for i in range(20000):
    timestamp = start_date + timedelta(
        minutes=random.randint(0, 3 * 365 * 24 * 60)
    )

    records.append({
        "timestamp": timestamp,
        "year": timestamp.year,
        "month": timestamp.month,
        "region": random.choice(regions),
        "application": random.choice(applications),
        "metric": random.choice(metrics),
        "value": round(random.uniform(10, 1000), 2)
    })

df = pd.DataFrame(records)

df.to_csv("data/metrics.csv", index=False)

print("Dataset generated successfully.")
print("Records:", len(df))
print("Saved to: data/metrics.csv")
print("\nSample:")
print(df.head())
