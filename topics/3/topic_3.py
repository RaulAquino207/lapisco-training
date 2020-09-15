'''
Questão 3
Abrir uma imagem colorida em RGB, visualizar e salvar cada um dos canais separadamente.
Obs: Busquem compreender o que significa cada um dos canais.
'''
#library import
import cv2
#loading the image into the variable img
img = cv2.imread('../input_images/image.jpg')
#the cv2 split function returns the 3 channels separately
blue_channel, green_channel, red_channel = cv2.split(img)
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)
#waitkey makes the image show until 0 is pressed
cv2.waitKey(0)
#storing the results
cv2.imwrite('blue_channel.jpg', blue_channel)
cv2.imwrite('green_channel.jpg', green_channel)
cv2.imwrite('red_channel.jpg', red_channel)