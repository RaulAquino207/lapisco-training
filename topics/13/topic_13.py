'''
Questão 13
Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada.
Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows).
Apliquem uma convolução fazendo uma varredura na matriz utilizando as máscaras do operador gradiente Sobel (procurem no google).
Visualizem os resultados e salvem.
Obs: busquem compreender os resultados do operador Sobel (parece com o de canny, apenas parece).

Operador de Sobel: Realça linhas verticais e horizontais mais escuras que o fundo, sem realçar pontos isolados.
Consiste na aplicação de duas máscaras, descritas a seguir, que compõem um resultado único:

Gx = [[-1,2,-1], [0,0,0], [1,2,1]]
Gy = [[-1,0,1],[-2,0,2],[-1,0,1]]
'''
#library import
import cv2 as cv
import numpy as np
#loading the image into the variable img
img = cv.imread('../input_images/image.jpg')
#transforming the image to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
rows, cols = grayscale_img.shape
sobel_img = np.zeros((rows,cols), dtype=np.uint8)
#apply convolution with the Sobel Kernel
for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        gx = grayscale_img[row - 1, col - 1] * (-1) + grayscale_img[row, col - 1] * (-2) + \
             grayscale_img[row + 1, col - 1] * (-1) + grayscale_img[row - 1, col + 1] + \
             grayscale_img[row, col + 1] * 2 + grayscale_img[row + 1, col + 1]
        print(gx)
        gy = grayscale_img[row - 1, col - 1] * (-1) + grayscale_img[row - 1, col] * (-2) + \
             grayscale_img[row - 1, col + 1] * (-1) + grayscale_img[row + 1, col - 1] + \
             grayscale_img[row + 1, col] * 2 + grayscale_img[row - 1, col + 1]
        print(gy)
        sobel_img[row, col] = (gx ** 2 + gy ** 2) ** (1 / 2)
'''
sobelx = cv.Sobel(grayscale_img, cv.CV_8U, 1, 0, ksize = 3)
sobely = cv.Sobel(grayscale_img, cv.CV_8U, 0, 1, ksize = 3)
cv.imshow("Original", grayscale_img)
cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
'''
#show the result image
cv.imshow('Sobel image', sobel_img)
cv.waitKey(0)
#save the result
cv.imwrite('sobel_result.jpg', sobel_img)

