from flask import Flask
from google.cloud import storage
import sys

# Initialize flask app
app = Flask(__name__)

def upload_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}."
    .format(source_file_name, destination_blob_name),
    file = sys.stderr)

# Homepage URL routing
@app.route('/', methods=['GET'])
def index():
    upload_file
    return "Do you wanna make an app?"

if __name__ == "__main__":
    app.run(debug=True)