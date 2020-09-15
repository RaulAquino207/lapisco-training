'''
Questão 4
Abrir uma imagem colorida, transformar em HSV, visualizar e salvar cada um dos canais separadamente.
Obs: Busquem compreender o que significa cada um dos canais.

HSV é a abreviatura para o sistema de cores formadas pelas componentes
hue (matiz), saturation (saturação) e value (valor).
'''
#library import
import cv2 as cv
#loading the image into the variable img
img = cv.imread('../input_images/image.jpg')
#converting the RGB image to an HSV image (COLOR_BGR2HSV)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#the cv2 split function returns the 3 channels separately
h,s,v = cv.split(img)
#showing the images
cv.imshow('HSV', hsv_img)
cv.imshow('H',h)
cv.imshow('S',s)
cv.imshow('V',v)
#waitkey makes the image show until 0 is pressed
cv.waitKey(0)
#storing the results
cv.imwrite('hsv_img.jpg', hsv_img)
cv.imwrite('h_channel.jpg', h)
cv.imwrite('s_channel.jpg', s)
cv.imwrite('v_channel.jpg', v)
