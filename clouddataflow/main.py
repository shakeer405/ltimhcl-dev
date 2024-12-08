import argparse
import json
from datetime import datetime

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from apache_beam.io.gcp.pubsub import ReadFromPubSub
from apache_beam.io.gcp.bigquery import WriteToBigQuery


def parse_message(message):
    """
    Parse and validate Pub/Sub message.
    """
    try:
        # Decode JSON message
        payload = json.loads(message)
        # Validate fields
        device_id = payload["device_id"]
        temperature = float(payload["temperature"])
        humidity = float(payload["humidity"])
        status = payload.get("status", "unknown")
        timestamp = payload.get("timestamp", datetime.utcnow().isoformat())

        # Ensure temperature and humidity are within range
        if not (-50 <= temperature <= 150):
            raise ValueError("Temperature out of range")
        if not (0 <= humidity <= 100):
            raise ValueError("Humidity out of range")

        # Return validated data
        return {
            "device_id": device_id,
            "temperature": temperature,
            "humidity": humidity,
            "status": status,
            "timestamp": timestamp,
        }
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        print(f"Invalid message: {e}")
        return None


def run(argv=None):
    """
    Main entry point for the Dataflow pipeline.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_topic",
        required=True,
        help="Pub/Sub topic to read data from, e.g., projects/your-project-id/topics/iot-data-topic",
    )
    parser.add_argument(
        "--output_table",
        required=True,
        help="BigQuery table to write data to, e.g., your-project-id:iot_data.telemetry",
    )
    args, pipeline_args = parser.parse_known_args(argv)

    # Define pipeline options
    options = PipelineOptions(pipeline_args)
    options.view_as(StandardOptions).streaming = True  # Enable streaming mode

    # Define the pipeline
    with beam.Pipeline(options=options) as p:
        (
            p
            | "ReadFromPubSub" >> ReadFromPubSub(topic=args.input_topic)
            | "DecodeMessage" >> beam.Map(lambda msg: msg.decode("utf-8"))
            | "ParseAndValidate" >> beam.Map(parse_message)
            | "FilterValidMessages" >> beam.Filter(lambda x: x is not None)
            | "WriteToBigQuery"
            >> WriteToBigQuery(
                args.output_table,
                schema={
                    "fields": [
                        {"name": "device_id", "type": "STRING", "mode": "REQUIRED"},
                        {"name": "temperature", "type": "FLOAT", "mode": "REQUIRED"},
                        {"name": "humidity", "type": "FLOAT", "mode": "REQUIRED"},
                        {"name": "status", "type": "STRING", "mode": "NULLABLE"},
                        {"name": "timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"},
                    ]
                },
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            )
        )
