'''
Questão 32
Após fazer a questão 31, calcule a área de cada contorno obtido através da função “cvContourArea”,
apresentando seu valor.
'''

import cv2 as cv
import numpy as np

img = cv.imread('../input_images/objects_canny.png')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny_img = cv.Canny(img, 80, 255)

contours, hierarchy = cv.findContours(canny_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours_img = np.copy(img)
cv.drawContours(contours_img, contours, -1, (0,0,255),3)
for i, contour in enumerate(contours):
    print(f"Area {i + 1}: " + str(cv.contourArea(contour)))

cv.imshow('Input grayscale image', grayscale_img)
cv.imshow('contours', contours_img)
cv.waitKey(0)