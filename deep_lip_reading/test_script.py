#!/usr/bin/env python

import numpy as np
from main import evaluate_model

import cv2

def load_vid():
    #cap = cv2.VideoCapture('media/example/yeeterson.mp4')
    cap = cv2.VideoCapture('media/example/where_is_the_bathroom.mp4')

    frames = []
    
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # yeeterson
            #gray = gray[100:700, 450:1050]

            # bathroom
            gray = cv2.transpose(gray)
            gray = gray[550:1050, 325:825]

            gray = cv2.resize(gray, (160, 160))
            gray = gray[:, :, np.newaxis]
            frames.append(gray)
        
            # Display the resulting frame
            #cv2.imshow('Frame',gray)
            
        
            # Press Q on keyboard to  exit
            #if cv2.waitKey(25) & 0xFF == ord('q'):
            #    break
        
        # Break the loop
        else: 
            break

    # When everything done, release the video capture object
    cap.release()
    
    # Closes all the frames
    #cv2.destroyAllWindows()

    np_video = np.stack(frames, axis=0)
    print(np_video.shape)
    return np_video


if __name__=="__main__":
    video = load_vid()
    prediction = evaluate_model(video)
    print(prediction)


