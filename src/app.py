from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *

from matplotlib import pyplot as plt
import cv2
import os
import numpy as np
import time
import random
from threading import Thread

base = BaseOverlay("base.bit")

### Step 2: Initialize Webcam and HDMI Out
# monitor configuration: 640*480 @ 60Hz
Mode = VideoMode(640, 480, 24)
hdmi_out = base.video.hdmi_out
hdmi_out.configure(Mode, PIXEL_BGR)
hdmi_out.start()
outframe = hdmi_out.newframe()

# monitor (output) frame buffer size
frame_out_w = 1920
frame_out_h = 1080
# camera (input) configuration
frame_in_w = 640
frame_in_h = 480

videoIn = cv2.VideoCapture(0)
videoIn.set(cv2.CAP_PROP_FRAME_WIDTH, frame_in_w)
videoIn.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_in_h)
videoIn.set(cv2.CAP_PROP_BUFFERSIZE, 1)

os.environ["OPENCV_LOG_LEVEL"] = "SILENT"
player_count = 3
try:
    player_count = int(os.environ["PLAYER_COUNT"])
except:
    pass
# initialize camera from OpenCV

### Step 3: Show input frame on HDMI output


def read_video():
    videoIn.read()
    videoIn.read()
    return videoIn.read()


# Capture webcam image
# plt.ion()

time_val = 10
right = 0
wrong = 0
while wrong < 2:
    if time_val > 2:
        time_val -= 1
    face_count = random.randint(0, player_count)
    for i in range(time_val, 0, -1):
        status, frame = read_video()
        # plt.pause(1)
        cv2.putText(
            frame,
            f"FACE COUNT:{face_count}, COUNTDOWN: {i}",
            (20, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 0),
            2,
        )
        # plt.imshow(frame[:, :, [2, 1, 0]])
        outframe[0:480, 0:640, :] = np_frame[0:480, 0:640, :]
        hdmi_out.writeframe(outframe)
        # plt.show()

    status, frame = read_video()
    # plt.pause(1)
    # plt.imshow(frame[:, :, [2, 1, 0]])
    outframe[0:480, 0:640, :] = np_frame[0:480, 0:640, :]
    hdmi_out.writeframe(outframe)
    cv2.imwrite("templates/pre_process.png", frame)
    # plt.show()

    ### Step 4: Now use matplotlib to show image inside notebook

    # Output webcam image as JPEG

    ### Step 5: Apply the face detection to the input

    np_frame = frame

    face_cascade = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(np_frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        cv2.rectangle(np_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    success = len(faces) == face_count
    if success:
        right += 1
    else:
        wrong += 1

    cv2.putText(
        np_frame,
        f"Faces Captured:{len(faces)}, SUCCESS:{success}",
        (20, 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 0),
        2,
    )
    cv2.putText(
        np_frame,
        f"Score:{right}, Failed:{wrong}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 0),
        2,
    )
    cv2.imwrite("templates/after_process.png", np_frame)

    # plt.pause(1)
    # plt.imshow(np_frame[:, :, [2, 1, 0]])
    # plt.show()

    ### Step 6: Show results on HDMI output
    # show the number of faces on the screen

    # Output OpenCV results via HDMI
    outframe[0:480, 0:640, :] = np_frame[0:480, 0:640, :]
    hdmi_out.writeframe(outframe)

    ### Step 7: Now use matplotlib to show image inside notebook

    # Output OpenCV results via matplotlib

    ### Step 8: Release camera and HDMI

    ## Game


videoIn.release()
hdmi_out.stop()
del hdmi_out
