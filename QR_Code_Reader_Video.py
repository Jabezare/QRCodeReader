import cv2
import numpy as np
from pyzbar.pyzbar import decode

capture = cv2.VideoCapture(0)

used_codes = []

camera = True
while camera == True:
    success, frame = capture.read()

    for code in decode(frame):
        points = code.polygon
        (x,y,w,h) = code.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255, 0, 0), 3)

        codeData = code.data.decode("utf-8")
        codeType = code.type
        floatingText = "Type: " + str(codeType) + " | Data: " + str(codeData)
        
        cv2.putText(frame, floatingText, (x,y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
        
        if codeData not in used_codes:
            print("New Code!")
            print("Type: "+codeType +" | Data: "+codeData)
            used_codes.append(code.data.decode('utf-8'))
        else:
            pass

    frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5)
    cv2.imshow('Video input', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera = False