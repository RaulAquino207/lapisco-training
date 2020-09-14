'''
Questão 1
Abrir uma imagem colorida, visualizar e salvar.
'''
#library import
import cv2
#loading the image into the variable img
img = cv2.imread('image.jpg')
#displaying the image
cv2.imshow('image', img)
#waitkey makes the image show until 0 is pressed
cv2.waitKey(0)
#storing the image
cv2.imwrite('result_image.jpg', img)