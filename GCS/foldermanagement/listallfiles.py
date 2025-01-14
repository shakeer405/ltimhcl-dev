from google.cloud import storage
from google.api_core.exceptions import GoogleAPICallError, NotFound, Forbidden
import logging
logging.getLogger('google').setLevel(logging.ERROR)
logging.getLogger('google.auth').setLevel(logging.ERROR)
def list_files_in_folder(bucket_name, folder_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_name)
    for blob in blobs:
        print(blob.name)



if __name__ == "__main__":
    bucketname="ltidevbucket-999"
    folder_name = "ltidevbucket-999"

    list_files_in_folder(bucketname, folder_name)