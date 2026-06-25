import cv2
import time


video = cv2.VideoCapture(1)
# 0: Iphone
# 1: Integrated Camera
time.sleep(1)

first_frame = None

while True:
    check, frame = video.read()

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()