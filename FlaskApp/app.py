import imageio
import os
import sys
import numpy as np
import cv2

from flask import Flask, request
from flask_socketio import SocketIO, emit
from gcp_utils import *
from datetime import datetime
from FaceDetector import FaceDetector

from deep_lip_reading.main import evaluate_model

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
        bucketname = "uofthacksvii"

        download_blob(storage_client, bucketname, filename, filename)

        # Lip tracking + model inferenece
        input_array = FaceDetector(filename)
        print(input_array.shape)
        prediction = evaluate_model(input_array).replace('-', ' ').capitalize()

        # Construct gcp url so frontend can stream it to webpage
        gcp_url = "https://storage.cloud.google.com/%s/%s" % (bucketname, filename)

        out_dict = {"url": gcp_url, "text": prediction}

        # Emit the url on the socket - frontend should be listening to this
        socketio.emit("FromAPI", out_dict)

        return "Success"

@socketio.on('connect')
def connect():
    print("Succesfully connected")

if __name__ == "__main__":
    socketio.run(app)