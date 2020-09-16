'''
Questão 12
Abram um arquivo de texto (pode ser o mesmo gerado no tópico 10), criem uma imagem em tom de cinza e visualizem esta imagem.
'''
#library import
import cv2 as cv
import numpy as np
image = []
with open('../10/result.txt', 'r') as imgfile:
    for i, line in enumerate(imgfile):
        #convert each number of the line to int
        row = [int(number) for number in line.split()]
        #verify if is the first iteration
        if i == 0:
            #create the first line of the image
            image = np.hstack(row)
            print(image)
        else:
            #if it is not the first iteration, then add new lines to compose the image
            image = np.vstack(([image, row]))
#asarray convert the input to an array.
result = np.asarray(image, np.uint8)

#show the read image
cv.imshow('Read image', result)
#waitkey makes the image show until 0 is pressed
cv.waitKey(0)

