'''
Questão 2
Abrir uma imagem colorida, transformar em níveis de cinza, visualizar e salvar imagem gerada.
'''
#library import
import cv2
#loading the image into the variable img
img = cv2.imread('../input_images/image.jpg')
#transforming the image to grayscale
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#showing the image in grayscale
cv2.imshow('image in grayscale', grayscale_img)
#waitkey makes the image show until 0 is pressed
cv2.waitKey(0)
#storing the resulting image
cv2.imwrite('result_image.jpg', grayscale_img)

