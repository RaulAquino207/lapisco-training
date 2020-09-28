'''
Questão 39
Abrir uma imagem colorida, transformar para tom de cinza e aplique a limiarização de otsu.
Apliquem o método cvErode de forma iterativa, apresentando o resultado de cada iteração, verificando o que o método causa.
Utilize um elemento estruturante com uma linha e três colunas, com a referencia no centro, então o objeto deve diminuir
apenas na vertical, pois o elemento estruturante é vertical. O objeto deve ser branco e o fundo preto.
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

structuring_elements = [cv.MORPH_RECT, cv.MORPH_ELLIPSE, cv.MORPH_CROSS]

plt.figure(1)
titles = ['Rectangle element', 'Elliptic element', 'Cross element']
for i, element in enumerate(structuring_elements):
    kernel = cv.getStructuringElement(element, (7,7))
    erosion = cv.erode(otsu_img, kernel, iterations=7)

    fig = 130 + (i+1)
    plt.subplot(fig)
    plt.title(titles[i])
    plt.imshow(erosion, cmap='gray')

plt.show()
cv.waitKey(0)