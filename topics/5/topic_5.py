'''
Questão 5
Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada.
Apliquem os filtros passa baixa mediana (cv_median) e media (cv_blur), visualizem os resultados e salvem.
Obs: busquem compreender os resultados de cada filtro.
'''
#library import
import cv2 as cv
#loading the image into the variable img
img = cv.imread('../input_images/image.jpg')
#transforming the image to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#applying the mean and median filters
#ksize aims to define the size of the mask applied
median_img = cv.medianBlur(grayscale_img, ksize=5)
blur_img = cv.blur(grayscale_img, ksize=(5, 5))
#showing the images
cv.imshow('input image', grayscale_img)
cv.imshow('Median', median_img)
cv.imshow('Blur', blur_img)
#waitkey makes the image show until 0 is pressed
cv.waitKey(0)
#storing the results
cv.imwrite('input_img.jpg', grayscale_img)
cv.imwrite('median_filter.jpg', median_img)
cv.imwrite('flur_filter.jpg', blur_img)

