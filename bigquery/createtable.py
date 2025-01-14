from google.cloud import bigquery
client = bigquery.Client()
# Define table schema
schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="NULLABLE"),
]

dataset_id ="ltmhcl-dev.iot_data"
table_id = "telemetry2"

table = bigquery.Table(f"{dataset_id}.{table_id}", schema=schema)
# client.create_table(table=table)

print(f"Created table {table_id}")

tab1 = list(client.list_tables(dataset_id))
# print(tab1)
# for tables in tab1:
#     print(tables.table_id)

if tab1:
    print("Tables:")
    for table in tab1:
        print(table.table_id)
else:
    print("No tables found in the dataset.")