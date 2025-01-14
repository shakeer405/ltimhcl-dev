from google.cloud import bigquery

# create a bigquery client
client = bigquery.Client()
queryjob = """
 SELECT device_id, temperature FROM `ltmhcl-dev.iot_data.telemetry1`
"""
jobres = client.query(queryjob)

for row in jobres:
    print(f"Iot device id: {row['device_id']}, and Temparature of Iot device: {row['temperature']} ")
