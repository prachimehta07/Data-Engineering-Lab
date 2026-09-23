import boto3
import os

MINIO_ENDPOINT = "http://localhost:9000"
ACCESS_KEY = "admin"
SECRET_KEY = "Minio@12345"
BUCKET_NAME = "metrics"

s3 = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="us-east-1"
)

try:
    s3.head_bucket(Bucket=BUCKET_NAME)
    print("Bucket found:", BUCKET_NAME)
except Exception:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print("Bucket created:", BUCKET_NAME)

count = 0

for root, dirs, files in os.walk("partitions"):
    for file in files:
        if file.endswith(".csv"):
            local_path = os.path.join(root, file)

            object_name = os.path.relpath(
                local_path, "partitions"
            ).replace("\\", "/")

            s3.upload_file(
                local_path,
                BUCKET_NAME,
                object_name
            )

            count += 1
            print("Uploaded:", object_name)

print("\nUpload completed.")
print("Total partitions uploaded:", count)