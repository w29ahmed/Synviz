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

        # Download .npy file from gcp
        download_blob(storage_client, bucketname, filename, filename)

        # Load data into a numpy array
        np_array = np.load(filename)

        # Remove .npy file locally and remove it from gcp
        os.remove(filename)
        delete_blob(storage_client, bucketname, filename)

        # Change extension to mp4 and write to disk
        pre, _ = os.path.splitext(filename)
        mp4_filename = pre + ".mp4"

        # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
        print(np_array.shape)
        out = cv2.VideoWriter(mp4_filename, cv2.VideoWriter_fourcc(*"H264"), 30, (np_array.shape[2], np_array.shape[1]))
        for frame in np_array:
            # Write the frame into the file 'output.avi'
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        out.release()

        # Upload .mp4 file to gcp
        upload_blob(storage_client, bucketname, mp4_filename, mp4_filename)

        # # Lip tracking + model inferenece
        # model_input_array = FaceDetector(np_array)
        # prediction = evaluate_model(model_input_array).replace('-', ' ').capitalize()
        # print(prediction)

        # # Construct gcp url so frontend can stream it to webpage
        # gcp_url = "https://storage.cloud.google.com/%s/%s" % (bucketname, mp4_filename)

        # out_dict = {"url": gcp_url, "text": prediction}

        # # Emit the url on the socket - frontend should be listening to this
        # socketio.emit("FromAPI", out_dict)

        return "Success"

@socketio.on('connect')
def connect():
    print("Succesfully connected")

if __name__ == "__main__":
    socketio.run(app)