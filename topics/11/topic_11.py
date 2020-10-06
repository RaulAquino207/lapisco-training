'''
Questão 11
Abrir uma imagem colorida com o fundo branco e um quadrado preto centralizado, transformar em tom de cinza, visualizar imagem de entrada.
Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows),
peguem cada um dos pixels da imagem e coloquem na matriz que criaram. Calculem as coordenadas (xc,yc) que representam o centróide deste quadrado.
Tentem pintar ou marcar ele na imagem para visualização.
Xc será a média todas as coordenadas x que fazem parte do quadrado, e yc é as médias de y do quadrado. As coordenadas do quadrado são identificadas pelo tom preto(valor 0). Façam esta imagem de entrada no Paint.
'''
#library import
import cv2 as cv
import numpy as np
#loading the image into the variable img
img = cv.imread('../input_images/white_black_square.jpg')
#transforming the image to grayscale
grayscale_img_square = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
The shape method can be used without problem because the cv2 library returns numpy.ndarray, and the "shape [: 2]"
is only necessary in an image with 3 color channels (RGB), in the grayscale image just use the shape method
'''
# rows, cols = img.shape[:2]
rows, cols = grayscale_img_square.shape
print(rows, cols)
#creating the static matrix
transformed_image = np.zeros((rows,cols), dtype=np.uint8)
#storing the image in grayscale in the static matrix
for i in range(rows):
    for j in range(cols):
        transformed_image[i, j] = grayscale_img_square[i, j]
#initialize the centroid coordinates
xc = 0
yc = 0
count = 0
#scrolling through the image to find the centroid of the image object, which in this case is a square
for row in range(rows):
    for col in range(cols):
        if transformed_image[row, col] == 0:
            xc += row
            yc += col
            count += 1
#averaging
xc = int(xc/count)
yc = int(yc/count)
print(xc,yc)
#another way to do it is by using the moments method

momentos = cv.moments(transformed_image)
cx = int(momentos['m10'] / momentos['m00'])
cy = int(momentos['m01'] / momentos['m00'])
print('moments', cx, cy)

#cv.circle() method is used to draw a circle on any image.
cv.circle(transformed_image, (xc,yc), 5, (255,255,255), -1)
#showing the input images
cv.imshow('image original', img)
cv.imshow('image in grayscale', grayscale_img_square)
#showing the result
cv.imshow('Centroid', transformed_image)
#waitkey makes the image show until 0 is pressed
cv.waitKey(0)
#storing the results
cv.imwrite('centroid.jpg', transformed_image)