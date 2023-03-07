import requests
import boto3

# Set the API endpoint URL
api_url = "https://data.cityofnewyork.us/resource/2upf-qytp.csv"

# Set the S3 bucket name and object key
bucket_name = "nyc-datalake"
object_key = "data.csv"

# Set the AWS access key and secret access key
aws_access_key = "AKIA46BI4X4MXAPO4F7H"
aws_secret_access_key = "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"

# Retrieve the data from the API
response = requests.get(api_url)

# Parse the CSV data
data = response.content.decode('utf-8')

# Upload the data to the S3 bucket
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_access_key)
s3.put_object(Bucket=bucket_name, Key='raw/data.csv', Body=data, ContentType="text/csv")

print(f"Data uploaded to s3://{bucket_name}/{object_key}")
