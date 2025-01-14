import os
from google.cloud import storage
print(os.getcwd())
source_directory = '.'

import os
from google.cloud import storage

def upload_directory_to_gcs(bucket_name, source_directory):
    """
    Uploads all files in a local directory to a GCS bucket while retaining the file names.

    Args:
        bucket_name (str): The name of your GCS bucket.
        source_directory (str): The local directory containing files to upload.
    """
    # Initialize GCS client
    client = storage.Client()

    # Get the bucket
    bucket = client.bucket(bucket_name)

    # Walk through the directory and upload files
    for root, _, files in os.walk(source_directory):
        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            blob_name = os.path.relpath(local_file_path, source_directory)  # Retains directory structure
            blob = bucket.blob(blob_name)

            # Upload file
            blob.upload_from_filename(local_file_path)
            print(f"Uploaded {local_file_path} to {blob_name}.")

# Example usage
bucket_name = "your-bucket-name"
source_directory = "."

upload_directory_to_gcs(bucket_name, source_directory)
