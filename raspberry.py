# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import io
import numpy
import requests
from google.cloud import storage
import time
import RPi.GPIO as GPIO

storage_client = storage.Client()

def upload_file_gcp(bucket_name, source_file_name, destination_blob_name):
    """Uploads a blob (GCP's name for a file) to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1280, 720)
rawCapture = PiRGBArray(camera, size=(1280, 720))

API_ENDPOINT = "http://17eadbde.ngrok.io"
 
# allow the camera to warmup
time.sleep(0.1)
accum = []
state = 0
# capture frames from the camera
print("entering main loop!")
def blink():
        GPIO.output(37, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(37, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(37, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(37, GPIO.LOW)
        time.sleep(0.1)

blink()

while True:
        accum = []
        GPIO.output(37, GPIO.LOW)
        if state == 1:
                time.sleep(0.5)
                print("entering recording loop")
                GPIO.output(37, GPIO.HIGH)
                for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
                        # grab the raw NumPy array representing the image, then initialize the timestamp
                        # and occupied/unoccupied text
                        image = frame.array
                        accum.append(image)
                        if GPIO.input(31) == GPIO.HIGH: #we're recording and we were touched
                                GPIO.output(37, GPIO.LOW)
                                print("saving...")
                                rawCapture.truncate(0)
                                final = numpy.asarray(accum)
                                numpy.save("final.npy", final)
                                fname = str(int(time.time()))+".npy"
                                data = {'filename': fname}
                                print("uploading")
                                upload_file_gcp("uofthacksvii", "final.npy", fname)
                                print("uploaded!")
                                blink()
                                state = 0
                                r = requests.post(url = API_ENDPOINT, data = data) 
      
                                # extracting response text  
                                pastebin_url = r.text 
                                print("The pastebin URL is: %s"%pastebin_url)
                                break # get out of the recording
                        rawCapture.truncate(0)
                        
        if GPIO.input(31) == GPIO.HIGH:
                state = 1
