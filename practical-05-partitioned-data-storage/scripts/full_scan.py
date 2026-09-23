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

start = time.time()

response = s3.list_objects_v2(Bucket=bucket)

all_data = []

for obj in response.get("Contents", []):
    if obj["Key"].endswith(".csv"):
        data = s3.get_object(
            Bucket=bucket,
            Key=obj["Key"]
        )["Body"].read()

        df = pd.read_csv(io.BytesIO(data))
        all_data.append(df)

full_df = pd.concat(all_data, ignore_index=True)

# Example query
result = full_df[
    (full_df["year"] == 2025) &
    (full_df["region"] == "Gujarat")
]

end = time.time()

print("FULL TABLE SCAN")
print("----------------")
print("Total records scanned:", len(full_df))
print("Records returned:", len(result))
print("Execution time:", round(end - start, 4), "seconds")