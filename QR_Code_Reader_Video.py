import cv2
from pyzbar.pyzbar import decode
import time

capture = cv2.VideoCapture(0)

used_codes = []

camera = True
while camera == True:
    success, frame = capture.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print(code.type)
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(1)
        else:
            pass

    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5)
    cv2.imshow('Video input', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera = False