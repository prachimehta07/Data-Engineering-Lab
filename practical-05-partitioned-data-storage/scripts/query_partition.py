import boto3
import pandas as pd
import io
import time

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="Minio@12345",
    region_name="us-east-1"
)

bucket = "metrics"

year = 2025
region = "Gujarat"

prefix = f"year={year}/"

start = time.time()

response = s3.list_objects_v2(
    Bucket=bucket,
    Prefix=prefix
)

result_data = []
records_scanned = 0

for obj in response.get("Contents", []):
    key = obj["Key"]

    if f"region={region}/" in key and key.endswith(".csv"):
        data = s3.get_object(
            Bucket=bucket,
            Key=key
        )["Body"].read()

        df = pd.read_csv(io.BytesIO(data))

        records_scanned += len(df)

        filtered = df[df["region"] == region]
        result_data.append(filtered)

if result_data:
    result = pd.concat(result_data, ignore_index=True)
else:
    result = pd.DataFrame()

end = time.time()

print("PARTITION QUERY")
print("----------------")
print("Partition:", f"year={year}, region={region}")
print("Records scanned:", records_scanned)
print("Records returned:", len(result))
print("Execution time:", round(end - start, 4), "seconds")