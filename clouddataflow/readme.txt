1. Enable Required APIs:

gcloud services enable dataflow.googleapis.com
gcloud services enable pubsub.googleapis.com
gcloud services enable bigquery.googleapis.com

Create a Pub/Sub Topic:

gcloud pubsub topics create iot-data-topic

Create a BigQuery Dataset and Table:

dataset: iot_data

Table: telemetry

CREATE TABLE `your_project_id.iot_data.telemetry` (
    device_id STRING,
    temperature FLOAT64,
    humidity FLOAT64,
    status STRING,
    timestamp TIMESTAMP
);


 Simulate Streaming Data:

 gcloud pubsub topics publish iot-data-topic \
    --message '{"device_id": "sensor-1", "temperature": 72.5, "humidity": 40, "status": "active"}'

Run the Dataflow Pipeline:

python main.py \
    --input_topic projects/your-project-id/topics/iot-data-topic \
    --output_table your-project-id:iot_data.telemetry \
    --runner DataflowRunner \
    --project your-project-id \
    --region us-central1 \
    --temp_location gs://your-bucket/temp \
    --staging_location gs://your-bucket/staging

