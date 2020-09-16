'''
Questão 10
Abrir uma imagem colorida, transformar em tom de cinza, visualizar imagem de entrada.
Criem uma matriz de forma estática com as mesmas dimensões da imagem de entrada (vejam nas propriedades da imagem no Windows),
peguem cada um dos pixels da imagem e coloquem na matriz que criaram.
Apliquem uma limiarização fazendo uma varredura na matriz.
Imprimam esta matriz em um arquivo de texto (*.txt) do mesmo modo que ela está alocada.
'''
import cv2 as cv
import numpy as np
img = cv.imread('../input_images/image.jpg')
grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
rows, cols = grayscale_img.shape
print(rows,cols)
threshold_matrix = np.zeros((rows, cols), dtype=np.uint8)
for i in range(rows):
    for j in range(cols):
        threshold_matrix[i, j] = grayscale_img[i, j]

def thresholding_def(archive, limiar, max_value):
    with open('result.txt', 'w') as outfile:
        for row in range(rows):
            for col in range(cols):
                # Define the limits of the threshold
                if archive[row, col] < limiar:
                    archive[row, col] = 0
                else:
                    archive[row, col] = max_value

                outfile.write(str(archive[row, col]) + ' ')
            outfile.write('\n')

thresholding_def(threshold_matrix, 127, 255)