import cv2
from pyzbar.pyzbar import decode

image = cv2.imread('tutorial.png')

for code in decode(image):
    print(code.type)
    print(code.data.decode('utf-8'))