import cv2
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

# To capture video from webcam.
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

def FaceDetector(filename):
    lastSeen = (350, 600, 160, 160)  # somewhere in the center
    frame_height = 720
    frame_width = 1280
    frames = []

    cap = cv2.VideoCapture(filename)
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            if len(faces) == 0:  # no detections
                (x, y, w, h) = lastSeen
            else:
                (x, y, w, h) = faces[0]
                lastSeen = faces[0]

            # cv2.circle(img, (x + (w // 2), y + (h // 2)), 2, (255, 0, 0), 2)
            scale = int(w * 0.9)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            center = (x + (w // 2), y + (h // 2) + int(h * 0.3))
            properX, properY = center
            # cv2.circle(img, center, 2, (255, 255, 255), 2)
            if properX - scale < 0 or properY - scale < 0 or properX + scale > frame_width or properY + scale > frame_height:
                properX = frame_width // 2
                properY = frame_height // 2
                print("UH OH!")

            # cv2.rectangle(img, (properX - scale, properY - scale), (properX + scale, properY + scale), (255, 255, 255),2)

            crop_img = gray[properY - scale:properY + scale, properX - scale:properX + scale]
            # Display
            resize = cv2.resize(crop_img, (160, 160))
            resize = resize[:, :, np.newaxis]
            frames.append(resize)

            # Display the resulting frame
            # cv2.imshow('Frame',gray)

            # Press Q on keyboard to  exit
            # if cv2.waitKey(25) & 0xFF == ord('q'):
            #    break

        # Break the loop
        else:
            break

    # When everything done, release the video capture object
    cap.release()

    return np.asarray(frames)
