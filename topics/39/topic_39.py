'''
Questão 39
Abrir uma imagem colorida, transformar para tom de cinza e aplique a limiarização de otsu.
Apliquem o método cvErode de forma iterativa, apresentando o resultado de cada iteração, verificando o que o método causa.
Utilize um elemento estruturante com uma linha e três colunas, com a referencia no centro, então o objeto deve diminuir
apenas na vertical, pois o elemento estruturante é vertical. O objeto deve ser branco e o fundo preto.
'''

import cv2 as cv
import numpy as np

img = cv.imread('../input_images/vase.jpg')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, otsu_img = cv.threshold(grayscale_img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (1,3))
print(kernel)

for i in range(7):
    erosion = cv.erode(otsu_img, kernel, iterations=i)
    cv.imshow('erosion', erosion)
    cv.waitKey(1000)
