from google.cloud import bigquery
from google.cloud import storage
import os

# client = bigquery.Client()
# query = "SELECT * FROM ltmhcl-dev.iot_data.telemetry LIMIT 10"
# query_job = client.query(query)
# client.copy_table('ltmhcl-dev.iot_data.telemetry','ltmhcl-dev.iot_data.telemetry1')
# print(query_job)

# for row in query_job:
#     print(row)
destination_file_name = "local-filename.txt"
storage_client = storage.Client()
bkt1=storage_client.bucket('pe-qe-3489')
print(bkt1)
blob=bkt1.blob('result.csv')
blob.download_to_filename(destination_file_name)
# storage_client.download_blob_to_file('gs://pe-qe-3489/result.csv','result.csv')
buck = storage_client.list_buckets()

for bkt in buck:
    print(bkt)






# def query_bigquery_and_upload_to_gcs(query, destination_bucket_name, destination_blob_name, output_file_path):

#     # Initialize BigQuery client
#     bigquery_client = bigquery.Client()

#     # Execute query
#     query_job = bigquery_client.query(query)
#     results = query_job.result()

#     # Write query results to a local file (CSV format)
#     with open(output_file_path, "w") as output_file:
#         fieldnames = [field.name for field in results.schema]
#         output_file.write(",".join(fieldnames) + "\n")  # Write header
#         for row in results:
#             output_file.write(",".join(str(row[field]) for field in fieldnames) + "\n")

#     print(f"Query results written to {output_file_path}")

#     # Initialize GCS client
#     storage_client = storage.Client()

#     # Upload file to GCS bucket
#     bucket = storage_client.bucket(destination_bucket_name)
#     blob = bucket.blob(destination_blob_name)
#     blob.upload_from_filename(output_file_path)

#     print(f"File uploaded to GCS: gs://{destination_bucket_name}/{destination_blob_name}")

#     # Optionally remove the local file
#     os.remove(output_file_path)
#     print(f"Local file {output_file_path} removed.")