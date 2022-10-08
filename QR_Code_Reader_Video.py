import cv2
from pyzbar.pyzbar import decode
import time

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

used_codes = []

camera = True
while camera == True:
    success, frame = capture.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print('Approved')
            print(code.type)
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(5)
        elif code.data.decode('utf-8') in used_codes:
            print('Disapproved')
            time.sleep(5)
        else:
            pass

    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(27)