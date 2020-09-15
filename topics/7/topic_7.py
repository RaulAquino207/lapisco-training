'''
Questão 7
Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Apliquem uma limiarização (thresholding), visualizem os resultados e salvem.
Obs: busquem compreender os resultados da técnica.
'''
#library import
import cv2 as cv
#loading the image into the variable img
img = cv.imread('../input_images/image.jpg')
#transforming the image to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#Once the image has been thresholded, the threshold and image are returned
ret, threshold_img = cv.threshold(grayscale_img, 50, 255, cv.THRESH_BINARY)
print(ret)
#show the input image
cv.imshow('Input grayscale image', grayscale_img)
#showing the image
cv.imshow('thresholding', threshold_img)
#waitkey makes the image show until 0 is pressed
cv.waitKey(0)
#storing the results
cv.imwrite('threshold_result.jpg', threshold_img)
