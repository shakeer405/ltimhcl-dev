#Exporting Data from Bigquery to GCS 
from google.cloud import bigquery
client = bigquery.Client()
table_id = "ltmhcl-dev.iot_data.telemetry1"
destination_uri = "gs://ltidevbucket-999/iottelemetry.csv"

extract_job = client.extract_table(
    table_id,
    destination_uri,
    location="US"  # Location of the dataset
)

extract_job.result()  # Wait for the job to complete
print(f"Exported data to {destination_uri}")