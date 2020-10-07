'''
As questão 30-34 serão sobre o uso da função "cv.FindContours"

Questão 30
Abrir uma imagem colorida, transformar para tom de cinza e aplique a transformada de canny para detectar bordas.
Apliquem o método cvFindContours para determinar quantos contornos existem na imagem.
Apresentem o resultado obtido e a imagem de entrada. O retorno deve ser a mesma quantidade de objetos existentes.
'''

import cv2 as cv
import numpy as np
img = cv.imread('../input_images/objects_canny.png')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny_img = cv.Canny(grayscale_img, 80, 255)

# Find how many contours are in the image
contours, hierarchy = cv.findContours(canny_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Create a copy of the image to draw the contours
contour_img = np.copy(img)

# Draw all the contours found
cv.drawContours(contour_img, contours, -1, (0, 0, 255), 3)

# Show the input image
cv.imshow('Input grayscale image', grayscale_img)
cv.imshow('Canny', canny_img)
# Show the contours found
cv.imshow('Contours', contour_img)
cv.waitKey(0)