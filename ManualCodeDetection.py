import cv2
import numpy as np

img = cv2.imread('tutorial.png')
scale = 1
width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)
resized = cv2.resize(img, (width, height))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (7,7), 0)

thresholded = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#kernel = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
closed = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel, iterations=2)

thresholded = cv2.dilate(closed, kernel)
original_sized = cv2.resize(thresholded, (img.shape[1],img.shape[0]), interpolation = cv2.INTER_LINEAR )# eredeti méretre vissza

contours, hierarchy = cv2.findContours(original_sized, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

img_contours = np.zeros(img.shape)
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 1)

candidates = []
for cont in contours:
    perim = cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, 0.04 * perim, True)
    x,y,w,h = cv2.boundingRect(approx)
    area = cv2.contourArea(cont)
    ratio = w / float(h)
    if len(approx) == 4 and area > 1000 and (ratio > .80 and ratio < 1.2):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        extracted = img[y:y + h, x:x + w]

    rect = cv2.minAreaRect(cont)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    candidate = {"coords": rect}
    candidates.append(candidate)

#print(candidates)
cv2.imshow('Original image', img)
#cv2.imshow('QR code', extracted)
cv2.imshow("Contours", img_contours)
cv2.waitKey()