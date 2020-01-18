from flask import Flask
from google.cloud import storage
import sys

# Initialize flask app
app = Flask(__name__)

# Instantiate Google Cloud client
storage_client = storage.Client()

def create_bucket_gcp(bucket_name):
    """Creates a new bucket. Can fail if bucket name is not available"""
    # bucket_name = "your-bucket-name"

    storage_client.create_bucket(bucket_name)
    print("Bucket {} created".format(bucket_name), file = sys.stderr)

def upload_file_gcp(bucket_name, source_file_name, destination_blob_name):
    """Uploads a blob (GCP's name for a file) to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))

def download_file_gcp(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob (GCP's name for a file) from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print("Blob {} downloaded to {}.".format(source_blob_name, destination_file_name))

def list_blobs_gcp(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)

# Homepage URL routing
@app.route('/', methods=['GET'])
def index():
    # upload_file_gcp("uofthacksvii", "test_img.png", "upload_img2.png")
    # download_file_gcp("uofthacksvii", "demo.mp4", "demo2.mp4")

    list_blobs_gcp("uofthacksvii")

    return "Do you wanna make an app?"

if __name__ == "__main__":
    app.run(debug=True)