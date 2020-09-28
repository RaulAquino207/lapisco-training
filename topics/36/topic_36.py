'''
Questão 36
Abrir uma imagem colorida, transformar para tom de cinza e aplique a limiarização de otsu.
Apliquem o método cvDilate de forma iterativa, apresentando o resultado de cada iteração,
verificando o que o método causa. Utilize um elemento estruturante com uma linha e três colunas,
com a referencia no centro, então o objeto deve crescer apenas na vertical, pois o elemento estruturante é vertical.
O objeto deve ser branco e o fundo preto.
'''
import cv2 as cv
import numpy as np
img = cv.imread('../input_images/vase.jpg')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, otsu_img = cv.threshold(grayscale_img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
'''
We manually created a structuring elements in the previous examples with help of Numpy. It is rectangular shape. 
But in some cases, you may need elliptical/circular shaped kernels. 
So for this purpose, OpenCV has a function, cv.getStructuringElement(). 
You just pass the shape and size of the kernel, you get the desired kernel.

# Rectangular Kernel
cv.getStructuringElement(cv.MORPH_RECT,(5,5))

# Elliptical Kernel
cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))

# Cross-shaped Kernel
cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
'''
kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 3))
print(kernel)

for i in range(9):
    dilation = cv.dilate(otsu_img, kernel, iterations=i)
    cv.imshow('Dilated image', dilation)
    cv.waitKey(1000)