'''
As questões 35-40 são sobre o uso das funções "cvDilate" e "cvErode", e devem ser feitas em sequência.

Questão 35
Abrir uma imagem colorida, transformar para tom de cinza e aplique a limiarização de otsu.
Apliquem o método cvDilate de forma iterativa, apresentando o resultado de cada iteração, verificando
o que o método causa. O resultado deve ser aumentar as regiões brancas, então se o objeto for branco este
método aumentará o objeto.
'''
import cv2 as cv
import numpy as np
img = cv.imread('../input_images/vase.jpg')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, otsu_img = cv.threshold(grayscale_img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
kernel = np.ones((5, 5), np.uint8)
for i in range(7):
    dilation = cv.dilate(otsu_img, kernel, iterations = i)
    cv.imshow('Dilated image', dilation)
    cv.waitKey(1000)