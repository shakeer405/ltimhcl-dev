from google.cloud import storage
import os
bucketname="ltidevbucket-999"
client = storage.Client(project='ltmhcl-dev')
# bucket = client.create_bucket(bucketname, location='us-east1')
def createbucket(bucketname):
    # client = storage.Client(project='ltmhcl-dev')
    # bucket = client.create_bucket(bucketname, location='us-east1')
    print(f"created {bucket.name} in GCP project.")

def listbuckets():
    bucketlist = client.list_buckets()
    
    print(f"bucket list under project ltimdevhcl")
    for buckets in bucketlist:
        print(f" - {buckets.name}")
        # print ("Blob are:",client.list_blobs(buckets.name))
        blobobjs = client.list_blobs(buckets.name)
        for bobj in blobobjs:
            print(f"Blobs {bobj} under bucket are {buckets.name}")
            print(bobj)

def fileupload():
    # bucketobj = client.bucket(bucketname)
    print(f"present working is {os.getcwd()}")
    bucket = client.bucket('bucketname')
    # print(bucket)
    filename='C://Users//Shakeer//Documents//gcpautomationwebsite//dataflow//GCS//prodnotes.txt'
    blobobj = bucket.blob(filename)
    with open(filename, 'rb') as file:
        contents = file.read()
    
    blobobj.upload_from_string(contents)
    # blobobj.upload_from_filename(filename)
    # print(blobobj)

if __name__ == "__main__":
    bucketname="ltidevbucket-999"
    # blobname=filenew.txt
    # filepath=pro
    # project="ltmhcl-dev"
    # createbucket(bucketname)
    # listbuckets()
    # fileupload(blobname, filepath, bucketname)
    fileupload()

