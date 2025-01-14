from google.cloud import bigquery
client = bigquery.Client()

dataset_id = "ltmhcl-dev.iot_data"
table_id = "telemetry1"

filepath = "D://GCP_Architect//ltimhcl-dev//ltimhcl-dev//bigquery//jcb.csv"

job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=False)

with open(filepath, "rb") as source_fie:
    load_job = client.load_table_from_file(source_fie, f"{dataset_id}.{table_id}", job_config=job_config)

load_job.result()

print(f"Loaded {load_job.output_rows} rows into {dataset_id}.{table_id}")