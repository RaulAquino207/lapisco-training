'''
Questão 20
Abrir uma imagem colorida, transformar para tom de cinza e aplique a técnica Crescimento de Regiões (Region Growing).
Para isto, inicialmente faça uma imagem com dimensões 320×240 no paint, onde o fundo da imagem seja branco e exista
um círculo preto no centro. Utilize algum ponto dentro do circulo preto como semente, onde você deve determinar este
ponto analisando imagem previamente.
A regra de adesão do método deve ser: “Sempre que um vizinho da região possuir tom de cinza menor que 127, deve-se agregar
este vizinho à região”.
Aplique o Crescimento de Regiões de forma iterativa, em que o algoritmo irá estabilizar apenas quando a região parar de crescer.
'''

import cv2
import numpy as np
from numba import njit
'''
After performing some tests without using the "njit" I realized that it uses a pipeline to carry out the operations faster
'''
@njit
def region_growing(image, seed=None):

    # Get the rows and columns of the image
    rows, cols = image.shape[:2]

    # Get the seed point
    xc, yc = seed
    print(xc,yc)
    # Create a matrix that will contain the segmented region
    segmented = np.zeros_like(image)

    # Mark the seed point in the image
    segmented[xc, yc] = 255

    # Loop through the image until the region stop growing
    current_found = 0
    previous_points = 1
    i = 0
    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                # Verify if we reach the ROI and search through the neighborhood to see if the pixel is of the same
                # object, then if the pixel is part of the object put them in the segmented image
                if segmented[row, col] == 255:
                    if image[row - 1, col - 1] < 127:
                        # print('a')
                        segmented[row - 1, col - 1] = 255
                        current_found += 1
                    if image[row - 1, col] < 127:
                        # print('b')
                        segmented[row - 1, col] = 255
                        current_found += 1
                    if image[row - 1, col + 1] < 127:
                        # print('c')
                        segmented[row - 1, col + 1] = 255
                        current_found += 1
                    if image[row, col - 1] < 127:
                        # print('d')
                        segmented[row, col - 1] = 255
                        current_found += 1
                    if image[row, col + 1] < 127:
                        # print('e')
                        segmented[row, col + 1] = 255
                        current_found += 1
                    if image[row + 1, col - 1] < 127:
                        # print('f')
                        segmented[row + 1, col - 1] = 255
                        current_found += 1
                    if image[row + 1, col] < 127:
                        # print('g')
                        segmented[row + 1, col] = 255
                        current_found += 1
                    if image[row + 1, col + 1] < 127:
                        # print('h')
                        segmented[row + 1, col + 1] = 255
                        current_found += 1
    #         i += 1
    #         cv2.imwrite(f"frame_{i + 1}.jpg", segmented)
    # print('executando')
    i += 1
    return segmented


if __name__ == '__main__':
    # Read a rgb image
    image = cv2.imread('../input_images/black_circle.jpg')

    # Transform to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the region growing algorithm
    segmented_image = region_growing(grayscale_image,
                                     seed=(int(grayscale_image.shape[0]/2), int(grayscale_image.shape[1]/2)))

    # Show the result
    cv2.imshow('Segmented image', segmented_image)
    cv2.waitKey(0)

