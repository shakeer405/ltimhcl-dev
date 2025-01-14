from google.cloud import storage
from google.api_core.exceptions import GoogleAPICallError, NotFound, Forbidden
import logging
logging.getLogger('google').setLevel(logging.ERROR)
logging.getLogger('google.auth').setLevel(logging.ERROR)
def delete_bucket(bucketname):
    try:
        client = storage.Client()
        bucket = client.bucket(bucketname)
        bucket.delete()
        print(f"Bucket {bucketname} deleted")
    except NotFound:
        print(f"bucket {bucketname} not found")


if __name__ == "__main__":
    bucketname="ltidevbucket-998"
    delete_bucket(bucketname)