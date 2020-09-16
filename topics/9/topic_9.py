'''
Questão 9
Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada.
Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows),
peguem cada um dos pixels da imagem e coloquem na matriz que criaram.
Imprimam esta matriz em um arquivo de texto (*.txt) do mesmo modo que ela está alocada.
'''
#library import
import cv2 as cv
#loading the image into the variable img
img = cv.imread('../input_images/image.jpg')
#transforming the image to grayscale
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
'''
The shape method can be used without problem because the cv2 library returns numpy.ndarray, and the "shape [: 2]"
is only necessary in an image with 3 color channels (RGB), in the grayscale image just use the shape method
'''
# rows, cols = img.shape[:2]
rows, cols = grayscale_img.shape
#showing the image size
print(rows,cols)
#show the input image
cv.imshow('Input grayscale image', grayscale_img)
cv.waitKey(0)
#saving the content of the image in the .txt file, using the with function which will do the close function when the block is closed
#Save all pixels in a txt file
with open('result.txt', 'w') as outfile:
    for i in range(rows):
        for j in range(cols):
            outfile.write(str(grayscale_img[i, j]) + ' ')
        outfile.write('\n')