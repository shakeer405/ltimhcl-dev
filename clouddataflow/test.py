import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run(argv=None):
    """
    Entry point for the pipeline.
    """
    parser = argparse.ArgumentParser(description="Dataflow Pipeline")
    
    # Define expected arguments
    parser.add_argument(
        '--input_topic',
        required=True,
        help='Pub/Sub topic to read data from. Format: projects/<PROJECT_ID>/topics/<TOPIC_NAME>'
    )
    parser.add_argument(
        '--output_table',
        required=True,
        help='BigQuery table to write results to. Format: <PROJECT_ID>:<DATASET>.<TABLE>'
    )
    parser.add_argument(
        '--runner',
        default='DirectRunner',
        help='Pipeline runner to use. Options: DataflowRunner or DirectRunner'
    )
    parser.add_argument(
        '--project',
        required=True,
        help='Google Cloud project ID.'
    )
    parser.add_argument(
        '--region',
        required=True,
        help='Google Cloud region for the Dataflow job.'
    )
    parser.add_argument(
        '--temp_location',
        required=True,
        help='GCS path for temporary files.'
    )
    parser.add_argument(
        '--staging_location',
        required=True,
        help='GCS path for staging files.'
    )
    
    # Parse arguments
    known_args, pipeline_args = parser.parse_known_args(argv)

    # Print arguments (for debugging)
    print("Parsed arguments:", vars(known_args))

    # Pipeline logic (minimal example)
    pipeline_options = PipelineOptions(pipeline_args)
    with beam.Pipeline(options=pipeline_options) as pipeline:
        (
            pipeline
            | "Create Example Data" >> beam.Create([{"example_key": "example_value"}])
            | "Log Example Data" >> beam.Map(print)
        )

if __name__ == "__main__":
    run()

