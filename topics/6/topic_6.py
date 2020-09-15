'''
Questão 6
Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada. Apliquem os filtros passa alta de canny (cv_canny), visualizem os resultados e salvem.
Obs: busquem compreender os resultados do filtro.
'''
#library import
import cv2 as cv
#loading the image into the variable img
img = cv.imread('../input_images/image.jpg')
#transforming the image to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
Passa-Baixa: Suaviza a imagem atenuando as altas freqüências, que correspondem às transições abruptas. 
Tende a minimizar ruídos e apresenta o efeito de borramento da imagem. Exemplos de filtros de média 3x3, 5x5 e 7x7.

Passa-Alta: a filtragem passa-alta realça detalhes, produzindo uma "agudização" ("sharpering") da imagem, isto é, 
as transições entre regiões diferentes tornam-se mais nítidas. Estes filtros podem ser usados para realçar certas 
características presentes na imagem, tais como bordas, linhas curvas ou manchas, mas enfatizam o ruído existente na imagem.
'''
#doing high-pass filtering producing sharpering, using the canny filter
#the values 80 and 100 are the thresholds defined for such sharpening
canny_img = cv.Canny(grayscale_img, 80,100)
#show the input image
cv.imshow('Input grayscale image', grayscale_img)
#show the result of the canny filter
cv.imshow('Canny filter', canny_img)
cv.waitKey(0)
#storing the results
cv.imwrite('canny_filter_result.jpg', canny_img)