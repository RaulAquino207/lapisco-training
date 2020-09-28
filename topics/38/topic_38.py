'''
Questão 38
Faça o mesmo que a questão 37, alterando o elemento estruturante e sua referência e verifique o que acontece.
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../input_images/vase.jpg')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, otsu_img = cv.threshold(grayscale_img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

'''
# Rectangular Kernel
cv.getStructuringElement(cv.MORPH_RECT,(5,5))

# Elliptical Kernel
cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))

# Cross-shaped Kernel
cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
'''

cv.imshow('Threshold image', otsu_img)
structuring_elements = [cv.MORPH_RECT, cv.MORPH_ELLIPSE, cv.MORPH_CROSS]

# Apply dilation and show the results for each structuring element
plt.figure(1)
titles = ['Rectangle element', 'Elliptic element', 'Cross element']

for i, element in enumerate(structuring_elements):
    kernel = cv.getStructuringElement(element, (7,7))
    dilation = cv.dilate(otsu_img, kernel, iterations=7)

    fig = 130 + (i + 1)
    plt.subplot(fig)
    plt.title(titles[i])
    plt.imshow(dilation, cmap='gray')

plt.show()
cv.waitKey(0)