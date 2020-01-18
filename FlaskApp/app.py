from flask import Flask, request, redirect
from flask_socketio import SocketIO
# from google.cloud import storage
from gcp_utils import *
from datetime import datetime

# Initialize flask app
app = Flask(__name__)

# Configure socket IO
# TODO: Make more secure secret key, enables secure client connection
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Instantiate Google Cloud client
storage_client = storage.Client()

def gcp_test(storage_client):
    # Generate unique file name with a timestamp
    dt_string = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    bucket_name = "uofthacksvii_test_%s" % dt_string

    source_file_name = "python.png"

    # gcp test functions
    create_bucket(storage_client, bucket_name)
    upload_blob(storage_client, bucket_name, source_file_name, source_file_name)
    download_blob(storage_client, bucket_name, source_file_name, "gcp_test.png")
    list_blobs(storage_client, bucket_name)
    blob_metadata(storage_client, bucket_name, source_file_name)

# Homepage URL routing
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        gcp_test(storage_client)

        try:
            gcp_test(storage_client)
            return "Success"
        except:
            return "Something went wrong"
    else:
        filename = request.form['filename']

        try:
            download_blob(storage_client, "uofthacksvii", filename, filename)
            return "Success"
        except:
            return "Something went wrong"

if __name__ == "__main__":
    socketio.run(app)