import re
import os
import sys
import time

import cv2
import numpy as np

from math import *
from skimage.feature import local_binary_pattern


cap = cv2.VideoCapture('bread.mp4')

#
# if __name__ == "__main__":
#     r = cv2.selectROI(im)
#     extractFeature(gtPath);
#     print('ok')
# 2424 5800
#3838


# cap.set(1,5000)


ret, frame = cap.read()
res = cv2.resize(frame, None, fx=.7, fy=.7, interpolation=cv2.INTER_BITS)
res  = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)


selected = [ 0,0]
while selected == [0,0]:
    _, frame = cap.read()
    res = cv2.resize(frame, None, fx=.7, fy=.7, interpolation=cv2.INTER_BITS)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    r = cv2.selectROI(res)
    selected = [r[1],r[0]]


template = res[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
detector = cv2.ORB_create(nfeatures=500)


w = template.shape[1]
h = template.shape[0]

xSize, ySize, zSize = frame.shape
aux = 0;
print(xSize,ySize)

while(cap.isOpened()):

    ret, img = cap.read()
    res = cv2.resize(img, None, fx=.7, fy=.7, interpolation=cv2.INTER_BITS)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    start = time.time()

    res1 = cv2.matchTemplate(res, template, cv2.TM_CCOEFF_NORMED)  # TM_CCOEFF_NORMED TM_CCOEFF

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res1)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    #
    if max_val > 0.7:
        cv2.rectangle(res, top_left, bottom_right, 255, 2)

    end = time.time()

    cv2.imshow('Normal', res)

    if cv2.waitKey(0) & 0xFF == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()

# https://www.youtube.com/watch?v=QK-Z1K67uaA