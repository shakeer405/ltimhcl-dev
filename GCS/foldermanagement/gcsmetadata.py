from google.cloud import storage

def get_file_metadata(bucket_name, blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.reload()
    print(f"File Size: {blob.size} bytes")
    print(f"Content-Type: {blob.content_type}")
    # signed_url=blob.generate_signed_url(version='v4', expiration=40, method='GET')
    # print( signed_url)
    acl=blob.acl
    acl.get_entity(blob)
if __name__ == "__main__":
    bucketname="ltidevbucket-999"
    blob_name="prodnotes.txt"
    get_file_metadata(bucketname, blob_name)
