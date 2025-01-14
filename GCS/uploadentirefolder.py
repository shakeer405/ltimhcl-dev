from google.cloud import storage
import os

def upload_folder(bucket_name, folder_path):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    for root, dirs, files in os.walk(folder_path):
        print(root, dirs, files)
        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            print(local_file_path)
            blob_name = os.path.relpath(local_file_path, folder_path)
            blob = bucket.blob(blob_name)
            # blob.upload_from_filename(local_file_path)
            print(f"Uploaded {local_file_path} to {blob_name}.")

if __name__ == "__main__":
    bucketname="ltidevbucket-999"
    folder_path = "D:\GCP_Architect\ltimhcl-dev\ltimhcl-dev\dataflow"
    upload_folder(bucketname, folder_path)