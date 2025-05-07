from matplotlib import pyplot as plt
import cv2
import os
import random
import time

# ___pynq board display output (untested)___
# from pynq.overlays.base import BaseOverlay
# from pynq.lib.video import *

# frame_out_w = 1920
# frame_out_h = 1080
# base = BaseOverlay("base.bit")
# Mode = VideoMode(640, 480, 24)
# hdmi_out = base.video.hdmi_out
# hdmi_out.configure(Mode, PIXEL_BGR)
# hdmi_out.start()
# outframe = hdmi_out.newframe()


# def show_frame(frame):
#     outframe[0:480, 0:640, :] = frame[0:480, 0:640, :]
#     hdmi_out.writoutframe


# ___matplotlib display output ✔️___
from matplotlib import pyplot as plt

plt.ion()


def out_html(
    right,
    wrong,
    game_over,
    player_count,
    face_count,
):
    with open("templates/index.html", "w") as f:
        f.write(
            f"""
<!DOCTYPE html>
<html>

    <head>
        <title>The Admin Page™</title>
        <meta http-equiv="refresh" content="1">
    </head>

    <body>
        <h1>Right: {right}, Wrong: {wrong}, Game Over: {game_over}, Player Count: {player_count}, Face Count: {face_count}</h1>
        <img src="{{{{ url_for('static', filename='frame.png') }}}}" alt="Current frame" width="400">
        <img src="{{{{ url_for('static', filename='after_process.png') }}}}" alt="Last processed frame" width="400">
    </body>

</html>            
"""
        )


def show_frame(frame):
    plt.imshow(frame[:, :, [2, 1, 0]])
    plt.pause(1)
    plt.show()


# camera (input) configuration
videoIn = cv2.VideoCapture(0)
videoIn.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
videoIn.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
videoIn.set(cv2.CAP_PROP_BUFFERSIZE, 1)


def read_video():
    # get rid of buffer
    videoIn.read()
    videoIn.read()
    ret, frame = videoIn.read()
    cv2.imwrite("static/frame.png", frame)
    return ret, frame


os.environ["OPENCV_LOG_LEVEL"] = "SILENT"
player_count = 3
try:
    # TODO player count with button
    player_count = int(os.environ["PLAYER_COUNT"])
except:
    pass


time_val = 10
right = 0
wrong = 0
while wrong < 2:
    if time_val > 2:
        time_val -= 1
    face_count = random.randint(0, player_count)
    out_html(right, wrong, False, player_count, face_count)
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
        show_frame(frame)
        # plt.show()

    status, frame = read_video()
    show_frame(frame)
    ### Step 4: Now use matplotlib to show image inside notebook

    # Output webcam image as JPEG

    ### Step 5: Apply the face detection to the input

    frame = frame

    face_cascade = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    success = len(faces) == face_count
    if success:
        right += 1
    else:
        wrong += 1

    cv2.putText(
        frame,
        f"Faces Captured:{len(faces)}, SUCCESS:{success}",
        (20, 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 0),
        2,
    )
    cv2.putText(
        frame,
        f"Score:{right}, Failed:{wrong}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 0),
        2,
    )
    cv2.imwrite("static/after_process.png", frame)
    show_frame(frame)

out_html(right, wrong, True, player_count, 0)
status, frame = read_video()
cv2.putText(
    frame,
    f"Game over. Score:{right}",
    (20, 25),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 0),
    2,
)
show_frame(frame)
# TODO press button for new game
time.sleep(10)

videoIn.release()
# hdmi_out.stop()
# del hdmi_out
