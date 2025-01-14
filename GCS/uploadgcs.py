from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a file to a Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of your GCS bucket.
        source_file_name (str): The local file path to upload.
        destination_blob_name (str): The name of the file in the GCS bucket.
    """
    # Initialize a GCS client
    client = storage.Client()

    # Get the bucket
    bucket = client.bucket(bucket_name)

    # Create a blob in the bucket
    blob = bucket.blob(destination_blob_name)

    # Upload the file
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Example usage
bucket_name = "ltidevbucket-999"
source_file_name = "C://Users//Shakeer//Documents//gcpautomationwebsite//dataflow//GCS//prodnotes.txt"
destination_blob_name = "uploaded-file-name-in-gcs.txt"

upload_to_gcs(bucket_name, source_file_name, destination_blob_name)
