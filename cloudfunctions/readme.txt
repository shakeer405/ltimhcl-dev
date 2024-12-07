Here's a detailed example of using Google Cloud Functions for Data Transformation and ETL (Extract, Transform, Load) with real-time processing of data. This example will:

Extract data from Google Cloud Pub/Sub.
Transform the data by cleaning and normalizing it.
Load the transformed data into BigQuery.
Scenario
An IoT system sends telemetry data (e.g., temperature, humidity, device status) to a Pub/Sub topic. We want to:

Extract this data when a message is published.
Validate and normalize the data.
Load the cleaned data into a BigQuery table for analytics.
Project Setup
1. Enable Required APIs
Enable the following APIs in your Google Cloud project:

Cloud Functions:
bash

gcloud services enable cloudfunctions.googleapis.com
Pub/Sub:
bash

gcloud services enable pubsub.googleapis.com
BigQuery:
bash

gcloud services enable bigquery.googleapis.com
2. Create Resources
Create a Pub/Sub Topic:

bash

gcloud pubsub topics create iot-data-topic
Create a BigQuery Dataset and Table:

Dataset: iot_data
Table: telemetry
sql

CREATE TABLE `your_project_id.iot_data.telemetry` (
    device_id STRING,
    temperature FLOAT,
    humidity FLOAT,
    status STRING,
    timestamp TIMESTAMP
);
Cloud Function Code
1. Code Structure
css

cloud-function-etl/
├── main.py
├── requirements.txt
2. Code: main.py
python

import base64
import json
import os
from datetime import datetime

from google.cloud import bigquery

# Initialize BigQuery client
bigquery_client = bigquery.Client()

# BigQuery table details
BQ_DATASET = os.environ.get("BQ_DATASET", "iot_data")
BQ_TABLE = os.environ.get("BQ_TABLE", "telemetry")
BQ_TABLE_ID = f"{bigquery_client.project}.{BQ_DATASET}.{BQ_TABLE}"

def validate_and_transform(payload):
    """
    Validate and transform the incoming data.
    """
    try:
        # Extract fields from payload
        device_id = payload["device_id"]
        temperature = float(payload["temperature"])
        humidity = float(payload["humidity"])
        status = payload.get("status", "unknown")
        timestamp = payload.get("timestamp", datetime.utcnow().isoformat())

        # Ensure values are within expected ranges
        if temperature < -50 or temperature > 150:
            raise ValueError("Temperature out of range")
        if humidity < 0 or humidity > 100:
            raise ValueError("Humidity out of range")

        # Return cleaned and transformed data
        return {
            "device_id": device_id,
            "temperature": temperature,
            "humidity": humidity,
            "status": status,
            "timestamp": timestamp,
        }
    except Exception as e:
        print(f"Data validation error: {e}")
        return None

def insert_into_bigquery(data):
    """
    Insert transformed data into BigQuery.
    """
    try:
        # Insert data into BigQuery
        errors = bigquery_client.insert_rows_json(BQ_TABLE_ID, [data])
        if errors:
            print(f"BigQuery insert errors: {errors}")
        else:
            print("Data successfully inserted into BigQuery")
    except Exception as e:
        print(f"BigQuery insert error: {e}")

def process_pubsub_message(event, context):
    """
    Cloud Function triggered by Pub/Sub. Processes data and loads it into BigQuery.
    """
    try:
        # Decode the Pub/Sub message
        pubsub_message = base64.b64decode(event["data"]).decode("utf-8")
        payload = json.loads(pubsub_message)
        print(f"Received payload: {payload}")

        # Validate and transform the data
        transformed_data = validate_and_transform(payload)
        if not transformed_data:
            print("Invalid data, skipping BigQuery insertion.")
            return

        # Load the transformed data into BigQuery
        insert_into_bigquery(transformed_data)
    except Exception as e:
        print(f"Error processing message: {e}")
3. Dependencies: requirements.txt
plaintext

google-cloud-bigquery
Deploy the Cloud Function
Set Environment Variables: Define the BigQuery dataset and table for the function:

bash

export BQ_DATASET=iot_data
export BQ_TABLE=telemetry
Deploy the Function: Deploy the function with the Pub/Sub trigger:

bash

gcloud functions deploy process_pubsub_message \
    --runtime python310 \
    --trigger-topic iot-data-topic \
    --set-env-vars BQ_DATASET=iot_data,BQ_TABLE=telemetry \
    --region us-central1
Publish Messages to Pub/Sub
Simulate data by publishing a message to the Pub/Sub topic:

bash

gcloud pubsub topics publish iot-data-topic \
    --message '{"device_id": "sensor-1", "temperature": 72.5, "humidity": 40, "status": "active"}'
Verify Results
Logs: View the Cloud Function logs:

bash

gcloud functions logs read process_pubsub_message
BigQuery Table: Query the BigQuery table to verify data ingestion:

sql

SELECT * FROM `your_project_id.iot_data.telemetry` LIMIT 10;
How It Works
Trigger:
The function is triggered whenever a message is published to the iot-data-topic Pub/Sub topic.

Extract:
The function decodes and extracts the message payload.

Transform:

Validates that the data fields are within acceptable ranges.
Normalizes fields such as timestamp.
Load:

Inserts the cleaned and transformed data into a BigQuery table.
Use Cases
Real-time data pipelines for IoT, logs, or telemetry.
Streaming analytics for time-sensitive data.
ETL pipelines for preprocessing and storing data for dashboards and machine learning.
This approach can be extended to include more complex transformations or integrate with other services like Cloud Storage, Dataflow, or Dataproc for large-scale processing.
